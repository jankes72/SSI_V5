# SSI V5 — Current Research Roadmap

**Updated:** `2026-09-12`  
**Role:** `CANONICAL LIVING ROADMAP / CURRENT STATUS + LONG-TERM RESEARCH SEQUENCE`  
**Project:** SSI V5  
**Author / architecture:** Paweł Jankiewicz (`jankes72`)  
**Public boundary:** evidence, protocols, status, sanitized measurements, architectural summaries and claim boundaries; proprietary implementation remains private.

## 1. Status precedence

This file is the current roadmap. For current state, read it together with:

- [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md)
- [`CURRENT_BODY_S3_TRAINING_STATUS_20260910.md`](CURRENT_BODY_S3_TRAINING_STATUS_20260910.md)
- [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md)
- [`S10_CROSS_CONSOLIDATION_PUBLIC_OVERVIEW_20260912.md`](S10_CROSS_CONSOLIDATION_PUBLIC_OVERVIEW_20260912.md)
- [`CENTRAL_CONTROL_AND_REVIEW_INTERFACE_OVERVIEW_20260912.md`](CENTRAL_CONTROL_AND_REVIEW_INTERFACE_OVERVIEW_20260912.md)

Older files remain valuable as historical evidence and predeclarations. A historical statement such as `NOT_YET_EXECUTED` remains evidence of what was true when that document was recorded; it must not be mistaken for current status after a later execution has closed.

The governing rule is:

```text
HISTORICAL PREDECLARATION
!=
CURRENT STATUS

CURRENT STATUS
= latest evidence-backed state

LATER PASS
does not erase
EARLIER FAIL / INCONCLUSIVE / INTERRUPTION / PREDECLARATION
```

## 2. Current established milestones

```text
BODY_FROZEN T0
= preserved immutable historical control / 2026-09-05

6 BODY ISKRA T0 descendants
= NICE / GUARDIAN / JUSTICE / EXPLORER / PRAGMATIST / SKEPTIC
= START_STATE_VALIDATED / group QA 48/48 PASS

TEST 5
= DEVELOPMENT_VALIDATED
= 29/29 acceptance PASS
= 524/524 total regression PASS

7-BODY TECHNICAL READINESS
= CLOSED / 7/7 PASS
= A01-A21 x 7 = 147/147 PASS

DIRECTOR_FROZEN_C0
= CLOSED / validated engineering baseline in declared scope

DIRECTOR TRAIN08A FOUNDATION
= CLOSED / VERIFIED PASS
= 48/48 unique steps PASS
= 16/16 blind validations PASS
= 16 checkpoints
= DIRECTOR_FOUNDATION_S1 CREATED

BODY_FROZEN TRAIN01A FOUNDATION
= CLOSED / VERIFIED PASS
= 48/48 PASS
= 16/16 blind validations determinate PASS
= 16/16 checkpoints
= T0 integrity PASS
= BODY_FROZEN_FOUNDATION_S1 CREATED
= S1 SHA256 ed1331e38909db829859ca377e9858ee42fe5528537cf6c9c6d2a5ecc5e253e9

ROUTER S10 ENGINEERING LINE
= cross-consolidation architecture exists
= scoped local descendant import / reload path exercised
= calibration / regression work in progress
= complete seven-line scientific outcome not yet claimed

CENTRAL CONTROL / REVIEW INFRASTRUCTURE
= private local owner/operator control and public observer boundary documented
= OBSERVE != CONTROL
```

The BODY_FROZEN Foundation closure preserves the earlier `43 PASS / 5 INCONCLUSIVE / 0 FAIL` run, recovery attempts, infrastructure diagnosis and the step-24 evaluator-error lineage. The final PASS is a later evidence-backed closure, not a deletion of earlier outcomes.

## 3. Workstream A — controlled BODY / ISKRA research

### 3.1 Current execution boundary: S3 queue

The currently authorized queue is sequential by BODY line.

```text
01 BODY_FROZEN
   S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 -> STOP

02 ISKRA1 NICE
   T0 -> TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 -> STOP

03 ISKRA2 GUARDIAN
   T0 -> TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 -> STOP

04 ISKRA3 JUSTICE
   T0 -> TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 -> STOP

05 ISKRA4 EXPLORER
   T0 -> TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 -> STOP

06 ISKRA5 PRAGMATIST
   T0 -> TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 -> STOP

07 ISKRA6 SKEPTIC
   T0 -> TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 -> STOP
```

Current queue documents:

- [`BODY_S3_TRAINING_START_HERE_20260910.md`](BODY_S3_TRAINING_START_HERE_20260910.md)
- [`S3_QUEUE_PACKAGE_REGISTRY_20260910.md`](S3_QUEUE_PACKAGE_REGISTRY_20260910.md)
- [`evidence/BODY_FROZEN_TRAIN01A_FINAL_CLOSURE_20260910.md`](evidence/BODY_FROZEN_TRAIN01A_FINAL_CLOSURE_20260910.md)

A BODY-local blocker is preserved and may allow the queue to continue to another BODY under the declared protocol. A global integrity problem requires `GLOBAL_STOP`.

### 3.2 Current S3 stop is not the final experiment-entry gate

A prior prospective extension, recorded before the cross-domain outcomes are known, defines a stricter eventual maturity ladder:

```text
S3
-> TRAIN-D TEEN / INDEPENDENT ADAPTATION
-> S4
-> TRAIN-E PRE-PROFESSIONAL QUALIFICATION
-> S5
-> HELD-OUT MICRONETWORK + V10 MECHANISM TESTS
-> 21 CROSS-DOMAIN EXPERIMENTS
```

Therefore both statements are simultaneously true:

```text
CURRENT AUTHORIZED EXECUTION QUEUE = STOP AT S3
FUTURE EXPERIMENT-ENTRY REQUIREMENT = S5
```

TRAIN-D and TRAIN-E remain future stages. Their detailed curricula/packages/hashes are not yet frozen and no S4/S5 outcome is claimed.

Reference: [`PREEXPERIMENT_TRAINING_S3_S5_EXTENSION_20260909.md`](PREEXPERIMENT_TRAINING_S3_S5_EXTENSION_20260909.md).

## 4. Held-out Micronetwork + Router V10 mechanism tests

Seven Micronetwork + Router V10 mechanism-test packages were predeclared and hash-identified before their results were known.

Current state:

```text
PACKAGES = 7
PREDECLARED = YES
EXECUTED = NO
OUTCOMES = UNKNOWN
```

Before execution, the eventual S5 start state for each BODY must be identified and checked against the frozen experiment contract. If binding the new start state materially changes the earlier frozen input contract, the experiment package must receive a new version/hash rather than silently changing the original precommitment.

The mechanism tests are intended to stress, among other things:

```text
KNOWN -> REUSE
SIMILAR / AMBIGUOUS -> VERIFY / ADAPT
NOVEL -> DEEPER / FULL FLOW
DECEPTIVELY SIMILAR -> FALSE-REUSE PROTECTION
REPEATED FAILURE -> NO BLIND RETRY WITHOUT NEW EVIDENCE
RECOVERY -> ALTERNATIVE ROUTE / COMPOSITION / ESCALATION
PERSISTENCE -> HISTORY SURVIVES RESTART
```

## 5. Phase 1 — 21 cross-domain experiments

After the required training maturity and mechanism-test gates, the predeclared cross-domain program remains:

```text
7 independent BODY lines
x 3 unique domains
= 21 unique experiments

A = DRONES
B = HUMANOID
C = NEW DOMAIN independently selected by that SSI line
```

The core measurements include:

```text
KNOWN / SIMILAR / NOVEL classification
actual runtime-reported V10 route
REUSE / VERIFY-ADAPT / COMPOSE / FULL_FLOW
latency / decision cost
correctness / task outcome
false reuse / false escalation
recovery behavior
competence creation/update
Candidate / Challenger / Champion changes
provenance
model/tool/resource cost where available
```

For a successful first exposure, the later predeclared methodology permits an immediate exact repeat for route/time/reuse measurement. This may produce up to 42 execution runs while the scientific design remains 21 unique experiments.

No drone, humanoid or self-selected-domain PASS is currently claimed.

## 6. Phase 2 — competence consolidation with Router S10

The 21 experiments are not the endpoint.

The planned consolidation stage now has an explicit architectural mechanism: Router S10.

```text
COLLECT VERIFIED COMPETENCE FROM SELECTED BODY LINES
-> LOCAL HERMES MEMORY / IDENTITY SUMMARY
-> SHARED SKILL POOL
-> FAST PRE-SELECTION
-> FUNCTIONAL FAMILY GROUPING
-> DEEP COMPARISON WHERE NEEDED
-> EVIDENCE RANKING
-> CHAMPION / CHALLENGER / SPECIALIST / HOLD
-> CONSOLIDATION PLAN
-> VERSIONED CONSOLIDATED BODY DESCENDANT
-> RELOAD / VERIFICATION
```

Dynamic naming is not treated as proof of functional novelty. Different names may describe equivalent competence; similar names may still represent different functions.

An existing Champion is not permanently protected by historical status. If later combined evidence supports a Challenger more strongly, the role may change while preserving the former Champion and full provenance.

The historical `BODY_FROZEN T0` and other FAIR baselines remain immutable and recoverable. Consolidation must create a new versioned descendant rather than rewriting the controls.

### 6.1 Incremental local Hermes memory

Each BODY line may maintain a local Hermes memory summary for S10. The first pass is intended as a full bootstrap; later passes should consume deltas where possible:

```text
NEW SKILL
NEW EVIDENCE FOR EXISTING CHAMPION
NEW EVIDENCE FOR CHALLENGER
FAILURE / NEGATIVE EVIDENCE
TRANSFER EVIDENCE
IDENTITY CHANGE / CONFLICT
-> mark affected family dirty
-> reevaluate only what changed where possible
```

This is intended to reduce repeated full scans as the competence base grows.

### 6.2 S10 calibration

S10 is being treated as a system that should be empirically calibrated rather than assumed correct under one arbitrary parameter set.

The public methodology allows comparison of conservative, balanced, aggressive and research-oriented profiles using measures such as:

- false merge;
- false split;
- classification quality;
- Champion/Challenger promotion correctness;
- deep-comparison rate;
- processing cost;
- regression after tuning.

The exact implementation, thresholds, features and private representations remain proprietary.

### 6.3 Current scoped engineering evidence

A local engineering validation has exercised a real descendant import/reload path on a limited subset of BODY data, including expected-vs-loaded verification. Local checks have also exercised Challenger promotion behavior and incremental change detection.

This supports the engineering existence of the pipeline. It does **not** establish the final scientific result of seven-line cross-consolidation, calibration or later transfer.

Reference: [`S10_CROSS_CONSOLIDATION_PUBLIC_OVERVIEW_20260912.md`](S10_CROSS_CONSOLIDATION_PUBLIC_OVERVIEW_20260912.md).

## 7. Central control and observability layer

A private local control center is being used as a single owner/operator entry point across the seven BODY lines and S10 workflow.

Its public architectural role includes:

- opening per-BODY local control views;
- training and experiment package supervision;
- live progress and audit status;
- Hermes operator guidance;
- S10 collect / evaluate / descendant workflow;
- access to sanitized reviewer observability.

The public reviewer interface remains intentionally separate and observer-only.

```text
LOCAL OWNER CONTROL != PUBLIC REVIEWER OBSERVER
OBSERVE != CONTROL
```

No executable ROOT-control implementation, private path, credential, internal S10 scoring or private Hermes-memory content is published.

Reference: [`CENTRAL_CONTROL_AND_REVIEW_INTERFACE_OVERVIEW_20260912.md`](CENTRAL_CONTROL_AND_REVIEW_INTERFACE_OVERVIEW_20260912.md).

## 8. Phase 3 — three genuinely new domains

After consolidation and regression validation, the versioned consolidated BODY is intended to independently select three new domains.

The selections must not duplicate:

- drones;
- humanoid;
- any Phase-1 Experiment-C domain;
- cosmetic renamings of previously tested domains.

The three selections are frozen before outcomes are known.

Where practical, compare:

```text
PRE-CONSOLIDATION CONTROL
vs
POST-CONSOLIDATION BODY
```

on final task outcome, time-to-valid-solution, full-flow/reuse/verify rates, false reuse, attempts, recovery, new competence creation, resource cost and provenance retention.

The consolidated system is not preclaimed to outperform the control.

## 9. Phase 4 — transfer-mechanism evolution

A later predeclared stage tests whether transfer experience itself can become reusable competence.

Conceptual sequence:

```text
DRONE CONFIGURATION / GRID A
-> acquire and validate competence

TRANSFER A -> B
-> measure what transfers unchanged
-> adapt only where needed
-> preserve false reuse / failures / recovery
-> record transfer evidence

TRANSFER B -> C
-> reuse both task competence and earlier transfer experience
-> test whether the second transfer improves, remains unchanged or degrades

HUMANOID EXTENSION
-> test whether higher-level transfer structure helps in a substantially different domain
-> do not treat drone-specific skill as universal
```

This is a test of transfer mechanism evolution, not a claim that drone skills directly control a humanoid.

## 10. Workstream B — DIRECTOR -> ROBERT -> Worlds / Agents

The canonical engineering line remains separate from controlled BODY/ISKRA experiments.

Current Director sequence:

```text
DIRECTOR_FROZEN_C0
-> TRAIN08A FOUNDATION = CLOSED / VERIFIED PASS
-> DIRECTOR_FOUNDATION_S1 = CREATED
-> TRAIN08B LEGO + MICRONETWORK + V10 PRACTICUM = NEXT
-> DIRECTOR_TRAINED_START_S2 = NOT YET CLAIMED
```

Later engineering direction:

```text
DIRECTOR_TRAINED_START_S2
-> versioned Director engineering / validation
-> controlled DIRECTOR <-> ROBERT integration
-> ROBERT Eyes / Hands / execution development
-> Worlds / Hermes / Agents integration
-> evidence-based reputation / source comparison
-> practical task domains
```

The Director does not currently control the isolated experimental ISKRA lines. ROBERT remains a continuous engineering/execution line and is not reset when experimental BODY branches are cleaned.

## 11. Longer-term R&D architecture

If the consolidation and transfer hypotheses obtain supporting evidence, a later R&D layer may use the same lifecycle internally and externally:

```text
NEW IDEA / TECHNOLOGY / DOMAIN PROBLEM
-> CANDIDATE
-> SANDBOX / CONTROLLED PROJECT
-> TEST
-> EVIDENCE
-> COMPARE
-> REJECT / CHALLENGER / PROMOTE
-> VERSIONED DESCENDANT
```

Potential external domains include robotics, drones, autonomous systems, industrial automation and other areas selected because they provide useful falsifiable transfer problems.

A technology radar may feed candidate tools/models/techniques into this process, but discovery alone never authorizes insertion into the canonical SSI core.

## 12. External review and independent validation

The long-term evidence ladder should move from internal controlled validation toward stronger external challenge:

```text
INTERNAL PREDECLARED TESTS
-> READ-ONLY REVIEWER OBSERVABILITY
-> EXTERNALLY PROPOSED CHALLENGE PACKAGES
-> INDEPENDENT REPRODUCTION / METHODOLOGY REVIEW
-> DOMAIN-EXPERT ROBOTICS / DRONE VALIDATION
-> PHYSICAL EMBODIED TESTS WHERE SAFE AND RESOURCED
```

External reviewers may define challenge cases and falsification criteria under an agreed frozen contract. They remain observers/challenge providers rather than remote ROOT operators.

S10 adds further externally reviewable questions around functional identity, consolidation safety, evidence-gated promotion, calibration and reproducibility of descendants without requiring publication of proprietary implementation.

## 13. Collaboration and funding route

SSI V5 is open to controlled collaboration where a partner can add domain expertise, legal consortium eligibility, laboratory/simulation infrastructure, independent evaluation or physical validation.

Possible participation modes, where the relevant programme permits them, include:

```text
RESEARCH / TECHNOLOGY COLLABORATOR
CONSORTIUM PARTNER / BENEFICIARY THROUGH AN ELIGIBLE LEGAL ENTITY
ASSOCIATED PARTNER
SUBCONTRACTOR / TECHNOLOGY PROVIDER
EXTERNAL CHALLENGE / VALIDATION PARTNER
```

No role is preclaimed for a specific funding call. Eligibility, IP, liability, budget and consortium status must be agreed for each programme/project.

See [`COLLABORATION_AND_PARTNER_ENTRY.md`](COLLABORATION_AND_PARTNER_ENTRY.md) and [`FUNDING_STRATEGY_AND_INDEPENDENT_ROADMAP.md`](FUNDING_STRATEGY_AND_INDEPENDENT_ROADMAP.md).

## 14. Planned economic reinvestment model

The long-term independent-development policy remains a plan, not a revenue forecast:

```text
50% -> author / execution income
40% -> operational / investment capital
10% -> direct SSI infrastructure development
```

The infrastructure share may support compute, storage, models/APIs, networking, backup and laboratory hardware. A positive economic outcome is not guaranteed.

## 15. Current claim boundary

SSI V5 does **not** currently claim that:

- all seven BODY/ISKRA lines have reached S1, S2, S3, S4 or S5;
- BODY_FROZEN has reached S2/S3;
- any ISKRA has completed TRAIN-A/B/C;
- TRAIN-D/E have been frozen or executed;
- the seven held-out mechanism tests have passed;
- the 21 unique cross-domain experiments have passed;
- long-run ISKRA divergence has been demonstrated;
- full seven-line scientific S10 cross-consolidation has succeeded;
- S10 calibration is complete unless later evidence explicitly closes it;
- the three post-consolidation domains have been selected or passed;
- drone A -> B -> C transfer improvement has been demonstrated;
- higher-level humanoid transfer has been demonstrated;
- physical drone or humanoid deployment has been validated;
- Director TRAIN08B has passed or Director S2 exists;
- Director -> ROBERT -> Worlds -> Agents integration is complete;
- Router V10 or Router S10 is universally superior to unrelated systems;
- a hash proves scientific correctness;
- Kiro, Kilo, Codex or another execution tool is an independent scientific auditor;
- AGI, consciousness, universal transfer or production readiness has been established.

## 16. Canonical long-term sequence

```text
TEST 5 + T0 + 7-BODY READINESS
-> BODY_FROZEN FOUNDATION_S1 [CURRENTLY ACHIEVED]
-> SEQUENTIAL 7-BODY TRAINING TO S3 [CURRENT AUTHORIZED QUEUE]
-> PREDECLARE + EXECUTE TRAIN-D/E TO S5 [FUTURE]
-> 7 HELD-OUT MICRONETWORK + V10 MECHANISM TESTS
-> 21 UNIQUE CROSS-DOMAIN EXPERIMENTS
-> COMPETENCE INVENTORY / ROUTER S10 CROSS-CONSOLIDATION
-> VERSIONED CONSOLIDATED BODY DESCENDANT
-> 3 GENUINELY NEW SELF-SELECTED DOMAINS
-> DRONE CONFIGURATION TRANSFER A -> B -> C
-> HUMANOID HIGHER-LEVEL TRANSFER CHALLENGE
-> EXTERNAL FALSIFICATION / INDEPENDENT REPLICATION
-> CONTROLLED R&D TRANSFER INTO ROBERT / DIRECTOR AND EXTERNAL PROJECTS
```

Parallel engineering line:

```text
DIRECTOR_FROZEN_C0
-> TRAIN08A PASS
-> DIRECTOR_FOUNDATION_S1 [CURRENT]
-> TRAIN08B
-> DIRECTOR S2
-> DIRECTOR <-> ROBERT
-> Eyes / Hands / Worlds / Hermes / Agents
-> practical work + evidence + versioned improvement
```

The roadmap may evolve, but every material change should be recorded before the affected outcome is known and should preserve the older version as provenance.