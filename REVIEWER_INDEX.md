# SSI V5 — Reviewer Index

**Current public state:** `2026-09-23`  
**Repository role:** public evidence and review mirror for a private SSI implementation.  
**Audience:** grant reviewers, research collaborators, technical reviewers and validation partners.

This file is the shortest route through the repository. Historical files remain preserved for provenance, but they are not the recommended starting point.

## 5-minute review

1. [README.md](README.md) — concise project front door and current state.
2. [Complete S11 results](RESULTS/SSI_V5_S11_FULL_RESULTS_20260923.md) — all 210 outcomes, unresolved cases and deferred stages.
3. [LEGO Pocket, META-LEGO and Director-connected laboratories](SYSTEM/LEGO_POCKET_META_LEGO_AND_DIRECTOR_LABS_20260922.md) — component roles and implementation/validation boundaries.
4. [CURRENT_TRUTH_INDEX.md](CURRENT_TRUTH_INDEX.md) — canonical pointer to the latest evidence-backed state.
5. [START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md) — reviewer-oriented project summary.
6. [RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md) — latest measured cross-domain laboratory report.
7. [RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json](RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json) — machine-readable public summary.

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

## Current S11 and laboratory update — 2026-09-23

The previous run `RUN_20260922T221012Z_88df9df1` traversed all **210 S11 cases** across seven BODY: **197 PASS, 12 INCONCLUSIVE and 1 FAIL**. S11 remained **INCONCLUSIVE**, and all **29 S12–S40 stages were DEFERRED_PREREQUISITE**, with zero model calls recorded for them. Every case outcome and the original aggregate metrics are now published.

The follow-up private R3 package adds shared training/R&D diagnostics, no-progress detection, measurement controls and a **6 USD daily budget shared by all seven BODY**. Offline validation completed with **105 tests passed and one skipped**. Delivery is recorded; installation on the operator's machine and a new post-R3 run are not yet confirmed.

The signed evidence verifier detected all five controlled tampering attempts. Separate-UID key custody was not verified end to end here; external timestamping is not configured. The run remains **LOCAL_DEVELOPMENT / external_pilot_ready=false**. The UAV lab supports software experiments; physical adapters and an external Tailscale session are not demonstrated.

- [Complete previous S11 results: 197 PASS / 12 INCONCLUSIVE / 1 FAIL](RESULTS/SSI_V5_S11_FULL_RESULTS_20260923.md)
- [All 210 case outcomes and source hashes](evidence/S11_20260923/README.md)
- [DEV safeguards and adversarial tests](RESULTS/SSI_V5_DEV_SAFEGUARDS_20260923.md)
- [UAV and permanent R&D laboratory status](SYSTEM/SSI_V5_UAV_AND_RND_LABS_20260923.md)
- [R3 offline test summary](RESULTS/SSI_V5_LAB_RND_R3_TEST_SUMMARY_20260923.json)

The public outcome index and aggregate reports cover all 210 cases, but the review received full raw case records for only the 13 unresolved cases. The 197 PASS records require verification on the target machine before reuse. This update does not establish causal effects of feelings, learning or role prompts. Earlier dated reports remain unchanged.


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

