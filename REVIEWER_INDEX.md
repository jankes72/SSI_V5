# SSI V5 — Reviewer Index

**Current public state:** `2026-09-26`  
**Repository role:** public evidence and review mirror for a private SSI implementation.  
**Audience:** grant reviewers, research collaborators, technical reviewers and validation partners.

This file is the shortest route through the repository. Historical files remain preserved for provenance, but they are not the recommended starting point.

## 5-minute review

1. [README.md](README.md) — concise project front door and current state.
2. [Latest S12 live training + committed consolidation](RESULTS/SSI_V5_S12_LIVE_TRAINING_AND_CONSOLIDATION_20260926.md) — 210/210 live S12 traversal, 203 verified cases, 7 unresolved and committed consolidation.
3. [S11 consolidation + WEB LEGO update](RESULTS/SSI_V5_S11_CONSOLIDATION_AND_WEB_LEGO_UPDATE_20260926.md).
4. [Machine-readable latest summary](RESULTS/SSI_V5_S11_CONSOLIDATION_AND_WEB_LEGO_PUBLIC_SUMMARY_20260926.json).
5. [Preserved previous S11 results](RESULTS/SSI_V5_S11_FULL_RESULTS_20260923.md) — earlier 210-case traversal retained for provenance.
6. [LEGO Pocket, META-LEGO and Director-connected laboratories](SYSTEM/LEGO_POCKET_META_LEGO_AND_DIRECTOR_LABS_20260922.md) — component roles and implementation/validation boundaries.
7. [CURRENT_TRUTH_INDEX.md](CURRENT_TRUTH_INDEX.md) — canonical pointer to the latest evidence-backed state.
8. [START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md) — reviewer-oriented project summary.
9. [RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md) — latest measured cross-domain laboratory report.
10. [RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json](RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json) — machine-readable public summary.


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

## Current S11, consolidation and WEB LEGO update — 2026-09-26

The latest private S11 training run `RUN_20260925T163311Z_820718d5` executed **all 210 cases** across the seven actors under the revised continuation policy: **196 PASS, 13 INCONCLUSIVE and 1 FAIL**. The stage remains **INCONCLUSIVE**, while `execution_complete=true`.

Only the **196 verified PASS** cases were admitted to the recorded downstream consolidation. The 14 unresolved cases remained excluded. Transaction `CC_82dd0b3af825cd8543dcd59835023a5a` then completed PASS for BODY_FROZEN and the independent DIRECTOR view while preserving the stated identity split.

The private WEB LEGO extension is installed and reports **READY** with **126 LEGO items, 15 templates, 24 stages, 192 cases, 7 actors** and a **SYNTHETIC_ONLY** data policy. No successful WEB01-WEB24 live completion is claimed yet.

WEB01-WEB24 is configured as the **next gated SSI training phase after S40**. The installed hook requires S40 `execution_complete=true`, a committed S40 consolidation and WEB LEGO `READY` before the web-training track may start. The live S40 -> WEB01 transition has not yet occurred.

The learning-mode cross-run prerequisite repair is now validated by live S12 execution. Run `RUN_20260925T223720Z_6e1b1fc8` completed **210/210 cases: 203 PASS, 7 INCONCLUSIVE, 0 FAIL**. Consolidation transaction `CC_db09484eefd9db783742336b69296eb5` is **COMMITTED** and explicitly linked to this S12 training run; seven cases remained excluded.

- [S12 live training + committed consolidation](RESULTS/SSI_V5_S12_LIVE_TRAINING_AND_CONSOLIDATION_20260926.md)
- [S11 / WEB LEGO 2026-09-26 update](RESULTS/SSI_V5_S11_CONSOLIDATION_AND_WEB_LEGO_UPDATE_20260926.md)
- [Machine-readable 2026-09-26 summary](RESULTS/SSI_V5_S11_CONSOLIDATION_AND_WEB_LEGO_PUBLIC_SUMMARY_20260926.json)
- [Preserved previous S11 results](RESULTS/SSI_V5_S11_FULL_RESULTS_20260923.md)

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

