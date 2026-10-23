# Forge vs. Aider: a fair, native head-to-head

Status: **PHASES 1, 2, AND 4 ALL DONE.** Written 2026-09-22, updated
2026-09-25. Full write-up with both internal (Phase 2) and external
(Phase 4) results: `docs/10-forge-vs-aider-writeup.md`.

**Real blocker hit and resolved:** aider needs a genuine Anthropic API key to
call Sonnet directly (it uses litellm, not the `claude` CLI's subscription
auth the way forge's own cloud backend does) - no such key is configured in
this environment. Options were: (a) get a real API key, (b) have aider's
Stage 2 shell out to the `claude` CLI instead (a real design compromise -
would no longer be "aider using its own mechanism"), or (c) run local-only
for now. **User chose (c).** Phase 2 is running local-only; the local+cloud
comparison this doc originally called "Phase 1" is deferred until an API
key is available - revisit the phase numbering below if that happens.

Phase 1 (build + validate `tools/aider_bench.py`) is DONE - see the bottom
of this doc for what was found. Phase 2 (full 3-model run) is RUNNING via
`results/aider-bench-battery.sh`, local-only, expect 10+ hours given
per-trial times of 21-654s observed on the smoke test.

## Goal

Produce credible, reproducible evidence comparing what Forge can do against
what Aider can do, at solving the same coding tasks — specifically to make
the case that people should switch to Forge. The evidence has to survive
scrutiny from a skeptical engineer, not just look good in a bar chart.

## The one rule that shapes everything else

**Do not use `leash run --backend aider`.** That runs the real aider CLI
*inside forge's own orchestration loop* (forge's retry counts, forge's task
materialization, forge's decision about when to give up) — that's a fair way
to compare two *editors* under one harness, but it is not "aider at its
fullest capability." Aider has its own repair loop, its own test-driven
auto-fix behavior (`--auto-test`, `--test-cmd`), its own conventions. To make
a claim that will hold up, both tools need to run *as themselves*, doing
whatever they'd normally do, graded by the same yardstick at the end.

- **Forge** runs exactly as it does throughout the rest of this project:
  `leash run --model <doer> --escalate <engine> ...`. This already *is*
  forge at full capability — checks, same-model retries, park-on-failure,
  optional cloud escalation. No new code needed on this side.
- **Aider** needs a new, independent runner (Phase 1 below) that drives the
  real `aider` CLI directly against the same task fixtures, using aider's
  own mechanisms, then grades the result with the *same* task checks Leash
  already uses (reused as a library, not reimplemented) — never through
  forge's `runner.py`.

## Defining outcomes for Aider (parity with Leash's pass / silent_wrong / parked)

Aider has no native concept of "parking" a task for human/cloud review — it
either converges to something it thinks is right, or it errors out. The
wrapper has to infer the equivalent bucket from aider's actual behavior:

- **pass** — final worktree state passes the task's checks.
- **silent_wrong** — aider exits normally / reports success (a clean commit,
  no error), but the checks fail. This is the number that matters most:
  it's a case where aider *thought* it succeeded and didn't.
- **parked-equivalent** — aider's own retry budget (`--auto-test` re-invokes
  itself against `--test-cmd` failures) is exhausted without a passing
  state, and it exits with an error / no commit rather than confidently
  finishing. Detect this from aider's exit code and whether a commit
  landed — document the exact heuristic in the wrapper's code comments once
  built, since this is an interpretive judgment call the raw tool doesn't
  make explicit, and it needs to be auditable.

## "Full capability" definition, local+cloud phase (this phase, not all-local)

Forge already has a well-established local+cloud shape from this project:
local doer model, escalate to `claude:claude-sonnet-5` when parked. Aider
needs a comparable two-stage design that stays within "aider doing its own
thing" — no forge orchestration smuggled in:

- **Stage 1 (local):** `aider --model ollama/<doer> --test-cmd "<task's real
  check command>" --auto-test --yes-always --no-git-commit-verify --message
  "<task prompt>" --exit`, run against the task's materialized fixture.
  Aider uses its own auto-test loop to retry against real failures on its
  own terms.
- **Stage 2 (cloud repair, only if Stage 1's final state still fails
  checks):** re-invoke aider on the *same* worktree, now pointed at
  `--model claude-sonnet-5`, handing it the current (failing) state plus the
  actual failure output as the message — aider repairing its own local
  attempt with a stronger model. This is the closest aider-native analog to
  forge's `--repair-from`, built by just running aider again, not by
  borrowing forge's escalation code.

Retry-budget parity: forge's defaults are `--max-retries 2
--max-validation-retries 1` (this session found `--max-validation-retries 8`
is a real sweet spot for at least one local model). Aider's `--auto-test` retry count should be set to a
documented, comparable value — pick one number and state it plainly in the
results write-up rather than silently using whatever aider's default is.

## Model selection, first pass: 3 models

Pick models that already have full forge-side local+Sonnet data in this
project, so the new Aider numbers are being compared against a real,
existing bar rather than requiring new forge runs too:

1. **qwen3.8:27b** — the most-repeated forge datapoint (checked 22.9–26.6
   across runs, +Sonnet 26.2→28.8). Best baseline for statistical footing.
2. **muse-glimmer:30b** — current forge checked-only leader (27.1,
   +Sonnet 26.8→28.4, 100% catch rate). Tests whether forge's advantage
   holds at the top of the quality range.
3. **qwen2.5-coder:14b** — deliberately weaker (checked 10.4–10.5,
   +Sonnet 10.5→10.6). Tests whether forge's safety-net advantage is
   *bigger* on weaker models — the more interesting and more persuasive
   claim if true ("forge matters most exactly when you need it most").

Expand the model list later once this batch is validated; don't start wider
than 3 or the aider-wrapper's correctness can't be checked by hand first.

## Token tracking: split local vs. cloud, per trial

Every trial (both tools) records two token buckets, matching the shape
Leash's `results.jsonl` already uses per stage:

- `local_tokens` — every token from on-box model calls (forge's `lite`
  editor local calls; aider's Stage-1 local-model calls, including any
  auto-test retry iterations).
- `cloud_tokens` — every token from any Sonnet call (forge's escalation;
  aider's Stage-2 repair call).

Aider reports token usage in its own verbose/JSON output per message; the
wrapper needs to parse and accumulate this the same way `leash`'s adapter
already accumulates forge's per-stage token counts. Also record, per model,
the count of trials that needed Stage 2 at all (forge already calls this
"escalations needed") so **tokens-per-correctly-solved-task** is comparable
between tools, not just tokens-per-trial — this is the actual cost argument
from the persuasion discussion, and it only works if this is tracked
consistently.

## Output format

New JSONL files, schema-compatible with Leash's existing results rows where
possible (so `leash report` can read them), with an explicit
`"harness": {"adapter": "aider-native", ...}` tag so they're never confused
with forge-adapter rows. Check `report.py`'s assumptions before assuming
compatibility — if it doesn't fit cleanly, a small parallel report generator
is fine, but keep the row shape close enough that a human can diff the two.

## Deliverables

- `tools/aider_bench.py` (or similar) — the new standalone wrapper. Imports
  Leash's existing task-loading and grading code as a library; never touches
  `forge/src/forge/runner.py`.
- New results files: `results/aider-native-<model>-local-cloud.jsonl` per
  model.
- A head-to-head write-up (own artifact section, or a standalone doc) with:
  the Leash-Score-equivalent comparison, the outcome-shape breakdown
  (pass/silent_wrong/parked-equivalent), tokens-per-solved-task, and 2-3
  annotated failure-transcript pairs (same task, same model, aider went
  silent-wrong / forge parked or self-corrected) — these are the most
  shareable artifact from the whole exercise, pull them deliberately.

## Phased sequencing

- **Phase 0 (this doc):** plan only. Done.
- **Phase 1:** build `aider_bench.py`, validate on a tiny slice (1 trial ×
  14 tasks × 1 model) by hand-checking a few outcomes before trusting the
  wrapper's pass/silent_wrong/parked classification.
- **Phase 2:** full local+cloud run, 3 models × 15 trials × 14 tasks each
  (630 new Aider-side trials; forge's side already exists). Consider 5
  trials/task first if Phase 1 surfaces anything that needs iterating on.
- **Phase 3 (deferred, explicitly later):** all-local variant for both
  tools (no Stage 2 / no escalation) — same shape as this project's
  existing all-local batteries. Do this only after Phase 2 is solid.
- **Phase 4 (stretch, highest external credibility): DONE.** Ran Forge
  against 8 problems imported directly from Aider-AI/polyglot-benchmark
  (`tools/polyglot_import.py`), the exact repo Aider's own leaderboard
  scores against. Result: forge 20.0% pass / 0% silent-wrong / 80.0%
  parked; aider 73.3% pass / 26.7% silent-wrong / 0% parked - the same
  mechanism gap, at full statistical weight, on a benchmark neither tool
  was tuned against. Full result in `docs/10-forge-vs-aider-writeup.md`.

## The caveat to state plainly in any published result, always

Even after moving off forge's internal `--backend` switch, **the tasks
themselves are still Leash's own tasks**, and forge's `lite_editor` was
iteratively tuned against this exact task set (see `forge/calibration.jsonl`
/ `calibration-v2.jsonl` from forge's own development history) — aider was
never tuned against them. A forge win here is real evidence, but it should
be framed as *"forge outperforms aider on this benchmark"*, not *"forge is
a more capable editor in general"* — Phase 4 is the way to actually earn the
broader claim. Say this in the write-up before anyone else has to point it
out.


---

## Phase 1 result log (2026-09-23)

Built `tools/aider_bench.py`. Reuses `leash.tasks`/`leash.fixtures`/
`leash.grading` as a library (never touches forge). Validate-command
parity confirmed directly from the fixture's own `.aiderloop.toml`:
`python -m unittest discover -s tests -q` - the exact same target forge's
own retry loop uses, read from the fixture rather than hardcoded, so any
future fixture with a different validate command stays correct
automatically. Aider invoked via `aider --yes-always --no-gitignore
--no-stream --no-restore-chat-history --edit-format diff --auto-test
--test-cmd "<the above>" --model ollama/<model> --message <task prompt>`.
Token usage parsed from aider's own "Tokens: N sent, M received" stdout
line via a regex copied from forge's `runner.py` (not imported - forge
lives in its own pipx venv, this script needs to stay independently
runnable).

Smoke test: qwen3.8:27b, 1 trial x 14 tasks, local-only. Result: 14/14
ran clean (no wrapper crashes), 11 pass, 3 silent_wrong
(`exact_replace_function_file`, `rename_across_files`,
`tdd_average_transaction`) - real, sensible signal, not wrapper noise.
Zero "parked" outcomes at this trial count (aider always exited claiming
success, right or wrong, this time - worth watching whether "parked"
shows up at all once there's more trials, since it's aider's error-exit
path, which may simply be rare for this model). Per-trial time ranged
21.2s-653.8s (that longest one was the TDD budget task, consistent with
TDD being the slow/hard category throughout this whole project on every
tool tested).

## Phase 2: RUNNING as of 2026-09-23 22:09

Local-only, 3 models, sequential (fastest first): qwen2.5-coder:14b,
qwen3.8:27b, muse-glimmer:30b - 210 trials each (630 total). Script:
`results/aider-bench-battery.sh`. Log: `results/aider-bench-battery.log`.
Out files: `results/aider-native-<model>-local.jsonl`. Launched via
nohup + disown.

**IF THIS SESSION ENDS BEFORE THIS FINISHES:** check
`results/aider-bench-battery.log` for `AIDER-BENCH BATTERY COMPLETE`. If
missing, re-run `results/aider-bench-battery.sh` (recreate from this
description, or from `tools/aider_bench.py --help`, if the script itself
is gone) - `tools/aider_bench.py` resumes safely per-model from its own
`--out` file (same completed-key logic as leash's own runner). When done:
compare each model's aider-native local-only outcome-shape
(pass/silent_wrong/parked counts) against forge's existing checked-only
numbers for the same model (qwen2.5-coder:14b: 10.4-10.5; qwen3.8:27b:
22.9-26.6; muse-glimmer:30b: 27.1) - this is the first real forge-vs-aider
data point in the whole project. Revisit the local+cloud phase once an
Anthropic API key is available for aider.


---

## Phase 2 final result log (2026-09-24)

All 3 models complete, 630/630 trials, 0 wrapper errors.

| model | pass | silent_wrong | parked | tdd sw rate | non-tdd sw rate |
|---|---|---|---|---|---|
| qwen2.5-coder:14b | 140 (66.7%) | 70 (33.3%) | 0 | 100% | 22.2% |
| qwen3.8:27b | 135 (64.3%) | 75 (35.7%) | 0 | 100% | 25.0% |
| muse-glimmer:30b | 180 (85.7%) | 30 (14.3%) | 0 | 100% | 0% |

**Headline finding: model quality explains the non-TDD gap (tracks each
model's known general capability) but explains nothing about TDD, which
is 100% silent-wrong on all three models without exception.** That
flatness is the signature of a mechanism gap, not a capability gap -
aider has no equivalent of forge's checked/retry/park loop, so a model
that "isn't sure" always commits its best guess as final rather than
flagging it. Zero parked outcomes anywhere across all 630 trials.

muse-glimmer:30b is perfect on every non-TDD category under aider (100%
pass on all five), matching its flawless forge-side record and resolving
the qwen3.8:27b exact-spec anomaly (50% silent-wrong there) as
model-dependent, not a fixed aider/edit-format issue with that category.

Given the API-key decision above, this run ended up covering both the
originally-separate Phase 2 (full run) and Phase 3 (all-local variant) at
once, since local-only was the only viable path without cloud access -
worth noting if the phase numbering is revisited later.

**DONE - see `docs/10-forge-vs-aider-writeup.md`.** (Historical note, was:) the write-up deliverable (2-3 annotated
failure-transcript pairs, same task/model, aider silent-wrong vs. forge
parked/self-corrected). Raw material is ready -
`results/aider-native-*.jsonl`, each row carries a `log_tail` with
aider's actual last-4000-chars output. Ask before building this - it's a
curation/writing task, not another run.

Phase 4 (test forge against aider's own published benchmark) is DONE -
see the Phase 4 result log below and `docs/10-forge-vs-aider-writeup.md`.


---

## Phase 4 result log (2026-09-24 to 2026-09-25)

Built `tools/polyglot_import.py`: imports Exercism Python-track problems
from Aider-AI/polyglot-benchmark into a new, separate Leash bench
(`benches/polyglot-subset`, gitignored - regenerate via the importer
against a fresh clone). 8 problems: transpose, phone-number, proverb,
wordy, grade-school, book-store, bowling, list-ops (all single-file, no
external deps).

Two real setup bugs found and fixed, not tuning-for-forge:
1. Forge's preflight rules refuse any task with a fenced code block not
   preceded by "exactly" - a real safety feature Exercism's instructions
   trip since they use illustrative fences freely. Fixed by converting
   fences to plain indented text on import (content-neutral, identical
   for both tools).
2. Without an `.aiderloop.toml`, forge silently fell back to a
   syntax-only validate check instead of running the real test suite,
   producing false "passed and merged" results on the first smoke test
   (code returning `None` everywhere). Fixed by writing a real
   `.aiderloop.toml` per fixture pointing at the actual test command.

Final result, 240 trials (120 forge + 120 aider-native), qwen3.8:27b,
local-only, 0 errors either side:

| metric | forge | aider |
|---|---|---|
| pass | 24 (20.0%) | 88 (73.3%) |
| silent-wrong | 0 (0%) | 32 (26.7%) |
| parked | 96 (80.0%) | 0 (0%) |

Same finding as the internal (Phase 2) comparison, same magnitude of
safety asymmetry, on a benchmark neither tool has ever seen. Aider is
genuinely more capable here (73.3% vs 20.0% pass) but converts 100% of
its failures to silent-wrong; forge solves far less but never once ships
a wrong answer. `book-store` (15 trials each) is the cleanest single
pair: forge parked all 15 (project checkout untouched each time), aider
was silently wrong on all 15 (exited claiming success every time, the
real tests disagreed every time). Full write-up:
`docs/10-forge-vs-aider-writeup.md`.
