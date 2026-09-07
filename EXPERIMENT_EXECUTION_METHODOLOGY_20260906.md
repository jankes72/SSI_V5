# SSI V5 — Experiment Execution Methodology

**Recorded:** `2026-09-06`  
**Methodology hardening:** `2026-09-07`  
**Status:** `PREDECLARED EXECUTION METHODOLOGY / EXPERIMENT EXECUTION GATE NOT YET OPEN / OUTCOMES NOT YET CLAIMED`  
**Applies to:** `EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md`  
**Public boundary:** methodology and reviewer-safe evidence only; private SSI source code and implementation internals remain unpublished.

This document defines how the three-experiment sequence is intended to be executed for each experimental SSI line. Its purpose is to separate infrastructure validation, experiment design and experiment execution; reduce live author influence during a run; preserve failures as evidence; and make later result interpretation auditable.

A critical methodological rule is now explicit:

```text
NO 21-EXPERIMENT RUN STARTS
UNTIL
7/7 SSI BODY LINES PASS THE DECLARED TECHNICAL READINESS GATE
AND
THE REVIEWER INTERFACE PASSES ITS DECLARED READ-ONLY / ISOLATION / OBSERVABILITY GATE.
```

The experiment packages may be prepared before that point, but preparation is not execution and does not create experimental outcomes.

## 1. Research objective

The three experiments are intended to test whether the existing SSI V5 competence architecture — especially Micronetworks and Router V10 — can be transferred across different problem classes while retaining an auditable decision and evidence trail.

The sequence deliberately increases difficulty:

```text
EXPERIMENT A
= controlled transfer with relatively high scaffolding

EXPERIMENT B
= guided transfer with less implementation guidance

EXPERIMENT C
= SSI-selected new domain with the least domain specification
```

The purpose is not merely to produce three demonstrations. The research target is the full observable sequence:

```text
KNOWN START STATE
-> PROBLEM
-> SSI ROUTING / DECISION PATH
-> ATTEMPT
-> OUTCOME
-> RECOVERY / ADAPTATION IF ANY
-> EVIDENCE
-> FINAL CLASSIFICATION
```

## 2. Separation between author, executor and tested system

The experiment uses three distinct roles.

### Author / protocol designer

Before execution, the author prepares the experimental package, including:

- the frozen or identified starting state;
- experiment definitions;
- allowed domain information;
- acceptance criteria;
- PASS / FAIL / INCONCLUSIVE rules;
- evidence requirements;
- intervention rules;
- public/private publication boundary;
- package manifest and integrity references.

Once the run starts, the author is not intended to manually steer SSI toward a preferred answer, choose a solution after seeing an intermediate result, silently repair a failed attempt, or change acceptance criteria because of the observed outcome.

### Kilo / procedural executor

**Kilo is the operational executor of the predeclared procedure.**

Kilo is intended to perform the complete run sequence: verify the frozen experiment package and its integrity reference, identify and verify the target SSI BODY artifact, launch SSI BODY through its canonical execution path, run the three experiments, create checkpoints, collect evidence, execute the declared tests, and produce the final execution report.

Kilo is not presented as an independent external scientific auditor. It is an automation/coding agent used to reduce interactive author steering and to execute the same declared procedure in a repeatable way.

During an actual frozen experimental run, Kilo must not silently rewrite SSI source code, acceptance criteria, experiment prompts or tests in order to obtain a PASS. If a repair is required, the current run is closed with the appropriate outcome, the failure remains preserved, and any repaired execution is a separately versioned retest.

### SSI BODY / experimental line

SSI BODY, BODY_FROZEN or the corresponding BODY ISKRA descendant is the tested system. The decisions, routing behavior, competence reuse/adaptation, failures and recovery behavior attributed to SSI must come from the executed system state, not from an answer manually supplied by the author during the run.

## 3. Pre-experiment technical readiness gate

The 21-experiment research program is not allowed to begin merely because the protocols and packages exist.

Before the first research package is executed, the experimental platform must pass a separate technical readiness phase.

Required readiness scope includes the seven experimental lines:

```text
0 BODY_FROZEN
1 ISKRA NICE
2 ISKRA GUARDIAN
3 ISKRA JUSTICE
4 ISKRA EXPLORER
5 ISKRA PRAGMATIST
6 ISKRA SKEPTIC
```

Each line must pass the declared relevant acceptance/integration/runtime checks for the research platform. Where applicable this includes:

- canonical startup path;
- correct BODY identity;
- runtime responsiveness;
- CONTINUUM availability;
- Micronetwork availability;
- Router V10 availability;
- required bridges/IPC path;
- persistence/checkpoint behavior;
- isolation from the other BODY lines;
- local ROOT authority boundary;
- reviewer-safe observability path;
- existing declared regression/acceptance tests;
- no unresolved blocker that would materially compromise experiment interpretation.

The reviewer interface must separately pass its declared safety and integration checks, including read-only behavior and cross-BODY isolation.

The professional claim is not that the seven BODY lines are universally or mathematically "100% correct". The claim required to open the execution gate is narrower:

> All seven experimental BODY lines and the reviewer interface passed the predeclared technical acceptance gates required for the experiment platform, with no unresolved blocker known to invalidate the planned runs.

Until that evidence exists:

```text
EXPERIMENT_EXECUTION_GATE = CLOSED
EXPERIMENT_PACKAGE_STATE = PREPARED / NOT YET EXECUTED
RESEARCH_OUTCOMES = UNKNOWN
```

A technical readiness failure is an infrastructure result, not automatically a failure of the later cross-domain research hypothesis.

## 4. Frozen and hash-sealed experiment package

Each actual experiment run must begin from a frozen input package.

The package is intended to contain or reference, as appropriate:

- experiment specification;
- prompts/instructions provided to Kilo;
- success/failure/inconclusive criteria;
- permitted tools and boundaries;
- target BODY identity;
- required T0 references;
- run order;
- evidence schema;
- intervention rules;
- final verification procedure;
- package manifest.

Before execution, the package must receive an integrity digest, preferably `SHA256` or an equivalent cryptographic digest.

The intended provenance chain is:

```text
FROZEN PACKAGE CONTENT
-> PACKAGE MANIFEST
-> SHA256 / INTEGRITY DIGEST
-> GIT COMMIT / TIMESTAMPED PUBLIC REFERENCE WHERE SAFE
-> KILO PRE-RUN DIGEST VERIFICATION
-> EXECUTION
-> EVIDENCE DIRECTORY
-> FINAL REPORT
```

Where public disclosure of the complete private package is inappropriate, the repository may publish the digest, package identifier, sanitized manifest and Git reference while keeping proprietary contents private.

If any input file, prompt, criterion or other frozen package component changes after hashing, the previous package identity is no longer valid for that modified content. A new version must be created and frozen with a new digest before it can be executed.

Therefore:

```text
CHANGE INPUT
=> NEW PACKAGE VERSION
=> NEW HASH
=> NEW PRE-RUN RECORD
```

The integrity digest is intended to make post-hoc silent replacement detectable. It does not by itself prove scientific correctness; it proves identity of the frozen artifact against which the later evidence is associated.

## 5. Experiment directory as evidence artifact

The experiment directory is not merely a temporary workspace. It is intended to become the primary evidence artifact for that run.

Where technically available and reviewer-safe, it should preserve:

- package ID and integrity digest;
- associated Git commit/reference;
- run ID;
- execution timestamps;
- BODY/line identity;
- relevant tool/model/runtime version references;
- T0/start-state reference;
- prompts/instructions actually executed;
- Kilo procedural log;
- SSI inputs/outputs at the allowed evidence boundary;
- checkpoints;
- route/state summaries;
- failures and failure signatures;
- retries and recovery attempts;
- manual interventions, if any;
- acceptance-test outputs;
- final PASS / FAIL / INCONCLUSIVE classification;
- post-run state/provenance summary.

The design principle is:

```text
THE RUN PACKAGE + EXECUTION RECORD + EVIDENCE + FINAL REPORT
= ONE VERSIONED EXPERIMENT ARTIFACT
```

Evidence should be append-oriented where practical. A later success must not erase an earlier failed attempt.

## 6. Pre-run integrity and T0 capture

Before Experiment A begins, Kilo must verify that the intended SSI BODY artifact and experimental line are the ones being executed and that the experiment package matches the frozen integrity reference.

The run begins from an identified T0 state. Reviewer-safe evidence should record enough information to establish the experimental identity and starting condition without publishing proprietary source code.

The T0 record should include, where available:

- experiment-line identity;
- baseline/frozen-state identity;
- relevant inventory counts;
- test/QA status;
- Router V10 availability;
- Micronetwork state summary;
- experience/competence counters relevant to the experiment;
- integrity/hash references where appropriate;
- open blockers or known failures.

The purpose is to make it possible to answer later:

> What was already present before the experiment, and what changed only after execution?

## 7. Frozen origin and experimental descendant

The common BODY_FROZEN origin remains a preserved comparison point.

Where the protocol requires a working descendant, the experiment is executed on the designated descendant rather than silently rewriting the frozen origin.

Conceptually:

```text
BODY_FROZEN T0
= preserved reference / control origin

EXPERIMENTAL DESCENDANT
= working line used for new experiment experience
```

At the end of the run, the frozen/original reference should be rechecked where practical so later reviewers can distinguish baseline state from experiment-generated changes.

## 8. Kilo execution sequence

The intended execution sequence is:

```text
0. VERIFY THAT TECHNICAL READINESS GATE IS OPEN
1. VERIFY FROZEN EXPERIMENT PACKAGE + MANIFEST + HASH
2. IDENTIFY CANONICAL SSI BODY START PATH
3. VERIFY T0 / TARGET LINE
4. LAUNCH REAL SSI BODY
5. RECORD PRE-RUN CHECKPOINT
6. RUN EXPERIMENT A
7. RECORD EVIDENCE + CHECKPOINT
8. RUN EXPERIMENT B
9. RECORD EVIDENCE + CHECKPOINT
10. RUN EXPERIMENT C
11. RECORD EVIDENCE + CHECKPOINT
12. RUN DECLARED FINAL TESTS
13. VERIFY BASELINE/LINEAGE INTEGRITY
14. VERIFY EVIDENCE ARTIFACT COMPLETENESS
15. PRODUCE FINAL REPORT
```

If the pre-run package hash does not match, the research execution must not silently continue as if the package were unchanged.

The exact private commands, source paths and implementation internals are intentionally not part of this public document.

## 9. Experiment A — controlled cross-domain transfer

Experiment A uses the drones domain as a controlled research environment.

The experiment concerns a safe civilian simulation or equivalent controlled research setting. It does not claim physical deployment or autonomous control of real aircraft.

The domain may expose events such as:

- node loss;
- reduced energy;
- communication loss;
- changed coverage requirement;
- unsuccessful previous reorganization;
- need to choose between reuse, verification/adaptation or a deeper route.

The research question is:

> Can the existing SSI Micronetworks + Router V10 mechanism be applied to a new domain representation when the system receives relatively strong experimental scaffolding?

Experiment A is intentionally the most constrained of the three. A positive outcome is evidence of controlled transfer under the declared conditions, not evidence of unrestricted autonomous discovery.

## 10. Experiment B — guided transfer with reduced scaffolding

Experiment B uses the humanoid/robotics domain in a safe simulation or equivalent controlled environment.

The test concerns high-level strategy selection and adaptation rather than low-level motor control, torque control or physical-robot validation.

The experimental state may require the system to distinguish between situations such as:

- normal locomotion;
- balance disturbance;
- slip risk;
- loss-of-stability condition;
- failed previous recovery strategy;
- need to select a different validated strategy.

Compared with Experiment A, the system receives less implementation guidance. The tested line should create more of the problem-to-architecture mapping itself while still operating under predeclared safety and evaluation constraints.

The research question is:

> Can the same SSI mechanism be transferred to a substantially different problem class without receiving a complete solution mapping from the author?

## 11. Experiment C — self-selected new domain

Experiment C is the most open part of the sequence.

The corresponding SSI line selects a new domain rather than being given the expected third-domain answer by the author.

For the full 7-line program:

- BODY_FROZEN selects its own third domain;
- each BODY ISKRA descendant independently selects its own third domain;
- equivalent selections by two lines are preserved as evidence rather than silently replaced;
- selections should be recorded before later novelty analysis wherever practical.

The selected domain must not be merely a cosmetic renaming of drones or humanoid.

For its selected domain, the SSI line should, at a reviewer-safe level:

1. define the problem;
2. explain how the problem maps to its competence/routing architecture;
3. define a minimal testable demonstration;
4. define normal conditions;
5. define failure/exception conditions;
6. execute the test;
7. record the result and evidence.

The research question is:

> Can the system identify another functionally distinct problem class in which its existing mechanisms may be useful and create a testable transfer attempt without being supplied the expected domain by the author?

## 12. No live answer steering

Once a run begins, the author should not provide mid-run instructions that effectively supply the answer to the tested system.

Examples of prohibited silent steering include:

- telling SSI which specific route must be selected after observing a failure;
- manually replacing the system's chosen strategy with a preferred one;
- changing thresholds after seeing the result;
- deleting a failed attempt and retaining only a later successful attempt;
- manually repairing experiment-specific logic and presenting the same run as uninterrupted autonomy;
- changing a frozen package input without creating a new package version and hash.

If an intervention is necessary, it must be explicitly recorded.

## 13. Manual intervention rule

Any intervention that materially changes the natural experiment path should be recorded as:

```text
MANUAL_INTERVENTION
```

The evidence should state what changed, why it changed and at what point in the run it occurred.

A run containing manual intervention may still provide useful engineering evidence, but it must not be represented as a fully autonomous uninterrupted experiment.

If intervention requires changing the frozen experiment input, the current package/run identity is closed and a separately versioned retest must use a newly frozen package.

## 14. Evidence must preserve failures

Evidence should be produced during execution rather than reconstructed only after a successful final result exists.

Where available, the evidence chain should preserve:

- pre-decision state;
- state classification;
- Router V10 route choice;
- competence selected or created;
- attempt outcome;
- failure signature;
- retry/recovery behavior;
- changed strategy;
- checkpoints;
- final test results;
- competence/micronetwork state changes;
- lineage and provenance information.

The evidence history is intended to be append-oriented.

If attempt 1 fails and attempt 2 succeeds, both attempts remain part of the research record. The successful result must not silently erase the failed path.

## 15. Common measurement contract

The execution methodology preserves the measurement categories already defined by the 21-experiment program:

```text
STATE CLASS
= KNOWN / SIMILAR / NOVEL

ROUTING
= reuse / verify-adapt / alternative-compose / deeper-full-flow

TIMING
= detection + routing + retrieval + verification/adaptation + total decision cost

QUALITY
= correctness / outcome + false reuse + false escalation + recovery result

COMPETENCE
= prior competence used?
+ candidate created?
+ challenger updated?
+ champion enriched/replaced?
+ provenance retained?
+ verified outcome required before adaptation?
```

Not every domain must expose every metric identically, but deviations should be recorded rather than hidden.

## 16. Final outcome classification

Each experiment should end in one of three primary states:

### PASS

The predeclared acceptance criteria are met and sufficient evidence exists to support the result.

### FAIL

The declared criteria are not met or the evidence shows the tested behavior failed.

### INCONCLUSIVE

The evidence is insufficient, ambiguous or compromised enough that PASS or FAIL would overstate what the run establishes.

A missing or incomplete evidence chain is not automatically a PASS.

An infrastructure malfunction that prevents a fair test may produce `INCONCLUSIVE` rather than being silently interpreted as a research PASS or hidden from the record.

## 17. Why Kilo executes the complete procedure

Using Kilo as the procedural executor is intended to reduce one important source of bias: continuous interactive author steering during the experiment.

The intended division is:

```text
AUTHOR
= designs and freezes the protocol/package before execution

KILO
= verifies frozen package integrity
+ executes the declared procedure
+ records the run

SSI BODY
= produces the tested routing / adaptation behavior

REVIEWER
= observes through a read-only boundary where invited
+ later evaluates what the evidence actually supports
```

This arrangement does not make the experiment externally independent. It does make the author/executor boundary explicit and creates a cleaner basis for later independent review.

## 18. External challenge mode

The same methodology can be used for a problem proposed by an external reviewer, company or researcher.

In that mode:

```text
EXTERNAL PARTY
= defines or proposes the challenge/problem

AUTHOR + EXTERNAL PARTY WHERE PRACTICAL
= establish success/failure criteria before execution

AUTHOR
= packages and freezes the agreed test without changing it to favor SSI

PACKAGE
= versioned + hash-sealed before execution

KILO
= verifies and executes the frozen procedure

SSI
= tested system

REVIEWER
= may observe reviewer-safe live state through the read-only interface

RESULT
= PASS / FAIL / INCONCLUSIVE with failures retained
```

A challenge designed outside the SSI project is especially valuable because it reduces the risk that the problem was selected only around known system strengths.

## 19. Full 21-experiment application

The same three-experiment execution methodology is intended to be applied consistently across all seven experimental lines:

```text
BODY_FROZEN T0
NICE
GUARDIAN
JUSTICE
EXPLORER
PRAGMATIST
SKEPTIC
```

Therefore the methodology covers:

```text
7 experimental lines x 3 experiments = 21 predeclared runs
```

Each line should retain its own start-state identity, package hash/reference, evidence chain and outcome classification.

## 20. Current execution-state boundary

As of this methodology hardening entry, the experiment design and package methodology are prepared, but the proper 21-run research execution is not to be represented as started until the technical readiness gate is satisfied.

The current intended sequence is:

```text
FINISH BODY / ISKRA / REVIEWER-INTERFACE INTEGRATION
-> RUN DECLARED 7/7 TECHNICAL READINESS VALIDATION
-> RESOLVE BLOCKERS IF ANY
-> RE-RUN READINESS VALIDATION
-> OPEN EXPERIMENT EXECUTION GATE ONLY AFTER ACCEPTANCE
-> FREEZE FINAL EXPERIMENT PACKAGE VERSION
-> RECORD MANIFEST + HASH + GIT REFERENCE
-> KILO VERIFIES PACKAGE
-> BEGIN 21 RESEARCH EXPERIMENTS
```

This distinction is deliberate. It prevents unfinished platform integration from being confused with the scientific outcome of the later experiment program.

## 21. Scientific claim boundary

This document defines the intended methodology. It does not claim that all experiments are already complete or successful.

A successful run may support claims such as controlled cross-domain transfer under the tested conditions. It does not by itself establish:

- AGI;
- consciousness;
- universal autonomy;
- universal V10 superiority;
- production readiness;
- physical drone or humanoid deployment validity;
- long-term behavioral divergence of the six BODY ISKRA lines;
- success outside the measured conditions.

The intended rule remains:

```text
READINESS GATE NOT PASSED -> DO NOT START RESEARCH RUN
PACKAGE HASH MISMATCH -> DO NOT SILENTLY CONTINUE
NO EVIDENCE -> UNKNOWN
FAILURE -> PRESERVE
MANUAL INTERVENTION -> DISCLOSE
INPUT CHANGE -> NEW PACKAGE VERSION + NEW HASH
AMBIGUOUS EVIDENCE -> INCONCLUSIVE
VERIFIED RESULT -> CLAIM ONLY WHAT THE RESULT SUPPORTS
```
