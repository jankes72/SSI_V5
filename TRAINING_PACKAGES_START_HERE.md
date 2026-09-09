# SSI V5 — Pre-Experiment Training Packages

**Recorded:** `2026-09-08`  
**Updated:** `2026-09-09`  
**Package status:** `PREDECLARED / HASH-SEALED / NOT YET EXECUTED`  
**Execution gate:** `OPEN AFTER 7-BODY TECHNICAL READINESS PASS`  
**Immediate next stage:** `TRAIN-A FOUNDATION`

SSI V5 has a predeclared preparation stage between technical readiness and the later mechanism/cross-domain experiments.

The 7-BODY technical-readiness gate is now closed `7/7 PASS` in its declared scope. Therefore Phase A may now be executed, but **no training outcome is claimed yet**.

## Training package set

The research BODY program contains **14 independent training packages**:

```text
7 BODY lines
x
2 training phases per BODY
=
14 packages
```

Training phases:

```text
A — FOUNDATION
programming + debugging + planning + evidence + checkpoint/resume + resource-aware execution

B — LEGO / MICRONETWORK / V10 PRACTICUM
composition + reuse + verification + false-reuse protection + anti-loop + recovery + persistence + route-cost measurement
```

Canonical methodology:

- [`PREEXPERIMENT_TRAINING_PROGRAM_20260908.md`](PREEXPERIMENT_TRAINING_PROGRAM_20260908.md)

Canonical package/hash registry:

- [`PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md`](PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md)

Shared curriculum integrity references:

```text
FOUNDATION = 61a3069ce68d19c64d4ae7c5ebc730d04283d81b2e534f487c3fd5063d9b75b8
PRACTICUM  = abc3eccc4e19849f2d3b3be5b1a4d2752377b6024225f0da8d7d54f4ebafc7ce
```

## Immediate execution scope — Phase A

The next authorized research operation is only:

```text
TRAIN-A FOUNDATION
```

for all seven independent BODY lines:

```text
BODY_FROZEN
BODY_ISKRA1_NICE
BODY_ISKRA2_GUARDIAN
BODY_ISKRA3_JUSTICE
BODY_ISKRA4_EXPLORER
BODY_ISKRA5_PRAGMATIST
BODY_ISKRA6_SKEPTIC
```

The corresponding prepared Phase A packages are:

```text
SSI_TRAIN01A_BODY_FROZEN_FOUNDATION_V1_20260908
SSI_TRAIN02A_BODY_ISKRA1_NICE_FOUNDATION_V1_20260908
SSI_TRAIN03A_BODY_ISKRA2_GUARDIAN_FOUNDATION_V1_20260908
SSI_TRAIN04A_BODY_ISKRA3_JUSTICE_FOUNDATION_V1_20260908
SSI_TRAIN05A_BODY_ISKRA4_EXPLORER_FOUNDATION_V1_20260908
SSI_TRAIN06A_BODY_ISKRA5_PRAGMATIST_FOUNDATION_V1_20260908
SSI_TRAIN07A_BODY_ISKRA6_SKEPTIC_FOUNDATION_V1_20260908
```

All remain `NOT_YET_EXECUTED` until real execution evidence exists.

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

## Phase B remains blocked by Phase A result

Phase B is prepared but must not be treated as the current execution step.

```text
TRAIN-B PRACTICUM
= PREDECLARED / HASH-SEALED
= NOT YET EXECUTED
= follows the required Phase A / FOUNDATION_S1 state
```

Training descendants remain versioned:

```text
T0
-> FOUNDATION_S1
-> TRAINED_START_S2
```

Historical T0 states remain preserved.

## Held-out separation

The exact later experiment vectors are excluded from training. Training teaches general mechanisms and skills, not the held-out answers.

A worked/guided training example is not counted as independent blind-validation evidence.

## Timing / route evidence

Where training execution exercises routing, timing evidence must record the route actually reported by the runtime and compare only genuinely observed comparable cases, including where available:

```text
FULL_FLOW
VERIFY_TOPK / VERIFY-ADAPT
REUSE_TOP1
LEGO / ALTERNATIVE COMPOSITION
RECOVERY
```

Record correctness together with model/provider/call/tool/node/hardware context where available. Timing alone must not be used to infer route identity.

## Relationship to frozen experiment packages

The previously predeclared EXP-01 ... EXP-07 hashes remain historical precommitments and are not silently rewritten by training.

After Phase B, the exact `TRAINED_START_S2` state must be recorded. If binding that state materially changes a frozen experiment input, the experiment must receive a new version/hash while preserving the old precommitment.

## Current claim boundary

As of 2026-09-09:

```text
7-BODY TECHNICAL READINESS = CLOSED 7/7 PASS
TRAIN-A FOUNDATION GATE = OPEN
TRAIN-A FOUNDATION EXECUTION = NOT YET STARTED / NOT YET CLAIMED
FOUNDATION_S1 = NOT YET CLAIMED
TRAIN-B PRACTICUM = NOT YET EXECUTED
TRAINED_START_S2 = NOT YET CLAIMED
7 MECHANISM TESTS = NOT YET EXECUTED
21 CROSS-DOMAIN EXPERIMENTS = NOT YET EXECUTED
```

Readiness closure evidence:

- [`evidence/7BODY_TECHNICAL_READINESS_FINAL_CLOSURE_20260909.md`](evidence/7BODY_TECHNICAL_READINESS_FINAL_CLOSURE_20260909.md)

The correct next move is therefore not to jump to the V10 mechanism experiments: it is to execute the seven predeclared **TRAIN-A FOUNDATION** packages and freeze the resulting seven `FOUNDATION_S1` states.