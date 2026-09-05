# SSI V5 — Grant / Technical Reviewer FAQ

**Purpose:** concise answers to likely technical questions from grant reviewers, research groups, sponsors and independent evaluators.  
**Status:** `T0 BASELINE RECORDED / PRE-ISKRA / EXPERIMENTAL RESEARCH SYSTEM`  
**Updated:** `2026-09-05`

SSI V5 is not presented as proven AGI, consciousness or a production-ready autonomous system.

## 0. What changed on 2026-09-05?

SSI V5 now has a public sanitized **T0 / BODY_FROZEN / PRE-ISKRA baseline**.

T0 is the frozen starting point for the next controlled comparative experiments. It is **not TEST 6** and does not replace TEST 5 as the latest closed validation test.

```text
T0 = current experimental baseline
TEST 5 = latest closed validation test
NEXT = T1 controlled comparison
```

T0 evidence:

- [`BODY_FROZEN_T0_PRE_ISKRA.md`](BODY_FROZEN_T0_PRE_ISKRA.md)
- [`evidence/BODY_FROZEN_T0_20260905/README.md`](evidence/BODY_FROZEN_T0_20260905/README.md)

Recorded baseline includes CONTINUUM `CLOSED`, 23/23 CONTINUUM tests PASS, 22/22 main scenarios PASS, 19/19 E2E closure PASS, 26/26 final guard PASS, zero active failures/invariant violations/open blockers, a private BODY inventory count of 1781 files / 587 Python files, and a sanitized Micronetwork/V10 snapshot of 8 micronetworks, 8 modules, 3 layers and V10 ACTIVE.

The formal skill registry counters in the supplied T0 snapshot are zero; the public record does not infer formal skill counts from micronetwork candidate records.

## 1. What exactly is new in SSI V5?

SSI V5 does not claim that every individual mechanism is novel in isolation. The research focus is the combined persistent competence-development architecture:

```text
PERSISTENT STATE
+ EXPERIENCE
+ MICRONETWORK COMPETENCE LIFECYCLE
+ CANDIDATE -> CHALLENGER -> CHAMPION
+ COLLECTIVE COMPETENCE COMPARISON
+ V10 STATEFUL PREDICTIVE COMPETENCE & RECOVERY ROUTING
+ ANTI-LOOP / FAILURE-AWARE ROUTING
+ CONTINUUM
+ LEGO DEVELOPMENT METHODOLOGY
+ EVIDENCE / REPLAY / REGRESSION / PERSISTENCE
```

The central hypothesis is that capability should not live only inside one model or one prompt. It should be represented as persistent, testable, revisable system competence with provenance and lifecycle.

A formal state-of-the-art comparison is still required before strong originality claims such as "nothing similar exists elsewhere."

## 2. How are SSI micronetworks different from ordinary RAG, memory or cache?

RAG primarily retrieves information. A cache primarily returns a previously computed result. SSI micronetworks are intended to represent **validated and evolving competence**, not merely stored text or a previous answer.

```text
EXPERIENCE
-> CANDIDATE
-> EVIDENCE
-> CHALLENGER
-> VALIDATION
-> CHAMPION / REJECT / KEEP TESTING
```

A Champion may later be enriched, challenged, revalidated, replaced or rolled back.

## 3. Is V10 just a clever cache or faster semantic router?

No. The reviewer-safe canonical description is:

> **V10 is a Stateful Predictive Competence & Recovery Router.**

It is designed to combine:

```text
CURRENT TASK / WORLD STATE
+ VERIFIED COMPETENCE
+ ATTEMPT HISTORY
+ PRIOR OUTCOMES
+ FAILURE SIGNATURES
+ CONFIDENCE
-> NEXT ROUTE / STRATEGY
```

Possible decisions include `REUSE_TOP1`, `VERIFY_TOPK`, alternative competence/LEGO composition, blocking blind retry and `FULL_FLOW`.

## 4. What does anti-loop mean?

```text
SAME / EQUIVALENT STATE
+ SAME FAILURE SIGNATURE
+ SAME STRATEGY / ROUTE
+ NO NEW EVIDENCE
=> DO NOT BLINDLY REPEAT
```

This is an intended architectural rule. Existing evidence supports scoped routing/integration/recovery mechanisms; universal anti-loop behavior still requires dedicated future benchmarking.

## 5. What is the current experimental sequence?

```text
T0 = frozen PRE-ISKRA control baseline
T1 = controlled no-ISKRA transfer experiments
T1-ISKRA = variants starting from the same T0
T2 = separate competence consolidation / promotion experiment
```

The first T1 transfer is intentionally highly scaffolded: a clean Micronetworks + V10 LEGO package, detailed recipe, prepared blocks/adapters and explicit tests are used for a safe civilian drone simulation. This primarily tests technology transfer under known instructions.

The second transfer removes much of the ready-made implementation and requires more mapping/engineering by the system. A later open-ended task can test whether the system identifies a new application domain without being given the answer.

## 6. What is planned for T2?

T2 is intended to compare independently produced validated skills/competences.

```text
RESULTS / SKILLS
-> PROVENANCE + EVIDENCE + BENCHMARK
-> DEDUPLICATE EQUIVALENTS
-> ADD DATA / COVERAGE WHEN EQUIVALENT
-> CANDIDATE / CHALLENGER / CHAMPION
-> REQUEST MORE CASES IF AMBIGUOUS
-> PROMOTE ONLY UNDER EXPLICIT CONTRACT
```

An upgraded body should be a descendant of T0. The original T0 remains immutable for reproducibility.

No T2 outcome is claimed yet.

## 7. What did TEST 5 prove?

TEST 5 is the latest closed validation test:

```text
STAGE_12 = SUPERSEDED
STAGE_13_AUDIT_RETEST = PASS
29/29 acceptance PASS
524/524 total regression PASS
0 open blockers
```

An earlier `27/27 PASS` Stage 12 was preserved but superseded after audit found the contract too weak. The system/test boundary was repaired and retested.

Claim boundary: development validation of the tested local SSI BODY control/integration path — not production readiness of the whole system or proof of AGI/consciousness.

## 8. Why preserve SUPERSEDED results?

Because a green test may later turn out to measure too weak a contract. SSI's public methodology is:

```text
PASS
-> AUDIT WHAT WAS ACTUALLY MEASURED
-> PRESERVE WEAK RESULT
-> REPAIR
-> RETEST
-> CURRENT CLAIM
```

This is also conceptually aligned with failure-aware routing: failures and weak outcomes should become future decision information, not disappear from history.

## 9. Are micronetworks tied to one agent or task?

No. The intended architecture is multi-task and multi-space. Shared verified competence is distinct from shared private identity/history.

## 10. Can new micronetworks or competence appear dynamically?

That is an intended core property:

```text
NEW EXPERIENCE
-> NO SUITABLE VERIFIED COMPETENCE
-> FULL FLOW
-> CANDIDATE
-> EVIDENCE
-> CHALLENGER
-> VALIDATION
-> CHAMPION
-> NEW / EXTENDED MICRONETWORK
```

It does not mean one success automatically creates a Champion.

## 11. What happens when multiple agents produce the same skill?

The planned T2 behavior is not to multiply duplicate skill records blindly. Equivalent solutions should increase evidence, data coverage or confidence under a versioned counting rule. If benchmarks cannot distinguish candidates, the system should request additional cases rather than force promotion.

## 12. What are the role boundaries?

```text
BODY_FROZEN T0 = frozen experimental origin
AGENTS = operate in worlds and own laboratory/CONTINUUM trajectories
DIRECTOR = observes, audits, compares, ranks and evaluates
ROBERT = separate execution/runtime/tooling body
```

Agents can generate strategies and competence in worlds; Director evaluates outcomes; ROBERT remains the execution/runtime line. Later controlled skill promotion may strengthen shared system capability.

## 13. Does SSI persist across restarts?

Persistence is a core requirement and must be established through replay/restart evidence rather than inferred from files alone. Existing public test history includes replay/restart/persistence hardening and real process restart checks within scoped tests.

## 14. What is CONTINUUM?

CONTINUUM is the persistent mission-execution layer:

```text
MISSION
-> EXECUTION
-> CHECKPOINT
-> EVIDENCE
-> PAUSE / FAILURE / RESTART
-> RECONCILE
-> CONTINUE
```

T0 records CONTINUUM as `CLOSED` under the published T0 closure summary.

## 15. What is LEGO methodology?

LEGO decomposes large engineering tasks into small contract-driven blocks:

```text
LARGE GOAL
-> DECOMPOSE
-> SMALL BLOCK
-> INPUT / OUTPUT CONTRACT
-> EXECUTION
-> TEST
-> EVIDENCE
-> CHECKPOINT
-> INTEGRATION
-> REGRESSION
```

## 16. What would weaken the SSI hypothesis?

Examples:

- V10 provides speed but unacceptable false reuse;
- failure history does not prevent blind retry;
- recovery does not improve outcomes;
- competence fails to transfer beyond near duplicates;
- Champion accumulation causes degradation;
- deduplication/consolidation loses important competence;
- T1/T2 effects disappear under fair replication;
- future audits reveal that current tests measure weaker boundaries than claimed.

## 17. Does the public repo expose private implementation?

No. It publishes reviewer-safe architecture, measured results, test boundaries, sanitized counts, lineage and claim boundaries. Private source implementation, secrets, raw memory/user data, local paths and implementation-level source maps remain excluded.

## 18. What should reviewers not infer?

Do not infer that:

- SSI is proven AGI or conscious;
- the whole system is production-ready;
- V10 is universally superior;
- every candidate is a formal skill;
- T1/T2 already succeeded;
- future economic outcomes are guaranteed.

## 19. What is the shortest current description for a grant reviewer?

**SSI V5 is a persistent competence-development research architecture. Its current public state includes a frozen PRE-ISKRA T0 baseline, prior scoped validation of persistence/routing/control integration, a stateful V10 competence/recovery routing layer, and a planned controlled experiment series testing cross-domain transfer, independent agent divergence and later evidence-based competence consolidation.**

## 20. Where should a reviewer start?

1. [`BODY_FROZEN_T0_PRE_ISKRA.md`](BODY_FROZEN_T0_PRE_ISKRA.md)
2. [`evidence/BODY_FROZEN_T0_20260905/README.md`](evidence/BODY_FROZEN_T0_20260905/README.md)
3. [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md)
4. [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md)
5. [`evidence/TEST5_FINAL_CONVERGENCE_20260903.md`](evidence/TEST5_FINAL_CONVERGENCE_20260903.md)
6. [`V10_PREDICTIVE_ROUTING.md`](V10_PREDICTIVE_ROUTING.md)
7. [`evidence/README.md`](evidence/README.md)
