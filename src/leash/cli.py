"""leash - how long a leash can you give an AI coding model?

  leash selftest                 validate every task's grader (reference passes, mutants fail)
  leash tasks                    list tasks, categories and signals
  leash estimate --model M       how long a run would take, from earlier results
  leash run --model M            run the battery: unchecked / checked / escalated per trial
  leash report results/*.jsonl   markdown (stdout or --md) and HTML (--html) report
  leash sabotage ...             the attack condition: side tasks, framings, monitor (doc 12)
"""

from __future__ import annotations

import argparse
import datetime
import re
import statistics
import sys
import uuid
from pathlib import Path

from . import __version__, cascade, env, report, results, sabotage_cli, selftest, stats
from .adapters.forge import ForgeAdapter, ForgeUnavailable
from .outcomes import CHECKED, ESCALATED, STOPS_ESCALATION, UNCHECKED
from .tasks import TaskError, default_bench, load_tasks

DEFAULT_STAGE_TIMEOUT = 45 * 60
# Escalation model used unless --escalate says otherwise ("none" disables).
DEFAULT_ESCALATE = "gemini:gemini-3.8-flash-high"
# User-facing escalation engines -> the forge backend (CLI) that runs them.
# "ollama" repairs with a second *local* model through forge's own lite
# backend - no cloud CLI, no cost, no network dependency - which is why it
# needs its own branch below rather than going through cloud_cli_info.
ESCALATION_ENGINES = {"gemini": "agy", "agy": "agy", "claude": "claude", "ollama": "lite"}
LOCAL_ESCALATION_ENGINES = {"ollama"}
FALLBACK_STAGE_SECONDS = 120  # used by `estimate` when there are no earlier results


def _split(value: str | None) -> list[str] | None:
    return [v.strip() for v in value.split(",") if v.strip()] if value else None


def parse_escalate(value: str | None) -> tuple[str | None, str | None]:
    """`gemini:<model>` (via the agy CLI), `agy:<model>`, `claude[:<model>]`,
    `ollama:<model>` (a second local model, no cloud involved), or none/off.
    Returns (forge backend, model)."""
    if not value or value.lower() in ("none", "off"):
        return None, None
    engine, _, model = value.partition(":")
    backend = ESCALATION_ENGINES.get(engine)
    if backend is None:
        raise SystemExit(f"--escalate: expected gemini:<model>, agy:<model>, claude[:<model>], "
                         f"ollama:<model>, or none (got {value!r})")
    if backend == "agy" and not model:
        raise SystemExit(f"--escalate {value}: name the model, e.g. {DEFAULT_ESCALATE} (see `agy models`)")
    if engine == "ollama" and not model:
        raise SystemExit(f"--escalate {value}: name a pulled Ollama model, e.g. ollama:qwen2.5-coder:14b")
    return backend, model or None


def default_out(model: str) -> Path:
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", model)
    return Path("results") / f"{safe}-{datetime.date.today():%Y%m%d}.jsonl"


# ---- selftest / tasks ---------------------------------------------------------

def cmd_selftest(args) -> int:
    bench = args.bench
    tasks = load_tasks(bench, _split(args.tasks), _split(args.categories))

    def show(check):
        mark = "ok  " if check.ok else "FAIL"
        print(f"{mark} {check.task.id:32} {check.mutants_checked} mutant(s)")
        for problem in check.problems:
            print(f"       - {problem}")

    checks = selftest.check_tasks(tasks, bench, on_result=show)
    bad = sum(not c.ok for c in checks)
    print(f"\n{len(checks) - bad}/{len(checks)} tasks valid")
    return 1 if bad else 0


def cmd_tasks(args) -> int:
    tasks = load_tasks(args.bench, _split(args.tasks), _split(args.categories))
    print(f"{'task':32} {'category':22} {'tdd':>3} {'files':>5} {'exact':>5} {'mutants':>7}  visibility")
    for t in tasks:
        s = t.signals()
        print(f"{t.id:32} {t.category:22} {'y' if s['tdd'] else '-':>3} {s['files']:>5} "
              f"{'y' if s['exact'] else '-':>5} {len(t.mutants):>7}  {t.visibility}")
    print(f"\n{len(tasks)} tasks, {len({t.category for t in tasks})} categories")
    return 0


# ---- run ----------------------------------------------------------------------

def _progress(row: dict, done: int, total: int, used: int, cap: int | None) -> str:
    head = f"[{done}/{total}] {row['task_id']} #{row['trial']}"
    if row.get("status") != "ok":
        kinds = ", ".join(e["kind"] for e in row.get("errors", []))
        return f"{head}: ERROR ({kinds}) - will rerun on resume"
    c = row["conditions"]
    parts = [f"unchecked={c[UNCHECKED]['outcome']}", f"checked={c[CHECKED]['outcome']}"]
    if ESCALATED in c:
        esc = row.get("escalation") or {}
        parts.append(f"escalated={c[ESCALATED]['outcome']}"
                     + (f" ({esc['status']})" if esc.get("status") not in ("done", "not_needed") else ""))
    seconds = (row.get("local") or {}).get("seconds", 0) + ((row.get("escalation") or {}).get("seconds") or 0)
    budget = f"  escalations {used}/{cap if cap is not None else '∞'}" if c.get(ESCALATED) else ""
    return f"{head}: {'  '.join(parts)}  {seconds:.0f}s{budget}"


def _prepare(args, need_model: bool = True):
    bench = args.bench
    tasks = load_tasks(bench, _split(args.tasks), _split(args.categories))
    if not tasks:
        raise SystemExit("no tasks selected")

    adapter = ForgeAdapter(forge_cmd=args.forge_cmd.split(),
                           max_retries=args.max_retries,
                           max_validation_retries=args.max_validation_retries,
                           hard_validation_retries=args.hard_validation_retries,
                           lite_hard_num_predict=args.lite_hard_num_predict,
                           lite_hard_budget_directive=args.lite_hard_budget_directive,
                           lite_hard_think_off=args.lite_hard_think_off)
    engine, cloud_model = parse_escalate(args.escalate)
    raw_engine = (args.escalate or "").partition(":")[0].lower()
    is_local_escalation = raw_engine in LOCAL_ESCALATION_ENGINES
    try:
        adapter.check_available(backends=(args.backend,) + ((engine,) if engine else ()))
    except ForgeUnavailable as e:
        raise SystemExit(f"forge: {e}")

    cloud = None
    if engine and is_local_escalation:
        # Not "cloud" at all - a second local model, validated the same way
        # as the doer, through forge's own lite backend. Kept in the same
        # `cloud` field so report.py's grouping and labelling need no
        # special case; only the CLI-availability check is skipped.
        try:
            env.ollama_model_info(cloud_model)
        except env.ModelUnavailable as e:
            raise SystemExit(f"--escalate {args.escalate}: {e}")
        cloud = {"engine": "ollama", "cli_version": None, "available": True, "model": args.escalate}
    elif engine:
        cloud = env.cloud_cli_info(engine)
        if not cloud["available"]:
            raise SystemExit(f"--escalate {args.escalate}: `{engine}` CLI not found on PATH "
                             f"(or pass --escalate none)")
        cloud["model"] = args.escalate

    # The claude backend reaches its model over HTTP, not through Ollama, so
    # the model under test is whatever that endpoint serves - asking Ollama
    # about it would fail, and recording --model would label every row with
    # a name the server ignores.
    try:
        if args.backend == "claude":
            model = env.anthropic_endpoint_model_info(args.model)
        else:
            model = env.ollama_model_info(args.model)
    except env.ModelUnavailable as e:
        raise SystemExit(str(e))

    harness = adapter.harness_config(args.backend)
    harness["forge"] = adapter.version_info()
    out = Path(args.out) if args.out else default_out(model["name"])
    policy = cascade.EscalationPolicy(engine=engine, model=cloud_model, name=args.escalate if engine else None,
                                      artifact_dir=out.with_suffix(".artifacts"))
    base_meta = {
        "leash_version": __version__,
        "spec_version": stats.SPEC["version"],
        "model": model,
        "harness": harness,
        "cloud": cloud,
        "hardware": env.hardware(),
    }
    return bench, tasks, adapter, policy, base_meta, out


def cmd_run(args) -> int:
    bench, tasks, adapter, policy, meta, out = _prepare(args)

    if not args.skip_selftest:
        print(f"selftest: validating {len(tasks)} task(s)...")
        checks = selftest.check_tasks(tasks, bench)
        bad = [c for c in checks if not c.ok]
        for c in bad:
            print(f"  refusing {c.task.id}: {'; '.join(c.problems)}")
        tasks = [c.task for c in checks if c.ok]
        if not tasks:
            print("no valid tasks left to run")
            return 1

    existing = results.load(out)
    if args.fill_escalations:
        return _fill(args, bench, tasks, adapter, policy, meta, out, existing)

    probe = {"model": meta["model"], "harness": meta["harness"], "cloud": meta["cloud"]}
    done_keys = results.completed_keys(existing)
    plan = []
    for trial in range(1, args.trials + 1):        # round-robin: trial 1 of every task first
        for task in tasks:
            key = results.trial_key({**probe, "task_hash": task.content_hash(bench), "trial": trial})
            if key not in done_keys:
                plan.append((task, trial))
    total = len(plan)
    skipped = len(tasks) * args.trials - total
    print(f"model {meta['model']['name']} ({meta['model'].get('quantization') or '?'}), "
          f"harness {meta['harness']['backend']} [{meta['harness']['hash']}], "
          f"escalation {policy.label or 'off'}")
    print(f"results -> {out}  ({total} trial(s) to run, {skipped} already complete)")
    if not total:
        print(f"nothing to do. Report with: leash report {out}")
        return 0

    # Ollama-only: the claude backend's server loads its model at startup and
    # has no keep_alive to refresh.
    if args.backend == "claude":
        args.no_warmup = True
    if not args.no_warmup:
        print(f"warming up {meta['model']['name']}...", end=" ", flush=True)
        try:
            load_seconds = env.warm_up(meta["model"]["name"], keep_alive=args.keep_alive)
        except env.ModelUnavailable as e:
            print()
            raise SystemExit(str(e))
        meta["model"]["load_seconds"] = load_seconds
        print(f"{load_seconds}s")

    run_id = uuid.uuid4().hex[:12]
    used = 0
    written = 0
    try:
        for i, (task, trial) in enumerate(plan, 1):
            if policy.enabled and args.max_escalations is not None and used >= args.max_escalations \
                    and policy.allowed:
                policy.allowed, policy.skip_reason = False, "budget"
            key = f"{task.id}-t{trial}-{(meta['model'].get('digest') or 'nodigest')[:12]}"
            row = cascade.run_trial(task, trial, bench=bench, adapter=adapter, model=meta["model"]["name"],
                                    backend=args.backend, policy=policy, stage_timeout=args.stage_timeout,
                                    artifact_key=key)
            row.update(meta, run_id=run_id)
            if (row.get("escalation") or {}).get("status") in ("done", "error"):
                used += 1
            for err in row.get("errors", []):
                if err["stage"] == "cloud" and err["kind"] in STOPS_ESCALATION and policy.allowed:
                    policy.allowed, policy.skip_reason = False, err["kind"]
                    print(f"  escalations stopped for this run: {err['kind']}")
            results.append(out, row)
            written += 1
            print(_progress(row, i, total, used, args.max_escalations), flush=True)
    except KeyboardInterrupt:
        print(f"\ninterrupted - {written} trial(s) saved to {out}. Run the same command again to resume.")
        return 130

    print(f"\ndone: {written} trial(s) written to {out}")
    print(f"report: leash report {out} --html {out.with_suffix('.html')}")
    return 0


def _fill(args, bench, tasks, adapter, policy, meta, out, existing) -> int:
    if not policy.enabled:
        raise SystemExit("--fill-escalations needs --escalate")
    by_id = {t.id: t for t in tasks}
    pending = [r for r in results.latest(existing)
               if (r.get("escalation") or {}).get("status") == "skipped"
               and (r["escalation"].get("bundle")) and r["task_id"] in by_id
               and results.trial_key(r)[:2] == results.trial_key(
                   {"model": meta["model"], "harness": meta["harness"]})[:2]]
    if not pending:
        print("no skipped escalations with saved bundles to fill")
        return 0
    print(f"filling {len(pending)} skipped escalation(s) with {policy.label}")
    used = 0
    try:
        for i, row in enumerate(pending, 1):
            if args.max_escalations is not None and used >= args.max_escalations:
                print("escalation budget reached")
                break
            new = cascade.fill_escalation(row, by_id[row["task_id"]], bench=bench, adapter=adapter,
                                          policy=policy, stage_timeout=args.stage_timeout)
            used += 1
            if new is row or (new.get("escalation") or {}).get("status") == "skipped":
                kinds = [e["kind"] for e in new.get("errors", [])[len(row.get("errors", [])):]]
                print(f"[{i}/{len(pending)}] {row['task_id']} #{row['trial']}: not filled {kinds}")
                if any(k in STOPS_ESCALATION for k in kinds):
                    break
                continue
            new["cloud"] = meta["cloud"]
            results.append(out, new)
            print(_progress(new, i, len(pending), used, args.max_escalations))
    except KeyboardInterrupt:
        print("\ninterrupted - completed fills are saved")
        return 130
    return 0


# ---- estimate -----------------------------------------------------------------

def _timing_rows(paths: list[Path], model: str) -> list[dict]:
    """(local seconds, cloud seconds or None, parked?) per earlier trial of
    `model`, from Leash results or forge's older `forge calibrate` JSONL
    (where `model` is a plain string and `outcome` is top-level)."""
    names = (model, f"{model}:latest")
    out = []
    for path in paths:
        for r in results.load(path):
            if isinstance(r.get("model"), str):          # forge calibrate row
                if r["model"] in names and r.get("seconds") is not None:
                    out.append({"local": r["seconds"], "cloud": None,
                                "parked": r.get("outcome") in ("parked", "parked_ok")})
            elif r.get("status") == "ok" and (r.get("model") or {}).get("name") in names:
                esc = r.get("escalation") or {}
                out.append({"local": (r.get("local") or {}).get("seconds"),
                            "cloud": esc.get("seconds") if esc.get("status") == "done" else None,
                            "parked": r["conditions"][CHECKED]["outcome"] not in ("pass", "silent_wrong")})
    return out


def cmd_estimate(args) -> int:
    tasks = load_tasks(args.bench, _split(args.tasks), _split(args.categories))
    paths = [Path(p) for p in (args.from_results or [])] + ([Path(args.out)] if args.out else [])
    mine = _timing_rows([p for p in paths if p.exists()], args.model)
    trials = len(tasks) * args.trials
    local = [r["local"] for r in mine if r["local"] is not None]
    cloud = [r["cloud"] for r in mine if r["cloud"] is not None]
    parked = [r for r in mine if r["parked"]]
    local_s = statistics.median(local) if local else FALLBACK_STAGE_SECONDS
    cloud_s = statistics.median(cloud) if cloud else FALLBACK_STAGE_SECONDS
    park_rate = len(parked) / len(mine) if mine else 0.3
    escalations = round(trials * park_rate) if parse_escalate(args.escalate)[0] else 0
    capped = min(escalations, args.max_escalations) if args.max_escalations is not None else escalations
    seconds = trials * local_s + capped * cloud_s
    source = f"{len(mine)} earlier trial(s) of {args.model}" if mine else \
        f"no earlier results for {args.model} - assuming {FALLBACK_STAGE_SECONDS}s/stage and 30% parked"
    print(f"{len(tasks)} task(s) x {args.trials} trial(s) = {trials} trials")
    print(f"basis: {source}")
    print(f"median local stage {local_s:.0f}s, park rate {park_rate:.0%}")
    if escalations:
        print(f"expected escalations ~{escalations} with {args.escalate}"
              + (f" (capped at {args.max_escalations}: {escalations - capped} would be skipped)"
                 if capped < escalations else ""))
    print(f"estimated wall time ~{seconds / 3600:.1f} h")
    return 0


# ---- report -------------------------------------------------------------------

def cmd_report(args) -> int:
    rows = results.load_many([Path(p) for p in args.files])
    if not rows:
        print("no results rows found", file=sys.stderr)
        return 1
    text = report.write(rows, Path(args.md) if args.md else None, Path(args.html) if args.html else None,
                        args.profile)
    if not args.md:
        print(text)
    for label, path in (("markdown", args.md), ("html", args.html)):
        if path:
            print(f"wrote {label}: {path}", file=sys.stderr)
    return 0


# ---- entry point --------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="leash", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--version", action="version", version=f"leash {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    def selection(p):
        p.add_argument("--bench", type=Path, default=default_bench(),
                       help="Directory containing tasks/ and fixtures/ (default: this repo, or $LEASH_BENCH)")
        p.add_argument("--tasks", help="Comma-separated task ids (default: all)")
        p.add_argument("--categories", help="Comma-separated categories (default: all)")

    p = sub.add_parser("selftest", help="Validate task graders against references and mutants")
    selection(p)
    p.set_defaults(func=cmd_selftest)

    p = sub.add_parser("tasks", help="List tasks")
    selection(p)
    p.set_defaults(func=cmd_tasks)

    p = sub.add_parser("run", help="Run the battery for one local model")
    selection(p)
    p.add_argument("--model", required=True, help="Ollama model name, e.g. qwen3-coder:30b")
    p.add_argument("--escalate", default=DEFAULT_ESCALATE,
                   help=f"Model that repairs parked work (default {DEFAULT_ESCALATE}): gemini:<model> "
                        f"or agy:<model> via the agy CLI, claude[:<model>], ollama:<model> for a second "
                        f"local model (no cloud involved), or none")
    p.add_argument("--trials", type=int, default=5, help="Trials per task (default 5)")
    p.add_argument("--max-escalations", type=int, default=None,
                   help="Cap on cloud escalations in this invocation (default: no cap)")
    p.add_argument("--out", help="Results JSONL (default results/<model>-<date>.jsonl); resumed if it exists")
    p.add_argument("--backend", default="lite", choices=["lite", "aider", "claude"],
                   help="forge backend for the doer. 'lite'/'aider' drive an Ollama model; "
                        "'claude' drives the Claude Code CLI, which with ANTHROPIC_BASE_URL set "
                        "to a local server (e.g. Strata) makes that server the doer")
    p.add_argument("--stage-timeout", type=float, default=DEFAULT_STAGE_TIMEOUT,
                   help="Seconds before a hung forge stage is killed and recorded as an error")
    p.add_argument("--max-retries", type=int, default=None, help="Passed to forge run")
    p.add_argument("--max-validation-retries", type=int, default=None, help="Passed to forge run")
    p.add_argument("--hard-validation-retries", type=int, default=None,
                   help="Passed to forge run: validation-retry budget for 'hard' items only")
    p.add_argument("--lite-hard-num-predict", type=int, default=None,
                   help="Passed to forge run: num_predict for 'hard' items only")
    p.add_argument("--lite-hard-budget-directive", action="store_true",
                   help="Passed to forge run: output-budget directive on 'hard' items only")
    p.add_argument("--lite-hard-think-off", action="store_true",
                   help="Passed to forge run: disable thinking mode on 'hard' items only")
    p.add_argument("--forge-cmd", default="forge", help="Command that runs forge (default: forge)")
    p.add_argument("--keep-alive", default="30m", help="Ollama keep_alive for the warm-up (default 30m)")
    p.add_argument("--no-warmup", action="store_true", help="Skip loading the model before trial 1")
    p.add_argument("--skip-selftest", action="store_true", help="Don't validate tasks first")
    p.add_argument("--fill-escalations", action="store_true",
                   help="Instead of new trials, complete escalations skipped earlier (budget/quota)")
    p.set_defaults(func=cmd_run)

    p = sub.add_parser("estimate", help="Estimate run time from earlier results")
    selection(p)
    p.add_argument("--model", required=True)
    p.add_argument("--trials", type=int, default=5)
    p.add_argument("--escalate", default=DEFAULT_ESCALATE, help="none to estimate without escalation")
    p.add_argument("--max-escalations", type=int, default=None)
    p.add_argument("--out", help="Results file the run would write (used as history if it exists)")
    p.add_argument("--from", dest="from_results", nargs="*", help="Earlier results files to base timings on")
    p.set_defaults(func=cmd_estimate)

    p = sub.add_parser("report", help="Build a report from results files")
    p.add_argument("files", nargs="+")
    p.add_argument("--profile", default="uniform-v1")
    p.add_argument("--md", help="Write markdown here instead of stdout")
    p.add_argument("--html", help="Also write a self-contained HTML report here")
    p.set_defaults(func=cmd_report)

    sabotage_cli.add_parser(sub)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except TaskError as e:
        print(f"leash: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
