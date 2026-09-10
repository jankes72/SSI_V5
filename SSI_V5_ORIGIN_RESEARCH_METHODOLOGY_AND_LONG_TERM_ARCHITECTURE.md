# SSI V5 — Origin, Research Methodology, System Evolution, and Long-Term Architecture

**Recorded:** 2026-09-09  
**Last status sync:** 2026-09-10 / after BODY_FROZEN TRAIN01A Foundation closure  
**Status:** `PUBLIC PROJECT PROVENANCE / RESEARCH ROADMAP / CLAIM-BOUNDED`  
**Author / architecture:** Paweł Jankiewicz (`jankes72`)  
**Repository role:** public evidence-indexed research mirror; proprietary implementation remains private

**Current status synchronization — 2026-09-10:** `BODY_FROZEN TRAIN01A FOUNDATION` is now `CLOSED / VERIFIED PASS`: `48/48 PASS`, `16/16 blind validations determinate PASS`, `16/16 checkpoints`, `T0 integrity PASS`, and `BODY_FROZEN_FOUNDATION_S1` has been created. Historical outcomes remain preserved. For the canonical living status, see [`CURRENT_RESEARCH_ROADMAP_20260910.md`](CURRENT_RESEARCH_ROADMAP_20260910.md), [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md), and [`evidence/BODY_FROZEN_TRAIN01A_FINAL_CLOSURE_20260910.md`](evidence/BODY_FROZEN_TRAIN01A_FINAL_CLOSURE_20260910.md).

---

## 1. Purpose of this document

SSI V5 was not created as a finished architecture that was fully specified in advance and then implemented once.

It emerged through a long sequence of concrete problems, experiments, failed approaches, repairs, measurements, reorganizations, and increasingly structured attempts to understand which mechanisms were actually useful.

This document preserves the **technical and research provenance of SSI V5**.

It is not intended to present the author as someone who knew the final design from the beginning. It is also not intended to imply that standard statistical, machine-learning, software-engineering, or AI techniques used along the way were invented by the author.

Its purpose is to make the development lineage inspectable:

- where the project started;
- which practical problems forced architectural changes;
- which mechanisms exist today;
- which mechanisms have been validated only in a declared scope;
- which experiments were predeclared before their outcomes were known;
- which parts remain planned future architecture;
- how failures and superseded approaches are preserved;
- why proprietary source code can remain private while claims remain publicly reviewable at the evidence level.

The public SSI V5 repository is intentionally an **evidence-indexed research mirror, not a source-code distribution**. See the main [`README.md`](README.md).

---

## 2. Evidence and status vocabulary

To avoid mixing implementation facts, experimental results, and future plans, this document uses explicit status categories.

```text
HISTORICAL
= preserved earlier technology, code lineage, or development stage

EXISTS
= the mechanism is implemented

VALIDATED
= the mechanism passed a defined test in a declared scope

PRIVATE / PUBLIC EVIDENCE PENDING
= the author reports the mechanism as operational privately,
  but sufficient public evidence is not yet published here

PREDECLARED
= the experiment/protocol was recorded before its outcome was known

PLANNED
= intended future architecture or integration

UNKNOWN
= the outcome is not yet known

PUBLIC EVIDENCE
= sanitized reviewer-safe evidence that can be inspected publicly

PRIVATE IMPLEMENTATION
= proprietary source, internal memory, raw configuration,
  internal prompts/data, or implementation details not published here
```

The governing rule is simple:

> A planned capability is not described as existing; an existing capability is not automatically described as validated; internal validation is not described as external certification.

---

## 3. The project began with a problem, not with a claim about general intelligence

The earliest long-running problem behind SSI was sports analysis, especially football match analysis, bookmaker-market behavior, and exact-score prediction.

The work began with practical questions rather than a theory of general AI.

Over time, successive programs collected and compared many forms of information, including:

- teams and players;
- form and statistics;
- contextual information;
- time;
- bookmaker odds;
- changes in odds;
- movement amplitude;
- rate of change;
- pairwise relationships between prices/odds;
- repeated historical configurations.

A particularly important direction became the **temporal behavior of the odds themselves**, not merely their current value.

Historical systems developed custom representations of those movements, grouping methods, and ways to compare a current market configuration with earlier cases.

The work also used established methods including Random Forest, neural networks, Poisson models, Dixon-Coles-style football modeling, correlations, and feature ranking.

These standard methods are not claimed as original inventions.

The authorial contribution being explored is primarily the system-level combination of:

```text
PROBLEM REPRESENTATION
-> MULTIPLE ANALYTICAL VIEWS
-> HISTORY
-> ERROR OBSERVATION
-> MEMORY
-> TEACHERS
-> WORLD STRUCTURE
-> AGENTS
-> COMPETENCE LIFECYCLE
```

---

## 4. A turning point: a wrong answer can still contain useful structure

An important historical shift was moving beyond the question:

> “Was the prediction correct?”

and asking instead:

> **“What did the model detect if it repeatedly grouped these cases together?”**

A model could select the wrong final class while still identifying a non-random subgroup of cases with a characteristic real outcome distribution.

For example, a small group classified toward one score or result direction could later show a strong tendency toward an opposite outcome. Instead of discarding the model as completely useless, the error could be treated as **information about the structure of the data space**.

This became an important conceptual predecessor of later ideas such as:

- error memory;
- inverse patterns;
- alternative competence;
- Challenger behavior;
- recovery;
- learning from how a model fails, not only from whether it wins.

The claim is deliberately narrow: this was a development insight that shaped later SSI design. It is not presented as a universal ML law.

---

## 5. Learning programming by maintaining increasingly complex systems

The author of SSI V5 is self-taught.

Early systems were created mainly with the tools available and understood at the time: Python, large sequential scripts, and CSV-based data exchange.

Some historical implementations became very large and monolithic. Execution order, file dependencies, intermediate outputs, restarts, failures, and resource limits often had to be planned manually.

A recurring practical checklist was effectively:

```text
WHAT RUNS FIRST?
WHAT MUST FINISH BEFORE THE NEXT STEP?
WHICH FILE IS THE INPUT?
WHICH FILE IS THE OUTPUT?
WHAT HAPPENS IF A PROCESS FAILS?
WHAT CAN RESUME?
WHAT MUST RESTART?
```

Much of this planning was initially written on paper.

Constrained personal hardware made execution time, RAM/VRAM use, process ordering, and restart behavior impossible to ignore.

Later SSI architecture became more structured: modules, hooks, status records, checkpoints, CONTINUUM, LAB, Micronetworks, routing, evidence chains, and frozen/versioned states were added over time.

The earlier monolithic stages are therefore not hidden. They are part of the explanation for why the later architecture exists.

---

## 6. From one prediction model to Teacher, memory, and laboratory systems

As the sports systems evolved, a single model output stopped being the end of the process.

Historical implementations began retaining and comparing information such as:

```text
PREDICTION
+ VERIFIED OUTCOME
+ CONFIDENCE
+ ERROR
+ CLASS BEHAVIOR
+ FEATURE IMPORTANCE
+ MODEL GENERATION
+ OBSERVATION HISTORY
+ RULES / CONCLUSIONS
```

The historical sports lineage includes a cognitive Teacher concept, knowledge memory, world hierarchy, feature analysis, and a laboratory that evaluates model behavior after training.

A particularly important design pattern was separating part of the data from direct training and using it for later observation of model behavior. The goal was not only to fit a model, but to learn **how the fitted model behaves on data it did not learn from directly**.

This helped produce a broader principle:

> A model should not only answer. The surrounding system should learn when the model is useful, when it fails, how it fails, and what kind of knowledge can be extracted from those failures.

---

## 7. Football World — the first mature world lineage

Football World is the oldest and most mature domain lineage in the project.

Its main research value is the presence of an **external real-world outcome** that the agent cannot choose after the fact.

Conceptually:

```text
DATA
-> TEACHER
-> MODEL GENERATION
-> OBSERVATION
-> LAB
-> AGENT
-> PREDICTION
-> AUDIT / DIRECTOR LAYER
-> REAL MATCH RESULT
-> VERIFIED OUTCOME
-> EXPERIENCE
-> NEXT DECISION
```

The agent does not get to declare its own success. The result arrives from outside the agent.

The world-oriented architecture also motivates comparison of entire decision lineages rather than only isolated predictions:

```text
AGENT
-> STRATEGY
-> DATASET
-> MODEL
-> GENERATION
-> PREDICTION
-> VERIFIED OUTCOME
```

This makes it possible to ask which model generations, data representations, Teacher states, confidence ranges, inverse patterns, and strategies were genuinely useful over time.

Football World is therefore treated as an **origin world** and a source of long-term methodological experience, not as evidence that the same mechanisms automatically transfer to unrelated domains.

---

## 8. Hermes — Teacher as a changing source of knowledge

A planned extension of the historical Teacher lineage is the **Hermes** concept.

Hermes is not intended to be a static encyclopedia that always returns the same object.

A Hermes may maintain its own:

```text
DOMAIN CORPUS
MODEL GENERATIONS
OUTCOME MEMORY
LAB OBSERVATIONS
METADATA
CONFIDENCE HISTORY
ERROR HISTORY
INVERSE PATTERNS
```

Two agents asking “the same Hermes” at different points in time may therefore receive different generations of knowledge.

One agent may preserve:

```text
HERMES GENERATION G17
```

while another later uses:

```text
HERMES GENERATION G24
```

Between those generations, new outcomes, recalculations, data, rules, rankings, or even useful direction reversals may have appeared.

This creates **path dependence**:

> An agent’s future can depend not only on what it learned, but on when it learned it, from which knowledge source, and from which generation of that source.

This is a planned research architecture. It is not claimed here that the full Hermes system is already externally validated.

---

## 9. Agent inventory and private cognitive biography

The broader SSI design gives importance to what an agent preserves for later use.

A historical analogy comes from the earlier Moral AI work, where an entity could have its own inventory, memory, relationships, and state.

In the newer agent/world architecture, an agent’s “pocket” or private inventory may conceptually hold items such as:

```text
A HERMES KNOWLEDGE SNAPSHOT
A DATASET
METADATA
A MODEL
A STRATEGY
A LAB OBSERVATION
A VERIFIED COMPETENCE
A RESULT FROM A PRIOR EXPERIMENT
```

The important point is not the metaphor of a pocket. The important point is **versioned ownership of experience**.

Two agents that began from the same mechanical substrate may later possess different histories because they preserved different artifacts, trusted different sources, experienced different failures, or learned at different points in time.

This creates what can be described as different **cognitive biographies**.

---

## 10. ISKRA — six independent longitudinal histories

SSI V5 currently records six independent BODY ISKRA descendants of the same frozen BODY T0.

Their initial orientations are:

```text
NICE
GUARDIAN
JUSTICE
EXPLORER
PRAGMATIST
SKEPTIC
```

The public start state is documented in [`BODY_ISKRA_6X_T0.md`](BODY_ISKRA_6X_T0.md).

The public repository does **not** claim that long-term divergence has already been demonstrated.

The longitudinal research question is prospective:

> Can a common mechanical substrate, combined with different explicit initial value/emotion priors and later independent experience, produce measurably different decision trajectories, interpretations of experience, competence histories, trust relationships, and social strategies?

The distinction matters:

```text
DIFFERENT T0 PRIORS = EXISTS / START STATE VALIDATED

LONG-TERM DIVERGENCE = RESEARCH QUESTION / NOT YET CLAIMED
```

---

## 11. A second longitudinal layer: emergent agency and autonomy observation

In addition to competence and routing experiments, SSI includes a longer-term research interest in **emergent autonomy of behavior**.

This should not be misrepresented as a simple “consciousness detector.”

The project currently does not claim AGI or consciousness. The public claim boundary explicitly rejects such a conclusion at the present stage.

A more defensible research question is:

> **In a persistent system with memory, different priors, relationships, tools, independent experience, and freedom to choose among allowed actions, do stable and previously unscripted strategies emerge?**

Observable categories may include:

- self-created strategies;
- unexpected use of available data;
- self-created metadata;
- changing trust in Teachers/Hermes sources;
- changing trust in other agents;
- unscripted collaboration;
- refusal or avoidance of collaboration;
- persistent preferences;
- revision of prior beliefs after verified outcomes;
- creation of new tools or intermediate representations;
- self-selection of new domains;
- continued respect for authority and safety boundaries.

Even if such behaviors are observed, they do **not** by themselves prove consciousness.

They can, however, provide measurable material for research into:

```text
EMERGENT AGENCY
AUTONOMY
PATH DEPENDENCE
CONTINUAL ADAPTATION
MULTI-AGENT BEHAVIOR
LONG-TERM MEMORY EFFECTS
```

Some exact held-out observation criteria may remain private to reduce behavioral contamination. If used for a formal claim, the relevant protocol and evidence boundary should still be recorded before interpretation.

---

## 12. The 21-experiment cross-domain program

The current controlled research program contains seven independent lines:

```text
BODY_FROZEN
+
6 x BODY ISKRA
```

Each line receives three experiments:

```text
A = DRONES
B = HUMANOID
C = A NEW DOMAIN SELECTED BY THAT SSI LINE
```

Total:

```text
7 x 3 = 21
```

The program was recorded before the complete outcome set exists. See [`EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md`](EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md).

Measurement categories include, where applicable:

```text
KNOWN / SIMILAR / NOVEL
REUSE
VERIFY / ADAPT
ALTERNATIVE COMPOSITION
FULL FLOW
LATENCY
FALSE REUSE
RECOVERY
COMPETENCE CREATION
CANDIDATE / CHALLENGER / CHAMPION CHANGES
```

A particularly important constraint is Experiment C: the author does not supply the expected domain selection. The corresponding SSI line selects its own third domain, and the selection itself becomes evidence.

No future PASS result is claimed in advance.

---

## 13. Micronetworks and Router V10

A core SSI research direction is to treat competence as an evolving set of specialized, evidence-linked units instead of forcing every problem through one identical expensive path.

The competence lifecycle includes:

```text
CANDIDATE
-> CHALLENGER
-> CHAMPION
```

Router V10 is designed to distinguish among state classes such as:

```text
KNOWN
SIMILAR
NOVEL
```

The intended logic is approximately:

```text
KNOWN
-> reuse verified competence when justified

SIMILAR
-> verify / adapt / compose

NOVEL
-> avoid unsafe blind reuse
-> deeper / full flow
-> candidate competence may be created only after evidence
```

Historical route-speed evidence is preserved in the repository, including scoped Test 3 results. Those results are not presented as proof that V10 is universally faster or more accurate than unrelated systems. See [`V10_PREDICTIVE_ROUTING.md`](V10_PREDICTIVE_ROUTING.md).

---

## 14. Post-21 competence consolidation

The 21 experiments are not the endpoint.

Before their complete outcomes were known, SSI V5 recorded a subsequent consolidation stage in [`POST21_COMPETENCE_CONSOLIDATION_AND_NOVEL_TRANSFER_PROTOCOL_20260907.md`](POST21_COMPETENCE_CONSOLIDATION_AND_NOVEL_TRANSFER_PROTOCOL_20260907.md).

The intended sequence is:

```text
21 EXPERIMENTS
-> COMPETENCE INVENTORY
-> FUNCTIONAL IDENTITY CHECK
-> DEDUPLICATION
-> CHAMPION ENRICHMENT
-> CHALLENGER ENRICHMENT
-> PROMOTION WHERE EVIDENCE SUPPORTS IT
-> NEW MICRONETWORK WHERE FUNCTIONALLY NOVEL
-> VERSIONED CONSOLIDATED BODY
-> 3 NEW TRANSFER DOMAINS
```

A dynamic name is not considered proof of a new competence.

Two differently named Micronetworks may be functionally equivalent. Conversely, similar names do not automatically imply the same function.

The consolidation process is therefore intended to preserve provenance while comparing **function, evidence, lifecycle state, and outcome history**.

Not every newly discovered skill becomes a Champion.

Negative evidence remains evidence.

This stage is **PREDECLARED**. Its final result is still unknown.

---

## 15. ROBERT — the continuous engineering and execution line

ROBERT is not one of the cleaned experimental BODY branches.

It is the canonical continuous engineering/execution line.

The repository explicitly distinguishes:

```text
CANONICAL ROBERT
= continuous engineering / execution history

BODY_FROZEN / BODY ISKRA
= controlled experimental branches
```

See [`ROBERT_CANONICAL_CONTINUITY_VS_EXPERIMENTAL_RESET_20260906.md`](ROBERT_CANONICAL_CONTINUITY_VS_EXPERIMENTAL_RESET_20260906.md).

ROBERT retains the engineering lineage associated with TEST 1 through TEST 5 rather than being reset when experimental copies are cleaned.

Its intended operational role includes:

```text
EYES
HANDS
EXECUTION
TOOLS
PROGRAMMING
PRACTICAL INTERACTION
```

Its longer-term role is broader: experimentally validated practical competence from agent laboratories may later be consolidated and integrated into ROBERT under explicit promotion and regression gates.

That does not mean every experimental discovery is automatically copied into ROBERT.

The intended rule is:

```text
AGENT DISCOVERY
-> EVIDENCE
-> FUNCTIONAL IDENTITY
-> LIFECYCLE REVIEW
-> REGRESSION / ACCEPTANCE
-> VERSIONED ROBERT INTEGRATION
```

---

## 16. DIRECTOR — coordination, comparison, and long-term organizational memory

DIRECTOR is a separate canonical engineering line.

The immutable frozen engineering baseline remains `DIRECTOR_FROZEN_C0`, documented in [`DIRECTOR_MAINLINE_BODY_INTEGRATION_20260908.md`](DIRECTOR_MAINLINE_BODY_INTEGRATION_20260908.md). The current post-Foundation Director descendant is now `DIRECTOR_FOUNDATION_S1`, created by the closed TRAIN08A procedure.

Within the declared C0 engineering scope, public evidence records the validated local runtime, persistence/checkpoint behavior, CONTINUUM, LAB, Micronetwork and Router V10 integration, persistent conversation memory, local owner control panel, shared read-only observability, hardware/model status, and other scoped checks.

The final C0 record includes:

```text
FINAL PANEL / SYSTEM CHECKS = 27/27 PASS
SELECTED PYTEST VALIDATION = 19/19 PASS
INDEPENDENCE VALIDATION = PASS
FREEZE INTEGRITY = VERIFIED
```

These are internal engineering-validation results, not external certification or production-readiness evidence.

### 16.1 DIRECTOR TRAIN08A — first closed Foundation acquisition

After the original recording of this long-term document, the separate Director training line executed and formally closed its first Foundation stage:

```text
TARGET = DIRECTOR_FROZEN_C0
TRAINING PHASE = TRAIN08A FOUNDATION
RESULT = CLOSED / VERIFIED PASS
UNIQUE STEPS = 48
STEP OUTCOMES = 48 PASS / 0 FAIL / 0 INCONCLUSIVE
BLIND VALIDATIONS = 16/16 PASS
CHECKPOINTS = 16
FINAL CHECKPOINT = CHECKPOINT_16
VALID JSON EVENT RECORDS = 67
OUTPUT = DIRECTOR_FOUNDATION_S1 CREATED
HELD-OUT CONTAMINATION CHECK = PASS
MATERIAL INTEGRITY VIOLATION = false
```

Execution provenance was preserved rather than rewritten as uninterrupted:

```text
Kiro / kiro-cli / Auto cloud model = steps 01-17
Kilo / kilo-cli / free model = steps 18-48
handoff boundary = step 17 -> step 18
executor_transition_step = 18
```

Kiro stopped accepting requests because its monthly usage allowance was exhausted. This was an external service interruption, not a TRAIN08A acceptance failure and not a model switch selected because of a poor Director outcome.

At takeover, `PROGRESS.json` lagged behind the append-only event evidence: it reported step 15 while steps 16-17 were already preserved as PASS. Kilo reconstructed progress from the evidence and resumed from the first unrecorded step 18 rather than restarting the run or deleting the earlier Kiro history.

The final event-log accounting is:

```text
1 INIT
49 step-event records representing 48 unique steps
16 CHECKPOINT records
1 EXECUTOR_HANDOFF
= 67 valid JSON records
```

Step 47 has two preserved PASS records because a test-oracle arithmetic expectation was corrected from `210.0` to `190.0` (`50 + 100 + 40 = 190`). The original record remains preserved.

### 16.2 Predeclaration chronology and rebuild integrity boundary

The original Director Foundation package was publicly predeclared before the final outcome was known:

```text
PREDECLARED PACKAGE
SSI_TRAIN08A_DIRECTOR_FOUNDATION_V1_20260909

ZIP_SHA256
76847299993eb24090921b73de5e0bacb1bc021859327e0cebabf66a5526f739

FROZEN_MANIFEST_SHA256
eb38c5f8d9f914382202d410923c729bbdc3a37439e8450f85d78245a0ec3a27

FOUNDATION_CURRICULUM_SHA256
61a3069ce68d19c64d4ae7c5ebc730d04283d81b2e534f487c3fd5063d9b75b8

PREDECLARATION COMMIT
5433200ec2a1b10804050b03df9cf151a26bde0a
2026-09-09T00:00:18Z
```

The final execution result was published later:

```text
FINAL EXECUTION RECORD COMMIT
c7ebcfceda02cee74dd502180ea3097a189dd482
2026-09-09T15:30:27Z
```

The continued execution package is identified in the final records as:

```text
SSI_TRAIN08A_DIRECTOR_FOUNDATION_V1_20260909_REBUILT_FOR_KILO
```

The current public repository does **not** publish a separate exact ZIP SHA-256 or byte-by-byte/file-by-file diff for that rebuilt archive. Therefore SSI does not claim that the `REBUILT_FOR_KILO` archive is publicly proven byte-for-byte identical to the original predeclared ZIP.

The supported public statement is narrower: the TRAIN08A family, target, 48-step Foundation scope and curriculum identity were predeclared before the final result; the executor handoff and final evidence were preserved; the final evidence reports no material integrity violation; exact rebuilt-archive byte equivalence is not independently established by a separately published rebuilt hash/diff.

See:

- [`DIRECTOR_TRAINING_START_HERE.md`](DIRECTOR_TRAINING_START_HERE.md)
- [`PREDECLARED_DIRECTOR_TRAINING_PACKAGES_20260909.md`](PREDECLARED_DIRECTOR_TRAINING_PACKAGES_20260909.md)
- [`DIRECTOR_TRAIN08A_LIVE_EXECUTION_RECORD_20260909.md`](DIRECTOR_TRAIN08A_LIVE_EXECUTION_RECORD_20260909.md)
- [`DIRECTOR_TRAIN08A_FINAL_EXECUTION_RECORD_20260909.md`](DIRECTOR_TRAIN08A_FINAL_EXECUTION_RECORD_20260909.md)
- [`evidence/DIRECTOR_TRAIN08A_FINAL_CLOSURE_20260909.md`](evidence/DIRECTOR_TRAIN08A_FINAL_CLOSURE_20260909.md)
- [`evidence/DIRECTOR_TRAIN08A_REBUILD_INTEGRITY_RECORD_20260909.md`](evidence/DIRECTOR_TRAIN08A_REBUILD_INTEGRITY_RECORD_20260909.md)

### 16.3 Current Director lineage and future role

The evidence-backed Director line is now:

```text
DIRECTOR_FROZEN_C0
-> TRAIN08A FOUNDATION = CLOSED / VERIFIED PASS / 48 OF 48 PASS
-> DIRECTOR_FOUNDATION_S1 = CREATED
-> TRAIN08B LEGO + MICRONETWORK + V10 PRACTICUM = NEXT / PREDECLARED / NOT YET EXECUTED
-> DIRECTOR_TRAINED_START_S2 = FUTURE / NOT YET CLAIMED
```

The intended future Director role is to compare and coordinate information across:

```text
AGENTS
HERMES GENERATIONS
MODELS
DATASETS
STRATEGIES
MICRONETWORKS
WORLD OUTCOMES
RESOURCE COST
LONG-TERM EVIDENCE
CAPITAL / OPERATIONAL STATE
```

The current repository still explicitly states that Director does **not yet control the experimental ISKRA lines**. Later Director -> ROBERT -> World -> Agent integration remains a future engineering stage.

---

## 17. Director as a reputation source, not an oracle

In a future multi-agent environment, Director may publish rankings or evidence summaries about:

```text
AGENTS
TEACHERS / HERMES SOURCES
STRATEGIES
MODELS
COMPETENCE RECORDS
WORLDS
```

The ranking should not automatically become a command.

An agent may receive information such as:

```text
HERMES A
historical evidence = X

AGENT B
reliability in domain = Y

STRATEGY C
recent outcome record = Z
```

and independently decide whether to use it.

That opens a stronger research question:

> **Does evidence-based reputation influence later trust, cooperation, source selection, and strategy without directly scripting the agent’s answer?**

This is planned research architecture, not a completed longitudinal result.

---

## 18. Emerging Worlds — data accumulation before strong claims

Football World is not intended to remain the only world.

Additional long-running data worlds are being accumulated.

One private implementation line focuses on capital-market, currency, and cryptocurrency data. The author reports that this data collection is still young compared with the football lineage and is therefore being allowed to accumulate before strong claims are made.

This is an important methodological principle:

> **The existence of code is not treated as permission to claim mature knowledge when the world has not yet accumulated enough history.**

The intended public status for such worlds is therefore:

```text
EMERGING WORLD
= DATA ACCUMULATION
= MODEL / RELATIONSHIP CANDIDATES MAY EXIST
= STRONG LONGITUDINAL CLAIMS NOT YET MADE
```

Future worlds should be documented with the same separation between collection, training, held-out observation, outcome verification, and later claims.

---

## 19. Dynamic agent space and Moral AI lineage

A further planned stage extends concepts developed historically in the author’s Moral AI work.

The environment is not intended to be only a table of data. It may contain explicit spaces such as rooms and laboratories in which agents can act, meet, cooperate, refuse cooperation, preserve private resources, and build relationships over time.

Conceptually, the environment may include:

```text
ROOMS
LABORATORIES
TEACHERS
AGENTS
RELATIONSHIPS
PRIVATE INVENTORY
EVENTS
MEMORY
ACCESS CONDITIONS
CHANGING TRUST
```

The research value comes from **not fully scripting what social or knowledge strategy must emerge**.

The environment can expose possibilities without telling an agent exactly how to exploit them.

For example, access to a key, a Teacher, a dataset, metadata, or another agent is not equivalent to supplying the intended solution path.

The result of that freedom is unknown and is precisely what makes the longitudinal experiment useful.

---

## 20. BODY_FROZEN 2.0 — planned R&D layer

After competence consolidation, an important planned descendant is provisionally described as **BODY_FROZEN 2.0**.

Current status:

```text
PLANNED
```

It is not claimed as a completed current component.

Its intended role is dual.

### 20.1 External R&D

BODY_FROZEN 2.0 is intended to apply validated SSI competence and development mechanisms to external domains such as:

```text
DRONES
HUMANOID ROBOTICS
AUTOMATION
INDUSTRIAL SYSTEMS
OTHER NEW TECHNOLOGY DOMAINS
```

The intended pattern is:

```text
COMPANY / DOMAIN PROBLEM
-> AVAILABLE VERIFIED SSI COMPETENCE
-> IDENTIFY MISSING COMPETENCE
-> R&D
-> PROTOTYPE
-> TEST
-> EVIDENCE
-> VERSIONED IMPLEMENTATION
```

The intended claim is not “SSI already knows every domain.”

The research and engineering question is whether a validated competence substrate can help build and verify systems in domains that were not part of the original baseline.

### 20.2 Internal SSI R&D

The same development mechanism is intended to be applied back to SSI itself.

BODY_FROZEN 2.0 should not be allowed to silently rewrite the running SSI Champion.

Instead:

```text
NEW IDEA
-> CANDIDATE UPGRADE
-> SANDBOX
-> TEST
-> EVIDENCE
-> COMPARE WITH CURRENT SYSTEM
-> REJECT / CHALLENGER / PROMOTE
-> VERSIONED SSI DESCENDANT
```

This would make internal SSI evolution use the same evidence discipline that SSI R&D uses for external projects.

---

## 21. Technology radar and external knowledge intake

The author also describes a private technology-radar workflow intended to periodically monitor newly released programs, models, libraries, and techniques from public technical sources.

The author’s current intended cadence is approximately four checks per day.

Current public status should be treated conservatively as:

```text
PRIVATE OPERATIONAL / PUBLIC EVIDENCE PENDING
```

and its deeper R&D integration as:

```text
PLANNED
```

The intended purpose is not merely link collection.

The longer loop is:

```text
NEW TOOL / MODEL / TECHNIQUE
-> RECORD
-> CLASSIFY
-> RELATE TO EXISTING SSI PROBLEMS
-> CONNECT POSSIBLE USE CASES
-> CREATE CANDIDATE APPLICATION
-> R&D TEST
-> EVIDENCE
-> ADOPT / REJECT
```

A newly discovered technology should never be inserted directly into the canonical SSI core only because it appears promising.

It must still pass versioning, testing, and evidence gates.

---

## 22. GitHub as architectural provenance memory

The public GitHub repository has two intended audiences.

The first is human:

```text
REVIEWERS
GRANT EVALUATORS
RESEARCHERS
FUTURE COLLABORATORS
DOMAIN EXPERTS
```

The second, in the long-term architecture, is DIRECTOR itself.

The repository is therefore intended to become more than a portfolio.

It records a versioned public history of:

```text
WHAT EXISTED
WHAT FAILED
WHAT WAS REPAIRED
WHAT WAS SUPERSEDED
WHAT WAS PREDECLARED
WHAT WAS TESTED
WHAT PASSED
WHAT DID NOT PASS
WHY A MECHANISM EXISTS
WHICH VERSION INTRODUCED IT
WHAT THE CLAIM BOUNDARY WAS AT THAT TIME
```

The future value is that Director should be able to ask not only:

> “How does SSI work now?”

but also:

> **“Why does SSI work this way, and what evidence caused the architecture to change?”**

The public repository is not intended to be the only memory source. A future Director knowledge stack may combine:

```text
PUBLIC GITHUB HISTORY
+
PRIVATE VERSIONED EVIDENCE
+
CONTINUUM
+
RUNTIME STATE
+
CHECKPOINTS
+
PRIVATE MEMORY
-> DIRECTOR KNOWLEDGE
```

The public GitHub remains the sanitized, externally inspectable provenance layer.

---

## 23. Why failures must remain visible

If a future system is expected to reason about its own engineering history, a repository containing only successful results would be incomplete and potentially misleading.

FAIL is information.

SUPERSEDED is information.

A failed repair is information.

A regression is information.

The canonical experiment methodology therefore requires failure, interruption, repair, recovery, and rerun history to remain part of the lineage. See [`CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md`](CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md).

A future Director or R&D component should be able to recover a chain such as:

```text
THIS MECHANISM WAS TRIED
-> THIS VERSION FAILED
-> FOR THIS RECORDED REASON
-> VERSION B REPLACED IT
-> VERSION B PASSED THIS DECLARED TEST
-> ITS CLAIM BOUNDARY WAS STILL LIMITED TO THIS SCOPE
```

Without such history, an adaptive system could repeatedly rediscover its own old mistakes.

The TRAIN08A Kiro -> Kilo handoff and the preserved step-47 oracle correction are current concrete examples of this rule: interruption and correction remain part of provenance even though the final scoped result is PASS.

---

## 24. Official experiments are package-driven, not manually improvised runs

One of the most important methodological changes in SSI is the move away from manually steering an official experiment step by step after execution has begun.

Official SSI experiments use a versioned package standard.

The canonical sequence is documented in [`CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md`](CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md):

```text
EXPERIMENT IDEA / EXTERNAL CHALLENGE
-> DECLARED SCOPE
-> FROZEN CONTRACT
-> ACCEPTANCE CRITERIA
-> MICROSTEP PLAN
-> MANIFEST
-> SHA256 / INTEGRITY DIGEST
-> DECLARED EXECUTOR PRE-RUN VERIFICATION
-> REAL SSI BODY / TARGET EXECUTION
-> STEP RECEIPTS
-> CHECKPOINTS
-> FAILURE / INTERRUPTION / RECOVERY PRESERVED
-> PASS / FAIL / INCONCLUSIVE
-> SANITIZED PUBLIC EXPORT
```

Kilo is the normal procedural executor in the current package methodology.

Kilo is **not** presented as an independent scientific auditor.

TRAIN08A is a documented execution-continuity exception: Kiro executed steps 01-17 and Kilo executed steps 18-48 after the Kiro monthly usage-limit interruption. The executor transition is part of the evidence and is not rewritten as an uninterrupted single-executor run.

A procedural executor must not silently:

```text
CHANGE THE RESEARCH QUESTION
CHANGE ACCEPTANCE CRITERIA
MODIFY TESTED SSI LOGIC TO FORCE PASS
DELETE FAILURES
SUPPLY THE EXPECTED ANSWER
REWRITE HISTORY AFTER THE RESULT
```

---

## 25. Why packages and hashes matter

A manually entered terminal run can be changed accidentally by:

```text
A DIFFERENT COMMAND
A TYPO
A DIFFERENT INPUT
A DIFFERENT ORDER
A CHANGED PARAMETER
AN EXTRA HINT
```

The package/manifest/hash model reduces that ambiguity.

A cryptographic hash does **not** prove scientific correctness.

It does provide an integrity reference for artifact identity when the executed artifact itself is hash-identified:

> “This is the previously identified artifact associated with this execution record.”

If an executor-specific rebuild, repackaging, recovery artifact, or continuation package is used, its identity and relationship to the predeclared package must be recorded separately. A hash for the original archive must not be silently reused as proof of byte identity for a rebuilt archive.

TRAIN08A is a concrete example. The original predeclared ZIP and frozen manifest have public SHA-256 references, while the final execution record uses the label `...REBUILT_FOR_KILO`. Because the repository currently does not publish a separate rebuilt ZIP hash/diff, SSI does not claim byte-for-byte equivalence between those two archives. See [`evidence/DIRECTOR_TRAIN08A_REBUILD_INTEGRITY_RECORD_20260909.md`](evidence/DIRECTOR_TRAIN08A_REBUILD_INTEGRITY_RECORD_20260909.md).

That distinction is explicitly preserved in the current methodology.

---

## 26. Externally proposed challenge experiments

The current standard already allows an external researcher, reviewer, partner, or challenge provider to propose:

```text
CHALLENGE
TEST CASES
FAILURE CONDITIONS
ACCEPTANCE CRITERIA
MEASUREMENTS
```

After agreement and freezing, execution follows the same canonical package methodology.

A safe external model is an **External Challenge Package**, not the direct execution of arbitrary untrusted code on private SSI machines.

The intended sequence is:

```text
EXTERNAL EXPERT
-> CHALLENGE DEFINITION
-> SAFETY / FORMAT REVIEW
-> FROZEN CONTRACT
-> PACKAGE / MANIFEST
-> SHA256
-> PUBLIC PRECOMMIT / IDENTIFIER WHERE APPROPRIATE
-> SCHEDULED RUN
-> DECLARED PROCEDURAL EXECUTOR
-> SSI BODY / TARGET
-> LIVE READ-ONLY OBSERVATION
-> PASS / FAIL / INCONCLUSIVE
```

The external party controls the challenge difficulty and falsification criteria within the agreed scope, while the execution boundary remains protected.

External reviewers are explicitly allowed to disagree with SSI, attempt to break it, or design stronger tests.

---

## 27. Live reviewer interface

SSI V5 includes a separate reviewer-facing observability layer.

Its core security principle is:

```text
OBSERVE
!=
CONTROL
```

The shared reviewer interface may expose sanitized information such as:

```text
BODY IDENTITY
RUNTIME STATUS
MISSION / EXPERIMENT STAGE
CHECKPOINTS
CONTINUUM
LAB
ROUTING CLASS
FAILURE / RECOVERY EVENTS
RESOURCE UTILIZATION
PUBLIC EVIDENCE REFERENCES
FINAL STATUS
```

It may also provide an informational question channel.

It must not expose:

```text
MISSION CREATION / EXECUTION
KILO CONTROL
ROOT
RUNTIME CONFIGURATION WRITES
ARBITRARY CODE EXECUTION
PRIVATE FILESYSTEM ACCESS
PRIVATE MEMORY
PRIVATE SOURCE CODE
SECRETS / TOKENS / CREDENTIALS
```

See [`REVIEWER_LIVE_INTERFACE_20260907.md`](REVIEWER_LIVE_INTERFACE_20260907.md).

The local owner/operator control panel and the shared reviewer interface remain deliberately separate security surfaces.

---

## 28. Externally witnessed live sessions

A separate predeclared protocol exists for externally witnessed sessions: [`LIVE_EXTERNAL_REVIEW_SESSION_PROTOCOL_20260907.md`](LIVE_EXTERNAL_REVIEW_SESSION_PROTOCOL_20260907.md).

The intended session includes:

```text
SCHEDULED DATE / TIME
PRIVATE REVIEWER ACCESS
EXPERIMENT IDENTITY
BODY IDENTITY
PACKAGE IDENTITY
HASH / MANIFEST
DECLARED PROCEDURAL EXECUTOR
READ-ONLY LIVE OBSERVATION
FAILURE / RECOVERY PRESERVATION
FINAL PASS / FAIL / INCONCLUSIVE
```

The reviewer is a witness, not an operator.

The repository does not currently claim that a formally validated external session has already occurred.

The protocol exists before such a result so that the procedure cannot be invented after seeing the outcome.

If token-based authentication is later used for invited reviewers, that authentication mechanism should be separately implemented, security-tested, and evidenced before it is described as a validated capability.

---

## 29. Private code and public falsifiability are deliberately separated

SSI does not assume that public evaluation requires publication of all proprietary source code.

The intended model is:

```text
PRIVATE IMPLEMENTATION
+
PUBLIC PROTOCOL
+
PUBLIC PRECOMMITMENT
+
SANITIZED EVIDENCE
+
HASH / MANIFEST REFERENCES
+
READ-ONLY LIVE OBSERVATION
+
EXTERNAL CHALLENGES
```

The current public repository intentionally excludes proprietary implementation source for SSI V5, DIRECTOR, ROBERT, Router V10, Micronetworks, and ISKRA.

The canonical package standard also defines a publication firewall and allowlist-based export model designed to prevent private source, secrets, private paths, raw memory, or internal prompts from entering the public repository accidentally.

This allows the project to protect intellectual property while still exposing enough process and evidence for bounded claims to be challenged.

---

## 30. Protecting SSI from its own future R&D

If a future SSI R&D layer proposes changes to SSI itself, one safety rule is fundamental:

> **R&D must not silently rewrite the current Champion system.**

Every material change should create a candidate or versioned descendant.

```text
CURRENT SSI
= PRESERVED

PROPOSED CHANGE
= CANDIDATE

CANDIDATE
-> SANDBOX
-> TEST
-> REGRESSION
-> EVIDENCE
-> COMPARE
-> REJECT
   or
   CHALLENGER
   or
   PROMOTE
```

This is intended to support adaptive development without uncontrolled self-modification or loss of historical provenance.

---

## 31. Long-term infrastructure and economic reinvestment model

The project is intended to continue even without grant funding. The public funding roadmap already states that successful practical work by future ROBERT/Director domains could contribute to stronger local infrastructure, while explicitly making no guarantee of profitability. See [`FUNDING_STRATEGY_AND_INDEPENDENT_ROADMAP.md`](FUNDING_STRATEGY_AND_INDEPENDENT_ROADMAP.md).

The author’s current planned allocation policy is:

```text
50%
-> AUTHOR / EXECUTION INCOME

40%
-> OPERATIONAL / INVESTMENT CAPITAL

10%
-> DIRECT SSI INFRASTRUCTURE DEVELOPMENT
```

The 10% infrastructure share may fund, depending on future needs:

```text
COMPUTERS
GPU CAPACITY
STORAGE
LOCAL SERVERS
PAID LLMs
MODEL / API ACCESS
ELECTRICITY
NETWORKING
BACKUP
LABORATORY HARDWARE
```

The `50 / 40 / 10` model is a **planned economic policy**, not a revenue forecast or guarantee.

---

## 32. Intended self-reinforcing R&D loop

If later experiments support the underlying hypotheses, the long-term operational loop may become:

```text
WORLDS
-> HERMES
-> AGENTS / ISKRA
-> LAB
-> NEW COMPETENCE
-> EVIDENCE
-> CONSOLIDATION
-> BODY_FROZEN 2.0 / R&D
-> DIRECTOR + ROBERT
-> REAL PROJECTS
-> VERIFIED OUTCOMES
-> ECONOMIC RESULT
-> 50 / 40 / 10
-> STRONGER INFRASTRUCTURE
-> TECHNOLOGY RADAR
-> NEW CANDIDATE TECHNOLOGIES
-> R&D
-> NEXT SSI VERSION
```

This is **long-term planned architecture**, not a current experimental result.

---

## 33. Current public technical state

As of 2026-09-10, the public repository separates closed milestones from future research stages.

Current closed or recorded states include:

```text
BODY_FROZEN T0
= PRESERVED HISTORICAL BASELINE

6 BODY ISKRA
= INDEPENDENT START STATES / START_STATE_VALIDATED

TEST 5
= DEVELOPMENT_VALIDATED
= 29/29 acceptance
= 524/524 total regression

7-BODY TECHNICAL READINESS
= CLOSED / 7/7 PASS
= 147/147 declared common matrix

DIRECTOR_FROZEN_C0
= CLOSED ENGINEERING BASELINE
= INTEGRITY VERIFIED

DIRECTOR TRAIN08A FOUNDATION
= CLOSED / VERIFIED PASS
= 48/48 unique steps PASS
= 0 FAIL / 0 INCONCLUSIVE
= 16/16 blind validations PASS
= 16 checkpoints / final CHECKPOINT_16
= Kiro steps 01-17 -> Kilo steps 18-48
= DIRECTOR_FOUNDATION_S1 CREATED

DIRECTOR TRAIN08A REBUILD PROVENANCE
= DOCUMENTED
= PREDECLARATION BEFORE FINAL RESULT TRACEABLE
= REBUILT BYTE-LEVEL EQUIVALENCE NOT PUBLICLY CLAIMED

BODY_FROZEN TRAIN01A FOUNDATION
= CLOSED / VERIFIED PASS
= 48/48 PASS
= 16/16 blind validations determinate PASS
= 16/16 checkpoints
= T0 integrity PASS
= BODY_FROZEN_FOUNDATION_S1 CREATED
= S1 SHA256 ed1331e38909db829859ca377e9858ee42fe5528537cf6c9c6d2a5ecc5e253e9
```

The BODY_FROZEN Foundation closure preserves the earlier `43 PASS / 5 INCONCLUSIVE / 0 FAIL` run, recovery attempts, infrastructure diagnosis, and step-24 evaluator-error lineage. The later PASS does not erase the earlier evidence.

The immediate next gates are deliberately separated:

```text
BODY_FROZEN
= FOUNDATION_S1 ACHIEVED
-> TRAIN-B -> S2 -> TRAIN-C -> S3 = NEXT CONTROLLED QUEUE

6 BODY ISKRA LINES
= T0 START STATES VALIDATED
-> TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 = NOT YET EXECUTED

FUTURE PRE-EXPERIMENT MATURITY
= S3 -> TRAIN-D -> S4 -> TRAIN-E -> S5
= TRAIN-D/E NOT YET FROZEN OR EXECUTED

DIRECTOR TRAIN08B LEGO + MICRONETWORK + V10 PRACTICUM
= NEXT / PREDECLARED / NOT YET EXECUTED

DIRECTOR_TRAINED_START_S2
= NOT YET CLAIMED

7 MICRONETWORK + V10 MECHANISM TESTS
= PREDECLARED / NOT YET EXECUTED

21 CROSS-DOMAIN EXPERIMENTS
= PREDECLARED / FINAL OUTCOMES UNKNOWN
```

For the current execution sequence and status precedence, see [`CURRENT_RESEARCH_ROADMAP_20260910.md`](CURRENT_RESEARCH_ROADMAP_20260910.md), [`CURRENT_BODY_S3_TRAINING_STATUS_20260910.md`](CURRENT_BODY_S3_TRAINING_STATUS_20260910.md), and [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md).

---

## 34. What SSI V5 does not currently claim

SSI V5 does not currently claim that:

- AGI has been established;
- consciousness has been established;
- universal transfer has been demonstrated;
- the seven BODY/ISKRA TRAIN-A Foundation runs have already passed;
- all seven BODY/ISKRA `FOUNDATION_S1` states exist;
- Director TRAIN08B has passed;
- `DIRECTOR_TRAINED_START_S2` exists;
- the 21 experiments have all passed;
- the seven Micronetwork + V10 mechanism tests have passed;
- long-term ISKRA divergence has been demonstrated;
- physical drone deployment has been validated;
- physical humanoid deployment has been validated;
- Router V10 is universally faster or more accurate than unrelated systems;
- Kiro or Kilo is an independent scientific auditor;
- executor-independent speed equivalence between Kiro and Kilo has been established;
- a cryptographic hash proves a scientific result;
- the `REBUILT_FOR_KILO` TRAIN08A archive is publicly proven byte-for-byte identical to the original predeclared ZIP;
- BODY_FROZEN 2.0 already exists as a completed autonomous R&D organization;
- full Director -> ROBERT -> Worlds -> Agents integration is complete;
- Director currently controls the experimental ISKRA lines;
- the technology-radar workflow has already produced validated SSI upgrades;
- future practical work is guaranteed to be profitable;
- emergent behavior would by itself prove consciousness.

This restraint is intentional.

---

## 35. The author’s working method

The author is self-taught and does not treat that history as something to conceal.

Earlier mistakes and inefficient approaches are part of the project provenance.

The practical development loop can be summarized as:

```text
PROBLEM
-> DATA
-> CODE
-> EXPERIMENT
-> FAILURE / SUCCESS
-> ANALYSIS
-> CHANGE
-> MEMORY
-> NEXT EXPERIMENT
```

Over time, additional layers appeared:

```text
MODELS
-> TEACHERS
-> WORLDS
-> LAB
-> AGENTS
-> MICRONETWORKS
-> ROUTER
-> RECOVERY
-> CONTINUUM
-> ISKRA
-> DIRECTOR
-> CONTROLLED CONSOLIDATION
-> R&D
```

Programming was therefore not the original destination. It became the tool required to keep solving increasingly complex problems.

---

## 36. Why this history belongs in the repository

This document is not only an author biography.

It is intended to become part of SSI’s own future provenance structure.

A future Director or R&D layer should be able to ask:

```text
WHERE DID THIS MECHANISM COME FROM?
WHAT PROBLEM WAS IT INTENDED TO SOLVE?
WHAT DID THE PREVIOUS VERSION LOOK LIKE?
WHAT FAILED?
WHAT REPLACED IT?
WHICH TESTS SUPPORTED THE CHANGE?
WHAT WAS THE CLAIM BOUNDARY?
```

GitHub is therefore intended to serve not only as public presentation but as a **versioned public memory of SSI’s origin and development**.

The repository should help preserve not merely what SSI became, but why it became that way.

---

## 37. Final methodological principle

The shortest description of the current SSI philosophy is:

> **Do not treat an interesting result as true because it looks impressive. Freeze the conditions, execute the experiment, preserve success and failure, compare evidence, and only then revise the system or the claim.**

A second principle is equally important:

> **The implementation may remain private, but a public claim should have as much inspectable, falsifiable, versioned evidence as can be exposed without revealing proprietary source code.**

The long-term research question is therefore not simply whether SSI can solve a particular task.

It is:

> **Can a persistent system with versioned competence, independent agent histories, changing knowledge sources, routing, recovery, real-world outcomes, evidence-preserving consolidation, and controlled R&D progressively increase its ability to solve new problems without losing provenance, authority boundaries, or the ability to explain why a change was made?**

The answer remains an experimental question.

It is not assumed in advance.

---

## Related public records

- [`README.md`](README.md) — current research front door
- [`CURRENT_RESEARCH_ROADMAP_20260910.md`](CURRENT_RESEARCH_ROADMAP_20260910.md) — canonical living roadmap and current status precedence
- [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md) — current public truth index
- [`CURRENT_BODY_S3_TRAINING_STATUS_20260910.md`](CURRENT_BODY_S3_TRAINING_STATUS_20260910.md) — current sequential BODY/ISKRA training status
- [`evidence/BODY_FROZEN_TRAIN01A_FINAL_CLOSURE_20260910.md`](evidence/BODY_FROZEN_TRAIN01A_FINAL_CLOSURE_20260910.md) — BODY_FROZEN Foundation S1 closure
- [`AUTHOR_CONTEXT.md`](AUTHOR_CONTEXT.md) — author/project context
- [`BODY_ISKRA_6X_T0.md`](BODY_ISKRA_6X_T0.md) — six ISKRA start states
- [`ROBERT_CANONICAL_CONTINUITY_VS_EXPERIMENTAL_RESET_20260906.md`](ROBERT_CANONICAL_CONTINUITY_VS_EXPERIMENTAL_RESET_20260906.md) — ROBERT continuity
- [`DIRECTOR_MAINLINE_BODY_INTEGRATION_20260908.md`](DIRECTOR_MAINLINE_BODY_INTEGRATION_20260908.md) — Director mainline and C0
- [`DIRECTOR_TRAINING_START_HERE.md`](DIRECTOR_TRAINING_START_HERE.md) — current Director training lineage
- [`PREDECLARED_DIRECTOR_TRAINING_PACKAGES_20260909.md`](PREDECLARED_DIRECTOR_TRAINING_PACKAGES_20260909.md) — Director package predeclaration and original integrity references
- [`DIRECTOR_TRAIN08A_LIVE_EXECUTION_RECORD_20260909.md`](DIRECTOR_TRAIN08A_LIVE_EXECUTION_RECORD_20260909.md) — preserved interruption/handoff record
- [`DIRECTOR_TRAIN08A_FINAL_EXECUTION_RECORD_20260909.md`](DIRECTOR_TRAIN08A_FINAL_EXECUTION_RECORD_20260909.md) — authoritative final TRAIN08A execution result
- [`evidence/DIRECTOR_TRAIN08A_FINAL_CLOSURE_20260909.md`](evidence/DIRECTOR_TRAIN08A_FINAL_CLOSURE_20260909.md) — formal TRAIN08A closure
- [`evidence/DIRECTOR_TRAIN08A_REBUILD_INTEGRITY_RECORD_20260909.md`](evidence/DIRECTOR_TRAIN08A_REBUILD_INTEGRITY_RECORD_20260909.md) — rebuild provenance and exact public integrity boundary
- [`EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md`](EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md) — 21-experiment program
- [`POST21_COMPETENCE_CONSOLIDATION_AND_NOVEL_TRANSFER_PROTOCOL_20260907.md`](POST21_COMPETENCE_CONSOLIDATION_AND_NOVEL_TRANSFER_PROTOCOL_20260907.md) — post-21 consolidation
- [`CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md`](CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md) — official package/evidence methodology
- [`REVIEWER_LIVE_INTERFACE_20260907.md`](REVIEWER_LIVE_INTERFACE_20260907.md) — read-only reviewer observability
- [`LIVE_EXTERNAL_REVIEW_SESSION_PROTOCOL_20260907.md`](LIVE_EXTERNAL_REVIEW_SESSION_PROTOCOL_20260907.md) — externally witnessed session protocol
- [`FUNDING_STRATEGY_AND_INDEPENDENT_ROADMAP.md`](FUNDING_STRATEGY_AND_INDEPENDENT_ROADMAP.md) — independent-development and funding roadmap
- [`V10_PREDICTIVE_ROUTING.md`](V10_PREDICTIVE_ROUTING.md) — Router V10 public evidence boundary