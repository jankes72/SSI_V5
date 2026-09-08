# SSI V5 — Experimental Origins and Engineering Evolution

**Status:** `HISTORICAL_EVIDENCE / ROOT_ATTESTED / EVIDENCE_TO_EXPAND`  
**Date:** `2026-08-29`  
**SSI author:** Paweł Jankiewicz / `PROGRAMMER_ROOT`

## 1. Why this document exists

The public SSI history should not imply that the current architecture was invented from zero in a few weeks or created solely through modern LLM tools. The rapid formalization of SSI builds on earlier years of the author's experiments with football data, prediction, observation of model behavior, custom calculation methods and practical strategy testing.

GitHub confirms formalization of the MSDI/SSI architecture from July 2026. Earlier domain-experiment history is currently `ROOT_ATTESTED` and can be strengthened with machine evidence when preserved code, data and results are reattached and inspected.

## 2. Starting point: not "build AI", but understand prediction behavior

The original question was practical:

```text
DATA
-> MODEL
-> PREDICTION
-> REAL OUTCOME
-> WHAT IS THE MODEL ACTUALLY DOING?
```

Final accuracy alone was not enough. The author observed that a model may still carry useful information when its error is systematic — for example, a certain exact-score prediction may historically correlate with a repeatable opposite direction.

This led to analysis not only of `correct / incorrect`, but also:

- groups of similar predictions;
- exact-score hit rate;
- directional hit rate;
- systematic deviations;
- changes between generations;
- stability of the same prediction after retraining;
- cases where a new generation changes an earlier answer;
- history of the same match/case across observations;
- conditions where an apparently wrong model still carries useful signal.

## 3. 60% training / 40% unseen observation

One historical mechanism separated training data from later observation data. The purpose was not only to measure accuracy, but to observe the behavior of a trained network on data it did not use during training.

```text
60% TRAINING
-> MODEL / TEACHER GENERATION

40% UNSEEN OBSERVATION
-> PREDICTIONS
-> REAL OUTCOMES
-> MEMORY OF OBSERVATION
-> KNOWLEDGE
```

The observation layer preserved prediction history and changes between generations. If the same case reappeared later, the system could compare prior and current predictions and retain the change.

## 4. Generation as a historical competence state

A Teacher generation is not treated only as a training counter. It is a historical snapshot of model behavior that may differ in value from a later generation.

```text
TEACHER G_n
-> PREDICTION PROFILE
-> OBSERVATION HISTORY
-> GROUP STATISTICS
-> EXACT-SCORE BEHAVIOR
-> DEVIATIONS
-> REAL OUTCOMES
```

A later `G_n+1` may behave differently. An older generation may therefore remain useful as a separate research artifact and as input to a later Agent strategy.

## 5. Knowledge Collector

A Teacher should not be reduced to a single output. Its knowledge includes observations about how a prediction class behaves, outcome distribution, dominant result/direction, deviations between generations and the stability of a characteristic.

Historically this approach produced observation artifacts, Knowledge Laboratories and knowledge collectors described more fully in `FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md`.

## 6. Virtual strategy accounting

The author also ran earlier experiments where different models/strategies had their own names and produced virtual exact-score predictions. Results were settled against odds and cost/stake so the system could observe not only accuracy but also long-term economic value of a strategy.

This led to an important distinction:

```text
HIGH ACCURACY != POSITIVE ECONOMIC VALUE
LOW EXACT-SCORE HIT RATE != AUTOMATICALLY USELESS SIGNAL
```

This is not a claim of guaranteed financial advantage. It is part of the methodology history from which SSI later developed its emphasis on real outcome, Experience and long-term strategy evaluation.

## 7. Evolution of the author's programming method

The author did not begin with large multi-module systems. Earlier tools were often single Python scripts executed linearly; larger programs were split into logical parts (`part 1`, `part 2`, `part 3`, `part 4`) so successive data and calculation stages could be extracted and checked.

That decomposition practice predates current LEGO packages. The present pattern:

```text
LARGE PROBLEM
-> SMALL PARTS
-> EXPLICIT INPUTS / OUTPUTS
-> EXECUTION
-> TEST
-> CHECKPOINT
-> INTEGRATION
```

is an evolution of a practical work method, not merely an LLM prompting technique.

## 8. Custom calculation code and network features

The author has earlier network-calculation code and data concerning the effectiveness of custom feature-engineering / weighting / transformation mechanisms. The detailed architecture is not reconstructed from memory here because the source remains on the author's MSI machine and was not re-verified during this public update.

Current status:

```text
EXISTS ACCORDING TO AUTHOR = ROOT_ATTESTED
DETAILED IMPLEMENTATION = NOT YET RE-VERIFIED IN THIS PUBLIC UPDATE
NEXT STEP = INSPECT SOURCE CODE + ADD MACHINE-CHECKABLE EVIDENCE
```

Public documentation should not pretend to know exact layer counts, transformations or formulas that have not been re-confirmed from source.

## 9. Relationship to SSI micronetworks

Micronetworks did not appear in isolation. Their logic — observe behavior, preserve history, detect stable patterns, compare generations, collect evidence and only then strengthen competence — has methodological continuity with earlier model-observation practice.

```text
PREDICTION HISTORY
-> OBSERVATION MEMORY
-> PATTERN
-> KNOWLEDGE

later:

EXPERIENCE
-> MICRONETWORK BRANCH
-> CANDIDATE
-> CHALLENGER
-> CHAMPION
```

These are not identical mechanisms, but there is a clear methodological lineage.

## 10. Why the rapid 2026 timeline does not mean "one month of experience"

Public Git records very fast formal development of MSDI/SSI architecture in 2026. It does not record the beginning of the author's interest in data analysis, prediction or earlier domain experiments.

The honest public statement is:

> The current SSI architecture was formalized very quickly, but it builds on earlier experiments with data, prediction, model observation and custom programs. Public evidence of those earlier stages is incomplete and should be strengthened with source artifacts rather than reconstructed retrospectively from memory.

## 11. Evidence rule

```text
AUTHOR MEMORY / ROOT ATTESTATION
!= MACHINE EVIDENCE

OLD SOURCE CODE
+ DATA
+ TIMESTAMPS
+ OUTPUTS
+ REPRODUCTION
-> STRONGER HISTORICAL EVIDENCE
```

This document preserves the methodology's origin without turning personal history into unverified marketing.