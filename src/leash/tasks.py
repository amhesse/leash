"""Task directories: loading, validation, signals and content hashing.

A task is a directory under <bench>/tasks/:

    task.md        the instruction exactly as the agent sees it
    meta.toml      id, category, fixture, language, visibility, [mutants] name = description
    grader.py      hidden grader, run from the checkout root; exit 0 = correct
    reference/     overlay of a known-correct solution onto the fixture
    mutants/<n>/   overlays of known-WRONG solutions (the grader must reject each)

Adding a test is dropping in such a directory; `leash selftest` decides
whether it may be used.
"""

from __future__ import annotations

import dataclasses
import hashlib
import os
import re
import tomllib
from pathlib import Path

REQUIRED_META = ("id", "category", "fixture")
VISIBILITIES = ("public", "private")

_FENCE_RE = re.compile(r"```[^\n]*\n.*?```", re.S)
_FILE_RE = re.compile(r"`([\w./-]+\.[A-Za-z0-9]{1,8})`")
# `Ledger.add` and `ledger.store.Ledger` look like paths to the regex above;
# only names with a real file extension count as files.
_FILE_EXTENSIONS = frozenset(
    "py js jsx ts tsx mjs cjs go rs java kt rb php c h cc cpp hpp cs swift scala "
    "md txt rst json toml yaml yml ini cfg conf env html htm css scss sql sh bash "
    "csv xml proto gradle lock".split())
_TDD_RE = re.compile(r"^\s*TDD:\s*", re.I)


class TaskError(Exception):
    pass


@dataclasses.dataclass(frozen=True)
class Task:
    id: str
    category: str
    fixture: str
    language: str
    visibility: str
    text: str
    path: Path
    mutants: dict[str, str]

    @property
    def grader(self) -> Path:
        return self.path / "grader.py"

    @property
    def reference(self) -> Path:
        return self.path / "reference"

    def mutant_dir(self, name: str) -> Path:
        return self.path / "mutants" / name

    def fixture_dir(self, bench: Path) -> Path:
        return bench / "fixtures" / self.fixture

    def signals(self) -> dict:
        return task_signals(self.text)

    def content_hash(self, bench: Path) -> str:
        """Changes whenever anything that could change a trial's outcome
        changes: the instruction, the grader, the reference, or the
        fixture it starts from. Results are only comparable within a hash."""
        h = hashlib.sha256()
        h.update(self.text.encode())
        h.update(self.grader.read_bytes())
        for root in (self.reference, self.fixture_dir(bench)):
            for f in sorted(p for p in root.rglob("*") if p.is_file() and _hashable(p)):
                h.update(str(f.relative_to(root)).encode())
                h.update(f.read_bytes())
        return h.hexdigest()[:16]


def _hashable(p: Path) -> bool:
    return "__pycache__" not in p.parts and p.suffix != ".pyc"


def task_signals(text: str) -> dict:
    """Coarse, harness-independent shape signals of the instruction text.

    Deliberately simple: forge's own view (with its negation handling) is
    recorded per trial as `forge_expected_files`; these exist so tasks can
    be grouped without running anything."""
    prose = _FENCE_RE.sub("", text)
    files = sorted({f for f in _FILE_RE.findall(prose)
                    if f.rsplit(".", 1)[-1].lower() in _FILE_EXTENSIONS})
    exact = any("exactly" in text[:m.start()].rstrip()[-80:].lower()
                and text[:m.start()].rstrip().endswith(":")
                for m in _FENCE_RE.finditer(text))
    return {"tdd": bool(_TDD_RE.match(text)), "files": len(files), "exact": exact}


def load_task(path: Path) -> Task:
    meta_path = path / "meta.toml"
    if not meta_path.is_file():
        raise TaskError(f"{path.name}: missing meta.toml")
    try:
        meta = tomllib.loads(meta_path.read_text())
    except tomllib.TOMLDecodeError as e:
        raise TaskError(f"{path.name}: bad meta.toml: {e}")
    for key in REQUIRED_META:
        if not meta.get(key):
            raise TaskError(f"{path.name}: meta.toml needs `{key}`")
    if meta["id"] != path.name:
        raise TaskError(f"{path.name}: meta id {meta['id']!r} must match the directory name")
    visibility = meta.get("visibility", "public")
    if visibility not in VISIBILITIES:
        raise TaskError(f"{path.name}: visibility must be one of {VISIBILITIES}")
    for required in ("task.md", "grader.py", "reference"):
        if not (path / required).exists():
            raise TaskError(f"{path.name}: missing {required}")
    mutants = dict(meta.get("mutants", {}))
    for name in mutants:
        if not (path / "mutants" / name).is_dir():
            raise TaskError(f"{path.name}: mutant {name!r} listed in meta.toml has no mutants/{name}/")
    on_disk = {p.name for p in (path / "mutants").iterdir() if p.is_dir()} if (path / "mutants").is_dir() else set()
    for name in sorted(on_disk - set(mutants)):
        mutants[name] = "(undocumented)"
    return Task(
        id=meta["id"], category=meta["category"], fixture=meta["fixture"],
        language=meta.get("language", "unknown"), visibility=visibility,
        text=(path / "task.md").read_text().strip() + "\n", path=path, mutants=mutants,
    )


def load_tasks(bench: Path, ids: list[str] | None = None,
               categories: list[str] | None = None) -> list[Task]:
    root = bench / "tasks"
    if not root.is_dir():
        raise TaskError(f"no tasks/ directory in {bench}")
    tasks = [load_task(p) for p in sorted(root.iterdir()) if p.is_dir() and not p.name.startswith(".")]
    for t in tasks:
        if not t.fixture_dir(bench).is_dir():
            raise TaskError(f"{t.id}: fixture {t.fixture!r} not found in {bench / 'fixtures'}")
    if ids:
        known = {t.id for t in tasks}
        unknown = sorted(set(ids) - known)
        if unknown:
            raise TaskError(f"unknown task id(s): {', '.join(unknown)}")
        tasks = [t for t in tasks if t.id in ids]
    if categories:
        tasks = [t for t in tasks if t.category in categories]
    return tasks


def default_bench() -> Path:
    """LEASH_BENCH, else the repository this package lives in (editable install)."""
    env = os.environ.get("LEASH_BENCH")
    if env:
        return Path(env).expanduser().resolve()
    return Path(__file__).resolve().parents[2]
