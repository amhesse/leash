# 07 - Forge assets to reuse

What already exists in `~/projects/forge` (as of 2026-09-14) that Leash
builds on.

## Measurement

- **`src/forge/calibrate.py`** - the prototype harness. Per (model, item,
  trial): fresh git copy of `bench/fixture/`, one-item checklist, real
  `forge run` subprocess, hidden grader run against the result *and* against
  the parked branch. Produces the four outcomes (`pass`, `silent_wrong`,
  `parked_ok`, `parked`). Appends JSONL one trial at a time (resumable).
  Current safety rule: `SAFE_PASS_RATE = 0.8` with zero `silent_wrong` -
  to be replaced by Wilson bounds / Leash levels.
- **`signals()`** in calibrate - task routing signals forge can see: TDD,
  number of named files, exact-content spec, `estimate_difficulty()` tier.
- **`bench/`**
  - `fixture/ledger` + `fixture/tests` - one Python fixture repo
  - `graders/` - 13 hidden graders: `add_currency_field`,
    `add_method_single`, `algorithm_single`, `bugfix_from_symptom`,
    `bugfix_negative_fraction`, `exact_new_file`,
    `exact_replace_function_file`, `feature_single_dates`,
    `multi_file_cli_flag`, `rename_across_files`, `small_edit_single`,
    `split_evenly_signed`, `tdd_average_transaction`
  - `items.toml` - task definitions and categories
  - `reference/` - reference solutions (basis for grader validation)
- **Existing data** (repo root): `calibration.jsonl` (60 trials),
  `calibration-before-pathfix.jsonl` (60), `calibration-v2.jsonl` (84).
  Note the "before path fix" file: a harness bug once distorted results -
  exactly why harness version must be recorded per trial.
- **`src/forge/eval.py`** - forge's regression suite against stub editors;
  model for testing adapters without real models.

## Harness behaviour worth documenting in the methodology

The checks that decide merged vs. parked (from forge's README), in order:
editor crash/retry and restore of unnamed files; byte-exact content match;
named files touched; prompt leakage; garbage filenames; syntax + project
validate commands; TDD red-then-green with byte-identical test file; optional
second-model review. A "harness check configuration" in Leash = which of
these ran, with which settings.

## Known lessons from forge's history (seed material for mutants and report)

- Multi-line checklist items were once silently truncated to their first
  line - failures blamed on models were a parsing bug. (Harness bugs
  masquerade as model failures → grader + harness validation.)
- A TDD item merged a wrong implementation that passed its own narrow
  self-written test (`tdd_budget`: summed both signs). → classic
  `silent_wrong` mutant; motivates the TDD-aware review prompt.
- A TDD item used `entry.amount` where the real field was `.cents` and
  merged before review was wired into the TDD path.
- Claude reviews put APPROVE at the end, not the start; naive first-line
  parsing escalated correct work. (Parser robustness matters for any
  model-judged step.)
- A stale hardcoded review model (`claude-3-7-sonnet`) parked every item as
  needs-review - an infrastructure failure that must count as `error`, not a
  model outcome.

## Related memory

Model selection next step noted in forge memory: test `qwen3-coder:30b` vs
14B with `forge calibrate`, prioritising accuracy over speed - a natural first
experiment to rerun under Leash methodology.

## Added to forge for Leash (2026-09-14)

- `forge run --snapshot-first-attempt` - pins the first successful editor attempt
  at `refs/leash/first-attempt/<branch>` (and in the run record as
  `first_attempt_commit`) before any check, restore or retry; also after the TDD
  green phase. Powers the `unchecked` condition.
- `forge run --repair-from REV --repair-note FILE` - starts an item from a parked
  attempt and asks the editor to fix it, while every check still diffs against
  the original base. Powers repair escalation.
- `--backend claude` is now accepted on the command line (it was only reachable
  through config or `--fallback-backend`).
- `--backend agy` / `--fallback-backend agy` - new `forge/agy_editor.py`, editing
  through the agy CLI (Gemini models). Leash's default escalation. Note: agy's
  `--print` consumes the next argument, so it must be the last flag.
- Tests: `forge/tests/test_leash_hooks.py` (stub-aider end to end).
- `forge calibrate` is superseded by `leash run` but left in place.
