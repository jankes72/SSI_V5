# SSI V5 — Football World / Świat Hipnozy 01 — Current Status — 2026-09-16

**Status:** `IMPLEMENTED WORLD TEMPLATE / DIRECTOR-INTEGRATED / LOCAL SOFTWARE VALIDATION / PARTIAL SOURCE CONNECTION`  
**Repository role:** public evidence/status description only; proprietary implementation remains private.  
**Authorship:** Football World / Świat Piłki, historical T17, Organizer_swiat_Pilki, accumulated football data/history and the current Football World / Świat Hipnozy 01 are Paweł Jankiewicz's own project line.  
**Mechanism-level influence:** selected mechanics later added to the current world were adapted from four private source archives by Michał Jankiewicz: `Moralna SI.zip`, `recursio.zip`, `diana_core.zip`, `pierwotne JA.7z`. This does not transfer authorship of Football World or SSI V5.

## Current status

Football World is no longer only a historical origin concept or future integration target.

A first professional world template now exists as part of a Director-integrated package:

```text
SSI_DIRECTOR_FOOTBALL_WORLD_V1_20260916
```

The package contains one active world:

```text
FOOTBALL_WORLD / SWIAT HIPNOZY 01
```

and one extension contract:

```text
worlds/_template/
```

No drone, humanoid, market or other future world is claimed active inside this package.

## Authorship boundary

The authorship boundary for this world is explicit:

```text
FOOTBALL WORLD / ŚWIAT PIŁKI
T17 / 17 football Teachers
Organizer_swiat_Pilki
multi-year football data/history
current Football World / Świat Hipnozy 01
= Paweł Jankiewicz
```

Only the following four private source archives are attributed to Michał Jankiewicz:

```text
Moralna SI.zip
recursio.zip
diana_core.zip
pierwotne JA.7z
```

Some selected mechanisms from those four archives were later studied, modified or reimplemented inside the current world, but Football World itself is not derived ownership-wise from Michał Jankiewicz.

See [`MICHAL_JANKIEWICZ_SOURCE_PROJECTS_AND_SSI_ADAPTATION_20260916.md`](MICHAL_JANKIEWICZ_SOURCE_PROJECTS_AND_SSI_ADAPTATION_20260916.md).

## What now exists

The implemented Football World V1 template includes:

- a `worlds/registry.json` registry with exactly one active world: `FOOTBALL_WORLD`;
- a dedicated Football World runtime/state layer;
- a read-only Football World panel;
- a Director read-only `Worlds` integration view;
- 17 Hermes slots derived from the historical T17 `12 + 5` Teacher structure;
- versioned Hermes source generations;
- fail-closed `NOT_CONNECTED` state when a real source is unavailable;
- private Agent Pocket state for selected Hermes-generation snapshots and later artifacts;
- persistent room/visit/movement history;
- state-grounded narrative cues;
- an Agora/social-interaction state layer;
- SOLO and SHARED LAB1 paths;
- LAB2 grouping stage;
- LAB3 allocation/portfolio-plan stage;
- Freeze Gate;
- Outcome Hall;
- Reflection stage;
- persistent event/provenance logging;
- separation of prediction source from outcome source;
- an open `_template` contract for future worlds without pretending those worlds already exist.

## 17 Hermes structure

The current registry maps the preserved T17 perspectives into 17 Hermes positions:

```text
H01 FULL TREND
H02 ODDS CHANGE
H03 AMPLITUDE
H04 TEMPO
H05 MAX DEVIATION
H06 START RAW
H07 END RAW
H08 LOG START
H09 LOG END
H10 RATIO START
H11 RATIO END
H12 STATISTICS

H13 PREPARED ODDS
H14 START ODDS
H15 END ODDS
H16 ODDS DELTA
H17 PERCENT CHANGE
```

This is not a claim that all 17 historical predictive models are currently live and scientifically validated in the new canonical runtime.

The claim is narrower:

```text
17-HERMES WORLD STRUCTURE = IMPLEMENTED
SOURCE ADAPTER / SOURCE DISCOVERY = IMPLEMENTED
MISSING SOURCE = NOT_CONNECTED
FULL LIVE T17 SCIENTIFIC VALIDATION = NOT CLAIMED
```

## Existing Football organizer as source

The world is designed to read the existing sibling source tree:

```text
../Organizer_swiat_Pilki
```

through a read-only adapter.

The adapter recognizes existing Football World material such as:

```text
archiwa/
dane/
danePomocnicze/
laboratorium/
modele_dataBase_futbol_trend/
modele_kursy_przygotowane/
WORLD/
pamiec_swiatow.json
laboratorium_uczenia.json
```

and related result/model builder, collector, updater and validator tools.

The new world layer does not silently overwrite or duplicate those source assets.

## Narrative world mechanics

The current world template treats narrative as part of experimental state rather than decoration.

```text
WORLD STATE / PERSISTENT HISTORY
        |
        v
STATE-GROUNDED NARRATIVE CUE
        |
        v
AGENT INTERPRETATION / TACTIC
```

A narrative cue may reference real state such as:

- current room;
- previous visit;
- Hermes generation changes;
- items in the Agent Pocket;
- prior failure/success references;
- relationship history;
- missing gate artifact.

The narrator is not allowed to invent outcome, confidence, evidence or success that is absent from world state.

## Rooms and gates

The first template uses a staged world path:

```text
ENTRANCE
-> ORIENTATION
-> HERMES RING / 17 HERMES ROOMS
-> AGORA
-> LAB1 SOLO / SHARED
-> LAB2 GROUPS
-> LAB3 ALLOCATION
-> FREEZE GATE
-> OUTCOME HALL
-> REFLECTION
-> NEXT CYCLE
```

Progression is artifact-gated rather than a cosmetic `NEXT` button.

Current intended gate semantics include:

```text
LAB1
requires a real Hermes snapshot or an explicit Agent hypothesis

LAB2
requires a LAB1 strategy / prediction-set artifact

LAB3
requires a GROUP_SET

FREEZE
requires a PORTFOLIO_PLAN

OUTCOME HALL
requires a FROZEN_DECISION
```

## Pocket and path dependence

Each Agent has a private Pocket.

A snapshot such as:

```text
H04 / G20260916R01
```

remains attributable to the generation actually selected by that Agent even if the Hermes later advances to a newer generation.

This is intended to preserve:

```text
VERSIONED KNOWLEDGE OWNERSHIP
PATH DEPENDENCE
COGNITIVE BIOGRAPHY
REPRODUCIBLE EXPERIMENT LINEAGE
```

## SOLO / SHARED boundary

The world preserves the distinction:

```text
COMMUNICATION != MEMORY MERGE
OBSERVATION != COMPETENCE TRANSFER
```

SOLO LAB does not publish an Agent's private history.

SHARED LAB contains only artifacts explicitly contributed to the shared experiment, with provenance.

## Outcome boundary

Football World preserves the independent-outcome rule:

```text
PREDICTION SOURCE != OUTCOME SOURCE
```

The existing `archiwa/` source can be treated as an independent result source, but the current V1 package does not silently guess match identity across arbitrary prediction and result records.

Until an explicit match-identity resolver/validator integration is connected, the correct state is:

```text
PENDING_MATCH_IDENTITY_RESOLUTION
```

This is intentional fail-closed behavior.

## Director integration

The Director remains the existing strategic runtime line. The package does not create a second Director, Router V10, Router S10 or CONTINUUM.

The Director receives a read-only Worlds view and can observe Football World state.

The world runtime and panel remain separate from owner/operator authority. Public/remote observation does not imply arbitrary execution authority.

```text
OBSERVE != CONTROL
CAPABILITY != AUTHORITY
SIMULATION != REAL EXECUTION
```

## What is not yet claimed

The current Football World status does **not** claim:

- complete live integration of all BODY_FROZEN / ISKRA Agents into the world;
- complete long-duration Agent biographies already accumulated in the new runtime;
- complete automatic match-identity resolution;
- complete automatic verified-outcome ingestion;
- full live scientific validation of all 17 historical T17 Teachers in the new runtime;
- completed profitability evidence;
- real-money betting authority;
- completion of the separate 21 BODY / ISKRA programme;
- AGI or consciousness.

## Current research role

Football World is now best described as:

```text
PAWEŁ JANKIEWICZ MULTI-YEAR FOOTBALL WORLD / T17 LINE
+
IMPLEMENTED PROFESSIONAL WORLD TEMPLATE
+
DIRECTOR-INTEGRATED WORLD SLOT
+
17-HERMES KNOWLEDGE STRUCTURE
+
PERSISTENT NARRATIVE / POCKET / LAB / FREEZE ARCHITECTURE
+
PARTIAL CONNECTION TO EXISTING FOOTBALL SOURCE TREE
```

The next steps are controlled live Agent entry, explicit match/result identity integration, longer-cycle persistent Experience, and evidence-backed evaluation of how different Agent histories, Hermes generations, collaboration choices and narrative context affect later strategies.

## Related evidence and architecture

- [`evidence/FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md`](evidence/FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md)
- [`MICHAL_JANKIEWICZ_SOURCE_PROJECTS_AND_SSI_ADAPTATION_20260916.md`](MICHAL_JANKIEWICZ_SOURCE_PROJECTS_AND_SSI_ADAPTATION_20260916.md)
- [`evidence/ISKRA_MORAL_AI_ORIGIN_AND_ATTRIBUTION.md`](evidence/ISKRA_MORAL_AI_ORIGIN_AND_ATTRIBUTION.md)
- [`SSI_V5_ORIGIN_RESEARCH_METHODOLOGY_AND_LONG_TERM_ARCHITECTURE.md`](SSI_V5_ORIGIN_RESEARCH_METHODOLOGY_AND_LONG_TERM_ARCHITECTURE.md)
- [`DIRECTOR_COMMAND_CENTER_TAILSCALE_CROSS_CONSOLIDATION_ARCHITECTURE_20260914.md`](DIRECTOR_COMMAND_CENTER_TAILSCALE_CROSS_CONSOLIDATION_ARCHITECTURE_20260914.md)
