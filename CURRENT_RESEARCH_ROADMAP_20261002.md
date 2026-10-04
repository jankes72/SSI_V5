# SSI V5 — Current Research Roadmap — 2026-10-02

**Role:** canonical current roadmap for the public SSI V5 R&D, evidence and external-validation hub.  
**Project type:** independent / solo R&D programme.  
**Public boundary:** architecture, research protocols, training checkpoints, failures, repair records, benchmark plans, sanitized evidence and claim boundaries are public; proprietary implementation, credentials and reconstructive private runtime internals remain private.

## Longitudinal S40 / WEB comparative study — preregistered 2026-10-04

A separate longitudinal protocol is now preregistered in [LONGITUDINAL_S40_WEB_AND_AFFECT_STUDY_20261004.md](LONGITUDINAL_S40_WEB_AND_AFFECT_STUDY_20261004.md). After evidence-valid completion through S40, BODY_FROZEN and ISKRA1..ISKRA6 are intended to receive frozen pre-WEB snapshots binding their skill, memory/lifecycle, routing and affect-like state baselines. They will then be compared under the same declared WEB curriculum.

The primary comparison is actor-isolated: no cross-agent knowledge promotion during the first measurement phase. A later secondary phase may enable consultation/consolidation to measure transfer. Results will compare learning trajectories, not only final verdicts.

The "feelings" terminology is retained only as an informal project label for measurable affect-like state proxies. No claim of biological emotion, subjective experience, sentience or consciousness is made.

## Current position

SSI V5 is being developed as a persistent multi-agent research programme with several separately evidenced tracks. Results from one track are not automatically treated as evidence for another.

Current tracks:

1. core SSI reliability and competence training;
2. CZARA multilingual Human-AI research collaboration;
3. Dynamic Mission V6 full-mission training;
4. WEB engineering training;
5. Mexico robotics / offline-resilience research;
6. external partner-defined benchmark and later replication work;
7. ZERO-LAB / LAB_ARCHITECT laboratory-design research;
8. grant / consortium preparation and external validation packaging.

## Current programme path

### Core SSI reliability

The 2026-09-30 stopped run remains preserved: 1,326 cases with 848 PASS, 470 INCONCLUSIVE and 8 FAIL. The post-repair path now has two separately published runtime transcripts under plan `DUP_01fe5854e782f647a46351d1`.

| Run | Closed cases | PASS | INCONCLUSIVE | FAIL | Final runner status |
|---|---:|---:|---:|---:|---|
| `RUN_DOMAIN_20261002T070948Z_d8652beb` | 7 | 5 | 2 | 0 | DOMAIN_BATCH_COMPLETE |
| `RUN_DOMAIN_20261002T181736Z_f600e74c` | 7 | 4 | 3 | 0 | STOPPED_INFRASTRUCTURE |

The latest log reports `NO_CANDIDATE_GENERATED` and `INVALID_WORKER_JSON` on the final candidate. It does not establish whether the cause is model output, parsing, transport or another dependency. No live installation repair or restart was performed as part of this publication.

Across these two distinct case sets there are 14 closed outcomes: 9 PASS, 5 INCONCLUSIVE and 0 FAIL. The later log confirms a starting queue of 614; subtracting seven closed cases gives 607 at that boundary, derived rather than observed in a later status query. Full queue completion, full-stage acceptance and automatic stage consolidation are not claimed.

The 19/19 IPC R2 offline synthetic tests, 8/8 ZeroLab local pilot and completed CZARA curriculum remain separate measurements. See the [latest stop](RESULTS/SSI_FINAL_RECOVERY_STOP_20261002.md), [earlier batch and pilot](ZERO_LAB_V2_FIRST_RESULTS_20261002.md) and their evidence packs.

### CZARA — first internal training cycle complete

The current [CZARA overview](CZARA_CURRENT_STATUS.md) separates this completed curriculum from the later ZeroLab extension, Director_Czary/BODY 1.0 roles and the pending external benchmark.

`CZARA-RND-1.0.0` completed its first internal cycle.

```text
UNIQUE CURRICULUM STAGES = 160

TRAINING = 120 unique stages
VALIDATION = 24 frozen stages
CHAMPION_BENCHMARK = 16 frozen stages

FINAL CHECKPOINT = 160 / 160 PASS
FINAL QUALIFIED SKILLS = 520 / 520
```

Training was iterative:

```text
TRAINING ATTEMPTS = 497
PASS attempts = 120
INCONCLUSIVE attempts = 377
FAIL attempts = 0

FULL_FLOW = 473
ADAPT = 20
REUSE = 4
learning_applied = true for 497 / 497
```

The 377 INCONCLUSIVE records are intermediate learning/retry attempts. They are preserved rather than rewritten. The final checkpoint records all 120 unique training stages as PASS.

Frozen evaluation:

```text
VALIDATION = 24 / 24 PASS
VALIDATION REUSE = 24 / 24
VALIDATION coverage = 1.0
learning_applied = false

CHAMPION_BENCHMARK = 16 / 16 PASS
CHAMPION REUSE = 16 / 16
CHAMPION coverage = 1.0
learning_applied = false

FROZEN TOTAL = 40 / 40 PASS
AUTHORITY ERRORS = 0
```

This is an internal SSI result. It is not an independent Mexico benchmark, physical robotics validation, safety certification or external replication.

Primary records:

- [CZARA first training cycle — final results](CZARA_FIRST_TRAINING_CYCLE_RESULTS_20261001.md)
- [Machine-readable public summary](evidence/CZARA_FIRST_TRAINING_CYCLE_PUBLIC_SUMMARY_20261001.json)
- [Sanitized run-level evidence index](evidence/CZARA_FIRST_TRAINING_20261001/README.md)
- [Historical S120 checkpoint — 2026-09-30](RESULTS/CZARA_RND_1_0_0_TRAINING_CHECKPOINT_S120_20260930.md)

### Dynamic Mission V6

Dynamic Mission V6 was installed with a CZARA-completion prerequisite.

The prerequisite is now satisfied by the completed first CZARA cycle.

```text
CZARA COMPLETION GATE = SATISFIED

DYNAMIC MISSION V6
TOTAL = 72
TRAINING = 48
FROZEN VALIDATION = 12
BLIND CHAMPION = 12

LIVE DYNAMIC MISSION COMPLETION = NOT YET CLAIMED
```

The historical installation document remains valid for its date. Current documents should no longer describe CZARA completion itself as an open prerequisite.

### WEB engineering

The WEB engineering extension remains gated behind the core SSI continuation path.

Recorded readiness:

```text
status = READY
BLOCKS items = 126
templates = 15
stages = 24
cases = 192
actors = 7
data policy = SYNTHETIC_ONLY
```

Successful live completion of WEB01-WEB24 is not yet claimed.

### ZeroLab V2 — installed runtime and bounded local pilot

The earlier laboratory-design proposal now has a V2 runtime implementation for the separate CZARA and FINAL scopes. Operator output reports 9/9 checked services READY at `SSI_ZERO_LAB_V2_20261002`, followed by 8/8 executor results PASS on the local-data demonstration, with `training_pass=false` and `models_called=0`.

The implemented workflow accepts a lead researcher's experiment request, sends input-completeness checks to the selected BODY, versions the protocol and method separately, records local execution, and permits authorized shadow proposals. Selecting a shadow direction requires professor/operator approval and a new main execution. The full conversational workflow has not been established by the simple pilot.

The broad LAB_ARCHITECT research goal remains wider than V2's local software adapters. No physical adapter is established by this release. Installed procedures are not automatically qualified learned skills.

- [V2 architecture and authority](SYSTEM/ZERO_LAB_V2_ARCHITECTURE_AND_AUTHORITY_20261002.md)
- [V2 first results](ZERO_LAB_V2_FIRST_RESULTS_20261002.md)
- [Historical LAB_ARCHITECT design](CZARA_ZERO_LAB_LAB_ARCHITECT_MODULE_20261001.md)

### Mexico robotics / offline-resilience

The planned external Mexico workflow remains separate from the completed internal CZARA training.

The external path is intended to use the same controlled collaboration chain:

```text
Professor / Experts / Students
-> CZARA
-> Director_Czary
-> BODY_FROZEN_1_0 / ZeroLab
-> evidence
-> shared reviewer interface
```

The planned robotics/offline programme includes drones, humanoids, Mother/cross-domain systems, OFFLINE_DIRECTOR, BLOCKS Navigator / Space, no-network state exchange, optical/acoustic relay in controlled research environments and partner-defined unseen benchmark cases.

External Mexico execution, physical validation and independent replication remain unclaimed.

### External benchmark network

The validation maturity path remains:

```text
INTERNAL TRAINING
-> FROZEN INTERNAL VALIDATION
-> BLIND / HELD-OUT BENCHMARKS
-> PARTNER-DEFINED EXTERNAL R&D SESSION
-> SIMULATION / DIGITAL-TWIN VALIDATION
-> CONTROLLED PHYSICAL PILOTS
-> MULTI-PARTNER INDEPENDENT REPLICATION
```

A result at one level does not establish the next.

## Grant / consortium preparation layer

A dedicated proposal-building package is now published at [GRANT_AND_CONSORTIUM_ENTRY_20261001.md](GRANT_AND_CONSORTIUM_ENTRY_20261001.md) and [GRANT_CONSORTIUM/README.md](GRANT_CONSORTIUM/README.md).

It translates the technical evidence into partner-facing planning for:

- SSI consortium contribution and partner roles;
- background / foreground IP and access boundaries;
- conservative asset-specific TRL planning;
- candidate work packages, deliverables, milestones and KPI families;
- impact, exploitation and dissemination;
- risk, safety, cybersecurity and ethics;
- person-month / budget construction;
- data management and reproducibility.

These documents are planning artefacts. They do not establish a signed consortium, certified TRL, fixed budget, eligibility under a specific call or external validation.

## Current collaboration position

SSI is open to controlled collaboration with research laboratories, robotics groups, industrial R&D teams, Human-AI collaboration researchers, independent benchmark designers, replication/validation partners and Horizon Europe consortium partners where programme rules and roles fit.

Preferred first engagement:

```text
partner defines unseen bounded problem
-> acceptance criteria frozen
-> declared SSI version / target
-> run
-> PASS / FAIL / INCONCLUSIVE preserved
-> evidence retained
-> optional consolidation
-> target-specific re-validation
```

## Current claim boundary

Not currently claimed:

- successful live post-repair core continuation through S40;
- completed Dynamic Mission V6 curriculum;
- completed WEB01-WEB24 live training;
- end-to-end professor chat / CZARA shadow / approved promotion validation;
- automatic global consolidation across CZARA, both Directors, BODY 1.0 and Final actors;
- completed external Mexico benchmark;
- company endorsement or industrial benchmark participation;
- independent external replication;
- physical drone / humanoid / rescue-robot validation;
- safety certification;
- production readiness;
- AGI or consciousness.

## Current references

1. [README.md](README.md)
2. [CURRENT_TRUTH_INDEX.md](CURRENT_TRUTH_INDEX.md)
3. [REVIEWER_INDEX.md](REVIEWER_INDEX.md)
4. [START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md)
5. [CZARA first training cycle — final results](CZARA_FIRST_TRAINING_CYCLE_RESULTS_20261001.md)
6. [CZARA public run-level evidence](evidence/CZARA_FIRST_TRAINING_20261001/README.md)
7. [ZERO-LAB / LAB_ARCHITECT](CZARA_ZERO_LAB_LAB_ARCHITECT_MODULE_20261001.md)
8. [S20-S26 operator stop and LAB repair](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_AND_LAB_REPAIR_20260930.md)
9. [Dynamic Mission V6 installation and gate](DYNAMIC_MISSION_ORCHESTRATOR_V6_INSTALL_AND_GATE_20260930.md)
10. [Mexico pre-benchmark R&D protocol](MEXICO_PREBENCHMARK_RND_PROTOCOL_20260928.md)
11. [Mexico robotics training and external benchmark plan](MEXICO_ROBOTICS_TRAINING_AND_BENCHMARK_PLAN_20260926.md)
12. [Collaboration and partner entry](COLLABORATION_AND_PARTNER_ENTRY.md)
13. [Grant and consortium entry](GRANT_AND_CONSORTIUM_ENTRY_20261001.md)
14. [Grant / consortium package](GRANT_CONSORTIUM/README.md)

---

**Canonical roadmap rule:** this 2026-10-02 file supersedes the 2026-10-01 roadmap as the current programme pointer. Earlier dated roadmaps remain preserved as historical state and provenance.


