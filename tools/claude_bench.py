#!/usr/bin/env python3
"""Claude Code as its own harness - no forge.

The falsification test for forge's gates. forge's own claude backend runs
`claude -p` WITHOUT Bash ("an unattended agent with a shell is a bigger
blast radius than an item needs"), so the agent cannot run the tests and
forge's validation loop is what catches a wrong answer. That makes forge's
measured contribution partly an artifact of tying the agent's hands.

This runner gives the agent the shell, lets it run the tests itself, and
removes forge entirely: no worktree, no scope enforcement, no validation
loop, no park. Just the agent, the repo, and the hidden grader at the end.

Outcomes (same taxonomy as tools/aider_bench.py):
  pass         - the hidden grader passes
  silent_wrong - the CLI exited cleanly (it thinks it succeeded) but the
                 grader fails. The number that matters: an agent marking
                 its own homework and getting it wrong.
  parked       - the CLI itself failed (nonzero exit) and the grader fails.

CAVEAT for the polyglot bench: each imported task's hidden grader re-runs
the exercise's own visible test file, so an agent with a shell effectively
sees the answer key. A high score here says little about silent-wrong risk;
Leash's own bench (hidden graders plus mutants) is where that is testable.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from leash import env, fixtures, grading, tasks  # noqa: E402

SCHEMA = 2
TIMEOUT = 1800
# Bash included on purpose - that is the whole point of this comparison.
TOOLS = "Read,Edit,Write,Glob,Grep,Bash"


def prompt_for(task: tasks.Task, test_cmd: str) -> str:
    """Deliberately close to forge's own claude-backend prompt, with two
    differences that are the experiment: the shell is allowed and the agent
    is told to verify with it.

    What it does NOT say is "do not edit the test file". On a TDD item,
    writing the test IS the task, and that instruction would make those two
    items impossible - they are also the items most worth watching here,
    since an agent that writes its own test and then judges itself against
    it is marking its own homework. The task text governs instead.

    It also gives no file-scope hint. forge derives the allowed file set in
    Python and reverts anything outside it; a standalone agent has no such
    thing, and pretending otherwise would flatter this arm.
    """
    return (
        f"Implement this task in the current repository.\n\nTask:\n{task.text}\n\n"
        f"You have a shell. You can verify your work by running:\n    {test_cmd}\n\n"
        "Follow the task exactly. Make the edits directly, do not commit, and do "
        "not create files the task doesn't call for. When done, reply with one "
        "line summarising the change."
    )


def test_command(bench: Path, task: tasks.Task) -> str:
    conf = task.fixture_dir(bench) / ".aiderloop.toml"
    if conf.is_file():
        import tomllib
        cmds = tomllib.loads(conf.read_text()).get("validate", {}).get("commands") or []
        if cmds:
            return " && ".join(cmds)
    return "python -m unittest discover -s tests -q"


def final_message(stdout: str) -> dict:
    """The agent's own closing summary, from the CLI's JSON result.

    Kept as its own field because it is the evidence for whether a
    silent_wrong was disclosed or not, and log_tail cannot be trusted to
    hold it: the CLI can repeat warnings after the result until the tail
    is all warnings.
    """
    for line in [stdout] + list(reversed(stdout.strip().splitlines())):
        try:
            r = json.loads(line)
        except ValueError:
            continue
        if isinstance(r, dict) and r.get("type") == "result":
            return {"result": r.get("result"), "is_error": r.get("is_error"),
                    "num_turns": r.get("num_turns"), "subtype": r.get("subtype")}
    return {}


def run_trial(task: tasks.Task, trial: int, bench: Path, model: str, model_info: dict,
              work_root: Path) -> dict:
    project = fixtures.materialize(task, bench, work_root,
                                   name=f"claude-bench-{task.id}-t{trial}-{time.time_ns()}")
    cmd = ["claude", "-p", "--output-format", "json", "--permission-mode", "acceptEdits",
           "--allowedTools", TOOLS, "--model", model]
    row: dict = {"schema": SCHEMA, "harness": {"adapter": "claude-native-with-shell"},
                 "task_id": task.id, "category": task.category, "trial": trial,
                 "model": {**model_info, "label": model}, "started": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    try:
        started = time.monotonic()
        try:
            p = subprocess.run(cmd, input=prompt_for(task, test_command(bench, task)),
                               cwd=project, capture_output=True, text=True, timeout=TIMEOUT)
            rc, out = p.returncode, (p.stdout or "") + (p.stderr or "")
            row["agent"] = final_message(p.stdout or "")
        except subprocess.TimeoutExpired as e:
            rc, out = -1, ((e.stdout or "") if isinstance(e.stdout, str) else "") + "\n[timeout]\n"
        secs = time.monotonic() - started
        ok, detail = grading.grade(project, task.grader)
        row["stage1"] = {"exit_code": rc, "seconds": round(secs, 1), "log_tail": out[-3000:]}
        row["outcome"] = "pass" if ok else ("silent_wrong" if rc == 0 else "parked")
        row["grader_tail"] = (detail or "")[-1500:]
        row["status"] = "ok"
    except Exception as e:  # noqa: BLE001
        row["status"] = "error"; row["error"] = f"{type(e).__name__}: {e}"
        row["outcome"] = "error"
    finally:
        row["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        shutil.rmtree(project, ignore_errors=True)
    return row


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="claude-sonnet-4-20250514",
                    help="label the CLI requires; a local server ignores it")
    ap.add_argument("--trials", type=int, default=5)
    ap.add_argument("--tasks", default=None)
    ap.add_argument("--bench", default=None, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--work-root", default=Path("/tmp"), type=Path)
    a = ap.parse_args()
    # What actually answers: the --model value is only a label the CLI
    # requires, and a local server behind ANTHROPIC_BASE_URL ignores it.
    # Raises if the server is down or not loaded, before any trial runs.
    model_info = env.anthropic_endpoint_model_info(a.model)
    print(f"doer: {model_info['name']} ({model_info['provider']})")

    bench = a.bench or tasks.default_bench()
    task_list = tasks.load_tasks(bench, a.tasks.split(",") if a.tasks else None, None)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    done = set()
    if a.out.exists():
        for line in a.out.read_text().splitlines():
            if line.strip():
                r = json.loads(line)
                if r.get("status") == "ok":
                    done.add((r["task_id"], r["trial"]))
    plan = [(t, i) for i in range(1, a.trials + 1) for t in task_list if (t.id, i) not in done]
    print(f"claude-native (with shell): {len(plan)}/{len(task_list)*a.trials} trial(s) to run")
    with a.out.open("a", encoding="utf-8") as f:
        for i, (task, trial) in enumerate(plan, 1):
            row = run_trial(task, trial, bench, a.model, model_info, a.work_root)
            f.write(json.dumps(row, sort_keys=True) + "\n"); f.flush()
            print(f"[{i}/{len(plan)}] {task.id} #{trial}: {row.get('outcome')} "
                  f"({row.get('stage1', {}).get('seconds', '?')}s)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
