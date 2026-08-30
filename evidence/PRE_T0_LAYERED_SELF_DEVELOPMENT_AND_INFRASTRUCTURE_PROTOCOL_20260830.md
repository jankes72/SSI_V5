# SSI V5 — PRE-T0 Layered Self-Development and Infrastructure Protocol

**Status:** `PRE-T0 / RESEARCH PROTOCOL / ROOT-DEFINED`  
**Date:** `2026-08-30`  
**Scope:** ROBERT, CONTINUUM, micronetworks, LEGO development, Eyes/Hands, technology collection, infrastructure scaling and comparative evidence.

## 1. Why this document exists

The current PRE-T0 ROBERT configuration is intentionally simplified so that the core mechanisms can be observed without mixing too many active causes at once. The goal is not only to prove that a task can be completed. The goal is to measure **how the path to completion changes as capability layers are added**.

The baseline includes the core mechanisms needed to observe Experience, micronetwork growth, candidate/challenger/champion lifecycle, resolver/reuse, LEGO execution, checkpoint/restart/replay and evidence.

A successful final artifact is necessary, but it is not the only result.

## 2. What every experiment should measure

For each run, record at minimum:

- total execution time;
- number of LEGO steps;
- repeated LEGO steps;
- retries and failed attempts;
- returns to earlier checkpoints;
- model/provider/tool selected;
- model switches during the mission;
- feedback loops;
- human interventions;
- generated Experience;
- created/reused skills;
- created/reused micronetworks;
- candidate/challenger/champion transitions;
- final outcome quality;
- evidence and timestamps.

The research question is not only `DID IT WORK?`, but also `HOW DID IT WORK, HOW LONG DID IT TAKE, WHAT FAILED, WHAT WAS REUSED, AND WHAT CHANGED?`.

## 3. Layered comparison

The intended research pattern is:

```text
ROBERT BASELINE
-> TASK CLASS
-> FULL TRACE + OUTCOME

ROBERT + NEXT CAPABILITY LAYER
-> COMPARABLE TASK CLASS
-> FULL TRACE + OUTCOME

COMPARE
-> TIME
-> ERRORS
-> RETRIES
-> LEGO REBUILDS
-> MODEL SWITCHES
-> FEEDBACK LOOPS
-> CHECKPOINT RETURNS
-> SKILL REUSE
-> MICRONETWORK GROWTH
-> CHALLENGER / CHAMPION TRAJECTORY
-> FINAL QUALITY
```

Additional observation, classification, data-fragment selection, micronetwork-context, research, CEPA, Brainstorm/Tornado/Storm and other higher layers are not considered useful merely because they exist in code. Their value must be demonstrated by a measurable change in behavior.

Possible valid outcomes include:

```text
MORE LAYERS -> BETTER
MORE LAYERS -> NO CHANGE
MORE LAYERS -> MORE COMPLEXITY / MORE ERRORS
```

All are research results and should remain public when safe to publish.

## 4. Hello World and Tetris

Hello World is a minimal execution threshold. Tetris is a more complex controlled task because it can expose planning depth, model/tool selection, LEGO reuse, repair behavior, feedback loops, checkpointing and skill formation.

The Tetris test should therefore not be summarized only as `TETRIS BUILT = PASS`.

The trace should show the path that led to the result.

## 5. Eyes / Hands as a separate experiment

Eyes/Hands is a separate empirical claim from code generation.

```text
ROBERT / CONTINUUM BUILDS APPLICATION
-> APPLICATION IS FROZEN FOR TEST
-> EYES OBSERVE SCREEN / APPLICATION STATE
-> HANDS SEND CONTROL INPUT
-> ROBERT ACTS IN APPLICATION
-> OUTCOME IS OBSERVED
-> MACHINE EVIDENCE IS RECORDED
```

For Tetris, this separates:

1. ROBERT/CONTINUUM built a functioning Tetris application.
2. ROBERT later used Eyes/Hands to perceive and control it.

The second claim requires its own machine evidence, errors, retries, timestamps, process state and disclosure of human intervention.

## 6. Technology Memory / External Technology Knowledge Store

ROBERT's research architecture is not limited to searching for a solution only after a problem appears.

A cyclic technology collector may gather material about new:

- models;
- libraries;
- repositories;
- methods;
- benchmarks;
- experiment results;
- tools;
- technical solutions;
- independent work published by different people or teams.

The purpose is to build a persistent **Technology Memory / External Technology Knowledge Store** for later use.

Important distinction:

```text
COLLECTED MATERIAL
!= VERIFIED KNOWLEDGE
!= SSI EXPERIENCE
!= CHAMPION
```

Collected material becomes useful to SSI only after later analysis, combination, testing and outcome.

Example:

```text
SOURCE A -> solves fragment X
SOURCE B -> independently validates mechanism Y
SSI EXPERIENCE -> already contains bottleneck Z

A + B + SSI EXPERIENCE
-> NEW HYPOTHESIS
-> LEGO DECOMPOSITION
-> IMPLEMENTATION / SANDBOX
-> TEST
-> OUTCOME
-> EXPERIENCE
-> POSSIBLE SKILL / CHALLENGER / CHAMPION
```

The collector is therefore a long-term external technology memory, not an automatic truth engine.

## 7. Learning how to self-develop

In the early phase, Programmer Root deliberately provides patterns that teach SSI how controlled development should be performed:

- LEGO decomposition;
- test-before-integration;
- checkpoint/restart/replay;
- regression;
- evidence;
- candidate/challenger/champion lifecycle;
- controlled tool use;
- explicit authority boundaries.

The stronger hypothesis is that these development patterns can themselves become reusable competence.

```text
ROOT-PROVIDED DEVELOPMENT PATTERN
-> REPEATED EXPERIENCE
-> SKILL / MICRONETWORK
-> CHALLENGER
-> VALIDATION
-> CHAMPION
-> LATER SELF-DEVELOPMENT REUSE
```

Self-development therefore does not mean unrestricted self-modification. It means that new strategies or modifications may emerge from accumulated Experience, micronetworks, Technology Memory and validated engineering patterns even when the exact final solution was not explicitly hard-coded by Programmer Root.

## 8. Tailscale and infrastructure portability

Tailscale is not treated only as a convenient connection between current local computers. The local setup is a small-scale laboratory for a future distributed architecture.

The intended property is that a logical node role is not permanently tied to one physical machine.

```text
LOCAL NODE TODAY
-> SAME LOGICAL ROLE
-> VPS / DEDICATED SERVER TOMORROW
-> MULTIPLE REMOTE NODES LATER
```

This allows infrastructure to migrate from local machines to remote servers without redesigning the entire logical communication model.

Tailscale is only the network layer. Larger scale still requires separate orchestration mechanisms such as scheduling, queues, synchronization, locks/leases, deduplication, resource allocation, health checks, monitoring, retries, recovery and distributed evidence.

## 9. From one CONTINUUM to many

CONTINUUM is designed with future parallel execution in mind.

```text
ONE LOCAL EXECUTION PATH
-> MULTIPLE LOCAL/REMOTE WORKERS
-> MULTIPLE CONTINUUM EXECUTION INSTANCES
-> DISTRIBUTED SERVER INFRASTRUCTURE
-> LARGER PARALLEL CAPACITY
```

Claims about large numbers of parallel CONTINUUM instances remain `PLANNED/HYPOTHESIS` until verified by scaling tests.

Future tests should measure concurrency conflicts, synchronization, cost, failure isolation, restart/recovery, evidence consistency and resource contention.

## 10. Economic growth as capability growth

One SSI hypothesis links real economic outcome to real infrastructure growth.

At small scale, development budget can fund hardware, models, APIs and tools. At larger scale, it can fund compute, storage, VPS/dedicated servers, monitoring and distributed execution capacity.

```text
REAL VERIFIED PROFIT
-> DEVELOPMENT BUDGET
-> COMPUTE / STORAGE / MODELS / API
-> SERVERS / NETWORK / OBSERVABILITY
-> MORE EXECUTION CAPACITY
-> MORE CONTROLLED EXPERIMENTS
```

This is a planned resource-allocation mechanism, not a guarantee of profit.

The important research property is that increased capital can expand the physical capability envelope of SSI instead of remaining only an accounting result.

## 11. Public evidence vs private implementation

The public research mirror should make claims auditable without requiring publication of every private implementation detail.

Publicly useful material includes:

```text
HYPOTHESIS
-> MODULE / CAPABILITY NAME
-> ROLE
-> TEST PROTOCOL
-> MACHINE EVIDENCE
-> FAILURES
-> OUTCOME
-> INTERPRETATION
```

Private implementation may still retain secrets, tokens, private endpoints, internal heuristics, exact thresholds/weights, private runtime structures, full prompt chains and other implementation details that are not necessary to evaluate the research claim.

## 12. Final PRE-T0 principle

The public record should preserve the full trajectory:

```text
BASELINE
-> TASK
-> TRACE
-> FAILURES / RETRIES / MODEL SWITCHES
-> SKILLS / MICRONETWORKS
-> CHALLENGERS / CHAMPIONS
-> OUTCOME
-> NEXT CAPABILITY LAYER
-> COMPARABLE TASK
-> NEW TRACE
-> COMPARISON
```

The objective is not to produce a retrospective success story. The objective is to show, with evidence, whether added SSI mechanisms actually shorten, improve, stabilize or otherwise change the path from problem to verified outcome.

## 13. Collective Competence Evolution — target system effect

The long-term target is not only that ROBERT, Director and individual Agents learn separately. The intended SSI effect is that **independently acquired, portable and verified competence can improve the capability of the whole system**.

All research bodies may share a common trained substrate and verified baseline champions, while preserving separate identity, private history and individual Experience trajectories.

```text
COMMON SSI BODY / CONTINUUM / VERIFIED BASE CHAMPIONS
-> ROBERT
-> DIRECTOR
-> AGENT 1
-> AGENT 2
-> AGENT 3
-> AGENT 4
-> AGENT 5
-> AGENT 6
```

Each unit can then acquire its own Experience, micronetworks, strategies and local champions.

When an Agent develops a potentially useful practical skill, the intended flow is:

```text
AGENT EXPERIENCE
-> LOCAL MICRONETWORK / SKILL
-> CHALLENGER / CHAMPION
-> DIRECTOR COMPARISON
-> ROBERT / DIRECTOR CURRENT CHAMPION COMPARISON
-> INDEPENDENT VALIDATION
```

Possible outcomes include:

```text
NEW SKILL IS BETTER
-> PROMOTE / ADOPT
-> SHARED VERIFIED COMPETENCE

NEW SKILL IS EQUIVALENT BUT CONTAINS NOVEL VERIFIED CASES
-> DEDUPLICATE
-> ENRICH EXISTING CHAMPION
-> REVALIDATE

NEW SKILL IS LOCAL / WORSE / UNSTABLE
-> KEEP LOCAL / REJECT / CONTINUE TESTING
```

Director may also form higher-order micronetworks that compare and integrate evidence from multiple independently developed competence paths.

The intended collective effect is therefore:

```text
INDIVIDUAL LEARNING
-> LOCAL COMPETENCE
-> VALIDATION
-> COLLECTIVE COMPARISON
-> BEST VERIFIED KNOWLEDGE
-> SHARED PRACTICAL CHAMPION
-> STRONGER ROBERT + DIRECTOR
-> STRONGER FUTURE SSI BASELINE
```

This is the target meaning of **Collective Competence Evolution**: one unit may discover something independently, but after validation the practical value of that discovery can become available to the wider SSI system without copying the unit's complete private history, moral trajectory or identity.

For the six-agent longitudinal experiment, this separation is important. Agents may begin with a common trained body and common verified practical competence while later diverging through different worlds, retained data, relationships, decisions, Moral AI trajectories and private Experience. The research objective is then to observe both **individual divergence** and **collective competence gain**.

This section describes the intended target effect. Each transfer, enrichment and higher-order integration still requires machine evidence before it can be treated as empirically demonstrated.