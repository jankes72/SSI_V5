# SSI V5 — Shared S1–S10 Training Protocol for S10 Variant V1 and V2

**Date:** `2026-09-13`  
**Status:** `PREDECLARED SHARED TRAINING / V1-V2 COMPARISON CONTROL`  
**Applies to:** `S10 Variant V1 + S10 Variant V2`  
**Public boundary:** sanitized methodology only / no proprietary implementation source

## 1. Core rule

SSI V5 will use the **same ten-stage training curriculum, S1 through S10, for both S10 Variant V1 and S10 Variant V2**.

The purpose is methodological control. V1 and V2 are intended to differ in their S10 execution/control infrastructure, not in what they are taught.

```text
V1 TRAINING = S1 -> S2 -> S3 -> S4 -> S5 -> S6 -> S7 -> S8 -> S9 -> S10
V2 TRAINING = S1 -> S2 -> S3 -> S4 -> S5 -> S6 -> S7 -> S8 -> S9 -> S10

CURRICULUM = IDENTICAL
TASK FAMILIES = IDENTICAL
ORDER = IDENTICAL
ACCEPTANCE CONTRACT = IDENTICAL
BODY TARGET = MATCHED
START STATE = MATCHED WHERE COMPARISON REQUIRES IT
```

A difference in outcome should therefore not be explained by one variant receiving easier, richer or differently ordered training.

## 2. Why ten stages are used

The ten stages are designed to move from foundation and controlled tool use toward autonomy, robustness, multiple-solution reasoning and generalization.

### S1 — Foundation

Establish basic controlled competence, state continuity, evidence capture and correct execution through the authorized SSI interface/runtime.

### S2 — LEGO + Micronetwork + Router Practicum

Train controlled use of reusable competence components, Micronetworks, LEGO composition and routing decisions instead of treating every task as a fresh isolated prompt.

### S3 — Applied Autonomy

Move from explicit step-by-step instruction toward goal-level tasks where SSI must plan and execute within a frozen contract while preserving checkpoints and evidence.

### S4 — Robustness and Transfer Preparation

Expose the system to perturbations, near-miss cases, incomplete information and similar-looking tasks that may require different treatment.

### S5 — Pre-Experiment Maturity Gate

Verify that the foundational training path remains stable enough to proceed into stronger generalization training without silently weakening earlier acceptance requirements.

### S6 — Multi-Path Equivalence

Train the ability to identify multiple valid solution routes to the same objective and compare them by cost, evidence, risk, constraints and expected effectiveness.

### S7 — Counterfactual Rerouting

Block or invalidate a previously useful route and require SSI to detect the failure condition, avoid repetition loops and select or construct an alternative route.

### S8 — Cross-Domain Abstraction

Train recognition of shared underlying mechanisms across superficially different domains while penalizing false transfer based only on surface similarity.

### S9 — Novel Recombination

Require SSI to combine previously validated competence when no single existing skill is sufficient, while preserving provenance and distinguishing a new Challenger from an established Champion.

### S10 — Generalization Readiness Gate

Use a mixed evaluation to determine whether SSI can choose between reuse, adaptation, rerouting, recombination and rejection of false similarity before held-out experiments.

## 3. Training objective

The curriculum is not intended to teach answers to one particular experiment.

The intended learning target is a set of transferable problem-solving mechanisms:

```text
ONE GOAL
-> MULTIPLE POSSIBLE ROUTES

ROUTE FAILS
-> DETECT
-> REROUTE

SIMILAR TASK
-> TEST FUNCTIONAL SIMILARITY
-> TRANSFER ONLY WHEN JUSTIFIED

NO SINGLE SUFFICIENT SKILL
-> RECOMBINE VERIFIED COMPETENCE

NOVEL CASE
-> REASON FROM MECHANISM AND EVIDENCE
-> DO NOT REPLAY A MEMORIZED EXPERIMENT ANSWER
```

This design is intended to prepare the system for different held-out experiment paths rather than overfit it to a single expected experiment.

## 4. Interface-native execution rule

Training is intended to be executed through the authorized local SSI control/interface path.

Conceptually:

```text
LOCAL CENTRAL CONTROL
-> SELECT TARGET BODY
-> ENTER S1 ... S10
-> LOAD DECLARED STAGE CONTRACT
-> SSI INTERFACE / REAL RUNNER
-> TARGET BODY
-> ROUTER / MICRONETWORK / CONTINUUM PATH
-> RESULT + TELEMETRY + EVIDENCE
-> PASS / FAIL / INCONCLUSIVE
```

The public reviewer interface remains observer-only and is not an execution channel.

If a real backend/runner is unavailable, the stage must report the missing execution capability rather than simulate success.

## 5. Same-training requirement for V1 and V2

For a valid V1/V2 training comparison, the following must remain matched:

- S1–S10 stage definitions;
- task-family identities;
- task counts where comparison is intended;
- task order or declared randomization seed;
- perturbation rules;
- acceptance criteria;
- blind/held-out split;
- BODY identity and predecessor-state identity;
- model/backend policy where practical;
- training budget and retry policy;
- evidence fields;
- interruption/recovery rules.

The intended experimental variable is the **S10 variant**, not the curriculum.

```text
INDEPENDENT VARIABLE = V1 vs V2 execution/control configuration
CONTROLLED VARIABLE = S1-S10 training curriculum
```

## 6. No training advantage for either variant

Neither V1 nor V2 may receive privileged training information unavailable to the other during a controlled comparison.

Forbidden comparison shortcuts include:

```text
V2 receives extra examples but V1 does not
V1 receives easier variants
one variant sees held-out answers during training
acceptance is weakened after observing one result
one variant receives additional retries solely to rescue a failure
one variant is trained on the other variant's held-out result
```

If any such difference is intentionally introduced, it becomes a different experiment and must receive a separate identity.

## 7. Stage progression

The conceptual progression is:

```text
S1  FOUNDATION
S2  TOOL / MICRONETWORK / ROUTING PRACTICUM
S3  APPLIED AUTONOMY
S4  ROBUSTNESS / TRANSFER PREPARATION
S5  MATURITY GATE
S6  MULTI-PATH EQUIVALENCE
S7  COUNTERFACTUAL REROUTING
S8  CROSS-DOMAIN ABSTRACTION
S9  NOVEL RECOMBINATION
S10 GENERALIZATION READINESS GATE
```

A descendant stage should not be treated as passed merely because a later stage was attempted. Historical FAIL and INCONCLUSIVE outcomes remain evidence.

## 8. Evidence to compare after training

After both variants receive the same S1–S10 curriculum, the comparison should measure at minimum:

- stage pass/fail/inconclusive outcome;
- task success rate;
- number of alternative valid routes discovered;
- rerouting success after route invalidation;
- false-transfer rate;
- correct cross-domain transfer rate;
- Champion/Challenger proposal agreement;
- wrong promotion count/rate;
- recombination success;
- repeated-work amount;
- router/evaluation overhead;
- total execution time under declared conditions;
- recovery behavior after interruption;
- regression against earlier-stage competence;
- integrity-gate state.

Speed alone is not sufficient to determine which variant is better.

## 9. Relationship to V1 and V2

### Variant V1

V1 is the lean control/reference line. Its role is to provide a more direct recomputation-oriented comparison path with preserved S10 calibration and integrity gates.

### Variant V2

V2 is the richer control/observability line. It adds optimized modes such as incremental partial recomputation and whole-state reuse where verified reuse is safe.

Both variants are intended to receive **the same S1–S10 training program** before conclusions are drawn about which execution configuration performs better after training.

## 10. Held-out experiment firewall

The S1–S10 curriculum should train mechanisms, not leak the expected solutions to later held-out experiments.

This distinction is central:

```text
TRAIN GENERAL PROBLEM-SOLVING MECHANISMS
!=
TRAIN THE ANSWER TO THE FUTURE EXPERIMENT
```

Held-out experiments should therefore remain unavailable as direct answer templates during training.

## 11. Claim boundary

This document is a **predeclared methodology and comparison-control rule**.

It does not claim that:

- both variants have already completed S1–S10;
- every stage has already been executed on every BODY;
- V1 and V2 will produce identical results;
- V2 will necessarily outperform V1;
- V1 will necessarily generalize better because it recomputes more work;
- all future held-out experiments will pass;
- general intelligence or universal transfer has been demonstrated.

The intended narrow claim is:

> SSI V5 predeclares one shared ten-stage S1–S10 curriculum for both S10 Variant V1 and Variant V2. The curriculum, task families and acceptance contract are to remain matched so that later differences can be attributed to the compared execution/control variants rather than to unequal training exposure.
