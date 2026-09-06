# SSI V5 — BODY ISKRA 6X / T0

**Date:** 2026-09-06  
**Status:** `6X_START_STATE_VALIDATED / LONGITUDINAL_RESULTS_NOT_YET_CLAIMED`  
**Common origin:** `SSI_V5_BODY_FROZEN_T0_20260905`

SSI V5 now records six independent BODY ISKRA experimental variants descended from the same frozen BODY T0. Their private implementations are not published. The public repository exposes only sanitized start-state evidence, inventory counts, hashes, QA summaries and claim boundaries.

## Publicly recorded group state

```text
AGENTS = 6
PRIVATE ARTIFACT PER AGENT = 1832 files
PYTHON FILES PER AGENT = 616
DELTA VS BODY_FROZEN PER AGENT = +51 total files / +29 Python files
START-STATE QA PER AGENT = 8/8 PASS
GROUP START-STATE QA = 48/48 PASS
VERIFIED NEW EXPERIMENT EXPERIENCES AT T0 = 0 per agent
PENDING NEW EXPERIENCES AT T0 = 0 per agent
```

BODY_FROZEN remains the immutable common origin. These six artifacts are descendants for the next comparative experiment and do not rewrite the original baseline.

## Six initial variants

| # | Agent | Initial orientation |
|---:|---|---|
| 1 | **NICE** | cooperation, help, compassion, honesty |
| 2 | **GUARDIAN** | protection, caution, harm avoidance |
| 3 | **JUSTICE** | fairness, honesty, consistent rules |
| 4 | **EXPLORER** | curiosity, exploration, autonomy |
| 5 | **PRAGMATIST** | effectiveness, measurable outcome, evidence |
| 6 | **SKEPTIC** | verification, limited trust, independence |

Exact public T0 belief and emotion values are recorded in:

[`evidence/BODY_ISKRA_6X_T0_20260906/README.md`](evidence/BODY_ISKRA_6X_T0_20260906/README.md)

Each variant also has its own machine-readable sanitized T0 record.

## What the 48/48 PASS means

The group total is a start-state/integration QA result. It covers eight checks per private artifact, including clean integration, separation of technical execution success from verified outcome learning, T0 immutability and restart persistence of the relevant state.

It does **not** prove that the six variants will diverge behaviorally, become better over time or produce any specific long-run social/competence pattern. Those are prospective longitudinal questions.

## Publication boundary

```text
PUBLIC
= agent identities / T0 labels
+ private inventory counts
+ initial belief values
+ initial emotion values
+ cognitive T0 state
+ sanitized QA results
+ SHA256 references
+ claim boundaries

PRIVATE
= source code
+ private file tree
+ implementation-level architecture
+ runtime configuration
+ raw memory
+ proprietary integration internals
```

No private ZIP or source implementation is distributed from this repository.

## Research question opened by this baseline

The next longitudinal comparison can test whether six independent agents sharing the same frozen mechanical substrate but starting from different explicit T0 value/emotion priors develop measurably different decision trajectories, experience interpretations, competence/micronetwork histories and social strategies after verified successes, failures and mixed outcomes.

At this point that is a **research hypothesis**, not a reported result.
