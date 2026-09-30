# SSI V5 — Reviewer Index

**Current public state:** `2026-09-30`  
**Repository role:** public evidence and review mirror for a private SSI implementation.  
**Audience:** grant reviewers, research collaborators, technical reviewers and validation partners.

This file is the shortest route through the repository. Historical files remain preserved for provenance, but they are not the recommended starting point.

## 5-minute review

1. [S20-S26 operator stop and LAB repair incident](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_AND_LAB_REPAIR_20260930.md) — current training boundary, diagnosis, repair status and claim limits.
2. [Machine-readable S20-S26 stop/repair summary](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_PUBLIC_SUMMARY_20260930.json) — compact current state for audit tooling.

1. [README.md](README.md) — concise project front door and current state.
2. [S19 observability incident and pre-S20 status](RESULTS/SSI_V5_S19_OBSERVABILITY_INCIDENT_AND_PRE_S20_STATUS_20260929.md) — S19 executed 210/210; post-stage consolidation blocked by an observability-induced integration regression.
3. [Pre-S20 hardening preregistration](SYSTEM/SSI_V5_PRE_S20_OBSERVABILITY_AND_EVIDENCE_HARDENING_PREREGISTRATION_20260929.md) — frozen controls before S20.
4. [External review attribution](EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md) — maps Hamid Ahmadian's DEV feedback to concrete SSI requirements.
5. [Latest S13-S18 routing and recovery evidence](RESULTS/SSI_V5_S13_S18_ROUTING_AND_RECOVERY_UPDATE_20260929.md) — 1,260 unique completed cases, 1,197 PASS (95.00%), six committed consolidations and bounded routing claims.
6. [S11 consolidation + WEB BLOCKS update](RESULTS/SSI_V5_S11_CONSOLIDATION_AND_WEB_LEGO_UPDATE_20260926.md).
7. [Machine-readable S13-S18 routing summary](RESULTS/SSI_V5_S13_S18_ROUTING_PUBLIC_SUMMARY_20260929.json) — current unique-case training/routing state and claim boundaries.
8. [Preserved previous S11 results](RESULTS/SSI_V5_S11_FULL_RESULTS_20260923.md) — earlier 210-case traversal retained for provenance.
9. [BLOCKS Pocket, META-BLOCKS and Director-connected laboratories](SYSTEM/LEGO_POCKET_META_LEGO_AND_DIRECTOR_LABS_20260922.md) — component roles and implementation/validation boundaries.
10. [CURRENT_TRUTH_INDEX.md](CURRENT_TRUTH_INDEX.md) — canonical pointer to the latest evidence-backed state.
11. [START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md) — reviewer-oriented project summary.
12. [RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md) — latest measured cross-domain laboratory report.
13. [RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json](RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json) — machine-readable public summary.


## Planned Mexico robotics training / CZARA review path

For reviewers interested in the next planned robotics collaboration track:

1. [CZARA — Mexico Research Context, Translation and Learning Layer](SYSTEM/CZARA_MEXICO_RESEARCH_LAYER_20260926.md)
2. [Mexico Robotics Training and External Benchmark Plan](MEXICO_ROBOTICS_TRAINING_AND_BENCHMARK_PLAN_20260926.md)

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

A repair package (`SSI_LAB_REPAIR_20260930.zip`) was prepared and reported **17/17 offline tests PASS**. The public mirror does **not** yet claim that the live private runtime has been repaired/restarted successfully. Historical verdicts remain preserved.

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

- [COLLABORATION_AND_PARTNER_ENTRY.md](COLLABORATION_AND_PARTNER_ENTRY.md)
- [START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md)

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

