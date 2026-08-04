> This note is kept as originally written (April 2026) as a historical
> record. Two things below have since changed and are corrected inline:
> the classification (CWE-1387 is not a valid mapping target — see note)
> and the advisory link (now published in this same repository). Everything
> else is left as-is.

**SECURITY RESEARCH PROJECT**

This repository serves as a proof-of-concept for demonstrating 
Indirect Prompt Injection vulnerabilities in GraphRAG-based 
code analysis systems.

## Purpose
This is a honeypot repository containing controlled malicious 
payloads in docstrings to test AI security tools' resilience 
to indirect prompt injection attacks.

## Vulnerability Details
- **Type**: Indirect Prompt Injection via GraphRAG
- **CWE**: ~~CWE-1387~~ **CWE-1427** (corrected — CWE-1387 is a MITRE View,
  not a mappable weakness; see `../ADVISORY.md#classification`)
- **CVSS**: 7.5 (High)
- **CVSS Vector**: `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:L/I:L/A:L`
- **Target**: Potpie AI (responsible disclosure completed, no response received)
- **CVE**: Requested from MITRE (tracking `#2027937`, 2026-04-20); no CVE ID
  was ever assigned and no further response was received — see
  `../docs/TIMELINE.md`

## Research Context
Part of independent security audit conducted in March 2026.

**Timeline:**
- March 6-7, 2026: Audit & PoC development
- March 8, 2026: Responsible disclosure submitted
- April 8, 2026: 30-day window expired
- March 2026: Public advisory released

**Full advisory:**
- [`../ADVISORY.md`](../ADVISORY.md) — now published, in this repository
- [LinkedIn announcement](https://www.linkedin.com/posts/marsel-sultanov-719873373_technical-advisory-graphrag-prompt-injection-ugcPost-7478772826968121344-Y3uH/)

## Attack Pattern
1. Malicious instruction embedded in code documentation (docstrings)
2. Parser ingests content into Neo4j knowledge graph
3. GraphRAG retrieves node during code analysis
4. LLM receives content without data/instruction separation
5. Agent executes injected instruction via tool layer

## Proof of Concept
This repository contains:
- `app/schemas/compliance.py` — file with embedded payload
- `../poc/trigger_resilience_local.py` — testing script (sanitized)
- Technical artifacts demonstrating the vulnerability (see `../docs/EVIDENCE.md`)

## Impact
- ✅ Agent compromise via tool execution
- ✅ SSRF potential (AWS metadata access)
- ✅ Supply-chain attack vector (malicious PRs)
- ✅ Secret leakage from knowledge graph

## Remediation
See full remediation roadmap in the security advisory:
- Data/instruction segregation
- Context filtering
- Tool gating
- Egress controls

## ⚠️ Warning
**This repository contains intentional security vulnerabilities for 
research and educational purposes only. DO NOT deploy in production 
or connect to real systems.**

## Contact
**Researcher:** Marsel Sultanov  
**Email:** marsel.sultanov.aisensemaking@gmail.com  
**LinkedIn:** linkedin.com/in/marsel-sultanov-719873373  
**Skills:** AI Red Teaming, LLM Security, Prompt Injection, GraphRAG

---
*Independent AI Security Researcher · Agentic Security & LLM Failure Modes*
