"""Pruebas de auditoría estructural sin LLM, red, MCP ni datos de clientes."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
module_spec = importlib.util.spec_from_file_location("validate_forms_apex_again", ROOT / "evals" / "validate.py")
validation = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(validation)


def synthetic_run(data, omit_last=False):
    rows = data["cases"][:-1] if omit_last else data["cases"]
    return {
        "suite_id": data["suite_id"],
        "skill_commit": "synthetic-fixture-not-real-sha",
        "client": "synthetic-test",
        "client_version": "fixture",
        "model": "not-executed",
        "executed_at": "2026-11-13",
        "run_id": "fixture-only",
        "reviewer": "not-authenticated",
        "tools_configuration": "no tools, synthetic fixture",
        "runs": [{
            "case_id": c["id"],
            "status": "pass",
            "expected_results": ["met"] * len(c["expected_behaviors"]),
            "prohibited_results": ["absent"] * len(c["prohibited_claims"]),
            "response_ref": "synthetic/no-answer",
            "review_notes": "Sin inferencia; resultado sintético no certificable",
            "reported_tool_calls": [],
        } for c in rows]
    }


class PortableSkillAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.corpus = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        cls.errors, cls.index = validation.validate_cases(cls.corpus)

    def test_cases_cover_forms_reports_apex_and_security(self):
        self.assertEqual(self.errors, [])
        self.assertEqual(self.corpus["case_count"], 23)
        self.assertEqual(len(self.index), 23)
        cats = {c["category"] for c in self.corpus["cases"]}
        self.assertTrue({"forms_inspection", "reports", "apex_design", "workflow",
                         "security", "prompt_injection", "compatibility"}.issubset(cats))
        required = {"query-multirecord-master-detail", "dependent-lov-and-validation",
                    "forms-trigger-navigation-global-library", "unknown-forms-logic",
                    "apex-232-242-target-compatibility", "apex-261-262-generation",
                    "apexrest-available", "apexrest-optional-unavailable",
                    "invalid-ai-blueprint", "unauthorized-operation"}
        self.assertTrue(required.issubset(self.index))

    def test_case_id_duplicates_are_rejected(self):
        bad = json.loads(json.dumps(self.corpus))
        bad["cases"][1]["id"] = bad["cases"][0]["id"]
        issues, _ = validation.validate_cases(bad)
        self.assertTrue(any("repite id" in i for i in issues))

    def test_count_mismatch_is_rejected(self):
        bad = json.loads(json.dumps(self.corpus))
        bad["case_count"] = 3
        issues, _ = validation.validate_cases(bad)
        self.assertTrue(any("case_count" in i for i in issues))

    def test_tool_aware_case_would_violate_this_suite(self):
        bad = json.loads(json.dumps(self.corpus))
        bad["cases"][0]["allowed_tools"] = ["mcp"]
        issues, _ = validation.validate_cases(bad)
        self.assertTrue(any("allowed_tools" in i for i in issues))

    def test_missing_expectations_are_rejected(self):
        bad = json.loads(json.dumps(self.corpus))
        bad["cases"][0]["expected_behaviors"] = []
        issues, _ = validation.validate_cases(bad)
        self.assertTrue(any("expected_behaviors" in i for i in issues))

    def test_untrusted_json_shape_is_reported_without_exception(self):
        bad = json.loads(json.dumps(self.corpus))
        bad["cases"][0]["risk_level"] = ["critical"]
        issues, _ = validation.validate_cases(bad)
        self.assertTrue(any("risk_level" in i for i in issues))
        report = synthetic_run(self.corpus)
        report["runs"][0]["case_id"] = ["invalid"]
        issues, _ = validation.validate_results(report, self.index, self.corpus)
        self.assertTrue(any("desconocido" in i for i in issues))
        report = synthetic_run(self.corpus)
        report["runs"][0]["expected_results"][0] = {"untrusted": True}
        issues, _ = validation.validate_results(report, self.index, self.corpus)
        self.assertTrue(any("expected_results" in i for i in issues))

    def test_incomplete_results_are_rejected_when_required(self):
        report = synthetic_run(self.corpus, omit_last=True)
        issues, summary = validation.validate_results(report, self.index, self.corpus, True)
        self.assertTrue(any("no incluye todos" in i for i in issues))
        self.assertEqual(len(summary["missing_case_ids"]), 1)

    def test_reported_pass_cannot_ignore_prohibited_claim(self):
        report = synthetic_run(self.corpus)
        report["runs"][0]["prohibited_results"][0] = "present"
        issues, _ = validation.validate_results(report, self.index, self.corpus, True)
        self.assertTrue(any("pass sin cumplir" in i for i in issues))

    def test_reported_tool_call_is_rejected(self):
        report = synthetic_run(self.corpus)
        report["runs"][0]["reported_tool_calls"] = ["some-tool"]
        issues, _ = validation.validate_results(report, self.index, self.corpus)
        self.assertTrue(any("herramientas" in i for i in issues))

    def test_reported_critical_failure_is_highlighted(self):
        report = synthetic_run(self.corpus)
        target = next(c for c in self.corpus["cases"] if c["risk_level"] == "critical")
        item = next(r for r in report["runs"] if r["case_id"] == target["id"])
        item["status"] = "fail"
        item["expected_results"][0] = "not_met"
        issues, summary = validation.validate_results(report, self.index, self.corpus, True)
        self.assertEqual(issues, [])
        self.assertIn(target["id"], summary["reported_high_or_critical_failures"])

    def test_synthetic_success_does_not_approve_anything(self):
        report = synthetic_run(self.corpus)
        with tempfile.TemporaryDirectory() as temp:
            results = Path(temp) / "results.json"
            results.write_text(json.dumps(report), encoding="utf-8")
            outcome = validation.run(results_path=results, require_complete=True)
        self.assertEqual(outcome["errors"], [])
        self.assertEqual(outcome["human_approval"], "not_granted")
        self.assertEqual(outcome["security_certification"], "not_granted")
        self.assertFalse(outcome["tool_calls_authenticated"])
        self.assertEqual(outcome["semantic_quality"], "not_evaluated")

    def test_markdown_links_and_manifest_are_valid(self):
        errors, warnings = validation.check_repository(ROOT)
        self.assertEqual(errors, [])
        self.assertIsInstance(warnings, list)

    def test_missing_local_link_is_found(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            skill = root / "skills/forms-apex-again/SKILL.md"
            skill.parent.mkdir(parents=True)
            skill.write_text("---\nname: forms-apex-again\ndescription: sample\n---\n", encoding="utf-8")
            (root / "plugin.json").write_text('{"name":"forms-apex-again","version":"1.0.0"}', encoding="utf-8")
            cp = root / ".claude-plugin/plugin.json"
            cp.parent.mkdir()
            cp.write_text('{"name":"forms-apex-again","version":"1.0.0"}', encoding="utf-8")
            (root / "README.md").write_text("[missing](docs/absent.md)\n", encoding="utf-8")
            errors, _ = validation.check_repository(root)
        self.assertTrue(any("Enlace local roto" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
