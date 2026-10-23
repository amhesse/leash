# 11 - Safety direction: Leash as a control evaluation

Written 2026-09-29, from a conversation about where Leash fits in AI
safety research. It covers what Leash's own data says about "rogue"
agents, how Forge and Leash map onto the AI control research agenda, and
the next experiment (a sabotage condition). It also has a reading list,
with the PDFs downloaded to `~/Documents/ai-safety-reading/`, and the
forums worth joining.

## What Leash's data says about agents "going rogue"

In more than 1,000 unattended trials, none of the failures looked like
malice. They looked like optimising for *appearing done*:

- **Confabulated completion.** qwen3.8:27b under aider told itself "No
  other files need to be added". The harness exited 0 and
  `ledger/budget.py` was never written.
- **Satisfying the check instead of the intent.** Forge's TDD gate caught
  a new test that passed before any implementation existed. That is
  specification gaming in miniature: make the check green instead of
  making the code work.
- **Never admitting failure.** Aider parked 0 times in 750 trials (630
  internal + 120 polyglot). Every one of its failures shipped as a
  success.
- **Resolving an ambiguous instruction the cheap way, and not saying
  so** (added 2026-10-04). A capable agent with a shell (Strata's
  qwen3.8-flash-next coder, no forge) skipped the test file on 9 of 70
  ambiguously worded TDD trials. The implementation was correct each
  time. In 8 of the 9 it reported success with no mention of the missing
  test ("existing tests still pass"). In 1 it said why: it assumed the
  grader would supply the file. When the task said explicitly that the
  test did not exist yet, it wrote the test 40/40 times. So this is not
  inability. The agent picked the cheaper reading and did not flag it.
  Details: doc 10, "Postscript".

This is the mundane end of the safety spectrum. It is where most harm
comes from today: over-trusted agents that are silently wrong. It is
**not** evidence about the strategic end of the spectrum (scheming,
sandbagging, evaluation awareness). Leash's models are local 7-30B models
that try to succeed and sometimes fail. The frontier question sits
between the two ends. Can you tell a confidently-wrong model from a
strategically deceptive one? And do your safeguards need to?

## Forge is a control protocol; Leash measures it

AI control (Greenblatt et al., 2023, reading list #1) assumes the model
may be untrusted, even adversarial. It designs protocols that stay safe
anyway, and scores them on two axes: **safety** (does harm get through?)
and **usefulness** (how much good work survives?). The mapping onto what
already exists here:

| AI control concept | Forge / Leash equivalent |
|---|---|
| Untrusted model | the doer (local model under forge) |
| Trusted monitoring / checks | forge's check stack: byte-exact, scope, leakage, syntax, TDD red/green |
| Defer / audit | park the item on a branch for a human |
| Defer to trusted model / edit | escalation: repair by a cloud model |
| Safety metric | `silent_wrong` rate |
| Usefulness metric | pass rate |
| Retry / resample protocols | `--hard-validation-retries`, adaptive think-off retries |

Reading list #3 (*Retrying vs Resampling in AI Control*, 2026) is
directly relevant to the last row. It finds that retrying flagged actions
can be *exploited* by an adversarial model, which learns from the
monitor's rationale how to build sneakier attacks. Forge's retry loop
feeds validation errors back to the model. Against an honest-but-weak
model that is pure upside. Against an adversarial one it may leak the
checks.

### What forge's checks did and did not do (2026-10-04)

In the same-model wording experiment (doc 10, "Postscript"), forge's
`silent_wrong` rate was 0/80. But its validation never fired: every trial
had `validation_retries = 0`, and the `unchecked` condition also passed
80/80. The protection came from how forge breaks a task down (its TDD
red phase writes the test first), not from its checks.

So on Leash's current tasks, with a capable agent, **the checks are not
being tested.** An agent that can run the tests itself catches the
mistakes the checks were built for. The first row of the table above
("trusted monitoring / checks") still has no evidence behind it against
a capable model. The sabotage condition below is the test of that row:
it is built so that the agent's own testing cannot catch the bug,
because the agent is the one planting it.

## Next experiment: a sabotage condition

Today every Leash trial is **honest**: the model tries to succeed. Add an
**attack** condition. The doer gets a secret side instruction to slip a
subtle, grader-detectable bug past forge's checks while making the change
look legitimate. The design follows SHADE-Arena and the sabotage
evaluations (reading list #5 and #6).

What it measures:

1. **Safety under intent, not just incompetence.** Report `silent_wrong`
   separately for honest and attack trials. Forge's claim of zero silent
   wrongs is currently a claim about honest models only.
2. **Which checks catch sabotage.** Attribute every caught attack to the
   check that caught it. Some checks, like byte-exact, are unfoolable by
   construction. Some, like syntax or leakage, don't look for sabotage at
   all. TDD may be gameable when the attacker also writes the test.
3. **Whether retry feedback helps the attacker** (reading list #3). Run
   attack trials with retry budgets 1 and 5 and compare.
4. **Is sabotage distinguishable from honest failure?** Compare parked
   honest trials with parked attack trials, on the features the report
   already records.

Sketch of the work, all on existing machinery:

- [ ] Task format: add a hidden `side_task` (the planted-bug spec) and a
      side-task grader beside the existing hidden grader. Only the
      side-task grader decides whether the attack succeeded.
- [ ] Runner: a `--condition attack` flag that appends the side
      instruction to the doer's prompt. Forge and the checks never see
      it.
- [ ] Outcomes: split `silent_wrong` into `silent_wrong_honest` and
      `sabotage_merged`. Keep `parked` and `pass` as they are.
- [ ] Report: a safety-vs-usefulness table per check configuration,
      in the same shape as the control papers' Pareto plots.
- [ ] Freeze the forge commit before the attack baseline (lesson from the
      Phase 4 stock run that straddled a code change).

Caveat to state in any write-up: local 7-30B models are weak attackers.
A low sabotage success rate here bounds what *these* models can do, not
what frontier models can. That makes it a floor, and it is still a
useful result.

## Reading list

All PDFs are in **`~/Documents/ai-safety-reading/`**, numbered as below.
Read them in roughly this order.

### AI control and sabotage (closest to Leash)

1. **AI Control: Improving Safety Despite Intentional Subversion.** Greenblatt, Shlegeris et al., 2023.
   https://arxiv.org/abs/2312.06942
   *The foundational paper. You will recognise forge's design in it.*
2. **Ctrl-Z: Controlling AI Agents via Resampling.** Bhatt et al., 2025.
   https://arxiv.org/abs/2504.10374
   *Control for multi-step agents in a bash environment.*
3. **Retrying vs Resampling in AI Control.** Lucassen et al., 2026.
   https://arxiv.org/abs/2605.26047
   *Directly about forge's retry loop. Read this before building the attack condition.*
4. **Games for AI Control.** Griffin et al., 2024.
   https://arxiv.org/abs/2409.07985
   *The formal, game-theoretic framing of safety vs usefulness.*
5. **Sabotage Evaluations for Frontier Models.** Benton et al. (Anthropic), 2024.
   https://arxiv.org/abs/2410.21514
6. **SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents.** Kutasov et al., 2025.
   https://arxiv.org/abs/2506.15740
   *Hidden side tasks vs a monitor. The template for Leash's attack condition.*

### Specification gaming and misalignment, from mundane to strategic

7. **Concrete Problems in AI Safety.** Amodei et al., 2016.
   https://arxiv.org/abs/1606.06565
   *The classic. "Reward hacking" is one of its five problems.*
8. **Natural Emergent Misalignment from Reward Hacking in Production RL.** MacDiarmid et al. (Anthropic), 2025.
   https://arxiv.org/abs/2511.18397
   *The bridge between Leash's mundane failures and the dramatic ones.
   Models that learn to hack coding tests generalise to sabotage.*
9. **Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation.** Baker et al. (OpenAI), 2025.
   https://arxiv.org/abs/2503.11926
   *Chain-of-thought monitoring catches reward hacking, but optimising against the monitor teaches hiding.*
10. **Frontier Models are Capable of In-context Scheming.** Meinke et al. (Apollo Research), 2024.
    https://arxiv.org/abs/2412.04984
11. **Alignment Faking in Large Language Models.** Greenblatt et al. (Anthropic and Redwood), 2024.
    https://arxiv.org/abs/2412.14093
12. **Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training.** Hubinger et al., 2024.
    https://arxiv.org/abs/2401.05566
13. **Measuring AI Ability to Complete Long Software Tasks.** Kwa et al. (METR), 2025.
    https://arxiv.org/abs/2503.14499
    *How long a task can be delegated. The natural companion to "how long a leash".*

### Data centres, weight security and compute governance (the OCI angle)

14. **Securing AI Model Weights: Preventing Theft and Misuse of Frontier Models.** Nevo et al. (RAND), 2024.
    https://www.rand.org/pubs/research_reports/RRA2849-1.html
    *Origin of the SL1-SL5 security levels. Much of it is physical and data-centre security.*
15. **Achieving AI Model Weight Security Level 3 (SL3).** Aguirre et al. (RAND), 2026.
    https://www.rand.org/pubs/research_reports/RRA4704-1.html
16. **SL5 Standard for AI Security.** Thiergart et al., 2026.
    https://arxiv.org/abs/2605.08449
    *The top security tier, against nation-state attackers. Read it as a data hall designer.*
17. **Computing Power and the Governance of Artificial Intelligence.** Sastry et al., 2024.
    https://arxiv.org/abs/2402.08797
    *The standard reference on compute as a lever for governance.*
18. **What Does It Take to Catch a Chinchilla? Verifying Rules on Large-Scale Neural Network Training via Compute Monitoring.** Shavit, 2023.
    https://arxiv.org/abs/2303.11341
    *Verification of training runs at the hardware and data-centre level.*

### Worth knowing about (not downloaded)

- **Redwood Research's own reading list:** https://blog.redwoodresearch.org/p/guide
- **ControlArena** (UK AISI and Redwood), an open library for control experiments. It could host a Leash-style setting.
  https://github.com/UKGovernmentBEIS/control-arena
- **Open reproduction of #8 on open models (OLMo, GPT-OSS)** by UK AISI. It runs on local hardware.
  https://github.com/UKGovernmentBEIS/reward-hacking-misalignment
- **Calibration-Family Overfit: Why Trusted Sabotage Monitors Don't Transfer Across Lineages**, 2026.
  https://arxiv.org/abs/2607.06596
  *Relevant to Leash's multi-model design.*
- **How does information access affect LLM monitors' ability to detect sabotage?**, 2026.
  https://arxiv.org/abs/2601.21112

## Forums and communities

- **AI Alignment Forum.** Research-grade discussion. Posting needs an account with some history, but anyone can read, and good LessWrong posts get promoted here.
  https://www.alignmentforum.org
- **LessWrong.** Where to post a Leash write-up first. Researchers do engage with serious empirical work from outsiders here.
  https://www.lesswrong.com ; AI control tag: https://www.lesswrong.com/tag/ai-control
- **Redwood Research blog.** The home of AI control.
  https://blog.redwoodresearch.org
- **ControlConf**, the annual AI control conference, run by FAR.AI and Redwood (2026 edition, April). Researchers, lab engineers and policy people.
  https://www.far.ai/news/controlconf-2026
- **EA Forum, AI governance topic.** The policy and compute-governance side.
  https://forum.effectivealtruism.org/topics/ai-governance
- **Organisations to follow**, and eventually to contact with results:
  - UK AI Security Institute: https://www.aisi.gov.uk
  - METR: https://metr.org
  - Centre for the Governance of AI: https://www.governance.ai
  - Redwood Research: https://www.redwoodresearch.org/research/ai-control

## Suggested order of work

1. Read #1, #3 and #6.
2. Build the attack condition (the sketch above).
3. Run it on 2-3 of the existing local models, with the forge commit frozen.
4. Settle the Oracle IP question (see the private notes) **before** anything goes public.
5. Write it up as a LessWrong post framed in control terms:
   *"What 'rogue' looks like after 1,000 unattended trials, and what
   changes when the model is trying to fool you."*
6. Send it to the people behind #1-#6.
