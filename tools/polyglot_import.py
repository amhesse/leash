#!/usr/bin/env python3
"""Phase 4 of docs/09-forge-vs-aider-benchmark.md: import a subset of
Aider's own public benchmark (Aider-AI/polyglot-benchmark, sourced from
Exercism's Python track) as a separate Leash bench, so both forge (via
`leash run --bench <this>`) and aider (via `tools/aider_bench.py --bench
<this>`) can be run against tasks neither tool was tuned on - the highest-
credibility version of the forge-vs-aider comparison.

Exercism's own per-exercise layout is a near-exact match for Leash's task
format already:
  <name>.py          - the stub the model edits (this project's task.md
                        instruction + this stub become the fixture)
  <name>_test.py      - the exercise's real test suite (kept as the
                        fixture's own visible tests - exactly matching how
                        forge's own retry loop already validates every
                        other task in this project, and matching aider's
                        polyglot protocol of showing test failures back to
                        the model on a second attempt)
  .docs/instructions.md - becomes task.md
  .meta/example.py    - Exercism's own canonical reference solution,
                        becomes this task's reference/ (used by `leash
                        selftest` to confirm the task is achievable and
                        not already solved)

No mutants are authored for these tasks (optional in Leash's format) -
selftest still checks (1) the untouched stub fails, (2) the reference
solution passes.

Usage:
    python3 tools/polyglot_import.py --source /path/to/polyglot-benchmark \\
        --out benches/polyglot-subset --exercises transpose,phone-number,...
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

_FENCE_RE = re.compile(r"```[^\n]*\n(.*?)```\n?", re.S)


def defence(text: str) -> str:
    """Forge's own preflight rules refuse any item with a fenced code block
    that isn't preceded by the word "exactly" (a real safety feature: it
    means the block is an unverified, non-byte-exact target). Exercism's
    instructions use illustrative fenced examples freely, with no such
    convention. Converts every fence to a plain indented block instead -
    content-neutral, applies identically for both tools, only changes
    forge-incompatible markdown syntax, not the challenge itself."""
    def repl(m: re.Match) -> str:
        body = m.group(1)
        return "\n".join(f"    {line}" if line.strip() else "" for line in body.splitlines()) + "\n"
    return _FENCE_RE.sub(repl, text)

GRADER_TEMPLATE = '''"""Hidden grader for {name} (imported from Aider's polyglot-benchmark /
Exercism's Python track - see SOURCE.md in this bench for attribution).
Re-runs the exercise's own real test suite; that suite IS the grader for
these tasks, there is no separate hidden check beyond it, matching how
Exercism/Aider's own benchmark scores these exercises."""
import subprocess
import sys

r = subprocess.run([sys.executable, "-m", "unittest", "{test_module}", "-v"],
                   capture_output=True, text=True)
sys.stdout.write(r.stdout)
sys.stderr.write(r.stderr)
sys.exit(r.returncode)
'''

META_TEMPLATE = '''id = "{name}"
category = "external"
fixture = "{name}"
language = "python"
'''

TASK_MD_TEMPLATE = """{instructions}

Implement your solution in `{stub_file}`. The file {test_file} contains
the real test suite for this exercise - do not edit it.
"""


def import_one(src: Path, out: Path, name: str) -> None:
    slug = name.replace("-", "_")
    stub_file = f"{slug}.py"
    test_file = f"{slug}_test.py"

    if not (src / stub_file).is_file():
        raise SystemExit(f"{name}: expected stub {stub_file} not found under {src}")
    if not (src / test_file).is_file():
        raise SystemExit(f"{name}: expected test file {test_file} not found under {src}")
    example = src / ".meta" / "example.py"
    if not example.is_file():
        raise SystemExit(f"{name}: no .meta/example.py reference solution found")
    instructions = defence((src / ".docs" / "instructions.md").read_text())

    fixture_dir = out / "fixtures" / name
    fixture_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(src / stub_file, fixture_dir / stub_file)
    shutil.copy(src / test_file, fixture_dir / test_file)
    # Without this, forge falls back to its own built-in default validate
    # behavior (a syntax-only check) instead of actually running the real
    # test suite during its own retry loop - exactly the config every task
    # in this project's own tasks/ ships, here pointed at the test file's
    # real location (fixture root, not tests/, matching Exercism's layout).
    (fixture_dir / ".aiderloop.toml").write_text(
        "[validate]\n"
        'checks = ["python"]\n'
        f'commands = ["python -m unittest {test_file[:-3]} -q"]\n')

    task_dir = out / "tasks" / name
    task_dir.mkdir(parents=True, exist_ok=True)
    (task_dir / "meta.toml").write_text(META_TEMPLATE.format(name=name))
    (task_dir / "task.md").write_text(
        TASK_MD_TEMPLATE.format(instructions=instructions.strip(),
                                stub_file=stub_file, test_file=test_file))
    (task_dir / "grader.py").write_text(
        GRADER_TEMPLATE.format(name=name, test_module=test_file[:-3]))

    ref_dir = task_dir / "reference"
    ref_dir.mkdir(exist_ok=True)
    shutil.copy(example, ref_dir / stub_file)

    print(f"imported {name}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, type=Path,
                    help="Path to a checkout of Aider-AI/polyglot-benchmark")
    ap.add_argument("--out", required=True, type=Path,
                    help="Output bench directory (created if missing)")
    ap.add_argument("--exercises", required=True,
                    help="Comma-separated exercise names, e.g. transpose,wordy")
    args = ap.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    src_root = args.source / "python" / "exercises" / "practice"
    for name in args.exercises.split(","):
        import_one(src_root / name, args.out, name)

    (args.out / "SOURCE.md").write_text(
        "Imported from https://github.com/Aider-AI/polyglot-benchmark "
        "(Exercism Python track) via tools/polyglot_import.py, for Phase 4 "
        "of docs/09-forge-vs-aider-benchmark.md. All exercise content is "
        "copyright (c) Exercism, used under Exercism's open source "
        "licenses - see the source repo's own README for attribution.\n"
        f"Exercises: {args.exercises}\n")
    print(f"done: bench written to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
