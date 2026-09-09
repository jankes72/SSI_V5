# SSI V5 — Start Here for Grant and Technical Reviewers

**Updated:** 2026-09-09  
**Frozen baseline:** `BODY_FROZEN T0 / PRE-ISKRA / 2026-09-05`  
**Current ISKRA start state:** `6 independent T0 variants / START_STATE_VALIDATED / 2026-09-06`  
**Latest closed development validation:** `TEST 5 / DEVELOPMENT_VALIDATED`  
**7-BODY readiness:** `CLOSED / 7 OF 7 PASS / 147 OF 147 A01-A21 CELLS PASS`  
**BODY/ISKRA immediate research stage:** `TRAIN-A FOUNDATION / GATE OPEN / NOT YET EXECUTED`  
**Director Foundation training:** `TRAIN08A COMPLETE / 48 OF 48 PASS / FOUNDATION_S1 CREATED`  
**Training package set:** `14 HASH-SEALED PACKAGES / 7 BODY x 2 PHASES`  
**Mechanism tests:** `7 INDEPENDENT MICRONETWORK + V10 PACKAGES / PREDECLARED / NOT YET EXECUTED`  
**Cross-domain program:** `7 x 3 = 21 EXPERIMENTS / PREDECLARED / OUTCOMES UNKNOWN`

> **Disclosure boundary:** this repository is a public evidence/review mirror, not a source-code distribution. Proprietary SSI, DIRECTOR, ROBERT, Router V10, Micronetwork and ISKRA implementation code remains private. Public materials describe validated behavior, architecture at a safe level, test status, sanitized evidence and claim boundaries.

## What to understand first

SSI V5 has two deliberately separated tracks.

### Controlled BODY/ISKRA research track

```text
IMMUTABLE T0 CONTROLS
-> 7-BODY TECHNICAL READINESS = CLOSED 7/7 PASS
-> TRAIN-A FOUNDATION = NEXT
-> FOUNDATION_S1
-> TRAIN-B PRACTICUM
-> TRAINED_START_S2 + HASH
-> 7 MICRONETWORK + V10 MECHANISM TESTS
-> 21 CROSS-DOMAIN EXPERIMENTS
-> POST-21 CONSOLIDATION
-> 3 NEW DOMAINS
-> LATER EXTERNAL FALSIFICATION CHALLENGES
```

### Parallel Director engineering/training track

```text
VALIDATED BODY FOUNDATION
+ EXISTING WORKING DIRECTOR FUNCTIONS
-> NEW CANONICAL DIRECTOR
-> DIRECTOR_FROZEN_C0
-> TRAIN08A FOUNDATION = COMPLETE / 48 OF 48 PASS
-> DIRECTOR_FOUNDATION_S1 = CREATED
-> TRAIN08B PRACTICUM = NEXT / NOT YET EXECUTED
-> DIRECTOR_TRAINED_START_S2 = FUTURE
-> LATER DIRECTOR -> ROBERT INTEGRATION
```

The Director line is not a completed BODY experiment and does not rewrite `BODY_FROZEN T0`.

## 7-BODY readiness — final truth

The original sequential audit completed `43/43` declared audit stages on 2026-09-08 in `READ_ONLY / TEST_ONLY` mode and preserved real pre-repair findings.

Those findings were not hidden. The later repair/retest stage closed the technical-readiness gate:

```text
BODY_FROZEN        = PASS
ISKRA 1 NICE       = PASS
ISKRA 2 GUARDIAN   = PASS
ISKRA 3 JUSTICE    = PASS
ISKRA 4 EXPLORER   = PASS
ISKRA 5 PRAGMATIST = PASS
ISKRA 6 SKEPTIC    = PASS

GLOBAL = 7/7 PASS
A01-A21 x 7 = 147/147 PASS
CLOSURE VALIDATOR = PASS
```

Final package integrity reference:

```text
SSI_7BODY_READINESS_REPAIR_RETEST_KILO_V1_20260908(3).zip
SHA256 = 543092a3fe51540405d771415ffd25c376201e1aaa739ce4f8a672a8a41ac1d8
```

Actual restart/persistence scope in this package was `1 controlled restart per BODY`; no `20/20` claim is made. A launcher PID/status observability discrepancy remains explicitly recorded as a `KNOWN NON-BLOCKING ISSUE`.

Read first:

- [`7BODY_TECHNICAL_READINESS_START_HERE.md`](7BODY_TECHNICAL_READINESS_START_HERE.md)
- [`evidence/7BODY_TECHNICAL_READINESS_PRE_REPAIR_AUDIT_20260908.md`](evidence/7BODY_TECHNICAL_READINESS_PRE_REPAIR_AUDIT_20260908.md)
- [`evidence/7BODY_TECHNICAL_READINESS_FINAL_CLOSURE_20260909.md`](evidence/7BODY_TECHNICAL_READINESS_FINAL_CLOSURE_20260909.md)

## BODY/ISKRA immediate next stage — TRAIN-A FOUNDATION

The readiness gate is no longer blocking training for the seven controlled BODY/ISKRA lines.

```text
7 BODY/ISKRA TRAIN-A RUNS = NOT YET EXECUTED
7 BODY/ISKRA FOUNDATION_S1 STATES = NOT YET CLAIMED
```

This remains separate from the Director TRAIN08A result below.

References:

- [`TRAINING_PACKAGES_START_HERE.md`](TRAINING_PACKAGES_START_HERE.md)
- [`PREEXPERIMENT_TRAINING_PROGRAM_20260908.md`](PREEXPERIMENT_TRAINING_PROGRAM_20260908.md)
- [`PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md`](PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md)

## Director TRAIN08A — first completed Foundation acquisition run

The separate Director line has completed TRAIN08A against `DIRECTOR_FROZEN_C0`.

```text
RESULT = PASS
STEPS = 48/48 PASS
FAIL = 0
INCONCLUSIVE = 0
BLIND VALIDATIONS = 16/16 PASS
CHECKPOINTS = 16
FINAL CHECKPOINT = CHECKPOINT_16
OUTPUT STATE = DIRECTOR_FOUNDATION_S1 CREATED
```

Execution history is explicitly preserved:

```text
Kiro = steps 01-17
Kilo = steps 18-48
handoff boundary = step 17 -> step 18
```

Kiro stopped accepting requests after the account reached its monthly usage limit. This was an external service-usage interruption, not a TRAIN08A acceptance failure. The handoff was recorded while the final outcome was still unknown.

At takeover, `PROGRESS.json` lagged behind the event log: it reported step 15 while steps 16-17 were already present as PASS. Kilo reconstructed progress from preserved evidence and resumed from step 18 rather than restarting.

Final event-log accounting:

```text
67 valid JSON records
48 unique training steps
16 checkpoints
1 executor handoff
1 preserved correction event for step 47
```

The step-47 correction preserves both records and corrects a test-oracle arithmetic expectation from `210.0` to `190.0` (`50+100+40=190`).

Read:

- [`DIRECTOR_TRAINING_START_HERE.md`](DIRECTOR_TRAINING_START_HERE.md)
- [`DIRECTOR_TRAIN08A_LIVE_EXECUTION_RECORD_20260909.md`](DIRECTOR_TRAIN08A_LIVE_EXECUTION_RECORD_20260909.md)
- [`DIRECTOR_TRAIN08A_FINAL_EXECUTION_RECORD_20260909.md`](DIRECTOR_TRAIN08A_FINAL_EXECUTION_RECORD_20260909.md)

## Director next gate

```text
DIRECTOR_FOUNDATION_S1
-> TRAIN08B LEGO + MICRONETWORK + V10 PRACTICUM
-> DIRECTOR_TRAINED_START_S2
```

TRAIN08B has not yet been executed and S2 is not claimed.

## Current established evidence

```text
BODY_FROZEN T0 = preserved immutable origin / 2026-09-05
6 ISKRA T0 variants = recorded / 2026-09-06
START_STATE_QA = 8/8 per agent
GROUP_QA = 48/48 PASS
TEST 5 = 29/29 acceptance
TEST 5 TOTAL REGRESSION = 524/524 PASS
7-BODY FINAL READINESS = 7/7 PASS
A01-A21 COMMON MATRIX = 147/147 PASS
DIRECTOR_FROZEN_C0 = CLOSED ENGINEERING BASELINE / INTEGRITY VERIFIED
DIRECTOR TRAIN08A = 48/48 PASS
DIRECTOR TRAIN08A BLIND VALIDATIONS = 16/16 PASS
DIRECTOR FOUNDATION_S1 = CREATED BY DECLARED TRAIN08A PROCEDURE
```

## Current unknowns / not yet claimed

```text
7 BODY/ISKRA TRAIN-A outcomes
7 BODY/ISKRA FOUNDATION_S1 states
Director TRAIN08B outcome
DIRECTOR_TRAINED_START_S2
7 mechanism-test outcomes
21 cross-domain outcomes
Director -> ROBERT integration
post-21 consolidation outcome
three-new-domain result
long-run ISKRA divergence
physical drone/humanoid validation
external replication
AGI / consciousness / production readiness
```

## Recommended reading order

1. [`README.md`](README.md)
2. [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md)
3. [`DIRECTOR_TRAINING_START_HERE.md`](DIRECTOR_TRAINING_START_HERE.md)
4. [`DIRECTOR_TRAIN08A_FINAL_EXECUTION_RECORD_20260909.md`](DIRECTOR_TRAIN08A_FINAL_EXECUTION_RECORD_20260909.md)
5. [`DIRECTOR_TRAIN08A_LIVE_EXECUTION_RECORD_20260909.md`](DIRECTOR_TRAIN08A_LIVE_EXECUTION_RECORD_20260909.md)
6. [`7BODY_TECHNICAL_READINESS_START_HERE.md`](7BODY_TECHNICAL_READINESS_START_HERE.md)
7. [`evidence/7BODY_TECHNICAL_READINESS_FINAL_CLOSURE_20260909.md`](evidence/7BODY_TECHNICAL_READINESS_FINAL_CLOSURE_20260909.md)
8. [`TRAINING_PACKAGES_START_HERE.md`](TRAINING_PACKAGES_START_HERE.md)
9. [`CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md`](CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md)

The repository should be read with a strict separation between historical evidence, closed readiness/engineering baselines, actual executed training outcomes and prepared future work.