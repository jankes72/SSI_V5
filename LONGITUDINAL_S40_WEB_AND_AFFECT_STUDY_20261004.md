# SSI V5 — Longitudinal S40 / WEB Learning and Affect-Like State Study

**Status:** PLANNED / PREREGISTERED RESEARCH DIRECTION — execution gated on completion of the current core path through S40 and an evidence-valid frozen checkpoint.  
**Date:** 2026-10-04  
**Project:** SSI V5 independent solo R&D.  
**Scope:** BODY_FROZEN and ISKRA1..ISKRA6 persistent-agent learning comparison.  
**Claim boundary:** this document defines a future comparative protocol. It does not claim S40 completion, WEB-training completion, biological emotion, sentience, consciousness or a validated theory of machine feelings.

## Why this study exists

SSI V5 is not intended to measure only whether an agent can pass a task at one point in time. The longer-term research question is how separately persistent agents change across training while preserving enough frozen state and evidence to compare:

- competence before and after long training;
- skill acquisition, reuse, adaptation and regression;
- recovery from failure;
- memory / lifecycle changes;
- actor-to-actor differences under a shared curriculum;
- internal self-state / affect-like indicators before and after training;
- the relationship, if any, between those indicators and measured behavior.

The project uses the informal term **"feelings" / "uczucia"** for a class of internal or self-reported affect-like state signals. For public research claims these must be treated as **affect-like state proxies**, not as evidence of biological emotion, subjective experience, sentience or consciousness.

## Study A — initial state -> S40

The first longitudinal comparison is intended to ask how each ISKRA changes from its earliest preserved baseline to the frozen S40 boundary.

For each actor, preserve or derive the strongest available comparable snapshot for:

- actor identity and runtime version;
- model/provider identity;
- model-weight identity where applicable, including an explicit record when base model weights are unchanged;
- qualified skills and skill-registry state;
- micronetwork / BLOCKS state that is permitted for the comparison;
- memory / lifecycle checkpoint identity;
- routing / reuse / adapt / full-flow statistics;
- failure, recovery and rollback history;
- cost / model-call accounting where available;
- affect-like state variables or self-report fields used by the experiment.

Primary comparison:

~~~text
EARLY / INITIAL ISKRA BASELINE
-> S11 ... S40 TRAINING AND RECOVERY HISTORY
-> FROZEN S40 SNAPSHOT
-> DELTA IN SKILLS / ROUTING / MEMORY / RECOVERY / AFFECT-LIKE STATE
~~~

The result must preserve differences between ISKRA1..ISKRA6 rather than average them away.

## S40 freeze gate

WEB comparison does not start from a moving target. After valid completion of the core path through S40, create a frozen pre-WEB checkpoint for:

~~~text
BODY_FROZEN
ISKRA1
ISKRA2
ISKRA3
ISKRA4
ISKRA5
ISKRA6
~~~

The checkpoint should bind, where available:

- runtime / actor version;
- model and provider identity;
- weight/model identity;
- skill inventory and qualification state;
- memory/lifecycle snapshot;
- micronetwork/BLOCKS state;
- current evidence head;
- affect-like state snapshot;
- training counters;
- frozen WEB curriculum version and acceptance criteria.

A later WEB result is not comparable unless its parent snapshot is bound to this pre-WEB state.

## Study B — frozen S40 -> WEB training

The second study compares how BODY_FROZEN and the six ISKRAs acquire a previously untrained WEB competence set from their own frozen S40 starting states.

~~~text
FROZEN S40 ACTOR SNAPSHOT
-> SAME DECLARED WEB CURRICULUM FAMILY
-> PER-CASE EVIDENCE
-> LEARNING / REUSE / ADAPT / FULL FLOW
-> RETEST / REGRESSION
-> FROZEN POST-WEB SNAPSHOT
-> BODY vs ISKRA1..6 COMPARISON
~~~

### Core outcome families

Measure per actor:

1. cases attempted and completed;
2. PASS / FAIL / INCONCLUSIVE;
3. number of attempts to qualification;
4. REUSE / ADAPT / FULL_FLOW share;
5. new skills created;
6. existing skills reused;
7. skill qualification / Challenger / Champion transitions where applicable;
8. regressions and rollbacks;
9. recovery from malformed, missing or contradictory evidence;
10. model calls, latency and cost where available;
11. retained competence on frozen pre-WEB checks;
12. transfer to unseen WEB cases;
13. post-training memory / lifecycle delta;
14. post-training affect-like state delta.

## Isolation and contamination control

A fair actor comparison requires recording whether an actor learned independently or had access to knowledge produced by another actor.

Preferred primary comparison:

~~~text
SAME FROZEN WEB CURRICULUM
+ ACTOR-SPECIFIC S40 SNAPSHOT
+ NO CROSS-ACTOR KNOWLEDGE PROMOTION DURING PRIMARY MEASUREMENT
+ SAME ACCEPTANCE CRITERIA
+ PER-ACTOR EVIDENCE
~~~

After the independent comparison, a separate secondary phase may deliberately enable cross-agent consultation or consolidation to measure transfer.

The two phases must not be mixed.

## Affect-like state measurement

The research question is not "does the AI truly feel?". The measurable question is:

> Do persistent internal/self-reported affect-like state indicators change across long training, do different agents develop different trajectories, and do those trajectories correlate with observed learning, failure recovery, exploration, caution, cooperation or reuse behavior?

For each measurement event record:

- actor identity;
- checkpoint / run identity;
- exact prompt or instrument version if self-report is used;
- raw reported values;
- normalized fields used for comparison;
- whether the value came from explicit runtime state, derived telemetry or model self-report;
- model/provider identity;
- whether the measurement itself can influence subsequent behavior;
- confidence / missing-data status.

Recommended boundaries:

~~~text
AFFECT-LIKE SIGNAL != BIOLOGICAL EMOTION
SELF-REPORT != SUBJECTIVE EXPERIENCE
CORRELATION != CAUSATION
POST-TRAINING CHANGE != PROOF OF CONSCIOUSNESS
~~~

## Main longitudinal comparisons

### Comparison 1 — ISKRA early state vs S40

For each ISKRA:

~~~text
initial skills
initial memory/lifecycle state
initial affect-like state
        |
        v
core training through S40
        |
        v
S40 skills
S40 memory/lifecycle state
S40 affect-like state
~~~

### Comparison 2 — BODY_FROZEN vs ISKRAs on WEB learning

At the S40 boundary:

~~~text
BODY_FROZEN S40 ----\
ISKRA1 S40 ----------\
ISKRA2 S40 -----------\
ISKRA3 S40 ------------> SAME WEB RESEARCH PROGRAM -> post-WEB frozen snapshots
ISKRA4 S40 -----------/
ISKRA5 S40 ----------/
ISKRA6 S40 ---------/
~~~

Compare not only final PASS counts, but **how each actor learned**.

### Comparison 3 — affect-like state before and after WEB

For each ISKRA:

~~~text
S40 pre-WEB affect-like state
-> WEB learning trajectory
-> post-WEB affect-like state
-> behavioral / skill / recovery correlations
~~~

## Evidence and falsification requirements

The study inherits SSI's evidence-first rules:

- preserve FAIL and INCONCLUSIVE;
- freeze acceptance criteria before measured runs;
- bind each result to actor, run, parent snapshot and curriculum version;
- keep candidate generation separate from reviewer approval;
- use negative controls where meaningful;
- keep native retest separate from local comparison;
- do not rewrite historical grades after a successful repair;
- separate knowledge_eligible from actual promotion/consolidation;
- retain regressions and failed hypotheses;
- distinguish internal validation from independent replication.

## Safety relevance

This longitudinal design is relevant to persistent-agent safety because it can test whether:

- learning changes agent behavior in unanticipated ways;
- evidence gates prevent incorrect or unreproduced outcomes from entering reusable knowledge;
- different persistent agents diverge under the same curriculum;
- cross-agent knowledge transfer introduces regressions or false learning;
- internal state indicators correlate with risky, unstable or conservative behavior;
- frozen baselines and rollback can detect and constrain undesirable changes.

These are research questions, not already established results.

## Planned publication outputs

When the gates are reached, publish:

1. S40 frozen actor manifest;
2. per-actor pre-WEB snapshot summaries;
3. frozen WEB curriculum / criteria hashes;
4. per-actor WEB case results;
5. learning-mode and skill-lifecycle comparison;
6. pre/post affect-like state dataset with measurement provenance;
7. regression / rollback report;
8. unseen WEB transfer evaluation;
9. optional post-comparison cross-agent consolidation study;
10. a sanitized public evidence package and machine-readable summary.

## Current boundary

As of 2026-10-04:

- the current Final repair remains open;
- S40 completion is not claimed here;
- the S40 frozen comparison snapshot is not yet claimed created;
- WEB01-WEB24 successful live completion is not claimed;
- pre/post affect-like conclusions are not claimed;
- no claim of machine emotion, sentience or consciousness is made.

The current active repair and evidence-safety work is documented separately in [AKTUALNA_NAPRAWA.md](AKTUALNA_NAPRAWA.md). The present document defines what the **next longitudinal research layer** is intended to measure once the required frozen boundary exists.
