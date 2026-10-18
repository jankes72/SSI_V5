# SSI V5

> **Canonical architecture:** [SSI V5 — C4 Architecture](SSI_V5_C4_ARCHITECTURE.md) — single source of truth for the current public system structure. Update the C4 there instead of duplicating architecture diagrams across documents.


**Evidence-first research platform for persistent, adaptive multi-agent AI systems.**

## SSI-wide LEGO MultiControl — architecture decision (18 October 2026)

**[Global architecture decision R1](SYSTEM/SSI_MULTICONTROL_GLOBAL_ARCHITECTURE_DECISION_R1_20261018.md):** LEGO MultiControl will be an **optional, shared validation/composite-control layer for all SSI V5**, not a MultiQuant-owned service. It may advise SCC/Director/Router, historical micronetworks, LEGO Pocket/META, CODEX, ROBERT, labs and robotics through read-only, domain-qualified adapters. **No promotion, registry write, SCC interpreter replacement or automatic execution.** Status: `PLANNED / GLOBAL_SSI / SHADOW_ONLY`, not deployed.

## SSI MultiQuant — five directions and new BIG → MICRO / native low-bit research (18 October 2026)

**Today's declaration:** [SSI MultiQuant D1–D5 — implemented offline prototypes, operator CPU evidence and proposed D4/D5 research gates](PUBLIC_MODELS/SSI_MULTIQ_FIVE_DIRECTIONS_R4_R5_DECLARATION_20261018.md).

- **Offline control prototypes:** D1 hybrid competence memory (R2, 56/56 local tests), D2 fragment-stage gate/Polish observations (R1, 32/32), D3 multi-model fusion planning (R3, 64/64 with R2 integration), plus the existing inert SCC–MultiQuant adapter (23/23). **None is a trained, merged or production-deployed hybrid LLM.**
- **Separate Qwen3-1.7B OFFLINE MICRO:** BF16 source → Q4_K_M ~1.194 GiB artifact and CPU smoke pass; routing tests **R24 FAIL** and **R25 1/4 PASS**. R26 BF16-vs-Q4 comparison deferred; quantization is not proven to cause the failure. No Router promotion.
- **New research goals, not achievements:** **D4 BIG → MICRO** aims at carefully verified 16 GiB-deployable small students derived from selected very-large-model competencies; **D5 NATIVE LOW-BIT STUDENT** investigates distillation and quantization-aware training in the same learning loop. **Neither 70B/120B → 16 GiB production operation nor QAT+KD training has been performed.**
- The Qwen3 OFFLINE MICRO case is **separate** from CPU-7, which remains **1/7 candidates built and 0/7 promoted**. SCC remains the sole mission language; migration/production binding remains pending.

[Latest dated evidence supplement](RESULTS/SSI_V5_PUBLIC_PROGRESS_CPU7_SCC_AWARENESS_20261018.md#update-18-october-2026-director-offline-micro-r21r25-results-and-multiquant-d1d5).

## Latest verified public progress — 2026-10-18

**Operator-reported bounded evidence, not an independent replication:** one CPU-built and locally smoke-tested SSI MultiQuant 1.5B candidate (1/7 built, 0/7 production promoted; 7.16 tok/s in a one-thread sample), plus an **incomplete** SCC/Awareness/Research Memory inventory (25,001 entries scanned, limit reached, no migration or training run). Proprietary SSI code and know-how remain private.

- **[17–18 October public progress report — CPU-7 and SCC/Awareness](RESULTS/SSI_V5_PUBLIC_PROGRESS_CPU7_SCC_AWARENESS_20261018.md)**


## Robert: planned SCC, Luna Navigator and Radar upgrade — 2026-10-15

**PLANNED / NOT IMPLEMENTED / NOT DEPLOYED.** Robert's next upgrade covers integrated desktop control and its own GUI cockpit; a separate Luna instance for navigation, Radar analysis and mission prompts; Director SSI/Director Charlie task delegation; guided conversation/download/install/report training; Work and extensible domain adapters; and verification, Evidence, Notary, memory and evidence-backed replies. The existing Champion/Challenger hierarchy and promotion rules remain unchanged, with skill organization and task-scoped Champion matching through native Research Memory/Router contracts. This is a development plan, not an installation or a new result from Robert's earlier missions.

- **[Full planned scope, pending acceptance and preserved mission baseline](ROBERT/PLANNED_SCC_LUNA_NAVIGATOR_RADAR_UPGRADE_20261015.md)**
- [Robert's existing desktop missions and Technology Radar](ROBERT/README.md)

## SCC BLOCKS mission language — 2026-10-14

**The author/operator reports the first SCC mission-language module deployed and working in SSI.** A27 implements declarative goal notation, deterministic validation, the existing R1 planning contract and the Universal Lab construction view. This publication reproduced **22 Python tests and 10 JavaScript contract assertions, with zero provider calls**. The current scope is goal declaration and linear planning; Champion execution, a general imperative runtime, branches and parallel programs remain separate integration work.

**Inspiracja i źródło adaptowanych mechanizmów: mój brat [amnezja3](https://github.com/amnezja3) i jego [Awareness](https://github.com/amnezja3/awareness).** This continuing credit also records earlier source ideas behind Moralna SI/ISKRA, Football World recursion and the origin/first connection of CZARA. The full article includes a Polish introduction to Awareness, exact upstream module provenance and Paweł's personal appreciation of his brother's technical skills.

- **[SCC module, supported syntax, validation and full attribution](SCC_BLOCKS_MISSION_LANGUAGE_AND_AMNEZJA3_ATTRIBUTION_20261014.md)**
- [Earlier CZARA and source attribution](EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md)

## Director A16 and web access declaration — 2026-10-12

**A16 is installed on MSI and Universal Lab HTTP is ready, according to the operator's installation report.** The Director knowledge baseline now covers **48 topics in Polish and English**, with short, extended and technical answers: SSI, Router V10, Research Memory, six ISKRA actors, drones and Mother systems, humanoids, rescue research, BLOCKS, Hermes, Football World and future programmes.

**Planujemy stronę pierwszego kontaktu, na której po przejściu z GitHuba będzie można porozmawiać z Dyrektorem o SSI bez logowania, również z telefonu. Prywatna współpraca i centrum konferencyjne zachowają własny dostęp. Deklaracja: 12 października 2026. Termin uruchomienia: do ustalenia.** The future guest conversation service is planned; no live conversation URL is announced here. A16's HTTP readiness does not establish live narration or public-service availability.

- **[A16 installation, implemented scope and recorded tests](RESULTS/UNIVERSAL_LAB_DIRECTOR_A16_PROGRESS_20261012.md)**
- **[Full 48-topic Director knowledge — PL/EN, three depths](KNOWLEDGE/SSI_DIRECTOR_A16_PL_EN_20261012.md)**
- **[Dated web Director declaration and delivery gates](SSI_V5_C4_ARCHITECTURE.md#web-director-declaration-20261012)**
- [Long-term programme: core, ISKRA, robotics, worlds and external validation](SSI_V5_C4_ARCHITECTURE.md#long-term-programme-map-and-director-knowledge-coverage--2026-10-12)

## Robert and ISKRA worlds — 2026-10-12

Two complementary records describe the continuing Robert engineering line and the independent ISKRA research programme. They distinguish completed observations, implementation readiness, the operator's current bridge declaration and future acceptance gates.

- **[Robert: desktop missions, Technology Radar, repair learning and operational applications](ROBERT/README.md)** — includes the drone-to-desktop mission methodology, planned ChatGPT/social-account tests, archive-based repair training, collective skill flow and the 50/40/10 economic policy.
- **[ISKRA: worlds, Hermes generations, S1–S40, WEB and long-term learning](ROBERT/ISKRA_WORLDS_AND_LONG_TERM_RESEARCH.md)** — includes individual memory, Football World laboratories, own code, group/coupon evaluation, prospective outcomes, collaboration and affect-like research boundaries.

Both records begin with a five-part executive summary, followed by the full English documentation. Private code, teacher datasets, credentials and operational endpoints are not published.

## 60-second reviewer snapshot

SSI V5 is an independently developed, proprietary-core R&D programme for **persistent multi-agent AI, continual learning, AI-safety-oriented evaluation and evidence-preserving knowledge promotion**. The public repository is the review/evidence layer: it exposes architecture, frozen baselines, protocols, negative results, repairs, benchmark plans and sanitized evidence while keeping reconstructive implementation details private.

**What already exists:** a frozen BODY_FROZEN baseline; six separately persistent ISKRA lines with recorded T0 belief and affect-like control-state baselines; Router V10/S10 and persistent Micronetwork/BLOCKS competence; preserved PASS / FAIL / INCONCLUSIVE histories; ZeroLab V2; CZARA; and a preregistered longitudinal comparison from early ISKRA state through S40 and the later WEB curriculum.

**Why this is an AI-safety research problem:** SSI explicitly tests whether persistent agents can avoid promoting unverified or unreproduced outcomes into reusable knowledge, whether different long-running agents diverge under a shared curriculum, and whether frozen checkpoints, evidence gates, rollback and independent review expose unsafe or unstable learning trajectories.

**Why additional compute matters:** the next comparative layer is not a greenfield build. It requires repeated, isolated runs across BODY_FROZEN and ISKRA1..ISKRA6, frozen checkpoints, held-out/retest workloads and post-training WEB comparisons. More local compute increases experimental independence, repeatability and the number of controlled runs that can be completed without changing the research protocol to fit a single constrained development host.

**Research areas:** AI safety · persistent agents · multi-agent systems · continual/lifelong learning · agent evaluation · provenance · rollback/recovery · adaptive routing · Human–AI research collaboration.

**Fast review path:** [Start Here for Reviewers](START_HERE_FOR_REVIEWERS.md) → [Current Truth Index](CURRENT_TRUTH_INDEX.md) → [Longitudinal S40/WEB study](LONGITUDINAL_S40_WEB_AND_AFFECT_STUDY_20261004.md) → [ZeroLab V2 results](ZERO_LAB_V2_FIRST_RESULTS_20261002.md).

> **Claim boundary:** SSI does not claim completed S40/WEB training, biological emotion, consciousness, physical robotics validation, safety certification or independent external replication where those milestones have not been evidenced.


### Universal Lab evidence / notary target

Universal Lab is intended to inherit SSI's stricter evidence-hardening path: append-only hash-linked records, digital signatures, executor/verifier separation, and an independent signing/notary authority **when external attestation is claimed**. The outage path is preregistered as local commit -> pending external attestation -> bounded queue -> DEGRADED_SAFE_MODE at the buffer limit. The design also carries forward mutation/deletion/forged-PASS tests, chain-specific rejection reasons and a negative control.

The **2026-10-09 P2B operator report now records a native signed session prefix verified through record 4,603**, with matched Research Memory anchors. This bounded result does not establish independent external attestation; the broader contract remains the reference for the remaining work. See the [latest progress report](RESULTS/UNIVERSAL_LAB_RESEARCH_MEMORY_PROGRESS_20261009.md) and [Universal Lab Evidence, Digital Signature and Independent Notary/Attestation Contract](UNIVERSAL_LAB_EVIDENCE_NOTARY_AND_ATTESTATION_CONTRACT_20261008.md).


## Universal Lab / Research Memory — preserved progress, 2026-10-09

**Caption Chat R4 is installed on the MSI development host, and the operator has confirmed working translation.** The caption update provides the latest bilingual utterance over the camera and a scrollable 40-utterance history with timestamps and revision-based corrections.

**Research Memory has advanced through P1 audit, P2B native signing backfill and P3A installation.** Operator reports record three projects with verified local chains; a native session signed and verified through all **4,603** records at the fixed target; **335** matched anchors covering **861** meeting-memory observations; and a P3A qualification-reader check across **7 actors / 16 native artifact files**.

**The next integration gate is still closed:** the inspected memory has **0 skill trials**, the artifacts have **0 named-feature contracts**, and **0 native cases have been ranked**. P3A reads local native eligibility during its check; the trial-evidence verifier and production Router binding remain unconnected. The signature result supports bounded provenance claims, with **independent attestation still false**.

Caption Chat R4 is a targeted update, distinct from the broader R4 development package recorded as uninstalled on 2026-10-07. These results do not establish completion of all R5 meeting integrations or a partner benchmark.

- **[Latest Universal Lab / Research Memory progress and next gates](RESULTS/UNIVERSAL_LAB_RESEARCH_MEMORY_PROGRESS_20261009.md)**
- [Machine-readable public summary](RESULTS/UNIVERSAL_LAB_RESEARCH_MEMORY_PUBLIC_SUMMARY_20261009.json)
- [Earlier partner meeting baseline and plan — 2026-10-07](UNIVERSAL_LAB_MEETING_START_HERE_20261007.md)
- [Earlier installed state and R5 integration scope — 2026-10-07](SYSTEM/SSI_UNIVERSAL_LAB_STATUS_20261007.md)

SSI V5 is an independently developed R&D project focused on persistent competence, continual learning, cross-agent consolidation, adaptive routing, rollback/recovery and cross-domain transfer.

> **Repository status:** public R&D, evidence and external-validation hub for SSI V5. This repository publishes architecture, research protocols, training checkpoints, failures, benchmark plans, evidence and claim boundaries. Proprietary implementation, credentials, private runtime state and reconstructive internals remain private.

**Early CZARA contribution:** the SSI author credits **Amnezja / [@amnezja3](https://github.com/amnezja3) (Mikael)** as an early CZARA co-creator / seed contributor who introduced the initial direction and made the first CZARA connection step; Paweł Jankiewicz subsequently developed and expanded CZARA into its current SSI V5 role. See [attribution record](EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md).

## Two current research pillars — 2026-10-04

SSI V5 is a continuing research programme whose public history predates the current funding application. The lineage from Micronetworks through Router V10, Router S10, S1-S10 and the current S11-S40 path is summarized in [RESEARCH_PROGRAM_LINEAGE_AND_POST_S40_PLAN_20261004.md](RESEARCH_PROGRAM_LINEAGE_AND_POST_S40_PLAN_20261004.md).

SSI V5 now has two explicit, connected current research fronts:

1. **Evidence / safe knowledge promotion:** [AKTUALNA_NAPRAWA.md](AKTUALNA_NAPRAWA.md) studies whether a persistent agent can be prevented from turning an unverified, unreproduced or incorrectly reviewed outcome into reusable knowledge.
2. **Longitudinal persistent-agent change:** [LONGITUDINAL_S40_WEB_AND_AFFECT_STUDY_20261004.md](LONGITUDINAL_S40_WEB_AND_AFFECT_STUDY_20261004.md) preregisters the comparison of BODY_FROZEN and ISKRA1..6 from preserved baselines through S40 and then through the same declared WEB training programme.

The longitudinal study is designed to compare not only final PASS counts, but **how each actor learns**: REUSE / ADAPT / FULL_FLOW, new-skill creation, qualification transitions, regressions, rollback/recovery, memory/lifecycle changes, cost and unseen transfer. It also preserves pre/post measurements of the project's informal "feelings" variables as **affect-like state proxies**. WEB work will additionally produce frozen rendered artifacts, enabling comparison of layout structure, spacing, density, typography hierarchy, palette/contrast, responsive behavior and repeatable actor-specific visual signatures. These are operational/self-report measurements only; they are not claims of biological emotion, sentience or consciousness.

Primary sequence:

~~~text
EARLY ISKRA BASELINE
-> CORE TRAINING TO S40
-> FROZEN S40 SNAPSHOT
-> BODY_FROZEN vs ISKRA1..6 UNDER THE SAME WEB CURRICULUM
-> FROZEN POST-WEB SNAPSHOTS
-> SKILL / MEMORY / RECOVERY / AFFECT-LIKE STATE DELTAS
-> OPTIONAL LATER CROSS-AGENT CONSOLIDATION STUDY
~~~

S40 completion and WEB results are not claimed yet; this is a preregistered future measurement layer.

## Start here

| Purpose | Document |
|---|---|
| **Active evidence / repair** | **[AKTUALNA_NAPRAWA.md](AKTUALNA_NAPRAWA.md)** |
| **SSI research lineage + post-S40 plan** | **[RESEARCH_PROGRAM_LINEAGE_AND_POST_S40_PLAN_20261004.md](RESEARCH_PROGRAM_LINEAGE_AND_POST_S40_PLAN_20261004.md)** |
| **S40 → WEB longitudinal agent study** | **[LONGITUDINAL_S40_WEB_AND_AFFECT_STUDY_20261004.md](LONGITUDINAL_S40_WEB_AND_AFFECT_STUDY_20261004.md)** |
| Latest SSI Final continuation — stopped | **[RESULTS/SSI_FINAL_RECOVERY_STOP_20261002.md](RESULTS/SSI_FINAL_RECOVERY_STOP_20261002.md)** |
| Current research roadmap | **[CURRENT_RESEARCH_ROADMAP_20261002.md](CURRENT_RESEARCH_ROADMAP_20261002.md)** |
| CZARA current status and ZeroLab workflow | **[CZARA_CURRENT_STATUS.md](CZARA_CURRENT_STATUS.md)** |
| CZARA first training cycle — final result | **[CZARA_FIRST_TRAINING_CYCLE_RESULTS_20261001.md](CZARA_FIRST_TRAINING_CYCLE_RESULTS_20261001.md)** |
| CZARA sanitized run-level evidence | **[evidence/CZARA_FIRST_TRAINING_20261001/README.md](evidence/CZARA_FIRST_TRAINING_20261001/README.md)** |
| ZeroLab V2 — first runtime results | **[ZERO_LAB_V2_FIRST_RESULTS_20261002.md](ZERO_LAB_V2_FIRST_RESULTS_20261002.md)** |
| ZeroLab public evidence | **[evidence/ZERO_LAB_V2_20261002/README.md](evidence/ZERO_LAB_V2_20261002/README.md)** |
| Historical ZeroLab design | [CZARA_ZERO_LAB_LAB_ARCHITECT_MODULE_20261001.md](CZARA_ZERO_LAB_LAB_ARCHITECT_MODULE_20261001.md) |
| Historical CZARA S120 checkpoint | **[RESULTS/CZARA_RND_1_0_0_TRAINING_CHECKPOINT_S120_20260930.md](RESULTS/CZARA_RND_1_0_0_TRAINING_CHECKPOINT_S120_20260930.md)** |
| S20-S26 operator stop / LAB repair | **[RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_AND_LAB_REPAIR_20260930.md](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_AND_LAB_REPAIR_20260930.md)** |
| Dynamic Mission V6 — installation and post-CZARA gate | **[DYNAMIC_MISSION_ORCHESTRATOR_V6_INSTALL_AND_GATE_20260930.md](DYNAMIC_MISSION_ORCHESTRATOR_V6_INSTALL_AND_GATE_20260930.md)** |
| Supplied S20 runtime log | **[S20 live training excerpt](evidence/S20_20260929/S20_LIVE_EXCERPT_RUN_20260929T212837Z_92e516e1.log)** |
| First technical review | **[REVIEWER_INDEX.md](REVIEWER_INDEX.md)** |
| Current verified claims | **[CURRENT_TRUTH_INDEX.md](CURRENT_TRUTH_INDEX.md)** |
| Historical S19 incident / pre-S20 snapshot | **[RESULTS/SSI_V5_S19_OBSERVABILITY_INCIDENT_AND_PRE_S20_STATUS_20260929.md](RESULTS/SSI_V5_S19_OBSERVABILITY_INCIDENT_AND_PRE_S20_STATUS_20260929.md)** |
| Pre-S20 hardening preregistration | **[SYSTEM/SSI_V5_PRE_S20_OBSERVABILITY_AND_EVIDENCE_HARDENING_PREREGISTRATION_20260929.md](SYSTEM/SSI_V5_PRE_S20_OBSERVABILITY_AND_EVIDENCE_HARDENING_PREREGISTRATION_20260929.md)** |
| External review attribution | **[EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md](EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md)** |
| S13-S18 routing evidence | **[RESULTS/SSI_V5_S13_S18_ROUTING_AND_RECOVERY_UPDATE_20260929.md](RESULTS/SSI_V5_S13_S18_ROUTING_AND_RECOVERY_UPDATE_20260929.md)** |
| Reviewer orientation | **[START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md)** |
| Grant / consortium entry | **[GRANT_AND_CONSORTIUM_ENTRY_20261001.md](GRANT_AND_CONSORTIUM_ENTRY_20261001.md)** |
| Grant / consortium package | **[GRANT_CONSORTIUM/README.md](GRANT_CONSORTIUM/README.md)** |
| Collaboration and external challenges | **[COLLABORATION_AND_PARTNER_ENTRY.md](COLLABORATION_AND_PARTNER_ENTRY.md)** |
| Mexico pre-benchmark R&D protocol | **[MEXICO_PREBENCHMARK_RND_PROTOCOL_20260928.md](MEXICO_PREBENCHMARK_RND_PROTOCOL_20260928.md)** |

## Grant and consortium readiness

A dedicated proposal-building layer is now published for future grant reviewers and consortium partners. It covers proposed SSI contribution, background/foreground IP boundaries, provisional asset-specific TRL planning, candidate work packages/deliverables/milestones, impact/exploitation/dissemination, risk/safety/security/ethics, resources/budget and data/reproducibility.

Start with [GRANT_AND_CONSORTIUM_ENTRY_20261001.md](GRANT_AND_CONSORTIUM_ENTRY_20261001.md). These are planning documents, not a claim of a signed consortium, certified TRL, fixed grant budget or confirmed eligibility for a specific call.

Public CZARA run-level evidence is also checked by the repository's `Evidence Verification` GitHub Actions workflow, which recounts the machine-readable CSV against the published aggregate summary.

## Programme at a glance

**Research maturity path:** internal training -> frozen validation -> blind / held-out benchmarks -> partner-defined external benchmarks -> simulation / digital-twin validation -> controlled physical pilots -> independent multi-partner replication.

The current programme combines core SSI reliability work, CZARA Human-AI research collaboration, Dynamic Mission V6, post-S40 WEB engineering, Mexico robotics/offline-resilience research and a developing external benchmark network. Planned work is kept separate from completed evidence.

## Project at a glance

- **Architecture:** independent DIRECTOR core, BODY_FROZEN and six ISKRA agents with separate runtimes, memory and lifecycle.
- **Research controls:** versioned evidence, provenance, checkpoints, rollback and bounded claims.
- **Capability layers:** Router V10/S10, Micronetworks, BLOCKS Pocket, Pocket Micro, META-BLOCKS, laboratories and domain/world layers.
- **Public terminology:** `BLOCKS` is the public name for SSI's reusable modular competence layer. Current public names include **BLOCKS Pocket, BLOCKS Space, BLOCKS Navigator, BLOCKS Content, META-BLOCKS and WEB BLOCKS**. Legacy private/runtime paths, schema fields and historical filenames containing `lego` remain unchanged for backward compatibility; they are implementation identifiers, not public branding. SSI is not affiliated with the LEGO Group.
- **Demonstrated scope:** software laboratory results for drone, humanoid and cross-domain rescue scenarios.
- **Current boundary:** software evidence is published; physical validation, safety certification and independent external replication are not claimed.

**Current public state:** 2026-10-12 (Director A16 update; earlier measurements retain their original dates)

## Latest SSI Final continuation — infrastructure stop — 2026-10-02

The next operator-provided log records **4 PASS / 3 INCONCLUSIVE / 0 FAIL** across seven closed cases, ending with `STOPPED_INFRASTRUCTURE` in `RUN_DOMAIN_20261002T181736Z_f600e74c`. The last case first reported a LAB output mismatch, then `NO_CANDIDATE_GENERATED` / `INVALID_WORKER_JSON`; the runner preserved INCONCLUSIVE and stopped. The terminal log does not establish the underlying root cause.

Together with the earlier seven-case batch, the two published transcripts contain **14 distinct actor/case outcomes: 9 PASS / 5 INCONCLUSIVE / 0 FAIL**. This is not a whole-stage or whole-queue result, and it does not alter the separate ZeroLab pilot or CZARA curriculum totals.

- [Latest stop, all seven cases and evidence](RESULTS/SSI_FINAL_RECOVERY_STOP_20261002.md)

## ZeroLab V2 and first post-repair SSI batch — 2026-10-02

Operator-provided terminal evidence reports **9/9 ZeroLab services READY**, followed by an **8/8 PASS local-data pilot** (`training_pass=false`, `models_called=0`). A separate SSI Final recovery batch completed **7 cases: 5 PASS, 2 INCONCLUSIVE, 0 FAIL**. Both unresolved cases retain `LAB_OUTPUT_MISMATCH`; one passing case succeeded after a candidate revision.

The resumed Final batch is a selected S20-S26 recovery measurement after ZeroLab installation, not proof that those seven cases ran through ZeroLab. It does not establish full-stage acceptance or global per-case consolidation. The public export contains terminal evidence and reported receipt hashes; original pilot receipts and the signed Final run bundle have not been independently reverified for this publication.

- [CZARA current status: Director_Czary, BODY 1.0 and ZeroLab](CZARA_CURRENT_STATUS.md)
- [ZeroLab V2 results and provenance](ZERO_LAB_V2_FIRST_RESULTS_20261002.md)
- [Architecture, roles and consolidation boundaries](SYSTEM/ZERO_LAB_V2_ARCHITECTURE_AND_AUTHORITY_20261002.md)
- [Public evidence and machine-readable results](evidence/ZERO_LAB_V2_20261002/README.md)

## Preserved operator-stop snapshot — 2026-09-30

The following records the earlier stop. The 2026-10-02 result above documents the subsequent limited live restart; historical grades remain unchanged.

Core training progressed through completed S20-S25 stages and into S26. The operator then **manually stopped the run with Ctrl-C** because the number of `INCONCLUSIVE` outcomes and pending cases was increasing and no longer represented a trustworthy training signal.

Latest preserved diagnostic snapshot:

```text
TOTAL = 1,326
PASS = 848
INCONCLUSIVE = 470
FAIL = 8
S20-S25 verified-subset consolidations = PASS for BODY_FROZEN + DIRECTOR
S26 = interrupted / not claimed complete
```

A targeted diagnostic sample of **18 cases** showed that the apparent `unparseable_json` symptom was an **empty response after `INFLIGHT_LIMIT`**. This finding is limited to the inspected sample and is **not** generalized to every unresolved case.

The diagnosis also identified two additional reliability gaps: required task outputs were not always propagated correctly to the reviewer path, and dedicated R&D execution scenarios remain incomplete for parts of S20-S26.

A repair package (`SSI_LAB_REPAIR_20260930.zip`) was prepared and reported **17/17 offline tests PASS**. At that date, a successful live restart was not yet claimed; the separate 2026-10-02 batch above is the later retest. Historical verdicts remain preserved.

- [S20-S26 operator stop and LAB repair incident](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_AND_LAB_REPAIR_20260930.md)
- [Machine-readable S20-S26 stop/repair summary](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_PUBLIC_SUMMARY_20260930.json)

**Preserved continuation requirement:** a new post-repair provenance boundary was required. The later recovery batch uses a separate plan/run and preserves earlier verdicts; it does not certify completion through S40.


## CZARA first internal training cycle complete — 2026-10-01

`CZARA-RND-1.0.0` completed its first internal training, frozen validation and frozen Champion benchmark cycle.

```text
UNIQUE STAGES = 160
FINAL CHECKPOINT = 160 / 160 PASS
FINAL QUALIFIED SKILLS = 520 / 520

TRAINING
  120 unique stages
  497 attempts
  120 PASS attempts
  377 intermediate INCONCLUSIVE attempts
  0 FAIL
  learning_applied = true

FROZEN VALIDATION
  24 / 24 PASS
  24 / 24 REUSE
  skill coverage = 1.0
  learning_applied = false

FROZEN CHAMPION BENCHMARK
  16 / 16 PASS
  16 / 16 REUSE
  skill coverage = 1.0
  learning_applied = false

AUTHORITY ERRORS = 0
```

The **377 INCONCLUSIVE records are preserved intermediate training/retry attempts**, not unresolved final curriculum stages. The final checkpoint records all 160 unique stages as PASS.

This is internal SSI evidence for the planned Poland-Mexico research workflow. It is **not** an independent Mexico benchmark, physical robotics validation, safety certification or external replication.

- [CZARA first training cycle — final results](CZARA_FIRST_TRAINING_CYCLE_RESULTS_20261001.md)
- [Machine-readable public summary](evidence/CZARA_FIRST_TRAINING_CYCLE_PUBLIC_SUMMARY_20261001.json)
- [Sanitized run-level evidence](evidence/CZARA_FIRST_TRAINING_20261001/README.md)
- [Historical S120 checkpoint — preserved](RESULTS/CZARA_RND_1_0_0_TRAINING_CHECKPOINT_S120_20260930.md)
- [ZeroLab V2 — first runtime results](ZERO_LAB_V2_FIRST_RESULTS_20261002.md)

## Historical pre-S20 snapshot — S19 incident and consolidation hardening

The pre-S20 snapshot below includes completed software/runtime evidence for **S13 through S19**.

| Stage | Execution | PASS | INCONCLUSIVE | FAIL | Consolidation |
|---|---:|---:|---:|---:|---|
| S13 | 210/210 | 203 | 6 | 1 | COMMITTED |
| S14 | 210/210 | 208 | 1 | 1 | COMMITTED |
| S15 | 210/210 | 175 | 31 | 4 | COMMITTED |
| S16 | 210/210 | 209 | 1 | 0 | COMMITTED |
| S17 | 210/210 | 206 | 2 | 2 | COMMITTED |
| S18 | 210/210 | 196 | 12 | 2 | COMMITTED |
| **S19** | **210/210** | **182** | **24** | **4** | **NOT YET COMMITTED** |

S19 full execution was completed in `RUN_20260929T005550Z_a356e86c` with `execution_complete=true`. Its verified subset contains **182 cases**; 28 FAIL/INCONCLUSIVE cases remain preserved and excluded from the verified consolidation subset.

The post-stage consolidation transaction `CC_09eae1705906e8acaa653eb28123fc84` then stopped on the runtime SNAPSHOT path. Current root-cause classification is **OBSERVABILITY-INDUCED INTEGRATION REGRESSION**: the regression appeared while integrating new routing observability intended to distinguish actual Champion execution, exact reuse and Full Flow escalation from catalog labels or ambiguous log markers.

This is intentionally separated from the S19 capability result:

```text
S19 CASE EXECUTION = COMPLETE
S19 VERDICTS = 182 PASS / 24 INCONCLUSIVE / 4 FAIL
S19 CONSOLIDATION = NOT YET CLAIMED COMMITTED
S20 START = NOT YET CLAIMED
```

The new pre-S20 hardening is being preregistered **before** continuation. It includes:

- passive routing telemetry with an observability non-interference A/B gate;
- explicit Champion available/selected/executed/result evidence;
- explicit exact-reuse / Full-Flow / provider-fallback evidence;
- per-model/provider and cross-actor failure correlation;
- a 7/7 transaction-bound consolidation SNAPSHOT gate;
- chain-specific evidence attacks plus a negative control;
- explicit external-notary outage and buffer-limit behavior.

External reviewer **Hamid Ahmadian** is credited for feedback that materially shaped the evidence-hardening requirements, including executor/verifier separation, append-only signed hash chains, mutation/deletion/forged-PASS tests, previous-hash/missing-sequence causal controls, the negative control, and the notary buffer-limit question. Attribution is feedback provenance, not an endorsement or independent audit.

Current records:

- [S19 observability incident and pre-S20 status](RESULTS/SSI_V5_S19_OBSERVABILITY_INCIDENT_AND_PRE_S20_STATUS_20260929.md)
- [Pre-S20 hardening preregistration](SYSTEM/SSI_V5_PRE_S20_OBSERVABILITY_AND_EVIDENCE_HARDENING_PREREGISTRATION_20260929.md)
- [External review feedback and attribution](EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md)
- [Machine-readable pre-S20 hardening summary](RESULTS/SSI_V5_PRE_S20_HARDENING_PUBLIC_SUMMARY_20260929.json)
- [S13-S18 routing and recovery report](RESULTS/SSI_V5_S13_S18_ROUTING_AND_RECOVERY_UPDATE_20260929.md)

The intended continuation remains:

```text
pre-S20 hardening gates
-> S19 consolidation COMMITTED
-> S20 ... S40
-> S40 consolidation COMMITTED
-> WEB01 ... WEB24
-> final routing / Champion / Full-Flow / model / cross-actor diagnostic report
```

## Current verified state

```text
V4 S1-S10 = COMPLETE / PASS
7 BODY final state = 7/7 PASS
BODY_FROZEN promoted reload = 144/144

POST-S10 DRONE = 6/6 software scenarios PASS
POST-S10 HUMANOID = 15/15 software scenarios PASS

DUAL MOTHER CROSS LAB V1
DRONE MOTHER = 12/12 paired scenario families PASS
RESCUE ROBOT MOTHER = 12/12 paired scenario families PASS
60 deterministic repeats per scenario family
720 paired missions / 1,440 domain result rows

CROSS CONSULTATION = 720 measured rounds
CROSS CONSOLIDATION = 360 measured executions
ROLLBACK = 360 measured executions

PUBLIC RESEARCH PORTAL = PUBLISHED
PHYSICAL VALIDATION = not claimed
INDEPENDENT EXTERNAL REPLICATION = not claimed
```

Software-lab timing summaries:

```text
mean cross consultation = 2.4896 ms
mean rollback = 0.1170 ms
mean cross consolidation = 0.0369 ms
mean total software flow = 5.2559 ms
```

These are software execution timings, not physical drone/robot response times.

## Published training front and active internal continuation

The latest private S11 training run `RUN_20260925T163311Z_820718d5` completed all **210/210 cases** under the revised training-continuation policy: **196 PASS, 13 INCONCLUSIVE and 1 FAIL**. The stage remains **INCONCLUSIVE**, but `execution_complete=true`; FAIL/INCONCLUSIVE cases no longer stop the whole training traversal.

Only the **196 verified PASS** cases were exported for downstream consolidation. The remaining **14 cases** stayed excluded as unresolved/retry material. Cross-consolidation transaction `CC_82dd0b3af825cd8543dcd59835023a5a` subsequently completed **PASS** for both BODY_FROZEN and the independent DIRECTOR view, with `identity_transfer=false`, `BODY_FROZEN.identity_changed=false`, `DIRECTOR.body_core_imported=false` and `weights_retrained=false`.

A separate private **WEB BLOCKS** training extension is now installed and reports `READY`: **126 BLOCKS items, 15 templates, 24 WEB stages, 192 cases, 7 actors**, with `data_policy=SYNTHETIC_ONLY`. This records installation/readiness only; successful WEB01-WEB24 live training is not yet claimed.

- [2026-09-26 S11 consolidation + WEB BLOCKS update](RESULTS/SSI_V5_S11_CONSOLIDATION_AND_WEB_LEGO_UPDATE_20260926.md)
- [S12 live training + committed consolidation](RESULTS/SSI_V5_S12_LIVE_TRAINING_AND_CONSOLIDATION_20260926.md)
- [Current machine-readable training progress](RESULTS/SSI_V5_CURRENT_TRAINING_PROGRESS_20260926.json)
- [Preserved S11-named machine-readable update](RESULTS/SSI_V5_S11_CONSOLIDATION_AND_WEB_LEGO_PUBLIC_SUMMARY_20260926.json)
- [Preserved previous S11 report: 197 PASS / 12 INCONCLUSIVE / 1 FAIL](RESULTS/SSI_V5_S11_FULL_RESULTS_20260923.md)

The cross-run prerequisite repair is now backed by a **live post-fix S12 run**. Training run `RUN_20260925T223720Z_6e1b1fc8` executed **210/210 cases**: **203 PASS, 7 INCONCLUSIVE, 0 FAIL**, with `execution_complete=true`. Its verified subset contained 203 cases, while 7 remained excluded. Consolidation transaction `CC_db09484eefd9db783742336b69296eb5` is **COMMITTED** and explicitly references this S12 training run.

### Next SSI training stage after S40

The WEB training track is now configured as the **next automatic SSI training phase after S40**. The installed post-S40 gate is designed to start WEB01-WEB24 only after the core training reaches S40 with full execution and a committed consolidation.

```text
S11 -> S12 -> ... -> S40
                    |
                    v
          execution_complete = true
          S40 consolidation = COMMITTED
          WEB BLOCKS = READY
                    |
                    v
          WEB01 -> WEB02 -> ... -> WEB24
```

This is a configured training-roadmap/automation claim. The actual live transition from S40 to WEB01 has not yet occurred and is therefore not claimed as observed evidence.


## Planned Mexico robotics training and external benchmark track — 2026-09-26

A new **planned** research track has been documented for staged robotics training and later external benchmark collaboration with a research professor/team in Mexico.

The design introduces **CZARA** as a dedicated multilingual research-context layer:

```text
MEXICO RESEARCH TEAM
-> CZARA (Spanish / English -> original transcript + Polish translation)
-> DIRECTOR
-> BODY_FROZEN
-> LAB
-> EVIDENCE
```

CZARA is intentionally separated from DIRECTOR and BODY_FROZEN. It captures external research context, dissatisfaction, corrections and proposed changes; it does not directly control robots or replace the normal SSI training loop.

The planned robotics curriculum contains **48 stages**:

```text
38 TRAINING
  12 DRONES
  12 HUMANOIDS
   6 MOTHER / CROSS-DOMAIN
   8 OFFLINE DIRECTOR / BLOCKS OFFLINE

4 VALIDATION
6 FINAL CAPSTONE
```

The intended policy is **Champion-first**: SSI should reuse validated competence before escalating to Challenger/deeper collective reasoning. Final validation/capstone runs are intended to freeze pre-result competence so the hidden case is not silently learned during scoring.

Planned end-of-training scenarios include no-network underground mapping with `SPACE_BLOCKS`, multi-robot map merge, optical/acoustic offline relay, lost-unit recovery, dynamic map revision and an unseen partner-defined scenario. These are **planned benchmark designs**, not completed physical validations.

- [CZARA — Mexico Research Context, Translation and Learning Layer](SYSTEM/CZARA_MEXICO_RESEARCH_LAYER_20260926.md)
- [Mexico Robotics Training and External Benchmark Plan](MEXICO_ROBOTICS_TRAINING_AND_BENCHMARK_PLAN_20260926.md)
- [Pre-Benchmark R&D Protocol: Core, WEB and Mexico paths](MEXICO_PREBENCHMARK_RND_PROTOCOL_20260928.md)

## ŚWIAT PIŁKI — HIPNOZA

The private SSI V5 installation also contains the **ŚWIAT PIŁKI — HIPNOZA** world/interface layer.

```text
implementation = PRESENT
operator-observed runtime/interface behavior = WORKING
complete end-to-end data connection = NOT YET FULLY VALIDATED
evidence-backed domain validation = PENDING
```

See the [current Football World status](RESULTS/FOOTBALL_WORLD_IMPLEMENTATION_BOUNDARY_20260922.md). It is recorded as implemented, but not yet promoted to `VALIDATED / EVIDENCE-BACKED`. The intended closure sequence remains: micronetworks/routing → full data flow → BODY validation → cross-BODY consolidation into BODY_FROZEN → corresponding validated consolidation into the independent DIRECTOR view.

BODY_FROZEN and DIRECTOR remain separate cores with separate runtime, memory and lifecycle.

## Architecture at a glance

```text
DIRECTOR
+ BODY_FROZEN
+ ISKRA1..ISKRA6
+ HERMES
+ CONTINUUM
+ ROUTER V10
+ ROUTER S10
+ TECHNOLOGY RADAR
+ MICRONETWORKS / BLOCKS / POCKET / POCKET MICRO / META-BLOCKS
+ COST/QUALITY MODEL CASCADE
+ CONTRACT BINDING
+ WORLD / DOMAIN LAYERS
+ ŚWIAT PIŁKI — HIPNOZA
+ LOCAL ROOT CONTROL
+ PUBLIC OBSERVER INTERFACE
+ EVIDENCE / CHECKPOINT / PROVENANCE
```

## Read this repository in this order

1. [CURRENT_RESEARCH_ROADMAP_20261002.md](CURRENT_RESEARCH_ROADMAP_20261002.md)
2. [REVIEWER_INDEX.md](REVIEWER_INDEX.md)
3. [Latest S13-S18 routing and recovery evidence](RESULTS/SSI_V5_S13_S18_ROUTING_AND_RECOVERY_UPDATE_20260929.md)
4. [CURRENT_TRUTH_INDEX.md](CURRENT_TRUTH_INDEX.md)
5. [BLOCKS Pocket, META-BLOCKS, laboratories and Football World](SYSTEM/LEGO_POCKET_META_LEGO_AND_DIRECTOR_LABS_20260922.md)
6. [START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md)
7. [RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md)
8. [SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md](SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md)
9. [Mexico pre-benchmark R&D protocol](MEXICO_PREBENCHMARK_RND_PROTOCOL_20260928.md)
10. [COLLABORATION_AND_PARTNER_ENTRY.md](COLLABORATION_AND_PARTNER_ENTRY.md)

## Current milestone lineage

```text
BODY / ISKRA foundations
-> 7-BODY readiness
-> V4 S1-S10
-> promotion / regression
-> post-S10 drone + humanoid software labs
-> Dual Mother cross-domain consultation / rollback / consolidation
-> free-only / full-flow baseline
-> paid cost/quality model cascade
-> Technology Radar
-> Contract Binding
-> Pocket Micro
-> META-BLOCKS
-> ŚWIAT PIŁKI — HIPNOZA implemented / operator-observed
-> S11 smoke PASS
-> preserved earlier S11 stops and repairs
-> permanent R&D / controlled-experiment LAB and independent-case continuation
-> preserved 2026-09-23 S11 traversal: 197 PASS / 12 INCONCLUSIVE / 1 FAIL
-> revised training continuation semantics
-> latest S11 traversal: 210/210 executed; 196 PASS / 13 INCONCLUSIVE / 1 FAIL
-> verified-subset export: 196 admitted / 14 excluded
-> S11 cross consolidation PASS for BODY_FROZEN + independent DIRECTOR
-> cross-run prerequisite repair validated by live S12 execution
-> S12 traversal: 210/210 executed; 203 PASS / 7 INCONCLUSIVE / 0 FAIL
-> S12 verified subset: 203 admitted / 7 excluded
-> S12 consolidation COMMITTED: CC_db09484eefd9db783742336b69296eb5
-> WEB BLOCKS extension installed READY: 126 BLOCKS items / 15 templates / 24 stages / 192 cases / SYNTHETIC_ONLY
-> S13-S18 completed with committed consolidations
-> S19 fully executed: 182 PASS / 24 INCONCLUSIVE / 4 FAIL
-> S19 post-stage consolidation blocked during routing-observability integration
-> pre-S20 observability/evidence hardening preregistered
-> pre-S20 hardening passed and S19 consolidation subsequently reported committed
-> S20-S25 completed with verified-subset consolidations reported PASS
-> S26 entered, then manually stopped by operator after abnormal INCONCLUSIVE/pending growth
-> LAB/reviewer diagnosis completed; 18 sampled parse failures mapped to empty responses after INFLIGHT_LIMIT
-> initial repair package: 17/17 offline tests PASS; live restart unclaimed at that earlier date
-> ZeroLab V2 runtime readiness: 9/9; local pilot 8/8 PASS, not training qualification
-> IPC R2 resume: 19/19 offline tests; selected Final batch 5 PASS / 2 INCONCLUSIVE / 0 FAIL
-> configured next training phase after S40: automatic gated transition to WEB01-WEB24
```

Older dated files remain preserved as historical evidence. They are not the recommended starting point unless a reviewer is auditing provenance.

## Public / private boundary

```text
PUBLIC
= protocols
+ sanitized evidence
+ results
+ failures / repairs / retests
+ timings
+ hashes / provenance
+ claim boundaries
+ architecture at safe level
+ published observer portal

PRIVATE
= proprietary source code
+ Router V10 / S10 implementation internals
+ reconstructive Micronetwork details
+ private Hermes / BODY state
+ ROOT internals
+ prompts / private configuration
+ credentials / endpoints
```

## Claim boundary

The public evidence supports bounded software-laboratory claims about persistent multi-agent execution, versioned competence, consolidation, rollback/recovery and cross-domain experiments.

It does **not** establish:

- all-PASS S11 acceptance; the latest complete traversal contains 14 unresolved cases;
- completed S20-S40 training; S19 consolidation is preserved as having subsequently passed before S20 continuation;
- successful WEB01-WEB24 live training;
- physical drone validation;
- physical rescue-robot validation;
- physical humanoid validation;
- safety certification;
- independent external replication;
- production readiness;
- universal superiority;
- AGI or consciousness.

## Collaboration

SSI V5 is open to controlled research, validation, challenge-design and grant/consortium collaboration.

Preferred model:

```text
EXTERNAL PARTNER DEFINES UNSEEN PROBLEM
-> ACCEPTANCE CRITERIA FROZEN
-> SSI RUN
-> PASS / FAIL / INCONCLUSIVE PRESERVED
-> EVIDENCE RETAINED
-> OPTIONAL CONSOLIDATION
-> TARGET-SPECIFIC RE-VALIDATION
```

See [COLLABORATION_AND_PARTNER_ENTRY.md](COLLABORATION_AND_PARTNER_ENTRY.md).
