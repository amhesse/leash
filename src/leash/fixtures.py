"""Materializing a task's starting repository for one trial."""

from __future__ import annotations

import os
import shutil
import subprocess
import time
from pathlib import Path

from .tasks import Task

GIT_IDENTITY = ["-c", "user.email=leash@localhost", "-c", "user.name=leash"]
CHECKLIST = "TODO.md"
_IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc", ".git")


def git(cwd: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *GIT_IDENTITY, *args], cwd=cwd,
                          capture_output=True, text=True, check=check)


def unique_name(task: Task) -> str:
    # forge keys its cache directory on the project directory's name, so
    # every trial needs its own to keep records from mixing.
    return f"leash-{task.id}-{os.getpid()}-{time.time_ns()}"


def checklist_line(task: Task) -> str:
    return f"- [ ] {task.text.strip()}\n"


def materialize(task: Task, bench: Path, parent: Path, name: str | None = None) -> Path:
    """Copies the fixture into parent/<name>, writes the one-item checklist
    and commits it as the base. Returns the project directory."""
    project = parent / (name or unique_name(task))
    shutil.copytree(task.fixture_dir(bench), project, ignore=_IGNORE)
    (project / CHECKLIST).write_text(checklist_line(task))
    git(project, "init", "-q", "-b", "master")
    git(project, "add", "-A")
    git(project, "commit", "-q", "-m", f"fixture for {task.id}")
    return project


def reopen_checklist_item(project: Path, task: Task) -> None:
    """Puts the item back to `[ ]` so a follow-up `forge run` (escalation)
    picks it up. TODO.md is exempt from forge's clean-checkout check."""
    (project / CHECKLIST).write_text(checklist_line(task))


def overlay(src: Path, dst: Path) -> None:
    shutil.copytree(src, dst, dirs_exist_ok=True, ignore=_IGNORE)


def checkout_copy(task: Task, bench: Path, parent: Path, overlay_dir: Path | None = None) -> Path:
    """A plain (non-git) fixture copy with an optional overlay - what
    selftest grades references and mutants against."""
    target = parent / unique_name(task)
    shutil.copytree(task.fixture_dir(bench), target, ignore=_IGNORE)
    if overlay_dir is not None:
        overlay(overlay_dir, target)
    return target
