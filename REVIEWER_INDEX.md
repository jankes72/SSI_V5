# SSI V5 — Reviewer Index

**Current public state:** `2026-09-20`  
**Repository role:** public evidence and review mirror for a private SSI implementation.  
**Audience:** grant reviewers, research collaborators, technical reviewers and validation partners.

This file is the shortest route through the repository. Historical files remain preserved for provenance, but they are not the recommended starting point.

## 5-minute review

1. [README.md](README.md) — concise project front door and current state.
2. [RESULTS/SSI_V5_CONTROLLED_EVOLUTION_LIVE_S11_20260920.md](RESULTS/SSI_V5_CONTROLLED_EVOLUTION_LIVE_S11_20260920.md) — terminal S11 record: 22 PASS, then one INCONCLUSIVE gate.
3. [RESULTS/SSI_V5_IMPLEMENTATION_STATUS_20260920.md](RESULTS/SSI_V5_IMPLEMENTATION_STATUS_20260920.md) — implemented V5 scope and explicit validation boundary.
4. [CURRENT_TRUTH_INDEX.md](CURRENT_TRUTH_INDEX.md) — canonical pointer to the latest evidence-backed state.
5. [START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md) — reviewer-oriented project summary.
6. [RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md) — latest measured cross-domain laboratory report.
7. [RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json](RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json) — machine-readable public summary.

## Technical architecture review

1. [SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md](SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md)
2. [VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md](VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md)
3. [RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md](RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md)
4. [FOOTBALL_WORLD_CURRENT_STATUS_20260916.md](FOOTBALL_WORLD_CURRENT_STATUS_20260916.md)

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

## Current V5 implementation status

```text
Technology Radar + extended LEGO Pocket + Pocket Micro + META-LEGO + V5 interface
= IMPLEMENTED / NOT YET VALIDATED END-TO-END

7 BODY-family runtimes = AVAILABLE
independent DIRECTOR = AVAILABLE
S11 smoke after META-LEGO = PASS
FULL S11 BODY_FROZEN = STOPPED_INCONCLUSIVE
result before/at stop = 22 PASS / 0 FAIL / 1 INCONCLUSIVE
stopped at = S11-04-05
native evaluation at stop = PASS
Collective Intelligence at stop = INCONCLUSIVE / PARTIAL
S11 stage PASS = NOT CLAIMED
S12-S40 = NOT YET CLAIMED

ŚWIAT PIŁKI — HIPNOZA
= IMPLEMENTED / OPERATOR-OBSERVED
= FULL DATA-PATH AND DOMAIN EVIDENCE PENDING
```

This work continues the previously documented roadmap and preserved V4 BODY_FROZEN consolidation/promotion and Director-transfer lineage. BODY_FROZEN and DIRECTOR remain independent cores. Repository wording distinguishes `PLANNED / DOCUMENTED`, `IMPLEMENTED / NOT YET VALIDATED` and `VALIDATED / EVIDENCE-BACKED`.

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
