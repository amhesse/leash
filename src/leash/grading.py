"""Hidden graders.

A task is correct only if its hidden grader AND the fixture's own visible
tests pass - a solution that satisfies the grader by breaking existing
behaviour is still wrong. The grader is copied in only for the duration
of the check and never committed, so the model never sees it.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from .fixtures import git

GRADER_NAME = "_leash_grader.py"
GRADE_TIMEOUT = 120
DETAIL_CHARS = 1500


def grade(checkout: Path, grader: Path) -> tuple[bool, str]:
    target = checkout / GRADER_NAME
    shutil.copy(grader, target)
    try:
        commands = [[sys.executable, GRADER_NAME]]
        if (checkout / "tests").is_dir():
            commands.append([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"])
        for cmd in commands:
            try:
                r = subprocess.run(cmd, cwd=checkout, capture_output=True, text=True,
                                   timeout=GRADE_TIMEOUT)
            except subprocess.TimeoutExpired:
                return False, f"grading timed out after {GRADE_TIMEOUT}s: {' '.join(cmd[1:])}"
            if r.returncode != 0:
                return False, (r.stdout + r.stderr)[-DETAIL_CHARS:]
        return True, ""
    finally:
        target.unlink(missing_ok=True)


def grade_commit(repo: Path, rev: str, grader: Path) -> tuple[bool, str]:
    """Grades `rev` in a throwaway detached worktree, leaving the repo's
    own checkout (and every branch) exactly as it was."""
    with tempfile.TemporaryDirectory(prefix="leash-grade-") as d:
        wt = Path(d) / "wt"
        add = git(repo, "worktree", "add", "-q", "--detach", str(wt), rev, check=False)
        if add.returncode != 0:
            return False, f"could not check out {rev} for grading: {add.stderr.strip()}"
        try:
            return grade(wt, grader)
        finally:
            git(repo, "worktree", "remove", "--force", str(wt), check=False)
            git(repo, "worktree", "prune", check=False)
