# SSI V5 — Live Reviewer Interface

**Recorded:** `2026-09-07`  
**Status:** `LIVE / READ-ONLY REVIEWER OBSERVABILITY`  
**Scope:** multi-BODY observation and informational questioning  
**Execution authority:** local ROOT only

SSI V5 includes a shared live reviewer interface intended to demonstrate that the experimental BODY lines exist as running systems and expose observable state during operation.

The interface is a **demonstration and observability layer**, not a remote administration console.

## 1. Shared view, separate BODY runtimes

The reviewer interface can present the seven experimental lines in one place:

```text
BODY_FROZEN
ISKRA 1 — NICE
ISKRA 2 — GUARDIAN
ISKRA 3 — JUSTICE
ISKRA 4 — EXPLORER
ISKRA 5 — PRAGMATIST
ISKRA 6 — SKEPTIC
```

The shared interface does not merge these systems. Each BODY retains its own runtime, state, memory, CONTINUUM, LAB and mission history. The interface only aggregates reviewer-safe observations.

A BODY is shown as online only when its runtime is actually responsive. A configured but stopped BODY remains visible as offline.

## 2. What a reviewer can observe

For a running BODY the interface may expose a sanitized subset of live state, including:

- runtime status and uptime;
- active mission count and current mission stage;
- progress and latest checkpoint/result;
- CONTINUUM status;
- LAB progress and aggregate PASS/FAIL counts;
- reviewer-safe micronetwork status and routing class;
- high-level ISKRA profile/state where applicable;
- basic hardware utilization;
- sanitized public events and evidence references.

The goal is to let a reviewer see that the system is actively operating, rather than relying only on static README descriptions or screenshots.

## 3. Reviewer questions

The interface includes an informational query channel (`demo_query`).

A reviewer may ask questions such as:

```text
What are you doing now?
Which mission is active?
What stage are you currently executing?
What was the latest checkpoint result?
What is the current CONTINUUM state?
Why was the current route class selected?
What public evidence has been produced?
```

Responses are intended to be short, reviewer-facing explanations based on sanitized observable state.

For example, a question such as "Why was VERIFY selected?" may return a concise audit rationale such as:

```text
The current state was classified as similar to a previously verified case,
so the VERIFY path was selected before reuse.
```

This is an audit explanation, not disclosure of private chain-of-thought, hidden prompts or proprietary implementation details.

## 4. Read-only boundary

The reviewer interface is explicitly non-executive.

It must not provide remote access to:

- mission creation or execution;
- Kilo execution;
- pause/resume/restart controls;
- ROOT commands;
- runtime configuration changes;
- arbitrary code execution;
- private filesystem access;
- private memory access;
- source-code retrieval;
- secrets, tokens or credentials.

Requests attempting to perform an action rather than observe the system should be rejected as read-only.

Conceptually:

```text
REVIEWER
-> LIVE REVIEWER INTERFACE
-> SANITIZED OBSERVABILITY
-> INFORMATIONAL RESPONSE
```

There is no intended execution path from the reviewer interface into the local ROOT control surface.

## 5. Local ROOT remains separate

The local ROOT terminal remains the private execution and administration surface.

```text
LOCAL ROOT
= commands
+ missions
+ local tools
+ Kilo
+ execution control

REVIEWER INTERFACE
= observation
+ public status
+ public evidence
+ informational questions
```

This separation allows the project to demonstrate a running SSI BODY ecosystem without exposing the system's execution authority to external reviewers.

## 6. Public/private information boundary

The public reviewer view is intended to show **what the system is doing and what observable result it produces**, while withholding information that would expose private implementation or operational secrets.

Reviewer-safe information may include:

```text
status
mission stage
progress
checkpoint result
CONTINUUM state
LAB state
aggregate micronetwork state
route class
public evidence
basic resource utilization
```

Private information remains outside the reviewer interface, including:

```text
source code
private prompts/instructions
private memory
implementation-specific configuration
credentials/secrets
private filesystem contents
administrative control paths
```

## 7. Demonstration purpose

The primary purpose of this interface is evidentiary and demonstrational.

It gives a reviewer the ability to observe multiple SSI BODY lines live, compare their current states and ask the running system about its observable activity without requiring access to private code or the local execution console.

In practical terms, the reviewer can verify that the BODY lines are not merely static descriptions in a repository: they can be observed as separate running systems with changing state, missions, checkpoints and evidence.

## 8. Access publication policy

The existence and capability of the reviewer interface may be documented publicly.

The live access address is **not published in the public repository at this stage**. Access can be provided privately to an invited reviewer when a demonstration is arranged.

This keeps the public research record transparent about the capability without unnecessarily publishing an operational endpoint.

## 9. Claim boundary

The existence of the live reviewer interface demonstrates an observability and demonstration capability. It does not by itself prove correctness of every SSI component, production readiness, AGI, consciousness or the success of the 21-experiment program.

Its role is narrower and useful:

```text
STATIC DOCUMENTATION
+ SANITIZED EVIDENCE
+ LIVE READ-ONLY OBSERVATION
+ REVIEWER QUESTIONS
-> stronger auditability of the running research system
```
