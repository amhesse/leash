"""One trial, three conditions.

    model attempt ─► pinned first attempt ─► grade ─────────────► UNCHECKED
         │
         ▼
    forge's checks + retries ─► merged? grade : grade parked ────► CHECKED
         │ (parked)
         ▼
    cloud model repairs the parked branch ─► checks ─► grade ────► ESCALATED

All three are measured on the same attempt, so the differences between
them (harness lift, escalation lift) are paired comparisons rather than
three independent samples.

Rules worth knowing:
- UNCHECKED grades forge's first-attempt snapshot. With no snapshot (the
  editor never produced a usable attempt) it grades whatever the branch
  holds, usually the untouched base - an unwatched system would have
  "merged" nothing, which is wrong and unnoticed: silent_wrong.
- ESCALATED equals CHECKED when the local model already merged. When an
  escalation is skipped (budget, quota) or fails for infrastructure
  reasons, ESCALATED also falls back to CHECKED - the conservative choice;
  dropping those trials would drop only parked ones and inflate the score.
  Such trials are flagged, and a skipped one keeps a git bundle so
  `leash run --fill-escalations` can complete it later.
"""

from __future__ import annotations

import dataclasses
import datetime
import shutil
import tempfile
from pathlib import Path

from . import fixtures, grading, outcomes
from .adapters.forge import ForgeAdapter, StageResult, cache_dir
from .fixtures import git
from .tasks import Task

REPAIR_FIELDS = ("validation_output", "review_feedback", "red_phase_gate_output")


@dataclasses.dataclass
class EscalationPolicy:
    engine: str | None = None          # forge backend: "agy" or "claude"; None = disabled
    model: str | None = None           # e.g. "gemini-3.8-flash-high"; None = the CLI's default
    allowed: bool = True               # False once the budget is spent or quota hit
    skip_reason: str | None = None
    artifact_dir: Path | None = None   # where skipped escalations keep a bundle
    name: str | None = None            # what the user asked for, e.g. "gemini:gemini-3.8-flash-high"

    @property
    def enabled(self) -> bool:
        return self.engine is not None

    @property
    def label(self) -> str | None:
        if not self.enabled:
            return None
        return self.name or (f"{self.engine}:{self.model}" if self.model else self.engine)


def now() -> str:
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def repair_note(record: dict) -> str:
    """Why forge parked the attempt - what the cloud model is told to fix."""
    parts = [f"Status: {record.get('status', '?')}", f"Reason: {record.get('reason', 'unknown')}"]
    if record.get("touched_files"):
        parts.append(f"Files the attempt touched: {', '.join(record['touched_files'])}")
    for field in REPAIR_FIELDS:
        if record.get(field):
            parts.append(f"{field.replace('_', ' ').capitalize()}:\n{record[field][-3000:]}")
    return "\n\n".join(parts)


def _rev(repo: Path, rev: str) -> str | None:
    r = git(repo, "rev-parse", "--verify", "--quiet", f"{rev}^{{commit}}", check=False)
    return r.stdout.strip() if r.returncode == 0 else None


def _condition(outcome: str, detail: str) -> dict:
    return {"outcome": outcome, "grader_output": detail}


def _grade_after_stage(project: Path, task: Task, stage: StageResult, base: str) -> tuple[str, str]:
    """Checked-style outcome of a stage: grade the merged checkout, or the
    parked branch (or the base, when nothing was committed)."""
    if stage.merged:
        ok, detail = grading.grade(project, task.grader)
        return outcomes.merged_outcome(ok), detail
    branch = (stage.record or {}).get("branch")
    target = _rev(project, branch) if branch else None
    ok, detail = grading.grade_commit(project, target or base, task.grader)
    return outcomes.parked_outcome(ok), detail


def run_local_stage(task: Task, project: Path, base: str, adapter: ForgeAdapter, model: str,
                    backend: str, timeout: float) -> tuple[dict, StageResult]:
    stage = adapter.run(project, backend=backend, model=model,
                        extra=["--snapshot-first-attempt"], timeout=timeout)
    rec = stage.record or {}
    error = outcomes.classify_stage_error(stage.log, stage.returncode, stage.timed_out,
                                          stage.record, "local")
    local = {
        "seconds": stage.seconds,
        "tokens": stage.tokens,
        "marker": stage.marker,
        "status": rec.get("status"),
        "reason": rec.get("reason"),
        "branch": rec.get("branch"),
        "first_attempt_commit": rec.get("first_attempt_commit"),
        "forge_expected_files": rec.get("expected_files"),
        "touched_files": rec.get("touched_files"),
        "validation_retries": rec.get("validation_retries"),
        "validation_retry_budget": rec.get("validation_retry_budget"),
        # forge distinguishes "the editor produced nothing this harness could
        # parse" from "the editor errored": the first says nothing about
        # whether the model was right or careful, so it must not be summarised
        # as the item being honestly parked.
        "editor_failure": rec.get("editor_failure"),
        # How often an attempt was truncated before emitting a file, and how
        # often forge retried with thinking disabled because of it. Carried
        # explicitly because log_tail is bounded and drops the evidence.
        "truncated_attempts": rec.get("truncated_attempts"),
        "adaptive_think_off_retries": rec.get("adaptive_think_off_retries"),
        "editor_attempts": rec.get("aider_attempts"),
        "error": error,
        "log_tail": stage.log_tail if (error or not stage.merged) else "",
    }
    return local, stage


def grade_local(task: Task, project: Path, base: str, stage: StageResult) -> dict:
    rec = stage.record or {}
    snapshot = rec.get("first_attempt_commit")
    branch = rec.get("branch")
    tip = _rev(project, branch) if branch else None
    if snapshot:
        source, rev = "snapshot", snapshot
    elif tip and tip != base:
        source, rev = "branch_tip", tip
    else:
        source, rev = "base", base
    ok, detail = grading.grade_commit(project, rev, task.grader)
    unchecked = _condition(outcomes.merged_outcome(ok), detail)
    unchecked["source"] = source
    checked = _condition(*_grade_after_stage(project, task, stage, base))
    return {outcomes.UNCHECKED: unchecked, outcomes.CHECKED: checked}


def run_escalation(task: Task, project: Path, base: str, parked_branch: str, note: str,
                   adapter: ForgeAdapter, policy: EscalationPolicy, timeout: float) -> dict:
    """Repairs a parked branch with the cloud model. Returns the escalation
    record, including the ESCALATED condition when it produced one."""
    fixtures.reopen_checklist_item(project, task)
    with tempfile.NamedTemporaryFile("w", suffix=".txt", prefix="leash-repair-", delete=False) as f:
        f.write(note)
        note_path = Path(f.name)
    try:
        stage = adapter.run(project, backend=policy.engine, model=policy.model,
                            extra=["--repair-from", parked_branch, "--repair-note", str(note_path)],
                            timeout=timeout)
    finally:
        note_path.unlink(missing_ok=True)
    rec = stage.record or {}
    error = outcomes.classify_stage_error(stage.log, stage.returncode, stage.timed_out,
                                          stage.record, "cloud")
    escalation = {
        "status": "error" if error else "done",
        "model": policy.label,
        "seconds": stage.seconds,
        "tokens": stage.tokens,
        "marker": stage.marker,
        "reason": rec.get("reason"),
        "error": error,
        "log_tail": stage.log_tail,
    }
    if not error:
        outcome, detail = _grade_after_stage(project, task, stage, base)
        escalation["condition"] = _condition(outcome, detail)
        escalation["resolved_by"] = "cloud" if outcome == outcomes.PASS else (
            "cloud_wrong" if outcome == outcomes.SILENT_WRONG else "none")
    return escalation


def save_bundle(project: Path, path: Path) -> str | None:
    path.parent.mkdir(parents=True, exist_ok=True)
    r = git(project, "bundle", "create", str(path), "--all", check=False)
    return str(path) if r.returncode == 0 else None


def restore_bundle(bundle: Path, parent: Path, name: str) -> Path:
    project = parent / name
    project.mkdir(parents=True)
    git(project, "init", "-q", "-b", "master")
    # --update-head-ok: the fresh repo's unborn HEAD already points at master.
    git(project, "fetch", "-q", "--update-head-ok", str(bundle), "+refs/heads/*:refs/heads/*")
    git(project, "checkout", "-q", "-f", "master")
    return project


def run_trial(task: Task, trial: int, *, bench: Path, adapter: ForgeAdapter, model: str,
              backend: str, policy: EscalationPolicy, stage_timeout: float,
              artifact_key: str | None = None) -> dict:
    """Runs one trial end to end and returns its result row fragment
    (the caller adds run-level metadata)."""
    row: dict = {
        "task_id": task.id,
        "category": task.category,
        "task_hash": task.content_hash(bench),
        "signals": task.signals(),
        "trial": trial,
        "started": now(),
        "errors": [],
    }
    tmp = Path(tempfile.mkdtemp(prefix="leash-trial-"))
    project = tmp / fixtures.unique_name(task)
    try:
        fixtures.materialize(task, bench, tmp, name=project.name)
        base = git(project, "rev-parse", "HEAD").stdout.strip()
        local, stage = run_local_stage(task, project, base, adapter, model, backend, stage_timeout)
        row["local"] = local
        if local["error"]:
            row["errors"].append({"stage": "local", "kind": local["error"]})
            row["status"] = "error"
            return row

        conditions = grade_local(task, project, base, stage)
        checked = conditions[outcomes.CHECKED]
        escalation: dict = {"status": "disabled"} if not policy.enabled else {}

        if policy.enabled:
            if checked["outcome"] in outcomes.MERGED_OUTCOMES:
                escalation = {"status": "not_needed"}
                conditions[outcomes.ESCALATED] = dict(checked, resolved_by="local")
            elif not policy.allowed:
                note = repair_note(stage.record or {})
                escalation = {"status": "skipped", "reason": policy.skip_reason, "repair_note": note,
                              "parked_branch": local["branch"]}
                if policy.artifact_dir and artifact_key and local["branch"]:
                    escalation["bundle"] = save_bundle(project, policy.artifact_dir / f"{artifact_key}.bundle")
                conditions[outcomes.ESCALATED] = dict(checked, resolved_by="none", fallback="skipped")
            elif not local["branch"]:
                escalation = {"status": "skipped", "reason": "no parked branch to repair"}
                conditions[outcomes.ESCALATED] = dict(checked, resolved_by="none", fallback="skipped")
            else:
                note = repair_note(stage.record or {})
                escalation = run_escalation(task, project, base, local["branch"], note, adapter,
                                            policy, stage_timeout)
                escalation["repair_note"] = note
                if escalation["status"] == "done":
                    conditions[outcomes.ESCALATED] = escalation.pop("condition")
                    conditions[outcomes.ESCALATED]["resolved_by"] = escalation["resolved_by"]
                else:
                    row["errors"].append({"stage": "cloud", "kind": escalation["error"]})
                    conditions[outcomes.ESCALATED] = dict(checked, resolved_by="none", fallback="error")

        row["conditions"] = conditions
        row["escalation"] = escalation
        row["status"] = "ok"
        return row
    finally:
        row["finished"] = now()
        shutil.rmtree(cache_dir(project), ignore_errors=True)
        shutil.rmtree(tmp, ignore_errors=True)


def fill_escalation(row: dict, task: Task, *, bench: Path, adapter: ForgeAdapter,
                    policy: EscalationPolicy, stage_timeout: float) -> dict:
    """Completes a previously skipped escalation from its saved bundle.
    Returns the updated row (unchanged if it can't be completed)."""
    esc = row.get("escalation") or {}
    bundle = esc.get("bundle")
    if esc.get("status") != "skipped" or not bundle or not Path(bundle).is_file():
        return row
    tmp = Path(tempfile.mkdtemp(prefix="leash-fill-"))
    project = tmp / fixtures.unique_name(task)
    try:
        restore_bundle(Path(bundle), tmp, project.name)
        base = git(project, "rev-list", "--max-parents=0", "master").stdout.split()[0]
        result = run_escalation(task, project, base, esc["parked_branch"], esc["repair_note"],
                                adapter, policy, stage_timeout)
        if result["status"] != "done":
            row = dict(row, errors=row.get("errors", []) + [{"stage": "cloud", "kind": result["error"]}])
            return row
        condition = result.pop("condition")
        condition["resolved_by"] = result["resolved_by"]
        result["repair_note"] = esc["repair_note"]
        result["filled"] = now()
        new = dict(row)
        new["conditions"] = dict(row["conditions"], **{outcomes.ESCALATED: condition})
        new["escalation"] = result
        return new
    finally:
        shutil.rmtree(cache_dir(project), ignore_errors=True)
        shutil.rmtree(tmp, ignore_errors=True)
