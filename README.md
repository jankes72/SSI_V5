# SSI V5

**Evidence-first research platform for persistent, adaptive multi-agent AI systems.**

SSI V5 is an independently developed R&D project focused on persistent competence, continual learning, cross-agent consolidation, adaptive routing, rollback/recovery and cross-domain transfer.

> **Repository status:** public evidence and review mirror. Proprietary implementation, credentials, private runtime state and reconstructive internals remain private.

## Start here

| Purpose | Document |
|---|---|
| First technical review | **[REVIEWER_INDEX.md](REVIEWER_INDEX.md)** |
| Current verified claims | **[CURRENT_TRUTH_INDEX.md](CURRENT_TRUTH_INDEX.md)** |
| Reviewer orientation | **[START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md)** |
| Collaboration and external challenges | **[COLLABORATION_AND_PARTNER_ENTRY.md](COLLABORATION_AND_PARTNER_ENTRY.md)** |

## Project at a glance

- **Architecture:** independent DIRECTOR core, BODY_FROZEN and six ISKRA agents with separate runtimes, memory and lifecycle.
- **Research controls:** versioned evidence, provenance, checkpoints, rollback and bounded claims.
- **Capability layers:** Router V10/S10, Micronetworks, LEGO Pocket, Pocket Micro, META-LEGO, laboratories and domain/world layers.
- **Demonstrated scope:** software laboratory results for drone, humanoid and cross-domain rescue scenarios.
- **Current boundary:** software evidence is published; physical validation, safety certification and independent external replication are not claimed.

**Current public state:** 2026-09-26

## Current verified state

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

PUBLIC RESEARCH PORTAL = PUBLISHED
PHYSICAL VALIDATION = not claimed
INDEPENDENT EXTERNAL REPLICATION = not claimed
```

Software-lab timing summaries:

```text
mean cross consultation = 2.4896 ms
mean rollback = 0.1170 ms
mean cross consolidation = 0.0369 ms
mean total software flow = 5.2559 ms
```

These are software execution timings, not physical drone/robot response times.

## Current S11, consolidation and WEB LEGO update — 2026-09-26

The latest private S11 training run `RUN_20260925T163311Z_820718d5` completed all **210/210 cases** under the revised training-continuation policy: **196 PASS, 13 INCONCLUSIVE and 1 FAIL**. The stage remains **INCONCLUSIVE**, but `execution_complete=true`; FAIL/INCONCLUSIVE cases no longer stop the whole training traversal.

Only the **196 verified PASS** cases were exported for downstream consolidation. The remaining **14 cases** stayed excluded as unresolved/retry material. Cross-consolidation transaction `CC_82dd0b3af825cd8543dcd59835023a5a` subsequently completed **PASS** for both BODY_FROZEN and the independent DIRECTOR view, with `identity_transfer=false`, `BODY_FROZEN.identity_changed=false`, `DIRECTOR.body_core_imported=false` and `weights_retrained=false`.

A separate private **WEB LEGO** training extension is now installed and reports `READY`: **126 LEGO items, 15 templates, 24 WEB stages, 192 cases, 7 actors**, with `data_policy=SYNTHETIC_ONLY`. This records installation/readiness only; successful WEB01-WEB24 live training is not yet claimed.

- [2026-09-26 S11 consolidation + WEB LEGO update](RESULTS/SSI_V5_S11_CONSOLIDATION_AND_WEB_LEGO_UPDATE_20260926.md)
- [Machine-readable 2026-09-26 summary](RESULTS/SSI_V5_S11_CONSOLIDATION_AND_WEB_LEGO_PUBLIC_SUMMARY_20260926.json)
- [Preserved previous S11 report: 197 PASS / 12 INCONCLUSIVE / 1 FAIL](RESULTS/SSI_V5_S11_FULL_RESULTS_20260923.md)

A cross-run prerequisite repair has been installed and self-tested so learning-mode stages can recognize earlier execution-complete stages with committed consolidation. A live post-fix S12 run is **not yet evidenced** in this public update.

## ŚWIAT PIŁKI — HIPNOZA

The private SSI V5 installation also contains the **ŚWIAT PIŁKI — HIPNOZA** world/interface layer.

```text
implementation = PRESENT
operator-observed runtime/interface behavior = WORKING
complete end-to-end data connection = NOT YET FULLY VALIDATED
evidence-backed domain validation = PENDING
```

See the [current Football World status](RESULTS/FOOTBALL_WORLD_IMPLEMENTATION_BOUNDARY_20260922.md). It is recorded as implemented, but not yet promoted to `VALIDATED / EVIDENCE-BACKED`. The intended closure sequence remains: micronetworks/routing → full data flow → BODY validation → cross-BODY consolidation into BODY_FROZEN → corresponding validated consolidation into the independent DIRECTOR view.

BODY_FROZEN and DIRECTOR remain separate cores with separate runtime, memory and lifecycle.

## Architecture at a glance

```text
DIRECTOR
+ BODY_FROZEN
+ ISKRA1..ISKRA6
+ HERMES
+ CONTINUUM
+ ROUTER V10
+ ROUTER S10
+ TECHNOLOGY RADAR
+ MICRONETWORKS / LEGO / POCKET / POCKET MICRO / META-LEGO
+ COST/QUALITY MODEL CASCADE
+ CONTRACT BINDING
+ WORLD / DOMAIN LAYERS
+ ŚWIAT PIŁKI — HIPNOZA
+ LOCAL ROOT CONTROL
+ PUBLIC OBSERVER INTERFACE
+ EVIDENCE / CHECKPOINT / PROVENANCE
```

## Read this repository in this order

1. [REVIEWER_INDEX.md](REVIEWER_INDEX.md)
2. [Complete previous S11 results and follow-up release](RESULTS/SSI_V5_S11_FULL_RESULTS_20260923.md)
3. [LEGO Pocket, META-LEGO, laboratories and Football World](SYSTEM/LEGO_POCKET_META_LEGO_AND_DIRECTOR_LABS_20260922.md)
4. [CURRENT_TRUTH_INDEX.md](CURRENT_TRUTH_INDEX.md)
5. [START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md)
6. [RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md)
7. [SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md](SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md)
8. [COLLABORATION_AND_PARTNER_ENTRY.md](COLLABORATION_AND_PARTNER_ENTRY.md)

## Current milestone lineage

```text
BODY / ISKRA foundations
-> 7-BODY readiness
-> V4 S1-S10
-> promotion / regression
-> post-S10 drone + humanoid software labs
-> Dual Mother cross-domain consultation / rollback / consolidation
-> free-only / full-flow baseline
-> paid cost/quality model cascade
-> Technology Radar
-> Contract Binding
-> Pocket Micro
-> META-LEGO
-> ŚWIAT PIŁKI — HIPNOZA implemented / operator-observed
-> S11 smoke PASS
-> preserved earlier S11 stops and repairs
-> permanent R&D / controlled-experiment LAB and independent-case continuation
-> preserved 2026-09-23 S11 traversal: 197 PASS / 12 INCONCLUSIVE / 1 FAIL
-> revised training continuation semantics
-> latest S11 traversal: 210/210 executed; 196 PASS / 13 INCONCLUSIVE / 1 FAIL
-> verified-subset export: 196 admitted / 14 excluded
-> S11 cross consolidation PASS for BODY_FROZEN + independent DIRECTOR
-> cross-run prerequisite repair installed/self-tested; live S12 post-fix run not yet evidenced
-> WEB LEGO extension installed READY: 126 LEGO items / 15 templates / 24 stages / 192 cases / SYNTHETIC_ONLY
```

Older dated files remain preserved as historical evidence. They are not the recommended starting point unless a reviewer is auditing provenance.

## Public / private boundary

```text
PUBLIC
= protocols
+ sanitized evidence
+ results
+ failures / repairs / retests
+ timings
+ hashes / provenance
+ claim boundaries
+ architecture at safe level
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

## Claim boundary

The public evidence supports bounded software-laboratory claims about persistent multi-agent execution, versioned competence, consolidation, rollback/recovery and cross-domain experiments.

It does **not** establish:

- all-PASS S11 acceptance; the latest complete traversal contains 14 unresolved cases;
- S12-S40 completion;
- successful WEB01-WEB24 live training;
- physical drone validation;
- physical rescue-robot validation;
- physical humanoid validation;
- safety certification;
- independent external replication;
- production readiness;
- universal superiority;
- AGI or consciousness.

## Collaboration

SSI V5 is open to controlled research, validation, challenge-design and grant/consortium collaboration.

Preferred model:

```text
EXTERNAL PARTNER DEFINES UNSEEN PROBLEM
-> ACCEPTANCE CRITERIA FROZEN
-> SSI RUN
-> PASS / FAIL / INCONCLUSIVE PRESERVED
-> EVIDENCE RETAINED
-> OPTIONAL CONSOLIDATION
-> TARGET-SPECIFIC RE-VALIDATION
```

See [COLLABORATION_AND_PARTNER_ENTRY.md](COLLABORATION_AND_PARTNER_ENTRY.md).

