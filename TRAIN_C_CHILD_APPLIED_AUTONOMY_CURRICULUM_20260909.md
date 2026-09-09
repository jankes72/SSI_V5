# SSI V5 — TRAIN-C CHILD / APPLIED AUTONOMY Curriculum

**Recorded:** `2026-09-09`  
**Status:** `PREDECLARED CURRICULUM / HASH-IDENTIFIED / NOT YET EXECUTED`  
**Input state:** `TRAINED_START_S2`  
**Output state on qualified PASS:** `CHILD_S3`  
**Applies equally to:** `BODY_FROZEN` + six BODY ISKRA lines

## Shared curriculum identity

```text
TRAIN_C_CHILD_APPLIED_AUTONOMY_CURRICULUM_SHA256
= 4f9bb32d9a7f6074357b1f1eb55e539ab0e70e7ccc44bea73b10f2ca916061b5
```

The same curriculum core is used for all seven BODY lines so later differences are not explained merely by different training material.

## Structure

TRAIN-C contains 12 modules. Each module has five phases:

```text
INSTRUCTION
-> GUIDED_PRACTICE
-> BLIND_FIRST
-> IMMEDIATE_EXACT_REPEAT
-> NEAR_TRANSFER
```

Therefore:

```text
12 modules x 5 phases = 60 steps per BODY
7 BODY lines x 60 steps = 420 declared TRAIN-C steps
```

These are training steps, not 420 independent experiments.

## Module map

| Module | Competence target |
|---|---|
| C01 | Reconstruct a usable task contract from incomplete but sufficient facts without inventing requirements |
| C02 | Prioritize hard constraints, correctness gates and softer preferences |
| C03 | Create a self-generated LEGO decomposition with observable gates |
| C04 | Build a dependency-aware deterministic execution order |
| C05 | Decide REUSE vs VERIFY_ADAPT vs NOVEL_DEEPER_FLOW from functional evidence |
| C06 | Identify material similarity differences before adaptation |
| C07 | Compose multiple verified small skills while checking interfaces between them |
| C08 | Diagnose the earliest evidenced root cause and scope repair narrowly |
| C09 | Recover using a materially different strategy instead of looping the same failed attempt |
| C10 | Preserve checkpoint/context state and resume without depending on long conversational memory |
| C11 | Schedule work safely under resource/concurrency limits |
| C12 | Execute an integrated child-level autonomous mini-mission with minimal scaffolding |

## Immediate exact-repeat benchmark

`BLIND_FIRST` is evaluated before the exact repeat.

If `BLIND_FIRST = PASS`, the immediate repeat is eligible as an `EXACT_REPEAT_BENCHMARK`.

The exact repeat:

- uses the same task verbatim;
- runs immediately;
- stays on the same BODY;
- occurs before the next module/BODY;
- is evaluated against the same oracle;
- records timing and route/call information where runtime exposes them.

If `BLIND_FIRST != PASS`, the repeat is a `RECOVERY_RETEST_NOT_SPEED_BENCHMARK`.

No speedup threshold is required. A slower repeat is preserved as evidence rather than hidden.

## Near transfer

The fifth phase changes the concrete input/task while preserving the functional skill family.

This is intended to separate:

```text
memorized exact case
from
reusable functional competence
```

A clean S3 qualification therefore requires both correct exact-case behavior and correct near-transfer behavior under the declared package gate.

## Measurement contract

Where available and reviewer-safe:

```text
STATUS
MONOTONIC WALL-CLOCK ELAPSED
RUNTIME-REPORTED ROUTE
MODEL / PROVIDER
MODEL CALL COUNT
TOOL CALL COUNT
CPU / RAM
GPU / VRAM
COMPETENCE / LIFECYCLE STATE BEFORE
COMPETENCE / LIFECYCLE STATE AFTER
FAILURE SIGNATURE
RECOVERY ACTION
```

Timing never determines route classification.

## Qualification boundary

A clean TRAIN-C -> S3 PASS requires the package-level gate to verify, among other declared checks:

- correct BODY identity;
- real identified/frozen S2 predecessor;
- no overwrite of T0/S1/S2 history;
- all required 60 steps recorded;
- 12/12 BLIND_FIRST PASS;
- 12/12 immediate exact repeats executed and correct;
- 12/12 NEAR_TRANSFER PASS;
- complete checkpoint/evidence chain;
- preserved failures/retries;
- no unresolved blocker invalidating the run;
- versioned/hash-identified S3 descendant.

A material intervention or change to the frozen curriculum may require a separately versioned retest rather than silently converting a failed run into a clean PASS.

## Held-out firewall

TRAIN-C excludes:

- drones;
- humanoid;
- future self-selected Experiment C answer/domain mapping;
- `SEQ_PROFILE_STANDARD_V1`;
- `SEQ_PROFILE_ABS_V1`;
- `STATE_DIFF_V1`;
- later mechanism-test oracles;
- future TRAIN-D / TRAIN-E hidden validation cases.

## What S3 means

`CHILD_S3` means only that the corresponding BODY line passed the declared TRAIN-C qualification scope.

It does **not** mean experiment-ready.

The required future ladder remains:

```text
S3
-> TRAIN-D / INDEPENDENT ADAPTATION
-> S4
-> TRAIN-E / PRE-PROFESSIONAL QUALIFICATION
-> S5
-> held-out mechanism tests
-> cross-domain experiments
```

TRAIN-D/E details and outcomes remain future work and are not claimed here.