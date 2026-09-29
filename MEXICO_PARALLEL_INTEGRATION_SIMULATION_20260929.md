# SSI V5 — Parallel Mexico Integration Simulation Under Load
**Date:** 2026-09-29  
**Status:** INTERNAL INTEGRATION SIMULATION / LIVE TRAINING / NOT EXTERNAL VALIDATION

## Why this is running now

SSI V5 is currently running two training workloads in parallel on the private runtime in order to approximate the concurrency expected during a future Poland–Mexico research session.

The goal is not to publish a clean performance benchmark. The goal is to observe whether the system remains coherent while multiple major SSI layers are active at the same time.

The current private runtime combines:

- the main SSI core training, now active at **S20**;
- **BODY_FROZEN** case execution and LAB verification;
- the new **CZARA Live Training** track;
- DIRECTOR interaction;
- long-term conversation/context memory;
- ROOT GUI/TUI observation;
- evidence/event recording;
- the Mexico research-session ingress design.

The intended future remote session adds the external Web/Tailscale path on top of the same runtime rather than replacing the internal components.

## Current CZARA training track

The installed CZARA training track reports:

```text
CURRICULUM = 160
TRAINING = 120
VALIDATION = 24_FROZEN
CHAMPION_BENCHMARK = 16_FROZEN

PARTICIPANTS = 20
  15 students
   4 experts
   1 professor

SKILL_CANDIDATES = 520
```

The training is designed as a live research-session simulation rather than a detached unit-test loop.

A simulated professor message is intended to follow the same logical ingress used by the Mexico research interface:

```text
SIMULATED PROFESSOR (Spanish)
-> CZARA ingress
-> original Spanish preserved
-> Polish translation
-> role / authority classification
-> session memory
-> DIRECTOR
-> BODY_FROZEN / LAB when required
-> result / evidence
-> observer interfaces
```

The installed training path identifies the shared ingress as:

```text
czara.translate_and_append
```

The scheduler and trainer are separate live processes. The user-level service is active, the scheduler is polling the trainer state, and the trainer was observed running in:

```text
phase = TRAINING
resume = true
live = true
model_policy = AUTO
```

## Concurrent core S20 activity

At the same time, the main SSI training is active at S20.

A live runtime excerpt showed consecutive BODY_FROZEN S20 cases completing with first-candidate PASS decisions, for example:

```text
S20-01-02 PASS
S20-01-03 PASS
S20-01-04 PASS
S20-01-05 PASS
S20-01-06 PASS
S20-02-01 PASS
```

The same excerpt showed:

```text
[NATIVE_CANDIDATE] 1 evaluation=PASS ci=PASS
[TRAINING_EVENT] VERIFIED action=COMPLETE decision=CASE_VERIFIED
[LAB_FLOW] ... COMPLETE pending=0
```

This is a **partial live excerpt**, not a complete S20 result. No full-stage S20 claim is made here.

## What this simulation is intended to test

The important question is not whether CZARA can operate alone.

The intended operating condition is closer to:

```text
MAIN SSI TRAINING / BODY_FROZEN / LAB
                    |
                    |  same machine/runtime resources
                    |
CZARA / DIRECTOR / MEMORY / GUI / TUI
                    |
                    v
          MEXICO RESEARCH SESSION
```

The current parallel run is therefore useful for detecting:

- state leakage between core training and Mexico-session context;
- memory/session-ID mix-ups;
- resource contention between BODY_FROZEN, DIRECTOR, LAB and CZARA;
- translation/context latency while SSI is already busy;
- incorrect authority routing between professor, experts and students;
- GUI/TUI divergence from the underlying runtime;
- scheduler/checkpoint failures under concurrent activity;
- unnecessary Full Flow escalation where validated micro-networks should eventually be reusable.

## Target remote path

The later end-to-end rehearsal is intended to preserve the same internal path while replacing the simulated external source with a real remote device:

```text
REMOTE DEVICE IN MEXICO
-> Tailscale
-> Mexico Web interface
-> shared Mexico/CZARA ingress
-> CZARA
-> DIRECTOR
-> BODY_FROZEN
-> LAB
-> DIRECTOR response
-> CZARA / translation
-> Web
-> Tailscale
-> remote device
```

ROOT GUI and ROOT TUI should observe the same session and the same event IDs rather than maintaining independent copies of the conversation.

The intended event lineage is:

```text
one event_id
-> Mexico Web view
-> ROOT GUI view
-> ROOT TUI view
-> DIRECTOR context
-> evidence/provenance record
```

## Why the load is intentional

Running CZARA in parallel with S20 makes this a deliberately noisy integration environment.

That is useful for **robustness testing**, but it is not suitable for claiming clean speed improvements.

Champion-versus-Full-Flow latency comparisons will require a controlled run in which competing workloads are either fixed or removed.

This current run instead asks:

> Can SSI preserve role boundaries, session context, translation flow, memory, LAB verification and operator visibility while the core system is already working?

## Claim boundary

This document records an **internal integration simulation** and the observed startup/runtime state supplied by the project operator.

It does **not** establish:

- an independent Mexico benchmark result;
- real Mexico-to-Poland network latency;
- successful external Tailscale/Web execution from Mexico;
- full S20 completion;
- CZARA Champion qualification;
- physical drone or robot validation;
- safety certification;
- independent external replication.

The next meaningful step is a two-endpoint rehearsal using the remote Web/Tailscale path while keeping the same CZARA -> DIRECTOR -> BODY_FROZEN -> LAB -> evidence chain.
