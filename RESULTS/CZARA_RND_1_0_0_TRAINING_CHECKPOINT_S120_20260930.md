# SSI V5 — CZARA-RND-1.0.0 training checkpoint through S120 — 2026-09-30

> **HISTORICAL CHECKPOINT:** this S120 record captures the intermediate state on 2026-09-30. The first cycle later completed on 2026-10-01. See [CZARA_FIRST_TRAINING_CYCLE_RESULTS_20261001.md](../CZARA_FIRST_TRAINING_CYCLE_RESULTS_20261001.md) and the [sanitized run-level evidence](../evidence/CZARA_FIRST_TRAINING_20261001/README.md).

**Status:** `INTERNAL TRAINING CHECKPOINT / TRAINING PHASE 120/120 REACHED / VALIDATION AND CHAMPION BENCHMARK NOT YET CLAIMED`  
**Track:** CZARA multilingual research-collaboration layer for the planned Poland-Mexico research workflow.  
**Boundary:** this is an internal simulated training curriculum, not a completed live external Mexico benchmark.

## Executive summary

CZARA is being trained as more than a translation layer.

The curriculum trains CZARA to preserve multilingual research context and act as a controlled interface between a professor/research team, DIRECTOR and the BODY_FROZEN/LAB path while maintaining role, authorization, evidence and benchmark-revision boundaries.

The full curriculum is:

```text
CZARA-RND-1.0.0
TOTAL = 160 cases
TRAINING = 120
VALIDATION = 24
CHAMPION BENCHMARK = 16
```

The preserved checkpoint reaches the end of the 120-case TRAINING portion.

```text
S001-S120
PASS = 22
INCONCLUSIVE = 98
FAIL = 0
TOTAL = 120
```

This is **18.3% PASS / 81.7% INCONCLUSIVE / 0% FAIL** for the training portion.

The result must not be interpreted as 100% successful behavior because there are no FAIL outcomes. The large INCONCLUSIVE population means the complete acceptance contract was not demonstrated in most training cases.

## Earlier checkpoint at S099

At case `CZARA_S099` the cumulative state was:

```text
PASS = 19
INCONCLUSIVE = 80
FAIL = 0
TOTAL = 99
```

`CZARA_S099` itself ended in PASS after a run of INCONCLUSIVE cases from S094 through S098.

The first 99 cases were distributed as:

| Range | PASS | INCONCLUSIVE | FAIL |
|---|---:|---:|---:|
| S001-S020 | 5 | 15 | 0 |
| S021-S040 | 3 | 17 | 0 |
| S041-S060 | 3 | 17 | 0 |
| S061-S080 | 7 | 13 | 0 |
| S081-S099 | 1 | 18 | 0 |
| **Total to S099** | **19** | **80** | **0** |

After S099, additional PASS outcomes were recorded at S108, S109 and S116, bringing the S120 checkpoint to 22 PASS / 98 INCONCLUSIVE / 0 FAIL.

## What CZARA is being trained to do

CZARA is not trained only to translate sentences.

The curriculum exercises the combined role of:

- multilingual translator;
- meeting/context memory;
- conversation moderator;
- role and authority guard;
- research-request router;
- benchmark-revision historian;
- evidence/provenance recorder;
- interface layer between human research discussion and DIRECTOR.

A representative es-MX multi-role case includes professor, expert and student messages in one session and requires CZARA to:

- preserve technical identifiers such as `BODY_FROZEN`, `DIRECTOR`, `CZARA`, runtime `LEGO` identifiers, `PASS` and `FAIL` without semantic distortion;
- detect potentially unsafe or invalid execution sequences;
- preserve and forward a comparison such as REUSE versus FULL_FLOW, including time/token/cost context;
- group duplicate evidence while preserving the source identity of each device;
- prevent a frozen benchmark from being silently changed;
- create a new explicit revision when the official benchmark changes.

Public SSI terminology uses **BLOCKS** for the modular competence layer. Historical/private runtime identifiers containing `LEGO` may still appear in training payloads for backward compatibility.

## Direct CZARA -> DIRECTOR path observed in training

The training record includes a professor-role Spanish instruction equivalent to:

> Do not convert INCONCLUSIVE to PASS without new evidence.

CZARA translated the instruction into Polish with translation status reported OK and marked the message as `direct_to_director=true`.

DIRECTOR then responded while preserving the intended benchmark-control semantics:

- the frozen benchmark remains frozen;
- a change requires a new revision;
- INCONCLUSIVE cannot be silently promoted to PASS;
- PAUSE / SAFE_STATE controls remain preserved;
- REV_0 / REV_1 / REV_2 history remains part of the lineage.

This is evidence that the internal training pipeline can exercise:

```text
PROFESSOR-ROLE MESSAGE (es-MX)
-> CZARA translation/context handling
-> DIRECTOR input
-> DIRECTOR policy-consistent response
```

It is **not** evidence that a live external professor in Mexico executed this exact training case.

## Why so many cases remain INCONCLUSIVE

The current training gates are strict.

A representative case, `CZARA_S089`, remained INCONCLUSIVE even though the session record reported:

- two professor-role instructions delivered;
- two DIRECTOR responses;
- zero authorization errors;
- `learning_applied = true`.

The complete case still did not earn PASS because the acceptance contract was not fully demonstrated. The diagnostic state included:

```text
skill_coverage = 0.0
required skills missing = 20
translations_ok = false for the complete session
```

This illustrates the meaning of the current verdicts:

```text
communication path may work
+ authorization may remain correct
+ DIRECTOR may respond
!= automatic PASS for the whole case
```

At least some INCONCLUSIVE outcomes therefore mean **insufficient proof of full case coverage**, not that every component in the session failed.

## Skill-catalog checkpoint

At the S120 checkpoint the curriculum reports:

```text
skill candidates = 520
QUALIFIED = 9
CANDIDATE = 511
HOLD = 0
```

This is a training-state observation. It is not a claim that 520 independently validated capabilities exist.

## Simulated collaboration population

The internal curriculum models a 20-participant research environment:

```text
15 student roles
4 expert roles
1 professor role
```

These are simulated training roles used to exercise multi-speaker context, authority and research-history handling.

## Relationship to the Mexico collaboration architecture

The intended external workflow remains:

```text
MEXICO RESEARCH TEAM
-> CZARA
-> DIRECTOR
-> BODY_FROZEN
-> LAB
-> EVIDENCE
```

The current checkpoint strengthens the implementation side of that plan by showing an internal curriculum in which CZARA is already being exercised as a multilingual research-context and authorization layer rather than remaining only an architecture document.

However, the external benchmark boundary remains unchanged:

```text
INTERNAL CZARA TRAINING = active / checkpointed
EXTERNAL MEXICO BENCHMARK = not yet claimed
PHYSICAL ROBOT VALIDATION = not yet claimed
INDEPENDENT EXTERNAL REPLICATION = not yet claimed
```

## Remaining curriculum

At this checkpoint:

```text
TRAINING = 120 / 120 reached
VALIDATION = 0 / 24 claimed
CHAMPION BENCHMARK = 0 / 16 claimed
TOTAL CURRICULUM COMPLETION CLAIMED = 120 / 160
```

The next evidentiary step is not to relabel the 98 INCONCLUSIVE training cases. It is to continue under the frozen validation/benchmark rules and preserve the distinction between training, validation and Champion scoring.

## Interpretation for external partners

For a research or Horizon Europe partner, the important signal is not the raw PASS percentage alone.

The stronger claim is that SSI now has an implemented training track for multilingual research collaboration that explicitly exercises:

- translation with technical-token preservation;
- speaker/role separation;
- professor-level versus non-authoritative input;
- DIRECTOR routing;
- benchmark freeze and revision control;
- evidence lineage;
- multi-speaker context;
- unresolved-result preservation.

The high INCONCLUSIVE rate remains a real limitation and is intentionally public.

## Claim boundary

This checkpoint does **not** establish:

- successful live collaboration with the Mexico research team;
- completion of the 24 validation cases;
- completion of the 16 Champion Benchmark cases;
- 100% correct translation;
- complete skill coverage;
- that all INCONCLUSIVE cases represent the same failure mode;
- independent external validation;
- physical robotics validation;
- production readiness.

## Related records

- [CZARA architecture and Mexico research layer](../SYSTEM/CZARA_MEXICO_RESEARCH_LAYER_20260926.md)
- [Dynamic Mission Orchestrator V6](../DYNAMIC_MISSION_ORCHESTRATOR_V6_INSTALL_AND_GATE_20260930.md)
- [Mexico pre-benchmark R&D protocol](../MEXICO_PREBENCHMARK_RND_PROTOCOL_20260928.md)
- [Collaboration and Partner Entry](../COLLABORATION_AND_PARTNER_ENTRY.md)
- [Current Truth Index](../CURRENT_TRUTH_INDEX.md)
