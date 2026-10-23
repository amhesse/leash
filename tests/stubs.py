"""Scripted stand-ins for aider and the claude CLI, so the whole cascade -
real forge, real git, real graders - runs deterministically with no model.

A plan (JSON in $LEASH_STUB_PLAN) says what each editor call does:

    {"first": <action>, "fix": <action>, "cloud": <action>}

where an action is an overlay directory path to copy into the worktree,
or one of "crash", "nochange", "quota", "cloud_error". "first" answers the
initial attempt, "fix" answers forge's validation-retry prompt, "cloud"
answers the escalation (claude or agy). Every call is appended to $LEASH_STUB_LOG.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

STUB_AIDER = r'''#!PYTHON
import json, os, shutil, subprocess, sys
msg = sys.argv[sys.argv.index("--message") + 1]
plan = json.loads(os.environ["LEASH_STUB_PLAN"])
kind = "fix" if "did not pass validation" in msg else "first"
action = plan.get(kind, "nochange")
with open(os.environ["LEASH_STUB_LOG"], "a") as f:
    f.write(json.dumps({"tool": "aider", "kind": kind, "action": action}) + "\n")
if action == "crash":
    sys.exit(3)
if action == "nochange":
    sys.exit(0)
shutil.copytree(action, ".", dirs_exist_ok=True)
subprocess.run(["git", "add", "-A"], check=True)
subprocess.run(["git", "-c", "user.email=s@s", "-c", "user.name=s", "commit", "-q", "-m", "stub"])
'''

STUB_CLAUDE = r'''#!PYTHON
import json, os, shutil, sys
if "--version" in sys.argv:
    print("0.0.0-stub (Claude Code)")
    sys.exit(0)
prompt = sys.stdin.read()
plan = json.loads(os.environ["LEASH_STUB_PLAN"])
action = plan.get("cloud", "nochange")
model = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else None
with open(os.environ["LEASH_STUB_LOG"], "a") as f:
    f.write(json.dumps({"tool": "claude", "action": action, "model": model,
                        "repair": "already committed in this repository" in prompt}) + "\n")
if action == "quota":
    print(json.dumps({"is_error": True, "result": "Claude AI usage limit reached, resets at 5pm"}))
    sys.exit(1)
if action == "cloud_error":
    print(json.dumps({"is_error": True, "result": "There's an issue with the selected model"}))
    sys.exit(1)
if action != "nochange":
    shutil.copytree(action, ".", dirs_exist_ok=True)
print(json.dumps({"result": "done", "usage": {"input_tokens": 120, "output_tokens": 30},
                  "duration_ms": 1500}))
'''


STUB_AGY = r'''#!PYTHON
import json, os, shutil, sys
if "--version" in sys.argv:
    print("1.2.1-stub")
    sys.exit(0)
# Like the real CLI: --print consumes the next argument as the prompt.
prompt = sys.argv[sys.argv.index("--print") + 1]
plan = json.loads(os.environ["LEASH_STUB_PLAN"])
action = plan.get("cloud", "nochange")
model = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else None
with open(os.environ["LEASH_STUB_LOG"], "a") as f:
    f.write(json.dumps({"tool": "agy", "action": action, "model": model,
                        "print_last": sys.argv[-2] == "--print",
                        "repair": "already committed in this repository" in prompt}) + "\n")
if action in ("quota", "cloud_error"):
    error = "RESOURCE_EXHAUSTED: quota exceeded" if action == "quota" else "internal error"
    print(json.dumps({"status": "ERROR", "response": "", "error": error, "usage": {}}))
    sys.exit(1)
if action != "nochange":
    shutil.copytree(action, ".", dirs_exist_ok=True)
print(json.dumps({"status": "SUCCESS", "response": "done", "duration_seconds": 2.0,
                  "usage": {"input_tokens": 900, "output_tokens": 40, "thinking_tokens": 10,
                            "cache_read_tokens": 0}}))
'''


def install(bin_dir: Path) -> None:
    bin_dir.mkdir(parents=True, exist_ok=True)
    for name, body in (("aider", STUB_AIDER), ("claude", STUB_CLAUDE), ("agy", STUB_AGY)):
        path = bin_dir / name
        path.write_text(body.replace("PYTHON", sys.executable, 1))
        path.chmod(0o755)


def set_plan(plan: dict, log: Path) -> None:
    os.environ["LEASH_STUB_PLAN"] = json.dumps({k: str(v) for k, v in plan.items()})
    os.environ["LEASH_STUB_LOG"] = str(log)


def calls(log: Path) -> list[dict]:
    if not log.exists():
        return []
    return [json.loads(line) for line in log.read_text().splitlines() if line.strip()]
