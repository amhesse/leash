# Forge vs. Aider: what a safety net actually buys you

A head-to-head comparison of Forge and Aider, each run at its own fullest
capability (not one tool run inside the other's harness — see the design
rationale in `docs/09-forge-vs-aider-benchmark.md`), on the same 14 coding
tasks, the same three models, graded by the same hidden checks. 630 aider
trials, 0 wrapper errors, local-only (no cloud escalation — see the caveat
at the end for why).

## The headline number

| Model | Aider: pass | Aider: silent-wrong | Aider: parked | TDD silent-wrong rate |
|---|---:|---:|---:|---:|
| qwen2.5-coder:14b | 140 (66.7%) | 70 (33.3%) | 0 | **100%** |
| qwen3.8:27b | 135 (64.3%) | 75 (35.7%) | 0 | **100%** |
| muse-glimmer:30b | 180 (85.7%) | 30 (14.3%) | 0 | **100%** |

Every one of forge's own runs on these same three models parks the large
majority of the TDD trials it can't solve — it almost never ships one
silently. Aider ships one **every single time**, on every model, including
the model that's otherwise perfect on every other category.

**Zero parked outcomes anywhere in 630 trials.** Aider never once gave up
honestly. It always committed something as its final answer.

## Why this is the right comparison to make

Model quality tracks the *non-TDD* gap almost exactly the way you'd expect
— the weakest model (qwen2.5-coder:14b) is wrong most often, the strongest
(muse-glimmer:30b) is perfect:

| Model | Non-TDD silent-wrong rate under Aider |
|---|---:|
| qwen2.5-coder:14b | 22.2% |
| qwen3.8:27b | 25.0% |
| muse-glimmer:30b | **0%** |

But TDD stays flat at 100% regardless. **That flatness is the signature of
a mechanism gap, not a capability gap.** The same model (muse-glimmer:30b)
that makes zero mistakes elsewhere still goes completely wrong on every
TDD trial — because TDD is exactly the category where "am I actually done"
requires running your own tests and being willing to admit you're not
sure. Forge's checked/retry/park loop does that. Aider has nothing
equivalent, so a model that isn't sure just ships its best guess.

> **Revised 2026-10-04: read the "Postscript" section at the end before
> quoting this paragraph.** A same-model experiment found that at least
> part of the TDD gap is caused by the task wording, not by forge's checks.
> Both TDD tasks say "implement X so `tests/test_Y.py` passes" and never
> say to write that test. forge's `TDD:` handling writes it anyway. An
> agent working without forge often reads the task as "the test already
> exists". The aider transcript below ("if tests/test_budget.py exists")
> fits that reading. The flatness at 100% is real; this paragraph's
> explanation for it is not established.

## Two annotated failures, same task, same model, same tasks — different tools

### 1. `tdd_budget`, qwen3.8:27b — the clean case

**Task:** implement `ledger/budget.py` so `tests/test_budget.py` passes.

**Forge (parked, honestly):**
```
reason: the new test passed before any implementation was written -
        it may not test the described behavior, or the behavior
        already exists
marker: [?]
touched: (nothing merged)
```
Forge's TDD red/green gate ran the rewritten test *before* any real
implementation existed, noticed it passed anyway, and refused to merge —
a precise, human-readable catch of a known failure mode (a struggling
model rewriting the test to trivially pass rather than implementing the
real logic). Nothing shipped. The item stayed open for escalation or a
human.

**Aider (silent-wrong, confidently):**
```
[qwen3.8:27b's own chain-of-thought, verbatim from aider's transcript]
Need maybe mention if tests/test_budget.py exists and you want me to
inspect/edit it, add it. But we don't need edit. Could say no other
files are needed for the requested change...

Final: No other files need to be added.

No other files need to be added.

Tokens: 12k sent, 1.4k received.
```
Aider's chat loop asked the model whether other files were needed; the
model talked itself into "no," aider treated that as a complete,
successful turn (exit code 0, no error, nothing flagged), and ended the
session. `ledger/budget.py` was never written. The hidden grader:
`ModuleNotFoundError: No module named 'ledger.budget'`. Aider has no step
that would have caught this — the model said something that sounded like
closure, and that was enough.

### 2. `exact_replace_function_file`, qwen3.8:27b — the messier case

**Task:** replace one function's body in `ledger/money.py`, exactly.

**Forge:** passed every check and was merged, touched exactly
`ledger/money.py`. Unremarkable — which is the point.

**Aider:** silent-wrong. The transcript shows the model's own reasoning
about SEARCH/REPLACE block formatting leaking into the response — real
back-and-forth about whether to match trailing whitespace, whether to
replace the whole file or just the changed function — followed by a
literal `[Errno 36] File name too long` error from aider trying to parse
part of the model's reasoning text as a file path. Aider recovered and
moved on without surfacing this as a failure. This category (`exact-spec`)
was a near-universal 100% pass for every model under forge all session;
under aider it hit 50% silent-wrong on this specific model — likely a
combination of qwen3.8:27b's verbose reasoning-style output interacting
badly with aider's SEARCH/REPLACE parsing, not a fundamental task
difficulty. Notably, this exact category was **0% silent-wrong** for
muse-glimmer:30b under the identical aider setup — confirming the gap here
is model-and-output-style dependent, not a fixed weakness of the category
or the tool.

## Methodology, briefly (full detail in `docs/09-forge-vs-aider-benchmark.md`)

- Aider driven directly via its own CLI (`--auto-test`, `--test-cmd`,
  `--yes-always`), never through `leash run --backend aider` — which would
  run aider inside forge's own orchestration instead of at its own fullest
  capability.
- Both tools validated against the exact same command
  (`python -m unittest discover -s tests -q`), read from each fixture's own
  config — the same target forge's own retry loop uses.
- Both tools graded by the same hidden grader, reused as a library, never
  shown to either tool during the attempt.
- **Local-only.** Aider needs a real Anthropic API key to reach Sonnet
  (it doesn't use the `claude` CLI's subscription auth the way forge's
  cloud backend does); none was configured, and the choice was made to run
  local-only rather than substitute a different mechanism for aider's
  cloud stage. The local+cloud comparison remains open for later.

## The caveat, stated plainly

Forge's `lite_editor` was iteratively tuned against this exact task set
over the project's development. Aider was never tuned against it. Read in
isolation, this section's result should be *"forge outperforms aider on
this benchmark,"* not *"forge is a more capable editor in general."* The
way to earn the broader claim was to run forge against a subset of
Aider's own published benchmark — see the Phase 4 section below, which
does exactly that and finds the same mechanism gap holds.

## What this is for

This is the evidence for the "why switch to forge" case: not a benchmark
score, but a demonstrated, reproducible, same-model, same-task difference
in what happens when a model isn't sure it's right. Forge notices. Aider
ships it anyway. Read the Phase 4 section below before treating this as
settled — it's the same finding again, on a benchmark forge never saw.


---

## Phase 4: the same result, on a benchmark neither tool has ever seen

Everything above uses Leash's own tasks — tasks Forge's `lite_editor` was
iteratively tuned against over this project's development. That's a real
caveat, stated plainly above. Phase 4 closes it: the same comparison,
run on 8 problems imported directly from
[`Aider-AI/polyglot-benchmark`](https://github.com/Aider-AI/polyglot-benchmark)
— the exact repository Aider's own team maintains and scores its published
leaderboard against (`transpose`, `phone-number`, `proverb`, `wordy`,
`grade-school`, `book-store`, `bowling`, `list-ops`, sourced from
Exercism's Python track). Forge has never seen these tasks. Neither has
Aider's editor been specifically tuned on them beyond whatever general
training the underlying model received — this is genuinely neutral ground.

### The result

240 trials, qwen3.8:27b, 15 trials × 8 tasks per tool, local-only, 0
wrapper errors on either side.

| Metric | Forge | Aider |
|---|---:|---:|
| Pass | 24 (20.0%) | **88 (73.3%)** |
| Silent-wrong | **0 (0%)** | 32 (26.7%) |
| Parked | 96 (80.0%) | 0 (0%) |

**Aider is genuinely more capable at solving these problems outright** —
73.3% vs 20.0% pass, a real gap, likely because its interactive chat loop
suits hard algorithmic problems (dynamic programming, parsing) better than
Forge's single-shot attempt. This is not a contest Forge wins on raw
correctness, and this write-up isn't going to pretend otherwise.

**But every one of Aider's failures is silent-wrong. Zero parked outcomes
across all 120 trials** — exactly matching the 0-in-630 precedent from the
internal comparison above. Forge solves far fewer outright, but has zero
silent-wrong across all 120 of its trials: every failure is a park, not a
guess.

### The clearest single pair: `book-store`, 15 trials each

Both tools ran this task (a dynamic-programming discount-optimization
problem) 15 times. The results are a clean, maximal contrast:

- **Forge: 15/15 parked.** Every attempt ended with the project checkout
  left untouched — "aider itself failed after 3 attempt(s)... The project
  checkout is untouched." Nothing wrong ever shipped, because nothing
  shipped at all when the implementation wasn't confirmed working.
- **Aider: 15/15 silent-wrong.** Trial 1's transcript shows the model
  working through multiple candidate algorithms in the open —
  *"Let's search memory: The optimal algorithm for Book Store (Exercism)
  often... Another known solution: ... Let's [cut off]"* — never
  converging with confidence, spending its full 545-second budget
  rambling between approaches. It still exited with code 0 (a clean,
  reported success) on every one of the 15 trials. The real test suite
  disagreed every time: `AssertionError: None != 5120` — an incomplete
  implementation, shipped as final, 15 times in a row, with nothing in
  Aider's own output ever flagging uncertainty.

Same model, same problem, same 15 attempts. One tool never shipped the
broken code. The other shipped it every single time and called it done
every single time.

### Why this matters more than the internal result alone

It closes the one real objection to everything above: *"you only win on
your own benchmark."* This result comes from the benchmark Aider's own
creators use to score themselves. The magnitude isn't smaller here — if
anything the safety gap is starker, because Aider's real capability
advantage on these harder problems makes its zero-parks behavior more
consequential, not less: a tool that's actually good at solving hard
problems, with no way to tell you when it isn't, is a more dangerous
combination to leave unattended than a weak tool that's also silent.

### Methodology note specific to Phase 4

Importing external tasks into Leash's format surfaced two real,
documented setup issues, fixed before any comparison was trusted (see
`docs/09-forge-vs-aider-benchmark.md` for the full detail): Forge's own
preflight rules reject any task with an unmarked fenced code block
(Exercism's instructions use them freely for illustration; fixed by
converting them to plain indented text, applied identically for both
tools), and the imported fixtures needed an explicit `.aiderloop.toml`
pointing at the real test command, or Forge silently fell back to a
syntax-only check instead of actually validating against the hidden
tests. Both fixes are content-neutral — they make Forge's task-authoring
conventions work with imported content, they don't change what either
tool is being asked to do.

---

## Postscript (2026-10-04): the TDD gap is mostly wording

The TDD comparison above runs every task as written, so it cannot
separate what forge's checks contribute from what the task wording
contributes. Two runs on 2026-10-04 separated them. Both used **one
model throughout**: Strata serving `qwen3.8-flash-next-coder-iq1_m`,
driven by the Claude Code CLI through `ANTHROPIC_BASE_URL`.

**Run 1: an agent with a shell and no forge** (`tools/claude_bench.py`;
all 14 tasks x 15 = 210 trials). 206 passed and 4 were silent-wrong. All
four failures were on the two TDD tasks, and all four failed the same
way: the implementation was correct, but the test file was never written.
In one trial the agent said why: it had verified its work "rather than
adding a test file the grader would supply".

**Run 2: wording x harness** (`results/tdd-wording-2x2.sh`; 20 trials per
cell). The tasks `tdd_*_explicit` keep the same graders and references.
Only the wording changes: "first write a new test file, `tests/test_Y.py`
... The test file does not exist yet; writing it is part of the task."

| | Original wording | Explicit wording | Mean s/trial |
|---|---:|---:|---:|
| Agent + shell, no forge | 35/40 pass, **5 silent-wrong** | **40/40 pass** | 53 |
| forge (claude backend, no shell) | 40/40 pass | 40/40 pass | 110 |

- **With explicit wording, the agent alone matches forge**, at half the
  time per trial.
- **With the original wording, forge wins.** Pooling both runs, the agent
  alone was silent-wrong 9 times in 70 trials and forge 0 times in 40
  (Fisher one-sided p = 0.014).
- **forge's checks never fired.** All 80 forge trials had
  `validation_retries = 0`, and the `unchecked` condition also passed
  80/80. forge wins because `run_tdd_phases` (in forge's `runner.py`) runs
  the test-writing phase first whenever a task starts with `TDD:`. That is
  a better prompt, built into forge's structure; it is not a check that
  caught a mistake.

**What this changes above:**
- **The TDD paragraph is overstated.** "Mechanism gap, not capability
  gap" still holds, but the mechanism is mostly task decomposition (the
  red phase), not forge noticing that it is unsure.
- **Annotated failure 1 still holds as written.** forge's red/green gate
  really did catch qwen3.8:27b rewriting a test to pass trivially. That is
  a check doing its job, on a weaker model. The capable model here never
  gave the gate anything to catch.
- **The aider TDD numbers (100% silent-wrong) need a rerun.** Run aider
  on the `*_explicit` tasks before they are quoted again. Until then they
  measure the wording at least as much as aider.

The non-TDD and Phase 4 results are not affected. They do not depend on
this wording.
