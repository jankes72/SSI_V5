# SSI V5 — Pre-Experiment Training Program

**Recorded:** `2026-09-08`  
**Status:** `PREDECLARED / TRAINING PACKAGES HASH-SEALED / NOT YET EXECUTED`  
**Applies to:** `BODY_FROZEN` and BODY ISKRA `NICE / GUARDIAN / JUSTICE / EXPLORER / PRAGMATIST / SKEPTIC`  
**Executor:** Kilo as procedural executor  
**Public boundary:** curriculum, training contracts, test vectors, integrity references and sanitized evidence only; private SSI/Micronetwork/V10/ISKRA implementation remains unpublished.

## 1. Why a training phase exists

The research program should not silently treat an empty or minimally populated competence state as if it were a realistic prepared system. Before the later mechanism and cross-domain experiments, each independent BODY line receives the same controlled pre-experiment curriculum.

The purpose is analogous to foundational instruction before examination: teach general reusable skills and the operational use of SSI competence mechanisms without revealing or rehearsing the exact held-out experiment cases.

The training phase does **not** retroactively change the historical T0 baseline.

```text
IMMUTABLE T0
-> TRAINING A / FOUNDATION
-> FOUNDATION_S1
-> TRAINING B / LEGO + MICRONETWORK + V10 PRACTICUM
-> TRAINED_START_S2
-> S2 HASH / STATE RECORD
-> LATER EXPERIMENT EXECUTION
```

`BODY_FROZEN T0` and the six recorded ISKRA T0 start states remain historical controls. Training creates versioned descendants.

## 2. One BODY = two independent training packages

Each of the seven lines receives two separate packages and its own evidence chain:

```text
A = FOUNDATION
B = LEGO + MICRONETWORK + V10 PRACTICUM
```

Therefore:

```text
7 BODY LINES x 2 TRAINING PACKAGES = 14 PREDECLARED TRAINING PACKAGES
```

All seven Foundation packages share the same curriculum core. All seven Practicum packages share the same practicum curriculum core. BODY-specific package identity, execution state and evidence remain separate.

Shared curriculum SHA-256 references:

```text
FOUNDATION_CURRICULUM_SHA256
= 61a3069ce68d19c64d4ae7c5ebc730d04283d81b2e534f487c3fd5063d9b75b8

PRACTICUM_CURRICULUM_SHA256
= abc3eccc4e19849f2d3b3be5b1a4d2752377b6024225f0da8d7d54f4ebafc7ce
```

The matching curriculum hashes are intended to make later cross-BODY comparisons easier to interpret: differences should not be explained merely by giving different lines different schools.

## 3. Training A — Foundation

Foundation develops general reusable competence rather than domain-specific experiment answers.

The curriculum covers:

- reading and restating a task contract;
- decomposition into small verifiable steps;
- simple programming and structured-output tasks;
- debugging and root-cause identification;
- test-before-closure discipline;
- task/project dependency ordering;
- completion gates and checkpointing;
- PASS / FAIL / INCONCLUSIVE classification;
- failure preservation rather than result deletion;
- provenance and evidence recording;
- resume from the last valid checkpoint;
- resource-aware execution under constrained hardware.

Each lesson uses three distinct phases:

```text
INSTRUCTION
-> rule / concept / worked example

GUIDED PRACTICE
-> related task with declared scaffolding

BLIND VALIDATION
-> new task from the same skill family
-> expected answer not supplied to BODY
-> outcome checked against a deterministic oracle or declared acceptance rule
```

Instruction or guided examples alone do not count as independently validated competence. Only declared validation evidence may support lifecycle progression.

## 4. Training B — LEGO + Micronetwork + V10 Practicum

The second package teaches practical use and composition of competence produced during Foundation.

The practicum includes:

- LEGO decomposition of larger tasks;
- reuse of verified existing competence;
- verification of similar or ambiguous competence;
- composition of multiple skills;
- correct escalation to deeper/full flow for novel or unsuitable cases;
- deceptive-similarity and false-reuse traps;
- controlled first-strategy failure;
- repeated-failure anti-loop behavior;
- recovery using an alternative strategy or new evidence;
- persistence across a declared restart;
- CONTINUUM/checkpoint continuity;
- live reviewer-interface correlation;
- hardware/resource telemetry during real BODY execution.

The goal is not to force a preferred V10 route. The runtime must report the route that actually occurred. A route mismatch is evidence, not a reason to rewrite the lesson after execution.

## 5. Training-set / experiment-set separation

Training must not rehearse the exact held-out vectors used by the later mechanism-test packages.

The training contracts explicitly exclude the exact experiment vector families currently reserved for the predeclared mechanism tests, including:

```text
SEQ_PROFILE_STANDARD_V1
SEQ_PROFILE_ABS_V1
STATE_DIFF_V1
```

The principle is:

```text
TRAIN THE MECHANISM / GENERAL SKILL
!=
TRAIN THE HELD-OUT EXPERIMENT ANSWER
```

Training may teach concepts such as reuse, verification, false-reuse avoidance, anti-loop, recovery and LEGO composition, but it must do so on different tasks.

If later audit shows that an experiment case was materially leaked into training, that case must not be represented as clean held-out evidence.

## 6. Speed and route-cost measurement contract

Training is also an instrumented performance phase. Real BODY calls should measure the cost of the route actually used.

Reviewer-safe evidence should record, where available:

```text
CASE FAMILY / CASE ID
ACTUAL V10 ROUTE CLASS
MONOTONIC WALL-CLOCK ELAPSED TIME
ROUTING / RETRIEVAL / VERIFY / EXECUTION COMPONENTS IF EXPOSED
MODEL / PROVIDER CLASS
MODEL CALL COUNT
TOOL CALL COUNT
EXECUTION NODE ALIAS
CPU / RAM SNAPSHOT
GPU / VRAM SNAPSHOT WHERE AVAILABLE
CORRECTNESS / OUTCOME
```

Route families of interest include:

```text
FULL_FLOW
VERIFY_TOPK / INTERMEDIATE VERIFY-ADAPT
REUSE_TOP1 / FAST VALIDATED REUSE
LEGO COMPOSITION / ALTERNATIVE COMPOSITION
RECOVERY AFTER FAILURE
```

Timing must never be used to infer which route occurred. Route identity comes from the runtime/evidence contract; timing measures the cost of that reported route.

For sufficiently repeated comparable observations, report at least:

```text
count
min
mean
p50
p95
max
total elapsed
```

Percentiles should not be presented as meaningful for tiny samples. The current package convention requires at least five comparable observations before reporting p50/p95 summaries for a route group.

## 7. Hardware and comparability rule

Performance evidence is meaningful only with execution context.

Record, where reviewer-safe and technically available:

- execution node identity or public alias;
- CPU/load;
- RAM used/available;
- GPU and VRAM used/available;
- model/provider;
- runtime uptime/process state;
- infrastructure interruption state.

If hardware, provider or model changes materially, timing results are stratified rather than silently pooled.

The intended first claim is a **within-SSI route-cost comparison**, for example FULL_FLOW versus VERIFY versus REUSE on comparable tasks. The training program does not preclaim superiority over external systems. Any external performance comparison requires a separate controlled benchmark with matched tasks and conditions.

## 8. Live reviewer observability during training

At declared milestones, training should produce paired observations from the backend and reviewer-safe interface so a reviewer can see that the state displayed live corresponds to the running BODY.

Where available, correlate:

```text
BODY IDENTITY
PACKAGE ID
CURRENT MODULE / CASE
CHECKPOINT
CONTINUUM STATE
MICRONETWORK / LIFECYCLE SUMMARY
REVIEWER-SAFE V10 ROUTE CLASS
EXECUTION NODE
CPU / RAM / GPU / VRAM
```

The reviewer interface remains read-only. It must not become a route to start training, change lessons, issue ROOT commands, launch Kilo, alter configuration, edit source, access private memory or inject the expected answer.

## 9. Failure, interruption and repair policy

The training packages use the same evidence philosophy as official experiments:

```text
FAILURE
-> PRESERVE
-> CLASSIFY
-> ROOT CAUSE IF AVAILABLE
-> REPAIR OUTSIDE THE FROZEN RUN WHEN MATERIAL
-> NEW VERSION / RETEST WHEN REQUIRED
```

Infrastructure events such as OOM, Ollama failure, interface failure, Kilo crash or operating-system freeze are recorded separately from a learning/SSI failure when evidence supports that distinction.

A pure infrastructure restart may resume from the last valid checkpoint without changing the frozen curriculum. A material change to the curriculum, acceptance rule or tested SSI logic requires a new package/version where applicable.

## 10. Relationship to existing EXP-01 ... EXP-07 packages

The seven Micronetwork + V10 mechanism-test packages were already predeclared and hash-sealed before this training stage was added. Their historical hashes and contracts remain unchanged.

Training therefore does not silently rewrite those precommitments.

Before a post-training mechanism-test run, the actual start state must be made explicit:

```text
TRAINED_START_S2
-> RECORD S2 STATE / HASH
-> CHECK COMPATIBILITY WITH EXISTING FROZEN EXP PACKAGE
```

If binding the S2 state is already compatible with the frozen experiment contract, the execution record must identify that exact S2 state. If using S2 materially changes a frozen experiment input, a new version/hash of the experiment package is required rather than modifying the old package in place.

This preserves both facts:

1. the original experiment design existed before outcomes;
2. the tested post-training start state is not misrepresented as empty T0.

## 11. Execution order

The current intended order is:

```text
TECHNICAL READINESS
-> 7/7 BODY + reviewer interface acceptance

TRAIN-A FOUNDATION
-> seven independent runs
-> produce FOUNDATION_S1 per line

TRAIN-B PRACTICUM
-> seven independent runs
-> produce TRAINED_START_S2 per line

FREEZE / RECORD S2
-> inventory / lifecycle / competence / hash / hardware context

MECHANISM TESTS
-> BODY_FROZEN first
-> then independent ISKRA lines
-> package/start-state compatibility checked before each run

LATER CROSS-DOMAIN PROGRAM
-> drones
-> humanoid
-> self-selected third domain per line
```

Training package publication is not execution. At the time of this predeclaration:

```text
TRAINING_RUNS_COMPLETED = 0 CLAIMED
FOUNDATION_S1_RESULTS = UNKNOWN
TRAINED_START_S2_RESULTS = UNKNOWN
TRAINING_SPEED_RESULTS = UNKNOWN
TRAINING_LIFECYCLE_OUTCOMES = UNKNOWN
```

## 12. Claim boundary

The existence of these packages proves only that the curriculum, package identities, acceptance logic and integrity references were prepared before their outcomes were known.

It does not prove that:

- training will succeed;
- every BODY will create the same skills;
- every Candidate will become a Challenger or Champion;
- V10 will always select the fastest route;
- training will improve every later experiment;
- ISKRA lines will diverge;
- a route-speed advantage will generalize outside the tested hardware/task/model conditions;
- any external system is slower.

The useful future evidence is the difference between the recorded start state, the observed training path, the resulting versioned competence state and later held-out behavior.