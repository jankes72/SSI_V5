# SSI V5 — Research Front Door

**Experimental persistent-competence architecture for adaptive AI systems.**

SSI V5 investigates whether a long-running system can build, validate, preserve, reuse, compare and revise competence across tasks using persistent state, Experience, Micronetworks, Candidate -> Challenger -> Champion lifecycle, Router V10, LEGO composition and CONTINUUM persistence.

The public repository is an **evidence-indexed research mirror, not a source-code distribution**. Private SSI, Micronetwork, Router V10, ISKRA, DIRECTOR and ROBERT implementation source remains private by design. Public materials describe architecture, test protocols, sanitized states, measured outcomes, failures, repairs, retests and claim boundaries without publishing the proprietary implementation.

## Independent project context

SSI V5 is independently designed and developed by **Paweł Jankiewicz (`jankes72`)**. Coding/research assistants such as Kilo, OpenCode, Pi and local/open models are used as implementation, analysis and testing tools; they are not represented as the authors of the architecture or as independent scientific validators.

The project should be evaluated from its **predeclared protocols, measured outcomes, failures, repairs, retests, hashes, claim boundaries and reviewer-visible evidence**.

See [`AUTHOR_CONTEXT.md`](AUTHOR_CONTEXT.md).

## Current state — 2026-09-09

```text
FROZEN COMMON BASELINE
= BODY_FROZEN T0 / PRE-ISKRA / RECORDED / 2026-09-05

CURRENT ISKRA START STATE
= 6 independent BODY ISKRA descendants / START_STATE_VALIDATED / 2026-09-06

LATEST CLOSED DEVELOPMENT VALIDATION
= TEST 5 / DEVELOPMENT_VALIDATED
= 29/29 acceptance
= 524/524 total regression
= 0 open blockers in the TEST 5 tested scope

7-BODY TECHNICAL READINESS
= pre-repair sequential audit completed 43/43 on 2026-09-08
= audit mode READ_ONLY / TEST_ONLY
= readiness NOT YET CLOSED 7/7
= repair + common retest required before training execution

PRE-EXPERIMENT TRAINING
= 14 HASH-SEALED packages
= 7 BODY lines x 2 phases
= PREDECLARED / NOT YET EXECUTED

MICRONETWORK + V10 MECHANISM TESTS
= 7 independent packages
= PREDECLARED / HASH-SEALED / NOT YET EXECUTED

CROSS-DOMAIN PROGRAM
= 7 lines x 3 domains = 21 experiments
= PREDECLARED / FINAL CONTROLLED OUTCOMES UNKNOWN

DIRECTOR MAINLINE
= canonical engineering / operational line
= DIRECTOR_FROZEN_C0 baseline created and integrity-verified
= local Director runtime validated RUNNING
= local owner control panel validated
= shared WWW observability validated OBSERVER_ONLY
= restart / persistence / checkpoint / IPC validation PASS
= Router V10, Micronetwork, LAB, memory and model-status integration validated in the C0 scope
= central Director node intentionally OFFLINE in LOCAL-ONLY mode

CANONICAL ROBERT
= continuous engineering / execution line
= not reset by experiment-branch cleaning
```

## Two deliberately separated tracks

SSI V5 has a controlled research track and a parallel canonical engineering track.

### A. Controlled BODY research track

```text
BODY_FROZEN / ISKRA T0
-> 7-BODY TECHNICAL READINESS
-> PRE-REPAIR FINDINGS PRESERVED
-> TARGETED REPAIR
-> COMMON 7/7 RETEST
-> TRAIN-A FOUNDATION
-> FOUNDATION_S1
-> TRAIN-B LEGO + MICRONETWORK + V10 PRACTICUM
-> TRAINED_START_S2 + HASH
-> 7 MICRONETWORK + V10 MECHANISM TESTS
-> 21 CROSS-DOMAIN EXPERIMENTS
-> POST-21 COMPETENCE CONSOLIDATION
-> 3 NEW DOMAINS
-> LATER EXTERNAL FALSIFICATION CHALLENGES
```

No later-stage success is claimed in advance.

### B. Canonical engineering / operational mainline

```text
VALIDATED BODY FOUNDATION
+ EXISTING WORKING DIRECTOR FUNCTIONS
-> NEW CANONICAL DIRECTOR
-> LOCAL DIRECTOR CONTROL PANEL
-> SHARED READ-ONLY OBSERVABILITY
-> RESTART / PERSISTENCE / CHECKPOINT / IPC VALIDATION
-> DIRECTOR_FROZEN_C0
-> LATER DIRECTOR -> ROBERT INTEGRATION
-> LATER WORLD INFRASTRUCTURE
-> LATER AGENT/WORLD INTEGRATION
```

The Director mainline is **not counted as a completed BODY experiment**. It is a separate engineering descendant/integration line. `BODY_FROZEN T0` remains unchanged as a historical experimental control.

Primary Director record:

- [`DIRECTOR_MAINLINE_BODY_INTEGRATION_20260908.md`](DIRECTOR_MAINLINE_BODY_INTEGRATION_20260908.md)

## DIRECTOR_FROZEN_C0 — closed engineering baseline

On 2026-09-08 the canonical Director line reached a frozen engineering baseline named **`DIRECTOR_FROZEN_C0`**.

This is a **private implementation baseline with a public sanitized status description**. The source code, internal execution logic, secrets, private runtime configuration and proprietary implementation details are not published in this repository.

The C0 baseline records the following validated state within its tested scope:

```text
LOCAL DIRECTOR RUNTIME = RUNNING / validated
SINGLE RUNTIME PROTECTION = PASS
IPC = ACTIVE / validated
CHECKPOINT + RESTART/PERSISTENCE = PASS
CONTINUUM local integration = ACTIVE / validated
LAB integration = ACTIVE / validated
MICRONETWORK integration = validated
ROUTER V10 integration = validated
COLLECTIVE INTELLIGENCE status = validated
PERSISTENT CONVERSATION MEMORY = validated across restart
LOCAL DIRECTOR CONTROL PANEL = PASS
SHARED WWW INTERFACE = PASS / OBSERVER_ONLY
ROOT commands in shared WWW = NOT EXPOSED
HARDWARE STATUS incl. NVIDIA GPU/VRAM = validated
MODEL/BACKEND STATUS = validated in C0 scope
CENTRAL DIRECTOR NODE = intentionally OFFLINE / LOCAL-ONLY mode
```

The final C0 verification also recorded:

```text
FINAL PANEL / SYSTEM CHECKS = 27/27 PASS
SELECTED PYTEST VALIDATION = 19/19 PASS
INDEPENDENCE VALIDATION = PASS
FREEZE MANIFEST = CREATED
FREEZE INTEGRITY = VERIFIED
```

These are **scoped internal engineering-validation results**, not an external certification and not a claim of production readiness, AGI or consciousness.

The architectural boundary preserved by C0 is deliberate:

```text
LOCAL OWNER CONTROL PANEL
= execution and administration through existing authorized control paths

SHARED REVIEWER / OBSERVER INTERFACE
= read-only
= sanitized observability
= no ROOT commands
= no remote execution

DIRECTOR_FROZEN_C0
= immutable reference baseline
= later development continues above C0 rather than rewriting C0
```

## 7-BODY readiness — chronology preserved before repair

A sequential readiness audit completed all `43/43` declared audit stages on 2026-09-08 in `READ_ONLY / TEST_ONLY` mode. No BODY repair was performed during that audit.

The audit preserved open findings, including the JUSTICE launcher deviation, repeated ISKRA Stage 09 test-fixture failures, a CONTINUUM full-flow orchestrator syntax issue and unequal full-acceptance coverage across lines.

Therefore:

```text
AUDIT PROCEDURE COMPLETED = YES
BODY MODIFICATIONS DURING AUDIT = 0
AUTOMATIC REPAIRS DURING AUDIT = 0
7-BODY READINESS CLOSED = NO
REPAIR REQUIRED = YES
COMMON RETEST REQUIRED = YES
```

The repository intentionally records the state **before repair** so a later successful retest cannot erase the original findings.

References:

- [`7BODY_TECHNICAL_READINESS_START_HERE.md`](7BODY_TECHNICAL_READINESS_START_HERE.md)
- [`evidence/7BODY_TECHNICAL_READINESS_PRE_REPAIR_AUDIT_20260908.md`](evidence/7BODY_TECHNICAL_READINESS_PRE_REPAIR_AUDIT_20260908.md)

## Director Control Panel vs reviewer interface

The Director line includes a dedicated **local Director Control Panel** for the owner/operator. Its C0 integration is now validated in the tested scope.

The panel consolidates routine system state and authorized owner operations such as runtime lifecycle status, ROOT-terminal access, checkpoint/persistence visibility, V10/Micronetwork status, model/provider availability, diagnostics, Pocket status and hardware status. It does not create a second runtime, second CONTINUUM or independent execution authority.

This must not be confused with the shared reviewer/developer interface.

```text
DIRECTOR CONTROL PANEL
= LOCAL OWNER / OPERATOR
= AUTHORIZED EXECUTION + ADMINISTRATION
= uses existing control paths

SHARED REVIEWER INTERFACE
= OBSERVER_ONLY
= READ-ONLY
= SANITIZED OBSERVABILITY
= NO ROOT
= NO REMOTE EXECUTION
```

The shared interface and the local control panel deliberately remain separate security surfaces.

## Pre-experiment training — 14 independent packages

Training is an explicit methodological stage and has **not yet been executed**.

Each BODY receives two curriculum families:

```text
A = FOUNDATION
    task interpretation
    programming/debugging
    decomposition
    task/project management
    testing/evidence
    checkpoint/resume
    resource-aware execution

B = LEGO + MICRONETWORK + V10 PRACTICUM
    reuse
    verify/adapt
    multi-skill composition
    false-reuse protection
    controlled failure
    repeated-failure anti-loop
    recovery
    restart persistence
    route-cost measurement
```

Training uses task vectors separated from held-out mechanism-test vectors.

Shared curriculum integrity references:

```text
FOUNDATION_CURRICULUM_SHA256
= 61a3069ce68d19c64d4ae7c5ebc730d04283d81b2e534f487c3fd5063d9b75b8

PRACTICUM_CURRICULUM_SHA256
= abc3eccc4e19849f2d3b3be5b1a4d2752377b6024225f0da8d7d54f4ebafc7ce
```

References:

- [`PREEXPERIMENT_TRAINING_PROGRAM_20260908.md`](PREEXPERIMENT_TRAINING_PROGRAM_20260908.md)
- [`PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md`](PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md)
- [`TRAINING_PACKAGES_START_HERE.md`](TRAINING_PACKAGES_START_HERE.md)

## T0 remains immutable

```text
BODY T0
= preserved historical control

FOUNDATION_S1
= later versioned training descendant

TRAINED_START_S2
= later versioned post-practicum descendant
```

No S1/S2 result is currently claimed. If binding a future S2 state materially changes an already frozen mechanism-test input, a new package version/hash is required rather than rewriting the historical precommitment.

## Route-speed and compute evidence

SSI records the route actually reported by the runtime and measures its cost. Relevant route families include:

```text
FULL_FLOW
VERIFY_TOPK / VERIFY-ADAPT
REUSE_TOP1
LEGO / ALTERNATIVE COMPOSITION
RECOVERY AFTER FAILURE
```

Where available, evidence includes elapsed time, route class, model/provider, model/tool call counts, execution node, CPU/RAM/GPU/VRAM and correctness/outcome.

Historical scoped Test 3 evidence remains:

```text
57.61 s vs 126.65 s Test 2
REUSE_TOP1 = 534
VERIFY_TOPK = 66
fallback = 0
known-case correctness = 100/100
```

This is scoped internal evidence, not a universal superiority claim.

See [`V10_PREDICTIVE_ROUTING.md`](V10_PREDICTIVE_ROUTING.md).

## Current closed milestones

### BODY_FROZEN T0 — 2026-09-05

```text
BODY_FROZEN_TOTAL_FILES = 1781
BODY_FROZEN_PYTHON_FILES = 587
CONTINUUM_TESTS = 23/23 PASS
MAIN_SCENARIOS = 22/22 PASS
E2E_CLOSURE = 19/19 PASS
FINAL_GUARD = 26/26 PASS
ACTIVE_FAILURES = 0
OPEN_BLOCKERS = 0
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

### DIRECTOR_FROZEN_C0 — latest closed Director engineering baseline

```text
LOCAL RUNTIME = VALIDATED
CONTROL PANEL = PASS
OBSERVER_ONLY WWW = PASS
SINGLE RUNTIME PROTECTION = PASS
RESTART / PERSISTENCE / CHECKPOINT = PASS
FINAL PANEL / SYSTEM CHECKS = 27/27 PASS
SELECTED PYTEST VALIDATION = 19/19 PASS
FREEZE INTEGRITY = VERIFIED
CENTRAL DIRECTOR NODE = INTENTIONALLY OFFLINE / LOCAL-ONLY
```

These are scoped development/engineering-validation results, not claims of production readiness, AGI or consciousness.

## Current claim boundary

SSI V5 does **not** currently claim that:

- 7-BODY technical readiness has already closed 7/7;
- the readiness repair/retest has already passed;
- the 14 training packages have passed;
- `FOUNDATION_S1` or `TRAINED_START_S2` already exists for all seven lines;
- the seven mechanism tests have passed;
- the complete 21-run program has passed;
- `DIRECTOR_FROZEN_C0` is an external certification or production-readiness proof;
- the central Director node is currently connected — C0 intentionally operates in LOCAL-ONLY mode;
- Director currently controls the experimental ISKRA lines;
- ROBERT integration with the new Director is already complete;
- drones or humanoids are validated physical deployments;
- V10 is universally faster or more accurate than unrelated systems;
- Kilo is an independent scientific auditor;
- a cryptographic hash proves scientific correctness;
- AGI, consciousness, universal transfer or production readiness has been established.

## Source-code and disclosure boundary

The public repository intentionally does **not** publish the proprietary implementation source of SSI V5, DIRECTOR, ROBERT, Router V10, Micronetworks or ISKRA.

Public evidence may include:

- sanitized architecture descriptions;
- declared test protocols;
- scoped measurements and results;
- hashes and manifests where disclosure is safe;
- failure/repair/retest history;
- reviewer-oriented status summaries;
- claim boundaries.

Private materials remain private, including implementation code, internal execution logic, credentials/secrets and operational details that would disclose or materially reconstruct the proprietary system.

## Start here

1. [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md)
2. [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md)
3. [`7BODY_TECHNICAL_READINESS_START_HERE.md`](7BODY_TECHNICAL_READINESS_START_HERE.md)
4. [`DIRECTOR_MAINLINE_BODY_INTEGRATION_20260908.md`](DIRECTOR_MAINLINE_BODY_INTEGRATION_20260908.md)
5. [`TRAINING_PACKAGES_START_HERE.md`](TRAINING_PACKAGES_START_HERE.md)
6. [`EXPERIMENT_PACKAGES_START_HERE.md`](EXPERIMENT_PACKAGES_START_HERE.md)
7. [`CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md`](CANONICAL_EXPERIMENT_PACKAGE_STANDARD_20260908.md)
8. [`REVIEWER_LIVE_INTERFACE_20260907.md`](REVIEWER_LIVE_INTERFACE_20260907.md)
9. [`V10_PREDICTIVE_ROUTING.md`](V10_PREDICTIVE_ROUTING.md)
10. [`evidence/README.md`](evidence/README.md)

The standard is: **predeclare what will be tested, preserve what actually happened, keep engineering and experiment claims separate, never hide a failure, keep proprietary implementation private, and make stronger claims only when stronger evidence exists.**