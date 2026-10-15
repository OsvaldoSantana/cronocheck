#!/usr/bin/env python3
"""F00-E05: verify traceability and factual claims in the G0 readiness dossier.

Document validation only; this cannot grant G0 approval or establish test results.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
PRODUCT = ROOT / "docs" / "product"

def check(valid: bool, reason: str) -> None:
    if not valid:
        raise AssertionError(reason)

def load(path: Path) -> str:
    check(path.is_file(), f"missing document: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")

def local_links(path: Path, content: str) -> None:
    for link in re.findall(r"\]\(([^)]+)\)", content):
        if link.startswith(("http://", "https://", "mailto:", "#")):
            continue
        name = link.split("#", 1)[0]
        if name:
            check((path.parent / name).exists(),
                  f"{path.relative_to(ROOT)}: broken link {link}")

def main() -> int:
    gate_path = PRODUCT / "g0-readiness.md"
    decisions_path = PRODUCT / "decision-brief-f00.md"
    risks_path = PRODUCT / "risk-kpi-plan.md"
    gate = load(gate_path)
    decisions = load(decisions_path)
    risks = load(risks_path)
    state = load(ROOT / "docs" / "PROJECT_STATE.md")
    blueprint = load(ROOT / "docs" / "CRONOCHECK_BLUEPRINT_V1.md")
    prd = load(PRODUCT / "prd.md")
    oq = load(PRODUCT / "open-questions.md")
    backlog = load(PRODUCT / "f00-backlog.md")
    readme = load(ROOT / "README.md")

    for path, text in [(gate_path, gate), (decisions_path, decisions), (risks_path, risks)]:
        check(text.count("**") % 2 == 0, f"{path.name}: unbalanced strong text")
        check(text.count(chr(96) * 3) % 2 == 0, f"{path.name}: unbalanced fences")
        local_links(path, text)

    # The dossier must mirror the real F00-E01..05 outputs and avoid synthetic approvals.
    for i in range(1, 6):
        stage = f"F00-E{i:02d}"
        check(stage in blueprint and stage in gate, f"{stage}: missing from blueprint or dossier")
    check("Gate G0" in blueprint and "Gate G0" in gate, "gate source missing")
    for item in ("PRD", "hipóteses", "fixtures", "aprovado", "HOLD"):
        check(item.lower() in gate.lower(), f"gate dossier lacks {item}")

    # OQ-01 and OQ-02 are the only approvals yet; remaining options are recommendations.
    for i in range(1, 10):
        oqid = f"OQ-{i:02d}"
        check(oqid in oq, f"missing {oqid} in decision register")
        if i >= 3:
            check(oqid in decisions, f"decision brief missing {oqid}")
    for i in range(1, 3):
        check(f"OQ-{i:02d}" in gate and f"OQ-{i:02d}" in decisions,
              f"approved decision OQ-{i:02d} absent from gate dossier")
    check("GOV-01" in decisions and "GOV-02" in decisions, "governance decisions untracked")
    check("não foi modificado" in decisions.lower()
          or "nada foi modificado" in decisions.lower(),
          "governance change may be implied")

    for i in range(1, 10):
        rid = f"R-{i:02d}"
        check(re.search(rf"(?m)^\| \*\*{re.escape(rid)}\*\*", risks),
              f"risk R-{i:02d} missing from table")
        check(rid in prd, f"{rid}: not traced to PRD")
    for i in range(1, 4):
        kid = f"KPI-{i:02d}"
        check(re.search(rf"(?m)^\| {kid} \|", risks) is not None,
              f"missing definition {kid}")
    for metric in ("RNF-03", "RNF-04", "RNF-08"):
        check(metric in risks and metric in prd, f"provisional {metric} not traced")
    check("sem baseline" in risks.lower()
          or "nenhum valor numérico" in risks.lower(),
          "metrics cannot be claimed as measured")

    check("**Gate G0:** **não aprovado**" in state, "G0 appears approved without gate record")
    check("**Fase 01:** não iniciada" in state, "F01 started without approval")
    check("F00-E05 / Issue #14" in state and "T-E05-06" in backlog,
          "F00-E05 tasks not connected to project state")
    check("g0-readiness.md" in readme and "risk-kpi-plan.md" in readme,
          "README lacks dossier links")
    check("Não aprovado" in prd, "PRD has not been formally approved")
    check("F00-E03" in gate and "F00-E04" in gate and "F00-E05" in gate,
          "missing readiness stage")

    print("PASS F00-E05: 5 phase-zero stages and G0 criteria documented")
    print("PASS OQ-01..09 tracked; GOV-01/02 remain separate")
    print("PASS 9 risk entries, 3 KPI definitions and provisional RNF-03/04/08")
    print("PASS local references and factual unapproved Gate G0/F01 state")
    print("NOTE: Documentation-only; no product tests, interviews or approvals.")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, ValueError, TypeError) as exc:
        print(f"FAIL F00-E05: {exc}", file=sys.stderr)
        sys.exit(1)
