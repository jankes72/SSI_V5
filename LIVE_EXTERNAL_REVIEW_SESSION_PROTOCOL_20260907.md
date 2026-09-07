# SSI V5 — Live External Review Session Protocol

**Recorded:** `2026-09-07`  
**Protocol status:** `PREDECLARED / EXTERNAL SESSION NOT YET VALIDATED`  
**Interface stage:** `IMPLEMENTATION + HARDENING / READ-ONLY ACCEPTANCE PENDING`  
**Applies to:** invited external reviewers, research partners, grant evaluators and challenge providers  
**Execution authority:** local ROOT only  
**Reviewer authority:** observation + informational questions only

This document records the intended procedure for externally witnessed SSI V5 experiment sessions **before the first formally validated external live session is claimed**.

Its purpose is to make the future observation procedure auditable and to prevent the rules of a review session from being rewritten after an experiment result is already known.

---

## 1. What this protocol is intended to demonstrate

The live session is designed to let an invited reviewer observe an SSI experiment while it is actually executing rather than relying only on a later report, screenshot or edited demonstration.

Conceptually:

```text
PREDECLARED EXPERIMENT
-> FROZEN / VERSIONED PACKAGE
-> HASH / MANIFEST VERIFICATION
-> KILO PROCEDURAL EXECUTION
-> LIVE READ-ONLY REVIEWER OBSERVATION
-> INFORMATIONAL QUESTIONS
-> PRESERVED FAIL / RETRY / RECOVERY
-> PASS / FAIL / INCONCLUSIVE
-> CLOSED EVIDENCE CHAIN
```

The reviewer is a witness to execution, not an operator of the system.

---

## 2. Current stage on 2026-09-07

At the time this protocol is recorded:

```text
REVIEWER INTERFACE CONCEPT / IMPLEMENTATION = PRESENT
READ-ONLY SECURITY MODEL = DEFINED
MULTI-BODY OBSERVABILITY MODEL = DEFINED
INFORMATIONAL QUESTION CHANNEL = DEFINED
EXTERNAL LIVE-SESSION PROTOCOL = NOW PREDECLARED
FINAL 7/7 BODY + INTERFACE ACCEPTANCE = PENDING
FORMALLY VALIDATED EXTERNAL REVIEW SESSION = NOT YET CLAIMED
```

The project therefore does **not** claim that a grant evaluator, company or independent research partner has already completed a validated live review session.

The next gate is technical closure of the interface and acceptance testing of its read-only boundary and seven-BODY observability behavior.

---

## 3. Preconditions before an external session may be called validated

Before a formally witnessed live experiment session begins, the following should be satisfied where applicable:

```text
7/7 intended BODY lines available for the declared session scope
BODY identity verified
runtime responsiveness verified
CONTINUUM / LAB / Micronetwork / V10 observability available where required
reviewer-safe evidence stream available
read-only boundary tested
local ROOT separation tested
question channel tested
private code / secrets / memory boundary tested
experiment package frozen
manifest / version / hash recorded
acceptance criteria frozen
Kilo execution instruction frozen
known unresolved blockers disclosed
```

A failure of this readiness gate is an infrastructure result and must not be silently presented as a hypothesis failure or success.

---

## 4. Session scheduling and access

An external review session is arranged for a specific date and time.

The reviewer receives privately:

- the live interface address;
- the scheduled start window;
- the public experiment identifier;
- the reviewer-safe description of what is being tested;
- the rules of observation;
- the expected evidence fields;
- where appropriate, the pre-run package hash or public hash reference.

The operational endpoint is not required to be published permanently in the public repository.

---

## 5. Pre-run state visible to the reviewer

Before execution, the interface should make the reviewer-safe pre-run identity clear enough to distinguish the intended experiment from an unspecified run.

Where available, the reviewer should be able to see or verify:

```text
EXPERIMENT_ID
BODY_ID
BODY_VERSION
PACKAGE_VERSION
PACKAGE_HASH
MANIFEST / CONTRACT REFERENCE
CURRENT STATUS = NOT STARTED / READY
EXECUTION MODE
DECLARED ACCEPTANCE STATUS MODEL = PASS / FAIL / INCONCLUSIVE
```

The exact implementation may evolve, but the evidence must preserve which frozen/versioned artifact was executed.

---

## 6. Roles

### Author / local ROOT

The author may prepare infrastructure before the session but must not silently steer the experiment after the declared run begins.

Local ROOT remains the only execution authority.

### Kilo

Kilo acts as the procedural executor of the frozen experiment instructions.

Kilo is **not** described as an independent scientific auditor. Its role is to execute the declared procedure and preserve the resulting evidence.

### Reviewer

The reviewer may:

```text
OBSERVE
ASK INFORMATIONAL QUESTIONS
COMPARE LIVE STATE WITH THE DECLARED CONTRACT
NOTE FAILURES / RECOVERY / ROUTING EVENTS
REVIEW PUBLIC / SANITIZED EVIDENCE
```

The reviewer may not:

```text
CREATE OR MODIFY A MISSION
CHANGE THE PROMPT
CHANGE ACCEPTANCE CRITERIA
RUN KILO
PAUSE / RESUME / RESTART A BODY
ISSUE ROOT COMMANDS
EDIT CONFIGURATION
EXECUTE ARBITRARY CODE
ACCESS PRIVATE SOURCE
ACCESS PRIVATE MEMORY
ACCESS SECRETS / TOKENS
```

---

## 7. Live execution sequence

The intended witnessed run sequence is:

```text
1. REVIEWER CONNECTS
2. SESSION / EXPERIMENT IDENTITY DISPLAYED
3. BODY + PACKAGE VERSION DISPLAYED
4. HASH / MANIFEST VERIFICATION RECORDED
5. PRE-RUN STATUS CONFIRMED
6. KILO STARTS THE DECLARED PROCEDURE
7. AUTHOR DOES NOT SILENTLY STEER THE RUN
8. REVIEWER OBSERVES LIVE STATE
9. REVIEWER MAY ASK INFORMATIONAL QUESTIONS
10. FAILURES / RETRIES / RECOVERY REMAIN VISIBLE IN THE EVIDENCE LINEAGE
11. RUN REACHES PASS / FAIL / INCONCLUSIVE
12. FINAL EVIDENCE IS CLOSED / VERSIONED / HASHED WHERE APPLICABLE
13. REVIEWER CAN COMPARE THE FINAL RESULT WITH THE PRE-RUN CONTRACT
```

---

## 8. What the reviewer may observe live

The interface may expose a sanitized subset of live state including:

- BODY identity and online/offline state;
- runtime status and uptime;
- current mission / experiment stage;
- progress and checkpoints;
- CONTINUUM state;
- LAB progress and aggregate test results;
- reviewer-safe Micronetwork status;
- V10 route class such as known/similar/novel where exposed safely;
- selected Champion / Challenger class where reviewer-safe;
- attempt count;
- failure and recovery events;
- basic resource utilization;
- model/provider class where relevant and safe;
- public evidence references;
- final PASS / FAIL / INCONCLUSIVE state.

Private implementation details remain outside the interface.

---

## 9. Informational question channel

The reviewer may ask questions such as:

```text
What are you doing now?
Which experiment is active?
What stage are you on?
What was the latest checkpoint?
What is the current CONTINUUM state?
Was the current case classified as known, similar or novel?
Why was the current route class selected?
Was a Champion reused or a Challenger tested?
Did the previous attempt fail?
What recovery step is being executed?
What public evidence has been produced so far?
```

Responses must be short, reviewer-facing explanations based on sanitized observable state.

They must not expose hidden chain-of-thought, private prompts, proprietary source code or private memory.

The question channel must remain **non-executive**. A question cannot become a hidden command path.

---

## 10. No silent steering rule

After the declared experimental run begins, a material author intervention must not be hidden.

Examples of material intervention include:

- changing the task or prompt;
- changing the frozen input;
- changing acceptance criteria;
- editing SSI source required for the run;
- changing routing logic specifically to rescue the active run;
- manually selecting the answer/skill/route;
- restarting only to discard an unfavorable outcome.

If a material intervention is necessary, the evidence should record an intervention status such as:

```text
MANUAL_INTERVENTION
```

The original run result remains preserved.

A corrected experiment becomes a new versioned run rather than a silent replacement.

---

## 11. Failure preservation and rerun policy

The live methodology explicitly rejects:

```text
RUN
-> FAIL
-> DELETE FAILURE
-> CHANGE SOMETHING
-> RERUN UNTIL PASS
-> PUBLISH ONLY PASS
```

Instead:

```text
RUN N
-> FAIL / INCONCLUSIVE
-> PRESERVE RESULT + FAILURE SIGNATURE
-> ANALYZE / REPAIR
-> NEW VERSION / HASH IF MATERIAL INPUT OR MECHANISM CHANGED
-> RUN N+1
-> PRESERVE BOTH RESULTS
```

A visible failure followed by successful recovery can be valuable evidence, but the initial failure must remain part of the lineage.

---

## 12. External challenge mode

A stronger future review mode allows the external reviewer or partner to propose new challenge cases that the author and SSI have not previously optimized against.

Intended sequence:

```text
EXTERNAL PARTNER PROPOSES CHALLENGE
-> challenge scope and safety boundary checked
-> acceptance criteria agreed
-> challenge frozen / versioned
-> package hash recorded
-> SSI does not receive post-freeze hidden hints
-> scheduled live session
-> Kilo executes
-> reviewer observes first controlled run
-> PASS / FAIL / INCONCLUSIVE preserved
```

Where practical, the challenge should include cases not used during prior tuning.

This is stronger evidence than an author-selected demonstration, but it should still be described accurately as an **externally proposed and externally witnessed controlled execution**, not automatically as independent scientific validation.

---

## 13. Relationship to the 21-experiment program

The live review layer can be used to observe selected runs from the 21-experiment program once the technical readiness gate is closed.

The intended relationship is:

```text
21 PREDECLARED EXPERIMENTS
+ HASH-SEALED EXECUTION
+ KILO PROCEDURAL OPERATOR
+ READ-ONLY LIVE OBSERVABILITY
+ REVIEWER QUESTIONS
+ FAILURE PRESERVATION
=
STRONGER AUDITABILITY OF THE EXPERIMENT PROCESS
```

The live interface does not change the scientific result. It changes how much of the process an external observer can witness directly.

---

## 14. Relationship to later consolidation and transfer experiments

The same observation protocol is intended to be reusable for later SSI research stages, including:

- post-21 competence inventory;
- Champion / Challenger consolidation;
- versioned BODY_FROZEN upgrade descendants;
- three newly selected post-consolidation domains;
- drone configuration transfer A -> B -> C;
- transfer-mechanism enrichment;
- later humanoid transfer-extension tests.

This makes it possible for a reviewer to observe not only isolated task success, but the evolution of competence and transfer behavior across versioned research stages.

---

## 15. Evidence produced by a review session

A completed session should preserve, where available:

```text
SESSION_ID
DATE / TIME
EXPERIMENT_ID
BODY_ID / VERSION
PACKAGE_VERSION
PACKAGE_HASH
PRE-RUN CONTRACT REFERENCE
REVIEWER ACCESS MODE = READ_ONLY
START RECORD
CHECKPOINT / EVENT REFERENCES
FAIL / RETRY / RECOVERY REFERENCES
MANUAL_INTERVENTION STATUS
FINAL PASS / FAIL / INCONCLUSIVE
FINAL EVIDENCE VERSION / HASH
```

Reviewer identity need not be published without permission. A public record may state that an external session occurred while keeping private participant information confidential where appropriate.

---

## 16. Security boundary

The reviewer interface must remain isolated from execution authority.

Conceptually:

```text
EXTERNAL REVIEWER
        |
        v
READ-ONLY REVIEW INTERFACE
        |
        +-> SANITIZED STATE
        +-> SANITIZED EVIDENCE
        +-> INFORMATIONAL QUERY RESPONSE

NO PATH TO:
LOCAL ROOT / KILO CONTROL / MISSION CONTROL / CONFIG WRITES / SOURCE WRITES
```

The security objective is observability without delegation of operational authority.

---

## 17. Readiness transition

This protocol begins at:

```text
PREDECLARED
+ INTERFACE HARDENING
+ EXTERNAL SESSION VALIDATION PENDING
```

Only after the required acceptance tests pass should the project move the externally witnessed session capability to a stronger status such as:

```text
TECHNICALLY VALIDATED FOR INVITED READ-ONLY REVIEW
```

After an actual external session occurs, its own evidence should be recorded separately. The protocol file should not be rewritten to imply that a future event already happened.

---

## 18. Claim boundaries

At the time of recording this protocol, SSI V5 does **not** claim that:

- an external reviewer has already witnessed a formally validated session;
- the read-only interface has completed its final 7/7 acceptance gate;
- live observation proves the correctness of SSI;
- a reviewer observing a run constitutes independent replication;
- Kilo is an independent auditor;
- a successful live run proves universal transfer, AGI or consciousness;
- external challenge cases will necessarily be passed.

The narrower intended claim, once technically validated and actually used, is:

> SSI V5 can execute a predeclared, versioned/hash-identified experiment while an invited external reviewer observes sanitized live state through a non-executive read-only interface and asks informational questions, with failures, interventions and final evidence preserved in the experimental lineage.

That claim becomes applicable only after the relevant technical and session evidence exists.
