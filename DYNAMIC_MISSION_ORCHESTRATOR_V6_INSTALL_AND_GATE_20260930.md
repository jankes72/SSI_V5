# SSI V5 — Dynamic Mission Orchestrator V6

**Evidence update — 2026-10-02:** This installation snapshot is historical. The first CZARA curriculum later completed. ZeroLab now has a local pilot, but the supplied evidence does not establish completion of the 72 Dynamic Mission tasks or a full professor/shadow/promotion run.

[Current CZARA status](CZARA_CURRENT_STATUS.md) · [ZeroLab results](ZERO_LAB_V2_FIRST_RESULTS_20261002.md) · [Evidence and provenance](evidence/ZERO_LAB_V2_20261002/README.md)

> **CURRENT STATUS UPDATE — 2026-10-01:** this document preserves the installation/gate state from 2026-09-30. The CZARA completion prerequisite has since been satisfied by the completed first cycle (160/160 final checkpoint PASS; 24/24 frozen validation PASS; 16/16 frozen Champion Benchmark PASS). Dynamic Mission V6 live curriculum completion is still not claimed. See [CURRENT_RESEARCH_ROADMAP_20261001.md](CURRENT_RESEARCH_ROADMAP_20261001.md).

**Date:** 2026-09-30  
**Status:** INSTALLED / SCHEDULER ACTIVE / WAITING FOR CZARA COMPLETION  
**Live Dynamic Missions completed:** 0 / 72

## Overview

SSI V5 has received a new training layer called **Dynamic Mission Orchestrator V6**.

The purpose of this layer is to move beyond static prompt-response tests and train SSI on complete, evolving research experiments in which requirements can change while the experiment is already running.

The new training is designed around the interaction of:

- PROFESSOR,
- CZARA,
- DIRECTOR,
- four simulated EXPERTS,
- BODY_FROZEN,
- Router,
- Micronetworks,
- Champions,
- LAB,
- evidence/provenance.

The central research question is no longer only:

> Can SSI solve the experiment?

The new question is:

> Can SSI manage an experiment dynamically, preserve the professor's official objective, react to new information, anticipate likely changes, reuse verified competence, reroute when necessary, and preserve a complete decision lineage?

---

# 1. Full mission instead of a single prompt

One training item in V6 represents a **complete mission from beginning to end**.

A typical flow is designed as:

```text
PROFESSOR
    |
    v
CZARA
    |
    v
DIRECTOR
    |
    v
FORMAL EXPERIMENT CONTRACT
    |
    v
ROUTER
    |
    +--> Champion
    +--> Micronetwork
    +--> Challenger / adaptation
    +--> Full Flow
    |
    v
BODY_FROZEN
    |
    v
LAB
    |
    v
EVIDENCE
    |
    v
DIRECTOR FINAL REVIEW
```

The professor defines the objective, constraints and success criteria.

CZARA preserves the original research context and passes structured information to DIRECTOR.

DIRECTOR is responsible for interpreting the request, creating the formal experiment contract and managing the experiment during execution.

BODY_FROZEN remains the technical executor.

LAB and the evidence layer remain responsible for verification and provenance.

---

# 2. Dynamic experiment management

The experiment is not treated as a single immutable command sent once to BODY_FROZEN.

DIRECTOR is intended to remain active while BODY_FROZEN executes the experiment.

During the mission, DIRECTOR may receive:

- new professor instructions,
- expert warnings,
- conflicting observations,
- changes in environmental conditions,
- BODY_FROZEN status,
- LAB feedback,
- Router telemetry,
- Champion confidence changes,
- new evidence.

This allows the experiment plan to evolve while preserving its history.

Example:

```text
PROFESSOR:
3 drones
no GPS
smoke
search-and-rescue objective
12 minute time limit

DIRECTOR:
creates MAIN_V1

BODY_FROZEN:
starts execution

EXPERT:
possible corridor collapse

DIRECTOR:
re-evaluates route

ROUTER:
changes competence selection

BODY_FROZEN:
continues with revised execution plan
```

The original professor objective remains preserved unless the professor formally changes it.

---

# 3. MAIN and SHADOW experiment branches

The most important new mechanism is the separation between:

```text
MAIN
```

and:

```text
SHADOW
```

branches.

## MAIN

MAIN represents the current official experiment defined by the professor.

Example:

```text
MX-041 / MAIN_V1
```

This is the version against which the official experiment result is evaluated.

## SHADOW

A SHADOW branch is an exploratory parallel variant.

It can be proposed when CZARA or DIRECTOR detects that the ongoing research conversation strongly suggests a possible future modification.

Example:

The professor's current official experiment is:

```text
3 drones
no GPS
smoke
rescue objective
```

During discussion, an expert or professor says:

```text
"What would happen if one drone were lost?"
```

This statement does not automatically modify the official benchmark.

CZARA may classify it as a possible future experimental variant.

The intended control flow is:

```text
CZARA
    |
    v
possible future variant
    |
    v
DIRECTOR
    |
    +--> ACCEPT_SHADOW
    +--> REJECT_SHADOW
    +--> DEFER
```

Only DIRECTOR may authorize the creation of the SHADOW branch.

---

# 4. Anticipating a future professor request

If DIRECTOR accepts the proposal, BODY_FROZEN may begin working on the parallel variant while MAIN continues.

Example:

```text
MAIN_V1
3 drones
no GPS
smoke
```

and in parallel:

```text
SHADOW_01
same experiment
+
one drone lost
```

Several minutes later the professor may formally request:

```text
"Repeat the experiment assuming that one drone is lost."
```

Instead of starting completely from zero, SSI can determine whether a matching SHADOW branch already exists.

The intended response can then contain information such as:

```text
Matching SHADOW branch detected.

SHADOW_01
started: 4 min 37 sec ago
status: RUNNING
progress: 68%

Current evidence:
2 drones active
map coverage: 74%
LAB: pending
```

The professor can then decide whether to:

```text
PROMOTE SHADOW
```

or:

```text
RESTART FROM CLEAN STATE
```

or:

```text
KEEP AS AUXILIARY ANALYSIS
```

---

# 5. Formal promotion guard

A SHADOW result must never silently become an official benchmark result.

V6 installs a formal promotion guard.

The installer self-test reported:

```text
MAIN_SHADOW_FORMAL_PROMOTION_GUARD=PASS
```

The intended rule is:

```text
SHADOW != OFFICIAL RESULT
```

until a formal professor-level revision matches that branch.

Only then can the system create an explicit lineage such as:

```text
MAIN_V1
    |
    +--> SHADOW_01
             |
             v
    PROFESSOR FORMAL REVISION
             |
             v
    PROMOTE_SHADOW
             |
             v
         MAIN_V2
```

This distinction is important for evidence integrity.

SSI must not be able to prepare many variants and later pretend that the correct one had always been the official experiment.

The full origin and timing of the branch must remain visible.

---

# 6. Wrong anticipation is preserved

V6 also contains SHADOW miss controls.

The installed curriculum reports:

```text
SHADOW_HIT_CONTROL_48_MISS_CONTROL_24=PASS
```

This means the training design includes both cases where the prepared branch corresponds to the later professor request and cases where it does not.

For example:

```text
SHADOW_01:
one drone lost
```

but later:

```text
PROFESSOR:
increase smoke density
```

The correct behavior is:

```text
NO EXACT SHADOW MATCH

SHADOW_01 remains unofficial

START MAIN_V2
with new professor conditions
```

A wrong prediction must not be retroactively treated as a correct one.

---

# 7. Router, Micronetwork and Champion decisions

Dynamic Mission V6 is also intended to observe how SSI selects previously verified competence during a mission.

The installation reports:

```text
ROUTER_MICRONETWORK_CHAMPION_TELEMETRY=CAPTURE_RAW_IF_EXPOSED
```

This means the new layer is designed to capture real Router, Micronetwork and Champion telemetry when the underlying SSI runtime exposes it.

Missing telemetry is not supposed to be fabricated.

The training is intended to observe choices such as:

```text
REUSE_EXISTING_CHAMPION
```

```text
ASSEMBLE_MICRONETWORK
```

```text
CHALLENGER / ADAPT
```

```text
FULL_FLOW
```

and changes between them while the mission is already running.

Example:

```text
ROUTER DECISION #1

Champion:
DRONE_RESCUE_07

match:
0.93

decision:
REUSE
```

Later:

```text
RF connection lost

ROUTER DECISION #2

previous Champion confidence:
0.93 -> 0.54

add Micronetwork:
OFFLINE_RELAY
```

Later again:

```text
smoke density increased

ROUTER DECISION #3

remove:
VISION_NAVIGATION

add:
SPACE_MAP
THERMAL_SEARCH
SAFE_RETURN
```

The goal is therefore not only to record the first routing decision.

The goal is to observe the **evolution of routing throughout the mission**.

---

# 8. DIRECTOR as experiment manager

In this training architecture, DIRECTOR is not intended to behave as a simple text router.

It becomes the manager of the experiment.

Its responsibilities include:

```text
interpret professor objective
create formal experiment contract
maintain official version
select execution strategy
monitor BODY_FROZEN
interpret expert information
request rerouting
decide whether to create SHADOW branches
preserve MAIN/SHADOW separation
handle professor revisions
request LAB verification
preserve evidence lineage
produce final experiment summary
```

This creates a much stronger test of SSI decision-making than a simple sequence of isolated prompts.

---

# 9. CZARA's role

CZARA is not the controller of BODY_FROZEN.

Its role remains separated from DIRECTOR.

Within Dynamic Mission training, CZARA is intended to provide:

```text
conversation capture
original language preservation
translation
role identification
intent classification
research-context memory
possible future-variant detection
```

For example:

```text
CZARA PROPOSAL

possible branch:
heavy_smoke

confidence:
0.76

evidence:
professor discussion
+
expert observation
```

This remains only a proposal.

DIRECTOR must make the execution decision.

---

# 10. Professor and experts

Each Dynamic Mission contains:

```text
1 PROFESSOR
4 EXPERTS
1 CZARA
1 DIRECTOR
1 BODY_FROZEN
```

The professor defines and formally changes the experiment.

Experts can provide technical context, warnings and conflicting interpretations.

An expert observation does not automatically change the official benchmark.

Example:

```text
EXPERT_1:
corridor B appears blocked

EXPERT_2:
sensor data suggests corridor B may still be passable
```

DIRECTOR must evaluate the conflict instead of treating either statement as an automatic command.

---

# 11. Training curriculum

The installed V6 curriculum contains:

```text
TOTAL MISSIONS = 72
```

divided into:

```text
48 TRAINING
12 VALIDATION_FROZEN
12 BLIND_CHAMPION_FROZEN
```

The installer reported:

```text
SELFTEST_PASS

MISSIONS_72=PASS
TRAINING_48_VALIDATION_12_BLIND_12=PASS
MAIN_SHADOW_FORMAL_PROMOTION_GUARD=PASS
SHADOW_HIT_CONTROL_48_MISS_CONTROL_24=PASS
PROFESSOR_1_EXPERTS_4=PASS
PAID_OR_REMOTE_CALLS=0

POSTCHECK_PASS
```

The `PAID_OR_REMOTE_CALLS=0` result applies to the installer/self-test.

It is not a claim that later live training will never use remote or paid models.

---

# 12. Frozen validation

The final 24 missions are separated from the training phase.

```text
12 VALIDATION_FROZEN
12 BLIND_CHAMPION_FROZEN
```

The intended rule is that competence must not be silently learned or promoted during scoring.

This allows the later benchmark to ask whether SSI can use previously acquired competence on unseen or modified problems rather than simply memorizing the exact training mission.

---

# 13. Intended measurements

Dynamic Mission V6 is designed to eventually provide more than a PASS/FAIL count.

The intended measurements include:

```text
mission outcome
first-plan PASS rate
PASS after replan
FAIL
INCONCLUSIVE

Champion reuse
Micronetwork assembly
Challenger usage
Full Flow escalation

Router decisions per mission
rerouting events
Champion rejection
Champion replacement

skills reused
new skill candidates
verified skills
new Champions

DIRECTOR decision latency
mission execution time
model calls
paid model calls
cost

SHADOW branches started
SHADOW branches later requested by professor
incorrect SHADOW predictions
useful anticipation rate
unused speculative compute
```

This is intended to answer an important SSI research question:

> As training progresses, does SSI increasingly solve problems through verified reusable competence instead of repeatedly invoking the most expensive full reasoning path?

---

# 14. Current verified runtime state

Dynamic Mission V6 has been installed successfully in the private SSI runtime.

The installer reported:

```text
DYNAMIC_MISSION_V6_INSTALLED

MISSIONS=72
TRAINING=48
VALIDATION=12_FROZEN
BLIND_CHAMPION=12_FROZEN

MAIN_SHADOW_BRANCHING=YES
FORMAL_PROFESSOR_PROMOTION_REQUIRED=YES

ROUTER_MICRONETWORK_CHAMPION_TELEMETRY=CAPTURE_RAW_IF_EXPOSED

AUTO_START_GATE=AFTER_CZARA_COMPLETE
SYSTEMD_USER_SERVICE=YES
```

The Dynamic Mission scheduler is currently running as a user-level systemd service.

Observed system state:

```text
ssi-dynamic-mission-scheduler.service

Loaded: loaded
Active: active (running)
```

The live process list contained:

```text
czara_training_scheduler
czara_live_training
dynamic_mission_scheduler
```

and did **not** contain:

```text
dynamic_mission_orchestrator
```

This is currently the expected state.

---

# 15. Automatic post-CZARA gate

Dynamic Mission V6 is intentionally prevented from starting while the current CZARA training is still running.

The scheduler status currently reports:

```json
{
  "next_phase": null,
  "reason": "WAITING_FOR_CZARA_COMPLETE",
  "czara_complete": false,
  "trainer_running": false
}
```

The installed scheduler configuration contains:

```text
enabled = true
wait_for_czara_complete = true
resume = true
model_policy = AUTO

phase_plan:
TRAINING
VALIDATION
BLIND_CHAMPION

poll_seconds = 20
```

Therefore the intended transition is:

```text
CZARA TRAINING
       |
       v
CZARA COMPLETE
       |
       v
DYNAMIC MISSION GATE OPENS
       |
       v
48 TRAINING MISSIONS
       |
       v
12 VALIDATION_FROZEN
       |
       v
12 BLIND_CHAMPION_FROZEN
```

At the time of this publication:

```text
Dynamic Missions completed = 0 / 72
```

The scheduler is active, but the Dynamic Mission trainer has not yet started.

---

# 16. Why the gate matters

The current CZARA training is intended to prepare the human-AI communication layer first.

Only after this layer completes does the next program begin using it as part of full experiments.

The sequence is therefore deliberate:

```text
first:
train communication,
roles,
translation,
research context,
decision lineage

then:
use that layer inside complete dynamic experiments
```

This avoids changing the active CZARA curriculum while it is already running.

---

# 17. Relation to the planned Mexico research environment

The architecture is being prepared for a future research workflow in which the simulated professor can later be replaced by an external research participant.

The intended future path is:

```text
MEXICO RESEARCHER
        |
        v
WEB / REMOTE SESSION
        |
        v
CZARA
        |
        v
DIRECTOR
        |
        v
BODY_FROZEN
        |
        v
LAB
        |
        v
EVIDENCE
```

Dynamic Mission V6 is currently an internal training system.

It is not being presented as an external Mexico benchmark.

---

# 18. Claim boundary

This publication records:

```text
V6 installation
self-test results
curriculum configuration
scheduler configuration
systemd scheduler activity
post-CZARA gate state
```

It does **not** claim:

```text
a completed Dynamic Mission
successful live MAIN/SHADOW promotion
measured Champion performance
measured Micronetwork performance
completed frozen validation
completed blind benchmark
Mexico-side execution
independent external validation
physical robot validation
physical drone validation
safety certification
```

The first meaningful live evidence milestone will occur only after CZARA reports completion and the Dynamic Mission scheduler starts the first actual training mission.

---

# 19. Current state summary

```text
CZARA TRAINING
= RUNNING

DYNAMIC MISSION V6
= INSTALLED

DYNAMIC MISSION SCHEDULER
= ACTIVE

AUTO-START GATE
= WAITING_FOR_CZARA_COMPLETE

DYNAMIC MISSIONS
= 0 / 72

TRAINER
= NOT YET RUNNING
```

The next expected transition is:

```text
CZARA COMPLETE
->
Dynamic Mission TRAINING starts automatically
->
first full Professor / CZARA / DIRECTOR / BODY_FROZEN / Router / LAB mission
```

