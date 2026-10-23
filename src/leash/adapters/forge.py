"""Runs forge (`forge run`) as the harness under test.

forge is driven only through its CLI, as a subprocess in its own process
group - never imported, because it keeps module-level configuration state,
and never trusted to clean up its own children on a timeout.
"""

from __future__ import annotations

import dataclasses
import hashlib
import json
import os
import shutil
import signal
import subprocess
import time
from pathlib import Path

from ..fixtures import CHECKLIST

REQUIRED_FLAGS = ("--snapshot-first-attempt", "--repair-from", "--repair-note")
LOG_TAIL = 4000


class ForgeUnavailable(Exception):
    pass


@dataclasses.dataclass
class StageResult:
    returncode: int | None
    log: str
    seconds: float
    timed_out: bool
    record: dict | None
    marker: str  # "[x]", "[!]", "[?]" or "[ ]"

    @property
    def merged(self) -> bool:
        return self.marker == "[x]"

    @property
    def tokens(self) -> dict:
        return dict((self.record or {}).get("tokens") or {})

    @property
    def log_tail(self) -> str:
        return self.log[-LOG_TAIL:]


def cache_dir(project: Path) -> Path:
    # forge's per-project cache: ~/.cache/aider-loop/<project dir name>/
    return Path.home() / ".cache" / "aider-loop" / project.name


def read_marker(project: Path) -> str:
    text = (project / CHECKLIST).read_text()
    return next((m for m in ("[x]", "[!]", "[?]") if f"- {m}" in text), "[ ]")


class ForgeAdapter:
    name = "forge"

    def __init__(self, forge_cmd: list[str] | None = None, max_retries: int | None = None,
                 max_validation_retries: int | None = None,
                 hard_validation_retries: int | None = None,
                 lite_hard_num_predict: int | None = None,
                 lite_hard_budget_directive: bool = False,
                 lite_hard_think_off: bool = False):
        self.forge_cmd = forge_cmd or ["forge"]
        self.max_retries = max_retries
        self.max_validation_retries = max_validation_retries
        self.hard_validation_retries = hard_validation_retries
        self.lite_hard_num_predict = lite_hard_num_predict
        self.lite_hard_budget_directive = lite_hard_budget_directive
        self.lite_hard_think_off = lite_hard_think_off

    # ---- environment ---------------------------------------------------------

    def check_available(self, backends: tuple[str, ...] = ()) -> None:
        exe = shutil.which(self.forge_cmd[0])
        if exe is None:
            raise ForgeUnavailable(f"`{self.forge_cmd[0]}` not found on PATH")
        help_text = subprocess.run([*self.forge_cmd, "run", "--help"], capture_output=True,
                                   text=True, timeout=60).stdout
        missing = [f for f in REQUIRED_FLAGS if f not in help_text]
        if missing:
            raise ForgeUnavailable(
                f"installed forge lacks {', '.join(missing)} - update forge (it needs the "
                f"benchmark hooks added for Leash)")
        choices = help_text.split("--backend", 1)[-1].split("\n", 1)[0]
        for backend in backends:
            if backend not in choices:
                raise ForgeUnavailable(f"installed forge's --backend does not accept `{backend}` - update forge")

    def version_info(self) -> dict:
        """forge version and, when it is a git checkout, the exact commit
        (with a dirty flag) - results depend on the harness, so they must
        name it precisely."""
        info = {"version": None, "commit": None, "dirty": None, "path": None}
        exe = shutil.which(self.forge_cmd[0])
        if not exe:
            return info
        try:
            shebang = Path(exe).read_text(errors="replace").splitlines()[0]
            python = shebang[2:].strip() if shebang.startswith("#!") else None
        except (OSError, IndexError):
            python = None
        if not python:
            return info
        probe = subprocess.run(
            [*python.split(), "-c", "import forge, os; print(forge.__version__); "
                                    "print(os.path.dirname(forge.__file__))"],
            capture_output=True, text=True, timeout=30)
        if probe.returncode != 0:
            return info
        version, path = (probe.stdout.splitlines() + [None, None])[:2]
        info.update(version=version, path=path)
        if path:
            head = subprocess.run(["git", "-C", path, "rev-parse", "--short=12", "HEAD"],
                                  capture_output=True, text=True)
            if head.returncode == 0:
                info["commit"] = head.stdout.strip()
                status = subprocess.run(["git", "-C", path, "status", "--porcelain", "--", "."],
                                        capture_output=True, text=True)
                info["dirty"] = bool(status.stdout.strip())
        return info

    def harness_config(self, backend: str) -> dict:
        config = {
            "adapter": self.name,
            "backend": backend,
            "max_retries": self.max_retries,
            "max_validation_retries": self.max_validation_retries,
            "review": None,
            "escalation_mode": "repair",
        }
        config["hash"] = hashlib.sha256(json.dumps(config, sort_keys=True).encode()).hexdigest()[:12]
        return config

    # ---- running -------------------------------------------------------------

    def run(self, project: Path, *, backend: str, model: str | None, extra: list[str],
            timeout: float) -> StageResult:
        cmd = [*self.forge_cmd, "run", "--project-dir", str(project), "--todo-file", CHECKLIST,
               "--backend", backend, "--sleep-between", "0", "--keep-branches", "--max-items", "1"]
        if model:
            cmd += ["--models", model]
        if self.max_retries is not None:
            cmd += ["--max-retries", str(self.max_retries)]
        if self.max_validation_retries is not None:
            cmd += ["--max-validation-retries", str(self.max_validation_retries)]
        if self.hard_validation_retries is not None:
            cmd += ["--hard-validation-retries", str(self.hard_validation_retries)]
        if self.lite_hard_num_predict is not None:
            cmd += ["--lite-hard-num-predict", str(self.lite_hard_num_predict)]
        if self.lite_hard_budget_directive:
            cmd += ["--lite-hard-budget-directive"]
        if self.lite_hard_think_off:
            cmd += ["--lite-hard-think-off"]
        cmd += extra

        started_wall = time.time()
        started = time.monotonic()
        proc = subprocess.Popen(cmd, cwd=project, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                text=True, start_new_session=True)
        timed_out = False
        try:
            out, _ = proc.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            _kill_group(proc)
            out, _ = proc.communicate()
            out = (out or "") + f"\n[leash] stage killed after {int(timeout)}s\n"
        except KeyboardInterrupt:
            _kill_group(proc)
            proc.communicate()
            raise
        seconds = round(time.monotonic() - started, 1)
        return StageResult(returncode=proc.returncode, log=out or "", seconds=seconds,
                           timed_out=timed_out, record=_latest_record(project, started_wall),
                           marker=read_marker(project))


def _kill_group(proc: subprocess.Popen) -> None:
    for sig in (signal.SIGTERM, signal.SIGKILL):
        try:
            os.killpg(proc.pid, sig)
        except ProcessLookupError:
            return
        try:
            proc.wait(timeout=10)
            return
        except subprocess.TimeoutExpired:
            continue


def _latest_record(project: Path, since: float) -> dict | None:
    runs = cache_dir(project) / "runs"
    if not runs.is_dir():
        return None
    candidates = [p for p in runs.glob("*/item-*.json") if p.stat().st_mtime >= since - 1]
    for path in sorted(candidates, key=lambda p: p.stat().st_mtime, reverse=True):
        try:
            return json.loads(path.read_text())
        except (OSError, ValueError):
            continue
    return None
