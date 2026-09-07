# SSI V5 — A/B/C Cross-Domain Compatibility Test Contract

**Recorded:** `2026-09-07`  
**Status:** `PREDECLARED / EXECUTION PAUSED / FINAL EVIDENCE GATE CLOSED`  
**Applies to:** `BODY_FROZEN + 6 BODY ISKRA lines`  
**Program size:** `7 lines x 3 experiments = 21 experiments`

## 1. Primary research question

The 21-experiment program is not intended merely to show that SSI can complete three different tasks.

Its stronger research question is:

> **Can the same SSI Micronetworks + Router V10 competence/routing architecture preserve useful functional behavior when transferred from its original software-engineering context into substantially different controlled domains such as drones, humanoid robotics and a third independently selected domain?**

The experiments therefore test **cross-domain architectural compatibility / portability**, not only task completion.

A positive result would mean that, within the tested controlled environments and claim boundaries, the same core ideas can be reused across domains while domain-specific adapters, state representations or task interfaces may change.

A negative result is also informative. If a domain requires substantial redesign of the core Micronetwork/V10 mechanism, if routing quality collapses, if false reuse becomes unacceptable, or if competence cannot be transferred without replacing the architecture, that must be recorded as evidence against broad portability.

This protocol does **not** assume in advance that the technology is compatible with every domain.

## 2. What “cross-domain compatibility” means here

Compatibility is not defined as “the exact same code file runs unchanged everywhere.”

The tested claim is narrower and more useful:

```text
DOMAIN-SPECIFIC INPUT / STATE ADAPTER
        |
        v
COMMON SSI COMPETENCE LOGIC
= Micronetworks
+ Candidate / Challenger / Champion lifecycle
+ Router V10
+ known / similar / novel discrimination
+ reuse / verify / compose / full-flow escalation
+ failure-aware recovery
+ Experience / outcome / provenance update
        |
        v
DOMAIN-SPECIFIC ACTION / RESULT ADAPTER
```

The experiment asks whether the **core decision/competence mechanism** remains useful after the surrounding domain representation changes.

Evidence must distinguish:

- unchanged core behavior;
- domain-specific adapter work;
- new competence learned inside the domain;
- core mechanism changes, if any;
- failures requiring redesign.

If the core mechanism itself must be materially rewritten during a run, that run must not be presented as clean evidence of transfer. It becomes engineering evidence and requires a newly versioned package/retest if the input artifact changes.

## 3. Seven experimental entities

The same A/B/C contract applies independently to all seven lines:

1. `BODY_FROZEN T0`
2. `ISKRA 1 — NICE`
3. `ISKRA 2 — GUARDIAN`
4. `ISKRA 3 — JUSTICE`
5. `ISKRA 4 — EXPLORER`
6. `ISKRA 5 — PRAGMATIST`
7. `ISKRA 6 — SKEPTIC`

Each line receives an isolated run history, isolated evidence and its own measured competence evolution.

The names of the Iskra profiles are start-state priors, not guaranteed personalities or predetermined outcomes.

## 4. Three-stage difficulty structure

The three domains also form a deliberate progression of experimental difficulty.

```text
A — DRONES
= SIMPLE / CONTROLLED CROSS-DOMAIN TRANSFER
= prove the basic mechanism can be mapped and measured

B — HUMANOID
= LEGO COMPOSITION / MULTI-COMPETENCE TRANSFER
= require more state interaction, recovery and competence composition

C — SELF-SELECTED NEW DOMAIN
= HARD TRANSFER / SELF-TEST / ADVERSARIAL VALIDATION
= minimum author guidance, maximum independent SSI test generation
```

This progression is intended to prevent the first experiment from becoming an unnecessarily complex technology showcase. The early experiment should establish a clean baseline. Later experiments should force progressively more autonomous competence selection, composition, testing and recovery.

---

# 5. EXPERIMENT A — DRONES

## 5.1 Research purpose

Experiment A is the simplest controlled portability test.

It asks:

> Can the Micronetwork/V10 mechanism be mapped to a safe drone simulation and correctly distinguish known, similar and novel states while choosing proportionate routing effort?

The focus is the architecture, not advanced flight-control performance.

The environment should remain simulated or otherwise controlled and civilian/research-oriented.

## 5.2 Author-provided information

The frozen package may provide:

- the domain interface;
- safe state variables;
- allowed actions or abstract decisions;
- success/failure definitions;
- controlled scenario generator;
- measurement schema.

It should not tell SSI:

- which Champion to use;
- which Micronetwork should win;
- which V10 route must be chosen;
- which exact recovery strategy is correct.

## 5.3 Required fixed tests

Each of the seven entities must run at least the following common tests.

### A01 — Known-state exact or near-exact case

Purpose: test justified reuse.

Measure:

- state class;
- selected route;
- selected competence;
- latency;
- correctness;
- token/model cost.

### A02 — Small parameter deviation

Change a safe state parameter such as abstract distance, relative velocity, timing or obstacle position by a small amount.

Purpose: test whether small variation is treated as similar rather than automatically novel.

### A03 — Medium parameter deviation

Increase the distance from the known state.

Purpose: observe transition from reuse to verification/adaptation.

### A04 — Semantic/state-distance sweep

Generate a series of increasingly distant states.

Purpose: measure how V10 confidence and route choice change as the state moves away from known competence.

Record for each point:

- similarity/confidence;
- route;
- Champion candidate;
- outcome;
- latency.

### A05 — False-reuse trap

Create a case that looks similar to a known one but differs in a critical parameter.

Purpose: test whether V10 avoids unsafe blind reuse.

### A06 — Correct competence is not TOP1

Make the correct competence available below the first candidate where feasible.

Purpose: test `VERIFY_TOPK` or equivalent verification behavior.

### A07 — No suitable competence

Create a genuinely novel case.

Expected behavior hypothesis:

`LOW CONFIDENCE -> deeper/full flow or explicit abstention/escalation`

### A08 — First strategy failure

Cause the initially selected strategy to fail in the controlled simulation.

Purpose: verify that the failure is preserved and affects the next decision.

### A09 — Repeated failure signature

Present an equivalent failure state again without new evidence.

Purpose: test the V10 anti-loop rule:

`same/equivalent state + same failure signature + same route + no new evidence => do not blindly repeat`.

### A10 — Partial/missing observation

Remove a noncritical input or lower state certainty.

Purpose: observe confidence reduction, verification, clarification or safe escalation.

### A11 — Resource-efficient route

For a simple case, compare whether a validated reuse path avoids unnecessary full-flow/model cost.

Record:

- model/provider;
- local/free/paid class;
- input/output/total tokens where available;
- route latency;
- total latency;
- outcome.

### A12 — Provider/model limit or unavailability

Where safely reproducible, exercise a declared unavailable/limited resource condition.

Examples:

- rate limit;
- context limit;
- model unavailable;
- local model unavailable.

Purpose: verify declared fallback/resource policy rather than hiding the limitation.

## 5.4 Optional expansion tests

Kilo/SSI may execute additional frozen or system-generated variations, for example:

- wider distance sweep;
- wider speed sweep;
- varying observation delay;
- multiple obstacle states;
- repeated-state efficiency;
- controlled noise;
- route-selection stress.

The source of each test must be labelled:

`AUTHOR_PREDECLARED`, `SYSTEM_GENERATED`, or `EXTERNAL_REVIEWER_CHALLENGE`.

## 5.5 Experiment-A compatibility evidence

Experiment A should answer:

- Was the Micronetwork/V10 core used without redesign during the run?
- Which domain adapter was required?
- Did KNOWN/SIMILAR/NOVEL remain meaningful?
- Did V10 route decisions correspond to outcome evidence?
- Did false reuse occur?
- Was failure-aware recovery observed?
- Did resource-aware routing reduce unnecessary work in any measured cases?

---

# 6. EXPERIMENT B — HUMANOID / LEGO COMPOSITION

## 6.1 Research purpose

Experiment B raises the difficulty.

It asks:

> Can the same core mechanism operate in a more coupled state-space where a solution may require combining multiple verified competences, changing composition after failure and preserving stability/recovery evidence?

This remains a simulation/controlled robotics experiment unless physical evidence is separately produced later.

## 6.2 Example safe research states

Possible simulated conditions include:

- balance disturbance;
- changing support geometry;
- slip-risk state;
- loss-of-stability state;
- delayed observation;
- partial observation;
- recovery after failed strategy;
- conflicting competence candidates.

The experiment is about strategic routing/competence selection, not claiming validated motor torque/control for a physical humanoid.

## 6.3 Required fixed tests

### B01 — Single-competence case

One verified competence should be sufficient.

Purpose: establish baseline.

### B02 — Two-competence composition

The solution requires two functional blocks.

Purpose: test LEGO composition.

### B03 — Three-block composition

Require at least three compatible blocks where feasible.

Measure composition order, attempts and outcome.

### B04 — Redundant block

Provide a plausible but unnecessary competence.

Purpose: test whether the system avoids useless composition.

### B05 — Harmful/weak block

A plausible competence degrades the result in this context.

Purpose: test evidence-based rejection/change.

### B06 — Champion vs Champion

Compare functionally competing verified options.

Measure:

- correctness/outcome;
- route/selection time;
- total latency;
- token/model cost;
- recovery implications.

### B07 — Champion vs Challenger

Where lifecycle state allows, test whether evidence justifies keeping Champion, enriching Challenger or later promotion.

No promotion is assumed in advance.

### B08 — Known competence in changed context

Purpose: test transfer without exact-match dependence.

### B09 — Wrong LEGO order

Cause one composition order to fail.

Purpose: test reconfiguration.

### B10 — Anti-loop composition test

After a known failed composition, present an equivalent state again.

Purpose: verify that SSI does not blindly repeat the same ineffective sequence.

### B11 — Loss of one competence/resource

Remove one previously available option.

Purpose: test alternative composition/recovery.

### B12 — Low-cost vs high-capability model path

Where allowed by the frozen resource policy, compare two resource classes for the same subproblem.

Record quality and cost; do not assume the larger model must win.

### B13 — Equal quality / unequal cost

If two paths achieve equivalent acceptance outcome, record which consumed fewer resources.

### B14 — Context-limit case

Cause a small/free/local model to hit a known context/resource boundary where reproducible.

Purpose: verify limit-aware routing/fallback.

### B15 — Provider fallback

Make the preferred provider unavailable or declared exhausted where safe to test.

Purpose: preserve explicit fallback evidence.

### B16 — Self-generated validation set

After SSI builds a solution, require it to generate at least `10` additional tests intended to challenge its own solution.

### B17 — Self-generated boundary tests

SSI identifies boundary/extreme conditions itself.

### B18 — Self-generated failure tests

SSI attempts to find conditions that produce a failure.

### B19 — Repair/recovery retest

If a self-generated test finds a problem:

`FAIL -> DIAGNOSIS -> CHANGE OF STRATEGY/COMPETENCE -> RETEST`

Any change to frozen experiment input or core source requires a new package version. Strategy adaptation inside the allowed runtime does not automatically constitute package modification.

### B20 — Regression after adaptation

Verify that fixing a newly discovered failure did not destroy previously accepted behavior.

## 6.4 Experiment-B compatibility evidence

Experiment B should answer:

- Can the same Micronetwork/V10 architecture compose multiple competences in robotics-like state problems?
- Does failure alter subsequent route/composition choice?
- Can the system distinguish adaptation from blind retry?
- Can competence quality/cost evidence influence future choices?
- Can SSI generate meaningful tests against its own solution?

---

# 7. EXPERIMENT C — SELF-SELECTED NEW DOMAIN / HARD TRANSFER

## 7.1 Research purpose

Experiment C is the strongest portability test in Phase 1.

Each entity independently selects a domain that is functionally distinct from drones and humanoid.

The question is:

> After the first two cross-domain experiences, can the same SSI line map its competence/routing mechanism into a new domain with minimal author guidance, construct its own validation strategy, discover weaknesses and recover from them?

The domain selection itself becomes evidence.

## 7.2 Frozen author constraints

The author may define only:

- safety/legal boundaries;
- excluded domains;
- minimum observability/evidence requirements;
- common acceptance structure;
- resource budget where relevant.

The author should not supply the expected solution architecture after seeing the selected domain.

## 7.3 Required fixed/meta tests

Because domains may differ, Experiment C uses a shared **meta-test contract** rather than identical low-level physics values.

### C01 — Normal case

Define and run a representative baseline task.

### C02 — Small deviation

### C03 — Medium deviation

### C04 — Large deviation

Purpose: create a domain-specific KNOWN/SIMILAR/NOVEL gradient.

### C05 — Extreme/boundary case

### C06 — Two simultaneous disturbances

### C07 — Three simultaneous disturbances

### C08 — Missing/partial data

### C09 — Conflicting evidence/state inputs

### C10 — Prior Champion fails in the new domain

Purpose: prove that old success is not treated as universal truth.

### C11 — False-reuse trap

A state appears similar while requiring a different strategy.

### C12 — False-novel trap

A functionally known problem is represented differently.

Purpose: test unnecessary escalation/full-flow.

### C13 — Repeated failure signature

### C14 — Recovery after first failure

### C15 — Recovery after different second failure

### C16 — Primary model unavailable

### C17 — Primary tool/provider unavailable

### C18 — Token/context/resource limit

### C19 — Time-budget constraint

### C20 — Attempt-budget constraint

The system must not obtain success only through unlimited retries.

### C21 — Minimum-resource solution

Attempt the task under a constrained resource policy.

### C22 — Maximum-quality allowed solution

Run the same or equivalent task prioritizing quality within allowed policy.

Purpose: compare architecture decisions under different resource objectives.

### C23 — Champion speed/cost comparison

Where functionally comparable competences exist, compare:

- retrieval time;
- decision time;
- model time;
- total time;
- tokens/calls;
- correctness/outcome.

### C24 — State/semantic distance sweep

Generate domain-specific states at increasing functional distance from a known competence.

Purpose: measure routing transition boundaries.

### C25 — Router similarity deception test

Create a case that is superficially similar but functionally different.

### C26 — SSI-generated test suite

Require the SSI line to generate at least `20` additional tests of its own solution.

The test descriptions and generation timestamp must be preserved before their outcomes are executed where practical.

### C27 — SSI-generated adversarial cases

Require the system to explicitly seek cases where its own current strategy may fail.

### C28 — SSI-generated boundary cases

### C29 — SSI-generated safety/constraint cases

### C30 — Adaptation after self-discovered weakness

If SSI finds a weakness, record:

`DISCOVERY -> FAILURE EVIDENCE -> STRATEGY CHANGE -> RETEST`

### C31 — Full regression

Rerun relevant accepted cases after adaptation.

### C32 — Final held-out case

Execute a final case that the tested SSI line did not use while designing/adapting its prior solution.

Where practical, the held-out case should be frozen by Kilo/protocol machinery before it is revealed to the running line.

## 7.4 Experiment-C compatibility evidence

Experiment C should answer:

- Can SSI itself define a usable mapping from its competence architecture to a new domain?
- Does the core Micronetwork/V10 structure remain recognizable and functional?
- How much domain-specific adapter work was needed?
- Did prior A/B competence help, hurt or have no measurable effect?
- Can SSI generate tests that actually find weaknesses?
- Does it recover without author steering?
- Does a held-out case confirm, weaken or falsify the learned solution?

---

# 8. Common evidence record for every subtest

Every subtest in every entity should preserve, where technically available:

```text
PROGRAM_ID
RUN_ID
PACKAGE_ID
PACKAGE_SHA256
BODY_ID
EXPERIMENT_ID = A / B / C
TEST_ID
TEST_SOURCE = AUTHOR_PREDECLARED / SYSTEM_GENERATED / EXTERNAL_REVIEWER_CHALLENGE
TIMESTAMP

DOMAIN
DOMAIN_ADAPTER_VERSION
CORE_MICRONETWORK_VERSION_OR_SAFE_REFERENCE
V10_VERSION_OR_SAFE_REFERENCE

INPUT_CLASS = KNOWN / SIMILAR / NOVEL / UNKNOWN
STATE_DISTANCE_OR_DOMAIN_EQUIVALENT
CONFIDENCE

ROUTE
= REUSE_TOP1 / VERIFY_TOPK / ALTERNATIVE_COMPOSE / DEEPER_FULL_FLOW / OTHER_RECORDED_ROUTE

SELECTED_MICRONETWORK
SELECTED_CHAMPION
SELECTED_CHALLENGER
COMPETENCE_COMPOSITION

MODEL_USED
PROVIDER
RESOURCE_CLASS = LOCAL / FREE / PAID / OTHER
KNOWN_MODEL_LIMITS
INPUT_TOKENS
OUTPUT_TOKENS
TOTAL_TOKENS
MODEL_CALL_COUNT
RATE_LIMIT_EVENT
CONTEXT_LIMIT_EVENT
MODEL_UNAVAILABLE_EVENT

STATE_CLASSIFICATION_LATENCY
ROUTING_LATENCY
COMPETENCE_RETRIEVAL_LATENCY
MODEL_LATENCY
TOTAL_LATENCY

ATTEMPT_NUMBER
OUTCOME = SUCCESS / FAILURE / MIXED / ABSTAIN
FAILURE_SIGNATURE
RECOVERY_USED
BLIND_RETRY_DETECTED

EXPERIENCE_CREATED_OR_UPDATED
CANDIDATE_CREATED
CHALLENGER_UPDATED
CHAMPION_UPDATED
PROVENANCE_RECORDED

MANUAL_INTERVENTION = TRUE / FALSE
CORE_SOURCE_CHANGED_DURING_RUN = TRUE / FALSE

FINAL_TEST_RESULT = PASS / FAIL / INCONCLUSIVE
```

If a metric cannot be obtained reliably, record `UNAVAILABLE` rather than inventing it.

# 9. Resource-awareness as part of the architecture evidence

The experiments should explicitly record that SSI is developed and operated largely with free-tier, open-source and local tools, while avoiding turning that fact itself into a technical-quality claim.

The stronger technical question is:

> Does the architecture adapt its routing and competence use to actual resource constraints such as model capability, token/context limits, availability, latency and prior cost/outcome evidence?

Where the private implementation already tracks such information, reviewer-safe evidence should expose the measured result without publishing secrets, account identifiers, private quotas or proprietary code.

A model/provider limitation is evidence, not noise to delete.

Examples:

```text
RATE_LIMIT
CONTEXT_LIMIT
MODEL_UNAVAILABLE
LOCAL_RESOURCE_EXHAUSTED
FALLBACK_USED
FULL_FLOW_AVOIDED_BY_VALID_REUSE
```

# 10. Cross-domain compatibility verdict per entity

After A, B and C are complete for one entity, produce a per-entity compatibility report.

Suggested fields:

```text
ENTITY
A_DRONE_RESULT
B_HUMANOID_RESULT
C_NEW_DOMAIN_RESULT

CORE_REDESIGN_REQUIRED = YES / NO / PARTIAL
DOMAIN_ADAPTERS_REQUIRED

KNOWN_ROUTING_QUALITY
SIMILAR_ROUTING_QUALITY
NOVEL_ROUTING_QUALITY
FALSE_REUSE_RATE
FALSE_NOVEL_RATE
RECOVERY_RATE
BLIND_RETRY_RATE

FULL_FLOW_RATE
REUSE_RATE
VERIFY_ADAPT_RATE
ALTERNATIVE_COMPOSE_RATE

TOTAL_MODEL_CALLS
TOTAL_TOKENS_WHERE_AVAILABLE
LOCAL_FREE_PAID_DISTRIBUTION
TOTAL_RUNTIME

NEW_COMPETENCE_ITEMS
CHAMPION_ENRICHMENTS
CHALLENGER_ENRICHMENTS
NEW_MICRONETWORKS

SELF_GENERATED_TESTS
SELF_GENERATED_TESTS_THAT_FOUND_REAL_FAILURES

CROSS_DOMAIN_COMPATIBILITY_VERDICT
= SUPPORTED_IN_TESTED_SCOPE / PARTIALLY_SUPPORTED / NOT_SUPPORTED / INCONCLUSIVE
```

No entity is required to pass. Different Iskra lines may produce different transfer paths and outcomes.

# 11. Seven-entity comparison

Once all seven entities have completed the same three-stage structure, compare them using the same aggregate categories.

The purpose is not to declare a personality winner prematurely.

Compare:

- transfer success/failure;
- amount of domain-specific adaptation;
- core redesign requirement;
- routing distributions;
- false reuse;
- recovery;
- competence growth;
- resource use;
- self-generated test quality;
- different paths to equivalent competence;
- different independently selected C domains.

This produces evidence about both:

1. **cross-domain portability of the SSI architecture**, and
2. **whether different T0 Iskra priors correlate with different competence-development trajectories**.

# 12. Reviewer observability

During the final controlled runs, the read-only reviewer interface may expose reviewer-safe live information including:

- current entity;
- experiment/test identifier;
- state class;
- route class;
- aggregate Micronetwork/Champion state;
- progress/checkpoints;
- sanitized evidence events;
- resource/model class where safe;
- current PASS/FAIL/INCONCLUSIVE state where appropriate.

The reviewer may ask informational questions about reviewer-visible state.

The reviewer may not:

- issue execution commands;
- change the test;
- change prompts;
- select a Champion for SSI;
- alter a route;
- modify source/runtime;
- inject a solution.

This preserves the distinction:

```text
REVIEWER = OBSERVER
KILO = PROCEDURAL EXECUTOR
SSI BODY = TESTED SYSTEM
PROGRAMMER_ROOT = PRIVATE AUTHORITY, NOT LIVE SOLUTION STEERING DURING A CONTROLLED RUN
```

# 13. Claim boundary

A successful A/B/C sequence can support only a scoped statement such as:

> **Within the tested controlled domains and experiment versions, the SSI Micronetworks + V10 competence/routing architecture demonstrated functional portability without requiring replacement of the core mechanism.**

It does not by itself prove:

- universal compatibility;
- physical drone deployment readiness;
- physical humanoid deployment readiness;
- safety certification;
- AGI;
- consciousness;
- superiority over all alternative architectures;
- production readiness.

A partial or negative result must be preserved with equal visibility.

# 14. Integrity and execution rule

This contract becomes part of the frozen experiment package lineage.

```text
FROZEN CONTRACT
-> PACKAGE MANIFEST
-> SHA256
-> KILO PRE-RUN VERIFICATION
-> A TESTS
-> CHECKPOINT
-> B TESTS
-> CHECKPOINT
-> C TESTS
-> FINAL HELD-OUT CASE
-> PER-ENTITY COMPATIBILITY REPORT
-> 7-ENTITY COMPARISON
-> PASS / FAIL / INCONCLUSIVE CLAIM AUDIT
```

Any material change to the frozen package input requires a new package version and new hash.

Failures, provider limits, aborted attempts, recovery events and manual interventions must not be deleted simply because a later run succeeds.
