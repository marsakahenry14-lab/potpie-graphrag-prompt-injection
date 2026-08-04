# PoC

`trigger_resilience_local.py` is the original March 2026 test script,
reproduced for methodology transparency — see the header comment in that
file for why it isn't meant to be re-run against a live target as-is (dead
OAST endpoint, requires your own model-router credentials, belongs to the
researcher's own test harness rather than to Potpie's codebase).

The honeypot target it was run against, and both payloads embedded in it,
are documented in [`../docs/EVIDENCE.md`](../docs/EVIDENCE.md); the target
itself lives in [`../honeypot/`](../honeypot).

For a deterministic, dependency-free, immediately runnable reproduction of
the *current* (August 2026) architecture's version of this problem, see
[`potpie-context-provenance`](https://github.com/marsakahenry14-lab/potpie-context-provenance)
(part 2 of this disclosure).
