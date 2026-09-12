# SSI V5 — Central Control and Reviewer Interface Overview

**Status:** `PUBLIC ARCHITECTURE OVERVIEW / 2026-09-12`  
**Repository role:** evidence and review mirror only  
**Implementation:** proprietary / private

## Two intentionally separate interfaces

SSI V5 now distinguishes two control surfaces with different authority.

```text
LOCAL CENTRAL CONTROL
= owner/operator interface
= may launch local BODY control views
= may supervise training / experiment workflows
= may run S10 collection, evaluation and descendant preparation

PUBLIC REVIEWER INTERFACE
= observer-only
= sanitized state and evidence
= no ROOT authority
= no arbitrary mission execution
= no runtime configuration writes
```

The design principle remains:

```text
OBSERVE != CONTROL
```

## Central local control concept

The local control center is intended as a single entry point for the seven controlled BODY lines:

```text
BODY_FROZEN
ISKRA1 NICE
ISKRA2 GUARDIAN
ISKRA3 JUSTICE
ISKRA4 EXPLORER
ISKRA5 PRAGMATIST
ISKRA6 SKEPTIC
```

The operator can select a BODY and open its dedicated local control view while retaining access to the higher-level S10 cross-consolidation panel.

The central panel also exposes high-level research workflow controls such as:

- training-package directories per BODY;
- experiment-package directories per BODY;
- live supervision status;
- S10 collect / evaluate / upgrade workflow;
- Hermes guidance and status messages;
- calibration status;
- public reviewer-interface shortcut;
- evidence / report access.

The public repository does not expose executable control code, filesystem paths or credentials.

## Guided workflow

The higher-level S10 workflow is presented as a guided sequence:

```text
1. COLLECT
-> bootstrap or incremental Hermes memory

2. EVALUATE
-> family grouping / deep comparison / evidence ranking

3. UPGRADE
-> create a versioned descendant for selected target BODY lines
```

The operator may select one, several or all eligible BODY lines as upgrade targets while using a broader set of BODY lines as evidence sources.

## Hermes as an interface navigator

Hermes has an operator-guidance role in the central interface.

It can explain:

- what the current stage is doing;
- why a stage may take longer;
- whether the system is still actively processing;
- which next action is appropriate;
- whether a first full bootstrap or later incremental update is being performed.

This guidance is separate from ROOT authority. Hermes is not treated as an independent scientific auditor.

## Live progress

Long operations expose status rather than appearing frozen. The UI design includes:

- active stage;
- current BODY / family where available;
- progress indication;
- elapsed time;
- live/audit messages;
- READY / WORKING / WARNING / BLOCKED states.

This is a usability feature, not a scientific result.

## Training and experiment supervision

The central control layer can organize access to per-BODY training and experiment packages and supervise execution where an existing backend/runner is available.

The architecture deliberately avoids inventing a fake execution backend merely to make a button appear functional. If a real runner is unavailable, the control layer should report a missing backend rather than silently simulating success.

## Research safety and reproducibility

The central interface is designed around versioned descendants and preserved FAIR baselines.

```text
BASELINE
-> observe / collect / compare
-> create descendant
-> validate descendant

BASELINE
!= silently rewritten
```

This boundary is important for later before/after comparison and auditability.

## Public claim boundary

The existence of a local control center and reviewer interface does not imply that:

- every research stage has completed;
- all seven BODY lines have reached the same training maturity;
- S10 calibration is complete;
- external reviewers have independently validated SSI;
- the interface itself proves scientific correctness.

The interfaces are infrastructure for controlled execution, observation, provenance and review.
