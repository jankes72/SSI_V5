# SSI V5 — Collaboration and Partner Entry

**Updated:** `2026-10-02`  
**Preserved cross-domain evidence:** `2026-09-18`; latest ZeroLab / selected recovery update: `2026-10-02`  
**Status:** `OPEN TO CONTROLLED RESEARCH / TECHNOLOGY / CONSORTIUM COLLABORATION`  
**Public boundary:** proprietary implementation remains private unless separately licensed or explicitly disclosed.

> Grant and technical reviewers should start with [GRANT_AND_CONSORTIUM_ENTRY_20261001.md](GRANT_AND_CONSORTIUM_ENTRY_20261001.md), [GRANT_CONSORTIUM/README.md](GRANT_CONSORTIUM/README.md), [CURRENT_RESEARCH_ROADMAP_20261002.md](CURRENT_RESEARCH_ROADMAP_20261002.md) and [REVIEWER_INDEX.md](REVIEWER_INDEX.md).

## Grant / consortium package — 2026-10-01

The repository now includes a proposal-building layer covering contribution scope, IP, provisional TRL progression, candidate WPs/deliverables/milestones, impact/exploitation, risk/safety/security/ethics, budget/resource planning and data/reproducibility.

This package is designed so that a prospective partner can answer two separate questions quickly:

1. **What can SSI contribute now?**
2. **What must still be supplied or validated by a consortium?**

It does not label contacted organizations as partners and does not claim a grant award, fixed consortium, certified TRL or physical validation.

## External validation path

SSI's preferred collaboration sequence is deliberately staged:

```text
partner-defined bounded R&D problem
-> acceptance criteria frozen before the session
-> CZARA / DIRECTOR session benchmark without production write access
-> PASS / FAIL / INCONCLUSIVE preserved
-> optional simulation / digital-twin phase
-> optional controlled physical pilot
-> independent replication where feasible
```

A company, laboratory or university is not described as a partner or validator until it explicitly agrees to participate. Outreach alone is not treated as collaboration evidence.

## Latest SSI Final continuation — infrastructure stop — 2026-10-02

The next operator-provided log records **4 PASS / 3 INCONCLUSIVE / 0 FAIL** across seven closed cases, ending with `STOPPED_INFRASTRUCTURE` in `RUN_DOMAIN_20261002T181736Z_f600e74c`. The last case first reported a LAB output mismatch, then `NO_CANDIDATE_GENERATED` / `INVALID_WORKER_JSON`; the runner preserved INCONCLUSIVE and stopped. The terminal log does not establish the underlying root cause.

Together with the earlier seven-case batch, the two published transcripts contain **14 distinct actor/case outcomes: 9 PASS / 5 INCONCLUSIVE / 0 FAIL**. This is not a whole-stage or whole-queue result, and it does not alter the separate ZeroLab pilot or CZARA curriculum totals.

- [Latest stop, all seven cases and evidence](RESULTS/SSI_FINAL_RECOVERY_STOP_20261002.md)

## ZeroLab and earlier bounded evidence — 2026-10-02

ZeroLab V2 reports 9/9 checked services READY and an 8/8 local-data pilot PASS, including BODY_FROZEN_1_0. A separate Final recovery batch completed with 5 PASS, 2 INCONCLUSIVE and 0 FAIL. The pilot uses no models and is not training qualification; the live batch's total paid usage is not established by its transcript.

For a partner session, the professor brings the question and criteria to Director_Czary; BODY_FROZEN_1_0 checks inputs and executes a supported laboratory method. Czara preserves translated context and may develop authorized shadow alternatives. The professor/operator decides whether to change the main direction, followed by a new execution. The complete conversational workflow still needs an end-to-end test.

- [CZARA current status and roles](CZARA_CURRENT_STATUS.md)
- [ZeroLab first results](ZERO_LAB_V2_FIRST_RESULTS_20261002.md)
- [Public evidence and provenance](evidence/ZERO_LAB_V2_20261002/README.md)

## Preserved reliability / training boundary — 2026-09-30

Core training progressed through completed S20-S25 stages and into S26, then was **manually stopped by the operator** after abnormal growth of `INCONCLUSIVE` and pending cases.

The current public incident record preserves **1,326 verdicts: 848 PASS, 470 INCONCLUSIVE and 8 FAIL**. These values are not presented as a universal capability score.

A targeted sample of 18 apparent JSON failures traced the symptom to empty responses after `INFLIGHT_LIMIT`; reviewer-input propagation defects were also identified. A repair package passed 17/17 offline tests, with a live restart unclaimed at that date. The separate seven-case result above is the later retest; it does not certify full S20-S40 completion.

This is relevant to external partners because SSI's collaboration model requires the measurement pipeline to be trustworthy before an official frozen benchmark is accepted.

- [S20-S26 operator stop and LAB repair incident](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_AND_LAB_REPAIR_20260930.md)
- [Machine-readable stop/repair summary](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_PUBLIC_SUMMARY_20260930.json)
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
- [CZARA current status and ZeroLab](CZARA_CURRENT_STATUS.md)

## What SSI can offer a partner now

SSI V5 can already be evaluated through a bounded evidence contract without requiring a partner to accept broad claims about the system.

Current verified software evidence includes:

```text
V4 S1-S10 = COMPLETE / PASS
7 BODY final state = 7/7 PASS
BODY_FROZEN promoted reload = 144/144

POST-S10 DRONE = 6/6 software scenarios PASS
POST-S10 HUMANOID = 15/15 software scenarios PASS

DUAL MOTHER CROSS LAB V1
DRONE MOTHER = 12/12 paired scenario families PASS
RESCUE ROBOT MOTHER = 12/12 paired scenario families PASS
60 deterministic repeats per scenario family
720 paired missions / 1,440 domain result rows

CROSS CONSULTATION = 720 measured rounds
CROSS CONSOLIDATION = 360 measured executions
ROLLBACK = 360 measured executions
```

These are software-laboratory results. Physical validation and independent external replication are not claimed.

## Permanent controlled-experiment laboratory — 2026-09-22

The private installation now includes registered protocols, bounded comparison
execution, retained reports and expert review/stop controls. The release passed
165 offline software tests. The owner can issue private observer or expert
access; this does not grant ROOT or remote experiment-launch authority. The
public research portal remains observer-only.

The [component overview](SYSTEM/LEGO_POCKET_META_LEGO_AND_DIRECTOR_LABS_20260922.md) describes the capability and limits. A real
external expert session, independent replication and physical vehicle integration
are not established by the offline tests. The [latest runtime excerpt](RESULTS/SSI_V5_LAB_AND_S11_CONTINUATION_20260922.md)
records three additional BODY_FROZEN training case passes, not full curriculum
closure. The [Football World](RESULTS/FOOTBALL_WORLD_IMPLEMENTATION_BOUNDARY_20260922.md) retains its own pending data-path checks.


## Planned Mexico robotics collaboration track — 2026-09-26

A dedicated future collaboration workflow is now documented for staged robotics training followed by external benchmark work with a research professor/team in Mexico.

The design separates:

```text
CZARA = multilingual research context / translation
DIRECTOR = planning / curriculum / revision control
BODY_FROZEN = technical execution
LAB = verification
EVIDENCE = claim boundary
```

The external portal is intentionally narrow: the partner may submit files, request evidence, propose benchmark modifications, request reruns and inspect shared sanitized results. It is not intended to expose ROOT, the owner filesystem, private DIRECTOR/BODY chats, credentials or arbitrary runtime control.

The planned curriculum contains 48 stages across drones, humanoids, cross-domain/Mother systems and Offline Director / BLOCKS_OFFLINE, followed by validation and final capstone scenarios. The final independent benchmark is intended to use a previously unseen partner-defined problem with criteria frozen before the run.

See:
- [CZARA — Mexico Research Context, Translation and Learning Layer](SYSTEM/CZARA_MEXICO_RESEARCH_LAYER_20260926.md)
- [Mexico Robotics Training and External Benchmark Plan](MEXICO_ROBOTICS_TRAINING_AND_BENCHMARK_PLAN_20260926.md)

The external Mexico collaboration and benchmark remain **planned**. CZARA's first internal cycle is now complete: final checkpoint 160/160 PASS, 520/520 skills QUALIFIED, frozen validation 24/24 PASS and frozen Champion Benchmark 16/16 PASS, all 40 frozen evaluations using REUSE with `learning_applied=false`. External Mexico execution, physical validation and independent replication remain unclaimed.

## Relevant collaboration areas

```text
AGENTIC AI
MULTI-AGENT SYSTEMS
CONTINUAL / LIFELONG LEARNING
PERSISTENT COMPETENCE AND MEMORY
ADAPTIVE ROUTING
CROSS-AGENT CONSOLIDATION
FAILURE-AWARE RECOVERY / ROLLBACK
CROSS-DOMAIN CONSULTATION
AUTONOMOUS SYSTEMS
DRONES / MULTI-ROBOT SYSTEMS
SPECIALIST RESCUE ROBOTICS
HUMANOID MOTION / STABILITY
AUDITABLE AGENT WORKFLOWS
EXTERNAL FALSIFICATION / REPLICATION
```

## Preferred external challenge model

```text
EXTERNAL PARTNER DEFINES A PREVIOUSLY UNSEEN PROBLEM
-> SAFETY / FORMAT REVIEW
-> ACCEPTANCE CRITERIA FROZEN
-> SSI VERSION / TARGET DECLARED
-> RUN
-> PASS / FAIL / INCONCLUSIVE PRESERVED
-> FAILURES / TIMINGS / EVIDENCE RETAINED
-> OPTIONAL CONSOLIDATION
-> TARGET-SPECIFIC RE-VALIDATION
-> RESULT RETURNED TO PARTNER
```

## Possible partner roles

- research collaborator;
- consortium partner / beneficiary where programme rules permit;
- external challenge designer;
- independent replication / validation partner;
- continual-learning or multi-agent methods reviewer;
- drone/swarm research laboratory;
- specialist rescue-robotics laboratory;
- humanoid/robotics research laboratory;
- later physical validation partner.

## What a partner does not need to trust

A partner does not need to rely on a marketing claim about SSI.

The preferred evaluation model is:

- partner supplies an unseen problem or benchmark;
- success/failure criteria are frozen before execution;
- SSI runs under a declared version/configuration;
- PASS / FAIL / INCONCLUSIVE is retained;
- failures are preserved;
- before/after consolidation states may be compared;
- provenance and version identity are retained;
- disclosure occurs only by agreement.

## Reviewer / control boundary

```text
LOCAL CENTRAL CONTROL
= private owner/operator authority
= training / experiment supervision
= promotion / rollback / recovery

PUBLIC REVIEWER INTERFACE
= observer-only
= sanitized state and evidence
= no ROOT authority
= no arbitrary mission execution
= no runtime configuration writes
```

Principle:

```text
OBSERVE != CONTROL
```

## IP and disclosure boundary

```text
PUBLIC / REVIEWABLE
= architecture at safe level
+ protocols
+ sanitized measurements
+ failures / repairs / retests
+ provenance
+ domain-transfer evidence
+ reviewer-interface boundaries
+ claim boundaries

PRIVATE
= proprietary SSI source
+ Router V10 / S10 internals
+ exact scoring / thresholds / private feature construction
+ Micronetwork internals
+ private Hermes memory
+ ROOT implementation
+ prompts / private configuration
+ credentials / endpoints
```

## Claim boundary

Current evidence does **not** establish:

- physical drone validation or certification;
- physical rescue-robot validation;
- physical humanoid validation;
- safety certification;
- independent external replication;
- universal superiority of SSI, V10 or S10;
- production readiness;
- AGI or consciousness.

## Start review here

1. [REVIEWER_INDEX.md](REVIEWER_INDEX.md)
2. [CURRENT_TRUTH_INDEX.md](CURRENT_TRUTH_INDEX.md)
3. [START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md)
4. [RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md)
5. [SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md](SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md)

Older dated collaboration/status documents remain historical records.

