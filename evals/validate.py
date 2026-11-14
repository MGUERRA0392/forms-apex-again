#!/usr/bin/env python3
"""Auditoría estructural local de una skill portable; sin modelos, red ni dependencias externas."""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "evals" / "cases.json"
ID = re.compile(r"^[a-z][a-z0-9-]*$")
FRONT = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|$)", re.DOTALL)
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
RISKS = {"low", "medium", "high", "critical"}
STATUSES = {"pass", "fail", "inconclusive", "not_run"}
EXPECTED = {"met", "not_met", "unknown"}
PROHIBITED = {"absent", "present", "unknown"}


def good_text(value):
    return isinstance(value, str) and bool(value.strip())


def validate_cases(data):
    errors, index = [], {}
    if not isinstance(data, dict):
        return ["El corpus debe ser un objeto JSON"], index
    for field in ("suite_id", "schema_version", "skill_version", "execution_mode"):
        if not good_text(data.get(field)):
            errors.append("Falta el metadato " + field)
    if data.get("execution_mode") != "manual_by_client_no_tools":
        errors.append("execution_mode debe reflejar ejecución manual sin herramientas")
    if data.get("approval") != "not_granted":
        errors.append("El corpus no concede aprobación")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + ["cases debe ser una lista no vacía"], index
    if type(data.get("case_count")) is not int or data["case_count"] != len(cases):
        errors.append("case_count no coincide con el número de escenarios")
    for i, case in enumerate(cases, 1):
        key = "cases[" + str(i) + "]"
        if not isinstance(case, dict):
            errors.append(key + " no es objeto")
            continue
        cid = case.get("id")
        if not good_text(cid) or ID.fullmatch(cid) is None:
            errors.append(key + " tiene id inválido")
        elif cid in index:
            errors.append(key + " repite id: " + cid)
        else:
            index[cid] = case
        if not good_text(case.get("category")):
            errors.append(key + " requiere category")
        if not isinstance(case.get("risk_level"), str) or case["risk_level"] not in RISKS:
            errors.append(key + " tiene risk_level inválido")
        if not good_text(case.get("prompt")):
            errors.append(key + " no tiene prompt válido")
        for field in ("expected_behaviors", "prohibited_claims"):
            values = case.get(field)
            if not isinstance(values, list) or not values or not all(good_text(v) for v in values):
                errors.append(key + " requiere " + field + " no vacío")
            elif len({v.strip().casefold() for v in values}) != len(values):
                errors.append(key + " repite criterios en " + field)
        if case.get("allowed_tools") != []:
            errors.append(key + " debe declarar allowed_tools: []")
    return errors, index


def validate_results(data, index, suite, require_complete=False):
    errors, summary = [], {}
    if not isinstance(data, dict):
        return ["El registro debe ser un objeto JSON"], summary
    for key in ("suite_id", "skill_commit", "client", "client_version",
                "model", "executed_at", "run_id", "reviewer",
                "tools_configuration"):
        if not good_text(data.get(key)):
            errors.append("Falta metadato: " + key)
    if data.get("suite_id") != suite.get("suite_id"):
        errors.append("suite_id no corresponde al corpus")
    runs = data.get("runs")
    if not isinstance(runs, list):
        return errors + ["runs debe ser una lista"], summary
    seen, statuses, high_failures = set(), {}, []
    for pos, row in enumerate(runs, 1):
        key = "runs[" + str(pos) + "]"
        if not isinstance(row, dict):
            errors.append(key + " no es objeto")
            continue
        cid = row.get("case_id")
        if not isinstance(cid, str) or cid not in index:
            errors.append(key + " usa un ID desconocido")
            continue
        if cid in seen:
            errors.append(key + " repite caso: " + cid)
        seen.add(cid)
        status = row.get("status")
        if not isinstance(status, str) or status not in STATUSES:
            errors.append(key + " tiene status inválido")
            continue
        statuses[status] = statuses.get(status, 0) + 1
        if status == "fail" and index[cid]["risk_level"] in {"high", "critical"}:
            high_failures.append(cid)
        expected, prohibited = row.get("expected_results"), row.get("prohibited_results")
        calls = row.get("reported_tool_calls")
        if calls != []:
            errors.append(key + " declara herramientas o no incluye reported_tool_calls: []")
        if status == "not_run":
            if expected not in ([], None) or prohibited not in ([], None):
                errors.append(key + " no ejecutado tiene criterios evaluados")
            continue
        if not good_text(row.get("response_ref")) or not good_text(row.get("review_notes")):
            errors.append(key + " requiere response_ref y review_notes")
        if not isinstance(expected, list) or len(expected) != len(index[cid]["expected_behaviors"]) or any(not isinstance(x, str) or x not in EXPECTED for x in expected):
            errors.append(key + " expected_results inválido")
        if not isinstance(prohibited, list) or len(prohibited) != len(index[cid]["prohibited_claims"]) or any(not isinstance(x, str) or x not in PROHIBITED for x in prohibited):
            errors.append(key + " prohibited_results inválido")
        if status == "pass" and (not isinstance(expected, list) or any(x != "met" for x in expected)
                                 or not isinstance(prohibited, list) or any(x != "absent" for x in prohibited)):
            errors.append(key + " pass sin cumplir todos los criterios declarados")
    missing = sorted(set(index) - seen)
    if require_complete and (missing or statuses.get("not_run")):
        errors.append("La corrida no incluye todos los escenarios ejecutados")
    summary = {"reported_statuses": statuses, "missing_case_ids": missing,
               "reported_high_or_critical_failures": sorted(high_failures)}
    return errors, summary


def check_repository(root):
    """Comprobar enlaces locales, manifiestos y SKILL; no evalúa seguridad semántica."""
    root = Path(root).resolve()
    errors, warnings = [], []
    skill = root / "skills/forms-apex-again/SKILL.md"
    try:
        content = skill.read_text(encoding="utf-8-sig")
        m = FRONT.match(content)
        if not m or not re.search(r"(?m)^name:\s*forms-apex-again\s*$", m.group(1)) or not re.search(r"(?m)^description:\s*\S", m.group(1)):
            errors.append("SKILL.md carece de name/description en frontmatter")
    except OSError as exc:
        errors.append("No se puede leer SKILL.md: " + str(exc))
    versions = set()
    for relative in ("plugin.json", ".claude-plugin/plugin.json"):
        try:
            obj = json.loads((root / relative).read_text(encoding="utf-8-sig"))
            if obj.get("name") != "forms-apex-again" or not good_text(obj.get("version")):
                errors.append("Nombre o versión inválido en " + relative)
            versions.add(obj.get("version") if isinstance(obj.get("version"), str) else "")
        except (OSError, ValueError) as exc:
            errors.append("Manifiesto ilegible " + relative + ": " + str(exc))
    if len(versions) > 1:
        errors.append("Los manifiestos declaran versiones diferentes")
    if not (root / "LICENSE").is_file() and not (root / "LICENSE.md").is_file():
        warnings.append("Repositorio público sin archivo de licencia detectado; no se infiere licencia open source")
    for doc in sorted(root.rglob("*.md")):
        if any(p in {".git", ".venv", "node_modules"} for p in doc.relative_to(root).parts):
            continue
        try:
            text = doc.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as exc:
            errors.append("Markdown ilegible " + str(doc) + ": " + str(exc))
            continue
        for match in LINK.finditer(text):
            target = match.group(1).strip().strip("<>").split(' "', 1)[0].split(" '", 1)[0]
            if not target or target.startswith("#") or re.match(r"^(?:[a-z][a-z0-9+.-]*:|//)", target, re.I):
                continue
            target = target.split("#")[0].split("?")[0]
            if not target:
                continue
            resolved = (doc.parent / target).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                warnings.append("Referencia local fuera del repositorio: " + doc.relative_to(root).as_posix())
                continue
            if not resolved.exists():
                errors.append("Enlace local roto: " + doc.relative_to(root).as_posix() + " -> " + target)
    return errors, warnings


def run(cases_path=CASES, results_path=None, root=ROOT, require_complete=False):
    try:
        dataset = json.loads(Path(cases_path).read_text(encoding="utf-8-sig"))
        errors, index = validate_cases(dataset)
    except (OSError, ValueError) as exc:
        dataset, index, errors = {}, {}, ["Corpus ilegible: " + str(exc)]
    structural, warnings = check_repository(root)
    errors.extend(structural)
    summaries = {}
    if require_complete and results_path is None:
        errors.append("--require-complete requiere --results")
    if results_path is not None and not errors:
        try:
            res = json.loads(Path(results_path).read_text(encoding="utf-8-sig"))
            errs, summaries = validate_results(res, index, dataset, require_complete)
            errors.extend(errs)
        except (OSError, ValueError) as exc:
            errors.append("Resultados ilegibles: " + str(exc))
    return {"structural_status": "fail" if errors else "pass",
            "case_count": len(index), "errors": errors, "warnings": warnings,
            "result_summary": summaries, "semantic_quality": "not_evaluated",
            "tool_calls_authenticated": False, "human_approval": "not_granted",
            "security_certification": "not_granted"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=CASES)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--results", type=Path)
    parser.add_argument("--require-complete", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    outcome = run(args.cases, args.results, args.root, args.require_complete)
    if args.json:
        print(json.dumps(outcome, ensure_ascii=False, indent=2))
    else:
        print("Casos:", outcome["case_count"], "| estructura:", outcome["structural_status"])
        for err in outcome["errors"]:
            print("ERROR:", err)
        for w in outcome["warnings"]:
            print("ADVERTENCIA:", w)
    return 1 if outcome["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
