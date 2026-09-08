# SSI V5 — Start Here for Grant and Technical Reviewers

**Updated:** 2026-09-09  
**Frozen baseline:** `BODY_FROZEN T0 / PRE-ISKRA / 2026-09-05`  
**Current ISKRA start state:** `6 independent T0 variants / START_STATE_VALIDATED / 2026-09-06`  
**Latest closed validation:** `TEST 5 / DEVELOPMENT_VALIDATED`  
**7-BODY readiness:** `PRE-REPAIR AUDIT 43/43 COMPLETE / FINAL 7/7 NOT YET CLOSED`  
**Training:** `14 HASH-SEALED PACKAGES / PREDECLARED / NOT YET EXECUTED`  
**Mechanism tests:** `7 INDEPENDENT MICRONETWORK + V10 PACKAGES / PREDECLARED / NOT YET EXECUTED`  
**Cross-domain program:** `7 x 3 = 21 EXPERIMENTS / PREDECLARED / OUTCOMES UNKNOWN`  
**Director mainline:** `DIRECTOR_FROZEN_C0 / ENGINEERING BASELINE CLOSED / INTEGRITY VERIFIED`

> **Disclosure boundary:** this repository is a public evidence/review mirror, not a source-code distribution. Proprietary SSI, DIRECTOR, ROBERT, Router V10, Micronetwork and ISKRA implementation code remains private. Public materials describe validated behavior, architecture at a safe level, test status, sanitized evidence and claim boundaries.

## What to understand first

SSI V5 has two explicitly separated tracks.

### Controlled research track

```text
IMMUTABLE T0 CONTROLS
-> 7-BODY TECHNICAL READINESS
-> PRE-REPAIR FINDINGS PRESERVED
-> REPAIR
-> COMMON 7/7 RETEST
-> TRAIN-A FOUNDATION
-> FOUNDATION_S1
-> TRAIN-B PRACTICUM
-> TRAINED_START_S2 + HASH
-> 7 MICRONETWORK + V10 MECHANISM TESTS
-> 21 CROSS-DOMAIN EXPERIMENTS
-> POST-21 CONSOLIDATION
-> 3 NEW DOMAINS
-> LATER EXTERNAL FALSIFICATION CHALLENGES
```

### Parallel canonical engineering track

```text
VALIDATED BODY FOUNDATION
+ EXISTING WORKING DIRECTOR FUNCTIONS
-> NEW CANONICAL DIRECTOR
-> LOCAL DIRECTOR CONTROL PANEL
-> SHARED READ-ONLY REVIEWER OBSERVABILITY
-> RESTART / PERSISTENCE / CHECKPOINT / IPC VALIDATION
-> DIRECTOR_FROZEN_C0
-> LATER DIRECTOR -> ROBERT INTEGRATION
-> LATER WORLD / AGENT INTEGRATION
```

The Director line is **not** a completed BODY experiment and does not rewrite `BODY_FROZEN T0`.

## 7-BODY readiness — current truth

A sequential readiness audit completed all `43/43` declared audit stages on 2026-09-08 in `READ_ONLY / TEST_ONLY` mode.

The audit made:

```text
BODY MODIFICATIONS = 0
AUTOMATIC REPAIRS = 0
```

It also preserved open findings, including a JUSTICE launcher deviation, repeated ISKRA Stage 09 test-fixture failures, a CONTINUUM full-flow orchestrator syntax issue and unequal full-acceptance coverage across lines.

Therefore:

```text
AUDIT COMPLETE = YES
TECHNICAL READINESS CLOSED 7/7 = NO
REPAIR REQUIRED = YES
COMMON RETEST REQUIRED = YES
TRAINING MAY START = NO, until readiness closes
```

This distinction is deliberate: completing the audit procedure is not the same as proving all seven BODY lines ready.

Read first:

- [`7BODY_TECHNICAL_READINESS_START_HERE.md`](7BODY_TECHNICAL_READINESS_START_HERE.md)
- [`evidence/7BODY_TECHNICAL_READINESS_PRE_REPAIR_AUDIT_20260908.md`](evidence/7BODY_TECHNICAL_READINESS_PRE_REPAIR_AUDIT_20260908.md)

## Director mainline — validated C0 baseline

On 2026-09-08 the canonical Director engineering line reached a frozen engineering baseline:

```text
DIRECTOR_FROZEN_C0
```

The implementation remains private. What is publicly stated is the sanitized, tested state.

Validated in the C0 scope:

```text
LOCAL DIRECTOR RUNTIME = RUNNING / validated
SINGLE RUNTIME PROTECTION = PASS
IPC = ACTIVE / validated
START / STOP / RESTART / STATUS = PASS
CHECKPOINT + RESTART/PERSISTENCE = PASS
CONTINUUM local integration = ACTIVE / validated
LAB integration = ACTIVE / validated
MICRONETWORK integration = validated
ROUTER V10 integration = validated
COLLECTIVE INTELLIGENCE status = validated
PERSISTENT CONVERSATION MEMORY = validated across restart
LOCAL DIRECTOR CONTROL PANEL = PASS
SHARED WWW INTERFACE = PASS / OBSERVER_ONLY
ROOT commands in shared WWW = NOT EXPOSED
HARDWARE STATUS incl. NVIDIA GPU/VRAM = validated
MODEL/BACKEND STATUS = validated in C0 scope
CENTRAL DIRECTOR NODE = intentionally OFFLINE / LOCAL-ONLY mode
```

Final C0 verification recorded:

```text
FINAL PANEL / SYSTEM CHECKS = 27/27 PASS
SELECTED PYTEST VALIDATION = 19/19 PASS
INDEPENDENCE VALIDATION = PASS
FREEZE MANIFEST = CREATED
FREEZE INTEGRITY = VERIFIED
```

This is a scoped internal engineering-validation baseline, not an external certification or production-readiness claim.

Reference:

- [`DIRECTOR_MAINLINE_BODY_INTEGRATION_20260908.md`](DIRECTOR_MAINLINE_BODY_INTEGRATION_20260908.md)

## Local Director Control Panel

The Director mainline includes a validated **local Director Control Panel** for the project owner/operator.

Its purpose is to consolidate routine operational functions that would otherwise require multiple terminal windows, including runtime state, authorized ROOT access, checkpoint/persistence visibility, model/provider status, V10/Micronetwork status, Pocket status, diagnostics and hardware/resource monitoring.

It does **not** create a second runtime, second CONTINUUM or alternative execution authority.

It must not be confused with the shared reviewer interface.

```text
DIRECTOR CONTROL PANEL
= LOCAL
= OWNER / OPERATOR
= AUTHORIZED EXECUTION + ADMINISTRATION
= EXISTING CONTROL PATHS ONLY

SHARED REVIEWER INTERFACE
= OBSERVER_ONLY
= READ-ONLY
= SANITIZED OBSERVABILITY
= NO ROOT
= NO REMOTE EXECUTION
```

The separation between owner control and reviewer observability is a deliberate security boundary and is validated in the C0 scope.

## Pre-experiment training

Training remains predeclared and not yet executed.

```text
7 BODY LINES x 2 TRAINING PHASES = 14 PACKAGES
```

Phase A — Foundation:

```text
programming
+ debugging
+ task decomposition
+ task/project management
+ testing/evidence
+ checkpoints
+ resource-aware execution
```

Phase B — Practicum:

```text
LEGO composition
+ Micronetwork lifecycle use
+ V10 route choice
+ reuse / verify / full-flow
+ false-reuse protection
+ controlled failure
+ anti-loop / recovery
+ persistence/restart
+ route-cost measurement
```

Training is separated from held-out experiment vectors. A worked/guided example does not count as independent blind-validation evidence.

Shared curriculum hashes:

```text
FOUNDATION_CURRICULUM_SHA256
= 61a3069ce68d19c64d4ae7c5ebc730d04283d81b2e534f487c3fd5063d9b75b8

PRACTICUM_CURRICULUM_SHA256
= abc3eccc4e19849f2d3b3be5b1a4d2752377b6024225f0da8d7d54f4ebafc7ce
```

References:

- [`PREEXPERIMENT_TRAINING_PROGRAM_20260908.md`](PREEXPERIMENT_TRAINING_PROGRAM_20260908.md)
- [`PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md`](PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md)
- [`TRAINING_PACKAGES_START_HERE.md`](TRAINING_PACKAGES_START_HERE.md)

## Relationship to the seven mechanism-test packages

The seven Micronetwork + V10 experiment packages are already hash-sealed historical precommitments.

Current truth:

```text
PREDECLARED = YES
HASH-SEALED = YES
EXECUTED = NO
OUTCOMES = UNKNOWN
```

After training, the exact `TRAINED_START_S2` state must be recorded and checked against the frozen experiment contract. A material change requires a new package version/hash rather than silently editing the old one.

Reference:

- [`PREDECLARED_7BODY_MICRONETWORK_V10_PACKAGES_20260908.md`](PREDECLARED_7BODY_MICRONETWORK_V10_PACKAGES_20260908.md)

## 21-experiment program

```text
7 LINES
= BODY_FROZEN
+ NICE
+ GUARDIAN
+ JUSTICE
+ EXPLORER
+ PRAGMATIST
+ SKEPTIC

3 EXPERIMENTS PER LINE
= DRONES
+ HUMANOID
+ NEW DOMAIN SELECTED BY THAT SSI LINE

TOTAL = 21
STATUS = PREDECLARED / FINAL OUTCOMES UNKNOWN
```

References:

- [`EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md`](EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md)
- [`EXPERIMENT_EXECUTION_METHODOLOGY_20260906.md`](EXPERIMENT_EXECUTION_METHODOLOGY_20260906.md)

## Current established evidence

```text
BODY_FROZEN T0 = preserved immutable origin / 2026-09-05
6 ISKRA T0 variants = recorded / 2026-09-06
START_STATE_QA = 8/8 per agent
GROUP_QA = 48/48 PASS
TEST 5 = 29/29 acceptance
TEST 5 TOTAL REGRESSION = 524/524 PASS
OPEN BLOCKERS IN TEST 5 SCOPE = 0
7-BODY PRE-REPAIR AUDIT = 43/43 PROCEDURE COMPLETE
7-BODY FINAL READINESS = NOT YET CLOSED
DIRECTOR_FROZEN_C0 = CLOSED ENGINEERING BASELINE / INTEGRITY VERIFIED
DIRECTOR FINAL PANEL/SYSTEM CHECKS = 27/27 PASS
DIRECTOR SELECTED PYTEST = 19/19 PASS
```

## Current unknowns / not yet claimed

```text
7-BODY repair/retest PASS
TRAIN-A outcomes
TRAIN-B outcomes
FOUNDATION_S1 contents
TRAINED_START_S2 contents
7 mechanism-test outcomes
21 cross-domain outcomes
Director -> ROBERT integration
Director control of experimental ISKRA lines
post-21 consolidation outcome
three-new-domain result
long-run ISKRA divergence
physical drone/humanoid validation
external replication
AGI / consciousness / production readiness
```

## Public/private boundary

Public review materials may expose sanitized architecture descriptions, declared protocols, scoped results, hashes/manifests where safe, failures/repairs/retests and reviewer-facing status summaries.

They do **not** expose proprietary source code, private execution logic, credentials, API keys, tokens, private configuration, internal prompts or data that would materially reconstruct the private implementation.

## Recommended reading order

1. [`README.md`](README.md)
2. [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md)
3. [`7BODY_TECHNICAL_READINESS_START_HERE.md`](7BODY_TECHNICAL_READINESS_START_HERE.md)
4. [`DIRECTOR_MAINLINE_BODY_INTEGRATION_20260908.md`](DIRECTOR_MAINLINE_BODY_INTEGRATION_20260908.md)
5. [`PREEXPERIMENT_TRAINING_PROGRAM_20260908.md`](PREEXPERIMENT_TRAINING_PROGRAM_20260908.md)
6. [`PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md`](PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md)
7. [`CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md`](CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md)
8. [`PREDECLARED_7BODY_MICRONETWORK_V10_PACKAGES_20260908.md`](PREDECLARED_7BODY_MICRONETWORK_V10_PACKAGES_20260908.md)
9. [`REVIEWER_LIVE_INTERFACE_20260907.md`](REVIEWER_LIVE_INTERFACE_20260907.md)
10. [`evidence/README.md`](evidence/README.md)

The repository should be read with a strict separation between **historical evidence, closed engineering baselines, current implementation work, predeclared future work and executed outcomes**.