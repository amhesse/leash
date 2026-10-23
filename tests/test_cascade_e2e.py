"""End-to-end cascade tests: real forge, real git, real graders, scripted
editors (see stubs.py). One scenario per path through the cascade."""

from __future__ import annotations

import io
import json
import os
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
BENCH = HERE.parent
sys.path.insert(0, str(BENCH / "src"))
sys.path.insert(0, str(HERE))

import stubs  # noqa: E402
from leash import cascade, cli, outcomes as O, results  # noqa: E402
from leash.adapters.forge import ForgeAdapter  # noqa: E402
from leash.tasks import load_tasks  # noqa: E402

FORGE_SRC = Path(os.environ.get("FORGE_SRC", Path.home() / "projects" / "forge" / "src"))
TASK = "split_evenly_signed"


class _ForgeStubBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp(prefix="leash-e2e-"))
        stubs.install(cls.tmp / "bin")
        cls.env_patch = mock.patch.dict(os.environ, {
            "PATH": f"{cls.tmp / 'bin'}:{os.environ['PATH']}",
            "PYTHONPATH": f"{FORGE_SRC}:{os.environ.get('PYTHONPATH', '')}",
            "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
            "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t",
        })
        cls.env_patch.start()
        [cls.task] = load_tasks(BENCH, ids=[TASK])
        cls.reference = cls.task.reference
        cls.wrong = cls.task.mutant_dir("real_sign_lost")  # passes fixture tests, fails grader
        broken = cls.tmp / "broken"
        shutil.copytree(cls.reference, broken)
        money = broken / "ledger" / "money.py"
        money.write_text(money.read_text() + "\ndef broken(:\n")
        cls.broken = broken
        cls.adapter = ForgeAdapter(forge_cmd=[sys.executable, "-m", "forge.cli"], max_validation_retries=1)

    @classmethod
    def tearDownClass(cls):
        cls.env_patch.stop()
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def setUp(self):
        self.log = self.tmp / f"calls-{self._testMethodName}.jsonl"

    def trial(self, plan: dict, policy: cascade.EscalationPolicy | None = None, **kw) -> dict:
        stubs.set_plan(plan, self.log)
        policy = policy or cascade.EscalationPolicy(engine="claude", model="claude-opus-5")
        return cascade.run_trial(self.task, 1, bench=BENCH, adapter=self.adapter, model="stub-model",
                                 backend="aider", policy=policy, stage_timeout=120, **kw)

    def outcomes(self, row):
        return tuple(row["conditions"].get(c, {}).get("outcome") for c in O.CONDITIONS)


@unittest.skipUnless((FORGE_SRC / "forge" / "runner.py").is_file(), f"forge source not found at {FORGE_SRC}")
class CascadeE2E(_ForgeStubBase):

    def test_correct_first_attempt(self):
        row = self.trial({"first": self.reference})
        self.assertEqual(row["status"], "ok", row)
        self.assertEqual(self.outcomes(row), (O.PASS, O.PASS, O.PASS))
        self.assertEqual(row["conditions"]["unchecked"]["source"], "snapshot")
        self.assertEqual(row["escalation"]["status"], "not_needed")
        self.assertEqual(row["conditions"]["escalated"]["resolved_by"], "local")
        self.assertFalse([c for c in stubs.calls(self.log) if c["tool"] == "claude"])

    def test_broken_first_attempt_fixed_by_validation_retry(self):
        row = self.trial({"first": self.broken, "fix": self.reference})
        self.assertEqual(self.outcomes(row), (O.SILENT_WRONG, O.PASS, O.PASS))
        self.assertEqual([c["kind"] for c in stubs.calls(self.log)], ["first", "fix"])

    def test_wrong_but_passes_checks_is_silent_wrong_everywhere(self):
        row = self.trial({"first": self.wrong})
        self.assertEqual(self.outcomes(row), (O.SILENT_WRONG, O.SILENT_WRONG, O.SILENT_WRONG))
        self.assertEqual(row["escalation"]["status"], "not_needed")
        self.assertIn("[-34, -33, -33]", row["conditions"]["checked"]["grader_output"])

    def test_parked_then_repaired_by_cloud(self):
        row = self.trial({"first": self.broken, "fix": self.broken, "cloud": self.reference})
        self.assertEqual(self.outcomes(row), (O.SILENT_WRONG, O.PARKED, O.PASS))
        esc = row["escalation"]
        self.assertEqual(esc["status"], "done")
        self.assertEqual(esc["resolved_by"], "cloud")
        self.assertIn("validation failed", esc["repair_note"])
        [claude] = [c for c in stubs.calls(self.log) if c["tool"] == "claude"]
        self.assertTrue(claude["repair"], "cloud model should get the repair prompt")
        self.assertEqual(claude["model"], "claude-opus-5")

    def test_cloud_repair_that_is_still_wrong(self):
        row = self.trial({"first": self.broken, "fix": self.broken, "cloud": self.wrong})
        self.assertEqual(self.outcomes(row), (O.SILENT_WRONG, O.PARKED, O.SILENT_WRONG))
        self.assertEqual(row["escalation"]["resolved_by"], "cloud_wrong")

    def test_cloud_quota_is_an_error_and_conservative(self):
        row = self.trial({"first": self.broken, "fix": self.broken, "cloud": "quota"})
        self.assertEqual(row["status"], "ok")
        self.assertEqual(row["escalation"]["status"], "error")
        self.assertEqual(row["escalation"]["error"], "cloud_quota")
        self.assertEqual(row["conditions"]["escalated"]["outcome"], O.PARKED)
        self.assertEqual(row["conditions"]["escalated"]["fallback"], "error")
        self.assertIn({"stage": "cloud", "kind": "cloud_quota"}, row["errors"])

    def test_editor_crash_is_scored_not_infrastructure(self):
        row = self.trial({"first": "crash"}, policy=cascade.EscalationPolicy())
        self.assertEqual(row["status"], "ok")
        self.assertEqual(self.outcomes(row), (O.SILENT_WRONG, O.PARKED, None))
        self.assertEqual(row["conditions"]["unchecked"]["source"], "base")
        self.assertEqual(row["escalation"]["status"], "disabled")

    def test_gemini_via_agy_repairs_parked_work(self):
        policy = cascade.EscalationPolicy(engine="agy", model="gemini-3.8-flash-high",
                                          name="gemini:gemini-3.8-flash-high")
        row = self.trial({"first": self.broken, "fix": self.broken, "cloud": self.reference}, policy=policy)
        self.assertEqual(self.outcomes(row), (O.SILENT_WRONG, O.PARKED, O.PASS))
        self.assertEqual(row["escalation"]["model"], "gemini:gemini-3.8-flash-high")
        self.assertEqual(row["escalation"]["tokens"]["prompt_tokens"], 900)
        [agy] = [c for c in stubs.calls(self.log) if c["tool"] == "agy"]
        self.assertTrue(agy["repair"])
        self.assertTrue(agy["print_last"], "--print must be last or agy drops the prompt")
        self.assertEqual(agy["model"], "gemini-3.8-flash-high")

    def test_gemini_quota_stops_like_claude(self):
        policy = cascade.EscalationPolicy(engine="agy", model="gemini-3.8-flash-high")
        row = self.trial({"first": self.broken, "fix": self.broken, "cloud": "quota"}, policy=policy)
        self.assertEqual(row["escalation"]["error"], "cloud_quota")
        self.assertEqual(row["conditions"]["escalated"]["outcome"], O.PARKED)

    def test_skipped_escalation_saves_bundle_and_fill_completes_it(self):
        policy = cascade.EscalationPolicy(engine="claude", model=None, allowed=False, skip_reason="budget",
                                          artifact_dir=self.tmp / "artifacts")
        row = self.trial({"first": self.broken, "fix": self.broken}, policy=policy, artifact_key="k1")
        self.assertEqual(row["escalation"]["status"], "skipped")
        self.assertEqual(row["conditions"]["escalated"]["outcome"], O.PARKED)
        self.assertTrue(Path(row["escalation"]["bundle"]).is_file())

        stubs.set_plan({"cloud": self.reference}, self.log)
        filled = cascade.fill_escalation(row, self.task, bench=BENCH, adapter=self.adapter,
                                         policy=cascade.EscalationPolicy(engine="claude"), stage_timeout=120)
        self.assertEqual(filled["escalation"]["status"], "done")
        self.assertEqual(filled["conditions"]["escalated"]["outcome"], O.PASS)
        self.assertEqual(filled["conditions"]["checked"]["outcome"], O.PARKED)


@unittest.skipUnless((FORGE_SRC / "forge" / "runner.py").is_file(), f"forge source not found at {FORGE_SRC}")
class CliE2E(_ForgeStubBase):
    """`leash run` -> resume -> budget -> `leash report`, through cli.main."""

    FAKE_MODEL = {"name": "stub-model:1b", "provider": "ollama", "digest": "d1g3st00ffee",
                  "quantization": "Q4_K_M", "parameter_size": "1B", "runtime": {"ollama_version": "0.0-test"}}

    def run_cli(self, *argv) -> tuple[int, str]:
        out = io.StringIO()
        with mock.patch("leash.env.ollama_model_info", return_value=dict(self.FAKE_MODEL)), \
                redirect_stdout(out):
            code = cli.main(list(argv))
        return code, out.getvalue()

    def base_args(self, results_path: Path, *extra):
        return ["run", "--model", "stub-model:1b", "--backend", "aider", "--no-warmup", "--skip-selftest",
                "--forge-cmd", f"{sys.executable} -m forge.cli", "--max-validation-retries", "1",
                "--bench", str(BENCH), "--out", str(results_path), *extra]

    def test_run_resume_budget_and_report(self):
        out = self.tmp / "results" / "run.jsonl"
        stubs.set_plan({"first": self.broken, "fix": self.broken, "cloud": self.reference}, self.log)
        code, text = self.run_cli(*self.base_args(out, "--tasks", f"{TASK},exact_new_file", "--trials", "2",
                                                  "--escalate", "claude:claude-opus-5", "--max-escalations", "1"))
        self.assertEqual(code, 0, text)
        rows = results.load(out)
        self.assertEqual(len(rows), 4)
        self.assertEqual([(r["task_id"], r["trial"]) for r in rows],
                         [("exact_new_file", 1), (TASK, 1), ("exact_new_file", 2), (TASK, 2)])  # round-robin
        statuses = [r["escalation"]["status"] for r in rows]
        self.assertEqual(statuses.count("done"), 1, statuses)       # budget of one
        self.assertEqual(statuses.count("skipped"), 3, statuses)
        self.assertTrue(all(r["model"]["digest"] == "d1g3st00ffee" for r in rows))
        self.assertEqual(rows[0]["harness"]["backend"], "aider")

        code, text = self.run_cli(*self.base_args(out, "--tasks", f"{TASK},exact_new_file", "--trials", "2",
                                                  "--escalate", "claude:claude-opus-5"))
        self.assertEqual(code, 0, text)
        self.assertIn("0 trial(s) to run, 4 already complete", text)
        self.assertEqual(len(results.load(out)), 4)

        code, text = self.run_cli(*self.base_args(out, "--tasks", f"{TASK},exact_new_file", "--trials", "2",
                                                  "--escalate", "claude:claude-opus-5", "--fill-escalations"))
        self.assertEqual(code, 0, text)
        current = results.latest(results.load(out))
        self.assertEqual(len(current), 4)
        self.assertTrue(all(r["escalation"]["status"] == "done" for r in current),
                        [r["escalation"] for r in current])

        md, html_path = self.tmp / "report.md", self.tmp / "report.html"
        code, _ = self.run_cli("report", str(out), "--md", str(md), "--html", str(html_path))
        self.assertEqual(code, 0)
        text = md.read_text()
        self.assertIn("# Leash report", text)
        self.assertIn("stub-model:1b (Q4_K_M) + claude:claude-opus-5", text)
        self.assertIn("insufficient", text)
        self.assertIn("Every silent wrong", text)
        page = html_path.read_text()
        self.assertTrue(page.startswith("<!doctype html>"))
        self.assertNotIn("<script", page)

    def test_default_escalation_is_gemini_flash(self):
        out = self.tmp / "results" / "default.jsonl"
        stubs.set_plan({"first": self.broken, "fix": self.broken, "cloud": self.reference}, self.log)
        code, text = self.run_cli(*self.base_args(out, "--tasks", TASK, "--trials", "1"))
        self.assertEqual(code, 0, text)
        self.assertIn("escalation gemini:gemini-3.8-flash-high", text)
        [row] = results.load(out)
        self.assertEqual(row["cloud"]["model"], "gemini:gemini-3.8-flash-high")
        self.assertEqual(row["cloud"]["engine"], "agy")
        self.assertEqual(row["conditions"]["escalated"]["outcome"], O.PASS)
        self.assertTrue(any(c["tool"] == "agy" for c in stubs.calls(self.log)))

        code, text = self.run_cli(*self.base_args(self.tmp / "results" / "off.jsonl", "--tasks", TASK,
                                                  "--trials", "1", "--escalate", "none"))
        self.assertEqual(code, 0, text)
        self.assertIn("escalation off", text)
        [row] = results.load(self.tmp / "results" / "off.jsonl")
        self.assertNotIn("escalated", row["conditions"])

        # Regression: report used to raise AttributeError on a no-escalation
        # file, because cloud is explicitly None (not just missing) and
        # `.get(k, {})` only substitutes a default for a MISSING key, not a
        # None value. run_cli calls cli.main() in-process, so if that bug
        # were still there this call would raise, not just return nonzero.
        md = self.tmp / "off-report.md"
        code, text = self.run_cli("report", str(self.tmp / "results" / "off.jsonl"), "--md", str(md))
        self.assertEqual(code, 0, text)
        report_text = md.read_text()
        self.assertIn("| Escalation | disabled |", report_text)
        self.assertIn("Escalation was disabled for this run.", report_text)

    def test_local_infrastructure_error_reruns_on_resume(self):
        out = self.tmp / "results" / "infra.jsonl"
        stubs.set_plan({"first": self.reference}, self.log)
        with mock.patch("leash.outcomes.classify_stage_error", side_effect=["ollama_unreachable", None]):
            code, text = self.run_cli(*self.base_args(out, "--tasks", TASK, "--trials", "1", "--escalate", "none"))
        self.assertEqual(code, 0, text)
        self.assertIn("ERROR (ollama_unreachable)", text)
        with mock.patch("leash.outcomes.classify_stage_error", return_value=None):
            code, text = self.run_cli(*self.base_args(out, "--tasks", TASK, "--trials", "1", "--escalate", "none"))
        self.assertIn("1 trial(s) to run, 0 already complete", text)
        current = results.latest(results.load(out))
        self.assertEqual([r["status"] for r in current], ["ok"])


if __name__ == "__main__":
    unittest.main()
