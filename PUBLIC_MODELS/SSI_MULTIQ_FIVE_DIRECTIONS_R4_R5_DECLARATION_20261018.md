# SSI MultiQuant — five research directions, BIG → MICRO and native low-bit student (R1)

**Declaration date:** 2026-10-18 (Europe/Warsaw).  
**Owner:** SSI V5 / Paweł Jankiewicz.  
**Status:** D1–D3 have **offline, non-executing prototypes**; D4 and D5 are **NEW RESEARCH DIRECTIONS / NOT TRAINED / NOT DEPLOYED**.  
**Public boundary:** research scope, sanitized operator outcomes and acceptance gates only. Proprietary SCC syntax internals, source code, model weights, private prompts, datasets, service addresses, secrets and server configuration stay private.

> **Fundamental architecture rule:** MultiQuant does not invent a competing SCC language. Director owns goals and delegations; native SCC owns mission representation and explicit bindings; Router checks capability/authority; Pocket/META LEGO qualify reusable components; MultiQuant prepares model candidates, observations and evidence. A model's generated JSON is not a production routing decision.

## 1. The five directions — what actually exists

| Direction | Research objective | Evidence as of 18 October 2026 | Execution status |
| --- | --- | --- | --- |
| **D1 — Hybrid Skill Memory** | Keep verified, task-specific strengths and approved teaching examples from heterogeneous models in one persistent memory. | Private **R2** Python/SQLite offline prototype; **56/56 local tests PASS**. Contains synthetic teacher comparisons and bounded Polish speech/orthography ambiguity observations. | **Offline prototype.** No real multi-model benchmarking, no trained hybrid weights, no live SCC binding. |
| **D2 — Incremental Fragment Loop** | Quantize selected tensors/layers or specialize one competence at a time; after each stage test, checkpoint, and recover on regressions. | Private SCC/Awareness/fragment-control **R1**: **32/32 local tests PASS**; existing inert SCC–MultiQuant observation adapter: **23/23 local tests PASS**. | **Planning and gate control only**; neither tensorwise conversion nor knowledge-distillation worker is connected. |
| **D3 — MultiScale Fusion** | Combine D1+D2: propose a multi-model expert system, multi-teacher student, compatible same-base adapter merge, or layerwise quantization. | Private **R3** proposal/controller prototype: **64/64 local tests PASS**, with the four R2 bridge tests explicitly enabled. | **Offline proposal only**; no model/adapter merge, trained student or live expert serving. |
| **D4 — BIG → MICRO (NEW)** | Starting from very large teacher models (70B/120B+ as research targets), obtain a much smaller, task-specialized model/system usable on **16 GiB RAM**, leveraging SCC/micronetwork memory and segment-by-segment optimization. | Research declaration and proposed gates only. | **NOT IMPLEMENTED / NO 70B OR 120B CONVERSION CLAIM.** |
| **D5 — Native Low-Bit Student (NEW)** | Create/train a student with **knowledge distillation and quantization-aware training jointly in the training process**, testing and checkpointing competence/block increments. | Research declaration and proposed gates only. | **NOT IMPLEMENTED / NO QAT OR DISTILLATION TRAINING CLAIM.** |

**Clarification:** tests above are deterministic/offline checks of bounded control software. They do not measure actual student quality or demonstrate compression of a 70B/120B model. Review of real source licenses, teacher-output rights, training hardware, datasets, checkpoint/tokenizer compatibility and operational permission remains mandatory.

## 2. D4 — BIG → MICRO under the 16 GiB target

**Goal:** create an effective **small model for selected SSI tasks**, not advertise a 70B model that magically retains all capabilities at 1B or fits unchanged into 16 GiB.

Two explicitly different experiments:

1. **Streaming/segmentwise weight processing:** investigate bounded-memory tensor/shard reads, per-group quantization/calibration, integrity manifests, temporary disk residency and whole-model reconstruction. This can reduce *peak RAM during preprocessing*, subject to formats, tools, disk space and CPU time. It does **not** reduce the number of parameters or guarantee runnable 70B/120B inference on 16 GiB. Ordinary quantizers may still require much more working memory.
2. **Teacher → specialized micro-student:** identify selected SCC/Router/CODEX/Robert competencies, collect license-permitted, independently validated teacher examples, fine-tune/distill a **smaller** trainable student, then export a low-bit inference candidate. SSC/SCC construction memory and verified micronetwork skills may remain **outside** the weights as a retrieval/skill layer, with measured end-to-end performance.

**First measured acceptance gate** (not yet passed): a chosen candidate must load and answer under a **16 GiB RAM envelope** on the intended hardware; report peak resident/cgroup memory including context/KV cache, free disk and swap effects, throughput/latency, verified quality and regression against an unchanged baseline. Any offloading to disk must be disclosed and timed. On a 16 GiB host, real available RAM will be lower because of OS/services. No inference or quality-equivalence guarantee is implied.

**Stop/hold states:** source/licence/teacher rights not verified; tokenizer or architecture mismatch; insufficient RAM/disk/time; quality regression; missing validation of retained safety/routing behavior; missing authorization for expensive compute.

## 3. D5 — native low-bit student: joint QAT + KD

**Research hypothesis:** teach a student using verified teacher supervision while it trains with simulated/quantization-aware low precision, so the eventual **inference representation** tolerates 4-bit, 2-bit or (where architecture permits) ternary/approximately 1.58-bit parameters.

**Critical training distinction:** a low-bit *deployment* model does not imply that optimizer states, master weights, activation tensors or training compute are equally small. Standard QAT commonly keeps higher-precision trainable state and uses fake quantization; a GGUF Q4 file alone is not a training checkpoint.

**Proposed experimental progression (no results claimed):**

1. Select a **tiny reproducible student** and teacher data with explicit rights; establish FP/BF16 and static quantization baselines.
2. Test an isolated **QAT-only** run with a measurable memory/quality budget.
3. Test **KD-only**, then **QAT+KD** under the same data/splits, steps and resources. Use held-out benchmarks not used for teacher example selection.
4. If it helps, repeat in bounded layer/competence segments, preserving a trainable checkpoint and periodically exporting low-bit *inference candidates* for full-model regression.
5. Advance from a small laboratory model toward SSI-size students (e.g. 0.8B/1.7B) **only after** measured feasibility, compute approval and rollback evidence.

**Stop/hold:** no trainer or compatible quantizer, GPU/cost approval absent, invalid rights, unvalidated examples, catastrophic forgetting, or loss of routing/safety accuracy. No RunPod auto-start and no changes to production inference tags.

## 4. SCC and MultiQuant boundary — same contracts, no new runtime grammar

The existing SCC mission/intent contracts remain **`ssi.mission.goal.r1`** and **`ssi.mission.intent.r1`**; transition registry **`ssi.transition.champion-registry.r1`**. The MultiQuant bridge is a **proposal/observation** contract **`ssi.multiquant.scc.observation.r1`**, not an executor and not a signing authority.

The **12 existing MultiQuant step identifiers remain unchanged**, from `DISCOVER_MODEL`, `CHECK_LICENSE`, `CHECK_RESOURCES` through `REGISTER_RESULT`. Fragment distillation, per-layer QAT and multi-teacher synthesis are **future capabilities/plan stages**, **not** silently registered SCC execution commands, not new Champions and not automatic promotions. Each eventual worker needs a verified native binding, typed input/output, resource and rights contract, evidence/Notary integration, stage checkpoints and Director authorization.

Private R9.107 audit confirmed the presence of some SCC-native binding and observation-bridge source, but its readiness verdict was **NOT_READY** (25 of 26 inspected files accessible). Native production SCC migration and the R1/R2/R3 prototypes are **not yet shown end-to-end integrated**. Migration handoff is deferred by operator decision.

## 5. Real CPU model milestones — keep experiment families separate

### CPU-7 / Qwen2.5-Coder 1.5B

Existing public [CPU-7 report](../RESULTS/SSI_V5_PUBLIC_PROGRESS_CPU7_SCC_AWARENESS_20261018.md): **1 of 7 candidates built and smoke-tested, 0 of 7 production-approved** as reported. Later small synthetic tests exposed failures. Nothing about the independent Qwen3 experiment below increases the CPU-7 `1/7` count.

### Director Offline MICRO / Qwen3-1.7B — operator-provided R21–R25 logs

A **separate** pinned BF16 source was converted to GGUF and quantized to **Q4_K_M**; R21 read-only hash verification reported PASS, with BF16 ~3.79 GiB and Q4 ~1.194 GiB. Inference tests were **CPU-only**, bounded to one CPU thread, 4 GiB process-memory/swap-disabled envelope during Q4 inference, and not promoted into Router/Ollama production:

| Run | Operator-observed result | Interpretation |
| --- | --- | --- |
| **R22** | Correct short arithmetic answer (4); ~4.4 generated tokens/s | Smoke inference **PASS**, not quality certification. |
| **R23** | `ROBERT / WAITING_FOR_NODE01 / executed=false` for *physical* GNOME action while NODE-01 offline | One routing case **PASS**. |
| **R24** | `CODEX / WAITING_FOR_NODE01 / executed=false` for server-side repository coding | **FAIL** — agent correct, availability status incorrect. |
| **R25** | Four-case regression: **1/4 complete PASS**; agent selection 3/4, status selection 1/4, all four JSON envelopes and `executed=false` correct | **FAIL quality gate**. The model repeatedly blocked tasks that should remain SERVER_NATIVE. |

**No R26 BF16-vs-Q4 quality comparison was executed; operator deferred it.** The available logs **cannot attribute** the R25 error to quantization. No evidence of teacher distillation, QAT, 16 GiB 70B inference, multi-model fusion, SCC autonomous routing authority, or production promotion exists in these runs.

## 6. Resource, publishing and evidence policy

- **Director:** objective, mission ownership, permissions, progress and checkpoint decisions.
- **SCC:** native versioned mission representation and validated skill/transition bindings.
- **Router + Pocket/META LEGO:** capability matching, qualification, candidate/challenger/champion gates.
- **MultiQuant:** isolated model construction experiments, hybrid competence memory, proposals and quality/resource reports.
- **Robert/CODEX:** only the specifically authorized server-native and engineering execution paths; physical NODE-01 extension is optional.
- **Notary:** evidence provenance, not proof that a generated answer is semantically correct.

Prefer existing 24/7 resources and local machines. Treat GPU services as **separately approved options**, not zero-cost defaults. Never conflate a checkpoint hash with successful inference; a unit test with model quality; a proposed SCC step with a native executable binding; or a shared competence-memory record with distilled weights.

**Update discipline:** after every material experiment publish a dated, sanitized evidence note with model/revision class, hardware envelope, exact limited success/failure counts, whether comparison was paired, result category (`PASS`/`FAIL`/`BLOCKED`/`INCONCLUSIVE`), remaining gate and production status. Keep raw reports and private engineering packages off the public mirror. No retrospective overwriting of historical negative results.

## Next practical gates (not yet executed)

1. Private SCC R9.107/R9.108 → R1/R2/R3 compatibility audit and native binding inventory before migration.
2. D4 feasibility study: pick one very-large teacher, estimate full-precision source/disk cost, streaming-worker feasibility and a bounded 16 GiB student target; **no automatic weight download**.
3. D5 tiny QAT/KD research baseline with held-out data; **no model training without an approved backend/resource envelope**.
4. Compare candidate/student behavior on identical route semantics and task workloads, with rollback and no forced production promotion.

**Related records:** [SCC/Awareness lineage](../SCC_BLOCKS_MISSION_LANGUAGE_AND_AMNEZJA3_ATTRIBUTION_20261014.md) · [sanitized CPU-7/SCC history](../RESULTS/SSI_V5_PUBLIC_PROGRESS_CPU7_SCC_AWARENESS_20261018.md) · [existing CPU-7 plan](SSI_MULTIQUANT_CPU7_VPS_MODELS_R11_20261017.md).

### Short English summary

On 18 October 2026, SSI V5 declared **D4 BIG → MICRO (very large teachers to selected 16 GiB-deployable small-model competencies)** and **D5 native low-bit student (joint quantization-aware training and knowledge distillation)**. D1–D3 have **offline tested non-executing control prototypes**, not operational model trainers/mergers. Qwen3-1.7B Q4 smoke inference succeeded, but routing QA failed at **1/4** in R25; no model is promoted based on these observations. Full 70B/120B compression, QAT+KD training and native SCC execution remain unverified research goals.


## 7A. D4 resource correction / preferred pilot — 18 October 2026

**OPERATOR CORRECTION (supersedes the earlier preference for 14B and any optional 48 GiB-GPU path below):** the only authorized candidate test resource here is the **existing 24 GiB VRAM RunPod container**. The 48 GiB resource is **not available for this experiment due to reported space constraints**. The 24 GiB Pod already contains **one existing model**, which must be preserved. Current free container disk, durable volume, free host RAM, the actual GPU allocation and available GPU capacity have **NOT** been read in this update; do not infer them from VRAM. Do **not** start the GPU, delete files, resize storage, provision SWAP or download large files based solely on this plan.

**Preferred high-parametric, 16 GiB-RAM-compatible research family:** [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B), an Apache-2.0 MoE model with ~35B total/~3B active parameters per token. Unlike a 70B dense model, published aggressive quants plausibly fit the target **16 GiB CPU host including measured runtime headroom**. It is **not** the same checkpoint/architecture as Qwen3-14B/32B or the earlier Qwen3-1.7B pilot; cross-family comparisons must not be presented as quantization-only effects.

Published third-party GGUF examples (decimal GB file sizes, **not** measured GPU/CPU runtime usage): **IQ4_XS ~19.70 GB** as the preferred higher-quality reference on the **24 GiB GPU**, **Q3_K_M ~17.12 GB** intermediate, **IQ2_M ~12.96 GB**, **IQ2_XS ~11.69 GB**, and **IQ2_XXS ~10.68 GB** as aggressive **16 GiB CPU** candidates; published artifacts from [bartowski/Qwen_Qwen3.5-35B-A3B-GGUF](https://huggingface.co/bartowski/Qwen_Qwen3.5-35B-A3B-GGUF). These numbers can change across repository revisions: pin exact GGUF filenames, commit IDs and SHA256 before downloads. Do not promise quality at ultra-low bit rates.

**Storage-first gate:** inspect actual occupied disk in the existing 24 GiB Pod **without changing or deleting the pre-existing model**; account for the container/image, libraries, cache, logs, scratch files and a safe margin. If insufficient room for **even one** selected GGUF, use an independently checked transfer/staging strategy or record `BLOCKED_RESOURCE`; no silent storage upgrade or GPU bill. Only one reference needs to be GPU-loaded at a time; the smaller candidate can be independently tested on the 16 GiB CPU VPS after approved secure transfer.

**Alternative Polish-language benchmark, not the largest base:** [SpeakLeash Bielik-11B-v3.0-Instruct](https://huggingface.co/speakleash/Bielik-11B-v3.0-Instruct) (Apache-2.0; Polish-optimized; published Q4_K_M GGUF ~6.72 GB, Q6_K ~9.16 GB). Its 11B family can serve as a Polish teacher/comparator, but transferring its skills into a Qwen student would require permissible training data and a real distillation stage; tensors/tokenizers must not be blindly merged.

**SWAP policy:** host swap is **not additional GPU VRAM**; its presence does not cure inadequate CUDA allocation or container disk. CPU offloading can allow some execution at a substantial speed cost but does not prove “GPU fit”. For the final 16 GiB server, measure physically available memory and KV-cache usage first; existing server swap is only an emergency buffer, not assumed extra fast RAM.

**Evidence and current status:** `PLAN_ONLY / NO_MODEL_DOWNLOADED / NO_GPU_STARTED / NO_TRAINING / NO_PRODUCTION_PROMOTION`. Next gate: read-only status/disk inventory of the **24 GiB Pod** and existing model, then resource budget before any billed test. Earlier 14B-first plan immediately below is **historical/superseded** and retained for decision provenance.

## 7. D4 first pilot selection — 18 October 2026, PLAN / NO GPU START

**Operator research decision:** test one intermediate-size model, verify the maximum usable compression and RAM/speed/quality on the existing 16 GiB CPU host, and **only then** scale to a larger model from the **same family**. The intended reference worker is an **existing 24 GiB-VRAM GPU Pod if currently available**; a previously audited A40 48 GiB Pod was stopped. Free container disk, true live Pod availability, memory reservations, volume persistence and hourly price **must be rechecked**. Do not create, resume or bill GPU compute automatically.

**Selected family:** upstream `Qwen/Qwen3-14B` → later `Qwen/Qwen3-32B` (same Qwen3 generation, but different parameter configurations). Record exact immutable upstream revisions, tokenizer/chat-template compatibility and quantized source provenance before any paired comparison.

**Stage A — reference / feasibility only:** start with a *published pre-quantized* Qwen3-14B `Q6_K` (~12.12 decimal GB) on the authorized GPU as a higher-precision **reference**, compared with the **same checkpoint lineage** in published `Q4_K_M` (~9.00 GB), `IQ3_M` (~6.88 GB) and `IQ2_XS` (~4.69 GB), one model loaded at a time. The published files are external baselines — **not** proof of an SSI-built segmentwise converter. Stage and download **only those models for which measured free disk and GPU headroom suffice**, preserving existing Bonsai models/data. Keep identical prompts, decoding settings, deterministic SCC decision constraints and holdout tasks; record output quality, task outcomes, model memory incl. KV cache, prompt and generation speed, costs and provenance.

**Stage B — own fragment-worker research:** if Stage A confirms a useful 14B compression envelope, separately source compatible **BF16/FP16** weights and test **bounded-memory shard/tensor processing** with persistent manifests and stage gates. Do not pretend that requantizing `Q6 → IQ2` is equivalent to quantizing original BF16/FP16; aggressive cascaded requantization may damage quality. An actual claimed new result requires rebuilding the final GGUF and checking both whole-model inference and per-stage integrity. It is acceptable to enter `BLOCKED_RESOURCE` if true source and scratch space cannot fit.

**Stage C — increase parameter count only after A and B:** `Qwen3-32B` with published `Q4_K_M` (~19.76 decimal GB) as a **candidate reference** on a verified 24 GiB GPU **if runtime allocations actually fit**; published `IQ2_M` (~11.36 GB) or `IQ2_XS` (~9.95 GB) as compressed CPU 16 GiB *candidate files*. A weight file fitting 16 GiB does **not** prove operating-system headroom, context memory, acceptable latency or usable quality. Original 32B BF16 is ~65.53 GB and needs an independent source/scratch-storage plan. No automatic move to 70B/120B.

**Existing publication provenance for these specific GGUF *file sizes*:**
- [Qwen3-14B published GGUF quant list](https://huggingface.co/bartowski/Qwen_Qwen3-14B-GGUF).
- [Qwen3-32B published GGUF quant list](https://huggingface.co/bartowski/Qwen_Qwen3-32B-GGUF).
- [llama.cpp quantization and tensor-specific options](https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md).

**Current measurable outcome of this selection:** **PLAN_ONLY**. No GPU was resumed/started, no additional model was installed, downloaded, converted, executed, benchmarked or made production available by this declaration. Production Ollama tags and the canonical SCC/Router roles are untouched. Follow-up must begin with a read-only RunPod inventory; do not publish raw pod IDs, hostnames, credentials or proprietary task texts.


## Updated architecture decision — LEGO MultiControl belongs to SSI V5 (2026-10-18)

**Scope correction:** LEGO MultiControl is a **global SSI V5 shared control capability**, not owned by MultiQuant. MultiQuant uses a future **model-domain adapter** for compatibility, model composite proposals, quantization/distillation evidence and candidate review. The global core must remain domain-neutral and must not embed model/VRAM/GGUF internals. It is not a model-execution server or a new SCC parser.

The global decision [`SSI_MULTICONTROL_GLOBAL_ARCHITECTURE_DECISION_R1`](../SYSTEM/SSI_MULTICONTROL_GLOBAL_ARCHITECTURE_DECISION_R1_20261018.md) supersedes only earlier diagrams implying MultiControl is inside MultiQuant; existing D1–D5 goals, historical evidence, `NOT_READY` gates and separate Champion registries remain unchanged. **`PLANNED / GLOBAL_SSI / SHADOW_ONLY`; no live integration is claimed.**

## Current D4 infrastructure gate — R9.115 (2026-10-18)

**[RunPod 24 GiB dual-inventory read-only preflight](SSI_MULTIQ_RUNPOD24_DUAL_PREFLIGHT_R9_115_20261018.md)** corrects R9.114's Pod-only inventory: the existing 24 GiB Bonsai worker may be **Serverless** rather than a Pod. The separate v2 REST `GET /pods` and `GET /serverless` collections must both be examined. A private offline tool has **17/17 synthetic tests PASS**; live account connectivity, available disk, persistent model storage and the baseline installation are **not yet verified**. No GPU started or model downloaded.


## Latest real operator R9.115 audit — 24 GiB RunPod resource selection (2026-10-18)

Operator-provided **read-only** account inventory confirmed two **candidate Serverless 24 GiB endpoints** among five: one declared **40 GB container disk, workersMax=0**; another **30 GB disk, workersMax=1**. Existing 48 GiB Pod was `EXITED` and remains excluded. **Neither endpoint has verified image contents, installed Bonsai weights or free filesystem space; no network volumes were reported**. The next private R9.116 read-only image-identity audit has **22/22 offline software tests PASS**, but requires operator execution on MSI for real endpoint data.

**No 24 GiB GPU was started, no model was downloaded, and no model baseline is installed by this update.** See [bounded R9.115 evidence and R9.116 gate](SSI_MULTIQ_RUNPOD24_DUAL_PREFLIGHT_R9_115_20261018.md#operator-r9115-account-inventory-evidence-and-r9116-next-gate--2026-10-18).


## R9.118: approved 24 GiB Bonsai-to-Qwen-35B replacement gate (2026-10-18)

**New operator direction:** On the existing 24 GiB Serverless endpoint with **40 GB** temporary disk, **replace the Bonsai deployed model** with an independently versioned, SHA-pinned **Qwen3.5-35B-A3B IQ4_XS** (~19.70 GB third-party GGUF) reference. Keep original Bonsai GHCR R2 release and private endpoint history/recovery metadata. **Do not touch** the separate Qwen 27B 24 GiB/30 GB endpoint, any 48 GiB worker, SSI MODELS production weights, router aliases or Champion registries.

Same-base comparison candidates for the target CPU-only **16 GiB** VPS: **IQ2_M** (~12.96 GB), **IQ2_XS** (~11.69 GB), with further MultiQuant R&D contingent on held-out quality, actual RAM/CPU and correct high-precision-source provenance. 70B+ ultra-low-bit might fit 24 GiB VRAM as a research display, but has no straightforward practical 16 GiB RAM same-checkpoint CPU comparison and is **not selected** for first controlled D4 research. The original BF16 of this 35B family (~71 GB GGUF) must be staged outside the 40 GB Serverless scratch if true SSI re-quantization is attempted.

**Deployment not performed.** Private R9.118 preparation passed **26/26 synthetic software tests**; no new model is installed or running yet. See [operator decision and gates](SSI_MULTIQ_RUNPOD24_DUAL_PREFLIGHT_R9_115_20261018.md#r9118-operator-decision--replace-24-gib-bonsai-endpoints-model-with-a-pinned-qwen-35b-baseline-2026-10-18).
