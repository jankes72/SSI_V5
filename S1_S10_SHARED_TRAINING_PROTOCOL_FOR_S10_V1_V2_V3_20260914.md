# SSI V5 — Shared S1–S10 Training Protocol for S10 Variants V1, V2 and V3

**Date:** `2026-09-14`  
**Status:** `CURRENT PREDECLARED SHARED TRAINING / THREE-VARIANT COMPARISON CONTROL`  
**Applies to:** `S10 Variant V1 + Variant V2 + Variant V3`  
**Public boundary:** sanitized methodology only / no proprietary implementation source

## Core rule

SSI V5 will use the same ten-stage S1–S10 curriculum for all three active S10 engineering variants.

```text
V1 TRAINING = S1 -> S2 -> S3 -> S4 -> S5 -> S6 -> S7 -> S8 -> S9 -> S10
V3 TRAINING = S1 -> S2 -> S3 -> S4 -> S5 -> S6 -> S7 -> S8 -> S9 -> S10
V2 TRAINING = S1 -> S2 -> S3 -> S4 -> S5 -> S6 -> S7 -> S8 -> S9 -> S10

CURRICULUM = IDENTICAL
TASK FAMILIES = IDENTICAL
ORDER / RANDOMIZATION CONTRACT = MATCHED
ACCEPTANCE CONTRACT = MATCHED
BODY TARGET = MATCHED
START STATE = MATCHED WHERE COMPARISON REQUIRES IT
```

The experimental variable is the execution/control architecture, not unequal training exposure.

## Three comparison lines

```text
V1 = lean control/reference configuration
V3 = intermediate MetaNetwork configuration
V2 = richer optimized control/observability configuration
```

The numbering is historical lineage, not a ranking of quality or performance.

V3 is intentionally kept as its own MetaNetwork-oriented architecture. It may reuse verified common contracts from V2 where appropriate, but it is not to be turned into a copy of V2.

## S1–S10 curriculum

```text
S1  Foundation
S2  LEGO + Micronetwork + Routing Practicum
S3  Applied Autonomy
S4  Robustness / Transfer Preparation
S5  Pre-Experiment Maturity Gate
S6  Multi-Path Equivalence
S7  Counterfactual Rerouting
S8  Cross-Domain Abstraction
S9  Novel Recombination
S10 Generalization Readiness Gate
```

The training objective remains transferable problem-solving mechanisms rather than memorization of future held-out experiment answers.

## Fair comparison rule

For matched comparison among V1, V3 and V2, keep constant where practical:

- stage definitions;
- task-family identities;
- task counts;
- task order or declared seed;
- perturbation rules;
- acceptance criteria;
- blind / held-out split;
- BODY identity;
- predecessor state;
- model/backend policy;
- training budget and retry policy;
- evidence fields;
- interruption/recovery rules;
- hardware class;
- measurement boundaries.

Differences that intentionally violate those controls must be labeled as a separate experiment rather than silently included in the same comparison.

## Interface-native execution rule

Training is intended to pass through the authorized local SSI execution/control path.

```text
LOCAL CENTRAL CONTROL
-> SELECT TARGET BODY
-> SELECT CURRENT STAGE
-> LOAD DECLARED STAGE CONTRACT
-> REAL VERIFIED RUNNER
-> TARGET BODY
-> ROUTER / MICRONETWORK / CONTINUUM PATH
-> RESULT + TELEMETRY + EVIDENCE
-> PASS / FAIL / INCONCLUSIVE
```

The public reviewer interface remains observer-only.

If a real runner is unavailable, the system must report that fact and remain fail-closed rather than simulate completion.

## Stage progression

Package availability does not equal training completion.

```text
PACKAGE PRESENT != STAGE PASSED
PREDECLARED != EXECUTED
EXECUTED != PASSED
```

A later stage must not erase an earlier FAIL or INCONCLUSIVE result.

## Evidence to compare after matched training

At minimum compare:

- stage outcome;
- task success rate;
- alternative valid routes;
- rerouting after route invalidation;
- false-transfer rate;
- justified cross-domain transfer;
- Champion / Challenger agreement;
- wrong promotions;
- recombination success;
- repeated-work amount;
- router/evaluation overhead;
- execution time under declared conditions;
- interruption/recovery behavior;
- regression against earlier competence;
- integrity-gate behavior.

Speed alone is not sufficient to determine which variant is better for a given task class.

## Historical continuity

The earlier file:

[`S1_S10_SHARED_TRAINING_PROTOCOL_FOR_S10_V1_V2_20260913.md`](S1_S10_SHARED_TRAINING_PROTOCOL_FOR_S10_V1_V2_20260913.md)

remains preserved as historical evidence of the two-variant methodology that existed before V3 became an explicit comparison line.

This document is the current three-variant extension and does not retroactively rewrite that history.

## Claim boundary

This is a predeclared comparison-control methodology. It does not claim that all three variants have completed S1–S10, that any variant is universally superior, or that held-out experiments have succeeded.

The current narrow claim is:

> SSI V5 now defines one shared S1–S10 curriculum across three explicit S10 engineering variants — V1, V3 and V2 — so later differences can be evaluated as architectural/control differences rather than unequal training exposure.
