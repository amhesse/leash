"""Unit tests: statistics (against docs/04's worked examples), outcome and
error classification, results resume logic, and task loading."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

BENCH = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BENCH / "src"))

from leash import outcomes as O, results, stats  # noqa: E402
from leash.tasks import TaskError, load_task, load_tasks, task_signals  # noqa: E402


def trials(n, passes, silent, parked_ok=0):
    return [O.PASS] * passes + [O.SILENT_WRONG] * silent + [O.PARKED_OK] * parked_ok + \
        [O.PARKED] * (n - passes - silent - parked_ok)


class TestStats(unittest.TestCase):
    def test_wilson_matches_docs(self):
        self.assertAlmostEqual(stats.wilson(0, 30)[1], 0.114, places=3)
        self.assertAlmostEqual(stats.wilson(0, 73)[1], 0.05, places=3)
        self.assertAlmostEqual(stats.wilson(0, 188)[1], 0.02, places=3)
        self.assertAlmostEqual(stats.wilson(42, 50)[0], 0.715, places=3)
        self.assertEqual(stats.wilson(0, 0), (0.0, 1.0))

    def test_worked_examples_from_spec(self):
        # docs/04-leash-score.md "Worked examples"
        for n, p, s, score, level in [(50, 42, 1, 21.5, "L0"), (30, 27, 0, 18.1, "L0"),
                                      (50, 48, 0, 45.4, "L1"), (100, 95, 0, 66.9, "L2"),
                                      (30, 18, 2, 0.0, "L0")]:
            cs = stats.category_stats("c", trials(n, p, s))
            self.assertEqual((cs.score, cs.level), (score, level), (n, p, s))

    def test_off_leash_needs_lots_of_clean_evidence(self):
        self.assertEqual(stats.category_stats("c", trials(200, 199, 0)).level, "L3")
        self.assertNotEqual(stats.category_stats("c", trials(100, 100, 0)).level, "L3")

    def test_insufficient_data(self):
        cs = stats.category_stats("c", trials(29, 29, 0))
        self.assertIsNone(cs.score)
        self.assertFalse(cs.sufficient)
        self.assertEqual(cs.level_name, "Insufficient data")

    def test_leash_score_counts_missing_categories_as_zero(self):
        by = {"a": stats.category_stats("a", trials(100, 95, 0)),
              "b": stats.category_stats("b", trials(10, 10, 0))}
        weights = stats.profile_weights({"uniform": True}, ["a", "b"])
        self.assertEqual(stats.leash_score(by, weights), round(66.9 / 2, 1))
        explicit = stats.profile_weights({"weights": {"a": 3, "c": 1}}, ["a", "b"])
        self.assertEqual(explicit, {"a": 0.75, "c": 0.25})
        self.assertEqual(stats.leash_score(by, explicit), round(0.75 * 66.9, 1))
        self.assertIsNone(stats.leash_score(by, {}))

    def test_bundled_profile_loads(self):
        self.assertTrue(stats.load_profile("uniform-v1")["uniform"])
        with self.assertRaises(ValueError):
            stats.load_profile("nope")

    def test_efficiency_rates(self):
        def row(checked, esc=None, resolved=None):
            r = {"conditions": {O.CHECKED: {"outcome": checked}}, "local": {"seconds": 10, "tokens": {}}}
            if esc:
                r["escalation"] = {"status": esc, "resolved_by": resolved, "seconds": 5, "tokens": {}}
            return r
        rows = [row(O.PASS, "not_needed"), row(O.PARKED_OK, "done", "cloud"), row(O.PARKED, "done", "none"),
                row(O.SILENT_WRONG, "not_needed"), row(O.PARKED, "skipped")]
        e = stats.efficiency(rows)
        self.assertEqual(e["friction_rate"], 0.5)
        self.assertAlmostEqual(e["catch_rate"], 2 / 3)
        self.assertEqual((e["escalations_needed"], e["escalations_run"], e["escalations_skipped"]), (3, 2, 1))
        self.assertEqual(e["rescue_rate"], 0.5)


class TestOutcomeClassification(unittest.TestCase):
    EDITOR_FAILED = {"reason": "aider itself failed after 3 attempt(s)"}

    def classify(self, log, record, stage="local", rc=0, timed_out=False):
        return O.classify_stage_error(log, rc, timed_out, record, stage)

    def test_real_results_are_not_errors(self):
        self.assertIsNone(self.classify("[t] Parked [!]", {"reason": "validation failed"}))
        # An error line followed by a successful retry is a real result.
        log = "[t] claude -p reported an error: usage limit reached\n[t] [claude] committed: ok"
        self.assertIsNone(self.classify(log, {"reason": "passed every check and was merged"}, "cloud"))

    def test_infrastructure(self):
        self.assertEqual(self.classify("", None), "forge_failed")
        self.assertEqual(self.classify("x", {}, timed_out=True), "stage_timeout")
        self.assertEqual(self.classify("No TODO.md found in /p", {}, rc=1), "harness_preflight")
        self.assertEqual(self.classify("[t] [lite_editor] could not reach ollama at http://x: refused",
                                       self.EDITOR_FAILED), "ollama_unreachable")

    def test_cloud_kinds(self):
        cases = {
            "[t] claude CLI not found on PATH (claude)": "cloud_cli_missing",
            "[t] claude -p reported an error: Claude AI usage limit reached": "cloud_quota",
            "[t] claude -p reported an error: 429 Too Many Requests": "cloud_quota",
            "[t] claude -p timed out after 1800s": "cloud_timeout",
            "[t] claude -p reported an error: There's an issue with the selected model": "cloud_error",
        }
        for log, kind in cases.items():
            self.assertEqual(self.classify(log, self.EDITOR_FAILED, "cloud"), kind, log)
        self.assertIn("cloud_quota", O.STOPS_ESCALATION)

    def test_agy_kinds(self):
        cases = {
            "[t] agy CLI not found on PATH (agy)": "cloud_cli_missing",
            "[t] agy reported an error: RESOURCE_EXHAUSTED: quota exceeded": "cloud_quota",
            "[t] agy timed out after 1800s": "cloud_timeout",
            "[t] agy returned non-JSON output (exit 2): Error: --print took": "cloud_error",
        }
        for log, kind in cases.items():
            self.assertEqual(self.classify(log, self.EDITOR_FAILED, "cloud"), kind, log)

    def test_local_escalation_infra_error_in_cloud_stage(self):
        # ollama:<model> escalation repairs through forge's lite backend, so
        # a "cloud" stage can fail the same infrastructure way local does.
        self.assertEqual(self.classify("[t] [lite_editor] could not reach ollama at http://x: refused",
                                       self.EDITOR_FAILED, "cloud"), "ollama_unreachable")

    def test_quota_anywhere_wins(self):
        log = ("[t] claude -p reported an error: model issue\n"
               "[t] claude -p reported an error: rate limit exceeded")
        self.assertEqual(self.classify(log, self.EDITOR_FAILED, "cloud"), "cloud_quota")


class TestResults(unittest.TestCase):
    def row(self, trial, status="ok", digest="d1", **extra):
        return {"model": {"name": "m", "digest": digest}, "harness": {"hash": "h"}, "cloud": None,
                "task_hash": "t", "trial": trial, "status": status, **extra}

    def test_resume_keys_and_supersession(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "r.jsonl"
            results.append(path, self.row(1))
            results.append(path, self.row(2, status="error"))
            results.append(path, self.row(1, note="filled"))
            rows = results.load(path)
            self.assertEqual(len(rows), 3)
            self.assertTrue(all(r["schema"] == 1 for r in rows))
            current = results.latest(rows)
            self.assertEqual(len(current), 2)
            self.assertEqual(next(r for r in current if r["trial"] == 1)["note"], "filled")
            done = results.completed_keys(rows)
            self.assertIn(results.trial_key(self.row(1)), done)
            self.assertNotIn(results.trial_key(self.row(2)), done)      # error reruns
            self.assertNotIn(results.trial_key(self.row(1, digest="other")), done)

    def test_torn_last_line_is_ignored_but_corruption_is_not(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "r.jsonl"
            path.write_text(json.dumps(self.row(1)) + "\n{\"trunc")
            self.assertEqual(len(results.load(path)), 1)
            path.write_text("{bad\n" + json.dumps(self.row(1)) + "\n")
            with self.assertRaises(ValueError):
                results.load(path)


class TestTasks(unittest.TestCase):
    def test_bench_loads_and_filters(self):
        tasks = load_tasks(BENCH)
        self.assertGreaterEqual(len(tasks), 14)
        self.assertEqual([t.id for t in load_tasks(BENCH, ids=["exact_new_file"])], ["exact_new_file"])
        self.assertTrue(all(t.category == "tdd" for t in load_tasks(BENCH, categories=["tdd"])))
        with self.assertRaises(TaskError):
            load_tasks(BENCH, ids=["no_such_task"])

    def test_hash_is_stable_and_content_sensitive(self):
        [t] = load_tasks(BENCH, ids=["exact_new_file"])
        self.assertEqual(t.content_hash(BENCH), t.content_hash(BENCH))
        self.assertEqual(len(t.content_hash(BENCH)), 16)

    def test_signals(self):
        self.assertEqual(task_signals("TDD: implement `a/b.py` so `tests/test_b.py` passes"),
                         {"tdd": True, "files": 2, "exact": False})
        text = "Replace `x.py` with exactly:\n```python\nA = 1\n```\n"
        self.assertEqual(task_signals(text), {"tdd": False, "files": 1, "exact": True})
        self.assertEqual(task_signals("Call `Ledger.add` from `ledger.store.Ledger`")["files"], 0)

    def test_malformed_task_directories_are_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            t = Path(d) / "t1"
            t.mkdir()
            with self.assertRaisesRegex(TaskError, "meta.toml"):
                load_task(t)
            (t / "meta.toml").write_text('id = "other"\ncategory = "c"\nfixture = "f"\n')
            with self.assertRaisesRegex(TaskError, "must match"):
                load_task(t)
            (t / "meta.toml").write_text('id = "t1"\ncategory = "c"\nfixture = "f"\n[mutants]\nm = "x"\n')
            for f in ("task.md", "grader.py"):
                (t / f).write_text("x")
            (t / "reference").mkdir()
            with self.assertRaisesRegex(TaskError, "mutant 'm'"):
                load_task(t)


class TestEscalateOption(unittest.TestCase):
    def test_parse(self):
        from leash import cli
        self.assertEqual(cli.DEFAULT_ESCALATE, "gemini:gemini-3.8-flash-high")
        self.assertEqual(cli.parse_escalate("gemini:gemini-3.8-flash-high"), ("agy", "gemini-3.8-flash-high"))
        self.assertEqual(cli.parse_escalate("agy:gemini-3.1-pro-high"), ("agy", "gemini-3.1-pro-high"))
        self.assertEqual(cli.parse_escalate("claude"), ("claude", None))
        self.assertEqual(cli.parse_escalate("claude:claude-opus-5"), ("claude", "claude-opus-5"))
        self.assertEqual(cli.parse_escalate("none"), (None, None))
        self.assertEqual(cli.parse_escalate("ollama:qwen2.5-coder:14b"), ("lite", "qwen2.5-coder:14b"))
        self.assertIn("ollama", cli.LOCAL_ESCALATION_ENGINES)
        for bad in ("gpt:x", "gemini", "ollama"):
            with self.assertRaises(SystemExit):
                cli.parse_escalate(bad)


if __name__ == "__main__":
    unittest.main()
