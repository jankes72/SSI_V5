# SSI V5 — Public Evidence Index

**Updated:** 2026-09-08

This directory is the public evidence layer for SSI V5. It publishes sanitized results, machine-readable summaries, lineage, predeclared protocols, integrity references and claim boundaries without distributing the private SSI implementation.

## CURRENT RESEARCH SEQUENCE

```text
BODY_FROZEN / ISKRA T0 CONTROLS
-> FINAL TECHNICAL READINESS
-> 14 PRE-EXPERIMENT TRAINING PACKAGES
-> FOUNDATION_S1 / TRAINED_START_S2
-> 7 MICRONETWORK + V10 MECHANISM TESTS
-> 21 CROSS-DOMAIN EXPERIMENTS
-> POST-21 CONSOLIDATION
-> 3 NEW DOMAINS
-> LATER EXTERNAL FALSIFICATION CHALLENGES
```

Historical T0 states remain immutable. Training creates versioned descendants rather than rewriting T0.

## PRE-EXPERIMENT TRAINING — 14 HASH-SEALED PACKAGES

Recorded before training outcomes were known:

- [`../PREEXPERIMENT_TRAINING_PROGRAM_20260908.md`](../PREEXPERIMENT_TRAINING_PROGRAM_20260908.md)
- [`../PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md`](../PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md)
- [`../TRAINING_PACKAGES_START_HERE.md`](../TRAINING_PACKAGES_START_HERE.md)

```text
7 BODY LINES x 2 PHASES = 14 PACKAGES

A = FOUNDATION
B = LEGO + MICRONETWORK + V10 PRACTICUM
```

Shared curriculum hashes:

```text
FOUNDATION_CURRICULUM_SHA256
= 61a3069ce68d19c64d4ae7c5ebc730d04283d81b2e534f487c3fd5063d9b75b8

PRACTICUM_CURRICULUM_SHA256
= abc3eccc4e19849f2d3b3be5b1a4d2752377b6024225f0da8d7d54f4ebafc7ce
```

No training PASS, Foundation S1 or Trained Start S2 result is claimed yet.

Training is deliberately separated from held-out experiment vectors. If later audit finds material leakage from an experiment case into training, that case must not be represented as clean held-out evidence.

## PERFORMANCE / ROUTE-COST EVIDENCE

Training and later experiments may record the cost of the route actually reported by SSI:

```text
FULL_FLOW
VERIFY_TOPK / VERIFY-ADAPT
REUSE_TOP1
LEGO / ALTERNATIVE COMPOSITION
RECOVERY AFTER FAILURE
```

Reviewer-safe context should include, where available:

```text
elapsed time
actual route class
correctness / outcome
model / provider
model/tool call count
execution node
CPU / RAM / GPU / VRAM
```

Timing does not determine route identity. Route labels come from the runtime/evidence contract.

Historical scoped reference:

```text
TEST 3 duration = 57.61 s
TEST 2 duration = 126.65 s
REUSE_TOP1 = 534
VERIFY_TOPK = 66
fallback = 0
known correctness = 100/100
```

This does not establish universal superiority outside the tested workload/hardware/model conditions.

## PREDECLARED MICRONETWORK + V10 MECHANISM TESTS — 7 PACKAGES

The first seven independent mechanism-test packages were hash-sealed on 2026-09-08 before outcomes were known.

Registry:

- [`../PREDECLARED_7BODY_MICRONETWORK_V10_PACKAGES_20260908.md`](../PREDECLARED_7BODY_MICRONETWORK_V10_PACKAGES_20260908.md)
- [`../EXPERIMENT_PACKAGES_START_HERE.md`](../EXPERIMENT_PACKAGES_START_HERE.md)

Their original hashes remain unchanged after the later addition of the training stage.

Before post-training execution, the exact `TRAINED_START_S2` state must be recorded and checked against the frozen experiment contract. A material input change requires a new experiment-package version/hash rather than rewriting the original precommitment.

## PREDECLARED CROSS-DOMAIN PROGRAM — 21 EXPERIMENTS

Canonical protocol:

- [`../EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md`](../EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md)

```text
LINES = 7
EXPERIMENTS PER LINE = 3
TOTAL = 21
STATUS = PREDECLARED / FINAL CONTROLLED OUTCOMES UNKNOWN

A = DRONES
B = HUMANOID
C = NEW DOMAIN SELECTED BY THAT SSI LINE
```

Common measurement categories include `KNOWN / SIMILAR / NOVEL`, Router V10 route choice, reuse/verify/adapt/full-flow behavior, latency, correctness, false reuse, recovery, competence creation/update, provenance and hardware/model context.

This is a protocol record, not a claim of 21 completed PASS results.

## CURRENT RECORDED START STATE — 6X BODY ISKRA

Entry point:

- [`BODY_ISKRA_6X_T0_20260906/README.md`](BODY_ISKRA_6X_T0_20260906/README.md)

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

This is start-state evidence, not a claim of long-term behavioral divergence or superiority.

## FROZEN COMMON BASELINE — BODY_FROZEN / 2026-09-05

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

BODY_FROZEN remains the immutable historical control.

## LATEST CLOSED VALIDATION — TEST 5

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

TEST 5 remains the latest closed validation milestone. It is scoped development validation, not production readiness, AGI or consciousness evidence.

## FAILURE / RETEST POLICY

Public history should preserve:

```text
PASS
FAIL
INCONCLUSIVE
SUPERSEDED
ROOT CAUSE
REPAIR
RETEST
```

A later PASS does not erase an earlier failure or a weak historical test contract.

## PUBLICATION FIREWALL

Public evidence may contain:

```text
protocols
package IDs
SHA256 references
PASS / FAIL / INCONCLUSIVE / SUPERSEDED
sanitized lifecycle/routing state
counts and benchmark summaries
hardware/model context
claim boundaries
lineage
```

It must not intentionally publish:

```text
private SSI source code
private V10/Micronetwork/ISKRA implementation
private internal file tree
secrets / tokens
private local paths
raw private memory/user data
private prompts/configuration
raw logs or stack traces that disclose implementation
```

The public repository is an evidence mirror, not a source distribution.