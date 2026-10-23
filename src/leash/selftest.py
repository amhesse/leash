"""`leash selftest`: validates tasks before any model result may count.

For every task:
  1. the untouched fixture FAILS the grader  (the task isn't already done)
  2. the reference solution PASSES           (the task is achievable as graded)
  3. every mutant FAILS                      (the grader rejects plausible wrong answers)

A grader that can't reject its mutants is too lenient and would turn wrong
work into fake passes, so a failing task is refused by `leash run`.
"""

from __future__ import annotations

import dataclasses
import shutil
import tempfile
from pathlib import Path

from .fixtures import checkout_copy
from .grading import grade
from .tasks import Task


@dataclasses.dataclass
class TaskCheck:
    task: Task
    problems: list[str]
    mutants_checked: int

    @property
    def ok(self) -> bool:
        return not self.problems


def check_task(task: Task, bench: Path) -> TaskCheck:
    problems: list[str] = []
    with tempfile.TemporaryDirectory(prefix="leash-selftest-") as d:
        parent = Path(d)

        def run(overlay_dir: Path | None) -> tuple[bool, str]:
            checkout = checkout_copy(task, bench, parent, overlay_dir)
            try:
                return grade(checkout, task.grader)
            finally:
                shutil.rmtree(checkout, ignore_errors=True)

        if run(None)[0]:
            problems.append("grader passes on the untouched fixture (task is already solved)")
        ok, detail = run(task.reference)
        if not ok:
            problems.append(f"reference solution fails: {detail.strip()[-400:]}")
        for name in task.mutants:
            if run(task.mutant_dir(name))[0]:
                problems.append(f"mutant {name!r} passes - grader too lenient ({task.mutants[name]})")
    return TaskCheck(task, problems, len(task.mutants))


def check_tasks(tasks: list[Task], bench: Path, on_result=None) -> list[TaskCheck]:
    results = []
    for task in tasks:
        result = check_task(task, bench)
        results.append(result)
        if on_result:
            on_result(result)
    return results
