"""Run metadata: exactly which model, runtime, hardware and cloud CLI a
result came from, plus the warm-up that keeps model load time out of
trial 1."""

from __future__ import annotations

import json
import os
import platform
import shutil
import subprocess
import time
import urllib.error
import urllib.request


class ModelUnavailable(Exception):
    pass


def ollama_url() -> str:
    host = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434").strip()
    if not host.startswith(("http://", "https://")):
        host = f"http://{host}"
    return host.rstrip("/")


def _ollama(path: str, payload: dict | None = None, timeout: float = 30) -> dict:
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(f"{ollama_url()}{path}", data=data,
                                 headers={"Content-Type": "application/json"} if data else {})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode() or "{}")


def anthropic_endpoint_model_info(name: str) -> dict:
    """Identity of a doer reached through an OpenAI/Anthropic-compatible
    HTTP endpoint (ANTHROPIC_BASE_URL) rather than Ollama.

    A local server such as Strata serves one model and names it on
    /v1/status, which is the honest thing to record: the `--model` value
    on such a run is only a label the CLI insists on and the server
    ignores, so recording it as the model under test would put the wrong
    name on every row.
    """
    base = os.environ.get("ANTHROPIC_BASE_URL", "").rstrip("/")
    info = {"name": name, "provider": "anthropic-endpoint", "digest": None,
            "size_bytes": None, "family": None, "parameter_size": None,
            "quantization": None, "format": None,
            "runtime": {"base_url": base or None}}
    if not base:
        return info
    try:
        with urllib.request.urlopen(base + "/v1/status", timeout=10) as r:
            status = json.loads(r.read())
    except (urllib.error.URLError, OSError, ValueError) as e:
        raise ModelUnavailable(f"no endpoint at {base}/v1/status: {e}")
    if not status.get("loaded", True):
        raise ModelUnavailable(f"{base} reports the model is not loaded")
    served = status.get("model")
    if served:
        info["name"] = served
    info["provider"] = status.get("service") or "anthropic-endpoint"
    info["runtime"] = {"base_url": base, "engine": status.get("engine"),
                       "max_context": status.get("cache_max_tokens") or status.get("max_context"),
                       "concurrency": (status.get("concurrency") or {}).get("serving"),
                       "requested_model_label": name}
    return info


def ollama_model_info(name: str) -> dict:
    """Name, digest, quantization and size of a local Ollama model.
    Raises ModelUnavailable if Ollama is down or doesn't have the model."""
    try:
        version = _ollama("/api/version").get("version")
        tags = _ollama("/api/tags").get("models", [])
    except (urllib.error.URLError, OSError, ValueError) as e:
        raise ModelUnavailable(f"Ollama not reachable at {ollama_url()}: {e}")
    wanted = name if ":" in name else f"{name}:latest"
    match = next((m for m in tags if m.get("name") in (name, wanted)), None)
    if match is None:
        raise ModelUnavailable(f"model {name!r} is not pulled in Ollama (`ollama pull {name}`)")
    details = match.get("details") or {}
    info = {
        "name": match["name"],
        "provider": "ollama",
        "digest": match.get("digest"),
        "size_bytes": match.get("size"),
        "family": details.get("family"),
        "parameter_size": details.get("parameter_size"),
        "quantization": details.get("quantization_level"),
        "format": details.get("format"),
        "runtime": {"ollama_version": version},
    }
    try:
        show = _ollama("/api/show", {"model": match["name"]})
        model_info = show.get("model_info") or {}
        ctx = next((v for k, v in model_info.items() if k.endswith(".context_length")), None)
        info["context_length"] = ctx
    except (urllib.error.URLError, OSError, ValueError):
        pass
    return info


def warm_up(name: str, keep_alive: str = "30m", timeout: float = 600) -> float:
    """Loads the model and pins it in memory. Returns load seconds, which
    are recorded separately rather than charged to the first trial."""
    started = time.monotonic()
    try:
        _ollama("/api/generate", {"model": name, "prompt": "ok", "stream": False,
                                  "keep_alive": keep_alive, "options": {"num_predict": 1}},
                timeout=timeout)
    except (urllib.error.URLError, OSError, ValueError) as e:
        raise ModelUnavailable(f"warm-up of {name!r} failed: {e}")
    return round(time.monotonic() - started, 1)


def hardware() -> dict:
    info = {"host_os": f"{platform.system()} {platform.release()}", "python": platform.python_version(),
            "gpus": []}
    if shutil.which("nvidia-smi"):
        r = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total,driver_version",
                            "--format=csv,noheader,nounits"], capture_output=True, text=True, timeout=10)
        for line in r.stdout.strip().splitlines():
            parts = [p.strip() for p in line.split(",")]
            if len(parts) == 3:
                info["gpus"].append({"name": parts[0], "vram_mb": int(float(parts[1])), "driver": parts[2]})
    return info


def cloud_cli_info(engine: str) -> dict:
    exe = {"claude": "claude", "agy": "agy"}.get(engine)
    if not exe or not shutil.which(exe):
        return {"engine": engine, "cli_version": None, "available": False}
    try:
        r = subprocess.run([exe, "--version"], capture_output=True, text=True, timeout=30,
                           stdin=subprocess.DEVNULL)
    except (subprocess.TimeoutExpired, OSError):
        return {"engine": engine, "cli_version": None, "available": True}
    return {"engine": engine, "cli_version": (r.stdout or r.stderr).strip() or None, "available": True}
