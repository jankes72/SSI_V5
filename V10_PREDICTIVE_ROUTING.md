# V10 — Stateful Predictive Competence & Recovery Router

## Status

`DEVELOPMENT_VALIDATED — scoped adaptive-routing / replay / persistence evidence; dedicated anti-loop and adversarial validation still required`

## Core definition

V10 is not designed as a simple cache, a basic semantic router, or merely a latency optimization. Its primary role is **stateful selection of the next action strategy** based on the current problem, available competence, attempt history, prior outcomes, failure signatures and confidence.

In compact form:

```text
V10
= PREDICTIVE COMPETENCE ACCESS
+ STATE / HISTORY AWARENESS
+ CONFIDENCE GATING
+ FAILURE-AWARE ROUTING
+ ANTI-LOOP / RECOVERY DECISION
+ FEEDBACK-DRIVEN ROUTE UPDATE
```

Lower latency may result from correct reuse of validated competence, but **speed is not the primary definition of V10**.

## Why V10 exists

In a long execution task — for example building a program from LEGO-style blocks, repairing an artifact, or later operating ROBERT in an environment such as Tetris — finding a merely "similar answer" is not enough.

The system must distinguish, among other things:

- what has already been completed;
- which strategy was used;
- which block / Champion / route was already attempted;
- what the outcome was;
- whether the same failure signature already occurred;
- whether repeating the same route is still justified;
- whether a different competence, LEGO composition, verification step, or full flow is required.

Routing is therefore defined more broadly:

```text
ROUTING
!= INPUT SIMILARITY ONLY

ROUTING
= INPUT / TASK STATE
+ HISTORY OF ATTEMPTS
+ PRIOR OUTCOMES
+ FAILURE SIGNATURES
+ AVAILABLE VERIFIED COMPETENCE
+ CURRENT CONFIDENCE
+ RECOVERY OPTIONS
```

## Decision core

A simplified V10 contract is:

```text
CURRENT INPUT / STATE
+ MICRONETWORKS / CHAMPIONS
+ ATTEMPT HISTORY
+ OUTCOMES / FAILURES
        |
        v
V10 STATEFUL PREDICTIVE ROUTING
        |
        +-> HIGH CONFIDENCE + VALID HISTORY
        |      -> REUSE_TOP1
        |
        +-> MEDIUM / AMBIGUOUS
        |      -> VERIFY_TOPK
        |
        +-> REPEATED FAILURE / NEGATIVE OUTCOME
        |      -> BLOCK BLIND RETRY
        |      -> MODIFY ROUTE / SELECT ALTERNATIVE / ESCALATE
        |
        +-> LOW / UNKNOWN / CONFLICT
               -> CANONICAL FULL_FLOW
```

Exact lookup and similarity are only parts of this process.

## Anti-loop: do not repeat the same failed strategy without new evidence

A core V10 requirement is to reduce pointless execution loops.

The architectural contract can be written as:

```text
SAME / EQUIVALENT STATE
+ SAME FAILURE SIGNATURE
+ SAME STRATEGY / ROUTE
+ NO NEW EVIDENCE

=> DO NOT BLINDLY REPEAT
```

Instead, the system should move to at least one controlled response:

```text
BLOCK SAME ROUTE
OR
MODIFY PARAMETERS / LEGO COMPOSITION
OR
SELECT ALTERNATIVE CHAMPION / COMPETENCE
OR
VERIFY TOP-K
OR
ESCALATE TO FULL_FLOW
```

This is more important than latency reduction alone. The router should help the system **change how it acts after failure**, rather than only execute the same ineffective path faster.

## V10 + LEGO

LEGO decomposes a large task into small contract-driven blocks. V10 is intended to help select and recombine those blocks according to execution state.

```text
GOAL
-> LEGO DECOMPOSITION
-> BLOCK A
-> BLOCK B
-> TEST
-> FAILURE
-> FAILURE SIGNATURE / OUTCOME
-> V10
   -> do not repeat ineffective composition blindly
   -> reuse verified block where valid
   -> replace / reconfigure weak block
   -> escalate if no safe route exists
-> RETEST
-> EXPERIENCE
```

In this sense, V10 is not a router for one narrow task. It is intended as a competence-selection and recovery layer within multi-step build, repair and execution processes.

## Example: building and later playing Tetris

Tetris is a useful example because it separates two operating levels.

### 1. ROBERT builds / repairs Tetris

```text
BUILD
-> TEST
-> FAILURE / LIMITATION
-> DIAGNOSIS
-> V10 CONSULTS HISTORY
-> REUSE GOOD BLOCKS
-> AVOID KNOWN BAD ROUTE
-> MODIFY / REPLACE BLOCK
-> RETEST
-> OUTCOME
-> EXPERIENCE
```

### 2. ROBERT later plays

```text
BOARD STATE
-> PERCEPTION
-> V10 / COMPETENCE SELECTION
-> ACTION
-> OUTCOME
-> EXPERIENCE
-> NEXT STATE
```

If a strategy repeatedly produces the same failure in a comparable state, prior outcome history should affect the next decision. The goal is not to repeat the same action merely because it appears semantically similar.

## Micronetworks and V10 have different roles

```text
MICRONETWORK
= persistent, evolving, validated competence

CANDIDATE -> CHALLENGER -> CHAMPION
= quality / competition lifecycle

V10
= stateful predictive access
+ confidence gate
+ history / outcome-aware route selection
+ anti-loop / recovery decision
```

Together they form the loop:

```text
EXPERIENCE
-> CANDIDATE
-> CHALLENGER
-> CHAMPION
-> MICRONETWORK
-> V10
-> ACTION / REUSE / VERIFY / FULL_FLOW
-> OUTCOME
-> NEW EXPERIENCE
-> ROUTE / COMPETENCE EVOLUTION
```

## False-reuse protection

A second major risk is `false reuse`: using prior competence in a situation that looks similar but is not actually compatible.

```text
HIGH CONFIDENCE + VALID CONTEXT
-> REUSE

MEDIUM / AMBIGUOUS
-> VERIFY_TOPK

LOW / UNKNOWN / CONFLICT
-> FULL_FLOW

KNOWN NEGATIVE ROUTE IN COMPARABLE STATE
-> DO NOT BLINDLY REUSE
-> RECOVERY / ALTERNATIVE / ESCALATION
```

V10 safety therefore concerns two distinct problems:

1. **false reuse** — selecting an inappropriate prior competence;
2. **failure loop** — re-running the same ineffective strategy despite a known negative outcome.

## Test 3 evidence

Published Test 3 recorded:

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

Test 3 shows that V10 did not operate only as an exact-key cache and that selective routing could avoid part of the expensive full flow within the tested scope.

The measured `57.61 s` versus `126.65 s` in Test 2 is a meaningful performance result, but **it is not the primary V10 hypothesis**.

## What has been shown — and what has not

Current public evidence supports, within its tested scope:

- exact + similarity routing;
- selective `REUSE_TOP1` and `VERIFY_TOPK`;
- route compilation;
- feedback/state growth;
- earlier replay/retry/restart/idempotency hardening in the lifecycle;
- persistence and duplication resistance in tested scenarios.

Public tests should **not** yet be described as proving full anti-loop effectiveness in arbitrary dynamic tasks. Test 3 did not contain enough forced `FULL_FLOW` cases, deliberately repeated failure signatures, or a broad set of unknown/conflicting/adversarial cases.

## Most important next benchmark: stateful anti-loop + recovery

The next benchmark should measure not only speed and routing correctness, but whether strategy changes after failure:

```text
1. CLEAN STATE
2. TASK / WORLD STATE A
3. ROUTE / STRATEGY X
4. FAILURE SIGNATURE F
5. RECORD OUTCOME
6. SAME OR EQUIVALENT STATE A'
7. V10 SEES HISTORY F + X
8. PROVE: NO BLIND X RETRY WITHOUT NEW EVIDENCE
9. ALTERNATIVE ROUTE / MODIFIED LEGO / VERIFY / FULL_FLOW
10. RETEST
11. MEASURE RECOVERY SUCCESS
12. RESTART
13. VERIFY HISTORY PERSISTENCE
```

In parallel, test:

```text
KNOWN                    -> REUSE_TOP1
AMBIGUOUS                -> VERIFY_TOPK
UNKNOWN                  -> FULL_FLOW
DECEPTIVELY SIMILAR      -> NO FALSE REUSE
REPEATED FAILURE         -> NO BLIND LOOP
NEW EVIDENCE AFTER FAIL  -> CONTROLLED RECONSIDERATION
```

## Metrics to report

- routing precision / recall;
- false-reuse rate;
- false-escalation rate;
- confidence calibration;
- repeated-failure suppression rate;
- blind-retry rate;
- recovery success rate;
- alternative-route selection rate;
- time / cost saved versus canonical full flow;
- final task correctness;
- persistence of failure history after restart.

## Short grant/reviewer definition

**V10 is a stateful predictive competence and recovery router. Its role is not only to locate validated competence quickly, but also to use attempt history and outcomes to choose the next path, avoid blindly repeating known ineffective strategies, and decide between reuse, verification, alternative LEGO composition and full flow.**

Public documentation describes this contract and its evidence without publishing the private predictor implementation or the full Micronetwork engine.
