# SSI V5 — Start Here for Grant and Technical Reviewers

**Updated:** `2026-09-17`  
**Repository role:** `PUBLIC EVIDENCE / REVIEW MIRROR`  
**Proprietary implementation:** private by design.

## Current status in one view

```text
V4 S1-S10 = COMPLETE / PASS under one run ID
7 BODY final state = 7/7 PASS
CONSOLIDATION / PROMOTION / BRIDGE = PASS
REGRESSION = PASS
ROLLBACK = NOT REQUIRED
BODY_FROZEN final promoted reload = 144/144 expected entries
POST-S10 DRONE SOFTWARE LAB = 6/6 scenarios PASS
POST-S10 HUMANOID SOFTWARE LAB = 15/15 scenarios PASS
POST-S10 TOTAL = 21 scenarios
PUBLIC REVIEWER ACCESS = observer-only
PHYSICAL VALIDATION = not claimed
INDEPENDENT EXTERNAL REPLICATION = not claimed
```

## Why this project is now collaboration-ready

The 2026-09-17 V4 run moved SSI beyond a roadmap-only stage. A complete controlled software cycle now exists with:

- seven independent BODY development lines;
- staged S1-S10 progression under one run ID;
- declared consolidation / promotion / bridge gates;
- regression verification before advance;
- rollback accounting;
- promoted-state reload verification;
- post-training domain execution;
- preserved evidence, hashes and provenance;
- explicit claim boundaries.

The strongest current collaboration opportunities are therefore not generic advisory work, but externally defined validation, falsification, replication and domain transfer.

## Research areas relevant to partners

```text
AGENTIC AI
MULTI-AGENT SYSTEMS
CONTINUAL / LIFELONG LEARNING
PERSISTENT COMPETENCE AND MEMORY
ADAPTIVE ROUTING
CROSS-AGENT COMPETENCE CONSOLIDATION
FAILURE-AWARE RECOVERY
AUTONOMOUS SYSTEMS
DRONES / MULTI-ROBOT SYSTEMS
HUMANOID MOTION / STABILITY
AUDITABLE / EVIDENCE-ORIENTED AGENT WORKFLOWS
CROSS-DOMAIN TRANSFER
```

## External collaboration model

Preferred model:

```text
EXTERNAL PARTNER DEFINES A PREVIOUSLY UNSEEN PROBLEM
-> ACCEPTANCE CRITERIA FROZEN BEFORE RUN
-> SSI EXECUTION
-> PASS / FAIL / INCONCLUSIVE PRESERVED
-> EVIDENCE / TIMINGS / FAILURES RETAINED
-> OPTIONAL CONSOLIDATION
-> TARGET-SPECIFIC RE-VALIDATION
-> RESULT RETURNED TO PARTNER
```

Possible partner roles include:

- research collaborator;
- consortium partner / beneficiary where programme rules permit;
- external challenge designer;
- independent replication / validation partner;
- continual-learning or multi-agent methods reviewer;
- drone/swarm research laboratory;
- humanoid/robotics research laboratory;
- later physical validation partner.

## Current architecture summary

SSI is a persistent multi-agent software ecosystem containing:

```text
DIRECTOR
+ BODY_FROZEN
+ ISKRA1..ISKRA6
+ HERMES
+ CONTINUUM
+ ROUTER V10
+ ROUTER S10
+ MICRONETWORKS / LEGO / POCKET
+ WORLD / DOMAIN LAYERS
+ EVIDENCE / CHECKPOINT / PROVENANCE
```

S1-S10 is one controlled training/evaluation process inside this ecosystem, not the entire system.

## Latest completed V4 milestone

```text
RUN_ID = RUN_20260917T024400_DCD7FD
TRACE_ROOT = TRACE_5EE50008986B
FINAL_STAGE = S10
COMPLETE = true
```

Final state:

```text
BODY_FROZEN = PASS
ISKRA1 = PASS
ISKRA2 = PASS
ISKRA3 = PASS
ISKRA4 = PASS
ISKRA5 = PASS
ISKRA6 = PASS
CONSOLIDATION = PASS
REGRESSION = PASS
ROLLBACK = NOT_REQUIRED
ADVANCE_ALLOWED = true
```

Final promoted BODY_FROZEN reload:

```text
expected_count = 144
loaded_count = 144
complete_accounting = true
fresh_process = true
```

## Post-S10 software-domain results

```text
DRONE / SWARM = PASS / 6 scenarios
HUMANOID MOTION / STABILITY = PASS / 15 scenarios
TOTAL = 21 scenarios
```

These are software-domain results only. No physical drone or humanoid validation is claimed.

## Reviewer access boundary

```text
PUBLIC REVIEWER
= sanitized status / evidence / allowed questions
!= ROOT
!= arbitrary mission execution
!= runtime configuration write access
```

## What reviewers should not infer

Do not infer:

- physical drone validation;
- physical humanoid validation;
- live autonomous financial-account execution;
- independent external replication;
- universal superiority of SSI, V10, S10 or any V1-V4 configuration;
- production readiness;
- AGI or consciousness.

## Recommended reading order

1. [`CURRENT_TRUTH_INDEX_20260917.md`](CURRENT_TRUTH_INDEX_20260917.md)
2. [`SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md`](SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md)
3. [`RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md`](RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md)
4. [`RESULTS/V4_PUBLIC_SUMMARY_20260917.json`](RESULTS/V4_PUBLIC_SUMMARY_20260917.json)
5. [`VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md`](VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md)
6. [`COLLABORATION_AND_PARTNER_ENTRY.md`](COLLABORATION_AND_PARTNER_ENTRY.md)
7. [`EXTERNAL_CHALLENGE_ENTRY_20260914.md`](EXTERNAL_CHALLENGE_ENTRY_20260914.md)

Older dated files remain preserved as historical evidence. If an older status conflicts with the 2026-09-17 evidence-backed state, use the newer current-state documents above.