# CZARA — Mexico Research Context, Translation and Learning Layer

**Date:** `2026-09-26`  
**Status:** `ARCHITECTURE / PLANNED RESEARCH WORKFLOW`  
**Scope:** public, sanitized architectural description. Proprietary implementation, credentials, private prompts and reconstructive internals remain private.

> This document describes the intended role of **CZARA** in the planned SSI robotics collaboration with a research team in Mexico. It is a design and benchmark-plan document, not evidence that the external benchmark has already been executed.

## 1. Why CZARA exists

CZARA is designed as a **context-teaching layer between an external research team and SSI**.

It is deliberately separated from the execution cores:

```text
HUMAN RESEARCH TEAM (MEXICO)
        |
        v
      CZARA
        |
        v
translated / structured research context
        |
        v
     DIRECTOR
        |
        v
   BODY_FROZEN
        |
        v
 LAB / EVIDENCE
```

CZARA is **not** the Director, is **not** BODY_FROZEN and does not directly command robots.

Its job is to preserve what external researchers actually said, translate it into a stable internal working language, extract research context and provide that context to SSI without collapsing human conversation into direct execution authority.

## 2. Mexico-only listening model

The planned collaboration boundary is intentionally asymmetric:

```text
MEXICO SIDE
= microphone / conversation source
= file upload
= research requests
= benchmark view
= shared evidence view

ROOT / OWNER SIDE
= full local control
= DIRECTOR chat
= BODY_FROZEN chat
= training controls
= provider/model controls
= LEGO / micronetwork / laboratory controls
= private runtime and evidence administration
```

CZARA listens to the **Mexico research side only**.

The owner may observe the resulting transcription and Polish translation locally, but the owner side is not treated as a second CZARA microphone source.

This keeps the research interpretation problem clear: CZARA learns the collaborator's language, requirements, dissatisfaction, corrections and proposed changes.

## 3. Language pipeline

The intended language flow is:

```text
Spanish / English speech
        |
        v
temporary audio segment
        |
        v
speech-to-text
        |
        v
language detection
        |
        +--> original_text
        |
        v
Polish translation
        |
        +--> polish_text
        |
        v
structured research context
```

The working rule is:

- preserve the original transcription;
- create a Polish translation for SSI/operator use;
- preserve technical names, identifiers, file names, benchmark IDs and protocol terms unchanged;
- do not loosely translate values, IDs or technical tokens;
- retain provenance showing which text was original and which text was translated.

The intended long-term record is text-oriented. Audio is treated as a temporary transport artifact rather than the primary research memory. A failed transcription may retain a temporary segment until recovery; successful transcription should allow the temporary audio to be removed.

## 4. CZARA is a teacher, not a controller

SSI training must remain able to continue when CZARA is silent.

The intended relationship is:

```text
CZARA -> teaches / supplies context to DIRECTOR
DIRECTOR -> plans / coordinates
BODY_FROZEN -> executes technical work
LAB -> measures
EVIDENCE -> constrains what may be claimed
```

CZARA may communicate that:

- a researcher is dissatisfied with a result;
- a requirement has changed;
- a new constraint was introduced;
- a researcher wants a test repeated;
- the team wants stronger evidence;
- a new benchmark idea was proposed;
- a previous interpretation was incorrect.

The Director decides how that information changes a research mission. BODY_FROZEN then receives an explicit mission or revision through the normal SSI control path.

## 5. Two independent knowledge inputs to DIRECTOR

The planned Mexico collaboration gives DIRECTOR two distinct external information channels.

### A. CZARA_CONTEXT

Passive contextual knowledge derived from conversation:

```text
speaker
language
original text
Polish translation
topic
constraint
decision
open question
confidence / ambiguity
timestamp
session identity
```

### B. DOCTOR_REQUEST / RESEARCH_REQUEST

An explicit structured request submitted through the research portal.

Examples:

```text
REQUEST_EVIDENCE
PROPOSE_CHANGE
MODIFY_BENCHMARK
REQUEST_RERUN
REPORT_NOT_SATISFACTORY
OTHER_RESEARCH_NOTE
```

These sources must not be silently merged. DIRECTOR should retain their provenance so a later reviewer can distinguish:

```text
"the team discussed X"
from
"the team formally requested X"
```

## 6. No direct Director chat for the external side

The Mexico research portal is **not intended to expose a direct chat with DIRECTOR**.

That boundary is deliberate.

An external researcher may:

- propose a modification;
- request evidence;
- request a repeat;
- upload an input file;
- report that a result is not satisfactory;
- propose an additional case;
- inspect the shared benchmark state and sanitized evidence.

Those actions become research inputs. They do not become unrestricted commands to SSI.

## 7. Research-request lifecycle

A proposed workflow is:

```text
MEXICO RESEARCHER
    |
    v
RESEARCH_REQUEST
    |
    +--> CZARA context available to DIRECTOR
    |
    v
DIRECTOR REVIEW
    |
    +--> ACCEPT
    +--> REVISE
    +--> REQUEST CLARIFICATION
    +--> DEFER
    |
    v
versioned benchmark / mission revision
    |
    v
BODY_FROZEN
    |
    v
LAB
    |
    v
PASS / FAIL / INCONCLUSIVE
    |
    v
shared sanitized evidence
```

A request such as "this is not satisfactory" should therefore create a **versioned research change**, not silently overwrite the previous benchmark.

## 8. Interface boundary

The intended public Mexico HTTPS portal should expose only a narrow research surface:

```text
CZARA LIVE
UPLOAD FILE
RESEARCH REQUEST
CURRENT BENCHMARK
BENCHMARK STATUS
SHARED EVIDENCE / RESULT
```

It should not expose:

```text
owner filesystem
/home/... paths
LEGO Pocket internals
private DIRECTOR chat
private BODY_FROZEN chat
LLM credentials
provider configuration
ROOT runtime controls
arbitrary command execution
private evidence storage
```

The owner starts and stops the external HTTPS session from the local ROOT interface. The external research surface is intended to exist only while the owner has explicitly enabled the session.

## 9. Relationship to Champion-first SSI

CZARA is especially useful when SSI is operating in a **Champion-first** mode.

A typical training event may be:

```text
researcher proposes task
-> CZARA captures context
-> DIRECTOR maps task to existing competence
-> BODY_FROZEN uses current Champion
-> LAB measures result
-> researcher says result is not satisfactory
-> CZARA records why
-> explicit change request is created
-> DIRECTOR creates REV_1
-> BODY_FROZEN reuses / adapts / challenges the Champion
-> LAB retests
-> evidence is retained for both REV_0 and REV_1
```

The purpose is not to keep SSI permanently brainstorming. The purpose is to turn repeated research interaction into reusable, evidence-backed competence.

## 10. Research hypothesis

The project-specific hypothesis behind CZARA is:

> A persistent multi-agent system may learn external collaboration more effectively when human conversation is captured by a dedicated context/translation layer that remains separate from planning, execution and validation.

This repository does **not** claim academic priority, patent novelty or independent validation of that hypothesis.

The planned Mexico collaboration is intended to test whether this separation improves:

- requirement continuity;
- interpretation quality;
- change-request handling;
- multilingual research collaboration;
- benchmark reproducibility;
- traceability from human request to machine action;
- reuse of previously validated Champions.

## 11. Evidence policy

CZARA-derived information should remain auditable.

For each material research input, the intended evidence chain is:

```text
source session
-> original transcription
-> Polish translation
-> structured context / request
-> Director interpretation
-> mission / benchmark revision
-> BODY execution
-> LAB result
-> evidence
```

No translation or interpretation should be treated as proof that the associated technical action succeeded.

## 12. Claim boundary

This document describes a planned research architecture and collaboration workflow.

It does **not** establish:

- completed external Mexico validation;
- completed physical drone validation;
- completed physical humanoid validation;
- safety certification;
- independent replication;
- production readiness;
- proven academic novelty of CZARA;
- that automatic translation is error-free.

The external benchmark must remain evidence-driven: **PASS / FAIL / INCONCLUSIVE are preserved, and negative results remain part of the research record.**
