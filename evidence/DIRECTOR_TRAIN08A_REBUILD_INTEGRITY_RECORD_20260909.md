# DIRECTOR TRAIN08A — Rebuild Integrity and Provenance Record

**Date:** `2026-09-09`  
**Scope:** `TRAIN08A FOUNDATION / package provenance after Kiro -> Kilo handoff`  
**Status:** `DOCUMENTED / BYTE-LEVEL EQUIVALENCE NOT PUBLICLY CLAIMED`  
**Target baseline:** `DIRECTOR_FROZEN_C0`  
**Final output:** `DIRECTOR_FOUNDATION_S1`

## Purpose

This record closes a documentation gap between the package that was publicly predeclared before execution and the package label used for the continued Kilo execution after the Kiro service-limit interruption.

It is intentionally conservative. It records what the public evidence establishes and separately records what the current public repository does **not** establish.

## Predeclared TRAIN08A identity

Before the final TRAIN08A result was known, the Director Foundation package was publicly predeclared as:

```text
PACKAGE
SSI_TRAIN08A_DIRECTOR_FOUNDATION_V1_20260909

TARGET
DIRECTOR_FROZEN_C0

PHASE
FOUNDATION

STEPS
48

ZIP_SHA256
76847299993eb24090921b73de5e0bacb1bc021859327e0cebabf66a5526f739

FROZEN_MANIFEST_SHA256
eb38c5f8d9f914382202d410923c729bbdc3a37439e8450f85d78245a0ec3a27

FOUNDATION_CURRICULUM_SHA256
61a3069ce68d19c64d4ae7c5ebc730d04283d81b2e534f487c3fd5063d9b75b8
```

The predeclaration was committed before publication of the final result:

```text
PREDECLARATION COMMIT
5433200ec2a1b10804050b03df9cf151a26bde0a

COMMIT TIME
2026-09-09T00:00:18Z

COMMIT MESSAGE
Predeclare Director training packages
```

The later final execution record was committed after completion:

```text
FINAL EXECUTION RECORD COMMIT
c7ebcfceda02cee74dd502180ea3097a189dd482

COMMIT TIME
2026-09-09T15:30:27Z

COMMIT MESSAGE
Publish final DIRECTOR TRAIN08A 48/48 execution record
```

Therefore the public chronology supports that the package family, target, phase, step count and curriculum identity were recorded before the final 48/48 result was published.

## Executed continuation label

The final execution records identify the continued package as:

```text
SSI_TRAIN08A_DIRECTOR_FOUNDATION_V1_20260909_REBUILT_FOR_KILO
```

The rebuild/continuation occurred in the context of the executor transition:

```text
Kiro = steps 01-17
Kilo = steps 18-48
handoff = step 17 -> step 18
executor_transition_step = 18
```

The handoff followed exhaustion of the Kiro monthly usage allowance. The interruption was external to the TRAIN08A acceptance result and was documented before the final result was known.

## Scope continuity supported by public evidence

The current public records support continuity of the declared TRAIN08A training scope at the following level:

```text
TARGET BASELINE = DIRECTOR_FROZEN_C0
TRAINING PHASE = FOUNDATION
DECLARED UNIQUE STEPS = 48
FINAL UNIQUE STEP OUTCOMES = 48 PASS / 0 FAIL / 0 INCONCLUSIVE
BLIND VALIDATIONS = 16/16 PASS
CHECKPOINTS = 16
FINAL CHECKPOINT = CHECKPOINT_16
FOUNDATION CURRICULUM IDENTITY = 61a3069ce68d19c64d4ae7c5ebc730d04283d81b2e534f487c3fd5063d9b75b8
OUTPUT STATE = DIRECTOR_FOUNDATION_S1 CREATED
HELD-OUT CONTAMINATION CHECK = PASS
MATERIAL INTEGRITY VIOLATION = false
```

The execution history also preserves the progress/event-log discrepancy at takeover:

```text
PROGRESS.json last completed = step 15
EVENT LOG already contained = step 16 PASS + step 17 PASS
RESUME POINT = first unrecorded step 18
```

No restart from step 1 and no deletion of the earlier Kiro history is claimed.

## What is not publicly established

The repository currently does **not** publish a separate exact ZIP SHA-256 for:

```text
SSI_TRAIN08A_DIRECTOR_FOUNDATION_V1_20260909_REBUILT_FOR_KILO
```

It also does not currently publish a byte-by-byte or file-by-file diff proving that the rebuilt package is byte-identical to the originally predeclared ZIP.

Therefore the public project does **not** make either of these stronger claims:

```text
REBUILT_ZIP_SHA256 = VERIFIED PUBLICLY
REBUILT_PACKAGE = BYTE-FOR-BYTE IDENTICAL TO PREDECLARED ZIP
```

The correct public statement is narrower:

> TRAIN08A was predeclared before its final result, the executor interruption and handoff were preserved, the final records report continuity of the declared 48-step Foundation scope and shared Foundation curriculum identity, and the final evidence records no material integrity violation; however, exact byte-level equivalence of the `REBUILT_FOR_KILO` archive to the original predeclared ZIP is not independently established by a separately published rebuilt-package hash/diff in this repository.

## Step 47 correction boundary

The final event log contains 49 step-event records representing 48 unique steps because step 47 has two preserved PASS records.

The correction changes a test-oracle arithmetic expectation from `210.0` to `190.0`:

```text
50 + 100 + 40 = 190
```

The original record remains preserved. This is documented as a test-oracle correction rather than a hidden rewrite of the execution history.

## Evidence hierarchy for TRAIN08A

For current review, use the following order:

1. `DIRECTOR_TRAIN08A_FINAL_EXECUTION_RECORD_20260909.md` — authoritative final execution result.
2. `evidence/DIRECTOR_TRAIN08A_FINAL_CLOSURE_20260909.md` — formal closed verdict and claim boundary.
3. `DIRECTOR_TRAIN08A_LIVE_EXECUTION_RECORD_20260909.md` — preserved interruption/handoff record written before the final result was known.
4. `PREDECLARED_DIRECTOR_TRAINING_PACKAGES_20260909.md` — historical precommitment and original package hashes.
5. This record — rebuild/provenance reconciliation and exact public integrity boundary.

## Current verdict

```text
TRAIN08A RESULT = CLOSED / VERIFIED PASS
48/48 UNIQUE STEPS = PASS
16/16 BLIND VALIDATIONS = PASS
16 CHECKPOINTS = PRESENT
DIRECTOR_FOUNDATION_S1 = CREATED
PREDECLARATION BEFORE FINAL RESULT = PUBLICLY TRACEABLE
KIRO -> KILO HANDOFF = PUBLICLY PRESERVED
REBUILD PROVENANCE = DOCUMENTED
REBUILT BYTE-LEVEL EQUIVALENCE = NOT PUBLICLY CLAIMED
TRAIN08B = NEXT / NOT YET EXECUTED
DIRECTOR_TRAINED_START_S2 = NOT YET CLAIMED
```

## Claim boundary

This provenance record strengthens auditability; it does not convert TRAIN08A into external independent scientific validation, production certification, universal competence evidence, AGI evidence or consciousness evidence.

If a future sanitized integrity export publishes an exact hash and permitted diff/manifest comparison for the rebuilt archive, this record may be extended with that stronger evidence. Until then, the narrower boundary above is authoritative.
