# SSI V5 — BODY_FROZEN T0 / PRE-ISKRA Public Baseline

**Date:** 2026-09-05  
**Status:** `T0 BASELINE RECORDED / CONTINUUM CLOSED / PRE-ISKRA`  
**Publication model:** sanitized evidence only; private implementation is not distributed.

## What T0 means

T0 is the controlled starting point for the next experimental series. It is **not** the result of the later cross-domain or ISKRA experiments.

The purpose of this snapshot is to preserve a measurable pre-ISKRA baseline so that later stages can be compared against the same starting state.

Planned comparison logic:

```text
T0 = BODY_FROZEN baseline before ISKRA

T1 = the same baseline executes controlled cross-domain experiments
     without ISKRA, producing a no-ISKRA comparison line

T1-ISKRA = independent ISKRA variants start from the same T0
           and execute the same experiment contract

T2 = validated skills/competences from the independent lines may be
     compared, selected and consolidated under a separate test contract
```

Future stages are research plans, not results claimed by this T0 package.

## Current closure evidence

```text
CONTINUUM_FINAL_STATUS = CLOSED
CONTINUUM_TESTS = 23/23 PASS
MAIN_SCENARIOS = 22/22 PASS
E2E_CLOSURE = 19/19 PASS
FINAL_GUARD = 26/26 PASS
ACTIVE_FAILURES = 0
INVARIANT_VIOLATIONS = 0
OPEN_BLOCKERS = 0
EXISTING_SUITE = 580 PASS + 12 SUPERSEDED = 592
```

`SUPERSEDED` records are preserved as historical evidence and are not counted as active failures.

## BODY_FROZEN snapshot

The newest supplied private manifest records:

```text
TOTAL_FILES = 1781
PYTHON_FILES = 587
```

The source files themselves are not included here. These counts are published only as baseline metadata.

## Micronetwork / V10 public baseline

The supplied sanitized snapshot reports:

```text
MICRONETWORKS = 8
MODULES = 8
LAYERS = 3
V10 = ACTIVE
```

Implementation details remain private.

## Skill lifecycle baseline

The explicit public skill registry counters in the supplied T0 snapshot are currently `0` for skill/candidate/challenger/champion lifecycle counts. This package **does not infer skill counts from micronetwork candidate records or test artifacts**. That distinction is intentional so future T1/T2 comparisons do not silently change the counting definition.

## Publication boundary

This directory contains no private source code, local filesystem paths, secrets, raw memory stores, prompt templates, internal class/function names, or implementation-level migration maps.

See `CLAIM_BOUNDARIES.md` for the exact scope of the claims.
