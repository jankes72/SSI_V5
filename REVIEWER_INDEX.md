# SSI V5 — Reviewer Index

**Current public state:** `2026-10-01`  
**Repository role:** public R&D, evidence and external-validation hub for a private SSI implementation.  
**Audience:** grant reviewers, research collaborators, technical reviewers and validation partners.

This file is the shortest route through the repository. Historical files remain preserved for provenance, but they are not the recommended starting point.

## 5-minute review

For a grant, consortium or partner-entry review, start with [GRANT_AND_CONSORTIUM_ENTRY_20261001.md](GRANT_AND_CONSORTIUM_ENTRY_20261001.md) and the [grant/consortium package](GRANT_CONSORTIUM/README.md).

1. [Current research roadmap — 2026-10-01](CURRENT_RESEARCH_ROADMAP_20261001.md) — canonical current programme state and claim boundaries.
2. [CZARA first training cycle — final results](CZARA_FIRST_TRAINING_CYCLE_RESULTS_20261001.md) — 160/160 final checkpoint PASS, 520/520 skills QUALIFIED, frozen validation and Champion results.
3. [CZARA sanitized run-level evidence](evidence/CZARA_FIRST_TRAINING_20261001/README.md) — reviewer-accessible 537-run evidence index and CSV.
4. [S20-S26 operator stop and LAB repair incident](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_AND_LAB_REPAIR_20260930.md) — separate current core-training reliability boundary.
5. [Machine-readable S20-S26 stop/repair summary](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_PUBLIC_SUMMARY_20260930.json) — compact audit state.
6. [CURRENT_TRUTH_INDEX.md](CURRENT_TRUTH_INDEX.md) — canonical pointer to the latest evidence-backed state.
7. [START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md) — reviewer-oriented project summary.
8. [ZERO-LAB / LAB_ARCHITECT](CZARA_ZERO_LAB_LAB_ARCHITECT_MODULE_20261001.md) — next CZARA research module; local integration not yet claimed.
9. [Historical S19 observability incident](RESULTS/SSI_V5_S19_OBSERVABILITY_INCIDENT_AND_PRE_S20_STATUS_20260929.md) — preserved pre-S20 incident chronology.
10. [Pre-S20 hardening preregistration](SYSTEM/SSI_V5_PRE_S20_OBSERVABILITY_AND_EVIDENCE_HARDENING_PREREGISTRATION_20260929.md) — frozen controls used before continuation.
11. [External review attribution](EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md) — external DEV feedback provenance.
12. [Dual Mother measured laboratory report](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md) — preserved cross-domain software-lab evidence.

## CZARA first internal training cycle complete — 2026-10-01

`CZARA-RND-1.0.0` completed its first internal training, frozen validation and frozen Champion benchmark cycle.

```text
UNIQUE STAGES = 160
FINAL CHECKPOINT = 160 / 160 PASS
FINAL QUALIFIED SKILLS = 520 / 520

TRAINING
  120 unique stages
  497 attempts
  120 PASS attempts
  377 intermediate INCONCLUSIVE attempts
  0 FAIL
  learning_applied = true

FROZEN VALIDATION
  24 / 24 PASS
  24 / 24 REUSE
  skill coverage = 1.0
  learning_applied = false

FROZEN CHAMPION BENCHMARK
  16 / 16 PASS
  16 / 16 REUSE
  skill coverage = 1.0
  learning_applied = false

AUTHORITY ERRORS = 0
```

The **377 INCONCLUSIVE records are preserved intermediate training/retry attempts**, not unresolved final curriculum stages. The final checkpoint records all 160 unique stages as PASS.

This is internal SSI evidence for the planned Poland-Mexico research workflow. It is **not** an independent Mexico benchmark, physical robotics validation, safety certification or external replication.

- [CZARA first training cycle — final results](CZARA_FIRST_TRAINING_CYCLE_RESULTS_20261001.md)
- [Machine-readable public summary](evidence/CZARA_FIRST_TRAINING_CYCLE_PUBLIC_SUMMARY_20261001.json)
- [Sanitized run-level evidence](evidence/CZARA_FIRST_TRAINING_20261001/README.md)
- [Historical S120 checkpoint — preserved](RESULTS/CZARA_RND_1_0_0_TRAINING_CHECKPOINT_S120_20260930.md)
- [ZERO-LAB / LAB_ARCHITECT next module](CZARA_ZERO_LAB_LAB_ARCHITECT_MODULE_20261001.md)

## Planned Mexico robotics training / CZARA review path

For reviewers interested in the Mexico collaboration track, start with the active internal CZARA checkpoint, then the architecture and benchmark-plan records:

1. [CZARA first training cycle — final results](CZARA_FIRST_TRAINING_CYCLE_RESULTS_20261001.md)
2. [Sanitized CZARA run-level evidence](evidence/CZARA_FIRST_TRAINING_20261001/README.md)
3. [Historical CZARA S120 checkpoint](RESULTS/CZARA_RND_1_0_0_TRAINING_CHECKPOINT_S120_20260930.md)
4. [CZARA — Mexico Research Context, Translation and Learning Layer](SYSTEM/CZARA_MEXICO_RESEARCH_LAYER_20260926.md)
5. [Mexico Robotics Training and External Benchmark Plan](MEXICO_ROBOTICS_TRAINING_AND_BENCHMARK_PLAN_20260926.md)

These documents are **architecture and benchmark-plan records**, not completed external evidence. They describe the intended multilingual collaboration layer, Champion-first training policy, 48-stage curriculum, offline/underground capstones and the separation between training, validation and final external benchmark.

## Technical architecture review

1. [SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md](SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md)
2. [VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md](VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md)
3. [RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md](RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md)
4. [Current Football World implementation boundary](RESULTS/FOOTBALL_WORLD_IMPLEMENTATION_BOUNDARY_20260922.md)

## Evidence / falsification review

1. [evidence/README.md](evidence/README.md) — evidence-layer index and chronology.
2. [CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md](CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md)
3. [EXTERNAL_CHALLENGE_ENTRY_20260914.md](EXTERNAL_CHALLENGE_ENTRY_20260914.md)
4. [LIVE_EXTERNAL_REVIEW_SESSION_PROTOCOL_20260907.md](LIVE_EXTERNAL_REVIEW_SESSION_PROTOCOL_20260907.md)

Evidence policy:

```text
PRESERVE FAILURES
PRESERVE SUPERSEDED STATES
FREEZE ACCEPTANCE CRITERIA BEFORE OFFICIAL RUNS
KEEP VERSION / RUN / PROVENANCE IDENTITY
SEPARATE SOFTWARE-LAB RESULTS FROM PHYSICAL VALIDATION
DO NOT CLAIM UNPUBLISHED OR IN-PROGRESS WORK AS VERIFIED
```

## Current training status — operator stop and LAB repair boundary — 2026-09-30

Core training progressed through completed S20-S25 stages and into S26. The operator then **manually stopped the run with Ctrl-C** because the number of `INCONCLUSIVE` outcomes and pending cases was increasing and no longer represented a trustworthy training signal.

Latest preserved diagnostic snapshot:

```text
TOTAL = 1,326
PASS = 848
INCONCLUSIVE = 470
FAIL = 8
S20-S25 verified-subset consolidations = PASS for BODY_FROZEN + DIRECTOR
S26 = interrupted / not claimed complete
```

A targeted diagnostic sample of **18 cases** showed that the apparent `unparseable_json` symptom was an **empty response after `INFLIGHT_LIMIT`**. This finding is limited to the inspected sample and is **not** generalized to every unresolved case.

The diagnosis also identified two additional reliability gaps: required task outputs were not always propagated correctly to the reviewer path, and dedicated R&D execution scenarios remain incomplete for parts of S20-S26.

A repair package (`SSI_LAB_REPAIR_20260930.zip`) was prepared and reported **17/17 offline tests PASS**. The public hub does **not** yet claim that the live private runtime has been repaired/restarted successfully. Historical verdicts remain preserved.

- [S20-S26 operator stop and LAB repair incident](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_AND_LAB_REPAIR_20260930.md)
- [Machine-readable S20-S26 stop/repair summary](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_PUBLIC_SUMMARY_20260930.json)

**Continuation boundary:** do not treat the old S20-S40 launcher as authorized for restart. The next continuation must preserve a new post-repair runtime/provenance boundary and support frozen-case replay.


## Preserved verified milestone

```text
V4 S1-S10 = COMPLETE / PASS
7 BODY final state = 7/7 PASS
BODY_FROZEN promoted reload = 144/144

POST-S10 DRONE = 6/6 software scenarios PASS
POST-S10 HUMANOID = 15/15 software scenarios PASS

DUAL MOTHER CROSS LAB V1
DRONE MOTHER = 12/12 paired scenario families PASS
RESCUE ROBOT MOTHER = 12/12 paired scenario families PASS
REPEATS = 60 per scenario family
PAIRED MISSIONS = 720
DOMAIN RESULT ROWS = 1,440

CROSS CONSULTATION = 720 measured rounds
CROSS CONSOLIDATION = 360 measured executions
ROLLBACK = 360 measured executions
```

These are software-laboratory results. Physical validation and independent external replication are not claimed.

## Collaboration / grant review

- [Grant and Consortium Entry](GRANT_AND_CONSORTIUM_ENTRY_20261001.md)
- [Grant / Consortium Package Index](GRANT_CONSORTIUM/README.md)
- [COLLABORATION_AND_PARTNER_ENTRY.md](COLLABORATION_AND_PARTNER_ENTRY.md)
- [START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md)

The grant package includes an IP/background-foreground boundary, conservative TRL/validation roadmap, candidate WPs/deliverables/milestones, impact/exploitation/dissemination framework, risk/safety/security/ethics controls, resourcing/budget template and data/reproducibility framework. These are proposal-planning artefacts and do not claim a signed consortium or grant award.

Preferred external model:

```text
PARTNER DEFINES UNSEEN PROBLEM
-> ACCEPTANCE CRITERIA FROZEN
-> SSI RUN
-> PASS / FAIL / INCONCLUSIVE PRESERVED
-> EVIDENCE RETAINED
-> OPTIONAL CONSOLIDATION
-> RE-VALIDATION
```

## Public / private boundary

```text
PUBLIC
= architecture at safe level
+ protocols
+ sanitized evidence
+ results
+ failures / repairs / retests
+ timings
+ hashes / provenance
+ claim boundaries
+ published observer portal

PRIVATE
= proprietary source code
+ Router V10 / S10 implementation internals
+ reconstructive Micronetwork details
+ private Hermes / BODY state
+ ROOT internals
+ prompts / private configuration
+ credentials / endpoints
```

## Historical material

The repository intentionally keeps dated files and older status records. They are evidence of development history, not clutter to be silently rewritten.

When a historical file conflicts with a newer current-state document:

```text
USE THE NEWEST DATED CURRENT-STATE DOCUMENT
KEEP THE OLDER FILE AS HISTORICAL EVIDENCE
```

No historical file needs to be deleted to keep the reviewer path concise.

