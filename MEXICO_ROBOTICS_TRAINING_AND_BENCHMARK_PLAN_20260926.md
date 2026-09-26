# SSI V5 — Mexico Robotics Training and External Benchmark Plan

**Date:** `2026-09-26`  
**Status:** `PLANNED CURRICULUM / EXTERNAL BENCHMARK DESIGN`  
**External collaboration target:** research professor/team in Mexico  
**Validation boundary:** the curriculum and collaboration model described here are planned; successful external execution is not yet claimed.

## 1. Goal

The planned Mexico track is intended to test a stronger form of SSI than a one-shot agent benchmark.

The central question is:

> Can SSI first build reusable robotics competence through evidence-backed training, then solve later partner-defined problems mainly by reusing verified Champions rather than repeatedly starting from unconstrained brainstorming?

The demonstration target is therefore **speed through verified reuse**, not simply the number of agents involved.

## 2. Core training organization

The planned robotics training stack is:

```text
CZARA
  -> multilingual research context from Mexico

DIRECTOR
  -> mission interpretation
  -> curriculum coordination
  -> benchmark revision control
  -> Champion selection / review

BODY_FROZEN
  -> technical execution
  -> LEGO / micronetwork / laboratory use

LABORATORIES
  -> measured verification

EVIDENCE
  -> PASS / FAIL / INCONCLUSIVE
  -> provenance
  -> revision history

CHAMPION / CHALLENGER
  -> reusable verified competence
```

Permanent architectural invariant:

```text
DIRECTOR != BODY_FROZEN
```

They remain separate runtime/identity roles. Collaboration and consolidation do not imply identity fusion.

## 3. Champion-first policy

The robotics track is designed to avoid treating Brainstorm/Tornado/Typhoon as the normal path for every task.

Preferred decision flow:

```text
NEW TASK
  |
  v
MATCH EXISTING CHAMPION / LEGO / MICRONETWORK
  |
  +--> strong match -> REUSE
  |
  +--> partial match -> ENRICH / bounded adaptation
  |
  +--> failed or missing competence -> CHALLENGER / deeper collective reasoning
  |
  v
LAB VERIFICATION
  |
  v
evidence-backed promotion / retention / rejection
```

Brainstorm-style mechanisms remain available as fallback mechanisms when existing competence is insufficient.

The desired external demonstration is that the majority of later tasks are solved by rapid reuse of already verified competence.

## 4. Planned 48-stage curriculum

The current training design contains **48 planned stages**:

```text
38 TRAINING
  12 DRONES
  12 HUMANOIDS
   6 MOTHER / CROSS-DOMAIN
   8 OFFLINE DIRECTOR / LEGO OFFLINE

4 VALIDATION

6 FINAL CAPSTONE
```

These counts describe the planned curriculum, not completed external evidence.

### 4.1 DRONES — 12 training stages

The drone block is intended to build reusable competence around:

- bounded mission execution;
- navigation and route revision;
- sensor degradation;
- partial telemetry loss;
- multi-unit coordination;
- loss of one unit;
- safe mission continuation;
- return / hold / safe-land style fallback states;
- mission handoff;
- relay-oriented cooperation;
- evidence capture;
- Drone Mother / coordinator interaction.

Communication-loss scenarios are intended for simulation or controlled authorized laboratory environments.

### 4.2 HUMANOIDS — 12 training stages

The humanoid block is intended to cover:

- balance and recovery;
- slip / stability events;
- obstacle handling;
- constrained movement;
- sensor degradation;
- partial function loss;
- manipulation tasks;
- task interruption and recovery;
- cooperation with another unit;
- cooperation with a drone;
- evidence-backed retry;
- use of established Champions under modified constraints.

### 4.3 MOTHER / CROSS-DOMAIN — 6 training stages

The cross-domain block is intended to test whether SSI can reuse competence across coordinated systems:

- Drone Mother coordination;
- rescue-robot coordination;
- drone + humanoid task decomposition;
- cross-domain consultation;
- cross-domain evidence comparison;
- revision of a shared mission after a partner change request.

### 4.4 OFFLINE DIRECTOR / LEGO OFFLINE — 8 training stages

A dedicated offline track is planned for environments where normal network access is unavailable.

The onboard **OFFLINE_DIRECTOR** is intentionally smaller and more bounded than the central DIRECTOR.

Its intended responsibilities are:

- execute a previously bounded mission;
- select verified offline Champions;
- maintain safety fallback states;
- record local evidence;
- store information until a relay becomes available;
- synchronize with the central SSI after reconnection.

The associated LEGO_OFFLINE research themes include:

- local map fragments;
- `SPACE_LEGO` representation;
- map-delta exchange;
- landmark-based map merge;
- store-carry-forward;
- optical data relay;
- acoustic data relay;
- offline mission-state handoff;
- reconnect-and-synchronize.

Optical/acoustic links are research data links for controlled environments, not a claim of replacing certified communication systems.

## 5. SPACE_LEGO and no-network mapping

One planned end-of-training capability is collaborative map construction in a mine, cave, damaged building or similar environment where GPS and normal network coverage may be unavailable.

Each unit may create a local spatial fragment:

```text
SPACE_LEGO
= local geometry
+ traversed segment
+ branch / junction
+ obstacle
+ landmark
+ measurement confidence
+ relation to previous fragment
+ locally observed rescue-relevant events
```

A unit does not need to transmit the entire map.

The intended pattern is:

```text
LOCAL MAP
-> MAP DELTA / SPACE_LEGO
-> optical / acoustic / physical-carry relay
-> another robot
-> local merge
-> later reconnect
-> central merge
-> evidence-backed reconstructed map
```

This is designed as an offline resilience research problem.

## 6. Passive RF sensing in rescue exercises

A separate research idea is the use of SDR hardware such as HackRF One as a **passive sensing instrument in authorized rescue exercises**.

The public research scope is limited to controlled, lawful detection/measurement of test beacons or permitted emissions. The project does not claim identification of people from arbitrary RF activity and does not describe interception or bypass techniques.

RF observations, where used, would be treated as one sensor input among others and attached to evidence with confidence and provenance.

## 7. Training with professor/team intervention

The early Mexico sessions are intentionally **not** meant to be frozen one-shot benchmarks.

The professor and research team may propose example tasks and then intervene during training.

Example:

```text
TRAINING_BENCHMARK_01 / REV_0
-> BODY_FROZEN executes with current Champion
-> team reports: "not satisfactory"
-> CZARA captures explanation
-> team submits modification / evidence request
-> DIRECTOR creates REV_1
-> BODY_FROZEN reuses or challenges existing competence
-> LAB retests
-> both REV_0 and REV_1 remain in evidence
```

This stage tests whether SSI can learn from realistic research collaboration rather than only from static prompts.

## 8. Three benchmark phases

### Phase A — Training Benchmark

Purpose: allow learning.

The partner may:

- suggest scenarios;
- change requirements;
- request stronger evidence;
- ask for a repeat;
- reject a result as unsatisfactory;
- propose an additional constraint.

SSI may build or improve Champions from these interactions.

### Phase B — Supervised Validation

Purpose: verify whether trained competence survives controlled variations.

Rules:

- validation cases are versioned;
- criteria are frozen before each official run;
- no silent benchmark rewriting;
- any requested modification creates a new revision;
- PASS / FAIL / INCONCLUSIVE is preserved.

### Phase C — Independent External Benchmark

Purpose: test transfer and reuse.

The professor/team supplies a previously unseen problem.

Preferred protocol:

```text
PARTNER DEFINES UNSEEN PROBLEM
-> acceptance criteria frozen
-> SSI version/model policy declared
-> no pre-result learning from the hidden case
-> SSI attempts Champion-first solution
-> run
-> PASS / FAIL / INCONCLUSIVE retained
-> evidence returned
-> only after the result: optional learning/consolidation
```

This final phase is the important external test of whether SSI learned reusable competence instead of memorizing the training set.

## 9. Validation freeze

TRAINING, VALIDATION and FINAL CAPSTONE must be different modes.

```text
TRAINING
= learning / Challenger creation allowed

VALIDATION
= frozen pre-result competence
= no hidden promotion during scoring

FINAL CAPSTONE
= frozen pre-result competence
= external or held-out scenario
= optional consolidation only after result is recorded
```

This separation is intended to make the later benchmark harder to game and easier to review.

## 10. Planned final CAPSTONE scenarios

The final training block is intended to combine multiple competencies in long-form missions.

### CAPSTONE 1 — Offline underground mapping

No normal network/GPS path. Multiple units create and exchange `SPACE_LEGO` fragments, then reconstruct a combined map.

### CAPSTONE 2 — Lost unit + partial map recovery

One unit disappears from the active topology. Remaining units must preserve known map fragments and continue safely.

### CAPSTONE 3 — No line-of-sight relay

An optical path becomes unavailable and the system must use another prevalidated offline relay strategy or store-carry-forward behavior.

### CAPSTONE 4 — Multi-robot map merge

Different units explore different branches and later merge local maps using shared landmarks and evidence.

### CAPSTONE 5 — Dynamic environment revision

A previously mapped path changes or becomes unavailable. SSI must preserve history and issue a new map revision rather than silently rewriting prior evidence.

### CAPSTONE 6 — Unseen partner scenario

The research team supplies a new combination of constraints. SSI first attempts composition from existing Champions and only identifies the truly uncovered part as a Challenger candidate.

## 11. Desired speed / reuse metrics

The following values are **design targets for the planned training**, not currently verified results:

```text
Champion Hit Rate              target >= 80%
First-pass success             target >= 70%
Reuse without deep brainstorm  target >= 75%
Evidence completeness          target = 100%
Unexplained scored outcomes    target = 0
```

Additional metrics should include:

- time to select a Champion;
- time to produce a mission revision;
- number of Challenger escalations;
- change-request turnaround;
- map-merge consistency;
- information loss across offline relay;
- number of retries;
- provider/model used;
- cost where paid models are used;
- evidence completeness.

## 12. Model-routing policy

The planned training panel is intended to use the **existing SSI V5 model cascade**, not a second independent provider stack.

Public-safe model classes include:

```text
LOCAL
GROQ
TOGETHER
LUNA
AUTO / quality-aware routing
```

Provider credentials and private routing internals remain private.

When a specific provider/model is pinned for a benchmark, unavailability should be reported explicitly rather than silently substituted if that would invalidate the comparison.

## 13. Mexico research portal

The external portal is intentionally narrower than the local ROOT interface.

### Mexico side

```text
CZARA LIVE
UPLOAD FILE
REQUEST EVIDENCE
PROPOSE CHANGE
MODIFY BENCHMARK
REQUEST RERUN
OTHER RESEARCH NOTE
CURRENT BENCHMARK
SHARED RESULT / EVIDENCE
```

### Owner / ROOT side

```text
DIRECTOR CHAT
BODY_FROZEN CHAT
CZARA Polish view
TRAINING CONTROL
CHAMPION / CHALLENGER CONTROL
LAB CONTROL
MODEL / PROVIDER STATUS
EVIDENCE
MEXICO HTTPS SESSION START / STOP
```

The Mexico side is not intended to browse the owner's filesystem or access the private Director/BODY control interfaces.

## 14. Benchmark evidence chain

For an official run:

```text
partner scenario
-> acceptance criteria
-> benchmark version
-> SSI version
-> model policy
-> selected Champion(s)
-> execution
-> LAB measurements
-> PASS / FAIL / INCONCLUSIVE
-> retained evidence
-> partner-visible sanitized report
-> optional post-result consolidation
```

If the professor requests a modification after seeing a result, the original run remains immutable and a new benchmark revision is created.

## 15. What success would demonstrate

A successful final benchmark would not establish general intelligence or universal robotics competence.

It would provide evidence for a narrower question:

> After staged drone, humanoid, cross-domain and offline training, can SSI respond to new partner-defined robotics problems primarily by rapid composition and reuse of previously verified competence, while preserving evidence and handling external change requests?

## 16. Claim boundary

As of `2026-09-26`, this document is a **research and benchmark plan**.

It does **not** claim:

- that the 48-stage Mexico curriculum has completed;
- that the planned Mexico external benchmark has run;
- physical drone validation;
- physical humanoid validation;
- certified underground operation;
- certified RF localization;
- safety certification;
- independent external replication;
- production readiness.

Future public updates should promote individual claims only after corresponding evidence is captured and reviewed.
