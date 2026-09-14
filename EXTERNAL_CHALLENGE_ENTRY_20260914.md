# SSI V5 — External Challenge Entry — 2026-09-14

**Purpose:** define the preferred next validation step after internal software-domain demonstration.

## Core proposal

An external robotics, drone, warehouse or research partner can provide a problem that SSI has not previously seen.

The preferred protocol is:

```text
PARTNER SUPPLIES PROBLEM
-> CHALLENGE FROZEN BEFORE EXECUTION
-> PASS / FAIL / INCONCLUSIVE CRITERIA DECLARED
-> START STATE RECORDED
-> RUN
-> FAILURES PRESERVED
-> TIMINGS RECORDED
-> TRANSFER / CONSOLIDATION IF APPLICABLE
-> RESULT RETURNED TO PARTNER
-> PUBLICATION ONLY WITH PARTNER APPROVAL
```

## Publication modes

```text
PUBLIC
ANONYMIZED PARTNER
PRIVATE VALIDATION
```

The public repository will not publish partner proprietary code, confidential operating data or private internal systems without explicit authorization.

## Why this matters

An externally supplied challenge reduces the risk that the project author selected a scenario specifically favorable to SSI. The result remains useful even when it is FAIL or INCONCLUSIVE, provided the challenge was frozen before execution and the evidence is preserved.

## Public showcase

Current reviewer-facing showcase:

https://echotrip.jankespawel98.workers.dev/

The showcase can later host approved external challenge evidence alongside internal benchmarks while preserving the distinction between internal demonstration and independent validation.
