# 05 - Roadmap

## Phase 0 + 1 - Built 2026-09-14 (v1 runner)

Delivered as one build instead of hardening `forge calibrate` first
(details in [08 - Runner design](08-runner-design.md)):

- [x] forge hooks: `--snapshot-first-attempt`, `--repair-from` / `--repair-note`,
      `--backend claude` accepted on the command line.
- [x] `leashbench` repo: task directory format; forge's 14 bench items ported
      (`tools/port_forge_bench.py`) with 29 mutants, including the real
      `silent_wrong` failures from forge calibration.
- [x] Grader validation (`leash selftest`): fixture fails, reference passes,
      every mutant fails. `leash run` refuses invalid tasks.
- [x] Cascade trial: `unchecked` / `checked` / `escalated` from one attempt;
      Claude repair escalation with budget, quota stop, bundles, `--fill-escalations`.
- [x] Infrastructure `error` outcome - never scored, reruns on resume.
- [x] Full trial metadata (model digest, quantization, Ollama version, context,
      GPU, harness config hash, forge commit + dirty flag, cloud CLI version).
- [x] JSONL results, resume keys, round-robin scheduling, `leash estimate`.
- [x] Wilson intervals, category scores, levels, Leash / raw / system scores,
      harness and escalation lift; markdown + self-contained HTML report.

Still open from the original Phase 1:

- [ ] Adapter for a second harness (Claude Code CLI as the *doer*, aider standalone).
- [ ] Second fixture in **TypeScript**; grow to ~40 tasks across categories.
- [x] Gemini escalation - forge `agy` backend; `gemini:gemini-3.8-flash-high` is the default.
- [ ] `maintenance-v1` / `feature-v1` profiles derived from real checklist histories.
- [ ] Energy per task (GPU power sampling).

## Phase 2 - First public report (after Phase 1)

9. Overnight battery: 5-8 local models (plus 1-2 hosted for reference),
   forge-lite harness; harness lift comes from the `unchecked` condition.
10. Publish **The Silent Wrong Report #1**: methodology, public task subset,
    category tables, Leash Scores, harness lift, efficiency metrics, and
    explicit limitations.
11. Demand check: collect requests; talk to ~10 potential buyers.

## Phase 2b - Sabotage condition (added 2026-09-29)

Turns Leash from a reliability benchmark into a small AI control
evaluation. Every trial today is honest; this adds trials where the doer
is secretly told to slip a bug past forge's checks. Full design, framing,
reading list and forums: [11 - Safety direction](11-safety-direction.md).

- [ ] Read the core papers first: AI Control, Retrying vs Resampling, and
      SHADE-Arena (PDFs in `~/Documents/ai-safety-reading/`).
- [ ] Task format: a hidden `side_task` plus a side-task grader.
- [ ] Runner: `--condition attack`. The side instruction goes to the doer
      only.
- [ ] Outcomes: `silent_wrong_honest` vs `sabotage_merged`; attribute
      each caught attack to the check that caught it.
- [ ] Compare retry budgets 1 vs 5 under attack: does feedback help the
      attacker?
- [ ] Safety-vs-usefulness report table; forge commit frozen before the
      baseline.
- [ ] Settle the Oracle IP question before anything is published (private
      notes in `docs/private/`, gitignored).
- [ ] Write-up for LessWrong, framed in control terms.

## Phase 3 - Only if demand shows up

12. **Private evaluations** offer (first revenue): run on customer repos /
    tasks / on-prem models; report with levels and routing policy.
13. **Routing library** (`leash.route`) consumed by forge's worker tiers.
14. **`leash-gate`** CI action - only after paying interest in evals.
15. Scheduled re-runs; rotate private tasks; add Go fixture and more agents
    (aider, Codex CLI, OpenHands).

## Open questions

- Which 5-8 local models define the first report (current forge favourites:
  qwen3-coder:30b, qwen2.5-coder:14b, ...)? Include quantization variants of
  the same model?
- How many GPU-hours does a credible first report cost? (Estimate from
  existing calibration timings before committing.)
- License: open-source harness + public tasks (MIT/Apache), private tasks
  proprietary?
- Publish where: GitHub Pages site, blog, HN/Reddit (r/LocalLLaMA is the
  natural first audience)?
- Should friction (`parked_ok`) enter the score for any profile?
