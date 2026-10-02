# CZARA ZERO-LAB / LAB_ARCHITECT — Module Definition

**Evidence update — 2026-10-02:** This is the preserved V1 design. ZeroLab V2 now has an installed local software runtime and an 8/8 executor pilot. Its bounded adapters cover part of this broader research design; they do not establish a general physical laboratory builder.

[Current CZARA status](CZARA_CURRENT_STATUS.md) · [ZeroLab results](ZERO_LAB_V2_FIRST_RESULTS_20261002.md) · [Evidence and provenance](evidence/ZERO_LAB_V2_20261002/README.md)

**Date:** 2026-10-01  
**Status:** design frozen for implementation  
**Purpose:** allow CZARA to help design the laboratory required by a new experiment instead of assuming that a suitable laboratory already exists.

## Core rule

The module starts from the following assumption:

> **No laboratory exists yet.**

It receives an experiment description and must derive the minimum auditable environment required to test it.

It must not silently reuse the current SSI LAB merely because that LAB exists.

## Intended flow

```text
EXPERIMENT REQUEST
      |
      v
CZARA
      |
      v
ZERO-LAB / LAB_ARCHITECT
      |
      +--> hypothesis and falsification target
      +--> actors / roles / authority
      +--> required hardware and software
      +--> sensors / data sources
      +--> measurements and metrics
      +--> PASS / FAIL / INCONCLUSIVE rules
      +--> evidence requirements
      +--> negative controls
      +--> safety states
      +--> simulation vs physical requirements
      +--> budget / resource constraints
      +--> required BLOCKS / micronetworks
      |
      v
LAB BLUEPRINT
      |
      v
DIRECTOR REVIEW
      |
      v
BODY_FROZEN BUILD / ADAPT
      |
      v
LAB SELF-TEST
      |
      v
FREEZE EXPERIMENT CONTRACT
      |
      v
BENCHMARK
      |
      v
EVIDENCE
```

## Authority boundary

LAB_ARCHITECT is a design module, not ROOT.

It may:
- propose a laboratory architecture;
- list missing equipment or software;
- define candidate measurements and controls;
- identify ambiguity or missing evidence;
- produce alternative blueprints;
- request clarification through CZARA / DIRECTOR;
- recommend that an experiment remain INCONCLUSIVE if it cannot be tested honestly.

It may not:
- promote a result to PASS;
- rewrite a frozen benchmark silently;
- bypass DIRECTOR;
- directly command BODY_FROZEN outside the normal authority path;
- hide missing hardware or evidence;
- claim physical validation from simulation.

## ZERO-LAB contract

Input should include, when available:

```json
{
  "experiment_id": "...",
  "research_question": "...",
  "hypothesis": "...",
  "environment": "...",
  "participants": [],
  "available_hardware": [],
  "available_software": [],
  "constraints": [],
  "safety_constraints": [],
  "budget": null,
  "time_limit": null,
  "requested_evidence": []
}
```

Output is a versioned `LAB_BLUEPRINT`:

```json
{
  "schema": "ssi.czara.lab-blueprint.v1",
  "experiment_id": "...",
  "blueprint_revision": "REV_0",
  "assumption": "ZERO_LAB",
  "testability": "TESTABLE | PARTIALLY_TESTABLE | NOT_TESTABLE",
  "required_components": [],
  "measurement_plan": [],
  "controls": [],
  "negative_controls": [],
  "pass_rules": [],
  "fail_rules": [],
  "inconclusive_rules": [],
  "evidence_plan": [],
  "safety_plan": [],
  "self_tests": [],
  "missing_resources": [],
  "blocks_required": [],
  "open_questions": []
}
```

## Multi-Iskra design mode

A later variant may ask several Iskras to independently design the laboratory for the same experiment.

```text
Experiment
   +--> Iskra A -> Blueprint A
   +--> Iskra B -> Blueprint B
   +--> Iskra C -> Blueprint C
                      |
                      v
DIRECTOR + EVIDENCE_SCEPTIC
                      |
                      v
consolidated LAB blueprint
```

The comparison must preserve disagreements instead of forcing consensus.

## Mexico use case

For the planned external workflow, a professor can define a new research problem in Spanish. CZARA preserves the original statement and translates it for ROOT. LAB_ARCHITECT then derives what environment is required to test the claim.

Example:

```text
"Test UAV behavior after GPS and network loss."
```

The output should describe, at minimum:
- how GPS loss is introduced and verified;
- what "network loss" means operationally;
- control run conditions;
- safety / return / safe-land states;
- telemetry and evidence capture;
- repeated trials;
- what constitutes PASS, FAIL, or INCONCLUSIVE;
- what can be simulated and what requires physical hardware.

## Acceptance gates for implementation

The module is not considered deployed merely because the file exists.

A local deployment should prove:

1. module import/self-test PASS;
2. one synthetic ZERO-LAB request produces a valid versioned blueprint;
3. the module cannot write PASS results;
4. frozen benchmark mutation is rejected;
5. missing-resource cases remain explicit;
6. DIRECTOR remains the authority boundary;
7. all blueprint revisions are auditable;
8. no paid/remote model call occurs during installer self-test unless explicitly enabled.

## Relationship to first CZARA training

The first CZARA training cycle is now a frozen evidence point.

ZERO-LAB / LAB_ARCHITECT is the next module and should be evaluated separately. Its future results must not be retroactively mixed into the first-cycle evidence.

