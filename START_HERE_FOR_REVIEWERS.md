# SSI V5 — Start Here for Grant and Technical Reviewers

**Updated:** `2026-09-12`  
**Repository role:** `PUBLIC EVIDENCE / REVIEW MIRROR`  
**Proprietary implementation:** private by design

## Current status in one view

```text
TEST 5 = 29/29 acceptance PASS / 524/524 total regression PASS
7-BODY READINESS = CLOSED / 7/7 PASS / 147/147 common matrix
DIRECTOR TRAIN08A = CLOSED / VERIFIED PASS / 48/48 / 16/16 blind validations
DIRECTOR_FOUNDATION_S1 = CREATED
BODY_FROZEN TRAIN01A = CLOSED / VERIFIED PASS / 48/48 / 16/16 blind validations
BODY_FROZEN_FOUNDATION_S1 = CREATED
6 ISKRA T0 LINES = START_STATE_VALIDATED / group QA 48/48
CURRENT BODY QUEUE = sequential training to S3
FUTURE EXPERIMENT-ENTRY MATURITY = S5
7 mechanism tests = PREDECLARED / NOT YET EXECUTED
21 cross-domain experiments = PREDECLARED / OUTCOMES UNKNOWN
ROUTER S10 = cross-consolidation engineering line exists / scoped local descendant import-reload path exercised
CENTRAL CONTROL = private owner/operator control center + separate public observer boundary
```

## What changed by 2026-09-12

Two additional engineering layers have been added to the public architecture description without publishing proprietary implementation.

### Router S10 — cross-consolidation

Router S10 is a competence-consolidation layer complementary to Router V10.

```text
V10
TASK / STATE -> choose how competence should be used

S10
COMPETENCE FROM MULTIPLE BODY LINES -> identify, compare, rank and consolidate competence
```

The public S10 workflow is:

```text
LOCAL BODY COMPETENCE
-> LOCAL HERMES MEMORY / IDENTITY SUMMARY
-> SHARED SKILL POOL
-> FAST PRE-SELECTION
-> FAMILY GROUPING
-> DEEP COMPARISON WHERE NEEDED
-> EVIDENCE RANKING
-> CHAMPION / CHALLENGER / SPECIALIST / HOLD
-> CONSOLIDATION PLAN
-> VERSIONED DESCENDANT
-> RELOAD / VERIFICATION
```

A scoped local engineering run has exercised a real descendant import/reload path on a limited subset and expected-vs-loaded verification passed. Local checks also exercised Challenger promotion behavior and incremental change detection. These results are internal engineering evidence, not independent scientific validation and not a claim that the complete seven-line research hypothesis has succeeded.

See [`S10_CROSS_CONSOLIDATION_PUBLIC_OVERVIEW_20260912.md`](S10_CROSS_CONSOLIDATION_PUBLIC_OVERVIEW_20260912.md).

### Central local control and public reviewer interface

SSI V5 now documents a stronger operational boundary:

```text
LOCAL CENTRAL CONTROL
= private owner/operator authority
= per-BODY control entry points
= training / experiment supervision
= Hermes guidance
= S10 workflow

PUBLIC REVIEWER INTERFACE
= observer-only
= sanitized state / evidence
= no ROOT authority
= no arbitrary mission execution
= no runtime configuration writes
```

The core rule remains:

```text
OBSERVE != CONTROL
```

See [`CENTRAL_CONTROL_AND_REVIEW_INTERFACE_OVERVIEW_20260912.md`](CENTRAL_CONTROL_AND_REVIEW_INTERFACE_OVERVIEW_20260912.md).

## BODY_FROZEN Foundation milestone

BODY_FROZEN completed its Foundation training stage:

```text
BODY_FROZEN T0
-> TRAIN01A FOUNDATION
-> 48/48 PASS
-> 16/16 blind validations determinate PASS
-> 16/16 checkpoints
-> T0 integrity PASS
-> BODY_FROZEN_FOUNDATION_S1 CREATED
```

S1 identity:

```text
SHA256 = ed1331e38909db829859ca377e9858ee42fe5528537cf6c9c6d2a5ecc5e253e9
```

The final closure preserves earlier inconclusive outcomes, recovery attempts, infrastructure diagnosis and the step-24 evaluator-error record. The history was not rewritten to look clean after the fact.

Read first:

- [`evidence/BODY_FROZEN_TRAIN01A_FINAL_CLOSURE_20260910.md`](evidence/BODY_FROZEN_TRAIN01A_FINAL_CLOSURE_20260910.md)
- [`CURRENT_BODY_S3_TRAINING_STATUS_20260910.md`](CURRENT_BODY_S3_TRAINING_STATUS_20260910.md)

## Controlled BODY/ISKRA research track

The seven lines are:

```text
BODY_FROZEN
ISKRA1 NICE
ISKRA2 GUARDIAN
ISKRA3 JUSTICE
ISKRA4 EXPLORER
ISKRA5 PRAGMATIST
ISKRA6 SKEPTIC
```

Current authorized queue:

```text
BODY_FROZEN: S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3
then each ISKRA: T0 -> TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3
```

Only BODY_FROZEN S1 is currently claimed in this new training sequence. S2/S3 and the six ISKRA A/B/C outcomes remain unknown.

A prior prospective extension defines the eventual experiment-entry maturity as S5:

```text
S3 -> TRAIN-D -> S4 -> TRAIN-E -> S5
-> 7 held-out Micronetwork + V10 mechanism tests
-> 21 cross-domain experiments
```

TRAIN-D/E are future stages and are not currently frozen or executed.

## Why S10 is relevant to the research programme

The seven BODY lines are intentionally independent before later evidence-gated consolidation. S10 provides an explicit mechanism for testing what happens when competence from independent histories is compared and consolidated without deleting provenance.

Important research questions include:

- whether two differently named skills are functionally equivalent;
- whether similarly named skills are actually different;
- whether a Challenger becomes stronger than an earlier Champion after cross-line evidence is combined;
- whether incremental local Hermes memory can reduce repeated full rescans;
- whether consolidation improves later transfer without increasing false reuse;
- whether versioned descendants preserve reproducibility and rollback.

The scientific result of these questions remains open until the relevant controlled experiments close.

## 21-experiment research programme

```text
7 lines x 3 unique domains = 21 unique experiments
A = DRONES
B = HUMANOID
C = NEW DOMAIN selected independently by each SSI line
```

The research target is not merely task completion. The programme measures, where applicable:

- known/similar/novel state handling;
- runtime-reported route selection;
- reuse vs verify/adapt vs alternative composition vs full flow;
- latency and decision cost;
- false reuse and false escalation;
- recovery after failure;
- competence creation and lifecycle changes;
- provenance and persistence.

No drone, humanoid or cross-domain PASS is currently claimed.

## Post-21 research programme

The later plan was recorded before Phase-1 outcomes are known:

```text
21 experiment evidence sets
-> competence inventory
-> functional identity / S10 cross-consolidation
-> Champion enrichment
-> Challenger enrichment and evidence-gated promotion
-> new Micronetwork only for genuinely new function
-> regression / validation
-> versioned consolidated BODY descendant
-> 3 genuinely new self-selected domains
-> before/after comparison
-> drone configuration transfer A -> B -> C
-> humanoid higher-level transfer challenge
-> external falsification / independent replication
```

The intended question is whether accumulated, provenance-preserving competence improves later transfer without creating false reuse. A positive answer is not assumed.

## Director engineering line

The Director line is separate from the controlled BODY experiments:

```text
DIRECTOR_FROZEN_C0
-> TRAIN08A FOUNDATION = CLOSED / VERIFIED PASS / 48/48
-> DIRECTOR_FOUNDATION_S1 = CREATED
-> TRAIN08B LEGO + MICRONETWORK + V10 PRACTICUM = NEXT
-> DIRECTOR_TRAINED_START_S2 = NOT YET CLAIMED
```

Kiro executed steps 01-17 of TRAIN08A and Kilo steps 18-48 after the Kiro usage-limit interruption. The transition is preserved in evidence. The final result is not represented as a single uninterrupted executor run.

## Why Router V10 is relevant

V10 is defined as a state/history/outcome-aware competence and recovery router:

```text
HIGH CONFIDENCE + VALID HISTORY -> REUSE_TOP1
SIMILAR / AMBIGUOUS -> VERIFY_TOPK / VERIFY-ADAPT
LOW / UNKNOWN / CONFLICT -> FULL_FLOW
REPEATED KNOWN FAILURE -> DO NOT BLINDLY REPEAT
-> alternative / composition / verification / escalation
```

Historical scoped evidence includes `REUSE_TOP1 = 534`, `VERIFY_TOPK = 66`, `fallback = 0`, `known-case correctness = 100/100` and a `57.61 s` vs `126.65 s` comparison. This is not claimed as universal superiority.

See [`V10_PREDICTIVE_ROUTING.md`](V10_PREDICTIVE_ROUTING.md).

## Collaboration and consortium entry

SSI V5 is open to controlled collaboration in agentic AI, multi-agent systems, continual/lifelong learning, adaptive routing, competence consolidation, robotics, humanoids, drones, autonomous systems and trusted/auditable agent workflows.

Depending on programme rules and legal structure, realistic roles may include research/technology collaborator, consortium partner through an eligible legal entity, associated partner, subcontractor/technology provider or external validation/challenge partner.

The public S10 and central-control descriptions are intended to make the project easier to review without exposing proprietary source code. They provide reviewers with additional falsifiable questions around competence identity, cross-agent consolidation, provenance, promotion safety, calibration and descendant verification.

The project does **not** preclaim eligibility or acceptance into any specific funding programme.

See [`COLLABORATION_AND_PARTNER_ENTRY.md`](COLLABORATION_AND_PARTNER_ENTRY.md).

## Reviewer interface and authority boundary

The reviewer-facing interface follows:

```text
OBSERVE != CONTROL
```

It may expose sanitized status, experiment stage, checkpoints, CONTINUUM, route class, failures/recovery, S10 stage/status and reviewer-safe evidence references. It must not expose ROOT, arbitrary code execution, mission creation, runtime configuration writes, private filesystem access, private memory, internal S10 scoring or credentials.

## Public/private boundary

```text
PUBLIC
= protocols
+ evidence
+ package identities / hashes
+ measured outcomes
+ failures / repairs / retests
+ provenance
+ S10 purpose / workflow / sanitized status
+ central-control / reviewer-interface architecture
+ claim boundaries

PRIVATE
= SSI source code
+ Router V10 implementation
+ Router S10 implementation
+ exact S10 scoring / thresholds / private feature construction
+ Micronetwork internals
+ private Hermes memory contents
+ private ISKRA / DIRECTOR / ROBERT implementation
+ executable ROOT-control implementation
+ private prompts / memory / configuration
+ credentials / sensitive endpoints
```

## What reviewers should not infer

SSI V5 does **not** currently claim AGI, consciousness, production readiness, universal transfer, physical drone/humanoid validation, universal V10/S10 superiority, long-run ISKRA divergence, completed S5 training, successful mechanism tests, completed 21 experiments, successful full seven-line scientific S10 cross-consolidation, completed S10 calibration unless later evidence explicitly closes it, or completed Director -> ROBERT -> Worlds -> Agents integration.

## Recommended reading order

1. [`README.md`](README.md)
2. [`CURRENT_RESEARCH_ROADMAP_20260910.md`](CURRENT_RESEARCH_ROADMAP_20260910.md)
3. [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md)
4. [`S10_CROSS_CONSOLIDATION_PUBLIC_OVERVIEW_20260912.md`](S10_CROSS_CONSOLIDATION_PUBLIC_OVERVIEW_20260912.md)
5. [`CENTRAL_CONTROL_AND_REVIEW_INTERFACE_OVERVIEW_20260912.md`](CENTRAL_CONTROL_AND_REVIEW_INTERFACE_OVERVIEW_20260912.md)
6. [`CURRENT_BODY_S3_TRAINING_STATUS_20260910.md`](CURRENT_BODY_S3_TRAINING_STATUS_20260910.md)
7. [`evidence/BODY_FROZEN_TRAIN01A_FINAL_CLOSURE_20260910.md`](evidence/BODY_FROZEN_TRAIN01A_FINAL_CLOSURE_20260910.md)
8. [`DIRECTOR_TRAINING_START_HERE.md`](DIRECTOR_TRAINING_START_HERE.md)
9. [`evidence/DIRECTOR_TRAIN08A_FINAL_CLOSURE_20260909.md`](evidence/DIRECTOR_TRAIN08A_FINAL_CLOSURE_20260909.md)
10. [`7BODY_TECHNICAL_READINESS_START_HERE.md`](7BODY_TECHNICAL_READINESS_START_HERE.md)
11. [`TRAINING_PACKAGES_START_HERE.md`](TRAINING_PACKAGES_START_HERE.md)
12. [`EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md`](EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md)
13. [`POST21_RESEARCH_PHASE_INDEX_20260907.md`](POST21_RESEARCH_PHASE_INDEX_20260907.md)
14. [`COLLABORATION_AND_PARTNER_ENTRY.md`](COLLABORATION_AND_PARTNER_ENTRY.md)

Historical documents remain part of the evidence chain even when later files supersede their status statements.