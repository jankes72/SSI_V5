# SSI V5 — Research Front Door

**Experimental persistent competence architecture for adaptive AI systems.**  
SSI V5 investigates whether a long-running system can build, validate, preserve, reuse, compare and revise competence across tasks using persistent state, Experience, micronetworks, Candidate -> Challenger -> Champion lifecycle, V10 stateful routing, LEGO composition and CONTINUUM persistence.

## Current state — 2026-09-05

```text
CURRENT EXPERIMENTAL BASELINE = T0 / BODY_FROZEN / PRE-ISKRA
T0 STATUS = RECORDED
CONTINUUM = CLOSED
NEXT EXPERIMENTAL PHASE = T1
LATEST CLOSED VALIDATION TEST = TEST 5 / DEVELOPMENT_VALIDATED
```

**Important distinction:** `T0` is the newest experimental baseline/checkpoint. It is **not TEST 6** and it does not replace TEST 5 as the latest closed validation test. TEST 5 validates a scoped SSI BODY control/integration path; T0 freezes the state from which the next comparative experiments will begin.

Public T0 entry point:

- [BODY_FROZEN_T0_PRE_ISKRA.md](BODY_FROZEN_T0_PRE_ISKRA.md)
- [evidence/BODY_FROZEN_T0_20260905/README.md](evidence/BODY_FROZEN_T0_20260905/README.md)

## T0 — BODY_FROZEN PRE-ISKRA baseline

The public T0 snapshot records:

```text
CONTINUUM_FINAL_STATUS = CLOSED
CONTINUUM_TESTS = 23/23 PASS
MAIN_SCENARIOS = 22/22 PASS
E2E_CLOSURE = 19/19 PASS
FINAL_GUARD = 26/26 PASS
ACTIVE_FAILURES = 0
INVARIANT_VIOLATIONS = 0
OPEN_BLOCKERS = 0
EXISTING_SUITE = 580 PASS + 12 SUPERSEDED = 592

BODY_FROZEN_TOTAL_FILES = 1781
BODY_FROZEN_PYTHON_FILES = 587

MICRONETWORKS = 8
MODULES = 8
LAYERS = 3
ROUTER_V10 = ACTIVE
```

The `1781 / 587` values are **private baseline inventory counts only**. Source code itself is not published.

The explicit formal skill lifecycle counters in the supplied sanitized T0 snapshot are currently `0`. The public record deliberately does **not** reinterpret micronetwork candidate records as formal skills. This gives future T1/T2 comparisons a stable counting definition.

T0 is intended to remain immutable as the comparison origin. Later upgrades should create descendants of T0 rather than rewriting the original baseline.

---

## What this repository publishes — and what it does not

This repository is a **public, evidence-indexed research mirror** of SSI V5. It publishes research history, measured effects, machine-readable summaries, failures, repairs, test boundaries, claim boundaries and reviewer-facing documentation.

It is **not** the source-code distribution of the private SSI runtime, V10 implementation or full micronetwork engine.

SSI V5 is an independently developed system architecture authored by **Paweł Jankiewicz**. Third-party language models, frameworks and tools remain third-party components and are not presented as models created or owned by SSI.

```text
PUBLIC
= research history
+ architecture at reviewer-safe level
+ machine evidence
+ measured outcomes
+ failures / superseded results
+ claim boundaries

PRIVATE
= SSI source implementation
+ proprietary routing internals
+ full micronetwork implementation
+ raw memory / user data
+ local paths / secrets
+ implementation-level migration maps
```

## Start here

- **Current T0 baseline:** [BODY_FROZEN_T0_PRE_ISKRA.md](BODY_FROZEN_T0_PRE_ISKRA.md)
- **Technical reviewers / grant evaluators:** [START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md)
- **General project entry:** [START_HERE.md](START_HERE.md)
- **Current project truth:** [CURRENT_TRUTH_INDEX.md](CURRENT_TRUTH_INDEX.md)
- **Grant / methodology FAQ:** [GRANT_REVIEWER_FAQ.md](GRANT_REVIEWER_FAQ.md)
- **V10 architecture:** [V10_PREDICTIVE_ROUTING.md](V10_PREDICTIVE_ROUTING.md)
- **Public machine evidence:** [evidence/README.md](evidence/README.md)

---

# Latest closed validation milestone — TEST 5

**Status:** `DEVELOPMENT_VALIDATED / PASS`  
**Date:** `2026-09-03`

```text
STAGE_12 = SUPERSEDED
STAGE_13_AUDIT_RETEST = PASS
TEST5_ACCEPTANCE = 29/29 PASS
ROOT_CONTROL = 111/111 PASS
ROOT_RUNTIME_BRIDGE = 338/338 PASS
ROBERT_STABLE = 46/46 PASS
TOTAL = 524/524 PASS
OPEN_BLOCKERS = 0
FINAL_CONVERGENCE_PASS = TRUE
```

TEST 5 remains the newest closed public validation test. Its main methodological value is that an earlier green Stage 12 result (`27/27`) was **not accepted as closure** after audit showed the contract was too weak. The result was preserved as `SUPERSEDED`, the system/test contract was repaired, and Stage 13 was rerun.

Public evidence:

- [evidence/TEST5_FINAL_CONVERGENCE_20260903.md](evidence/TEST5_FINAL_CONVERGENCE_20260903.md)
- [evidence/TEST5_FINAL_RESULT_20260903.json](evidence/TEST5_FINAL_RESULT_20260903.json)
- [evidence/TEST5_FINAL_MATRIX_20260903.json](evidence/TEST5_FINAL_MATRIX_20260903.json)
- [evidence/TEST5_STAGE12_SUPERSEDED_20260903.json](evidence/TEST5_STAGE12_SUPERSEDED_20260903.json)

**Claim boundary:** TEST 5 supports development validation of the tested local SSI BODY control/integration path. It does not prove production readiness of the whole SSI system, universal reliability, AGI or consciousness.

---

# Research sequence from T0

The project has now moved from integration closure into a controlled comparative experiment series.

```text
T0
= one frozen PRE-ISKRA starting body

T1 / NO-ISKRA
= BODY descended from the same T0 performs controlled cross-domain transfer experiments

T1 / ISKRA VARIANTS
= independent variants start from the same T0 under comparable task/resource contracts

T2
= separately tested competence consolidation / promotion stage
```

## T1 — planned no-ISKRA comparison line

The immediate first experiment is intentionally highly controlled: a clean Micronetworks + V10 LEGO package is to be transferred into a **safe civilian drone simulation** using a detailed recipe, prepared blocks/adapters and explicit PASS/FAIL tests. Its purpose is to test **technology transfer under known instructions**, not creativity.

A second transfer experiment should reduce scaffolding: the direction remains comparable, but the system receives less ready-made implementation and must perform more of the mapping and engineering itself.

A later open-ended experiment can test whether the system can identify a genuinely different application domain without being given the answer in advance.

Safe drone-simulation scope may include battery management, positioning, coverage, redundancy, node loss and recovery. Weapon targeting or attack behavior is outside this research scope.

## T2 — planned skill/competence consolidation

T2 is intended to test a new consolidation mechanism after independent experimental lines have produced validated competence.

Conceptually:

```text
MULTIPLE INDEPENDENT RESULTS / SKILLS
-> COMPARE PROVENANCE + EVIDENCE + BENCHMARKS
-> DEDUPLICATE EQUIVALENT COMPETENCE
-> ADD EVIDENCE / DATA COVERAGE WHEN EQUIVALENT
-> CANDIDATE / CHALLENGER / CHAMPION EVALUATION
-> REQUEST MORE CASES WHEN RESULT IS AMBIGUOUS
-> PROMOTE ONLY UNDER EXPLICIT TEST CONTRACT
-> CREATE UPGRADED DESCENDANT BODY
```

T0 itself must remain unchanged so the comparison remains reproducible.

No T1 or T2 performance result is claimed yet.

---

# Core research model

```text
MODEL / TOOL / EXECUTION
+ EXPERIENCE
+ REAL OUTCOME
+ EVIDENCE
+ VALIDATION
+ HISTORY
-> PERSISTENT COMPETENCE
```

The central hypothesis is that competence should not exist only inside one model or one prompt context. It should be represented as persistent, testable, revisable system competence with provenance and lifecycle.

## Micronetwork lifecycle

```text
EXPERIENCE
-> CANDIDATE
-> EVIDENCE
-> CHALLENGER
-> VALIDATION
-> CHAMPION / REJECT / KEEP TESTING
```

A Champion may later be enriched, challenged, revalidated, replaced or rolled back.

Equivalent independently discovered solutions should not automatically become duplicate skills. They may instead increase evidence, coverage or confidence under a versioned counting rule.

---

# V10 — stateful predictive competence & recovery routing

V10 is not defined only as a speed optimization or cache.

```text
CURRENT TASK / WORLD STATE
+ VERIFIED COMPETENCE
+ ATTEMPT HISTORY
+ PRIOR OUTCOMES
+ FAILURE SIGNATURES
+ CONFIDENCE
-> ROUTE / STRATEGY DECISION
```

Core anti-loop principle:

```text
SAME / EQUIVALENT STATE
+ SAME FAILURE SIGNATURE
+ SAME STRATEGY / ROUTE
+ NO NEW EVIDENCE
=> DO NOT BLINDLY REPEAT
```

Possible decisions include reuse, verify-top-k, alternative competence/LEGO composition, route blocking or canonical full flow.

Full reviewer-safe description:

- [V10_PREDICTIVE_ROUTING.md](V10_PREDICTIVE_ROUTING.md)
- [V10_PREDICTIVE_ROUTING_FAQ.md](V10_PREDICTIVE_ROUTING_FAQ.md)

---

# BODY_FROZEN, Agents, Director and ROBERT

These roles should not be conflated.

```text
BODY_FROZEN T0
= immutable experimental starting organism

AGENTS
= operate inside worlds
+ maintain their own trajectories / CONTINUUM / laboratory history
+ collect data and metadata
+ develop/train/evaluate domain strategies
+ produce candidate competence / skills

DIRECTOR
= observes results
+ audits / compares / ranks
+ evaluates maturation of strategies and competence

ROBERT
= separate execution/runtime body
+ tools / engineering / environment interaction
```

In the intended world/laboratory cycle, weak strategies may be rejected while their historical outcome remains preserved; stronger strategies continue through maturation/ranking. Validated skills can later be candidates for controlled promotion into shared system competence and upgrades of Director/ROBERT, subject to explicit validation and regression contracts.

---

# Public validation history

## Test 2 — lifecycle / persistence hardening

```text
600/600 PASS
126.65 s
0 duplication failures
0 half-promoted objects
```

## Test 3 — historical V10 selective routing run

```text
600/600 PASS
57.61 s
534 REUSE_TOP1
66 VERIFY_TOPK
100/100 known-case correctness
```

The measured speed difference is scoped evidence for this setup, not a universal V10 performance claim.

## Test3 100x v2 — migration closure hardening

```text
60 000 / 60 000 accounted
failed = 0
unresolved_failures = 0
incorrect_routing = 0
restart = 20/20 PASS
```

This retest followed discovery of a weak earlier PASS formula.

## Test 4 — ROOT Terminal / Authority / Recovery

```text
461/461 final regression
1000/1000 controlled pipeline E2E
1000 commands / 20 workers concurrency
20/20 real process restart
0 duplicate/orphan/missing receipt problems
```

## Test 5 — SSI BODY Final Convergence

```text
Stage 12 27/27 = SUPERSEDED after audit
Stage 13 audit retest = PASS
29/29 acceptance
524/524 total regression
0 open blockers
```

## T0 — new experimental baseline

```text
2026-09-05
BODY_FROZEN PRE-ISKRA baseline recorded
CONTINUUM CLOSED
23/23 CONTINUUM tests PASS
22/22 main scenarios PASS
19/19 E2E closure PASS
26/26 final guard PASS
0 active failures
0 invariant violations
0 blockers
```

T0 is a **baseline state**, not an additional closed validation suite replacing TEST 5.

---

# Claim boundaries

SSI V5 does **not** currently claim that:

- it is proven AGI;
- it is conscious;
- every SSI mechanism is production-ready;
- V10 is universally superior to other routing architectures;
- anti-loop/recovery is universally validated;
- every candidate skill is safe to promote;
- T1/T2 experiments have already succeeded;
- future economic performance is guaranteed.

Preferred public statuses include:

```text
VERIFIED_MACHINE_EVIDENCE
DEVELOPMENT_VALIDATED
SUPERSEDED
HISTORICAL_EVIDENCE
IMPLEMENTED_NOT_YET_REPLICATED
T0_BASELINE_RECORDED
PLANNED
HYPOTHESIS
UNKNOWN
```

---

# Public chronology

```text
2026-07-19  root Git commit: MSDI AI v0.01
2026-07-27  public msdi-ai repository
2026-08-01  explicit SSI V5 line appears
2026-08-14  CONTINUUM repository
2026-08-16  SSI_V5_MASTER
2026-08-25  SSI_V5 public research mirror
2026-08-31  scoped 600x persistence/lifecycle hardening PASS
2026-09-01  V10 Hybrid Router historical Test 3
2026-09-02  micronetwork migration closure + TEST 4 ROOT terminal closure
2026-09-03  TEST 5 Stage 12 marked SUPERSEDED after audit
2026-09-03  TEST 5 Stage 13: 29/29 acceptance, 524/524 regression, 0 blockers
2026-09-05  BODY_FROZEN T0 / PRE-ISKRA baseline recorded and sanitized public evidence published
```

---

# Reviewer invitation

The project is designed to be challenged. Useful review includes replication attempts, adversarial tests, false-reuse cases, blind-retry cases, recovery tests, distribution shift, critiques of acceptance gates and comparisons with state of the art.

The standard is:

```text
CLAIM
-> IMPLEMENTATION
-> TEST
-> MACHINE EVIDENCE
-> AUDIT WHAT THE TEST ACTUALLY PROVES
-> PRESERVE FAILURE / WEAK PASS
-> REPAIR
-> RETEST
-> CURRENT CLAIM BOUNDARY
```

The public repository is intended to show not only successful outcomes, but also when an earlier PASS was too weak, when a hypothesis remains unverified and when a future experiment has not yet been run.