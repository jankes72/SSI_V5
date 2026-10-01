# SSI V5 — Risk, Safety, Security and Ethics — 2026-10-01

**Purpose:** proposal-level risk and assurance framework.  
**Status:** planning baseline; each physical or domain-specific pilot requires its own detailed assessment.

## Risk governance principle

```text
CAPABILITY CLAIM
!=
PERMISSION TO DEPLOY

TEST PASS
!=
SAFETY CERTIFICATION

AUTONOMOUS OUTPUT
!=
UNSUPERVISED AUTHORITY
```

## Core technical risks

| Risk | Example | Mitigation / evidence |
|---|---|---|
| Evaluation contamination | held-out cases learned before scoring | frozen evaluation state; version/state manifest |
| False PASS | reviewer contract misses required output | explicit output binding; independent verifier |
| Silent regression | new observability or routing changes behavior | non-interference / regression gates |
| Backlog / concurrency failure | INFLIGHT_LIMIT creates unresolved cases | hard execution gate; replay; concurrency telemetry |
| Stale competence | old reusable skill used outside validity | versioning, expiry/target validation, escalation |
| Unsafe cross-domain reuse | competence transfers without evidence | domain-specific acceptance criteria and re-validation |
| Evidence tampering | deleted/modified/forged result | hashes, chain checks, negative controls, immutable history |
| Single-operator bias | developer also evaluates system | external benchmark designers and replication partners |

## Robotics / physical safety

Physical pilots should not start until the responsible partner defines:

- operational design domain;
- maximum speeds/forces/energy where relevant;
- geofencing / workspace limits;
- emergency stop;
- human supervisory authority;
- safe state on communication loss;
- sensor uncertainty limits;
- prohibited actions;
- abort conditions;
- incident logging;
- hardware-specific risk assessment.

SSI public software evidence is not a substitute for machinery, robotics, aviation, workplace or sector-specific compliance.

## Cybersecurity

Minimum project controls should include:

- least-privilege access;
- separated public reviewer and private control planes;
- no credentials in public evidence;
- authenticated partner access;
- audit logs for configuration and run changes;
- dependency and secret scanning where feasible;
- threat modelling for remote interfaces;
- bounded upload/input handling;
- incident response and key rotation procedures.

For degraded-connectivity/offline research, resilience experiments must remain controlled and lawful. Research on signal environments must not be interpreted as authorization to interfere with third-party communications.

## Data protection

Before using partner or human-participant data, classify:

- personal data;
- sensitive personal data;
- confidential industrial data;
- security-sensitive operational data;
- public/synthetic data.

Use data minimization and purpose limitation. The current WEB training record is SYNTHETIC_ONLY; future partner datasets require separate governance.

## Human-AI interaction

CZARA and related layers should preserve:

- original expert input where allowed;
- translation provenance;
- role/authority;
- distinction between observation, suggestion and approved experiment change;
- chronology;
- human override and stop authority.

The system should not silently convert informal comments into formal experimental requirements.

## Dual-use and misuse review

Potentially sensitive capabilities should be screened before external release, including:

- autonomous-system integration;
- RF/sensor environment analysis;
- degraded-connectivity coordination;
- surveillance-adjacent sensing;
- security-sensitive infrastructure scenarios.

Where dissemination could materially increase misuse risk, publish bounded findings rather than reconstructive implementation details.

## Ethics and research integrity

The project should preserve:

- negative results;
- superseded states;
- declared limitations;
- authorship and attribution;
- conflict-of-interest disclosure;
- separation of internal evidence from independent validation;
- no fabricated external endorsement.

## Risk register template

For each WP maintain:

```text
RISK_ID
DESCRIPTION
PROBABILITY
IMPACT
OWNER
EARLY_WARNING
MITIGATION
CONTINGENCY
RESIDUAL_RISK
EVIDENCE
```

## Current critical risks before external benchmark

1. live post-repair core continuation must be re-established under a new provenance boundary;
2. partner-defined benchmark independence must be protected;
3. physical validation still requires external hardware/facility and safety ownership;
4. proposal-specific legal/IP/data responsibilities are not yet frozen.

## Claim boundary

This document is a planning control layer, not a formal safety case, ethics approval, cybersecurity certification or regulatory compliance statement.
