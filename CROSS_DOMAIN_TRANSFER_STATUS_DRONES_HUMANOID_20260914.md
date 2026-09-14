# SSI V5 — Cross-domain transfer status: DRONES + HUMANOID

**Date:** 2026-09-14  
**Status:** `IMPLEMENTED SOFTWARE-LEVEL DOMAIN TRANSFER IN TWO EXTERNAL DOMAINS`

## Summary

SSI V5 now has two implemented software-level domain-transfer laboratories outside the original BODY environment:

1. **DRONE / SWARM DOMAIN**
2. **HUMANOID MOTION / STABILITY DOMAIN**

This is an important project-status change. Both domains were previously described mainly as planned or predeclared research targets. They now exist as runnable software research demonstrators with dedicated interfaces, scenario libraries and evidence-oriented experiment paths.

The public repository still does not distribute proprietary SSI source code. It documents capabilities, experiment structure, evidence boundaries and current claim limits.

## Why these two domains matter

The two domains were selected because they stress different kinds of transfer.

### Drone / swarm domain

The drone branch stresses:

- multiple independent units and groups;
- local versus collective experience;
- distributed task reassignment;
- coverage-gap recovery;
- route adaptation;
- communication / localization degradation;
- retained incident history;
- comparison of local learning versus cross-grid consolidation;
- execution-depth and timing comparisons.

### Humanoid domain

The humanoid branch stresses:

- coupled whole-body state;
- articulated joint chains;
- balance and center-of-mass effects;
- slip / low-friction conditions;
- obstacle / terrain interaction;
- prediction before instability;
- recovery after instability;
- retained failure experience;
- before/after learning comparisons;
- new-scene / held-out combinations.

Together, the two laboratories test whether the same higher-level SSI research methodology can be represented across materially different problem structures.

## Shared cross-domain research pattern

Both laboratories follow the same high-level pattern:

```text
NEW DOMAIN
-> DOMAIN-SPECIFIC STATE
-> EVENT / CHALLENGE
-> FLOW SELECTION
-> RESULT
-> EXPERIENCE RETAINED
-> REPEAT / ADAPT
-> OPTIONAL CONSOLIDATION
-> BEFORE / AFTER COMPARISON
-> EVIDENCE
```

The domain-specific details differ, but the research questions remain consistent:

- can experience be retained rather than discarded;
- can previous failures affect later decisions;
- can different execution depths be compared;
- can local competence remain local before consolidation;
- can validated competence later be shared;
- can the resulting change be measured and reviewed.

## Implemented interfaces

Both branches include dedicated domain interfaces rather than relying only on text logs.

### Drone laboratory interface

The drone interface is designed around:

- multiple grids / groups;
- visual scenario state;
- event injection in controlled software scenarios;
- local versus collective state;
- flow-depth comparison;
- before / after memory effects;
- consolidation result summaries;
- evidence and timing views.

Representative scenarios include coverage-gap recovery, communication blackspots, degraded localization, task handoff, route obstruction and adverse-environment rerouting.

### Humanoid laboratory interface

The humanoid interface is designed around:

- a ready 3D humanoid representation;
- articulated joint chains;
- locomotion state;
- obstacle and terrain scenes;
- slip / low-friction scenes;
- instability and recovery state;
- prediction / reaction comparison;
- before / after learning loops;
- scene switching and external-scene extension.

Representative cases include normal walking, stopping before an obstacle, bypass, uneven terrain, slip, recovery, load change and combined challenge scenes.

## What is demonstrated now

At the software-laboratory level, the project now demonstrates that SSI-oriented experiment structure can be instantiated in at least two substantially different external domains.

This includes:

- dedicated domain state;
- domain-specific scenarios;
- domain-specific interfaces;
- repeatable attempts;
- retained incident / failure history;
- before / after comparisons;
- timing / flow measurements;
- evidence capture;
- external challenge entry points.

This is stronger than a roadmap claim, but weaker than physical validation.

## What is deliberately not public

The public repository does not expose the proprietary implementation required to reproduce SSI internally.

Not published:

- proprietary source code;
- private Router V10 implementation;
- private Router S10 implementation;
- private Micronetwork topology;
- prompts;
- private thresholds;
- ROOT controls;
- internal skill definitions.

Public evidence focuses on:

- what was tested;
- what happened;
- what changed;
- how long it took;
- whether prior experience changed a later run;
- whether consolidation changed availability of competence;
- current limitations.

## Current status table

| Domain | Status | Interface | Scenario library | Before/after | External challenge path | Physical validation |
|---|---|---|---|---|---|---|
| Drones / Swarm | Implemented software research demonstrator | Yes | Yes | Yes | Yes | Not claimed |
| Humanoid | Implemented software research demonstrator | Yes, including 3D view | Yes | Yes | Yes | Not claimed |

## Recommended reviewer path

For drone-domain details:

- [`DRONE_DOMAIN_RND_COLLABORATION_STATUS_20260914.md`](DRONE_DOMAIN_RND_COLLABORATION_STATUS_20260914.md)

For humanoid-domain details:

- [`HUMANOID_DOMAIN_TRANSFER_RND_STATUS_20260914.md`](HUMANOID_DOMAIN_TRANSFER_RND_STATUS_20260914.md)

For the original planned transfer mechanism and predeclared experiment logic:

- [`POST21_TRANSFER_MECHANISM_EVOLUTION_DRONES_HUMANOID_PROTOCOL_20260907.md`](POST21_TRANSFER_MECHANISM_EVOLUTION_DRONES_HUMANOID_PROTOCOL_20260907.md)
- [`EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md`](EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md)

## Claim boundary

The current evidence supports **implemented software-level cross-domain research infrastructure** in drones and humanoid robotics.

It does not yet establish:

- certified physical drone operation;
- certified physical humanoid operation;
- production readiness;
- complete hardware integration;
- independent external replication;
- universal cross-domain transfer;
- AGI;
- universal superiority over domain-specific control systems.

The next credibility step is external challenge definition and independent domain review under frozen acceptance criteria.
