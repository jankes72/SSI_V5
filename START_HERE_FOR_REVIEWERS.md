# SSI V5 — Start Here for Grant and Technical Reviewers

**Updated:** 2026-09-09  
**Frozen baseline:** `BODY_FROZEN T0 / PRE-ISKRA / 2026-09-05`  
**Current ISKRA start state:** `6 independent T0 variants / START_STATE_VALIDATED / 2026-09-06`  
**Latest closed development validation:** `TEST 5 / DEVELOPMENT_VALIDATED`  
**7-BODY readiness:** `CLOSED / 7 OF 7 PASS / 147 OF 147 A01-A21 CELLS PASS`  
**BODY/ISKRA immediate research stage:** `TRAIN-A FOUNDATION / GATE OPEN / NOT YET EXECUTED`  
**Director Foundation training:** `TRAIN08A CLOSED / VERIFIED PASS / 48 OF 48 PASS / FOUNDATION_S1 CREATED`  
**Director next gate:** `TRAIN08B LEGO + MICRONETWORK + V10 PRACTICUM / PREDECLARED / NOT YET EXECUTED`  
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
-> TRAIN08A FOUNDATION = CLOSED / VERIFIED PASS / 48 OF 48 PASS
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

## Director TRAIN08A — CLOSED / VERIFIED PASS

The separate Director line completed TRAIN08A against `DIRECTOR_FROZEN_C0`.

```text
RESULT = CLOSED / VERIFIED PASS
STEPS = 48/48 PASS
FAIL = 0
INCONCLUSIVE = 0
BLIND VALIDATIONS = 16/16 PASS
CHECKPOINTS = 16
FINAL CHECKPOINT = CHECKPOINT_16
OUTPUT STATE = DIRECTOR_FOUNDATION_S1 CREATED
HELD-OUT CONTAMINATION CHECK = PASS
MATERIAL INTEGRITY VIOLATION = false
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

### Predeclaration and rebuild integrity

The original Director TRAIN08A package was publicly predeclared before publication of the final result:

```text
PREDECLARATION COMMIT
5433200ec2a1b10804050b03df9cf151a26bde0a
2026-09-09T00:00:18Z

FINAL EXECUTION RECORD COMMIT
c7ebcfceda02cee74dd502180ea3097a189dd482
2026-09-09T15:30:27Z
```

Original predeclared identity:

```text
PACKAGE = SSI_TRAIN08A_DIRECTOR_FOUNDATION_V1_20260909
STEPS = 48
ZIP_SHA256 = 76847299993eb24090921b73de5e0bacb1bc021859327e0cebabf66a5526f739
FROZEN_MANIFEST_SHA256 = eb38c5f8d9f914382202d410923c729bbdc3a37439e8450f85d78245a0ec3a27
FOUNDATION_CURRICULUM_SHA256 = 61a3069ce68d19c64d4ae7c5ebc730d04283d81b2e534f487c3fd5063d9b75b8
```

The continued execution package is labeled:

```text
SSI_TRAIN08A_DIRECTOR_FOUNDATION_V1_20260909_REBUILT_FOR_KILO
```

The public repository does not currently publish a separate exact ZIP SHA-256 for this rebuilt archive or a byte-by-byte/file-by-file equivalence proof against the original predeclared ZIP. Therefore SSI does **not** claim byte-level identity of the rebuilt archive. The supported public claim is continuity of the declared 48-step Foundation scope, target, curriculum identity, preserved executor handoff and final evidence state with `material_integrity_violation = false`.

Read:

- [`DIRECTOR_TRAINING_START_HERE.md`](DIRECTOR_TRAINING_START_HERE.md)
- [`DIRECTOR_TRAIN08A_LIVE_EXECUTION_RECORD_20260909.md`](DIRECTOR_TRAIN08A_LIVE_EXECUTION_RECORD_20260909.md)
- [`DIRECTOR_TRAIN08A_FINAL_EXECUTION_RECORD_20260909.md`](DIRECTOR_TRAIN08A_FINAL_EXECUTION_RECORD_20260909.md)
- [`evidence/DIRECTOR_TRAIN08A_FINAL_CLOSURE_20260909.md`](evidence/DIRECTOR_TRAIN08A_FINAL_CLOSURE_20260909.md)
- [`evidence/DIRECTOR_TRAIN08A_REBUILD_INTEGRITY_RECORD_20260909.md`](evidence/DIRECTOR_TRAIN08A_REBUILD_INTEGRITY_RECORD_20260909.md)

## Director next gate

```text
DIRECTOR_FOUNDATION_S1
-> TRAIN08B LEGO + MICRONETWORK + V10 PRACTICUM
-> DIRECTOR_TRAINED_START_S2
```

TRAIN08B has not yet been executed and S2 is not claimed.

The predeclared TRAIN08B package remains:

```text
SSI_TRAIN08B_DIRECTOR_LEGO_MICRONETWORK_PRACTICUM_V1_20260909
STEPS = 60
ZIP_SHA256 = 5db64c0ed006f785e1eb64c611be22d37d9386553f2815cc45fe7a83592cd441
FROZEN_MANIFEST_SHA256 = 2335793ffa7df41b8a9f9b85e46fc701c325ccf75e6bf3ddba20a204acbff250
PRACTICUM_CURRICULUM_SHA256 = abc3eccc4e19849f2d3b3be5b1a4d2752377b6024225f0da8d7d54f4ebafc7ce
```

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
DIRECTOR TRAIN08A = CLOSED / VERIFIED PASS / 48/48 PASS
DIRECTOR TRAIN08A BLIND VALIDATIONS = 16/16 PASS
DIRECTOR FOUNDATION_S1 = CREATED BY DECLARED TRAIN08A PROCEDURE
TRAIN08A PREDECLARATION BEFORE FINAL RESULT = PUBLICLY TRACEABLE
KIRO -> KILO HANDOFF = PUBLICLY PRESERVED
```

## Current unknowns / not yet claimed

```text
exact rebuilt TRAIN08A ZIP SHA256
byte-for-byte rebuilt/original package equivalence
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
4. [`evidence/DIRECTOR_TRAIN08A_REBUILD_INTEGRITY_RECORD_20260909.md`](evidence/DIRECTOR_TRAIN08A_REBUILD_INTEGRITY_RECORD_20260909.md)
5. [`DIRECTOR_TRAIN08A_FINAL_EXECUTION_RECORD_20260909.md`](DIRECTOR_TRAIN08A_FINAL_EXECUTION_RECORD_20260909.md)
6. [`evidence/DIRECTOR_TRAIN08A_FINAL_CLOSURE_20260909.md`](evidence/DIRECTOR_TRAIN08A_FINAL_CLOSURE_20260909.md)
7. [`DIRECTOR_TRAIN08A_LIVE_EXECUTION_RECORD_20260909.md`](DIRECTOR_TRAIN08A_LIVE_EXECUTION_RECORD_20260909.md)
8. [`PREDECLARED_DIRECTOR_TRAINING_PACKAGES_20260909.md`](PREDECLARED_DIRECTOR_TRAINING_PACKAGES_20260909.md)
9. [`7BODY_TECHNICAL_READINESS_START_HERE.md`](7BODY_TECHNICAL_READINESS_START_HERE.md)
10. [`evidence/7BODY_TECHNICAL_READINESS_FINAL_CLOSURE_20260909.md`](evidence/7BODY_TECHNICAL_READINESS_FINAL_CLOSURE_20260909.md)
11. [`TRAINING_PACKAGES_START_HERE.md`](TRAINING_PACKAGES_START_HERE.md)
12. [`CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md`](CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md)

The repository should be read with a strict separation between historical evidence, closed readiness/engineering baselines, actual executed training outcomes and prepared future work.