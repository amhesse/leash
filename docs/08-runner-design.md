# 08 - Runner design (`leash run` → `leash report`)

Written 2026-09-14, alongside the v1 implementation. How one command turns
a loaded local model into a Leash report, and the rules behind each number.

## Commands

```
leash selftest [--tasks ids] [--categories c]      # graders vs references and mutants
leash tasks                                          # list tasks, categories, signals
leash estimate --model M [--escalate E] [--from results.jsonl ...]
leash run --model M [--escalate gemini:<model>|claude[:model]|none] [--trials 5] [--max-escalations N]
          [--tasks ...] [--out results/x.jsonl] [--fill-escalations]
leash report results/*.jsonl [--profile uniform-v1] [--md out.md] [--html out.html]
```

Run from the repo with `PYTHONPATH=src python3 -m leash ...`, or install with
`pipx install -e .` for a `leash` command. Stdlib only; needs `forge` (with the
benchmark hooks), `git`, Ollama, and the escalation CLI (`agy` by default, or `claude`).

## Who does what in a trial

Only **one model is under test** - the local model given as `--model`. No other
model is involved in `unchecked` or `checked`:

- `unchecked`: the model's own first attempt, graded as-is.
- `checked`: the same model inside forge's **deterministic** checks - exact
  content, touched files, prompt leakage, garbage filenames, syntax and the
  fixture's test suite - with forge feeding validation failures back to the
  **same model** for its retries. forge's optional second-model review is
  **off** (`harness.review = null`); a reviewer model would be a different
  harness configuration, and would get its own score.
- `escalated`: one cloud model, repairing only work that forge parked. Default
  **`gemini:gemini-3.8-flash-high`**, run through forge's `agy` backend (the agy
  CLI; `agy models` lists ids). `--escalate claude[:model]` uses Claude instead,
  `--escalate none` disables the condition. One escalation model per results
  file; comparing escalation models means one run each (the local conditions
  are re-measured, which also adds trials).

## Conditions

"Long leash" etc. are **results** (Leash levels, see [04](04-leash-score.md)).
The conditions a trial is measured under are:

| Condition | What is graded | Question it answers |
|---|---|---|
| `unchecked` | the model's first successful attempt, before any check, restore or retry | How often is raw output right? |
| `checked` | what forge merged, or the branch it parked | How safe is it behind automated checks? (**headline**) |
| `escalated` | checked, plus a cloud model repairing anything parked | How good is the local + cloud system? |

## The cascade: one trial, three outcomes

```
fixture copy + one-item TODO.md, committed as base
  │
  ▼
forge run --backend lite --models M --snapshot-first-attempt --keep-branches --max-items 1
  │   ├─ first successful editor attempt pinned at refs/leash/first-attempt/<branch>
  │   └─ checks, validation retries → merged [x] or parked [!]/[?]
  │
  ├─► UNCHECKED  grade(snapshot)                → pass | silent_wrong
  ├─► CHECKED    merged ? grade(HEAD) : grade(parked branch)
  │                                             → pass | silent_wrong | parked_ok | parked
  └─► ESCALATED
        merged locally        → same as CHECKED (resolved_by: local)
        parked, budget left   → reopen TODO item; write repair note from forge's record;
                                forge run --backend agy|claude [--models X]
                                          --repair-from <parked branch> --repair-note <file>
                                → pass (cloud) | silent_wrong (cloud_wrong) | parked_ok | parked
        parked, no budget     → CHECKED outcome, flagged skipped; git bundle saved
        cloud infra error     → CHECKED outcome, flagged error
```

Measuring all three on the **same attempt** makes harness lift and escalation
lift paired comparisons, and costs one local generation instead of three.

### Outcome rules and edge cases

- **Unchecked with no snapshot** (the editor never produced a usable attempt):
  grade the parked branch tip if it has commits, otherwise the base. An
  unwatched system would have "merged" nothing - wrong and unnoticed, so
  `silent_wrong`. `conditions.unchecked.source` records `snapshot` /
  `branch_tip` / `base`.
- **Skipped or failed escalations count as the checked outcome** (still
  parked). Dropping them would drop only parked trials and inflate the system
  score; counting them conservatively can only understate it. The report
  shows how many were skipped or failed.
- **TDD items in repair mode** take forge's single-pass path with both files
  named; the project's validate commands still run the tests. Red/green is not
  replayed on top of an attempt that already wrote the test.
- **Correct = hidden grader AND fixture's visible tests pass.** The grader is
  copied in only while grading and never committed.

### Repair mode (forge `--repair-from`)

The item's worktree is reset to the parked branch, but forge keeps `base` as
the original fixture commit, so every check (touched files, exact content,
restore of unnamed files) judges the *whole* change, not just the fix. The
editor prompt is the task, then why the attempt was rejected (forge's reason,
validation output, review feedback), then "fix it; keep what's correct".

## Infrastructure errors (never scored)

Classified from forge's own log lines and record, only when the editor never
succeeded (forge retries - an error followed by a good attempt is a real result):

| Kind | Trigger | Effect |
|---|---|---|
| `stage_timeout` | stage exceeded `--stage-timeout` (process group killed) | row status `error` (local) / escalation error |
| `harness_preflight` | forge refused to start (no checklist, not git, dirty tree) | as above |
| `forge_failed` | non-zero exit or no run record | as above |
| `ollama_unreachable` | `[lite_editor] could not reach ollama` | local trial → `error`, reruns on resume |
| `cloud_cli_missing` | `agy CLI not found` / `claude CLI not found` | escalation error; **stops escalations** |
| `cloud_quota` | agy/claude error line mentioning quota, limits, 429, overloaded | escalation error; **stops escalations** |
| `cloud_timeout`, `cloud_error` | other agy/claude failures | escalation error |

## Results schema (JSONL, one row per trial, `schema = 1`)

```
schema, run_id, leash_version, spec_version, status ("ok" | "error"),
task_id, category, task_hash, signals{tdd, files, exact}, trial, started, finished,
model{name, provider, digest, quantization, parameter_size, family, context_length,
      size_bytes, load_seconds, runtime{ollama_version}},
harness{adapter, backend, max_retries, max_validation_retries, review, escalation_mode, hash,
        forge{version, commit, dirty, path}},
cloud{engine, model, cli_version, available} | null,
hardware{host_os, python, gpus[{name, vram_mb, driver}]},
local{seconds, tokens, marker, status, reason, branch, first_attempt_commit,
      forge_expected_files, touched_files, validation_retries, editor_attempts, error, log_tail},
conditions{unchecked{outcome, grader_output, source}, checked{outcome, grader_output},
           escalated{outcome, grader_output, resolved_by, fallback?}},
escalation{status: disabled|not_needed|skipped|done|error, model, seconds, tokens, marker,
           reason, resolved_by, error, repair_note, bundle?, parked_branch?, filled?},
errors[{stage, kind}]
```

## Resume, budget, scheduling

- **Resume key** = (model digest, harness config hash, cloud model, task hash,
  trial). Re-running the same command skips completed keys. `error` rows are
  not complete and rerun. Later rows supersede earlier ones for the same key.
- **Round-robin order:** trial 1 of every task, then trial 2, ... so a partial
  run is balanced across categories.
- **Budget:** `--max-escalations` caps cloud escalations per invocation. After
  the cap (or a quota / missing-CLI error), parked trials record
  `escalation.status = skipped` with a git bundle in `<out>.artifacts/`.
  `leash run ... --fill-escalations` later repairs those from the bundles and
  appends superseding rows.
- **Ctrl+C:** the in-flight trial is dropped (its forge process group killed),
  completed rows are already fsynced; rerun to resume.
- **Warm-up:** one Ollama generate with `keep_alive` before trial 1; load
  seconds recorded in `model.load_seconds`, not charged to a trial.

## Report sections

1. Summary table across result groups (model digest × harness × cloud model).
2. Per group: metadata (model, digest, quantization, runtime, GPU, harness +
   forge commit/dirty, cloud CLI, dates, trial/error counts).
3. Scores: Leash (checked), raw (unchecked), system (escalated), harness lift,
   escalation lift.
4. Per-category tables for each condition: weight, n, the four outcomes,
   P_lo, S_hi, score (or *insufficient*), level.
5. Escalation: needed / run / skipped / failed, rescue rate, cloud silent
   wrongs, median cloud seconds and tokens.
6. Efficiency: median local seconds and tokens, friction rate, catch rate.
7. Per-task outcome counts per condition.
8. Every silent wrong, grouped per trial, with the grader's failure.
9. Infrastructure errors by kind; limitations (including thin categories).

## Adding a task

1. `tasks/<id>/task.md` - the instruction as the agent sees it.
2. `tasks/<id>/meta.toml` - `id`, `category`, `fixture`, `language`,
   `visibility`, and a `[mutants]` table `name = "what's wrong with it"`.
3. `tasks/<id>/grader.py` - exits 0 only for a correct solution; runs from the
   checkout root.
4. `tasks/<id>/reference/` - files overlaid on the fixture to make it correct.
5. `tasks/<id>/mutants/<name>/` - overlays of plausible wrong solutions. Real
   `silent_wrong` results are the best source.
6. `leash selftest --tasks <id>` must pass before `leash run` will use it.

## Known limitations of v1

- One fixture (Python `ledger`), 14 tasks, 6 categories - far below the 30
  trials per category needed for any category to score; a full battery at 5
  trials is a smoke test of the pipeline, not a publishable result.
- Only forge as the harness and `lite` / `aider` as local backends; escalation
  through `agy` (Gemini, default) or `claude`.
- Gemini through `agy` loads a large agent context: a trivial repair measured
  ~249k prompt tokens and ~50 s, against ~53k and ~13 s for Claude Opus.
- No energy measurement yet.
