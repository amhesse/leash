"""Results files: one JSON object per line, one line per trial.

Append-only while running (a killed run loses at most the trial in
flight). Rows are keyed so a re-run resumes instead of repeating work:
the same model digest, harness configuration, task content and trial
number is the same measurement.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

from . import RESULTS_SCHEMA


def trial_key(row: dict) -> tuple:
    return (
        (row.get("model") or {}).get("digest") or (row.get("model") or {}).get("name"),
        (row.get("harness") or {}).get("hash"),
        (row.get("cloud") or {}).get("model"),
        row.get("task_hash"),
        row.get("trial"),
    )


def load(path: Path) -> list[dict]:
    """Every row, in file order. Later rows for the same key supersede
    earlier ones (a fill or a re-run after an error), so callers wanting
    the current state should use latest()."""
    if not path.exists():
        return []
    rows = []
    lines = path.read_text().splitlines()
    for lineno, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except ValueError:
            # A torn final line from a hard kill: skip it, the trial reruns.
            if lineno != len(lines):
                raise ValueError(f"{path}:{lineno}: corrupt results row")
    return rows


def latest(rows: list[dict]) -> list[dict]:
    by_key: dict[tuple, dict] = {}
    for row in rows:
        by_key[trial_key(row)] = row
    return list(by_key.values())


def load_many(paths: list[Path]) -> list[dict]:
    rows: list[dict] = []
    for p in paths:
        rows.extend(load(p))
    return latest(rows)


def completed_keys(rows: list[dict]) -> set[tuple]:
    """Keys that need no further local work. Error rows are not complete:
    an infrastructure failure says nothing about the model, so it reruns."""
    return {trial_key(r) for r in latest(rows) if r.get("status") == "ok"}


def append(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    row = {"schema": RESULTS_SCHEMA, **row}
    line = json.dumps(row, sort_keys=True) + "\n"
    with path.open("a", encoding="utf-8") as f:
        f.write(line)
        f.flush()
        os.fsync(f.fileno())
