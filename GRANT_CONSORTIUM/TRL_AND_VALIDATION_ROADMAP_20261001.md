# SSI V5 — TRL and Validation Roadmap — 2026-10-01

**Latest Final follow-up:** [4 PASS / 3 INCONCLUSIVE, followed by an infrastructure stop](../RESULTS/SSI_FINAL_RECOVERY_STOP_20261002.md). This later run supersedes the first batch as the latest core-runtime observation; the earlier result remains preserved.

**Evidence update — 2026-10-02:** The local ZeroLab demonstration is an additional internal software evidence point. It does not automatically advance the existing planning bands or inherit the first CZARA curriculum's qualification.

[Current CZARA status](../CZARA_CURRENT_STATUS.md) · [ZeroLab results](../ZERO_LAB_V2_FIRST_RESULTS_20261002.md) · [Evidence and provenance](../evidence/ZERO_LAB_V2_20261002/README.md)

**Purpose:** translate SSI's evidence history into a conservative maturity path for proposal planning.  
**Important:** the bands below are internal planning hypotheses, not an external TRL certification. The selected funding call and consortium must agree the formal TRL interpretation.

## Why SSI should not use one TRL number for everything

SSI contains different assets at different maturity levels:

- core persistent multi-agent software;
- LAB / evidence / provenance tooling;
- CZARA Human-AI collaboration layer;
- dynamic mission training;
- WEB engineering track;
- drone / humanoid / rescue software laboratories;
- offline-resilience concepts;
- physical robotics integrations that are not yet validated.

A single project-wide TRL would hide these differences.

## Provisional planning bands

| Asset | Current evidence | Planning band | Target with partners |
|---|---|---:|---:|
| Core SSI multi-agent/evidence runtime | repeated internal software-lab operation and regression evidence | TRL 3-4 | TRL 5-6 where call permits |
| LAB / evidence / provenance workflow | operational internally; failures/replay preserved | TRL 4 | TRL 5-6 |
| CZARA RND layer | completed internal training + frozen validation/Champion cycle | TRL 3-4 | TRL 5 in partner workflow |
| ZeroLab V2 extension | operator-reported 8/8 local-data executor pilot; no training qualification | not assigned from pilot alone | partner-defined end-to-end experiment validation |
| Drone / humanoid / rescue domain logic | software-lab scenarios only | TRL 3-4 | TRL 5 with relevant simulator/physical environment |
| Offline / degraded-connectivity research | architecture and planned experiments | TRL 2-3 | TRL 4-5 after controlled validation |
| Physical robot deployment | not established | below claimed physical validation level | call-specific controlled pilot |

These are deliberately conservative. They should be replaced by asset-specific, evidence-linked TRL statements in the final proposal.

## Validation ladder

```text
L0  ARCHITECTURE / HYPOTHESIS
L1  INTERNAL SOFTWARE TEST
L2  REPEATED SOFTWARE-LAB EVIDENCE
L3  FROZEN INTERNAL VALIDATION
L4  PARTNER-DEFINED HELD-OUT BENCHMARK
L5  INDEPENDENT REPLICATION
L6  SIMULATION / DIGITAL-TWIN VALIDATION
L7  CONTROLLED PHYSICAL PILOT
L8  MULTI-SITE / MULTI-PARTNER VALIDATION
L9  DEPLOYMENT / PRODUCT-SPECIFIC QUALIFICATION
```

These levels are an SSI evidence ladder, not a replacement for official TRL definitions.

## Current position by evidence ladder

- Core software: L2-L3 depending on subsystem.
- CZARA first cycle: L3 for the completed internal curriculum.
- Mexico/partner benchmark: planned L4.
- Independent replication: not yet L5.
- Physical robotics: not yet L7.
- Production qualification: not claimed.

## Proposed grant progression

### Phase 1 — baseline freeze

- select exact SSI version;
- freeze datasets / task generators / evaluation logic;
- establish comparator baselines;
- define partner-specific KPIs;
- reproduce current public aggregate where possible.

### Phase 2 — partner-defined held-out benchmark

- partner owns unseen test design;
- criteria fixed before run;
- SSI cannot learn from frozen evaluation cases while they are scored;
- all PASS / FAIL / INCONCLUSIVE retained.

### Phase 3 — simulation / digital twin

- integrate with partner simulator;
- model latency, sensor uncertainty, failures and environmental variation;
- compare SSI against agreed baseline/controller.

### Phase 4 — controlled physical pilot

Only after safety and integration gates:

- bounded operational envelope;
- human stop authority;
- no unrestricted autonomous deployment;
- instrumentation and replay;
- predefined abort states;
- target-specific acceptance criteria.

### Phase 5 — independent replication

A different team/site repeats a frozen benchmark using an agreed package and reports discrepancies.

## Required evidence for a TRL advance

No TRL advance should be based only on narrative. Each proposed advance should link:

```text
CLAIM
-> TARGET ENVIRONMENT
-> VERSION
-> ACCEPTANCE CRITERIA
-> BASELINE
-> EXECUTION
-> EVIDENCE
-> FAILURE ANALYSIS
-> RETEST
-> EXTERNAL REVIEW
```

## Current non-claims

The roadmap does not establish physical drone/humanoid/rescue validation, safety certification, independent replication or production readiness.

