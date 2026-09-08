# SSI V5 — Research Front Door

**Experimental persistent-competence architecture for adaptive AI systems.**

SSI V5 investigates whether a long-running system can build, validate, preserve, reuse, compare and revise competence across tasks using persistent state, Experience, Micronetworks, Candidate -> Challenger -> Champion lifecycle, V10 stateful routing, LEGO composition and CONTINUUM persistence.

The public repository is an **evidence-indexed research mirror**, not a source-code distribution. Private SSI, Micronetwork, Router V10, ISKRA and ROBERT implementation source remains private by design.

## Independent project context

SSI V5 is independently designed and developed by **Paweł Jankiewicz (`jankes72`)**, a self-taught developer working outside a formal academic or AI-lab path. Coding/research assistants such as Kilo, OpenCode, Pi and local/open models are used as implementation, analysis and testing tools; they are not presented as the authors of the architecture or research claims.

The project should be evaluated from its **predeclared protocols, measured outcomes, failures, repairs, retests, hashes, claim boundaries and reviewer-visible evidence**, not from the author's background alone.

See [`AUTHOR_CONTEXT.md`](AUTHOR_CONTEXT.md).

## Current research state — 2026-09-08

```text
FROZEN COMMON BASELINE
= BODY_FROZEN T0 / PRE-ISKRA / 2026-09-05

CURRENT ISKRA START STATE
= 6 independent BODY ISKRA descendants / START_STATE_VALIDATED / 2026-09-06

LATEST CLOSED DEVELOPMENT VALIDATION
= TEST 5 / DEVELOPMENT_VALIDATED
= 29/29 acceptance
= 524/524 total regression
= 0 open blockers in tested scope

TECHNICAL READINESS
= 7 BODY lines + reviewer interface
= final validation in progress / required before training or final experiment execution

PRE-EXPERIMENT TRAINING
= 14 HASH-SEALED packages
= 7 BODY lines x 2 phases
= PREDECLARED / NOT YET EXECUTED

MECHANISM TEST PACKAGES
= 7 independent Micronetwork + V10 packages
= PREDECLARED / HASH-SEALED / NOT YET EXECUTED

CROSS-DOMAIN PROGRAM
= 7 lines x 3 domains = 21 experiments
= PREDECLARED / final controlled outcomes not yet claimed

LIVE REVIEWER INTERFACE
= READ-ONLY OBSERVABILITY
= local ROOT execution remains separate

CANONICAL ROBERT
= continuous engineering line
= not reset by experiment-branch cleaning
```

## Research sequence

The current controlled sequence is:

```text
1. TECHNICAL READINESS
   7/7 BODY lines
   + reviewer interface
   + runtime / CONTINUUM / Micronetwork / V10 / persistence / isolation / read-only gates

2. PRE-EXPERIMENT TRAINING
   TRAIN-A FOUNDATION
   -> FOUNDATION_S1
   TRAIN-B LEGO + MICRONETWORK + V10 PRACTICUM
   -> TRAINED_START_S2
   -> record S2 identity/hash

3. MICRONETWORK + V10 MECHANISM TESTS
   BODY_FROZEN first
   -> then NICE
   -> GUARDIAN
   -> JUSTICE
   -> EXPLORER
   -> PRAGMATIST
   -> SKEPTIC

4. CROSS-DOMAIN PROGRAM
   DRONES
   -> HUMANOID
   -> third domain independently selected by each SSI line

5. POST-21 CONSOLIDATION
   compare actual competence
   -> functional deduplication
   -> Champion/Challenger enrichment
   -> versioned consolidated BODY descendant
   -> 3 new domains

6. LATER EXTERNAL FALSIFICATION
   external specialists propose unseen / adversarial challenge classes
   -> frozen challenge package
   -> first controlled run
   -> read-only live observation
   -> preserve PASS / FAIL / INCONCLUSIVE
```

No later-stage success is claimed in advance.

## Pre-experiment training — 14 independent packages

Training is now an explicit methodological stage rather than an undocumented preparation step.

Each BODY receives the same two curriculum families:

### A — Foundation

General reusable competence:

- task interpretation and decomposition;
- programming fundamentals;
- debugging and root-cause analysis;
- test-before-closure discipline;
- task/project management;
- evidence and provenance;
- checkpoint/resume;
- resource-aware execution.

The lesson structure is:

```text
INSTRUCTION
-> GUIDED PRACTICE
-> BLIND VALIDATION
```

Only verified blind-validation outcomes may support canonical Experience/lifecycle progression.

### B — LEGO + Micronetwork + V10 Practicum

Practical competence use:

- LEGO decomposition/composition;
- known-skill reuse;
- similar/ambiguous verification;
- multi-skill composition;
- deceptive-similarity / false-reuse protection;
- controlled failure;
- repeated-failure anti-loop;
- recovery with new evidence;
- persistence across restart;
- route-cost and hardware measurement;
- backend-to-live-interface correlation.

Training uses **different task vectors from the held-out mechanism experiments**. The exact later experiment answers are not taught during training.

Canonical training methodology:

- [`PREEXPERIMENT_TRAINING_PROGRAM_20260908.md`](PREEXPERIMENT_TRAINING_PROGRAM_20260908.md)

Training package registry and hashes:

- [`PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md`](PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md)
- [`TRAINING_PACKAGES_START_HERE.md`](TRAINING_PACKAGES_START_HERE.md)

Shared curriculum integrity references:

```text
FOUNDATION_CURRICULUM_SHA256
= 61a3069ce68d19c64d4ae7c5ebc730d04283d81b2e534f487c3fd5063d9b75b8

PRACTICUM_CURRICULUM_SHA256
= abc3eccc4e19849f2d3b3be5b1a4d2752377b6024225f0da8d7d54f4ebafc7ce
```

All fourteen training outcomes are currently `UNKNOWN`.

## T0 remains immutable

Training does not rewrite historical baselines.

```text
BODY T0
= preserved historical control

FOUNDATION_S1
= versioned training descendant

TRAINED_START_S2
= versioned post-practicum descendant
```

Before a later research run, the exact S2 identity/hash must be recorded. The seven previously predeclared EXP-01 ... EXP-07 package hashes remain unchanged historical precommitments. If binding S2 materially changes a frozen experiment input, a **new experiment package version and new hash** are required rather than silently editing the old package.

## Route speed and compute measurement

SSI V5 measures not only whether a route is correct, but what the route actually costs on real tasks.

Where the runtime exposes the relevant evidence, training and later experiments record:

```text
ACTUAL V10 ROUTE CLASS
+ elapsed time
+ routing/retrieval/verification/adaptation timing
+ model/provider class
+ model-call count
+ tool-call count
+ execution-node identity/class
+ CPU / RAM
+ GPU / VRAM
+ correctness / outcome
```

Route families include:

```text
FULL_FLOW
VERIFY_TOPK / intermediate verify-adapt
REUSE_TOP1 / fastest validated reuse
LEGO / alternative composition
RECOVERY AFTER FAILURE
```

For at least five comparable observations in one route/hardware/model stratum, summaries may include `count`, `min`, `mean`, `p50`, `p95`, `max` and total elapsed time.

The strongest current comparison is **within SSI under controlled conditions**, for example full flow versus verification versus validated reuse. SSI V5 does not claim that V10 is faster than unrelated external systems without a separately controlled benchmark using matched tasks, models/providers and hardware.

Historical scoped Test 3 evidence recorded `57.61 s` versus `126.65 s` for Test 2, with `534 REUSE_TOP1`, `66 VERIFY_TOPK`, `0 fallback`, and `100/100` measured correctness on the known-case subset. That result is preserved as scoped development evidence, not universal performance proof.

See [`V10_PREDICTIVE_ROUTING.md`](V10_PREDICTIVE_ROUTING.md).

## Live reviewer observability

The shared reviewer interface presents reviewer-safe live state for:

```text
BODY_FROZEN
ISKRA 1 — NICE
ISKRA 2 — GUARDIAN
ISKRA 3 — JUSTICE
ISKRA 4 — EXPLORER
ISKRA 5 — PRAGMATIST
ISKRA 6 — SKEPTIC
```

Where available, a reviewer may observe:

- real online/offline/runtime state;
- mission or training/experiment stage;
- checkpoint/progress;
- CONTINUUM state;
- Micronetwork/lifecycle summary;
- reviewer-safe V10 route class;
- execution-node identity/class;
- CPU/RAM/GPU/VRAM;
- sanitized events/evidence references.

The interface is **read-only**. It cannot issue ROOT commands, create or alter missions, start/stop Kilo, change prompts or acceptance criteria, edit configuration/source, access private memory or provide a hidden execution route.

See [`REVIEWER_LIVE_INTERFACE_20260907.md`](REVIEWER_LIVE_INTERFACE_20260907.md).

## Canonical experiment-package standard

Official SSI experiments use the common format defined in:

- [`CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md`](CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md)

Core flow:

```text
DECLARED SCOPE
-> FROZEN CONTRACT
-> ACCEPTANCE CRITERIA
-> MICROSTEP PLAN
-> MANIFEST
-> SHA256
-> KILO PRE-RUN VERIFY
-> REAL BODY EXECUTION
-> STEP RECEIPT
-> CHECKPOINT
-> FAILURE / INTERRUPTION / RECOVERY PRESERVED
-> PASS / FAIL / INCONCLUSIVE
-> SANITIZED PUBLIC EXPORT
-> PUBLICATION FIREWALL
```

One BODY receives one independent package/evidence chain. A later cross-BODY analysis may compare closed results but must not rewrite them.

## Failure and repair policy

A failure is not removed because a later retest passes.

```text
FAIL
-> preserve evidence
-> identify root cause
-> repair
-> new version/retest where required
-> preserve both outcomes
```

Infrastructure failures are classified separately where evidence permits, for example:

```text
SOFTWARE_FAILURE
INFRASTRUCTURE_FAILURE_CONFIRMED
INFRASTRUCTURE_FAILURE_SUSPECTED
NETWORK_FAILURE
UNKNOWN_CAUSE
```

Kilo, Ollama, interface or host restarts may resume a frozen procedure from the last valid checkpoint when no frozen input, acceptance rule, tested logic or supplied answer changes.

## Public/private publication boundary

```text
PUBLIC
= protocols
+ package IDs
+ SHA-256 references
+ sanitized manifests/evidence
+ PASS / FAIL / INCONCLUSIVE
+ timing and hardware summaries
+ route classes
+ failure/recovery lineage
+ claim boundaries

PRIVATE
= SSI source
+ Micronetwork source
+ Router V10 implementation
+ ISKRA implementation
+ ROBERT private source
+ private file tree
+ raw private prompts/memory/config
+ local private paths
+ credentials/secrets
+ operational reviewer endpoint
```

The public evidence flow uses a positive allowlist and pre-push publication firewall. Broad staging such as `git add .` / `git add -A` is not part of the canonical evidence-publication path.

## Current validated / recorded milestones

### BODY_FROZEN T0 — 2026-09-05

```text
BODY_FROZEN_TOTAL_FILES = 1781
BODY_FROZEN_PYTHON_FILES = 587
CONTINUUM = CLOSED
CONTINUUM_TESTS = 23/23 PASS
MAIN_SCENARIOS = 22/22 PASS
E2E_CLOSURE = 19/19 PASS
FINAL_GUARD = 26/26 PASS
ACTIVE_FAILURES = 0
OPEN_BLOCKERS = 0
MICRONETWORKS = 8
MODULES = 8
LAYERS = 3
ROUTER_V10 = ACTIVE
```

### BODY ISKRA start state — 2026-09-06

```text
AGENTS = 6
START_STATE_QA_PER_AGENT = 8/8 PASS
GROUP_START_STATE_QA = 48/48 PASS
VERIFIED_NEW_EXPERIENCES_AT_T0 = 0 per agent
PENDING_NEW_EXPERIENCES_AT_T0 = 0 per agent
```

### TEST 5 — latest closed development validation

```text
STAGE_12 = SUPERSEDED
STAGE_13_AUDIT_RETEST = PASS
TEST5_ACCEPTANCE = 29/29 PASS
ROOT_CONTROL = 111/111 PASS
ROOT_RUNTIME_BRIDGE = 338/338 PASS
ROBERT_STABLE = 46/46 PASS
TOTAL = 524/524 PASS
OPEN_BLOCKERS = 0
```

These are scoped development-validation results, not claims of production readiness, AGI or consciousness.

## Predeclared research programs

Mechanism-test package front door:

- [`EXPERIMENT_PACKAGES_START_HERE.md`](EXPERIMENT_PACKAGES_START_HERE.md)
- [`PREDECLARED_7BODY_MICRONETWORK_V10_PACKAGES_20260908.md`](PREDECLARED_7BODY_MICRONETWORK_V10_PACKAGES_20260908.md)

21-experiment cross-domain program:

- [`EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md`](EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md)
- [`EXPERIMENT_EXECUTION_METHODOLOGY_20260906.md`](EXPERIMENT_EXECUTION_METHODOLOGY_20260906.md)

Post-21 continuation:

- [`POST21_COMPETENCE_CONSOLIDATION_AND_NOVEL_TRANSFER_PROTOCOL_20260907.md`](POST21_COMPETENCE_CONSOLIDATION_AND_NOVEL_TRANSFER_PROTOCOL_20260907.md)
- [`POST21_RESEARCH_PHASE_INDEX_20260907.md`](POST21_RESEARCH_PHASE_INDEX_20260907.md)
- [`POST21_TRANSFER_MECHANISM_EVOLUTION_DRONES_HUMANOID_PROTOCOL_20260907.md`](POST21_TRANSFER_MECHANISM_EVOLUTION_DRONES_HUMANOID_PROTOCOL_20260907.md)

External reviewer/falsification protocol:

- [`LIVE_EXTERNAL_REVIEW_SESSION_PROTOCOL_20260907.md`](LIVE_EXTERNAL_REVIEW_SESSION_PROTOCOL_20260907.md)

## Canonical ROBERT continuity

Canonical ROBERT is a continuous engineering/execution line. Cleaning/freeze operations for BODY_FROZEN or BODY ISKRA experiment branches do not erase ROBERT's previous engineering history, TEST 1 -> TEST 5 lineage or private retained competence/tooling history.

See [`ROBERT_CANONICAL_CONTINUITY_VS_EXPERIMENTAL_RESET_20260906.md`](ROBERT_CANONICAL_CONTINUITY_VS_EXPERIMENTAL_RESET_20260906.md).

## Claim boundaries

SSI V5 does **not** currently claim that:

- it is proven AGI or conscious;
- every mechanism is production-ready;
- V10 is universally faster or more accurate than other systems;
- the 14 training packages have already passed;
- `TRAINED_START_S2` already exists for all seven lines;
- the seven mechanism tests have already passed;
- the complete final 21-run program has passed;
- the consolidated post-21 BODY already exists or is superior;
- ISKRA long-term divergence is already demonstrated;
- drones or humanoids are already validated physical deployments;
- Kilo is an independent scientific auditor;
- a cryptographic hash proves scientific correctness;
- a live reviewer session is equivalent to independent replication.

## Start here

1. [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) — grant/technical reviewer entry.
2. [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md) — current public truth and boundaries.
3. [`TRAINING_PACKAGES_START_HERE.md`](TRAINING_PACKAGES_START_HERE.md) — pre-experiment training.
4. [`EXPERIMENT_PACKAGES_START_HERE.md`](EXPERIMENT_PACKAGES_START_HERE.md) — mechanism-test precommitments.
5. [`CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md`](CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md) — execution/evidence standard.
6. [`REVIEWER_LIVE_INTERFACE_20260907.md`](REVIEWER_LIVE_INTERFACE_20260907.md) — live read-only observability.
7. [`BODY_FROZEN_T0_PRE_ISKRA.md`](BODY_FROZEN_T0_PRE_ISKRA.md) — frozen baseline.
8. [`BODY_ISKRA_6X_T0.md`](BODY_ISKRA_6X_T0.md) — six independent start-state descendants.
9. [`V10_PREDICTIVE_ROUTING.md`](V10_PREDICTIVE_ROUTING.md) — stateful predictive competence/recovery routing.
10. [`evidence/README.md`](evidence/README.md) — public evidence index.

The intended standard is simple: **predeclare what will be tested, preserve what actually happened, never hide a failure, never publish private implementation by accident, and make stronger claims only when stronger evidence exists.**
