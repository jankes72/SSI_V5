# SSI V5 — Candidate Work Packages, Deliverables and Milestones — 2026-10-01

**Status:** reusable proposal skeleton.  
**Rule:** exact WP numbering, leaders, dates, person-months and deliverable types must be adapted to the selected call.

## Candidate project structure

### WP1 — Requirements, governance and benchmark contract

**Objectives**
- freeze use cases, roles, safety boundaries and evaluation rules;
- define baselines, KPIs and evidence requirements;
- establish background IP and data-governance boundaries.

**Candidate tasks**
- T1.1 use-case and stakeholder requirements;
- T1.2 benchmark/acceptance contract;
- T1.3 data, ethics, security and IP governance.

**Candidate deliverables**
- D1.1 Requirements and benchmark specification;
- D1.2 Governance, IP, data and security baseline.

**Milestone**
- M1: acceptance criteria and baseline frozen before official SSI benchmark.

### WP2 — SSI reproducibility and evidence baseline

**Objectives**
- reproduce public SSI aggregate evidence;
- harden machine-verifiable evidence;
- create partner-readable version/provenance manifest.

**Tasks**
- T2.1 public evidence verification CI;
- T2.2 run/provenance manifest;
- T2.3 failure, replay and rollback verification;
- T2.4 comparator baseline harness.

**Deliverables**
- D2.1 SSI reproducibility package;
- D2.2 baseline comparison protocol.

**Milestone**
- M2: consortium accepts baseline and evidence pipeline.

### WP3 — Human-AI collaboration and continual learning

**Objectives**
- validate CZARA / DIRECTOR / BODY_FROZEN research workflow;
- measure training-to-reuse transition;
- test frozen evaluation and revision lineage.

**Tasks**
- T3.1 multilingual expert interaction;
- T3.2 controlled competence acquisition;
- T3.3 frozen validation;
- T3.4 expert corrections and provenance.

**Deliverables**
- D3.1 Human-AI collaboration demonstrator;
- D3.2 frozen benchmark evidence pack.

**Milestone**
- M3: partner-defined unseen evaluation completed without scoring-time learning.

### WP4 — Simulation and domain integration

**Objectives**
- connect SSI to consortium simulation/digital-twin assets;
- validate domain-specific planning under failures and uncertainty.

**Possible domains**
- drones / swarms;
- multi-robot rescue;
- humanoid motion/stability;
- degraded-connectivity/offline scenarios.

**Deliverables**
- D4.1 integration adapters;
- D4.2 simulation benchmark report;
- D4.3 robustness/failure-recovery report.

**Milestone**
- M4: agreed simulation KPIs reached or limitations formally documented.

### WP5 — Controlled physical pilot

**Objectives**
- perform a bounded physical validation where the call and safety case permit.

**Prerequisites**
- partner-owned appropriate hardware/facility;
- safety owner;
- emergency stop and abort criteria;
- risk assessment;
- instrumentation and evidence capture.

**Deliverables**
- D5.1 physical pilot plan and safety case;
- D5.2 pilot evidence and deviation report.

**Milestone**
- M5: controlled physical pilot completed or stopped under predefined safety criteria.

### WP6 — Independent replication and scientific evaluation

**Objectives**
- separate development from final validation;
- run frozen tasks at a second team/site where feasible.

**Deliverables**
- D6.1 independent replication package;
- D6.2 replication report;
- D6.3 discrepancy and limitation analysis.

**Milestone**
- M6: independent result accepted as PASS / FAIL / INCONCLUSIVE without retrospective criterion changes.

### WP7 — Exploitation, dissemination and standardization path

**Objectives**
- identify deployable outputs;
- protect exploitable IP;
- publish suitable research outputs;
- define post-project continuation.

**Deliverables**
- D7.1 exploitation plan;
- D7.2 dissemination/reproducibility package;
- D7.3 post-project integration roadmap.

## SSI-specific responsibility candidates

SSI may lead or contribute strongly to:

- WP2 evidence/reproducibility;
- WP3 agentic/Human-AI continual-learning work;
- SSI-side tasks in WP4;
- experiment logging and replay in WP5;
- technical input to exploitation/IP boundaries.

A partner with established EU-project management capability may be better placed to coordinate the complete project unless the final consortium decides otherwise.

## KPI families

Use call-specific targets, but candidate KPI families include:

- frozen benchmark completion rate;
- PASS / FAIL / INCONCLUSIVE distribution;
- capability reuse rate;
- escalation rate;
- rollback/recovery success;
- evidence completeness;
- reproducibility discrepancies;
- latency and cost;
- expert correction traceability;
- safety-stop correctness;
- simulator-to-physical transfer gap.

## Anti-inflation rule

A deliverable should not be marked achieved solely because code exists. Each technical milestone should define the evidence required to close it.
