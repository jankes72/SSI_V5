# SSI V5 — Michał Jankiewicz Source Projects and Later SSI Adaptation

**Recorded:** `2026-09-16`  
**Status:** `AUTHOR ATTRIBUTION / SOURCE-LINEAGE RECORD`  
**Public role:** preserve authorship and explain how earlier family projects contributed mechanisms later adapted into SSI V5.  
**Source-code boundary:** the public repository documents lineage and mechanisms; it does not publish the private source archives.

## 1. Attribution rule

According to the direct attribution of Paweł Jankiewicz (`jankes72`, `PROGRAMMER_ROOT`), the following earlier projects were authored by his brother, **Michał Jankiewicz**:

```text
1. Moralna SI
2. Recursio
3. Diana
4. Pierwotne JA
```

Paweł Jankiewicz later used selected ideas and mechanisms from these projects as source material and expanded/adapted them inside his own SSI V5 architecture.

The correct lineage is therefore:

```text
ORIGINAL SOURCE PROJECTS
Michał Jankiewicz
        |
        v
SELECTED IDEAS / MECHANISMS
        |
        v
SSI-SPECIFIC ADAPTATION / EXPANSION / INTEGRATION
Paweł Jankiewicz
        |
        v
SSI V5 / ISKRA / FOOTBALL WORLD / DIRECTOR / WORLDS
```

This document does **not** state that SSI V5 is authored by Michał Jankiewicz. It states that important earlier mechanisms used as inspiration/source material originated in Michał Jankiewicz's projects and that this origin must remain explicit.

Likewise, later SSI-specific architecture must not be retroactively attributed to the source projects when it was designed during SSI development.

Fundamental rule:

```text
SOURCE PROJECT
!=
LATER SSI ADAPTATION
!=
LATER SSI EXPERIMENTAL RESULT
```

---

## 2. Moralna SI — world actions, rooms, Teachers, relations and moral/emotional state

`Moralna SI` is an earlier agent/world project by Michał Jankiewicz.

The reviewed private source material shows a world-oriented agent structure rather than only a text prompt or score calculator. Its mechanics include, at a high level:

- Agents existing in rooms / mapped environments;
- inventory and item possession;
- knowledge and learned skills;
- actions such as movement, taking/picking up an item, using it and talking;
- Teachers/residents able to provide knowledge, skills, items or values;
- room-dependent actions and progression;
- relationships between Agents, including trust/loyalty-style state;
- moral/value parameters;
- emotional-state mechanisms;
- experience updated by action and consequence.

A representative abstract mechanism is:

```text
WORLD / ROOM
+
AGENT STATE
+
ITEM / KNOWLEDGE / SKILL
+
OTHER AGENT OR TEACHER
        |
        v
ACTION
        |
        v
CONSEQUENCE
        |
        +-> EXPERIENCE
        +-> RELATIONSHIP CHANGE
        +-> MORAL / EMOTIONAL INTERPRETATION
```

### What SSI later adapted from this line

SSI did not copy Moralna SI 1:1. Selected mechanisms were generalized into, among other things:

```text
ROOM / WORLD STRUCTURE
-> persistent SSI World rooms

INVENTORY
-> Agent Pocket / artifact ownership

ITEM + KNOWLEDGE + SKILL REQUIREMENTS
-> artifact / competence / evidence gates

TEACHERS / RESIDENTS
-> later resident-knowledge concepts, including Hermes roles

RELATIONSHIPS
-> Agent <-> Agent trust/history/social state

ACTION -> CONSEQUENCE -> EXPERIENCE
-> SSI Experience and persistent learning lineage

MORAL / EMOTIONAL INTERPRETATION
-> Iskra/value-oriented interpretation layer
```

For Football World this lineage is visible especially in the Pocket, room/gate logic, Hermes-as-resident interaction model and Agent-to-Agent social space.

---

## 3. Recursio — persistent world context, exploration and narration

`Recursio` is an earlier project by Michał Jankiewicz centered on a persistent self/world context and continuing interaction rather than a stateless single exchange.

The reviewed private source material contains persistent categories corresponding to concepts such as:

```text
SELF / JA
EXPERIENCE
ENVIRONMENT
EVENTS
SELF-ASSESSMENT
DISCOVERIES
CONTACT / PEOPLE
HISTORY
```

At a high level, Recursio maintains a current context of where the entity is, what has happened, what has previously been experienced, what has been discovered and which parts of prior state should matter now.

Its useful conceptual flow is:

```text
CURRENT WORLD STATE
+
PRIOR EXPERIENCE
+
RECENT EVENTS
+
POSITION / ENVIRONMENT
+
CONTACT HISTORY
        |
        v
CURRENT CONTEXT
        |
        v
NARRATED / CONTEXTUALIZED NEXT INTERACTION
```

### What SSI later adapted from this line

For SSI V5 and especially Football World, Paweł Jankiewicz adapted the idea into a **state-grounded narrator and world-navigation layer**.

The later SSI concept is:

```text
CONTINUUM / WORLD STATE
        |
        v
RECURSIO-STYLE NARRATIVE LAYER
        |
        v
WHAT THE AGENT IS REMINDED OF / SEES / CAN DO NEXT
```

This includes:

- remembering previously visited spaces;
- describing what changed since the last visit;
- presenting current available actions;
- recalling relevant prior experience;
- giving continuity to movement through a world;
- connecting conversations and events across time.

The narrator is not allowed to invent evidence or modify world truth.

```text
WORLD TRUTH
-> NARRATIVE PRESENTATION
-> AGENT INTERPRETATION

NOT:
NARRATIVE
-> INVENTED WORLD TRUTH
```

---

## 4. Diana — persistent self-model, autobiographical memory and self-assessment

`Diana` is another earlier project by Michał Jankiewicz.

The reviewed private source archive contains explicit persistent structures for identity/self-state, experience, self-assessment, environment, events, history and memory, together with mechanisms for extending/updating the entity's representation of itself.

At a conceptual level:

```text
WHO I AM
+
WHAT I EXPERIENCED
+
WHERE I AM
+
WHAT HAPPENED
+
HOW I CURRENTLY ASSESS MYSELF
        |
        v
PERSISTENT SELF MODEL
```

The important property is continuity: the entity is not represented only by the latest message. Previous experience and a persistent self-description can remain part of later context.

### What SSI later adapted from this line

SSI uses this as one of the historical sources for the concept of a persistent Agent biography/self-model:

```text
AGENT IDENTITY
+
EXPERIENCE HISTORY
+
IMPORTANT EVENTS
+
RELATIONSHIP HISTORY
+
STRATEGY HISTORY
+
ERRORS / SUCCESSES
+
CURRENT SELF-ASSESSMENT / UNCERTAINTY
        |
        v
PERSISTENT AGENT SELF/HISTORY
```

This mechanism is relevant to the ISKRA research lines because two Agents may start from related architecture but accumulate different autobiographical histories and later interpret the same event differently.

This document does **not** treat a persistent self-model as proof of machine consciousness.

```text
PERSISTENT SELF MODEL
!=
PROOF OF CONSCIOUSNESS
```

It is an implementable and observable research mechanism.

---

## 5. Pierwotne JA — earlier identity/self line

`Pierwotne JA` is identified by Paweł Jankiewicz as another source project by Michał Jankiewicz and belongs to the historical family of projects that informed later work on persistent identity / `JA` concepts.

The source artifact is currently preserved privately as a `7z` archive. During the 2026-09-16 source review used for this public attribution record, its exact implementation was **not fully unpacked and inspected** in the available environment.

Therefore the public claim is intentionally narrow:

```text
AUTHOR ATTRIBUTION
= Michał Jankiewicz

ROLE IN LINEAGE
= earlier identity / self-model source line

DETAILED TECHNICAL MECHANICS
= not claimed here without direct source inspection
```

This prevents later SSI documentation from inventing details that have not been re-verified.

When the archive is inspected in a compatible environment, this section can be extended with an evidence-backed technical description while preserving this version as history.

---

## 6. Agora is an SSI adaptation, not a fifth source program

In the current Football World documentation, `Agora` is the name of the SSI social space where Agents can meet, communicate, offer an artifact, criticize a hypothesis, collaborate or refuse collaboration.

Based on the currently reviewed source set, `Agora` should **not** be presented as a separate fifth source project by Michał Jankiewicz.

It is better described as a later SSI construction combining mechanisms whose historical roots include:

```text
MORALNA SI
-> Agents
-> Teachers/residents
-> relationships
-> trust / loyalty style state
-> interaction and consequence

RECURSIO
-> conversation continuity
-> prior-event context
-> persistent contact/history

SSI V5
-> private Agent histories
-> provenance
-> explicit artifact transfer
-> contamination boundaries
-> SOLO / SHARED experiment control
```

Therefore:

```text
AGORA
= later SSI World construct

NOT
= separate original source program
```

---

## 7. How these projects entered Football World / Świat Hipnozy 01

The current Football World does not simply place the four earlier programs side by side.

Paweł Jankiewicz selected mechanisms and reassembled them inside the SSI V5 architecture:

```text
MORALNA SI
-> rooms / Pocket / gates / Teachers / relationships / action-consequence

RECURSIO
-> movement continuity / world context / state-grounded narration

DIANA
-> persistent self-history / autobiographical continuity / self-assessment concept

PIERWOTNE JA
-> historical identity/self lineage

FOOTBALL T17 / SSI FOOTBALL DATA
-> 17 specialized knowledge perspectives / outcome evidence

SSI V5
-> CONTINUUM
-> Micronetworks
-> V10
-> S10
-> Hermes generations
-> Agent provenance
-> Director audit
-> World contracts
-> Freeze / verified-outcome separation
```

This produced the later Football World structure:

```text
ENTRANCE / ORIENTATION
-> 17 HERMES ROOMS
-> POCKET
-> AGORA
-> LAB1 SOLO / SHARED
-> LAB2 GROUPING
-> LAB3 ALLOCATION
-> FREEZE
-> OUTCOME
-> REFLECTION
-> EXPERIENCE
-> NEXT CYCLE
```

The source-project authorship and the later integration authorship are both important and should remain visible.

---

## 8. Authorship summary

The public attribution should be read as follows:

```text
MICHAŁ JANKIEWICZ
= author of the earlier source projects:
  Moralna SI
  Recursio
  Diana
  Pierwotne JA

PAWEŁ JANKIEWICZ
= author/developer of SSI V5 architecture and the later adaptation,
  expansion and integration of selected mechanisms from those projects
  into SSI / Iskra / Worlds / Football World / Director architecture
```

This distinction should be preserved in public README/status/evidence material and in later presentations, grant materials or publications.

Development lineage does not erase source authorship, and source authorship does not imply authorship of every later SSI-specific extension.

---

## 9. Evidence and publication boundary

The source archives used for this lineage review remain private. This repository does not publish their source code.

Public documentation may describe:

- author attribution;
- high-level mechanisms;
- conceptual lineage;
- which mechanisms were later adapted;
- boundaries between source idea and later implementation.

Public documentation should not expose private source code or imply that the source projects and current SSI runtime are the same implementation.

Related SSI records:

- [`evidence/ISKRA_MORAL_AI_ORIGIN_AND_ATTRIBUTION.md`](evidence/ISKRA_MORAL_AI_ORIGIN_AND_ATTRIBUTION.md)
- [`FOOTBALL_WORLD_CURRENT_STATUS_20260916.md`](FOOTBALL_WORLD_CURRENT_STATUS_20260916.md)
- [`evidence/ISKRA_AGENT_MICRONETWORK_SOCIAL_DYNAMICS.md`](evidence/ISKRA_AGENT_MICRONETWORK_SOCIAL_DYNAMICS.md)
- [`SSI_V5_ORIGIN_RESEARCH_METHODOLOGY_AND_LONG_TERM_ARCHITECTURE.md`](SSI_V5_ORIGIN_RESEARCH_METHODOLOGY_AND_LONG_TERM_ARCHITECTURE.md)
