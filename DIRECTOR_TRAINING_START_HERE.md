# DIRECTOR Training — Start Here

**Updated:** 2026-09-09  
**Baseline:** `DIRECTOR_FROZEN_C0 / VALIDATED ENGINEERING BASELINE`  
**Training packages:** `2`  
**Status:** `TRAIN08A CLOSED / VERIFIED PASS / 48 OF 48 PASS / FOUNDATION_S1 CREATED`

## Sequence

```text
DIRECTOR_FROZEN_C0
-> TRAIN08A FOUNDATION [CLOSED / VERIFIED PASS / 48 OF 48 PASS]
-> DIRECTOR_FOUNDATION_S1 [CREATED]
-> TRAIN08B LEGO + MICRONETWORK + V10 PRACTICUM [NEXT / NOT YET STARTED]
-> DIRECTOR_TRAINED_START_S2 [NOT YET CLAIMED]
-> RECORD EXACT S2 IDENTITY / HASH
```

`DIRECTOR_FROZEN_C0` remains immutable. Training creates descendants and does not rewrite the frozen C0 baseline.

## TRAIN08A — Foundation

```text
EXECUTED PACKAGE
SSI_TRAIN08A_DIRECTOR_FOUNDATION_V1_20260909_REBUILT_FOR_KILO

TARGET
DIRECTOR_FROZEN_C0

STEPS
48

FINAL RESULT
CLOSED / VERIFIED PASS

STEP OUTCOMES
48 PASS / 0 FAIL / 0 INCONCLUSIVE

BLIND VALIDATIONS
16/16 PASS

CHECKPOINTS
16

FINAL CHECKPOINT
CHECKPOINT_16

OUTPUT STATE
DIRECTOR_FOUNDATION_S1 CREATED

HELD-OUT CONTAMINATION CHECK
PASS

MATERIAL INTEGRITY VIOLATION
false
```

Shared Foundation curriculum identity:

`61a3069ce68d19c64d4ae7c5ebc730d04283d81b2e534f487c3fd5063d9b75b8`

## Predeclaration chronology

The original TRAIN08A package family was committed before the final result was published.

```text
ORIGINAL PREDECLARED PACKAGE
SSI_TRAIN08A_DIRECTOR_FOUNDATION_V1_20260909

ZIP_SHA256
76847299993eb24090921b73de5e0bacb1bc021859327e0cebabf66a5526f739

FROZEN_MANIFEST_SHA256
eb38c5f8d9f914382202d410923c729bbdc3a37439e8450f85d78245a0ec3a27

PREDECLARATION COMMIT
5433200ec2a1b10804050b03df9cf151a26bde0a

PREDECLARATION TIME
2026-09-09T00:00:18Z

FINAL EXECUTION RECORD COMMIT
c7ebcfceda02cee74dd502180ea3097a189dd482

FINAL RECORD TIME
2026-09-09T15:30:27Z
```

This supports that the declared Director Foundation package family, target, step count and curriculum identity existed publicly before the final 48/48 result was published.

## Rebuilt package integrity boundary

The continued execution package is labeled:

```text
SSI_TRAIN08A_DIRECTOR_FOUNDATION_V1_20260909_REBUILT_FOR_KILO
```

The public repository currently does not publish a separate exact ZIP SHA-256 for that rebuilt archive and does not publish a byte-by-byte/file-by-file proof that it is byte-identical to the originally predeclared ZIP.

Therefore the project does **not** claim:

```text
REBUILT PACKAGE = BYTE-FOR-BYTE IDENTICAL TO ORIGINAL PREDECLARED ZIP
REBUILT ZIP SHA256 = PUBLICLY VERIFIED
```

The public evidence supports the narrower continuity claim:

```text
TARGET = DIRECTOR_FROZEN_C0
PHASE = FOUNDATION
UNIQUE STEPS = 48
FOUNDATION CURRICULUM IDENTITY = PRESERVED IN PUBLIC RECORDS
FINAL STEP OUTCOMES = 48/48 PASS
BLIND VALIDATIONS = 16/16 PASS
CHECKPOINTS = 16
HELD-OUT CONTAMINATION CHECK = PASS
MATERIAL INTEGRITY VIOLATION = false
OUTPUT = DIRECTOR_FOUNDATION_S1 CREATED
```

See [`evidence/DIRECTOR_TRAIN08A_REBUILD_INTEGRITY_RECORD_20260909.md`](evidence/DIRECTOR_TRAIN08A_REBUILD_INTEGRITY_RECORD_20260909.md).

## Executor history

TRAIN08A was executed in two auditable segments:

```text
Kiro / kiro-cli / Auto cloud model
steps 01-17

Kilo / kilo-cli / free model
steps 18-48
```

Exact handoff boundary:

```text
step 17 -> step 18
M06 GUIDED_PRACTICE -> M06 BLIND_VALIDATION
executor_transition_step = 18
```

The handoff was caused by exhaustion of Kiro's monthly usage allowance. It was an external service-usage interruption, not a TRAIN08A acceptance failure and not a model switch selected because of a poor Director outcome.

At takeover time, `PROGRESS.json` lagged behind the event log: it reported step 15 as last completed while steps 16-17 were already present as PASS in the preserved events. Kilo reconstructed progress from the evidence and continued from the first unrecorded step 18 rather than restarting or repeating prior work.

Historical Kiro evidence remained preserved.

## Event-log accounting

Final `TRAIN08A_EVENTS.jsonl` contains 67 valid JSON records:

```text
1 INIT
49 step records representing 48 unique steps
16 CHECKPOINT records
1 EXECUTOR_HANDOFF
= 67 total valid JSON events
```

Step 47 appears twice because an original PASS record and a preserved correction record are both retained. The correction fixes a test-oracle arithmetic expectation (`210.0` -> `190.0`, where `50+100+40=190`) rather than silently overwriting the first event.

Curriculum-contained debugging failures may exist inside PASS steps. The public `48/48 PASS` claim refers to the final acceptance outcome of the 48 declared steps, not to an assertion that no intermediate debugging failure occurred.

## Public records

- [`DIRECTOR_TRAIN08A_LIVE_EXECUTION_RECORD_20260909.md`](DIRECTOR_TRAIN08A_LIVE_EXECUTION_RECORD_20260909.md) — same-day interruption/handoff record published before final completion.
- [`DIRECTOR_TRAIN08A_FINAL_EXECUTION_RECORD_20260909.md`](DIRECTOR_TRAIN08A_FINAL_EXECUTION_RECORD_20260909.md) — authoritative final execution result.
- [`evidence/DIRECTOR_TRAIN08A_FINAL_CLOSURE_20260909.md`](evidence/DIRECTOR_TRAIN08A_FINAL_CLOSURE_20260909.md) — formal closure.
- [`evidence/DIRECTOR_TRAIN08A_REBUILD_INTEGRITY_RECORD_20260909.md`](evidence/DIRECTOR_TRAIN08A_REBUILD_INTEGRITY_RECORD_20260909.md) — rebuild/provenance reconciliation.
- [`PREDECLARED_DIRECTOR_TRAINING_PACKAGES_20260909.md`](PREDECLARED_DIRECTOR_TRAINING_PACKAGES_20260909.md) — original precommitment and package hashes.

## TRAIN08B — LEGO + Micronetwork + V10 Practicum

```text
PACKAGE
SSI_TRAIN08B_DIRECTOR_LEGO_MICRONETWORK_PRACTICUM_V1_20260909

REQUIRED START STATE
DIRECTOR_FOUNDATION_S1

STEPS
60

ZIP_SHA256
5db64c0ed006f785e1eb64c611be22d37d9386553f2815cc45fe7a83592cd441

FROZEN_MANIFEST_SHA256
2335793ffa7df41b8a9f9b85e46fc701c325ccf75e6bf3ddba20a204acbff250

STATE
NEXT / NOT_YET_EXECUTED
```

Shared Practicum curriculum identity:

`abc3eccc4e19849f2d3b3be5b1a4d2752377b6024225f0da8d7d54f4ebafc7ce`

## Same methodology, separate state

Director uses the same two curriculum families as BODY_FROZEN and the six ISKRA lines:

```text
A = FOUNDATION
B = LEGO + MICRONETWORK + V10 PRACTICUM
```

But Director training is an independent evidence/history line. It does not share or merge private memory, Experience, lifecycle state or training outcomes with BODY/ISKRA.

## Evidence rule

Training preserves actual outcomes and execution history:

```text
PASS
FAIL
INCONCLUSIVE
INTERRUPTION
RECOVERY
CHECKPOINT
EXECUTOR_HANDOFF
CORRECTION
```

Instruction and guided examples do not count as blind validation. Held-out experiment answers must not be taught during training.

Executor changes must be recorded explicitly and historical evidence must not be erased or rewritten.

## Current truth

```text
DIRECTOR_FROZEN_C0 = CLOSED / VALIDATED IN DECLARED ENGINEERING SCOPE
TRAIN08A = CLOSED / VERIFIED PASS
TRAIN08A STEPS = 48/48 PASS
BLIND VALIDATIONS = 16/16 PASS
CHECKPOINTS = 16 / FINAL CHECKPOINT_16
KIRO -> KILO HANDOFF = STEP 17 -> STEP 18 / RECORDED
DIRECTOR_FOUNDATION_S1 = CREATED
PREDECLARATION BEFORE FINAL RESULT = PUBLICLY TRACEABLE
REBUILD PROVENANCE = DOCUMENTED
REBUILT BYTE-LEVEL EQUIVALENCE = NOT PUBLICLY CLAIMED
TRAIN08B = NEXT / PREDECLARED / NOT YET EXECUTED
DIRECTOR_TRAINED_START_S2 = NOT YET CLAIMED
```

Director integration/C0 record:

- [`DIRECTOR_MAINLINE_BODY_INTEGRATION_20260908.md`](DIRECTOR_MAINLINE_BODY_INTEGRATION_20260908.md)
