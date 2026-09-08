# V10 Stateful Predictive Competence & Recovery Router — Reviewer FAQ

## Is V10 only a router or cache?

No. V10 is designed as a **stateful predictive competence and recovery router**. In addition to similarity and confidence, it considers attempt history, prior outcomes and known failure signatures when selecting the next execution path.

```text
CURRENT STATE
+ AVAILABLE VERIFIED COMPETENCE
+ ATTEMPT HISTORY
+ PRIOR OUTCOMES / FAILURES
-> V10
-> REUSE / VERIFY / ALTERNATIVE / FULL_FLOW
```

Exact-cache behavior is only one possible path.

## What does V10 predict?

At the architectural level, V10 estimates not only whether existing competence matches the current problem, but also **whether a given path still makes sense in light of execution history**.

A decision may result in:

- `REUSE_TOP1`;
- `VERIFY_TOPK`;
- an alternative competence or LEGO composition;
- blocking blind retry of a known ineffective route;
- `FULL_FLOW` for unknown/conflict/low-confidence cases.

## Why is attempt history important?

In multi-step tasks, input similarity alone is insufficient. The system should know whether a strategy was already used in a comparable state and what outcome it produced.

```text
SAME / EQUIVALENT STATE
+ SAME FAILURE SIGNATURE
+ SAME STRATEGY
+ NO NEW EVIDENCE
=> DO NOT BLINDLY REPEAT
```

This is the core anti-loop idea in V10.

## What does anti-loop mean?

Anti-loop means that the system should not keep cycling through the same ineffective strategy without new information.

After detecting a repeated negative outcome, V10 should consider:

```text
BLOCK SAME ROUTE
OR
MODIFY PARAMETERS / LEGO COMPOSITION
OR
SELECT ALTERNATIVE CHAMPION
OR
VERIFY TOP-K
OR
ESCALATE TO FULL_FLOW
```

This distinguishes V10 from a simple "find something similar and reuse it" mechanism.

## How does V10 work with LEGO?

LEGO decomposes a large problem into smaller blocks. V10 helps decide which verified blocks can be reused, which should be changed, and when the current composition is leading to repeated failure.

```text
GOAL
-> LEGO BLOCKS
-> EXECUTION
-> TEST
-> FAILURE
-> HISTORY / OUTCOME
-> V10
-> REUSE GOOD BLOCKS
-> REPLACE / RECONFIGURE BAD PATH
-> RETEST
```

## Why is Tetris a useful example?

Because it separates two different operating layers.

First, ROBERT may build and repair Tetris:

```text
BUILD -> TEST -> FAILURE -> DIAGNOSIS -> ROUTE CHANGE -> RETEST
```

Later, ROBERT may play:

```text
BOARD STATE -> PERCEPTION -> COMPETENCE SELECTION -> ACTION -> OUTCOME -> NEXT STATE
```

If a strategy repeatedly fails in comparable states, prior outcomes should influence the next decision.

## Is speed the main advantage of V10?

No. Speed is an important possible consequence of correct reuse, but the broader role is:

```text
FAST ACCESS
+ SAFE REUSE
+ HISTORY-AWARE DECISION
+ FAILURE-AWARE RECOVERY
+ ANTI-LOOP
```

Test 3 recorded `57.61 s` versus `126.65 s` for Test 2 within that benchmark, but reducing V10 to this speed result would be an incomplete description of the architecture.

## What public evidence is already available?

Test 3 recorded:

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

Earlier lifecycle stress tests also covered replay, retry, restart, concurrency, persistence and idempotency.

## Have public tests already proven full anti-loop behavior?

No. This is an important claim boundary.

Current evidence supports routing, replay/persistence hardening and selective reuse/verify, but a dedicated benchmark still needs to deliberately trigger:

- the same failure signature;
- a comparable state;
- repeated ineffective strategy;
- an alternative recovery path;
- restart and post-restart retry behavior.

Only then can anti-loop performance be reported quantitatively.

## What metrics are appropriate for V10?

Not latency alone. Important metrics include:

- false-reuse rate;
- false-escalation rate;
- routing precision/recall;
- confidence calibration;
- repeated-failure suppression rate;
- blind-retry rate;
- recovery success rate;
- alternative-route selection rate;
- persistence of failure history;
- final task correctness;
- time/cost saved versus canonical full flow.

## Shortest reviewer answer

**V10 is not merely a faster router. It is a decision layer over persistent competence: it uses state, confidence, attempt history and outcomes to decide what to reuse, what to verify, what not to repeat, and when to change strategy or return to full flow.**

Public documentation describes this function without publishing private V10 source code or the full Micronetwork engine.
