# SSI V5 — Reviewer Index

**Current public state:** `2026-09-30`  
**Repository role:** public evidence and review mirror for a private SSI implementation.  
**Audience:** grant reviewers, research collaborators, technical reviewers and validation partners.

This file is the shortest route through the repository. Historical files remain preserved for provenance, but they are not the recommended starting point.

## 5-minute review

1. [Latest public status](LATEST_PUBLIC_STATUS_20260930.md) — separates ongoing core/CZARA training, source-excerpt counts, runtime-reported S19 recovery and the waiting V6 scheduler.
2. [Current grant and technical reviewer summary](GRANT_REVIEWER_CURRENT_STATUS_20260930.md) — demonstrated software scope and remaining evidence.
3. [S20 runtime source excerpt](evidence/S20_20260929/S20_LIVE_EXCERPT_RUN_20260929T212837Z_92e516e1.log) — startup reports hardening PASS + S19 COMMITTED; contains 116 completed cases, not a final stage result.
4. [Dynamic Mission V6](DYNAMIC_MISSION_ORCHESTRATOR_V6_INSTALL_AND_GATE_20260930.md) — installation/self-tests, MAIN/SHADOW rules and 0/72 live missions pending CZARA completion.
5. [Machine-readable latest snapshot](RESULTS/SSI_V5_CURRENT_PUBLIC_STATUS_20260930.json) — source identity, captured counts, track gates and claim boundaries.

## Mexico / CZARA / dynamic experiment review

1. [Parallel core/CZARA integration simulation](MEXICO_PARALLEL_INTEGRATION_SIMULATION_20260929.md) — internal under-load preparation, not external validation.
2. [Mexico pre-benchmark R&D protocol](MEXICO_PREBENCHMARK_RND_PROTOCOL_20260928.md) — collaborative revisions, baseline participants, controlled comparisons and official benchmark separation.
3. [Mexico team interface and CZARA controls](MEXICO_TEAM_INTERFACE_AND_CZARA_CONTROLS_20260928.md).
4. [CZARA architecture](SYSTEM/CZARA_MEXICO_RESEARCH_LAYER_20260926.md).
5. [Planned 48-stage Mexico robotics programme](MEXICO_ROBOTICS_TRAINING_AND_BENCHMARK_PLAN_20260926.md).

The planned 48-stage robotics programme, active 160-item CZARA curriculum and installed 72-mission V6 curriculum are distinct tracks. The public records do not establish Mexico-side execution or independent external validation.

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

## Current training snapshot — 2026-09-30

The operator reports that core SSI training continues alongside CZARA. The public S20 log is a partial capture of `RUN_20260929T212837Z_92e516e1`, not a final stage report.

| Track | Latest published state | Evidence scope |
|---|---|---|
| Core S20-S40 | S20 started; core training reported ongoing | S20 excerpt: 116 unique completed cases, 79 PASS, 37 INCONCLUSIVE, 0 FAIL; full-stage completion not established |
| S19 recovery / pre-S20 hardening | Startup banner reports hardening PASS and S19 COMMITTED | Operator-supplied log; transaction journal and detailed gate reports are not included in this excerpt |
| CZARA Live Training | Running alongside core training | Internal integration snapshot; 160-item curriculum = 120 training + 24 frozen validation + 16 frozen Champion benchmark; final completion not published |
| Dynamic Mission V6 | Installed; scheduler active; waiting for CZARA completion | 0/72 live missions at the recorded snapshot; 48 training + 12 frozen validation + 12 frozen blind Champion |
| WEB01-WEB24 | Installed / READY; gated after S40 | Requires S40 execution completion and COMMITTED consolidation; live completion not published |
| Mexico external benchmark | Planned | Internal simulations do not establish Mexico-side execution or independent validation |

The S20 excerpt covers BODY_FROZEN, ISKRA1, ISKRA2 and part of ISKRA3. It declares seven actors and 210 assignments, but does not include results for the entire stage. All captured verdicts remain visible, including the 37 INCONCLUSIVE rows. The excerpt contains no FAIL rows; the final stage outcome is not established.

V6 adds complete evolving experiments with a simulated professor and four experts, DIRECTOR-managed MAIN/SHADOW branches and explicit formal promotion. Installer self-tests are recorded separately from live mission results. The planned 48-stage Mexico robotics curriculum, the 160-item CZARA curriculum and the 72-mission V6 curriculum are distinct programmes.

Current sources:

- [Latest public status and source map](LATEST_PUBLIC_STATUS_20260930.md)
- [Machine-readable current snapshot](RESULTS/SSI_V5_CURRENT_PUBLIC_STATUS_20260930.json)
- [Supplied S20 runtime log](evidence/S20_20260929/S20_LIVE_EXCERPT_RUN_20260929T212837Z_92e516e1.log)
- [Parallel core/CZARA integration simulation](MEXICO_PARALLEL_INTEGRATION_SIMULATION_20260929.md)
- [V6 installation, self-tests and post-CZARA gate](DYNAMIC_MISSION_ORCHESTRATOR_V6_INSTALL_AND_GATE_20260930.md)

The earlier S19 incident and pre-S20 preregistration remain historical evidence. S20 startup is now recorded; the excerpt does not independently audit all prerequisite gates or the S19 commit.

## Earlier training and hardening records

- [S13-S18 routing and recovery](RESULTS/SSI_V5_S13_S18_ROUTING_AND_RECOVERY_UPDATE_20260929.md) — 1,260 unique cases; 1,197 PASS, 53 INCONCLUSIVE, 10 FAIL; six committed consolidations.
- [S11/S12 quality and efficiency signal](RESULTS/SSI_V5_S11_S12_QUALITY_EFFICIENCY_SIGNAL_20260926.md).
- [S11 consolidation and WEB installation](RESULTS/SSI_V5_S11_CONSOLIDATION_AND_WEB_LEGO_UPDATE_20260926.md).
- [Preserved 23 September S11 results](RESULTS/SSI_V5_S11_FULL_RESULTS_20260923.md) — earlier run, not the later S11 traversal.
- [Historical S19 incident](RESULTS/SSI_V5_S19_OBSERVABILITY_INCIDENT_AND_PRE_S20_STATUS_20260929.md).
- [Pre-S20 hardening preregistration](SYSTEM/SSI_V5_PRE_S20_OBSERVABILITY_AND_EVIDENCE_HARDENING_PREREGISTRATION_20260929.md).
- [Hamid Ahmadian feedback attribution](EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md) — requirements provenance, not endorsement or independent audit.

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

- [Current grant-reviewer summary](GRANT_REVIEWER_CURRENT_STATUS_20260930.md)
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
FOLLOW CURRENT_TRUTH_INDEX.md TO THE LATEST SOURCE-BACKED SNAPSHOT
KEEP THE OLDER FILE AS HISTORICAL EVIDENCE
```

No historical file needs to be deleted to keep the reviewer path concise.

