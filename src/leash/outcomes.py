"""Outcome vocabulary and infrastructure-error classification.

Every scored condition of a trial ends in one of four outcomes:

  pass           merged, and the hidden grader says correct
  silent_wrong   merged, but wrong - nothing caught it
  parked_ok      not merged, though the work was actually correct
  parked         not merged, and wrong - the safety net worked

Infrastructure failures (Ollama down, CLI missing, quota, a hung harness)
are not outcomes: they say nothing about the model, so they are recorded
as errors and never scored.
"""

from __future__ import annotations

import re

PASS = "pass"
SILENT_WRONG = "silent_wrong"
PARKED_OK = "parked_ok"
PARKED = "parked"
OUTCOMES = (PASS, SILENT_WRONG, PARKED_OK, PARKED)
MERGED_OUTCOMES = (PASS, SILENT_WRONG)

UNCHECKED = "unchecked"
CHECKED = "checked"
ESCALATED = "escalated"
CONDITIONS = (UNCHECKED, CHECKED, ESCALATED)


def merged_outcome(correct: bool) -> str:
    return PASS if correct else SILENT_WRONG


def parked_outcome(correct: bool) -> str:
    return PARKED_OK if correct else PARKED


# (kind, pattern). Matched against forge's own log lines, never against
# model output or test output quoted inside them.
_LOCAL_PATTERNS = [
    ("ollama_unreachable", re.compile(r"\[lite_editor\] could not reach ollama")),
    ("model_not_configured", re.compile(r"\[lite_editor\] called with no model")),
]
_PREFLIGHT_PATTERNS = re.compile(
    r"^(No \S+ found in |Project dir does not exist|.* is not a git repo; per-item worktrees need one"
    r"|The project checkout has uncommitted changes)", re.M)
# forge's claude_editor and agy_editor log these when the CLI itself failed.
_CLOUD_FAILURE_LINE = re.compile(
    r"^.*(claude CLI not found|claude -p timed out|claude -p reported an error|"
    r"claude -p returned non-JSON output|agy CLI not found|agy timed out|agy reported an error|"
    r"agy returned non-JSON output).*$", re.M)
_QUOTA = re.compile(r"rate.?limit|usage limit|quota|\b429\b|overloaded|credit balance|limit reached|"
                    r"too many requests", re.I)

STOPS_ESCALATION = {"cloud_quota", "cloud_cli_missing"}


# forge's reason when the editor never produced a usable attempt at all
# (process_item: "aider itself failed after N attempt(s)"; TDD phases:
# "TDD red phase: aider itself failed").
_EDITOR_NEVER_RAN = re.compile(r"itself failed")


def classify_stage_error(log: str, returncode: int | None, timed_out: bool,
                         record: dict | None, stage: str) -> str | None:
    """Returns an error kind if the stage failed for infrastructure reasons,
    else None (the stage produced a real, scoreable result).

    Editor-level failures (Ollama unreachable, claude quota) only count as
    infrastructure when the editor never succeeded: forge retries, so an
    error line followed by a successful attempt is a real result."""
    if timed_out:
        return "stage_timeout"
    if _PREFLIGHT_PATTERNS.search(log):
        return "harness_preflight"
    if returncode not in (0, None) or record is None:
        return "forge_failed"
    # The editor ran, but this harness could not parse a file out of what it
    # said - typically a thinking model truncated mid-reasoning before
    # emitting one. That is the harness losing the output, not the model
    # declining to answer, so it is an error rather than a park: scoring it
    # as a park credits the safety net for a bug. forge retries such an
    # attempt with thinking disabled first, so reaching here means the
    # remedy was already tried and still produced nothing.
    if record.get("editor_failure") == "no_parseable_output":
        return "editor_no_output"
    if not _EDITOR_NEVER_RAN.search(record.get("reason") or ""):
        return None
    if stage == "local":
        for kind, pattern in _LOCAL_PATTERNS:
            if pattern.search(log):
                return kind
        return None
    # "cloud" covers every escalation stage, including a second *local*
    # model repairing through forge's lite backend - which can fail the
    # same infrastructure ways the first local stage can (Ollama down).
    for kind, pattern in _LOCAL_PATTERNS:
        if pattern.search(log):
            return kind
    lines = [m.group(0) for m in _CLOUD_FAILURE_LINE.finditer(log)]
    if not lines:
        return None
    # Most specific first, across all retries: one quota hit anywhere means
    # further escalations this run will hit it too.
    if any("CLI not found" in line for line in lines):
        return "cloud_cli_missing"
    if any(_QUOTA.search(line) for line in lines):
        return "cloud_quota"
    if all("timed out" in line for line in lines):
        return "cloud_timeout"
    return "cloud_error"
