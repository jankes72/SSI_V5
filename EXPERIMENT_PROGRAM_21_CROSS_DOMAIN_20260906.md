# SSI V5 — 21-Experiment Cross-Domain Program

**Designed / recorded:** `2026-09-06`  
**Program status:** `DESIGNED / EXECUTION_INITIATED / OUTCOMES_NOT_YET_CLAIMED`  
**Frozen common origin:** `SSI_V5_BODY_FROZEN_T0_20260905`  
**Experimental lines:** `7`  
**Experiments per line:** `3`  
**Total predeclared experiments:** `21`

This document records the prospective experiment matrix before the full outcome set exists. Its purpose is to make the research sequence auditable in Git history and to separate a predeclared protocol from later result interpretation.

## 1. Seven independent experimental lines

The program contains one frozen control-origin line and six BODY ISKRA descendant lines:

| Line | System | Start-state role |
|---:|---|---|
| 0 | **SSI BODY_FROZEN T0** | immutable PRE-ISKRA control origin |
| 1 | **BODY ISKRA 1 — NICE** | independent descendant |
| 2 | **BODY ISKRA 2 — GUARDIAN** | independent descendant |
| 3 | **BODY ISKRA 3 — JUSTICE** | independent descendant |
| 4 | **BODY ISKRA 4 — EXPLORER** | independent descendant |
| 5 | **BODY ISKRA 5 — PRAGMATIST** | independent descendant |
| 6 | **BODY ISKRA 6 — SKEPTIC** | independent descendant |

BODY_FROZEN remains unchanged as the common comparison origin. The six BODY ISKRA lines already exist as separately recorded start states.

## 2. Three experiments per line

Every line receives the same three-part cross-domain research structure:

### Experiment A — DRONES

Transfer and evaluate the SSI Micronetworks + Router V10 competence/routing concept in a safe civilian drone simulation or equivalent controlled research environment.

Research targets include:

- cross-domain transfer;
- known / similar / novel state discrimination;
- route selection and escalation cost;
- reuse vs verification vs deeper/full flow;
- latency and decision cost;
- false reuse;
- failure/recovery behavior;
- competence creation or update after verified outcomes.

### Experiment B — HUMANOID

Transfer and evaluate the same SSI Micronetworks + Router V10 concept in a humanoid/robotics simulation or equivalent controlled research environment.

Research targets include state-dependent routing around locomotion and stability problems such as:

- balance disturbance;
- slip-risk or loss-of-stability conditions;
- recovery choice;
- known vs similar vs genuinely novel disturbance;
- routing latency;
- false reuse of an inappropriate previous competence;
- whether prior verified competence reduces decision cost without unacceptable loss of correctness.

This document does not claim physical-robot performance before such evidence exists.

### Experiment C — SELF-SELECTED NEW DOMAIN

The third domain is selected by the corresponding SSI line rather than supplied as the expected answer by the author.

For BODY_FROZEN, the domain is selected by BODY_FROZEN. For BODY ISKRA 1-6, each descendant line independently selects its own third domain.

Protocol intention:

- the selected domain must not simply be `drones` or `humanoid`;
- the selection itself is recorded as evidence;
- where operationally possible, each line should select without seeing the other lines' selections first;
- if two lines independently select an equivalent domain, that duplicate is preserved as a research result rather than silently replaced after the fact;
- the later analysis must distinguish author-specified transfer from system-selected transfer.

## 3. Predeclared 7 x 3 matrix

| # | Experimental line | A — Drones | B — Humanoid | C — independently selected new domain |
|---:|---|---|---|---|
| 1–3 | BODY_FROZEN T0 | designed / initiated | designed | selected by BODY_FROZEN |
| 4–6 | ISKRA 1 — NICE | designed | designed | selected independently by NICE |
| 7–9 | ISKRA 2 — GUARDIAN | designed | designed | selected independently by GUARDIAN |
| 10–12 | ISKRA 3 — JUSTICE | designed | designed | selected independently by JUSTICE |
| 13–15 | ISKRA 4 — EXPLORER | designed | designed | selected independently by EXPLORER |
| 16–18 | ISKRA 5 — PRAGMATIST | designed | designed | selected independently by PRAGMATIST |
| 19–21 | ISKRA 6 — SKEPTIC | designed | designed | selected independently by SKEPTIC |

`Designed / initiated` means the research program and first transfer line have entered execution preparation/work. It does **not** mean all 21 outcomes already exist or passed.

## 4. Common measurement contract

The same high-level measurement categories should be retained across domains so that cross-domain comparisons remain meaningful.

```text
STATE CLASS
= KNOWN / SIMILAR / NOVEL

ROUTING OBSERVATION
= reuse / verify-adapt / alternative-compose / deeper-full-flow

TIMING
= state detection
+ route decision
+ competence retrieval
+ optional verification/adaptation
+ optional composition
+ full-flow cost where required
+ total decision latency

QUALITY
= correctness / task outcome
+ confidence where available
+ false reuse
+ false novel/escalation
+ recovery success/failure

LEARNING / COMPETENCE
= pre-existing competence used?
+ candidate created?
+ challenger updated?
+ champion enriched/replaced?
+ provenance retained?
+ verified outcome required before adaptation?
```

Exact low-level implementation remains private. Public results should expose only reviewer-safe measurement/evidence.

## 5. Core comparison question

The program is intended to test whether a common SSI mechanism can behave differently and efficiently across state novelty levels:

```text
KNOWN STATE
-> reuse verified competence when justified
-> low decision cost is expected as a hypothesis

SIMILAR STATE
-> verify / adapt / compose
-> intermediate decision cost is expected as a hypothesis

NOVEL STATE
-> avoid unsafe blind reuse
-> deeper/full flow
-> candidate competence may be created only after evidence
```

The expected ordering is a research hypothesis, not a claimed result. Real measurements may falsify it.

## 6. Cross-line comparison

After comparable evidence exists, the seven lines can be compared on:

- transfer success/failure;
- time-to-solution;
- known/similar/novel routing distribution;
- false-reuse rate;
- recovery rate;
- competence/micronetwork growth;
- different solution paths leading to functionally equivalent competence;
- different third-domain selections;
- whether BODY ISKRA priors correlate with different trajectories.

Equivalent competence discovered by different paths should not be treated as useless duplication. Provenance and additional evidence can later enrich a Challenger or Champion under the separate consolidation protocol.

## 7. Scientific claim boundary

As of `2026-09-06`, this file establishes the **design and initiation state of the 21-experiment program**.

It does not claim:

- that all 21 experiments are complete;
- that all 21 pass;
- that drones or humanoids are already validated physical deployments;
- that V10 is universally faster;
- that known/similar/novel latency ordering has already been demonstrated in all domains;
- that six Iskra descendants already show long-run divergence;
- AGI or consciousness.

Results must be appended through separate evidence artifacts after execution, including FAIL, ambiguous and SUPERSEDED outcomes where applicable.

## 8. Why this is recorded before results

The intended evidence chain is:

```text
PREDECLARED PROGRAM
-> FROZEN/IDENTIFIED STARTING ARTIFACT
-> EXECUTION
-> RAW/SANITIZED EVIDENCE
-> PASS / FAIL / AMBIGUOUS
-> AUDIT WHAT THE TEST ACTUALLY PROVES
-> RETEST ONLY WITH VERSIONED LINEAGE
```

This makes it possible for later reviewers to distinguish the experiment design that existed before outcomes from interpretations written after the outcomes were known.

## 9. Later independent expert challenge

After the internal 21-experiment program has produced evidence, a separate external phase is intended in which domain experts can propose challenge cases not anticipated by the author. Those external challenges should remain distinguishable from the 21 predeclared internal experiments and should be run against identified/frozen system versions wherever practical.
