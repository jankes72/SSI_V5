# SSI V5 — Pre-Benchmark R&D Protocol: Core Training, WEB Engineering and Mexico Robotics

> **Current-state navigation — 2026-09-30:** [latest public status](LATEST_PUBLIC_STATUS_20260930.md) records S20 execution, runtime-reported S19 recovery, concurrent CZARA training and the installed post-CZARA V6 scheduler. Section 3 below preserves the earlier pre-S20 snapshot; its NOT YET STARTED statement is historical. Protocol requirements and original results are retained.

**Recorded:** `2026-09-28`  
**Status:** `PRE-BENCHMARK PROTOCOL / ACTIVE DEVELOPMENT / RESULTS NOT PRECLAIMED`  
**Scope:** public, sanitized description of the intended research sequence, integration boundary and measurements. Proprietary implementation, credentials, prompts, private runtime state and reconstructive internals remain private.

> This document is recorded before the first official Mexico robotics benchmark. It separates implemented/readiness claims, active internal training, planned comparisons and future external evidence. A plan is not a result.

## 1. Purpose

SSI V5 is being developed as a solo R&D system with separate runtime roles for research coordination, technical execution, multilingual context handling, laboratory validation and evidence retention.

This protocol declares in advance:

- the three distinct training/research paths;
- the identity boundaries of DIRECTOR, BODY_FROZEN and ISKRA1..ISKRA6;
- the first Mexico benchmark configuration;
- two concurrent R&D communication channels;
- the role of CZARA and unstructured conversation context;
- the OFFLINE_DIRECTOR / BLOCKS Navigator / BLOCKS Space baseline;
- later comparisons against independent ISKRA trajectories;
- token, reuse, quality and evidence measurements;
- preservation of FAIL and INCONCLUSIVE outcomes.

## 2. Three distinct paths

The project contains three related but distinct paths. They must not be presented as one continuous benchmark.

### Path 1 — Core SSI training: S11-S40

```text
S11 -> S12 -> ... -> S40
  each stage:
  execute declared cases
  -> preserve PASS / FAIL / INCONCLUSIVE
  -> export verified subset only
  -> cross consolidation to BODY_FROZEN + DIRECTOR
  -> COMMITTED gate
  -> next stage
```

The core path develops and measures reusable competence, routing, BLOCKS/micronetwork use, Champion-Challenger selection, failure handling, evidence and cross-stage continuity.

BODY_FROZEN and DIRECTOR receive the same compatible verified competence payload and Champion state through consolidation, while retaining separate identity, runtime, memory, role and decision topology.

The six ISKRA lines retain independent trajectories. They are not reduced after each stage to one shared ISKRA state.

### Path 2 — WEB01-WEB24 engineering training

After S40, a separate WEB engineering track is configured to start only when:

```text
S40 execution_complete = true
AND S40 consolidation = COMMITTED
AND WEB BLOCKS = READY
-> WEB01 -> ... -> WEB24
```

Declared readiness metadata:

```text
stages = 24
cases = 192
BLOCKS items = 126
templates = 15
actors = 7
data policy = SYNTHETIC_ONLY
```

Actors are BODY_FROZEN and ISKRA1..ISKRA6.

The track covers reusable web/programming engineering mechanisms. Its declared progression includes HTML/CSS decomposition, routing, CRUD, authentication, REST/API work, FastAPI, localization, security and a final capstone.

The track uses synthetic/neutralized fixtures rather than real company data. Installation/readiness does not establish live completion.

### Path 3 — Mexico robotics research and external benchmarks

The Mexico path is a separate research programme. It is not a continuation label for WEB training.

Its planned scope includes:

- staged drone and humanoid work;
- cross-domain coordination;
- OFFLINE_DIRECTOR;
- BLOCKS Navigator;
- BLOCKS Space / SPACE_BLOCKS;
- no-network state and map exchange;
- CZARA multilingual research context;
- versioned partner requests;
- supervised validation;
- later unseen external benchmark cases.

The existing Mexico curriculum remains a planned 48-stage programme: 38 training stages, 4 validation stages and 6 capstone stages.

Physical validation, independent external replication and benchmark success are not claimed before corresponding evidence exists.

## 3. Preserved pre-S20 training snapshot — recorded 2026-09-29

The public core-training front now extends through full S19 execution.

```text
S13-S18 = completed with committed consolidations
S19 run = RUN_20260929T005550Z_a356e86c
S19 execution_complete = true
S19 PASS = 182
S19 INCONCLUSIVE = 24
S19 FAIL = 4
S19 verified subset = 182
S19 consolidation = NOT YET CLAIMED COMMITTED
S20 = NOT YET CLAIMED STARTED
```

The S19 case workload completed. The post-stage consolidation then stopped after the project integrated new routing observability intended to resolve whether Champion/Top-1 reuse and Full Flow were actually executing rather than being inferred from catalog state or ambiguous markers.

The current engineering classification is:

```text
OBSERVABILITY_INDUCED_INTEGRATION_REGRESSION
```

This incident is being used as a pre-benchmark hardening input. Before S20 continuation, the routing observer must pass a non-interference A/B gate and the consolidation path must demonstrate 7/7 actor+transaction SNAPSHOT correctness.

The intended core sequence remains continuous after the gates pass:

```text
S19 consolidation COMMITTED
-> S20 ... S40
-> S40 consolidation COMMITTED
-> WEB01 ... WEB24
```

The exact S19 incident and planned hardening are recorded separately:

- [S19 observability incident and pre-S20 status](RESULTS/SSI_V5_S19_OBSERVABILITY_INCIDENT_AND_PRE_S20_STATUS_20260929.md)
- [Pre-S20 observability/evidence hardening preregistration](SYSTEM/SSI_V5_PRE_S20_OBSERVABILITY_AND_EVIDENCE_HARDENING_PREREGISTRATION_20260929.md)

### Evidence-chain and notary addendum informed by external review

External DEV feedback from **Hamid Ahmadian** materially influenced the evidence requirements carried into the Mexico phase. The current preregistered additions include:

- previous-hash-only mutation and missing-sequence causal controls;
- a negative-control field explicitly outside the signed/hash-dependent payload;
- append-only signed local chaining with monotonic sequence;
- separation of executor/verifier/signing authority where independent attestation is claimed;
- explicit notary outage behavior;
- a bounded unsigned-attestation queue;
- a defined buffer-limit transition to safer/degraded operation rather than silent evidence loss or unbounded local-only continuation.

These are requirements to implement and test. They are not presented as already independently validated.

Attribution and source chronology are preserved in [External review feedback and attribution](EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md).

## 4. Champion-Challenger and accumulated competence

A candidate is not promoted merely because it is new. A reusable candidate is expected to carry a compatible package including:

```text
competence
+ input/output contract
+ BLOCKS / micronetwork artifact
+ LAB result
+ evidence
+ provenance
+ version identity
```

The intended lifecycle is:

```text
new verified candidate
-> domain qualification
-> HOLD when no active comparison is justified
OR
-> CHALLENGER when it competes with an existing Champion
-> matched validation
-> retain Champion or promote Challenger
-> retain rollback path
```

The earlier S16 snapshot reported full accounting of 875 BODY_FROZEN candidates:

```text
CHAMPION = 1
CHALLENGER = 1
HOLD = 873
SPECIALIST = 0
accounted = 875 / 875
```

The recorded formal software-engineering Champion was `s10_9769b8e74e6230f29df90218568d4ecf`; the active Challenger was `s10_97a39fdb193470923d6de3f5f0764412`. Both had disclosed validation PASS with approximately `accuracy=0.85` and `F1=0.82`. These values do not establish universal superiority.

Router behavior of interest includes:

```text
sufficient match -> REUSE_TOP1
weak match -> ESCALATE_FULL_FLOW
```

Observed examples included reuse at confidence `0.71` and escalation around confidence `0.3065`. Future reports should connect routing decisions to task identity, model/provider policy, cost and outcome.

## 5. BODY_FROZEN, DIRECTOR and ISKRA identity boundaries

### BODY_FROZEN and DIRECTOR

BODY_FROZEN and DIRECTOR may receive the same verified skills and compatible Champion state after consolidation.

They remain different systems:

```text
BODY_FROZEN
= technical execution role
= separate runtime, memory and identity

DIRECTOR
= planning, coordination, resource and research communication role
= separate runtime, memory and identity
```

Shared skill formats do not imply shared personality or identical decisions. Consolidation transfers compatible verified competence, not BODY identity, ISKRA identity or model weights.

### Independent ISKRA trajectories

Each ISKRA retains:

- its own S-stage history;
- its own PASS / FAIL / INCONCLUSIVE path;
- its own candidate, Champion and Challenger evolution;
- its own micronetwork connections;
- its own reuse/escalation history;
- its own dynamic affective-state trajectory.

The ISKRA affective layer is described as computational state, not a claim of consciousness or subjective experience. Its variables may be updated by decisions, outcomes, failures, uncertainty and feedback, and may modify later risk tolerance, escalation, planning, reuse or Champion selection.

Frozen checkpoints should allow comparison of initial state, post-S40 state, post-WEB state and later task replay.

## 6. Mexico integration readiness boundary

The owner currently estimates the internal Mexico implementation/training readiness at approximately 85%.

This is an engineering estimate, not an external benchmark score.

```text
internal Mexico implementation/training readiness ~= 85% (owner estimate)
official external Mexico benchmark completion = 0%
independent external validation = NOT YET PERFORMED
```

Already implemented or prepared components include:

- Mexico panel;
- DIRECTOR chat;
- BODY_FROZEN chat;
- contextual conversation memory;
- DIRECTOR/BODY role separation;
- consolidated competence compatibility;
- Champion-Challenger and BLOCKS mechanisms;
- laboratory/evidence foundations;
- CZARA architectural boundary;
- OFFLINE_DIRECTOR / BLOCKS Navigator / BLOCKS Space design.

Remaining work before the first official run includes integration, authorization, shared event chronology, stop/pause control verification, evidence completeness tests, offline synchronization checks, an internal rehearsal and version freeze.

## 7. First Mexico benchmark configuration

The first official Mexico configuration is intentionally simpler than the later comparative programme:

```text
DIRECTOR
+ BODY_FROZEN
+ OFFLINE_DIRECTOR
+ CZARA
+ BLOCKS Navigator
+ BLOCKS Space
+ LAB
+ EVIDENCE
```

ISKRA agents are excluded from the first baseline benchmark.

The first question is:

> Can the bounded OFFLINE_DIRECTOR mechanism execute a declared offline mission, use validated competence, preserve local state/evidence, build or exchange spatial BLOCKS fragments and synchronize after reconnection?

Only after this baseline is established should the project compare alternative ISKRA-based offline configurations.

## 8. Two concurrent R&D communication channels

The Mexico panel is intended to support two auditable conversations in parallel.

### Channel A — Professor / research partner to DIRECTOR

```text
VERIFIED PROFESSOR CHAT
-> DIRECTOR
-> interpretation / explanation / versioned research request
-> benchmark or mission revision when authorized
```

DIRECTOR remains the research coordination and explanation interface.

### Channel B — Authorized technical staff to BODY_FROZEN

```text
AUTHORIZED R&D STAFF CHAT
-> BODY_FROZEN
-> technical diagnosis / bounded execution request
-> immediate STOP / PAUSE / SAFE STATE where authorized
```

The direct BODY channel reduces avoidable coordination latency during technical work. DIRECTOR observes BODY state/events and can explain to the professor what stopped, why it stopped, who or what initiated the stop, what evidence was retained and what next revision is proposed.

Authority boundary:

```text
STOP / PAUSE / SAFE STATE
= direct and immediate when authorized

change of benchmark objective, acceptance criteria or frozen protocol
= versioned revision through the declared research-control path
```

A technical chat must not silently rewrite a frozen benchmark.

## 9. CZARA and structured versus unstructured context

CZARA is a multilingual context/translation layer, not a robot controller.

It should preserve original Spanish/English text, Polish translation, source session, verified speaker identity where available, uncertainty, topic, requirement, decision, correction, open question, confidence and provenance.

Two information classes must remain distinct:

```text
VERIFIED PROFESSOR MESSAGE
!=
UNSTRUCTURED CONVERSATION CONTEXT
```

Unstructured conversation may contain a mixture of professor, student, technical team and incidental remarks. SSI must segment and classify this context rather than treating every sentence as an instruction.

Where intent or authority is uncertain, DIRECTOR should request confirmation through the verified professor channel before changing a frozen mission.

The evidence chain should be:

```text
source
-> original text
-> translation
-> structured context
-> DIRECTOR interpretation
-> versioned decision
-> BODY_FROZEN execution
-> LAB result
-> evidence
```

## 10. Later offline comparison: consolidated core versus independent ISKRA

After the baseline OFFLINE_DIRECTOR mechanism is demonstrated, later controlled comparisons may include:

```text
OFFLINE_DIRECTOR with consolidated competence
vs
BODY_FROZEN Offline
vs
ISKRA1..ISKRA6 Offline
```

A preregistered research question is:

> Can an independent ISKRA trajectory, using its own training history, affective-state evolution, micronetworks and Champion-Challenger state, outperform the consolidated OFFLINE_DIRECTOR/BODY_FROZEN baseline in selected BLOCKS Navigator or BLOCKS Space tasks without internet access?

Example hypothesis for ISKRA6:

```text
H0:
consolidated OFFLINE_DIRECTOR/BODY_FROZEN is equal or superior.

H1:
ISKRA6 achieves better quality, stability or efficiency because its independent trajectory preserves a domain-specialized solution.
```

No particular ISKRA is predeclared as the winner.

## 11. Longitudinal and replay measurements

Recommended frozen checkpoints:

```text
initial state
post-S16
post-S40
post-WEB24
final selected-task replay
```

Earlier FAIL and INCONCLUSIVE cases may be replayed after later training under matched conditions.

Where technically possible, controlled replay variants should separate competence evolution from affective-state evolution:

```text
initial competence + initial affective state
final competence + final affective state
final competence + initial affective state
initial competence + final affective state
```

This design is intended to distinguish association from stronger causal evidence. Model/provider, tools, limits and acceptance rules must be recorded.

## 12. Token and efficiency evidence

A decrease in paid-model token consumption has been observed by the owner across later training activity. The measured decrease should be published from retained ledgers and routing records.

Observed token reduction is a result. Its cause remains a hypothesis until connected to controlled routing and task comparisons.

Reports should include:

- paid input/output tokens per case;
- cost per verified PASS;
- model/provider class;
- daily token/cost limit;
- REUSE_TOP1 count;
- intermediate verify/adapt count;
- ESCALATE_FULL_FLOW count;
- cache/local-model use;
- time and retries;
- PASS / FAIL / INCONCLUSIVE.

A stronger efficiency result requires:

```text
lower paid-token use
+ stable or improved verified quality
+ increased validated reuse
+ fewer unnecessary full-flow escalations
```

## 13. Post-WEB artifact comparison

After WEB01-WEB24, BODY_FROZEN and each ISKRA may receive the same previously unseen specification for a page, panel or application.

Controls should include identical functional requirements, identical allowed assets, matched model/tool policy, matched time and token limits, no access to another actor's solution and frozen evaluation criteria.

The comparison should retain:

- screenshots and interaction recordings;
- code/version hashes;
- DOM/component structure where applicable;
- selected BLOCKS and templates;
- Champion/Challenger identity;
- iterations, tokens, time and cost;
- automated functional/security/accessibility results;
- blind human visual evaluation.

Research hypothesis:

> Independent training, micronetwork, Champion-Challenger and affective-state trajectories may produce measurable differences in architecture, interaction design and visual finish despite the same functional objective.

Different-looking outputs are not guaranteed and must be measured rather than assumed.

## 14. Minimum benchmark evidence

For every official benchmark/revision:

```text
benchmark ID and revision
acceptance criteria
SSI version
actor/runtime identity
model/provider policy
initial checkpoint
selected Champion(s)
selected BLOCKS/micronetwork packages
routing decisions
token/cost ledger
execution events
STOP/PAUSE events
LAB observations
PASS / FAIL / INCONCLUSIVE
retained integrity evidence
partner-visible sanitized report
optional post-result consolidation
```

Negative and inconclusive results must not be deleted or silently converted to PASS.

## 15. Claim boundary

This protocol does not establish:

- completion of S13-S40 in the public evidence mirror;
- completion of WEB01-WEB24;
- completion of the 48-stage Mexico programme;
- superiority of any ISKRA;
- proof that affective state caused a particular improvement;
- physical drone or humanoid validation;
- certified offline navigation;
- safety certification;
- independent external replication;
- production readiness;
- AGI or consciousness;
- superiority over external R&D teams.

It establishes that the intended sequence, controls, measurements and later comparative questions were recorded before the first official Mexico benchmark.
