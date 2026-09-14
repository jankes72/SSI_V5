# SSI V5 — Public Showcase + Measured Cross-Domain Evidence — 2026-09-14

**Status:** `PUBLIC SHOWCASE DEPLOYED / MEASURED SOFTWARE-DOMAIN EVIDENCE RECORDED`  
**Public showcase:** https://echotrip.jankespawel98.workers.dev/  
**Repository role:** public evidence mirror; proprietary SSI implementation remains private.

## Executive statement

On 2026-09-14 the SSI V5 cross-domain research showcase was deployed publicly. The public site presents the same higher-level SSI competence-management architecture in two materially different software domains:

1. distributed drone / swarm coordination;
2. humanoid motion / stability.

The showcase is not the source of truth for the measurements. The source of truth is the recorded experiment output produced by the domain runners and evidence files. The site is a reviewer-facing visualization layer over those results.

The timing values documented here are **measured values produced by executed software experiments**. They are not decorative numbers and were not inserted to make the presentation look faster.

Two timing classes must remain distinct:

```text
WALL-CLOCK / FLOW-COST TIME
= actual elapsed computation/runtime measurement from the executed software run

SIMULATION TIME
= actual timestamp produced by the simulation clock during the executed scenario

NEITHER
= certified physical-world drone or physical-humanoid timing
```

Therefore `simulation time` is a real measured result of the executed simulator, but it must not be re-labelled as physical robot response time.

## Public deployment

Public reviewer URL:

https://echotrip.jankespawel98.workers.dev/

The deployed showcase is intended to make the following evidence understandable without exposing proprietary SSI internals:

```text
SSI CORE
-> DOMAIN ADAPTER
-> DRONE / HUMANOID LAB
-> FLOW / LEARNING / RECOVERY
-> CROSS-CONSOLIDATION
-> BEFORE / AFTER
-> REGRESSION GATE
-> EVIDENCE
```

The site includes a bilingual reviewer-facing presentation, measured flow/timing views, domain-transfer explanation, cross-consolidation visualization, humanoid failure/recovery visualization, evidence views and explicit claim boundaries.

## Drone-domain measured results

The drone benchmark was executed across:

```text
11 scenarios
x 4 execution profiles
= FAST / PARTIAL / FULL / MAX-SAFETY measurements
```

The values below are actual measurements from the executed software benchmark.

### Example — route_blocked

| Flow | Measured flow cost |
|---|---:|
| FAST | 12.265 ms |
| PARTIAL | 17.394 ms |
| FULL | 22.300 ms |
| MAX / SAFETY | 30.105 ms |

### Example — multi_fault

| Flow | Measured flow cost |
|---|---:|
| FAST | 21.835 ms |
| PARTIAL | 30.966 ms |
| FULL | 39.700 ms |
| MAX / SAFETY | 53.595 ms |

The important observation is not only the absolute millisecond value. The benchmark makes execution-depth cost visible under the same laboratory architecture:

```text
FAST < PARTIAL < FULL < MAX / SAFETY
```

### Cross-consolidation measurement

A public demonstrator cross-consolidation hook executed in:

```text
0.147 ms
```

This value is specifically the measured software-demonstrator consolidation hook. It is **not** claimed to be a complete production Router S10 global-consolidation latency.

Observed competence-pool availability changed from:

```text
before: 6 / 5 / 5
 after: 8 / 8 / 8
```

Across the comparative drone benchmark, the median post-consolidation flow-cost effect was approximately:

```text
1.384x speedup
~27.76% lower median flow cost
```

This is a scoped result for this benchmark and must not be generalized to every task or every future physical system.

### Preserved regression — wind_corridor

The benchmark also produced an important negative result. In the targeted `wind_corridor` post-consolidation comparison, outcome regression was observed:

```text
PASS -> FAIL
```

across the tested flow profiles in that comparison.

This result is intentionally preserved and shown publicly. It demonstrates why SSI requires a post-consolidation regression gate rather than treating consolidation as automatically beneficial.

The correct conclusion is therefore:

```text
CONSOLIDATION CAN REDUCE COST
BUT
CONSOLIDATION BENEFIT IS NOT UNIVERSAL
AND MUST BE RE-VALIDATED
```

## Humanoid-domain measured results

The humanoid branch was executed across the H00-H14 scenario family, including baseline and consolidated paths. The comparative data set contains:

```text
15 scenarios
x baseline / consolidated
= 30 measured scenario runs
```

The humanoid self-test suite also recorded:

```text
13 / 13 PASS
```

### H00 — learning-loop timing

Measured simulation-clock events include:

```text
hard stop = 2.90 s simulation time
PASS_AFTER_LEARNING = 11.46 s simulation time
```

These are actual simulator timestamps from the executed run.

### H01 — slip / retained strategy

In the first forced slip attempt:

```text
RECOVERING = 0.14 s simulation time
FALL       = 0.34 s simulation time
```

After retaining the resulting experience, the retry used:

```text
PREEMPTIVE_SLIP_PREP
```

and completed without the corresponding fall observed in the first attempt.

The meaningful evidence is therefore the before/after difference:

```text
ATTEMPT 1 -> FALL
RETAIN EXPERIENCE
ATTEMPT 2 -> PREEMPTIVE PREPARATION -> NO FALL
```

This is software-domain evidence of retained failure experience changing a later path. It is not physical-humanoid validation.

### H13 — recovery-state timing

A measured software-state transition recorded:

```text
FALL -> STABILIZED = 0.08 s simulation time
```

Again, this is an actual simulator-clock interval from the executed run, not a claim that a physical humanoid can stand up in 80 ms.

## What the transfer demonstrates

The two domains do not share the same physical skill. A drone navigation skill is not claimed to become a humanoid balance skill.

What is transferred is the higher-level SSI experiment and competence-management structure:

```text
NEW PROBLEM
-> STATE
-> FLOW SELECTION
-> EXPERIENCE
-> RETENTION
-> CANDIDATE / CHALLENGER / CHAMPION LOGIC
-> TRANSFER / REUSE
-> CROSS-CONSOLIDATION
-> RE-VALIDATION
-> REGRESSION GATE
-> EVIDENCE
```

The drone domain stresses distributed units, local-versus-collective experience, routing, faults and cross-grid consolidation.

The humanoid domain stresses coupled whole-body state, slip, failure, recovery, prediction, retained failure experience and before/after behavior.

The current evidence therefore supports **implemented and measured transfer of the SSI competence-management methodology into two different software research domains**.

## External-challenge path

The preferred next validation step is an externally supplied problem that SSI has not previously seen.

Intended protocol:

```text
EXTERNAL PARTNER DEFINES PROBLEM
-> CHALLENGE FROZEN BEFORE RUN
-> PASS / FAIL / INCONCLUSIVE CRITERIA DECLARED
-> RUN
-> FAILURES PRESERVED
-> TIMINGS RECORDED
-> TRANSFER / CONSOLIDATION IF APPLICABLE
-> RESULT RETURNED TO PARTNER
-> PUBLICATION ONLY WITH PARTNER APPROVAL
```

Public challenge modes may be:

```text
PUBLIC
ANONYMIZED PARTNER
PRIVATE VALIDATION
```

This allows a robotics, drone, warehouse or research partner to test SSI without requiring disclosure of its own proprietary information.

## Rapid-build provenance of the showcase layer

The public presentation layer was assembled as a rapid engineering sprint during one weekend, approximately within a 24-hour development window.

This context is recorded for provenance because the showcase itself is also an engineering artifact. Visual, audio or browser-TTS imperfections should therefore be interpreted as **rapid-prototype presentation-layer limitations**, not as experiment results.

In particular:

- Hermes voice quality depends partly on browser / operating-system speech synthesis;
- audio polish is not treated as a research result;
- presentation defects do not change stored domain-run evidence;
- the purpose of the showcase is to expose SSI behavior and evidence, not to establish a finished commercial voice/entertainment product.

The author reports that this sprint was carried out continuously over the weekend with minimal/no sleep. This is author-supplied development context, not a scientific claim and not part of the benchmark methodology.

## Technology used for the public presentation layer

The public showcase uses a modern web presentation stack around the existing EchoTrip/Cloudflare deployment path, including:

- Next.js / React / TypeScript;
- responsive CSS and dynamic viewport-scaled typography;
- JavaScript-driven real-time visual state and animations;
- browser speech synthesis for optional Hermes narration;
- local/browser audio controls;
- Cloudflare Workers / OpenNext deployment;
- sanitized JSON evidence payloads generated from the domain measurements.

This presentation stack is separate from the proprietary SSI core.

## Claim boundary

Supported now:

- public SSI showcase is deployed;
- software-level drone-domain transfer exists;
- software-level humanoid-domain transfer exists;
- actual executed software benchmarks produced measured wall-clock / flow-cost values;
- actual executed simulator scenarios produced measured simulation-clock values;
- drone flow-depth differences are measured;
- cross-consolidation effects are measured in the scoped drone demonstrator;
- a post-consolidation regression was detected and preserved;
- humanoid before/after slip behavior is measured in the software demonstrator;
- external challenge entry is defined.

Not claimed:

- physical drone timing equivalence;
- physical humanoid timing equivalence;
- certified flight or robotics safety;
- universal consolidation benefit;
- universal superiority over competing robotics systems;
- completed independent external replication;
- completed full S1-S10 training across every BODY line;
- completed 21-experiment scientific programme;
- AGI or consciousness.

## Recommended interpretation

The correct statement is:

> **SSI V5 now has a public, evidence-oriented showcase of measured software-domain transfer into drone/swarm and humanoid motion/stability laboratories. The published timings are actual results from executed software runs or their simulation clocks, not invented presentation values. Physical-world validation and independent external replication remain future steps.**
