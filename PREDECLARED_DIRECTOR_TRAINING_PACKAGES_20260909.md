# SSI V5 — Predeclared DIRECTOR Training Packages

**Recorded:** `2026-09-09`  
**Historical purpose:** `PREDECLARATION / HASH-SEAL BEFORE EXECUTION`  
**Current registry status:** `TRAIN08A CLOSED / VERIFIED PASS; TRAIN08B PREDECLARED / NOT YET EXECUTED`  
**Target baseline:** `DIRECTOR_FROZEN_C0`  
**Packages:** `2`  
**Training model:** same two-phase methodology used for BODY_FROZEN and the six ISKRA lines

This record preserves the original Director training precommitment and now also links that precommitment to the later observed execution state. Historical predeclaration facts are not rewritten or removed.

`DIRECTOR_FROZEN_C0` remains an immutable engineering baseline. Training creates versioned descendants rather than modifying C0 in place.

## Predeclaration chronology

The Director package family was committed before the final TRAIN08A result was published.

```text
PREDECLARATION COMMIT
5433200ec2a1b10804050b03df9cf151a26bde0a

TIME
2026-09-09T00:00:18Z

MESSAGE
Predeclare Director training packages
```

The final execution record was published later:

```text
FINAL EXECUTION RECORD COMMIT
c7ebcfceda02cee74dd502180ea3097a189dd482

TIME
2026-09-09T15:30:27Z

MESSAGE
Publish final DIRECTOR TRAIN08A 48/48 execution record
```

This chronology supports that the package family, target, curriculum identity and declared step count existed publicly before the final 48/48 result was published.

## Shared curriculum identities

The Director uses the same declared curriculum families already frozen for BODY_FROZEN and ISKRA:

```text
FOUNDATION_CURRICULUM_SHA256
= 61a3069ce68d19c64d4ae7c5ebc730d04283d81b2e534f487c3fd5063d9b75b8

PRACTICUM_CURRICULUM_SHA256
= abc3eccc4e19849f2d3b3be5b1a4d2752377b6024225f0da8d7d54f4ebafc7ce
```

This means the Director is trained under the same general methodological rules as the seven BODY research lines while preserving its own independent state, history and engineering role.

## Package registry

| Package | Target/start state | Phase | Steps | ZIP SHA-256 | Frozen-manifest SHA-256 | Current state |
|---|---|---|---:|---|---|---|
| `SSI_TRAIN08A_DIRECTOR_FOUNDATION_V1_20260909` | `DIRECTOR_FROZEN_C0` | FOUNDATION | 48 | `76847299993eb24090921b73de5e0bacb1bc021859327e0cebabf66a5526f739` | `eb38c5f8d9f914382202d410923c729bbdc3a37439e8450f85d78245a0ec3a27` | `HISTORICAL PREDECLARED PACKAGE; TRAIN08A LATER CLOSED / VERIFIED PASS` |
| `SSI_TRAIN08B_DIRECTOR_LEGO_MICRONETWORK_PRACTICUM_V1_20260909` | `DIRECTOR_FOUNDATION_S1` | LEGO + MICRONETWORK + V10 PRACTICUM | 60 | `5db64c0ed006f785e1eb64c611be22d37d9386553f2815cc45fe7a83592cd441` | `2335793ffa7df41b8a9f9b85e46fc701c325ccf75e6bf3ddba20a204acbff250` | `PREDECLARED / NOT_YET_EXECUTED` |

The ZIP hashes above identify the exact originally generated package bytes. They must not be silently reassigned to later rebuilt package bytes.

## TRAIN08A execution reconciliation

The final TRAIN08A execution records identify the continued package as:

```text
SSI_TRAIN08A_DIRECTOR_FOUNDATION_V1_20260909_REBUILT_FOR_KILO
```

Final observed result:

```text
TRAIN08A = CLOSED / VERIFIED PASS
48/48 unique steps = PASS
0 FAIL
0 INCONCLUSIVE
16/16 blind validations = PASS
16 checkpoints = present
final checkpoint = CHECKPOINT_16
DIRECTOR_FOUNDATION_S1 = CREATED
held-out contamination check = PASS
material integrity violation = false
```

Executor continuity:

```text
Kiro = steps 01-17
Kilo = steps 18-48
handoff = step 17 -> step 18
```

The Kiro interruption was caused by exhaustion of its monthly usage allowance, not by a TRAIN08A acceptance failure.

At handoff, `PROGRESS.json` reported step 15 while the append-only event log already contained PASS records for steps 16-17. The continuation reconstructed state from preserved evidence and resumed from step 18 without deleting the earlier history.

## Rebuild integrity boundary

The public repository currently does **not** publish a separate exact ZIP SHA-256 for the `REBUILT_FOR_KILO` archive and does not publish a byte-by-byte/file-by-file proof that it is byte-identical to the originally predeclared ZIP.

Therefore the project does not claim:

```text
REBUILT PACKAGE = BYTE-FOR-BYTE IDENTICAL TO ORIGINAL PREDECLARED ZIP
REBUILT ZIP SHA256 = PUBLICLY VERIFIED
```

What is supported publicly is narrower: continuity of the declared TRAIN08A Foundation scope, target, 48 unique steps, shared Foundation curriculum identity, preserved executor transition and final evidence state with `material_integrity_violation = false`.

See:

- [`evidence/DIRECTOR_TRAIN08A_REBUILD_INTEGRITY_RECORD_20260909.md`](evidence/DIRECTOR_TRAIN08A_REBUILD_INTEGRITY_RECORD_20260909.md)
- [`DIRECTOR_TRAIN08A_FINAL_EXECUTION_RECORD_20260909.md`](DIRECTOR_TRAIN08A_FINAL_EXECUTION_RECORD_20260909.md)
- [`evidence/DIRECTOR_TRAIN08A_FINAL_CLOSURE_20260909.md`](evidence/DIRECTOR_TRAIN08A_FINAL_CLOSURE_20260909.md)

## Director training lineage

```text
DIRECTOR_FROZEN_C0
= immutable validated engineering baseline

-> TRAIN08A FOUNDATION
-> DIRECTOR_FOUNDATION_S1 [CREATED]

-> TRAIN08B LEGO + MICRONETWORK + V10 PRACTICUM
-> DIRECTOR_TRAINED_START_S2 [NOT YET CLAIMED]
-> record exact S2 identity/hash
```

## Phase A — FOUNDATION

The first package applies the same general Foundation discipline used for BODY_FROZEN and ISKRA:

- task interpretation and decomposition;
- programming/debugging discipline;
- root-cause analysis;
- test-before-closure;
- task/project management;
- evidence/provenance;
- checkpoint/resume;
- resource-aware execution.

Lesson structure remains:

```text
INSTRUCTION
-> GUIDED PRACTICE
-> BLIND VALIDATION
```

Worked or guided examples do not count as independent competence evidence.

## Phase B — FOUNDATION status

TRAIN08A is now closed in its declared training scope. Step-level acceptance is 48/48 PASS, including 16/16 blind validations. Curriculum-contained debugging failures may exist inside PASS steps; the 48/48 claim refers to final declared step acceptance outcomes.

Step 47 retains two PASS records because a test-oracle arithmetic expectation was corrected from `210.0` to `190.0` (`50 + 100 + 40 = 190`). The original event remains preserved.

## TRAIN08B — LEGO + Micronetwork + V10 Practicum

The second package remains future work and applies the same general practicum family:

- LEGO decomposition/composition;
- validated reuse;
- verify/adapt for similar or ambiguous states;
- multi-skill composition;
- false-reuse protection;
- controlled first failure;
- repeated-failure anti-loop behavior;
- alternative/recovery strategy;
- checkpoint/restart persistence;
- route-cost/hardware measurement.

Actual Router V10 route identity must come from runtime/evidence state, not from timing inference.

## Separation from BODY/ISKRA research experiments

Director training is an engineering-line activity. It does not alter the frozen BODY/ISKRA research controls, their training histories or their predeclared mechanism-test packages.

```text
BODY_FROZEN / ISKRA TRAINING
= seven independent research-line histories

DIRECTOR TRAINING
= separate canonical engineering-line history
```

The same curriculum family does not imply shared memory, shared Experience or merged lifecycle state.

## Contamination boundary

The Director training packages follow the same held-out separation rule as the BODY/ISKRA packages:

```text
TRAINING SET != HELD-OUT EXPERIMENT TEST SET
```

Training must not teach exact answers from reserved mechanism-test vectors. If material leakage is later discovered, affected evidence must not be represented as clean held-out validation.

TRAIN08A final evidence records the held-out contamination check as PASS.

## Evidence and failure policy

Training preserves:

```text
PASS
FAIL
INCONCLUSIVE
INTERRUPTION
RECOVERY
CHECKPOINT
EXECUTOR_HANDOFF
CORRECTION
ROUTE CLASS
TIMING / HARDWARE CONTEXT where available
```

A later PASS does not erase an earlier failure, interruption or correction.

## Current claim boundary

As of 2026-09-09:

```text
DIRECTOR_FROZEN_C0 = VALIDATED IN ITS DECLARED ENGINEERING SCOPE
DIRECTOR TRAIN08A = CLOSED / VERIFIED PASS / 48 OF 48 PASS
DIRECTOR TRAIN08A BLIND VALIDATIONS = 16/16 PASS
DIRECTOR_FOUNDATION_S1 = CREATED
DIRECTOR TRAIN08B = PREDECLARED / HASH-SEALED / NOT YET EXECUTED
DIRECTOR_TRAINED_START_S2 = NOT YET CLAIMED
REBUILT TRAIN08A BYTE-LEVEL EQUIVALENCE = NOT PUBLICLY CLAIMED
```

These records do not establish production readiness, AGI, consciousness, universal competence, successful future transfer or independent external scientific validation.