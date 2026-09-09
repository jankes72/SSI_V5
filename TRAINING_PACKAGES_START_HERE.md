# SSI V5 — Pre-Experiment Training Packages

**Recorded:** `2026-09-08`  
**Updated:** `2026-09-09`  
**Program status:** `A/B PREDECLARED + TRAIN-C S3 EXTENSION PREPARED / OUTCOMES NOT YET CLAIMED`  
**Execution gate:** `OPEN AFTER 7-BODY TECHNICAL READINESS PASS`  
**Immediate next stage:** `TRAIN-A FOUNDATION`  
**Future experiment-entry maturity gate:** `S5`

SSI V5 has a controlled preparation ladder between technical readiness and the later held-out mechanism/cross-domain experiments.

The 7-BODY technical-readiness gate is closed `7/7 PASS` in its declared scope. Phase A may therefore execute, but no seven-line BODY/ISKRA training outcome is claimed yet.

## Training program evolution

The original pre-experiment program recorded two packages per BODY:

```text
A — FOUNDATION
B — LEGO / MICRONETWORK / V10 PRACTICUM
```

Those historical precommitments remain preserved.

On `2026-09-09`, before the final 21-experiment outcomes were known, the project prospectively extended the maturity ladder:

```text
T0 / VALIDATED START STATE
-> TRAIN-A FOUNDATION
-> FOUNDATION_S1
-> TRAIN-B LEGO + MICRONETWORK + V10 PRACTICUM
-> TRAINED_START_S2
-> TRAIN-C CHILD / APPLIED AUTONOMY
-> CHILD_S3
-> TRAIN-D TEEN / INDEPENDENT ADAPTATION
-> TEEN_S4
-> TRAIN-E PRE-PROFESSIONAL QUALIFICATION
-> QUALIFIED_S5
-> HELD-OUT MICRONETWORK + V10 MECHANISM TESTS
-> 21 CROSS-DOMAIN EXPERIMENTS
```

The important new boundary is:

```text
S2 != EXPERIMENT_READY
S3 != EXPERIMENT_READY
S4 != EXPERIMENT_READY
S5 = REQUIRED FUTURE EXPERIMENT-ENTRY STATE
```

Canonical extension:

- [`PREEXPERIMENT_TRAINING_S3_S5_EXTENSION_20260909.md`](PREEXPERIMENT_TRAINING_S3_S5_EXTENSION_20260909.md)

## Prepared package set now

Prepared training packages now cover three stages for seven BODY lines:

```text
7 BODY lines x TRAIN-A = 7 packages
7 BODY lines x TRAIN-B = 7 packages
7 BODY lines x TRAIN-C = 7 packages
-------------------------------------
21 prepared training packages through S3
```

TRAIN-D and TRAIN-E are required future stages but their detailed curricula/packages/hashes are not yet frozen and are not claimed as executed.

## Shared curriculum identities

```text
FOUNDATION_CURRICULUM_SHA256
= 61a3069ce68d19c64d4ae7c5ebc730d04283d81b2e534f487c3fd5063d9b75b8

PRACTICUM_CURRICULUM_SHA256
= abc3eccc4e19849f2d3b3be5b1a4d2752377b6024225f0da8d7d54f4ebafc7ce

TRAIN_C_CHILD_APPLIED_AUTONOMY_CURRICULUM_SHA256
= 4f9bb32d9a7f6074357b1f1eb55e539ab0e70e7ccc44bea73b10f2ca916061b5
```

A/B registry:

- [`PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md`](PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md)

TRAIN-C registry and curriculum:

- [`PREDECLARED_7BODY_TRAIN_C_S3_PACKAGES_20260909.md`](PREDECLARED_7BODY_TRAIN_C_S3_PACKAGES_20260909.md)
- [`TRAIN_C_CHILD_APPLIED_AUTONOMY_CURRICULUM_20260909.md`](TRAIN_C_CHILD_APPLIED_AUTONOMY_CURRICULUM_20260909.md)

## Immediate execution scope remains TRAIN-A

The next authorized BODY/ISKRA operation is still:

```text
TRAIN-A FOUNDATION
```

for:

```text
BODY_FROZEN
BODY_ISKRA1_NICE
BODY_ISKRA2_GUARDIAN
BODY_ISKRA3_JUSTICE
BODY_ISKRA4_EXPLORER
BODY_ISKRA5_PRAGMATIST
BODY_ISKRA6_SKEPTIC
```

The corresponding Phase A packages remain the first execution gate:

```text
SSI_TRAIN01A_BODY_FROZEN_FOUNDATION_V1_20260908
SSI_TRAIN02A_BODY_ISKRA1_NICE_FOUNDATION_V1_20260908
SSI_TRAIN03A_BODY_ISKRA2_GUARDIAN_FOUNDATION_V1_20260908
SSI_TRAIN04A_BODY_ISKRA3_JUSTICE_FOUNDATION_V1_20260908
SSI_TRAIN05A_BODY_ISKRA4_EXPLORER_FOUNDATION_V1_20260908
SSI_TRAIN06A_BODY_ISKRA5_PRAGMATIST_FOUNDATION_V1_20260908
SSI_TRAIN07A_BODY_ISKRA6_SKEPTIC_FOUNDATION_V1_20260908
```

All remain outcome-unknown until real execution evidence exists.

## Phase A output rule

Each Phase A run must preserve the exact starting state and produce an independently versioned result:

```text
T0 / validated start state
-> TRAIN-A FOUNDATION
-> FOUNDATION_S1
```

Before execution:

```text
verify target BODY identity
verify package/hash
verify start-state identity/checkpoint
verify training package has not been silently modified
```

After execution:

```text
record PASS / FAIL / INCONCLUSIVE
preserve interruptions and recovery
record checkpoint/evidence
freeze exact FOUNDATION_S1 identity/hash if created
```

A failed or inconclusive Phase A run must not be converted into `FOUNDATION_S1 PASS` by inference or by rerunning until success without preserving the earlier outcome.

## Phase B

Phase B remains dependent on the corresponding S1 state:

```text
FOUNDATION_S1
-> TRAIN-B PRACTICUM
-> TRAINED_START_S2
```

It includes LEGO decomposition, Micronetwork/V10 reuse/verification/composition, deceptive-similarity protection, anti-loop/recovery, persistence and route-cost measurement.

Historical A/B methodology remains:

- [`PREEXPERIMENT_TRAINING_PROGRAM_20260908.md`](PREEXPERIMENT_TRAINING_PROGRAM_20260908.md)

## Phase C — CHILD / APPLIED AUTONOMY

TRAIN-C consumes an identified/frozen S2 predecessor and may create a separately versioned S3 descendant:

```text
TRAINED_START_S2
-> TRAIN-C CHILD / APPLIED AUTONOMY
-> CHILD_S3
```

TRAIN-C contains:

```text
12 modules x 5 phases = 60 steps per BODY
```

Each module uses:

```text
INSTRUCTION
-> GUIDED_PRACTICE
-> BLIND_FIRST
-> IMMEDIATE_EXACT_REPEAT
-> NEAR_TRANSFER
```

Competence targets include:

- reconstructing a task contract from incomplete but sufficient information;
- prioritizing hard constraints and correctness gates;
- self-generated LEGO decomposition;
- dependency-aware planning;
- evidence-based REUSE vs VERIFY_ADAPT vs NOVEL_DEEPER_FLOW selection;
- similarity verification before adaptation;
- multi-skill composition;
- root-cause debugging;
- alternative recovery after failed strategy;
- checkpoint/context compression and resume;
- resource-aware scheduling;
- integrated autonomous mini-mission execution.

### Immediate exact-repeat rule

After every `BLIND_FIRST`, the same BODY immediately receives the exact same task before another module or BODY is started.

If `BLIND_FIRST = PASS`, the repeat is an `EXACT_REPEAT_BENCHMARK` and may measure exact-case reuse/retention and route/cost change.

If `BLIND_FIRST = FAIL` or `INCONCLUSIVE`, the repeat is a `RECOVERY_RETEST_NOT_SPEED_BENCHMARK`.

No minimum speedup is a PASS criterion. A slower repeat is preserved as evidence.

### Near transfer

The fifth phase is a different task from the same functional skill family. This is intended to distinguish memorizing the exact answer from transferring the competence.

A clean S3 PASS therefore depends on both declared blind-first and near-transfer gates, not only on a fast exact repeat.

## Training-set / experiment-set separation

Training must not rehearse the held-out experiment answers.

The firewall includes:

```text
drones
humanoid
future self-selected Experiment C answers
SEQ_PROFILE_STANDARD_V1
SEQ_PROFILE_ABS_V1
STATE_DIFF_V1
later held-out mechanism-test oracles
future TRAIN-D / TRAIN-E hidden validation cases
```

The principle remains:

```text
TRAIN THE MECHANISM / GENERAL SKILL
!=
TRAIN THE HELD-OUT EXPERIMENT ANSWER
```

## Timing / route evidence

Where runtime exposes it, training records the route actually reported by runtime and its measured cost, including where available:

```text
FULL_FLOW
VERIFY_TOPK / VERIFY-ADAPT
REUSE_TOP1
LEGO / ALTERNATIVE COMPOSITION
RECOVERY
```

Timing must never be used to infer which route occurred.

For exact-repeat pairs, reviewer-safe evidence may record:

```text
FIRST_STATUS
REPEAT_STATUS
FIRST_ELAPSED
REPEAT_ELAPSED
FIRST_RUNTIME_ROUTE
REPEAT_RUNTIME_ROUTE
FIRST_MODEL_CALLS
REPEAT_MODEL_CALLS
FIRST_TOOL_CALLS
REPEAT_TOOL_CALLS
FIRST_COMPETENCE_STATE
REPEAT_COMPETENCE_STATE
EXACT_REPEAT_SPEEDUP
```

Speedup is calculated only when the first execution is PASS and both timings are valid.

## Relationship to frozen mechanism-test and cross-domain packages

The earlier mechanism-test and 21-experiment precommitments remain historical records and are not silently rewritten.

However, the prospective maturity gate has changed before those outcomes are known:

```text
S5 must be the identified experiment-entry state.
```

If binding S5 materially changes an older frozen experiment input contract, a new experiment-package version/hash must be created while preserving the earlier precommitment.

The later 21 unique cross-domain experiments retain their identity:

```text
7 lines x 3 unique domains = 21 unique experiments
```

The execution methodology is extended so that after a successful first exposure, the same BODY immediately repeats the exact experiment for route/time/reuse measurement. Thus the program may yield up to 42 execution runs while remaining 21 unique experiments.

Canonical extension details:

- [`PREEXPERIMENT_TRAINING_S3_S5_EXTENSION_20260909.md`](PREEXPERIMENT_TRAINING_S3_S5_EXTENSION_20260909.md)

## Current claim boundary

As of `2026-09-09`:

```text
7-BODY TECHNICAL READINESS = CLOSED 7/7 PASS
TRAIN-A FOUNDATION = NEXT / OUTCOMES NOT YET CLAIMED FOR 7 BODY LINES
FOUNDATION_S1 x7 = NOT YET CLAIMED
TRAIN-B PRACTICUM = PREPARED / NOT YET EXECUTED FOR 7 BODY LINES
TRAINED_START_S2 x7 = NOT YET CLAIMED
TRAIN-C S3 PACKAGES = 7 PREPARED / HASH-IDENTIFIED / NOT YET EXECUTED
CHILD_S3 x7 = NOT YET CLAIMED
TRAIN-D -> S4 = REQUIRED FUTURE STAGE / CURRICULUM NOT YET FROZEN
TRAIN-E -> S5 = REQUIRED FUTURE STAGE / CURRICULUM NOT YET FROZEN
S5 = REQUIRED FUTURE EXPERIMENT-ENTRY STATE
7 MECHANISM TESTS = NOT YET EXECUTED
21 UNIQUE CROSS-DOMAIN EXPERIMENTS = NOT YET EXECUTED
EXACT-REPEAT SPEEDUP RESULTS = UNKNOWN
```

The standard remains: preserve earlier precommitments, record extensions before outcomes, keep training separate from held-out experiments, preserve failures, and claim only what the evidence actually establishes.