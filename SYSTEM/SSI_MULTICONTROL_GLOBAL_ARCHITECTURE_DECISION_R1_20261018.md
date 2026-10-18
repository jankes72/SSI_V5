# SSI LEGO MultiControl — GLOBAL_SSI architecture decision R1

**Decision ID:** `SSI_MULTICONTROL_GLOBAL_ARCHITECTURE_DECISION_R1`  
**Operator decision:** 2026-10-18  
**Applies to:** all SSI V5 domains, not only SSI MultiQuant.  
**Status:** `PLANNED / GLOBAL_SSI / SHADOW_ONLY`. **No production component, SCC runtime binding, Champion promotion or cross-VPS deployment is claimed by this document.**  
**Public document:** architectural decision and acceptance requirements, not source code, an installation script, a production release or independent performance evidence.

## 1. Decyzja nadrzędna

**LEGO MultiControl będzie współdzieloną zdolnością całego SSI V5.** Jest neutralną domenowo warstwą kontroli kompatybilności, kontraktów, jakości, wersji, zależności, pochodzenia zasobów, dowodów, warunków kwalifikacji i możliwych punktów przywracania stanu.

Nie należy do samego MultiQuant. Każdy system korzysta z tej samej warstwy kontrolnej przez jawny adapter, zachowując własny model danych, identyfikatory, rejestry, historię i uprawnienia. MultiControl **proponuje/raportuje**, ale nie wykonuje, nie zmienia polityki Routera, nie potwierdza niezależnie semantycznego sukcesu i nie awansuje kandydatów.

## 2. Historyczne granice i źródła

- **Mikrosieci SSI są starsze niż mechanizmy LEGO.** LEGO Decomposer, LEGO Pocket i META LEGO powstały później jako odrębne mechanizmy pozyskiwania, kwalifikacji i ponownego wykorzystania klocków. LEGO nie „tworzy” historycznych mikrosieci.
- Existing LEGO Decomposer R9.109: isolated synthetic fixture **PASS (5 blocks: 3 MODULE, 2 ATOM)**; the newer adapter's expected call signature was incompatible. **Do not rewrite a working native decomposer to hide an adapter error.**
- R9.111 historical read-only comparison: **`NOT_READY`**, 11/11 JSON files readable, Pocket SQLite read in immutable mode, 37 candidate shared values. **Shared values do not establish a verified PM_ ↔ s10_ relationship or end-to-end runtime connection.**
- The previous private R9.112 LEGO Composer / Multi-LEGO control prototype is **SHADOW_ONLY**. Test-count assertions (including reported 63/63 offline) pertain only to its bounded control logic and do **not** qualify native SCC or production integration.
- The private R9.113 handoff introduced a MultiQuant-oriented integration narrative. **This decision supersedes only the ownership/scope of MultiControl**: it is now SSI-wide, while MultiQuant remains one client. Keep the earlier negative findings, tests, R9.111 `NOT_READY` and evidence boundaries unchanged.

## 3. Granice odpowiedzialności (nieprzekraczalne)

| Existing owner | Remains authoritative for | MultiControl contribution |
| --- | --- | --- |
| **SSI DIRECTOR** | Goals, approvals, delegation and mission lifecycle | May request checks, review impact reports and approve separately authorized changes |
| **Native SCC** | Existing mission grammar and versioned goals/intents/transitions | Typed read-only views and compatibility annotations; **no second language** |
| **Router V10** | Capability classification, routing and operational selection | Advisory availability/compatibility signals; no direct routing-table mutation |
| **Micronetwork registry** | Micronetwork candidates, lifecycle, its own Champion/Challenger/Hold decisions | Verify references and evidence; never write/promote |
| **LEGO Pocket registry** | Pocket family/bundle/qualification and Pocket Champion decisions | Inspect contracts and provenance; no registry writes |
| **META LEGO** | Meta/index data and canonical identifier lineage | Detect missing/ambiguous links without inventing links |
| **MultiQuant model qualification** | Model evaluation and its future qualification/promotion rules | Advisory model compatibility, quantization/distillation composition and regressions; no automatic model Champion |
| **Evidence/Notary** | Hash/signature provenance and attestation as independently specified | Request/verifies *references* to evidence; does not forge signatures or infer semantic success |
| **Robert, CODEX, laboratory/robotics runtimes** | Authorized work through their own execution and safety policies | Domain-specific compatibility preflight; no direct execution commands |

**Czara stays parallel SHADOW**, not the Director's decision authority. MultiControl can be optional: ordinary mission execution must not require a live MultiControl response; any future enforcement gate must be independently approved, versioned and tested for safe outage behaviour.

## 4. Dziesięć rodzin adapterów domenowych (proponowane, nie wdrożone)

| Domain | Proposed check |
| --- | --- |
| SSI MultiQuant | Teacher/student model lineage, tokenizer/license compatibility, tensor/adapter constraints, training/quantization quality evidence |
| SSI Micronetworks | `s10_`/`cand_` references, feature contracts, benchmark provenance and lifecycle |
| LEGO Decomposer | Source provenance, output block manifests and adapter-call compatibility |
| LEGO Pocket | Explicit package/family/qualification references and registry read-only snapshots |
| META LEGO | Link integrity, index version and canonical ID provenance |
| SSI CODEX | Software composites, declared APIs/typed ports, tests and dependency graph |
| SSI ROBERT | Authorized mission requirements versus SERVER_NATIVE/LOCAL_EXTENSION/HYBRID capabilities |
| Universal Lab / Zero Lab | Experimental protocols, held-out evaluation, repeatability, checkpoint and NOTARY references |
| Robotics / drones | Driver/firmware/hardware compatibility and simulation-vs-real-evidence distinction; safety approvals stay with domain authority |
| SSI Router V10 | Optional read-only hints for verified capability availability/constraints; no automatic routing change |

Adapter APIs are **proposals only**; exact signatures must be derived from native implementations before code is considered compatible.

## 5. Rozszerzenie SCC i historia identyfikatorów

**Preserve native:** `ssi.mission.goal.r1`, `ssi.mission.intent.r1`, `ssi.transition.champion-registry.r1`, and the existing `SSI_MISJA 1` syntax and current A27/A34/R17 private implementation/semantics when independently verified. **Do not introduce an alternative SCC parser, second promotion engine or previously unknown executable SCC opcodes.**

All separate identifier families remain distinct: `s10_`/`cand_` (micronetwork/candidate), `SKILL_`, `mission_`, `ISKRA1..6`, `PM_` (Pocket package), `F_` (Pocket family), `Q_` (Pocket qualification), `ML_`/`MLI_` (META), `LR_` (indexed canonical ID). Proposed model-candidate identities must be source-verified and typed, not inferred from a status string such as `CHAMPION`.

A proposed cross-system link needs **two explicit source identifiers and an independently checkable origin/link record**. The same text or hash occurring in multiple registries is **not** automatic entity equality. Domain-qualified kind, canonical source, version, content SHA and type-specific registry namespace must travel together in any future interop contract.

**Only proposed common control response (NOT native SCC grammar):** reference to inspected resource, adapter/domain name, immutable input snapshot or hash, validated typed ports/contracts, known provenance edges, warnings/gaps, required evidence, proposed corrective action, rollback capability reference, verdict (`PROPOSAL_ONLY`/`BLOCKED`/`INCONCLUSIVE`) and **`authority=NONE`, `execution_permitted=false`, `promotion_permitted=false`, `production_write=false`**. Any executor action requires separate existing authorization and registry API calls; MultiControl output alone confers none.

For model operations, preserve the original 12 MultiQuant action identifiers (from `DISCOVER_MODEL` to `REGISTER_RESULT`) and the explicitly inert `ssi.multiquant.scc.observation.r1` interface. **A Composite or LEGO structure is not a 13th registered SCC action.**

## 6. Lokalizacja i dostępność

- Canonical coordination/API ownership may reside logically alongside **SSI DIRECTOR VPS**, but CPU-heavy analysis, model weights, historical full training datasets and archives are not automatically moved to Director.
- **SSI ROBERT**, **SSI CODEX**, **SSI MODELS**, MSI, NODE-01 and Lenovo should use bounded, authenticated, versioned adapters according to existing network/permission contracts. No new endpoints, public access or implicit credential sharing.
- MSI/NODE-01/local backups keep their known historic storage roles; the VPS layer retains only required operational metadata/cache. Outage handling must not prevent unrelated server-native missions.
- Shadow inspection is read-only with constrained scan limits, process isolation and explicit exposure policy. Cross-domain data minimisation is mandatory, especially for clients and commercial twins.

## 7. Four development phases and acceptance gates

1. **CORE (shadow):** schema-neutral, read-only validation of typed identities, versions, ports, compatibility, evidence refs, cycle/dependency graph, rollback metadata and `UNKNOWN`/missing proofs. Unit tests should include cross-domain identity collisions and negative evidence.
2. **DOMAIN ADAPTERS:** bind each real domain's read-only API and test against immutable fixture/snapshot copies. Restore native Decomposer compatibility **in the adapter**; do not adjust existing file/repository formats just to satisfy a new control interface.
3. **SCC NATIVE CONFORMANCE:** inspect actual A27/A34/R17 parser, registry, feature/port contracts and actor permissions on MSI, map any proposed fields to already existing constructs; unsupported constructs remain external inert annotations.
4. **SHADOW → VALIDATE → AUTHORIZED ROLLOUT:** compare controlled recommendations against existing registries and authorized native outputs, verify performance/availability and rollback under faults, then request explicit separate authorization for a selected integration. **No auto-promotion of micronetwork, Pocket or model Champions.**

**Required hard gates before any production change:** native SCC source/grammar audit, explicit source↔Pocket↔META↔micronet relationship verification where claimed, authoritative qualification/promotion engine inspection, identity-preserving API contracts, independent held-out quality evaluation, Notary/evidence policy, rollback tests, security and privacy review, and operator approval. **Absent proof = `NOT_READY`, not `PASS`.**

## 8. MultiQuant relationship and next work

MultiQuant is the **first designated client for experiments**, **not the owner** of MultiControl. MultiQuant's current D1 skill memory, D2 incremental fragment loop, D3 multi-scale fusion, D4 BIG → MICRO and D5 native low-bit student research goals are unchanged. Future model-specific checks are implemented only as an isolated MultiQuant adapter; core must not embed GPU state or GGUF tensor logic.

The 24 GiB RunPod storage/read-only preflight and independent native SCC R9.114 audit remain separate pending inputs. No paid GPU start, training, quantization, live model compression or production promotion is a consequence of this decision.

## English handoff

**Decision:** MultiControl is a **shared, optional, read-only-by-default SSI V5 control capability**, coordinated with Director and consumed via per-domain adapters; it is not a MultiQuant-owned promotion/routing/execution engine. Maintain historical micronetwork-before-LEGO provenance, distinguish all Champion registries, preserve native SCC grammar and existing interfaces, and mark the entire cross-domain integration `PLANNED / GLOBAL_SSI / SHADOW_ONLY` until verified.
