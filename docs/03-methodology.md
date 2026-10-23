# 03 - Methodology

Design of the benchmark battery. v1 (`leash run`, see
[08 - Runner design](08-runner-design.md)) has 14 tasks ported from forge's
bench, one Python fixture and 29 mutants - enough to exercise the pipeline, not
enough to publish. Everything below is what "credible" requires.

## Unit of measurement

A **trial** = one (model, harness configuration, task, repetition). Each
trial runs in isolation: a fresh git copy of the task's fixture repo, the
task handed to the agent through an adapter, then graders run on the result.

## Outcomes

| Outcome | Merged by harness? | Hidden grader says correct? | Meaning |
|---|---|---|---|
| `pass` | yes | yes | Delegation worked |
| `silent_wrong` | yes | **no** | Safety net missed it - **the trust-killer** |
| `parked_ok` | no | yes | False alarm - costs review time, not trust |
| `parked` | no | no | Safety net did its job |

Plus infrastructure outcomes that are **excluded** from scores but reported:
`error` (harness crash, timeout, model unavailable). A trial is re-run, not
scored, on infrastructure failure.

## Conditions

Every trial is measured under three **conditions**, all from the same attempt
(the cascade - details in [08](08-runner-design.md)):

| Condition | Graded | Meaning |
|---|---|---|
| `unchecked` | the model's first attempt, before any check or retry | Raw output, no safety net: anything it commits counts as merged |
| `checked` | what the harness merged, or the branch it parked | Behind automated checks - **the headline** |
| `escalated` | checked, plus a cloud model repairing parked work | The local + cloud system |

`unchecked` replaces the earlier idea of a separate "raw commit-everything
adapter": the same attempt, graded before the harness touches it, so the
difference between conditions is a paired comparison.

Terminology: *conditions* are how a trial was run. *Leash levels* (Supervised,
Short leash, Long leash, Off leash) are **results** assigned per category - "long
leash" never names a condition.

## Task design

- **Scale target:** 60-150 tasks across ~10 task shapes, ≥3 fixture repos in
  different languages (Python, TypeScript, Go to start).
- **Task shapes (categories), initial list:**
  `exact-spec`, `small-edit`, `add-method`, `feature-single-file`,
  `bugfix-from-symptom`, `multi-file`, `rename-across-files`, `tdd`,
  `algorithm`, `config/infra`, `dependency-upgrade`.
- **Signals** recorded per task (so routing can use them): TDD or not,
  number of named files, exact-content spec present, estimated difficulty
  tier, fixture language, diff size of the reference solution.
- **Public vs. private split:** publish ~30% of tasks with graders; keep the
  rest private and rotate new ones in. Never publish private graders.

### Task directory format (proposed)

```
tasks/<task-id>/
  task.md            # the instruction exactly as the agent sees it
  meta.toml          # id, category, fixture, language, signals, visibility
  grader.py          # hidden grader: exit 0 = correct; stdout = reason
  reference.patch    # a known-correct solution
  mutants/*.patch    # known-wrong solutions (for grader validation)
fixtures/<fixture-id>/   # the starting repo, with its own visible tests
```

## Grader validation (non-negotiable)

Every grader must, automatically and in CI:

1. **Pass** the fixture + `reference.patch`.
2. **Fail** the untouched fixture (the task isn't already solved).
3. **Fail** every mutant in `mutants/` - plausible wrong solutions
   (off-by-one, wrong sign, wrong field, partial implementation, test
   edited instead of code).

A grader that can't kill its mutants is too lenient and manufactures fake
passes. Mutants are cheap to collect: real `silent_wrong` results from past
runs are the best mutants there are.

## Agent adapters

One interface, so any agent can be measured:

```
adapter.run(checkout: Path, task: str, config: dict) -> AdapterResult
  # AdapterResult: merged: bool, commit: str | None, parked_branch: str | None,
  #                tokens, seconds, log_tail
```

Initial adapters: forge (lite / aider / claude backends), aider, Claude Code
CLI, Codex CLI, OpenHands. Measuring the same models across harnesses
isolates **model** effects from **harness** effects - rarely published, and
a key differentiator.

## Metadata recorded per trial (reproducibility)

- model name, **digest/hash**, quantization, provider (ollama / API / CLI)
- runtime version (Ollama version, CLI version), context size, sampling params
- hardware (GPU, VRAM), host OS
- harness + adapter version, harness **check configuration**
- leashbench commit, task id + task content hash, grader hash
- timestamps, seconds, prompt/completion tokens, energy estimate (GPU power
  sampling) where available
- outcome, grader output, harness log tail

Results: one JSONL row per trial; resumable (skip finished trials); a report
generator builds tables from JSONL, never from memory.

## Statistics

- **Always report intervals.** Use Wilson score intervals (95%, z = 1.96).
  Point estimates alone are not published.
- **Zero is not zero.** 0 silent_wrong in n trials bounds the true rate only
  at roughly `z² / (n + z²)`:

  | Trials with 0 silent_wrong | 95% upper bound |
  |---|---|
  | 30 | 11.4% |
  | 35 | 10% |
  | 73 | 5% |
  | 188 | 2% |

  So claims like "≤5% silent-wrong on this category" need ~73 clean trials
  *in that category*. Thresholds directly set the trial budget.
- **Minimum evidence:** below a minimum trial count per category (proposed
  30), report "insufficient data" rather than a score.
- **Repetitions:** ≥5 per (model, harness, task) for variance; more for
  categories near a threshold.
- **Sampling:** fixed temperature/seed where the provider allows; record
  when it doesn't.

## Separately reported efficiency metrics

Not folded into the Leash Score, reported alongside it:

- median seconds per task, tokens per task, energy per task
- **friction rate** = `parked_ok / (pass + parked_ok)` - how often correct
  work is rejected (review cost)
- **catch rate** = `parked / (parked + silent_wrong)` - how often the harness
  catches wrong work (harness quality)
- **harness lift** = Leash Score (`checked`) − raw score (`unchecked`)
- **escalation lift** = system score (`escalated`) − Leash Score (`checked`)
- escalation rate, **rescue rate** (cloud passes ÷ escalations run), cloud
  silent wrongs, cloud seconds and tokens per escalation
