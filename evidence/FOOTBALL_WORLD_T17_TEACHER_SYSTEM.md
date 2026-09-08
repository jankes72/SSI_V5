# Football World — Historical T17 Teacher Knowledge System

**Evidence status:** `HISTORICAL_EVIDENCE / ROOT_ATTESTED`  
**Scope:** earlier SSI architecture / Football World  
**Meaning:** historical mechanism to preserve during migration to the current SSI V5 architecture  
**Architecture author:** Paweł Jankiewicz (`PROGRAMMER_ROOT`)

> This document preserves an earlier Football World mechanism that predates the current formalization of `SSI ORGANISM CORE`. It does not claim that the entire T17 system is currently active in canonical runtime. It records preserved structure, artifacts and a learning contract that should not be lost during migration.

---

## 1. T17 — 17 specialized Teachers

T17 consisted of **17 Teachers in two model families: 12 + 5**.

### Family A — `dataBase_futbol_trend` (12)

1. `dataBase_futbol_trend` — aggregate Teacher / full trend view;
2. `siec_01_zmiana_kursow` — odds change;
3. `siec_02_amplituda` — movement amplitude;
4. `siec_03_tempo` — rate of change;
5. `siec_04_max_wahanie` — maximum deviations;
6. `siec_05_start_raw` — raw starting values;
7. `siec_06_koniec_raw` — raw ending values;
8. `siec_07_log_start` — logarithmic start-value representation;
9. `siec_08_log_koniec` — logarithmic end-value representation;
10. `siec_09_ratio_start` — starting ratios;
11. `siec_10_ratio_koniec` — ending ratios;
12. `siec_11_statystyka` — statistical and aggregate features.

### Family B — `kursy_przygotowane` (5)

13. `kursy_przygotowane` — aggregate Teacher based on prepared odds;
14. `siec_01_start_kursow` — starting odds;
15. `siec_02_koniec_kursow` — ending odds;
16. `siec_03_zmiana_kursow` — start-to-end difference;
17. `siec_04_procent_kursow` — relative / percentage odds change.

A key property of T17 was that one problem was not observed through a single model. Each Teacher represented a different view of the same match and the same market/sport process.

---

## 2. 60% / 40% contract

The historical flow separated training from later observation:

```text
SOURCE DATA
      |
      v
BUILD / TRAIN
      |
      +-------------------------+
      |                         |
      v                         v
60% TRAINING              40% OBSERVATION
      |                         |
      v                         v
MODEL TEACHER             UNSEEN DATA
                                |
                                v
                           PREDICTION
                                |
                                v
                         REAL OUTCOME
                                |
                                v
                      OBSERVATION MEMORY
```

The 40% observation portion was not treated as a simple extension of training. It was used to observe the behavior of an already-built Teacher on unseen cases.

---

## 3. Teacher artifacts

A typical Teacher had a structure similar to:

```text
siec_03_tempo/
|
|-- model.h5
|-- metadata.json
|-- klasy.json
|-- historia.json
|
|-- walidacja_40_procent.csv
|
|-- predykcje/
|   |-- predykcja_grupy.csv
|   `-- predykcja_z_wynikiem.csv
|
`-- obserwacja/
    |-- ocena.json
    `-- pamiec_obserwacji.json
```

Artifact meaning:

- `model.h5` — Teacher predictive model;
- `metadata.json` — configuration and model/input description;
- `klasy.json` — output-class mapping;
- `historia.json` — training history;
- `walidacja_40_procent.csv` — separated observation data;
- `predykcja_z_wynikiem.csv` — historical linkage between prediction and outcome;
- `pamiec_obserwacji.json` — memory of Teacher behavior over subsequent observations.

---

## 4. Teacher behavior memory

`pamiec_obserwacji.json` was not only an accuracy report. It retained observations for studying:

- whether the Teacher changed its prediction;
- whether confidence changed;
- whether confidence increases were justified;
- whether high confidence correlated with correctness;
- which classes of cases produced recurring errors;
- how behavior changed across observations.

Fundamental distinction:

```text
PREDICTION SCORE
!=
KNOWLEDGE ABOUT MODEL BEHAVIOR
```

---

## 5. Knowledge Laboratory

Each Teacher had a separate analysis area, for example:

```text
laboratorium/
`-- dataBase_futbol_trend/
    `-- siec_03_tempo/
        |-- analiza_klas.json
        |-- analiza_odchylen.json
        |-- analiza_pamieci.json
        |-- analiza_pewnosci.json
        |-- analiza_pewnosci_klasy.json
        |-- analiza_przyszlych_predykcji.csv
        `-- kolektor_wiedzy.json
```

These layers answered different questions:

- `analiza_klas.json` — where the Teacher is strong or weak by class;
- `analiza_pewnosci.json` — confidence versus actual correctness;
- `analiza_pewnosci_klasy.json` — confidence calibration per class;
- `analiza_odchylen.json` — error type and magnitude;
- `analiza_pamieci.json` — model behavior across observations;
- `analiza_przyszlych_predykcji.csv` — material for continued monitoring;
- `kolektor_wiedzy.json` — consolidated knowledge about one Teacher's behavior.

---

## 6. Two forms of a Teacher

T17 separated:

```text
MODEL TEACHER
= model.h5
= predictive capability

TEACHER KNOWLEDGE
= kolektor_wiedzy.json
= knowledge learned by observing model behavior
```

The later system therefore did not need to copy Teacher weights or treat every Teacher prediction as equally valuable. It could use information such as:

```text
Teacher is strong in situation A
Teacher is weak in situation B
high confidence in class C is reliable
in case D the Teacher systematically overestimates
```

This is the mechanism:

```text
TEACHER -> OBSERVATION -> MEMORY -> ANALYSIS -> KNOWLEDGE
```

not merely:

```text
TEACHER -> LABEL / ACCURACY
```

---

## 7. T17 knowledge consolidation

The aggregate layer included artifacts such as:

```text
PAMIEC_MODEL_POZNAWCZY.json
WIEDZA_DLA_MODELU_DOCELOWEGO.json
```

`WIEDZA_DLA_MODELU_DOCELOWEGO.json` could contain:

- Teacher recommendation;
- confidence;
- weights for `home / draw / away` classes;
- level and number of examples taken from the world;
- `condition -> consequence -> confidence` rules.

Example rule type:

```text
IF a feature is within a given range
THEN a particular outcome direction occurs more often
CONFIDENCE = value derived from evidence
```

T17 was therefore intended to move from many specialized perspectives to explicit, analyzable knowledge rather than only one aggregate model score.

---

## 8. Full historical flow

```text
17 TEACHERS
      |
      +-- 12 x dataBase_futbol_trend
      |
      `-- 5 x kursy_przygotowane
              |
              v
       MODELS + METADATA
              |
              v
       40% UNSEEN OBSERVATION
              |
              v
          PREDICTIONS
              |
              v
        REAL OUTCOME
              |
              v
      OBSERVATION MEMORY
              |
              v
      KNOWLEDGE LABORATORY
              |
              +-- classes
              +-- deviations
              +-- memory
              +-- confidence
              +-- confidence / class
              `-- future predictions
              |
              v
      TEACHER KNOWLEDGE COLLECTOR
              |
              v
       T17 CONSOLIDATION
              |
              v
     PAMIEC_MODEL_POZNAWCZY
              |
              v
 WIEDZA_DLA_MODELU_DOCELOWEGO
```

---

## 9. Relationship to future Agents

In current SSI architecture this historical mechanism may serve as a source of knowledge and experimental material for future Agents.

An Agent does not need to copy a Teacher blindly. The intended pattern is:

```text
WORLD / TEACHER KNOWLEDGE
+
OWN OBSERVATIONS
+
OWN METADATA
+
OWN FEATURES
+
OWN HYPOTHESIS
        |
        v
OWN DATASET
        |
        v
OWN EXPERIMENT
        |
        v
OWN MODEL / STRATEGY
        |
        v
SIMULATED DECISION
        |
        v
INDEPENDENT REAL OUTCOME
        |
        v
OWN EXPERIENCE
```

Six persistent Agents could therefore develop different research methodologies while entering the same world.

Director is intended to observe not only final ranking but the full experiment lineage, strategy development, micronetworks, private Agent histories, and the effect of prior Experience and value systems on decisions.

---

## 10. Authority and real-world execution

Agent experiments remain separate from real execution:

```text
AGENTS
explore / simulate / learn
        |
        v
DIRECTOR
observes / evaluates / decides
        |
        v
ROBERT
executes approved real-world actions
```

An Agent may create predictions, simulated strategies and experimental decision combinations. Ranking or high accuracy alone does not grant real-world authority.

The same distinction applies to Moral AI / Iskra: an Agent may make decisions inside an experimental environment and learn from consequences, but capability is not authority.

```text
CAPABILITY != AUTHORITY
SIMULATION != REAL EXECUTION
```

---

## 11. Significance for SSI V5 migration

The current MASTER rebuild should preserve more than the `60% training / 40% observation` rule.

The broader mechanism is:

```text
OBSERVATION
-> MEMORY
-> BEHAVIOR ANALYSIS
-> KNOWLEDGE COLLECTOR
-> CONSOLIDATED KNOWLEDGE
```

This is a historical Football World domain mechanism that may later be mapped onto neutral `SSI ORGANISM CORE` interfaces without copying one Agent's private history into other Agents.

---

## 12. Claim boundaries

This document does not claim that:

- T17 is currently fully connected to the canonical SSI V5 runtime;
- all 17 Teachers are currently active in production;
- historical predictions guarantee future performance;
- the mechanism proves AGI or consciousness;
- an Agent receives authority for real financial actions.

The document preserves a **historical design, retained artifacts and research mechanism** relevant to later Football World integration.