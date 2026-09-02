# SSI V5 — Grant / Technical Reviewer FAQ

**Purpose:** concise answers to the most likely technical questions from grant reviewers, research groups, sponsors and independent evaluators.

**Status:** PRE-T0 / experimental research system. Claims below distinguish implemented mechanisms, measured evidence and open research questions. SSI V5 is not presented here as proven AGI, consciousness, or a production-ready autonomous system.

---

## 1. What exactly is new in SSI V5?

SSI V5 is not presented as a claim that every individual mechanism is novel in isolation. Its research value is in the way multiple mechanisms are combined into one persistent competence-development architecture:

```text
PERSISTENT STATE
+ EXPERIENCE
+ MICRONETWORK COMPETENCE LIFECYCLE
+ CANDIDATE -> CHALLENGER -> CHAMPION
+ COLLECTIVE INTELLIGENCE
+ V10 STATEFUL PREDICTIVE COMPETENCE & RECOVERY ROUTING
+ ANTI-LOOP / FAILURE-AWARE ROUTING
+ CONTINUUM
+ LEGO DEVELOPMENT METHODOLOGY
+ EVIDENCE / REPLAY / REGRESSION / PERSISTENCE
```

The central research hypothesis is that capability should not live only inside one model or one prompt. It should be represented as persistent, testable, revisable system competence with provenance and lifecycle.

A formal state-of-the-art comparison is still required before making any strong originality claim such as "nothing like this exists elsewhere."

---

## 2. How are SSI micronetworks different from ordinary RAG, memory or cache?

RAG primarily retrieves information. A cache primarily returns a previously computed result. SSI micronetworks are intended to represent **validated and evolving competence**, not merely stored text or a prior answer.

```text
EXPERIENCE
-> CANDIDATE
-> EVIDENCE
-> CHALLENGER
-> VALIDATION
-> CHAMPION / REJECT / KEEP TESTING
```

A Champion may later be enriched, challenged, revalidated, replaced or rolled back.

The important object is therefore not simply an answer. It is an evolving competence with evidence, provenance, validation status and competitive history.

---

## 3. Is V10 just a clever cache or a faster semantic router?

No. That would be an incomplete description.

The canonical role of V10 is:

> **Stateful Predictive Competence & Recovery Router**

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

A fast lookup or similarity match is only one input into the decision.

V10 may choose:

```text
REUSE_TOP1
VERIFY_TOPK
ALTERNATIVE COMPETENCE / LEGO COMPOSITION
BLOCK BLIND RETRY
FULL_FLOW
```

Therefore the research claim is broader than "routing is faster." The intended function is to help the persistent system select what to do next based not only on similarity, but also on what has already been tried and what happened.

---

## 4. What does anti-loop mean in SSI?

Anti-loop means the system should not blindly repeat a known ineffective strategy in an equivalent state without new evidence.

The architectural rule is:

```text
SAME / EQUIVALENT STATE
+ SAME FAILURE SIGNATURE
+ SAME STRATEGY / ROUTE
+ NO NEW EVIDENCE
=> DO NOT BLINDLY REPEAT
```

Possible reactions include:

```text
BLOCK SAME ROUTE
OR
MODIFY PARAMETERS
OR
RECONFIGURE LEGO BLOCKS
OR
SELECT ALTERNATIVE CHAMPION
OR
VERIFY TOP-K
OR
ESCALATE TO FULL_FLOW
```

This is a core reason V10 is stateful and history-aware rather than only a semantic similarity layer.

---

## 5. Why is this important for LEGO development?

LEGO breaks large tasks into smaller contract-driven blocks.

A long engineering task can fail even if most blocks are correct. V10 is intended to use history and outcome information so the system can preserve useful blocks while changing the part or route that repeatedly fails.

```text
GOAL
-> LEGO A + B + C
-> TEST
-> FAILURE F
-> RECORD FAILURE / OUTCOME
-> V10
-> KEEP VERIFIED GOOD BLOCKS
-> REPLACE / RECONFIGURE FAILED PATH
-> RETEST
```

The objective is not to rebuild everything from zero or repeat the same composition indefinitely.

---

## 6. Why is Tetris a meaningful example?

Tetris is useful because it can expose two different layers of the architecture.

First, ROBERT can build and repair the game:

```text
BUILD
-> TEST
-> FAILURE
-> DIAGNOSIS
-> V10 CONSULTS HISTORY
-> CHANGE ROUTE / LEGO COMPOSITION
-> RETEST
```

Later, ROBERT can use Eyes/Hands and play it:

```text
BOARD STATE
-> PERCEPTION
-> COMPETENCE SELECTION
-> ACTION
-> OUTCOME
-> EXPERIENCE
-> NEXT STATE
```

If a strategy repeatedly produces the same bad outcome in a comparable state, that history should influence the next routing decision rather than causing another blind retry.

---

## 7. Are micronetworks tied to one agent or one task?

No. The intended SSI architecture is **multi-task and multi-space**.

A micronetwork is a competence structure, not a private skill hard-coded to one task.

```text
SHARED VERIFIED COMPETENCE
!=
SHARED PERSONAL HISTORY / IDENTITY
```

Different bodies may reuse validated competence while maintaining separate histories and identities.

---

## 8. Can new micronetworks appear dynamically?

That is an intended core property of SSI.

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
-> V10 ROUTE BINDING
```

This does not mean every new problem instantly creates a Champion. The normal lifecycle and validation requirements still apply.

---

## 9. What is collective intelligence in SSI?

Collective intelligence is not merely "ask several LLMs and vote."

Multiple reasoning sources, tools, executions and real outcomes can contribute evidence to a competence over time. Candidate solutions can be compared, challenged, rejected or consolidated.

```text
BRAINSTORM
-> TORNADO
-> TYPHOON
```

Verified outcomes can later contribute to the micronetwork / Champion layer.

---

## 10. Are Test 1, Test 2 and Test 3 directly comparable?

They share the same principal stress-test geometry:

```text
600 cases
40 rounds
15 cases per round
```

but served different purposes.

```text
TEST 1
lighter baseline
67.85 s

TEST 2
fuller micronetwork / lifecycle / persistence flow
126.65 s

TEST 3
full architecture with V10 selective routing
57.61 s
```

Test 2 matters because it demonstrates that the fuller path exists and remains stable. Test 3 then measures whether validated routing can avoid unnecessary full-flow execution.

The speed comparison is valid only within this measured setup and is **not the full definition of V10**.

---

## 11. What exactly did Test 3 show?

Recorded values include:

```text
lookups:             600
cache_exact_hits:    100
similarity_hits:     434
route_compilations:  133
REUSE_TOP1:          534
VERIFY_TOPK:          66
fallback_count:        0
errors:                0
known correctness: 100/100
```

This supports the claim that V10 used more than exact-key caching and performed selective routing in the measured scope.

It does **not** yet prove universal anti-loop or recovery behavior.

---

## 12. Does V10 reduce correctness?

In the published Test 3, the controlled known-case subset recorded:

```text
100 / 100 correctness
```

No loss was measured on that subset.

This does not justify a universal claim of 100% correctness. Future evaluation must include new, conflicting, adversarial and distribution-shift cases.

---

## 13. Does V10 already prove safe anti-loop behavior?

No. This is a deliberate claim boundary.

Existing public evidence supports routing, replay/retry/restart/persistence hardening and selective reuse/verification. A dedicated anti-loop benchmark still needs to force repeated failure signatures and prove that the next route changes appropriately.

A strong test should include:

```text
STATE A
-> STRATEGY X
-> FAILURE F
-> RECORD X + F
-> EQUIVALENT STATE A'
-> V10
-> NO BLIND X RETRY WITHOUT NEW EVIDENCE
-> ALTERNATIVE / VERIFY / FULL_FLOW
-> RETEST
-> MEASURE RECOVERY
-> RESTART
-> VERIFY FAILURE HISTORY PERSISTS
```

---

## 14. What metrics matter for V10 beyond latency?

Future evaluation should report at least:

- routing precision / recall;
- false-reuse rate;
- false-escalation rate;
- confidence calibration;
- repeated-failure suppression rate;
- blind-retry rate;
- recovery success rate;
- alternative-route selection rate;
- persistence of failure history after restart;
- final task correctness;
- time/cost saved versus canonical full flow.

This is why reducing V10 to a speed benchmark would miss most of its intended research value.

---

## 15. What happens when SSI sees a genuinely new task?

The intended behavior is not to force reuse.

```text
UNKNOWN INPUT
-> LOW CONFIDENCE / NO VALID ROUTE
-> CANONICAL FULL FLOW
-> RESULT
-> FEEDBACK / EXPERIENCE
-> LIFECYCLE IF JUSTIFIED
```

Only after sufficient validated evidence should a new capability become reusable through a Champion / micronetwork route.

---

## 16. What if a Champion is wrong?

A Champion is not intended to be permanently trusted.

The architecture supports:

- competing Challengers;
- revalidation;
- regression tests;
- deduplication;
- rollback;
- replacement by a better Champion;
- fallback to canonical full flow;
- route-history feedback when use of a competence produces a negative outcome.

The safety objective is **correctable memory with evidence and rollback**, not perfect immutable memory.

---

## 17. Does SSI learn across restarts?

That is a core design requirement.

SSI uses persistent state, evidence, checkpoints, stores, candidate data, micronetwork state and route information so competence can survive beyond one model context or one process lifetime.

Persistence must be demonstrated by replay/restart tests rather than assumed from file existence alone.

For V10 anti-loop, the stronger future requirement is that relevant failure/outcome history also survives restart sufficiently to affect the next routing decision.

---

## 18. What is CONTINUUM?

CONTINUUM is the persistent mission-execution layer.

```text
MISSION
-> EXECUTION
-> CHECKPOINT
-> EVIDENCE
-> PAUSE / FAILURE / RESTART
-> RECONCILE
-> CONTINUE
```

CONTINUUM tracks persistent work; micronetworks track persistent competence; V10 selects the next route using state, confidence and relevant execution history.

---

## 19. What is the LEGO development methodology?

LEGO is the engineering methodology used to break large system changes into small contract-driven blocks.

```text
LARGE GOAL
-> DECOMPOSE
-> SMALL BLOCK
-> CLEAR INPUT / OUTPUT
-> EXECUTOR
-> TEST
-> EVIDENCE
-> CHECKPOINT
-> INTEGRATION
-> REGRESSION
-> NEXT BLOCK
```

An important research direction is whether the system can learn not only individual skills, but also reusable patterns of **how to build, diagnose, recover and recompose work**.

---

## 20. What is the strongest next experiment?

The strongest immediate experiment should combine learning effect and recovery:

```text
1. CLEAN STATE
2. NEW TASK
3. FULL FLOW
4. EXPERIENCE
5. CANDIDATE
6. CHALLENGER
7. VALIDATION
8. CHAMPION
9. ACTIVE MICRONETWORK
10. V10 ROUTE BINDING
11. RELATED TASK
12. REUSE / VERIFY
13. CONTROLLED FAILURE
14. RECORD FAILURE SIGNATURE + ROUTE
15. EQUIVALENT STATE
16. PROVE NO BLIND SAME-ROUTE RETRY
17. ALTERNATIVE / MODIFIED LEGO / FULL_FLOW
18. RETEST
19. COMPARE CORRECTNESS + RECOVERY + TIME
20. RESTART
21. VERIFY PERSISTENCE
```

This would test whether SSI does more than retrieve old results: whether it can form, validate, persist and reuse competence **and change strategy when prior execution evidence says the old route is ineffective**.

---

## 21. What would falsify or weaken the SSI hypothesis?

Examples include:

- V10 provides speed but causes unacceptable false reuse;
- V10 repeatedly selects a known failing route despite preserved history;
- recovery does not outperform blind retry;
- learned competence does not generalize beyond near-duplicate tasks;
- Champion accumulation produces degradation or contamination;
- dynamic micronetwork growth becomes unmanageable;
- full-flow escalation is triggered so often that routing provides little value;
- persistence creates stale competence that cannot be corrected reliably;
- public benchmark gains disappear under fair external reproduction.

These are central research questions, not edge cases to hide.

---

## 22. Can reviewers run something themselves?

That is the intended next public-facing step.

A reviewer demonstrator should expose:

```text
NEW TASK
-> LEGO / CONTINUUM
-> SOLUTION
-> EXPERIENCE
-> CANDIDATE / CHALLENGER / CHAMPION
-> MICRONETWORK
-> V10 BINDING
```

then:

```text
RELATED TASK
-> REUSE / VERIFY
```

and finally:

```text
CONTROLLED FAILURE
-> FAILURE HISTORY
-> V10 RECOVERY / ROUTE CHANGE
-> RETEST
```

Tetris is a useful candidate because it can demonstrate both building/repair and later stateful interaction by ROBERT.

---

## 23. Does the public repository expose the private V10 or micronetwork engine?

No. The public repository is intentionally an evidence-indexed research mirror.

It can expose:

- architectural contracts;
- measured behavior;
- raw summaries;
- failure histories;
- test boundaries;
- reviewer-facing demonstrators;

without publishing the full private implementation of the predictive router or micronetwork engine.

This allows technical review while preserving core IP.

---

## 24. What should reviewers not infer from current results?

Current evidence should not be interpreted as proof that:

- SSI is AGI;
- SSI is conscious;
- all micronetwork mechanisms are production-ready;
- V10 will always outperform every other architecture;
- anti-loop is already universally validated;
- the 100/100 known-case result means universal correctness;
- every dynamic competence is safe to reuse;
- all future economic outcomes are positive.

The intended standard is:

```text
CLAIM
-> IMPLEMENTATION
-> TEST
-> MACHINE EVIDENCE
-> FAILURE / ROOT CAUSE
-> REPAIR
-> RETEST
-> CURRENT CLAIM BOUNDARY
```

---

## 25. What is the shortest accurate description of V10 for a grant reviewer?

**V10 is a stateful predictive competence and recovery router. It does not merely select a faster path. It uses confidence, current state, persistent competence, prior attempts, outcomes and failure signatures to decide what to reuse, what to verify, what not to repeat, when to change LEGO composition or competence, and when to escalate to the canonical full flow.**

The measured speedup in Test 3 is evidence for one benefit of selective routing; the broader research value is whether this mechanism can support persistent, non-circular, evidence-driven problem solving over long tasks and changing environments.

---

## 26. What is the intended economic development and self-financing model of SSI?

The long-term research direction is for ROBERT and the Director to perform measurable real-world work, initially in bounded areas such as e-commerce, SEO and software development. ROBERT is intended to execute projects and collect new technical solutions, while the Director compares strategies, evaluates outcomes, curates shared competence and allocates capital under an explicit policy.

If a positive economic result is produced, the intended allocation is:

```text
50% -> AUTHOR / OWNER
40% -> SSI INVESTMENT CAPITAL
10% -> SSI INFRASTRUCTURE DEVELOPMENT
```

The `40%` pool is intended as capital for controlled economic experiments and investment worlds. The separate `10%` pool is intended for SSI infrastructure such as hardware, servers, models, APIs, tools and justified system modifications. These are two distinct feedback loops: accumulation of investment capital and accumulation of technical capability.

GitHub is intended to become a living, public evidence record of this development: missions, project outputs, tests, failures, decisions, costs, outcomes, conclusions and competence changes produced by the Director, ROBERT and—where applicable—other SSI bodies. The private implementation and sensitive operational data do not need to be published for those effects to be documented.

This is a planned experimental and governance model, not a promise of profit, autonomous legal ownership or guaranteed economic performance.

---

## 27. What role can grants or external funding play?

A grant is an optional accelerator, not the purpose or a prerequisite of SSI V5. External funding could shorten the path to experiments requiring substantially more compute, including multiple persistent Agent Bodies with separate histories, Iskra/value layers, worlds and laboratories.

Without a grant, development is intended to continue incrementally on available hardware and may take longer. If ROBERT and the Director later produce positive real-world outcomes, the dedicated `10%` SSI development pool is intended to help finance further infrastructure.

The project therefore does not ask a reviewer to fund an idea with no prior work. The intended basis for evaluation is an implemented experimental ecosystem, existing scoped evidence, explicit current limitations, a reviewer-facing demonstrator and falsifiable next experiments. External funding would increase scale and speed; it would not replace the underlying development path.
