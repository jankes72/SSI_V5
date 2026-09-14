# SSI V5 — Humanoid-domain transfer and R&D status

**Date:** 2026-09-14  
**Status:** `IMPLEMENTED SOFTWARE-LEVEL DOMAIN TRANSFER / RESEARCH DEMONSTRATOR`  
**Disclosure model:** public capability and evidence description only; proprietary SSI implementation remains private.

## Executive statement

SSI V5 now includes an implemented software-level humanoid motion, stability and domain-transfer laboratory. The humanoid branch is therefore no longer only a future research concept.

The correct claim is:

> **SSI has been instantiated in a humanoid software research environment with a dedicated 3D interface, scenario library, motion/stability state, failure/recovery experiments and evidence-oriented before/after evaluation.**

This is a software research demonstrator. It is not a claim of certified physical humanoid control, production robotics readiness or complete hardware validation.

## What exists now

The humanoid laboratory provides a dedicated domain interface rather than reusing the original BODY view. The implemented research surface includes:

- a ready humanoid representation in a 3D laboratory environment;
- articulated body sections representing legs, arms, pelvis and spine-related coordination;
- tracked joint-state concepts;
- center-of-mass / balance-related state;
- ground / contact / support conditions;
- configurable environment and disturbance scenarios;
- scene switching without rebuilding the whole application;
- replay / repeated-attempt workflow;
- before/after learning comparison;
- evidence capture and run-state summaries;
- an external-scene entry path for future independently supplied challenge cases.

The interface is designed so that a reviewer can observe a complete case rather than only raw telemetry.

## Representative humanoid-domain scenarios

The implemented scenario family includes software-level tests around:

- basic locomotion and root movement;
- stopping before an obstacle;
- obstacle avoidance / bypass;
- uneven terrain / step interaction;
- low-friction / slip conditions;
- recovery after instability;
- whole-body coordination across ankle, knee, hip and spine-related state;
- dynamic environmental interference;
- load / balance change;
- combined or held-out scene configurations.

A central focus is the difference between **reaction after failure** and **prediction before failure**.

For example, a slip-oriented case can be represented as:

```text
NORMAL CONTACT
-> FRICTION DEGRADES
-> INSTABILITY SIGNAL RISES
-> PREDICTION / ROUTING DECISION
-> ANKLE / KNEE / HIP / SPINE RESPONSE
-> STABLE / RECOVERING / FALL OUTCOME
-> EXPERIENCE RETAINED
-> REPEAT / BEFORE-AFTER COMPARISON
```

This lets a reviewer see whether a second attempt changes after retained experience rather than only watching an isolated animation.

## Learning-loop representation

The humanoid demonstrator includes an explicit learning-loop concept rather than only a scripted obstacle course.

A representative visible sequence is:

```text
ATTEMPT 1
-> FAILURE / HARD STOP / FALL
-> NEGATIVE EXPERIENCE RETAINED
-> BACKOFF / RESET
-> ALTERNATIVE ROUTE OR CONTROL STRATEGY
-> ATTEMPT 2
-> VALIDATION
-> BEFORE / AFTER RESULT
```

The public description focuses on the observable effect: what changed between attempts, whether a failure signature was retained and whether a later strategy produced a different result.

It does not disclose proprietary Router or Micronetwork implementation.

## Domain-transfer training concept

The humanoid branch is also structured as a progressive domain-learning path rather than one preprogrammed final skill.

Representative stages include:

```text
S0  BODY / JOINT DISCOVERY
S1  BASIC LOCOMOTION
S2  STOP BEFORE OBSTACLE
S3  LEARNED BYPASS
S4  TERRAIN / STEP
S5  SLIP PREDICTION
S6  DYNAMIC HUMAN-SPACE CASE
S7  LOAD CHANGE
S8  COMBINED CHALLENGE
S9  HELD-OUT / NEW COMBINATION
```

The research question is not simply whether a humanoid can be animated. The question is whether the SSI-style process can acquire, retain, compare and reuse experience in a new domain while preserving evidence and before/after comparisons.

## Interface role

The humanoid branch includes a dedicated visual interface intended to make domain behavior understandable to both technical and non-technical reviewers.

The interface can expose high-level information such as:

- current scene;
- attempt number;
- current stability / recovery state;
- selected execution mode;
- prediction status;
- relevant joint-chain summary;
- before/after result;
- run timing;
- evidence identifier.

A reviewer-facing mode is intended to explain the process without exposing private source code, private skill definitions, private Micronetwork topology, routing thresholds or ROOT authority.

## Why slips and instability matter in this branch

The slip / stability cases are included because they force the system to reason about a coupled body rather than one isolated actuator.

A visible failure can involve a chain such as:

```text
FOOT CONTACT
-> ANKLE RESPONSE
-> KNEE ADJUSTMENT
-> HIP COMPENSATION
-> SPINE / CORE COUNTERBALANCE
-> CENTER-OF-MASS CHANGE
-> RECOVERY OR FALL
```

This makes the humanoid branch materially different from the drone branch while preserving the same higher-level SSI research questions: state, experience, routing, adaptation, retention, validation and transfer.

## External challenge path

The humanoid laboratory is intentionally designed so that a later external expert or laboratory can provide a new scene or challenge without requiring a rewrite of the whole interface.

The intended future protocol is:

```text
EXTERNAL PROBLEM
-> FROZEN SCENE / CHALLENGE CONTRACT
-> DECLARED ACCEPTANCE CRITERIA
-> RUN
-> PREDICTION / RESPONSE / OUTCOME
-> REPEAT IF ALLOWED
-> EVIDENCE
-> EXTERNAL REVIEW
```

This is the preferred next credibility step after internal software-level demonstration.

## Public disclosure boundary

The public repository may describe:

- scenario classes;
- interface existence;
- software-level behavior;
- before/after outcomes;
- high-level flow states;
- timing and evidence records;
- claim boundaries.

It does not disclose:

- proprietary SSI source code;
- private Router V10 / S10 implementation;
- private Micronetwork topology;
- private prompts / thresholds;
- ROOT control;
- private runtime internals.

## What this changes in project status

Previously the humanoid domain appeared primarily as a planned cross-domain experiment.

Current status:

```text
HUMANOID DOMAIN
PLANNED DOMAIN
-> IMPLEMENTED SOFTWARE RESEARCH LAB
-> DEDICATED 3D INTERFACE EXISTS
-> SCENE LIBRARY EXISTS
-> SLIP / INSTABILITY CASES EXIST
-> OBSTACLE / TERRAIN CASES EXIST
-> BEFORE / AFTER LEARNING LOOP EXISTS
-> DOMAIN-TRANSFER TRAINING PATH EXISTS
-> EXTERNAL SCENE ENTRY PATH EXISTS
```

## Claim boundary

### Supported now

- a runnable software-level humanoid research demonstrator exists;
- a dedicated humanoid-oriented interface exists;
- multiple domain scenes exist;
- slip / low-friction / instability cases are represented;
- obstacle and terrain cases are represented;
- articulated joint-chain and whole-body coordination concepts are represented;
- before/after learning and retained-failure concepts are represented;
- externally supplied software-level scenes can be added without rebuilding the entire project.

### Not claimed yet

- certified physical humanoid operation;
- production robotics readiness;
- complete biomechanical fidelity;
- independent external replication;
- physical robot validation of every scenario;
- universal superiority over existing humanoid-control systems;
- that the public repository exposes proprietary SSI internals.

The humanoid branch should therefore be read as **implemented software-level cross-domain R&D infrastructure and demonstrator evidence**, with physical hardware validation reserved for later collaboration.
