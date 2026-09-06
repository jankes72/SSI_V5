# SSI V5 — Public Evidence Index

**Updated:** 2026-09-06

This directory is the public evidence layer for SSI V5. It publishes sanitized results, machine-readable summaries, lineage and claim boundaries without distributing the private SSI implementation.

## CURRENT EXPERIMENTAL STATE — 6X BODY ISKRA / START_STATE_VALIDATED

The newest recorded experimental state is now the six-agent BODY ISKRA start set descended from the same frozen BODY_FROZEN T0.

Entry point:

- [`BODY_ISKRA_6X_T0_20260906/README.md`](BODY_ISKRA_6X_T0_20260906/README.md)

Key files:

- [`BODY_ISKRA_6X_T0_20260906/GROUP_PUBLIC_SUMMARY.json`](BODY_ISKRA_6X_T0_20260906/GROUP_PUBLIC_SUMMARY.json)
- [`BODY_ISKRA_6X_T0_20260906/AGENT_01_NICE_PUBLIC_T0.json`](BODY_ISKRA_6X_T0_20260906/AGENT_01_NICE_PUBLIC_T0.json)
- [`BODY_ISKRA_6X_T0_20260906/AGENT_02_GUARDIAN_PUBLIC_T0.json`](BODY_ISKRA_6X_T0_20260906/AGENT_02_GUARDIAN_PUBLIC_T0.json)
- [`BODY_ISKRA_6X_T0_20260906/AGENT_03_JUSTICE_PUBLIC_T0.json`](BODY_ISKRA_6X_T0_20260906/AGENT_03_JUSTICE_PUBLIC_T0.json)
- [`BODY_ISKRA_6X_T0_20260906/AGENT_04_EXPLORER_PUBLIC_T0.json`](BODY_ISKRA_6X_T0_20260906/AGENT_04_EXPLORER_PUBLIC_T0.json)
- [`BODY_ISKRA_6X_T0_20260906/AGENT_05_PRAGMATIST_PUBLIC_T0.json`](BODY_ISKRA_6X_T0_20260906/AGENT_05_PRAGMATIST_PUBLIC_T0.json)
- [`BODY_ISKRA_6X_T0_20260906/AGENT_06_SKEPTIC_PUBLIC_T0.json`](BODY_ISKRA_6X_T0_20260906/AGENT_06_SKEPTIC_PUBLIC_T0.json)
- [`BODY_ISKRA_6X_T0_20260906/CLAIM_BOUNDARIES.md`](BODY_ISKRA_6X_T0_20260906/CLAIM_BOUNDARIES.md)
- [`BODY_ISKRA_6X_T0_20260906/PRIVATE_ARTIFACT_SHA256SUMS.txt`](BODY_ISKRA_6X_T0_20260906/PRIVATE_ARTIFACT_SHA256SUMS.txt)

Public group summary:

```text
AGENTS = 6
PRIVATE ARTIFACT PER AGENT = 1832 files
PYTHON FILES PER AGENT = 616
DELTA VS BODY_FROZEN PER AGENT = +51 files / +29 Python files
START-STATE QA PER AGENT = 8/8 PASS
GROUP START-STATE QA = 48/48 PASS
VERIFIED NEW EXPERIENCES AT T0 = 0 per agent
PENDING NEW EXPERIENCES AT T0 = 0 per agent
```

Each agent record includes sanitized initial beliefs, emotions, cognitive T0 state, inventory counts, QA status and a SHA256 reference to the corresponding private artifact.

This is **start-state evidence**, not a claim of long-term behavioral divergence or superiority.

---

## FROZEN COMMON BASELINE — BODY_FROZEN / 2026-09-05

BODY_FROZEN remains the immutable common origin for all six agents.

Entry point:

- [`BODY_FROZEN_T0_20260905/README.md`](BODY_FROZEN_T0_20260905/README.md)

```text
BODY_FROZEN inventory = 1781 files / 587 Python files retained privately
CONTINUUM = CLOSED
23/23 CONTINUUM tests PASS
22/22 MAIN SCENARIOS PASS
19/19 E2E CLOSURE PASS
26/26 FINAL GUARD PASS
ACTIVE FAILURES = 0
INVARIANT VIOLATIONS = 0
OPEN BLOCKERS = 0
```

BODY_FROZEN is preserved as historical control and is not rewritten by the six descendant agents.

---

## LATEST CLOSED VALIDATION — TEST 5

**Status:** `DEVELOPMENT_VALIDATED / PASS`  
**Date:** `2026-09-03`

- [`TEST5_FINAL_CONVERGENCE_20260903.md`](TEST5_FINAL_CONVERGENCE_20260903.md)
- [`TEST5_FINAL_RESULT_20260903.json`](TEST5_FINAL_RESULT_20260903.json)
- [`TEST5_FINAL_MATRIX_20260903.json`](TEST5_FINAL_MATRIX_20260903.json)
- [`TEST5_STAGE12_SUPERSEDED_20260903.json`](TEST5_STAGE12_SUPERSEDED_20260903.json)

```text
TEST5_ACCEPTANCE = 29/29 PASS
ROOT_CONTROL = 111/111 PASS
ROOT_RUNTIME_BRIDGE = 338/338 PASS
ROBERT_STABLE = 46/46 PASS
TOTAL = 524/524 PASS
OPEN_BLOCKERS = 0
STAGE_12 = SUPERSEDED
STAGE_13_AUDIT_RETEST = PASS
```

TEST 5 remains the newest closed validation milestone. The 6X BODY ISKRA record is the newest experimental start state, not a relabeling of TEST 5.

---

## PUBLICATION RULE

Public evidence may contain:

```text
PASS / FAIL / SUPERSEDED
counts
sanitized initial beliefs/emotions
benchmark summaries
sanitized lifecycle state
claim boundaries
lineage
SHA256 references
```

It must not intentionally publish:

```text
private SSI source code
private internal file tree
implementation-level architecture
secrets / tokens
private local paths
raw memory/user data
full proprietary prompt/routing/integration internals
```

The public repository is an evidence mirror, not a source distribution.