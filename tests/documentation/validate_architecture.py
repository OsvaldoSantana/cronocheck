#!/usr/bin/env python3
"""CRONO-006: structural cross-reference checks for proposed architecture ADRs.

Documentation-only: does not validate a deployed system, build, or approved ADR.
"""
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[2]
ADR=ROOT/"docs"/"architecture"/"adr"
FILES=[
    ADR/"ADR-001-modular-monolith.md",
    ADR/"ADR-002-frontend-boundary.md",
    ROOT/"docs"/"architecture"/"context-and-containers.md",
]
BLUEPRINT=ROOT/"docs"/"CRONOCHECK_BLUEPRINT_V1.md"
OPEN=ROOT/"docs"/"product"/"open-questions.md"
STATE=ROOT/"docs"/"PROJECT_STATE.md"
REQUIRED_MODULES=["Projects", "Imports", "Audits", "Reviews", "Reports"]
CRITICAL=["RF-01","RF-05","RF-08","RF-11","RNF-06","RNF-07","RNF-09","RNF-10"]

def check(condition, description):
    if not condition:
        raise AssertionError(description)

def read(path):
    check(path.is_file(),f"missing: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")

def main():
    one,two,c4=[read(path) for path in FILES]
    blueprint=read(BLUEPRINT)
    decisions=read(OPEN)
    state=read(STATE)
    for path,doc in zip(FILES,[one,two,c4]):
        check(doc.count(chr(96)*3)%2 == 0, f"{path.name}: unbalanced fences")
        check("mermaid" in doc, f"{path.name}: diagram missing")
        for link in re.findall(r"\]\(([^)]+)\)",doc):
            if link.startswith(("https://","http://","mailto:","#")):
                continue
            target=link.split("#",1)[0]
            if target:
                check((path.parent/target).exists(),f"{path.name}: invalid local link: {link}")
    check("**Estado:** Proposto" in one and "**Estado:** Proposto" in two,
          "ADRs must remain proposed")
    check("Monólito modular" in one and "Microsserviços" in one, "ADR-001 alternatives missing")
    check("transa" in one.lower() and "AuditEvent" in one, "ADR-001 transactional rationale missing")
    check("F01-E02" in one and "F01-E04" in one, "ADR-001 future proof requirements missing")
    for module in REQUIRED_MODULES:
        check(module in one and module in c4, f"module boundary missing: {module}")
    check("SharedKernel" in one, "SharedKernel constraints missing")
    check("React" in two and "TypeScript" in two and "ASP.NET Core" in two,
          "frontend/backend separation missing")
    check("Next.js" in two and "Vite" in two and "Razor" in two,
          "ADR-002 comparison missing")
    check("OIDC" in two and "PKCE" in two and "CSRF" in two and "CORS" in two,
          "auth/security trade-offs incomplete")
    check("OQ-04" in two and "pendente" in two.lower(),
          "hosting/identity selection must remain unapproved")
    check("OpenAPI" in two and "RNF-10" in two, "API contract governance missing")
    for rid in CRITICAL:
        check(any(rid in doc for doc in [one,two,c4]),f"untracked critical requirement {rid}")
    check("C4 L1" in c4 and "C4 L2" in c4, "context or container scope missing")
    check(c4.count(chr(96)*3+"mermaid")>=3, "C4 diagrams incomplete")
    check("CRONO-006" in blueprint, "blueprint task missing")
    check("OQ-04/OQ-05 pendentes" in decisions, "prior open decisions changed")
    check("**Gate G0:** **não aprovado**" in state and
          "**Fase 01:** não iniciada" in state,
          "phase/gate status changed without approval")
    print("PASS CRONO-006: ADR-001/002 remain proposed, C4 L1/L2 documented")
    print("PASS alternatives, module boundaries, contract and OIDC security considerations")
    print("PASS Markdown relative links, domain decisions and phase gate")
    print("NOTE: Docs checks only; no architecture implemented or ADRs approved.")
    return 0

if __name__=="__main__":
    try:
        sys.exit(main())
    except (AssertionError,ValueError,TypeError) as exc:
        print(f"FAIL CRONO-006: {exc}",file=sys.stderr)
        sys.exit(1)
