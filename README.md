# potpie-graphrag-prompt-injection

The technical advisory referenced in
[this LinkedIn post](https://www.linkedin.com/posts/marsel-sultanov-719873373_technical-advisory-graphrag-prompt-injection-ugcPost-7478772826968121344-Y3uH/)
(publishing announcement, ~3 July 2026), finally shipped as an actual,
citable artifact rather than an attachment nobody outside the original
thread could see.

Indirect prompt injection via Potpie AI's (March 2026) GraphRAG pipeline:
a payload placed in a Python docstring is parsed by `tree-sitter`, stored
unlabeled in a Neo4j knowledge graph, retrieved during code analysis, and
executed by Potpie's LLM agent via a tool call — confirmed with an
out-of-band HTTP callback.

**→ Full advisory: [ADVISORY.md](ADVISORY.md)**

## TL;DR

- **Disclosed**: 8 March 2026, to `hello@potpie.ai`, with a 30-day
  responsible-disclosure window (deadline 8 April 2026).
- **Followed up**: 25 March 2026, directly to both co-founders (CEO, CTO),
  by email and by LinkedIn message.
- **Response received**: none, on any channel, as of this publication.
- **CVE requested**: 20 April 2026, MITRE tracking reference `#2027937`.
  No CVE ID was ever assigned and no response was received from MITRE
  beyond the tracking number — reason unknown.
- **Publicly announced**: ~3 July 2026 (117 days post-disclosure), via
  LinkedIn, as responsible-disclosure practice.
- **This repository**: the advisory that announcement referenced, now
  actually published, with one correction — see below.

## Correction from the original announcement

Both the original March advisory and the July LinkedIn announcement
classified this as **CWE-1387**. That was wrong: CWE-1387 is not a
weakness — it's a MITRE *View* ("Weaknesses in the 2022 CWE Top 25"), an
organizational index over other CWEs, and its own page states
`Vulnerability Mapping: PROHIBITED`. The correct classification is
**CWE-1427** — Improper Neutralization of Input Used for LLM Prompting —
verified directly against cwe.mitre.org. See
[`ADVISORY.md`](ADVISORY.md#classification) for detail. Nothing about the
technical finding changes; the label does.

## What's in here

| Path | What it is |
|---|---|
| `ADVISORY.md` | The technical advisory: executive summary, CVSS, attack flow, PoC, impact, remediation. |
| `docs/TIMELINE.md` | Every disclosure attempt with dates and channels. |
| `docs/EVIDENCE.md` | The honeypot target, both embedded payloads, the confirmed callback. |
| `poc/` | The original proof-of-concept script (historical — the target OAST endpoint is no longer live). |
| `honeypot/` | The honeypot target itself — the source this repository's own git history traces back to (commits from 2026-02-25, predating the audit). |

This repository *is* the original honeypot (`honeypot/` below is its
unmodified content, with its own commit history intact) — reorganized
around the advisory it was built to demonstrate, rather than left sitting
unlabeled after the fact.

## Follow-up

A second, independent research pass in August 2026 checked whether this
was fixed. It wasn't — but the mechanism that made it possible no longer
exists either; Potpie's codebase changed substantially in between, and a
new instance of the same underlying defect turned up in different code.
See [`potpie-context-provenance`](https://github.com/marsakahenry14-lab/potpie-context-provenance)
(part 2 — link will 404 until that repo is published).

## License

MIT — see [`LICENSE`](LICENSE).
