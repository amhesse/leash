#!/usr/bin/env python3
"""Aider-native benchmark runner.

Drives the real `aider` CLI directly against Leash's task fixtures, using
aider's OWN mechanisms (its own --auto-test retry loop, its own
conventions) - never through forge's runner.py or leash's `--backend
aider`, which would run aider inside forge's orchestration instead of at
aider's own fullest capability. See docs/09-forge-vs-aider-benchmark.md
for the full design rationale; this file is Phase 1 of that plan.

Reuses Leash's existing task-loading/fixture/grading code as a library
(never reimplemented), so a trial here is graded by the exact same hidden
grader + visible tests as every other Leash result in this project.

Outcome taxonomy (aider has no native "park" concept, so this infers the
equivalent from its actual behavior - see docs/09-forge-vs-aider-benchmark.md
for why):
  pass         - final state passes the task's checks.
  silent_wrong - aider exited cleanly (thinks it succeeded) but checks fail.
  parked       - aider itself errored / gave up (nonzero exit, or its own
                 auto-test reflections were exhausted) without a passing
                 state - the aider-native equivalent of an honest park.

Local+cloud design: Stage 1 runs aider with a local ollama model against
the fixture's own real validate command (matching forge's own retry-loop
target exactly, not the hidden grader - the hidden grader is never shown
to either tool, only used for final scoring, exactly as forge does it).
If Stage 1's final state still fails the hidden grade, and an escalation
model was given, Stage 2 re-invokes aider on the SAME worktree pointed at
the cloud model - the aider-native analog of forge's --repair-from, built
by just running aider again.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

_LEASH_SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(_LEASH_SRC))

from leash import fixtures, grading, tasks  # noqa: E402

SCHEMA = 1
AIDER_TIMEOUT = 1800  # 30 min hard ceiling per aider invocation, same as forge's own

# Same regex forge/src/forge/runner.py uses to parse aider's own self-reported
# "Tokens: N sent, M received" lines - copied rather than imported, since
# forge lives in its own pipx venv and this script must stay independently
# runnable. Aider is a subprocess whose API traffic this script never sees
# directly, so its own stdout summary is the only token source available.
_AIDER_TOKENS_RE = re.compile(
    r"Tokens:\s*([\d.]+)(k?)\s*sent,\s*([\d.]+)(k?)\s*received", re.IGNORECASE)


def parse_aider_tokens(output: str) -> dict:
    prompt = completion = 0.0
    for sent, sent_k, recv, recv_k in _AIDER_TOKENS_RE.findall(output):
        prompt += float(sent) * (1000 if sent_k else 1)
        completion += float(recv) * (1000 if recv_k else 1)
    return {"prompt_tokens": int(prompt), "completion_tokens": int(completion)}


def validate_command(bench: Path, task: tasks.Task) -> str:
    """The fixture's own real validate command - same one forge's retry
    loop targets, read from the fixture's .aiderloop.toml. Never the hidden
    grader, which stays hidden from both tools until final scoring."""
    conf = task.fixture_dir(bench) / ".aiderloop.toml"
    if conf.is_file():
        import tomllib
        cfg = tomllib.loads(conf.read_text())
        commands = cfg.get("validate", {}).get("commands") or []
        if commands:
            return " && ".join(commands)
    return "python -m unittest discover -s tests -q"


def run_aider(project: Path, prompt: str, test_cmd: str, model: str) -> tuple[int, str]:
    cmd = [
        "aider",
        "--yes-always", "--no-gitignore", "--no-stream",
        "--no-restore-chat-history",
        "--edit-format", "diff",
        "--auto-test", "--test-cmd", test_cmd,
        "--model", model,
        "--message", prompt,
    ]
    try:
        proc = subprocess.run(cmd, cwd=project, capture_output=True, text=True,
                              timeout=AIDER_TIMEOUT)
        return proc.returncode, (proc.stdout or "") + (proc.stderr or "")
    except subprocess.TimeoutExpired as e:
        out = (e.stdout or "") + (e.stderr or "")
        return -1, out + "\n[aider_bench] killed after AIDER_TIMEOUT\n"


def task_prompt(task: tasks.Task) -> str:
    return (
        f"Complete this task:\n\n{task.text}\n\n"
        "Implement the change directly. Do not ask clarifying questions - "
        "make reasonable assumptions and note them in a comment if needed."
    )


def repair_prompt(task: tasks.Task, failure_output: str) -> str:
    return (
        f"The following task is not yet correctly implemented:\n\n{task.text}\n\n"
        "The current state fails validation with this output:\n\n"
        f"{failure_output[-4000:]}\n\n"
        "Fix it so the validation passes. Do not abandon the task."
    )


def run_trial(task: tasks.Task, trial: int, bench: Path, local_model: str,
              cloud_model: str | None, work_root: Path) -> dict:
    project = fixtures.materialize(task, bench, work_root,
                                   name=f"aider-bench-{task.id}-t{trial}-{time.time_ns()}")
    test_cmd = validate_command(bench, task)
    row: dict = {
        "schema": SCHEMA, "harness": {"adapter": "aider-native"},
        "task_id": task.id, "category": task.category, "trial": trial,
        "model": {"local": local_model, "cloud": cloud_model},
        "started": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
    }
    try:
        started = time.monotonic()
        rc1, out1 = run_aider(project, task_prompt(task), test_cmd, f"ollama/{local_model}")
        stage1_seconds = time.monotonic() - started
        ok1, detail1 = grading.grade(project, task.grader)
        local_tokens = parse_aider_tokens(out1)
        row["stage1"] = {
            "exit_code": rc1, "seconds": round(stage1_seconds, 1),
            "tokens": local_tokens, "log_tail": out1[-4000:],
        }
        if ok1:
            row["outcome"] = "pass"
        elif rc1 == 0:
            row["outcome"] = "silent_wrong"
        else:
            row["outcome"] = "parked"
        row["local_tokens"] = local_tokens
        row["cloud_tokens"] = {"prompt_tokens": 0, "completion_tokens": 0}

        # Escalation mirrors leash's own rule: never touch silent_wrong,
        # only ever repair an honest park.
        if cloud_model and row["outcome"] == "parked":
            started2 = time.monotonic()
            rc2, out2 = run_aider(project, repair_prompt(task, detail1), test_cmd, cloud_model)
            stage2_seconds = time.monotonic() - started2
            ok2, detail2 = grading.grade(project, task.grader)
            cloud_tokens = parse_aider_tokens(out2)
            row["stage2"] = {
                "exit_code": rc2, "seconds": round(stage2_seconds, 1),
                "tokens": cloud_tokens, "log_tail": out2[-4000:],
            }
            row["cloud_tokens"] = cloud_tokens
            if ok2:
                row["escalated_outcome"] = "pass"
            elif rc2 == 0:
                row["escalated_outcome"] = "silent_wrong"
            else:
                row["escalated_outcome"] = "parked"
        else:
            row["escalated_outcome"] = row["outcome"]

        row["status"] = "ok"
    except Exception as e:  # noqa: BLE001 - a bad trial must not kill the batch
        row["status"] = "error"
        row["error"] = f"{type(e).__name__}: {e}"
        row["outcome"] = row.get("outcome", "error")
        row["escalated_outcome"] = row.get("escalated_outcome", "error")
    finally:
        row["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        shutil.rmtree(project, ignore_errors=True)
    return row


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="Local ollama model, e.g. qwen3.8:27b")
    ap.add_argument("--escalate-model", default=None,
                    help="Cloud/aider model string for Stage 2, e.g. claude-sonnet-5. "
                         "Omit for local-only.")
    ap.add_argument("--trials", type=int, default=15)
    ap.add_argument("--tasks", default=None, help="Comma-separated task ids")
    ap.add_argument("--categories", default=None, help="Comma-separated categories")
    ap.add_argument("--bench", default=None, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--work-root", default=Path("/tmp"), type=Path)
    args = ap.parse_args()

    bench = args.bench or tasks.default_bench()
    task_ids = args.tasks.split(",") if args.tasks else None
    categories = args.categories.split(",") if args.categories else None
    task_list = tasks.load_tasks(bench, task_ids, categories)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    done_keys = set()
    if args.out.exists():
        for line in args.out.read_text().splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            if r.get("status") == "ok":
                done_keys.add((r["task_id"], r["trial"]))

    plan = [(t, trial) for trial in range(1, args.trials + 1) for t in task_list
            if (t.id, trial) not in done_keys]
    total = len(task_list) * args.trials
    print(f"aider-native: {args.model} + escalate={args.escalate_model or 'none'} "
          f"({len(plan)}/{total} trial(s) to run)")

    with args.out.open("a", encoding="utf-8") as f:
        for i, (task, trial) in enumerate(plan, 1):
            row = run_trial(task, trial, bench, args.model, args.escalate_model, args.work_root)
            f.write(json.dumps(row, sort_keys=True) + "\n")
            f.flush()
            esc = f" escalated={row.get('escalated_outcome')}" if args.escalate_model else ""
            print(f"[{i}/{len(plan)}] {task.id} #{trial}: outcome={row.get('outcome')}{esc} "
                  f"({row.get('stage1', {}).get('seconds', '?')}s)", flush=True)

    print(f"done: {len(plan)} trial(s) written to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
