# SSI V5 — DIRECTOR Command Center — Tailscale Cross-Consolidation Architecture — 2026-09-14

**Status:** `PREDECLARED BEFORE MATCHED BODY / ISKRA THREE-VARIANT TRAINING`  
**Interface base:** `DIRECTOR Command Center V1 = IMPLEMENTED / LOCAL VALIDATION PASS`  
**Cross-node live integration:** `PREPARED CONTRACTS / PARTIALLY CONNECTED / FULL BODY-ISKRA LIVE MESH NOT YET CLAIMED`  
**Repository role:** public architecture, chronology, evidence boundary and future integration contract  
**Implementation:** proprietary / private

## 1. Why this document exists

The earlier Command Center gate established that a real, hash-identified Director Command Center implementation exists before the later matched training outcomes.

This document freezes the **detailed organizational and cross-consolidation architecture** before those outcomes are known.

The purpose is to make the later system testable against a prior declaration rather than allowing the interface, cross-node skill flow or consolidation story to be invented after seeing which BODY / ISKRA / S10 line performs best.

The intended rule is:

```text
ARCHITECTURE FIRST
-> INDEPENDENT TRAINING / EXPERIENCE
-> EVIDENCE
-> CROSS-CONSOLIDATION
-> TARGET ADOPTION
-> RE-VALIDATION
-> ORGANIZATIONAL EFFECT
```

not:

```text
SEE THE RESULT FIRST
-> INVENT A CONVENIENT INTEGRATION STORY AFTERWARD
```

## 2. Existing drone-domain precedent

The cross-node SSI design deliberately reuses the research pattern already instantiated in the drone/swarm software laboratory.

The drone branch preserves multiple independent grids with their own local state and experience. A new skill or adaptation can remain local first and only later be considered for wider availability.

The visible drone process is:

```text
LOCAL EXPERIENCE IN GRID A
-> LOCAL RESULT
-> COMPARISON / VALIDATION
-> CONSOLIDATION DECISION
-> COLLECTIVE AVAILABILITY
-> RE-TEST ON OTHER GRIDS
```

The public drone benchmark also demonstrated why consolidation cannot be treated as automatically beneficial:

```text
scoped competence-pool availability
before: 6 / 5 / 5
after:  8 / 8 / 8

scoped comparative median effect
~1.384x speedup
~27.76% lower median flow cost

but:
wind_corridor = PASS -> FAIL regression after consolidation
```

The lesson carried into the organization-wide architecture is therefore:

> **A competence may become more widely available only after evidence-gated comparison, and wider availability must be followed by target-specific re-validation because a consolidation that helps one context can regress another.**

The measured drone numbers above remain scoped drone-demonstrator results. They are not predictions of future organization-wide performance.

## 3. Mapping from drone grids to SSI organizational lines

The organizational system uses the same logic at a higher level.

Conceptual mapping:

```text
DRONE GRID A / B / C
= independent local histories

SSI RESEARCH SOURCES
= BODY_FROZEN 2.0 / controlled descendant where applicable
+ ISKRA1 NICE
+ ISKRA2 GUARDIAN
+ ISKRA3 JUSTICE
+ ISKRA4 EXPLORER
+ ISKRA5 PRAGMATIST
+ ISKRA6 SKEPTIC

CANONICAL / OPERATIONAL TARGETS
= ROBERT
+ DIRECTOR
+ BODY_FROZEN 2.0 when acting as an R&D integration target
```

ROBERT and DIRECTOR are not silently redefined as additional FAIR experimental BODY lines. They are canonical engineering/operational lines with their own histories and integration gates.

## 4. Role separation

The Command Center must make the following responsibilities visually and technically distinct.

### Tailscale

```text
ROLE = PRIVATE NETWORK TRANSPORT
```

Tailscale carries approved snapshots, deltas, evidence references and node health between computers.

Tailscale does **not** decide which competence is a Champion, does not perform S10 scoring and does not become a scientific consolidation mechanism by itself.

### Router S10

```text
ROLE = CROSS-LINE COMPETENCE COMPARISON / CONSOLIDATION DECISION LAYER
```

S10 identifies functional families, compares evidence, preserves alternatives and supports roles such as:

```text
CHAMPION
CHALLENGER
SPECIALIST
HOLD
```

### DIRECTOR

```text
ROLE = ORGANIZATIONAL COORDINATION / LONG-TERM STATE / PRIORITIES / PROJECTS / ORDERS
```

Director observes the system-wide result, tracks organizational consequences, coordinates priorities and records what the organization is doing.

Director must not silently override an evidence-gated S10 result merely because a different result is operationally convenient.

### HERMES

```text
ROLE = KNOWLEDGE / CHANGE NAVIGATOR / OPERATOR EXPLANATION
```

Hermes explains what changed, where it changed, why it matters, what is waiting for validation and which next action is appropriate.

Hermes is not ROOT, not a second Director and not an independent scientific auditor.

### ROBERT

```text
ROLE = CANONICAL CONTINUOUS EXECUTION LINE
```

ROBERT may later receive experimentally validated competence only through explicit integration, regression and acceptance gates.

### BODY_FROZEN 2.0

```text
ROLE = VERSIONED R&D DESCENDANT / EXTERNAL + INTERNAL R&D
```

It may consume validated competence for new R&D work and can itself produce new candidate competence that returns to the evidence lifecycle.

### ISKRA lines

```text
ROLE = INDEPENDENT LONGITUDINAL RESEARCH / EXPERIENCE SOURCES
```

Their independent histories must remain attributable and must not be silently collapsed into one shared memory during controlled comparison.

## 5. Intended physical / network topology

The current deployment is designed around at least two computers connected by the existing private Tailscale network.

```text
COMPUTER A / EXECUTION SIDE

ROBERT
BODY_FROZEN 2.0 when assigned here
ISKRA runtimes when assigned here
LAB outputs
V10 state summaries
S10 source summaries
local competence inventories
local evidence references

              |
              |  TAILSCALE
              |  private transport
              v

COMPUTER B / DIRECTOR SIDE

DIRECTOR runtime
DIRECTOR organizational state
HERMES delta/change layer
DIRECTOR Command Center
projects / orders
technology radar state
capital / finance extension slots
cross-node aggregation view
```

The system is not permanently limited to two physical machines. Additional BODY / ISKRA runtimes may later move to separate hardware while retaining the same node/data contracts.

The architecture is therefore **node-contract based**, not hard-coded to one specific machine count.

## 6. What crosses Tailscale

The intended network boundary is selective.

Approved cross-node information classes include conceptually:

```text
NODE STATUS SNAPSHOT
ACTIVE MISSION / WORKFLOW STATE
BODY / AGENT IDENTITY
CURRENT STAGE
CONTINUUM HEALTH SUMMARY
V10 ROUTING SUMMARY
S10 SOURCE / FAMILY SUMMARY
COMPETENCE DELTA
EVIDENCE REFERENCE / HASH / PROVENANCE
FAILURE / RECOVERY EVENT
ADOPTION RECEIPT
TARGET RE-TEST RESULT
EFFECT MEASUREMENT
HERMES CHANGE EVENT
PROJECT / ORDER STATUS
TECHNOLOGY-RADAR CANDIDATE STATUS
FINANCE SOURCE STATUS WHEN CONNECTED
```

The Command Center does not require unrestricted remote filesystem replication.

The public architecture does not authorize transmission or exposure of:

```text
ROOT AUTHORITY
ARBITRARY SHELL EXECUTION
PRIVATE TOKENS / CREDENTIALS
PRIVATE PROMPTS
UNSANITIZED PRIVATE MEMORY
PROPRIETARY SOURCE CODE
UNBOUNDED REMOTE FILESYSTEM ACCESS
```

## 7. The core isolation rule before cross-consolidation

This rule is critical for the upcoming matched training programme:

```text
OBSERVATION
!=
COMPETENCE TRANSFER
```

During independent BODY / ISKRA training, the Command Center may display status, timing, progress, evidence counts and declared lifecycle state from multiple lines.

It must **not** silently make one line's newly learned competence available to another line before the applicable consolidation gate.

For matched V1 / V3 / V2 comparison, the interface must preserve variant identity and line identity.

Conceptually:

```text
V1 histories remain attributable to V1
V3 histories remain attributable to V3
V2 histories remain attributable to V2

ISKRA1 history remains attributable to ISKRA1
...
ISKRA6 history remains attributable to ISKRA6
```

The Command Center can observe all of them without contaminating them.

## 8. Organization-wide cross-consolidation workflow

Once the declared comparison/consolidation gate is reached, the intended workflow is:

### Stage 0 — local competence remains local

```text
AGENT / BODY / LAB
-> NEW LOCAL EXPERIENCE
-> LOCAL OUTCOME
-> LOCAL COMPETENCE / CANDIDATE
-> LOCAL EVIDENCE
```

No automatic global copy occurs.

### Stage 1 — delta publication

The source exposes a controlled competence delta rather than requiring the entire history to be rescanned every time.

A delta may represent:

```text
NEW COMPETENCE
NEW POSITIVE EVIDENCE
NEW NEGATIVE EVIDENCE
FAILURE SIGNATURE
CHALLENGER UPDATE
CHAMPION UPDATE
TRANSFER RESULT
IDENTITY / FAMILY CONFIDENCE CHANGE
```

### Stage 2 — Tailscale transport to aggregation layer

The approved delta and evidence references are transported through the private Tailscale network to the Director-side aggregation layer / S10 source intake.

Transport success is recorded separately from scientific validity.

```text
DELIVERED
!=
VALIDATED
```

### Stage 3 — incremental Hermes / identity update

Per-line incremental memory identifies what is actually new since the previous consolidation pass.

The intended long-term pattern remains:

```text
FIRST PASS = CONTROLLED BOOTSTRAP
LATER PASSES = DELTA UPDATE + DIRTY-FAMILY REVIEW
```

### Stage 4 — S10 fast pre-selection

S10 reduces the comparison space using identity/family information.

Clearly unrelated functions should not require expensive all-to-all deep comparison.

### Stage 5 — family / similarity grouping

Functionally related competence from different histories is grouped into candidate families.

Names alone are insufficient:

```text
DIFFERENT NAME MAY MEAN SAME FUNCTION
SAME/SIMILAR NAME MAY MEAN DIFFERENT FUNCTION
```

### Stage 6 — deep comparison where needed

Ambiguous families, potential merges, conflicts, possible promotions and uncertain identity cases receive deeper analysis.

### Stage 7 — evidence ranking and lifecycle decision

Evidence may support:

```text
KEEP CURRENT CHAMPION
PROMOTE CHALLENGER
KEEP SPECIALIST
HOLD / DO NOT MERGE
CREATE NEW FUNCTIONAL FAMILY
REQUIRE MORE EVIDENCE
```

A historical Champion is not permanently protected from stronger later evidence.

### Stage 8 — consolidation plan, not direct silent overwrite

The output is a versioned plan describing:

```text
SOURCE COMPETENCE
SOURCE LINE
EVIDENCE / PROVENANCE
TARGET FAMILY
DECISION
INTENDED TARGETS
REQUIRED RETESTS
ROLLBACK / REJECTION CONDITION
```

### Stage 9 — controlled target availability

Only after the applicable gate may the competence become available to selected targets such as:

```text
ROBERT
BODY_FROZEN 2.0
DIRECTOR
```

Availability must be target-specific. A competence useful to ROBERT is not automatically assumed useful to DIRECTOR or BODY_FROZEN 2.0.

### Stage 10 — target-specific re-test / regression gate

Each target performs its applicable acceptance/regression checks.

The drone `wind_corridor` regression is the explicit design warning:

```text
CONSOLIDATED / SHARED
!=
AUTOMATICALLY BETTER
```

Possible target outcomes include:

```text
ACCEPT
ACCEPT AS SPECIALIST
KEEP AS CHALLENGER
HOLD
REJECT
ROLL BACK TARGET ADOPTION
```

The source competence and original evidence remain preserved regardless of target rejection.

### Stage 11 — effect measurement

After accepted adoption, the system records whether anything actually changed.

Possible effect classes include:

```text
SUCCESS RATE
FAILURE RATE
LATENCY
FLOW DEPTH
MODEL / TOKEN / API COST
RECOVERY QUALITY
FALSE REUSE
REGRESSION
RESOURCE USE
PROJECT OUTCOME
ECONOMIC EFFECT WHEN A REAL FINANCIAL SOURCE EXISTS
```

No positive effect is assumed in advance.

### Stage 12 — Hermes change report

Hermes converts raw cross-node deltas into an operator-facing summary such as:

```text
ISKRA4 created competence X
S10 grouped X with family Y
X was promoted to Challenger
ROBERT accepted X after regression
BODY_FROZEN 2.0 still holds X for additional testing
DIRECTOR knows the result but did not activate X operationally
one negative effect was detected in scenario Z
```

### Stage 13 — Director organizational update

Director updates the organization-level picture:

```text
WHAT DO WE NOW KNOW?
WHAT IS STILL UNCERTAIN?
WHICH PROJECT BENEFITS?
WHICH RISK INCREASED?
WHICH TASK SHOULD BE CREATED?
DO WE NEED NEW R&D?
DO WE NEED A NEW EXTERNAL CHALLENGE?
```

This is organizational reasoning after evidence, not a replacement for the evidence gate.

## 9. Command Center — professional interactive information architecture

The Command Center is intended to expose the above system as an operator-grade control center rather than a raw process monitor.

### 9.1 COMMAND

Primary organizational view:

```text
CURRENT DIRECTOR OBJECTIVE
CURRENT PRIORITIES
ACTIVE WORLD / DOMAIN
ACTIVE PROJECT / ORDER
DECISIONS WAITING FOR EVIDENCE
BLOCKED ITEMS
NEW DIRECTOR ASSIGNMENTS
SYSTEM-WIDE WARNINGS
```

### 9.2 ORGANIZATION

Interactive organization map containing:

```text
DIRECTOR
ROBERT
BODY_FROZEN 2.0
ISKRA1 NICE
ISKRA2 GUARDIAN
ISKRA3 JUSTICE
ISKRA4 EXPLORER
ISKRA5 PRAGMATIST
ISKRA6 SKEPTIC
```

Each entity should expose at least:

```text
ONLINE / OFFLINE / NOT_CONFIGURED
current activity
current domain / mission
training / experiment stage
latest evidence change
local competence change
last accepted / rejected transfer
warnings
last update / latency
```

### 9.3 AGENT / BODY DETAIL

Selecting an ISKRA or BODY line should expose a life/history view rather than only a runtime heartbeat:

```text
CURRENT OBJECTIVE
CURRENT ACTIVITY
HERMES GENERATION / KNOWLEDGE SOURCE
LOCAL EXPERIENCE SUMMARY
CANDIDATES
CHALLENGERS
CHAMPIONS
SPECIALISTS
RECENT DECISIONS
FAILURES / RECOVERIES
TRUST / SOURCE RELATIONSHIPS WHERE DECLARED
EVIDENCE TIMELINE
CROSS-CONSOLIDATION STATUS
TRANSFER / ADOPTION HISTORY
```

The UI must distinguish local competence from collectively available competence.

### 9.4 CROSS-CONSOLIDATION LIVE

A dedicated view should visualize the active consolidation path:

```text
SOURCE LINE
-> DELTA
-> FAMILY
-> FAST PATH / DEEP PATH
-> EVIDENCE COMPARISON
-> ROLE DECISION
-> TARGET PLAN
-> TARGET RETEST
-> ACCEPT / HOLD / REJECT
-> EFFECT
```

The operator should be able to answer:

- where a competence originated;
- which other lines had functionally related competence;
- whether S10 used a fast or deeper comparison path;
- why a Champion/Challenger/Specialist/Hold role was selected at a public-safe level;
- which targets received an integration proposal;
- which targets accepted or rejected it;
- whether target behavior improved, stayed neutral or regressed.

### 9.5 SKILL / COMPETENCE FLOW

Prepared views include:

```text
NEW LOCAL
AWAITING COMPARISON
FAMILY IDENTIFIED
CANDIDATE
CHALLENGER
CHAMPION
SPECIALIST
HOLD
PROPOSED FOR ROBERT
PROPOSED FOR BODY_FROZEN 2.0
PROPOSED FOR DIRECTOR
ACCEPTED
REJECTED / REGRESSION
```

### 9.6 HERMES — WHAT CHANGED

Hermes should prioritize deltas, not repeat the whole system description on every refresh.

The primary operator question is:

> **What changed since I last looked?**

Change classes include:

```text
NODE CHANGE
MISSION CHANGE
COMPETENCE CHANGE
S10 ROLE CHANGE
EVIDENCE CHANGE
FAILURE / RECOVERY
TARGET ADOPTION / REJECTION
PROJECT / ORDER CHANGE
RADAR CANDIDATE CHANGE
FINANCE SOURCE CHANGE
CAPITAL / RESULT CHANGE WHEN CONNECTED
```

### 9.7 WORLDS

The panel reserves world/domain views such as:

```text
FOOTBALL / HISTORICAL ORIGIN WORLD
DRONES
HUMANOID
MARKETS / EMERGING DATA WORLD
FUTURE WORLDS
```

Each world should connect agents, competence, evidence, projects and verified outcomes rather than exist as a decorative label.

### 9.8 R&D / BODY_FROZEN 2.0

Prepared R&D flow:

```text
PROBLEM
-> EXISTING VERIFIED COMPETENCE
-> MISSING COMPETENCE
-> CANDIDATE SOLUTION
-> SANDBOX / LAB
-> TEST
-> EVIDENCE
-> REJECT / CHALLENGER / PROMOTE
-> VERSIONED DESCENDANT
```

The same gate applies to R&D changes proposed for SSI itself.

### 9.9 PROJECTS / ORDERS

Director may later create and track operational assignments.

Prepared states include conceptually:

```text
PROPOSED
APPROVED
ACTIVE
WAITING_FOR_EVIDENCE
BLOCKED
VERIFIED_COMPLETE
FAILED
CANCELLED
```

A Director-generated order is an organizational artifact; it is not evidence that the requested result was achieved.

### 9.10 TECHNOLOGY RADAR

Prepared technology-intake path:

```text
NEW TOOL / MODEL / TECHNIQUE
-> RECORDED
-> CLASSIFIED
-> RELATED TO SSI PROBLEM
-> CANDIDATE APPLICATION
-> R&D TEST
-> EVIDENCE
-> ADOPT / REJECT
```

A radar hit must never become an automatic SSI-core modification.

### 9.11 ECONOMY / CAPITAL

The interface reserves explicit slots for future real sources:

```text
BANK / CASH
BROKERAGE
CRYPTO
FX
```

Until connected, the correct state is:

```text
NOT_CONNECTED
UNAVAILABLE
```

not fabricated zero values.

When real sources exist, this area is intended to expose operationally relevant state such as capital, realized/unrealized results, project economics and the planned `50 / 40 / 10` allocation model with source/provenance labels.

### 9.12 DEVELOPER

Low-level diagnostics remain available but are not the primary organizational view.

Examples:

```text
TAILSCALE NODE / LATENCY
PORT / ENDPOINT HEALTH
CPU / RAM / GPU / VRAM
IPC
RAW V10 TRACE
RAW S10 TRACE
CONTINUUM TECHNICAL STATE
LOGS
ADAPTER STATUS
SCHEMA / CONTRACT VERSION
```

## 10. Prepared cross-node record contracts

The precise proprietary implementation may evolve, but the architecture reserves stable semantic record classes so later coding work plugs into known slots rather than inventing new parallel systems.

Conceptual record families include:

```text
NodeSnapshot
CompetenceDelta
EvidenceReference
ConsolidationProposal
LifecycleDecision
AdoptionReceipt
RegressionResult
EffectMeasurement
HermesDelta
ProjectOrder
TechnologyCandidate
FinanceSnapshot
```

Each record should carry, where applicable:

```text
source identity
source version
variant identity
BODY / agent identity
timestamp
evidence / provenance reference
status
schema version
```

## 11. Variant-aware presentation

Because the planned training compares S10 V1, V3 and V2, the Command Center must not flatten them into one indistinguishable result stream.

The interface should preserve at least:

```text
VARIANT = V1 / V3 / V2
BODY LINE = FROZEN / ISKRA1..6
TRAINING STAGE = S1..S10
SOURCE ARTIFACT / PACKAGE ID
EVIDENCE ID
```

Later cross-variant comparison can then ask:

- did the same functional family appear in all variants;
- did role decisions differ;
- did one line produce more false merges/splits;
- did one line require more deep comparisons;
- did target adoption lead to different regressions;
- did cost/speed differ without changing accepted outcomes.

## 12. Fail-closed behavior

The interface must not turn missing data into invented success.

Required visible states include:

```text
NOT_CONFIGURED
OFFLINE
STALE
UNAVAILABLE
WAITING_FOR_EVIDENCE
INCONCLUSIVE
BLOCKED
REGRESSION
```

Examples:

```text
missing finance source -> NOT_CONNECTED
missing BODY endpoint -> NOT_CONFIGURED
lost Tailscale node -> OFFLINE
old snapshot -> STALE
missing S10 evidence -> WAITING_FOR_EVIDENCE
failed target retest -> REGRESSION / REJECT / HOLD according to gate
```

## 13. Security / authority boundary

The organization-wide view is not permission for arbitrary remote execution.

The preserved principle remains:

```text
OBSERVE != CONTROL
```

The owner/operator may have authorized local control paths, but reviewer/public surfaces remain separate and observer-only.

Cross-node Tailscale connectivity does not itself authorize arbitrary remote ROOT or shell execution.

## 14. Pre-training frozen claims

Declared **before** future matched BODY / ISKRA three-variant training outcomes:

```text
DIRECTOR COMMAND CENTER EXISTS
PROFESSIONAL ORGANIZATIONAL INFORMATION MODEL EXISTS
REMOTE NODE SLOTS / CONTRACTS EXIST
TAILSCALE CROSS-NODE MODEL IS DECLARED
HERMES DELTA / CHANGE ROLE IS DECLARED
LOCAL-VS-COLLECTIVE COMPETENCE DISTINCTION IS DECLARED
S10 CROSS-CONSOLIDATION FLOW IS DECLARED
TARGET-SPECIFIC ADOPTION / RETEST IS DECLARED
REGRESSION GATE IS DECLARED
VARIANT-AWARE PRESENTATION IS DECLARED
FINANCE / CAPITAL EXTENSION SLOTS EXIST BUT ARE NOT CONNECTED
ADAPTER-FIRST EXTENSION RULE IS DECLARED
```

## 15. What is not claimed yet

This document does not claim that:

- all BODY / ISKRA nodes are already live over Tailscale;
- all three S10 variants have completed matched S1-S10 training;
- organization-wide cross-consolidation has already produced a positive scientific result;
- every locally learned competence will be transferable;
- every target will accept the same consolidated competence;
- organization-wide consolidation will reproduce the measured drone speedup;
- ROBERT / BODY_FROZEN 2.0 / DIRECTOR already share all future skills;
- technology-radar candidates have already improved SSI;
- financial accounts are connected;
- capital or profit values exist where sources are unavailable;
- the Command Center is production-certified.

## 16. Supported pre-training statement

The supported statement is:

> **Before later matched BODY / ISKRA training outcomes across S10 V1, V3 and V2, SSI V5 has frozen the intended organization-wide cross-consolidation architecture: independent local histories remain isolated during controlled learning; approved deltas and evidence can later move between computers over Tailscale; Router S10 performs evidence-gated functional comparison; target systems receive versioned integration proposals rather than automatic copies; every accepted transfer requires target-specific re-validation and regression control; Hermes reports what changed; Director updates the organizational state; and the Command Center exposes the full lineage interactively without pretending that unconnected systems or financial sources are already live.**

## Related records

- [`DIRECTOR_COMMAND_CENTER_PRETRAINING_GATE_20260914.md`](DIRECTOR_COMMAND_CENTER_PRETRAINING_GATE_20260914.md)
- [`S10_CROSS_CONSOLIDATION_PUBLIC_OVERVIEW_20260912.md`](S10_CROSS_CONSOLIDATION_PUBLIC_OVERVIEW_20260912.md)
- [`DRONE_DOMAIN_RND_COLLABORATION_STATUS_20260914.md`](DRONE_DOMAIN_RND_COLLABORATION_STATUS_20260914.md)
- [`DRONE_MEASURED_RESULTS_20260914.md`](DRONE_MEASURED_RESULTS_20260914.md)
- [`PUBLIC_SHOWCASE_AND_MEASURED_DOMAIN_TRANSFER_EVIDENCE_20260914.md`](PUBLIC_SHOWCASE_AND_MEASURED_DOMAIN_TRANSFER_EVIDENCE_20260914.md)
- [`ROBERT_CANONICAL_CONTINUITY_VS_EXPERIMENTAL_RESET_20260906.md`](ROBERT_CANONICAL_CONTINUITY_VS_EXPERIMENTAL_RESET_20260906.md)
- [`CURRENT_RESEARCH_ROADMAP_20260914.md`](CURRENT_RESEARCH_ROADMAP_20260914.md)
