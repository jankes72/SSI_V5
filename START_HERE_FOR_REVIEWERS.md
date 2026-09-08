# SSI V5 — Start Here for Grant and Technical Reviewers

**Updated:** 2026-09-08  
**Frozen baseline:** `BODY_FROZEN T0 / PRE-ISKRA / 2026-09-05`  
**Current ISKRA start state:** `6 independent T0 variants / START_STATE_VALIDATED`  
**Technical readiness:** `FINAL 7/7 BODY + REVIEWER INTERFACE VALIDATION REQUIRED`  
**Pre-experiment training:** `14 HASH-SEALED PACKAGES / PREDECLARED / NOT YET EXECUTED`  
**Mechanism tests:** `7 INDEPENDENT MICRONETWORK + V10 PACKAGES / PREDECLARED`  
**Cross-domain program:** `7 x 3 = 21 EXPERIMENTS / PREDECLARED / OUTCOMES UNKNOWN`  
**Latest closed validation:** `TEST 5 / DEVELOPMENT_VALIDATED`

## What to understand first

SSI V5 now has a deliberately staged research sequence:

```text
IMMUTABLE T0 CONTROLS
-> FINAL TECHNICAL READINESS
-> TRAIN-A FOUNDATION (7 independent BODY runs)
-> FOUNDATION_S1
-> TRAIN-B LEGO + MICRONETWORK + V10 PRACTICUM (7 independent BODY runs)
-> TRAINED_START_S2
-> S2 HASH / STATE RECORD
-> 7 MICRONETWORK + V10 MECHANISM TESTS
-> 21 CROSS-DOMAIN EXPERIMENTS
-> POST-21 COMPETENCE CONSOLIDATION
-> 3 NEW DOMAINS
-> LATER EXTERNAL FALSIFICATION CHALLENGES
```

Training does not rewrite historical T0. It creates versioned descendants.

## Pre-experiment training

Primary methodology:

- [`PREEXPERIMENT_TRAINING_PROGRAM_20260908.md`](PREEXPERIMENT_TRAINING_PROGRAM_20260908.md)
- [`PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md`](PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md)
- [`TRAINING_PACKAGES_START_HERE.md`](TRAINING_PACKAGES_START_HERE.md)

There are 14 packages:

```text
7 BODY LINES x 2 TRAINING PHASES
```

Phase A — Foundation:

```text
programming
+ debugging
+ task decomposition
+ task/project management
+ testing
+ checkpoints
+ provenance
+ failure preservation
+ resource-aware execution
```

Phase B — Practicum:

```text
LEGO composition
+ Micronetwork lifecycle use
+ V10 route choice
+ reuse / verify / full-flow
+ false-reuse traps
+ controlled failure
+ anti-loop
+ recovery
+ persistence/restart
+ route-cost measurement
```

All seven Foundation packages share one identical curriculum hash. All seven Practicum packages share a second identical curriculum hash. BODY-specific state/evidence remains isolated.

```text
FOUNDATION_CURRICULUM_SHA256
= 61a3069ce68d19c64d4ae7c5ebc730d04283d81b2e534f487c3fd5063d9b75b8

PRACTICUM_CURRICULUM_SHA256
= abc3eccc4e19849f2d3b3be5b1a4d2752377b6024225f0da8d7d54f4ebafc7ce
```

No training result is preclaimed.

## Why the training design matters

Training is separated from held-out experiment cases. The exact reserved mechanism-test vector families are excluded from the curriculum.

```text
TRAIN THE GENERAL MECHANISM
!=
TRAIN THE HELD-OUT ANSWER
```

Instruction, guided practice and blind validation are also separated. A worked example does not count as independently validated competence.

## Performance and routing evidence

Training records real route-cost evidence where technically available:

```text
FULL_FLOW
VERIFY_TOPK / VERIFY-ADAPT
REUSE_TOP1
LEGO / ALTERNATIVE COMPOSITION
RECOVERY AFTER FAILURE
```

with context such as:

```text
elapsed time
actual route class
correctness / outcome
model / provider
model/tool call count
execution node
CPU / RAM / GPU / VRAM
```

Timing never determines the route label. The route comes from the SSI runtime/evidence contract; timing measures its cost.

Historical Test 3 remains a scoped reference point:

```text
57.61 s vs 126.65 s Test 2
REUSE_TOP1 = 534
VERIFY_TOPK = 66
fallback = 0
known-case correctness = 100/100
```

This is not a universal superiority claim.

## Relationship to the seven predeclared mechanism-test packages

The seven mechanism-test packages were already hash-sealed before the training phase was added. Their original hashes remain unchanged.

Before any post-training run:

```text
TRAINED_START_S2
-> RECORD EXACT S2 STATE / HASH
-> CHECK COMPATIBILITY WITH EXISTING FROZEN PACKAGE
```

If S2 is compatible with the frozen package contract, the execution record binds that exact S2. If S2 materially changes a frozen input, a new package version/hash is required. The original precommitment remains preserved.

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
```

Primary references:

- [`EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md`](EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md)
- [`EXPERIMENT_EXECUTION_METHODOLOGY_20260906.md`](EXPERIMENT_EXECUTION_METHODOLOGY_20260906.md)
- [`CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md`](CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md)

## Live reviewer boundary

The reviewer interface is read-only.

A reviewer may observe sanitized BODY identity, stage, checkpoints, CONTINUUM/LAB, reviewer-safe Micronetwork/V10 state, evidence references and hardware utilization.

A reviewer cannot:

```text
issue ROOT commands
create/alter missions
start/stop Kilo
change prompts or acceptance criteria
edit configuration/source
inject expected answers
access private source, memory, prompts, secrets or filesystem contents
```

Reference: [`REVIEWER_LIVE_INTERFACE_20260907.md`](REVIEWER_LIVE_INTERFACE_20260907.md).

## Current established evidence

```text
BODY_FROZEN T0 = preserved immutable origin
6 ISKRA T0 variants = recorded
START_STATE_QA = 8/8 per agent
GROUP_QA = 48/48 PASS
TEST 5 = 29/29 acceptance
TOTAL TEST 5 REGRESSION = 524/524 PASS
OPEN_BLOCKERS IN TEST 5 SCOPE = 0
```

## Current unknowns

Not yet claimed:

```text
TRAIN-A outcomes
TRAIN-B outcomes
FOUNDATION_S1 contents
TRAINED_START_S2 contents
7 mechanism-test outcomes
21 cross-domain outcomes
post-21 consolidation outcome
three-new-domain result
long-run ISKRA divergence
universal V10 advantage
physical drone/humanoid validation
external replication
AGI / consciousness / production readiness
```

## Recommended reading order

1. [`README.md`](README.md)
2. [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md)
3. [`PREEXPERIMENT_TRAINING_PROGRAM_20260908.md`](PREEXPERIMENT_TRAINING_PROGRAM_20260908.md)
4. [`PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md`](PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md)
5. [`CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md`](CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md)
6. [`PREDECLARED_7BODY_MICRONETWORK_V10_PACKAGES_20260908.md`](PREDECLARED_7BODY_MICRONETWORK_V10_PACKAGES_20260908.md)
7. [`EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md`](EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md)
8. [`REVIEWER_LIVE_INTERFACE_20260907.md`](REVIEWER_LIVE_INTERFACE_20260907.md)
9. [`V10_PREDICTIVE_ROUTING.md`](V10_PREDICTIVE_ROUTING.md)
10. [`evidence/README.md`](evidence/README.md)

The repository should be read as an evidence mirror with explicit separation between historical controls, prepared training, held-out experiments, observed outcomes and still-prospective claims.