# Disclosure timeline

Every entry below is a primary-source fact (the researcher's own sent
mail/messages, or a live, fetched public post) — not a reconstruction.

| Date | Channel | Event |
|---|---|---|
| 2026-03-08, 15:26 | Email → `hello@potpie.ai` | Initial disclosure: full technical advisory, CVSS 7.5, 30-day responsible-disclosure window stated (deadline 2026-04-08). |
| 2026-03-25, 01:32 | LinkedIn message → Dhiren Mathur (Co-Founder & CTO, Potpie AI) | Follow-up, subject line "Follow-up: Security Advisory (CVSS 7.5) — Enterprise Risk Context". |
| 2026-03-25, 01:39 | LinkedIn message → Aditi Kothari (Co-Founder & CEO, Potpie AI) | Same follow-up. |
| 2026-03-25, 11:14 | Email → `dhiren@potpie.ai` | Same follow-up, by email. |
| 2026-03-25, 11:15 | Email → `aditi@potpie.ai` | Same follow-up, by email. |
| 2026-04-08 | — | 30-day disclosure window closes. No acknowledgment received on any channel to date. |
| 2026-04-20 | MITRE CVE request | Request submitted; MITRE issued tracking reference `#2027937`. No CVE ID was ever assigned, and no further communication was received from MITRE. Reason unknown — possibly a form/eligibility mismatch, possibly a severity/priority decision, possibly simple non-response. Not resolved as of this publication. |
| ~2026-07-03 (117 days post-disclosure, per the post's own count) | Public LinkedIn post | ["Technical Advisory: GraphRAG Prompt Injection"](https://www.linkedin.com/posts/marsel-sultanov-719873373_technical-advisory-graphrag-prompt-injection-ugcPost-7478772826968121344-Y3uH/) — names Potpie AI directly, states the 117-day silence, states responsible-disclosure practice was followed, references "the attached advisory" (this repository is that advisory, now actually published as a standalone artifact rather than a post attachment). Uses CWE-1387, corrected in this repository — see `ADVISORY.md#classification`. |
| This publication | This repository | The referenced advisory, published as a citable artifact with the classification correction. |

## Context: an earlier, anonymized post

Roughly four months before the July post (~April 2026), the researcher
published a separate, deliberately anonymized post describing the general
architectural pattern — "Reliance Drift," unstructured data ingested into
a knowledge graph, retrieved by an autonomous agent, executed as an
instruction because of missing data/instruction segregation — without
naming Potpie or any other vendor
([post](https://www.linkedin.com/posts/marsel-sultanov-719873373_graphrag-investigation-indirect-prompt-ugcPost-7443958745958895616-qIxC/),
confirmed live: no company names appear in it). It's noted here for
completeness, not as a disclosure milestone — it named no target and made
no claim about a specific vendor's system.

## Summary

Five distinct, personally-addressed outreach attempts (one general inbox,
two named executives by email, the same two by LinkedIn) across a 17-day
window, plus a formal CVE request, produced zero acknowledgment from
Potpie AI or MITRE. The public announcement came 117 days after the
initial report — well past any standard responsible-disclosure window
(30–90 days is typical industry practice).
