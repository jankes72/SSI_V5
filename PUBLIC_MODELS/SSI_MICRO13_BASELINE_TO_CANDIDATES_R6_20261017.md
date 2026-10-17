> **2026-10-17 correction — separate future five:** In addition to the 13 MICRO candidates, **five further Director/Robert-oriented model candidates are only PLANNED**. The user explicitly confirmed that these five **do not yet exist**, have **not been qualified by Robert's research**, and **are not distributed**. Do NOT label them as tested/approved, do NOT activate gateway entries, and do NOT invent names, hashes or claims about them. The planning total is **13 proposed MICRO + 5 proposed future Director/Robert = 18 candidates**, alongside **13 operator-reported existing Ollama baseline variants** (runtime metadata verification pending). See the independent five-candidate acceptance criteria at the end of this page.

# SSI MICRO-13 — baseline and first small-model cohort

**Date:** 2026-10-17  
**State:** **13 proposed variants, 0 built, 0 added to the live gateway, 0 independently benchmarked**. Actual installed-model tags/digests remain to be read from the production MODEL VPS.  
**Purpose:** Pair each of the 13 operator-reported Ollama variants on the existing 24/7 **MODEL VPS** with one future smaller candidate, for incremental comparison during **real SSI missions only**.

## Accepted three-server division

- **DIRECTOR VPS:** mission planning, model selection and policy; no quantization.
- **ROBERT VPS (~4 vCPU / 16 GB RAM CPU):** prepare and quantize **one** authorized model at a time using spare capacity, without interrupting Robert's primary missions. Source checkpoints too large for free RAM stay **BLOCKED**, not silently transferred to paid RunPod GPUs.
- **MODEL VPS:** keep all current 13 variants and the existing gateway intact. Once an independent build succeeds, a new versioned model tag may be installed **only after approval** as a controlled real-mission candidate; the original remains as fallback.

This is **13 reported installed variants, not necessarily 13 unique foundation models**: Hermes 8B and Qwen2.5-Coder 7B each appear with both Q4 and Q3 baselines.

## First 13 candidate selections — only suggestions, exact source compatibility pending

| Priority | Existing baseline (operator-reported) | First smaller quantization proposal | Task family for real SSI observations | Important condition |
|---|---|---|---|---|
| 1 | Qwen2.5-Coder 1.5B Q4 | Q3_K_M | Short code edits, software triage | Verify F16/BF16 source and quality impact |
| 2 | Qwen3 1.7B Q4 | Q3_K_M | Classification, routine model routing | Verify Qwen3 source/revision |
| 3 | Hermes3 3B Q4 | Q3_K_M | Agent intent, bounded instructions | Preserve accurate tool and goal instructions |
| 4 | Qwen2.5-Coder 3B Q4 | Q3_K_M | Code patch plans, error diagnosis | Prefer source quantization, not requant |
| 5 | Tev1 0.8B (reported) | Q4_K_M | Typed decisions and routing | **HOLD** until System One runtime/quantizer and original precision verified |
| 6 | Liquid D1 3B (reported) | Q4_K_M | Typed classification and risk decisions | **HOLD** until System One runtime/quantizer and original precision verified |
| 7 | Qwen3.5 4B Q4 | Q3_K_M | Multilingual SSI mission triage | Verify model-generation-specific quantizer support |
| 8 | DeepSeek-Coder 6.7B Q4 | Q3_K_M | Coding and failure recovery | CPU RAM feasibility from higher precision source |
| 9 | Qwen2.5-Coder 7B Q4 | Q3_K_S | Coding, error analysis | Different from typical existing Q3_K_M; avoid duplicate after exact audit |
| 10 | Hermes3 8B Q4 | Q3_K_S | Agent planning, tool workflow | Different from typical existing Q3_K_M; CPU RAM feasibility |
| 11 | LFM2.5 8B-A1B Q4 | Q3_K_M | Tools/automation/general planning | **HOLD** until MoE architecture/source RAM and execution compatibility reviewed |
| 12 | Qwen2.5-Coder 7B Q3 | Q2_K | Ultra-compact coding decisions | **HIGH RISK**: quality regression; quantize from appropriate full-precision source |
| 13 | Hermes3 8B Q3 | Q2_K | Ultra-compact agent/routing decisions | **HIGH RISK**: quality regression; quantize from appropriate full-precision source |

The choices are **targets to assess**, not claims that the quantizers or available checkpoints support them. **A smaller file does not automatically produce a more accurate, faster or suitable SSI decision model.** If an existing original variant already uses the desired exact quantization and revision, register it as a baseline rather than waste disk with an equivalent copy.

**Important technical point:** [llama.cpp's official quantization guidance](https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md) warns that re-quantizing already Q3/Q4 weights can severely reduce quality compared with quantizing the original 16/32-bit model. The production MODEL VPS is *not* the build machine; original weight hashes/licenses and actual ROBERT resource headroom must be checked before a build. System One decision interfaces for [Tev1](https://ollama.com/library/tev1) and [Liquid D1](https://ollama.com/library/d1) are different from plain text generation.

## Gateway admission and meaningful comparison

1. **Read-only inventory** of the 13 existing Ollama models: exact name, immutable digest, GGUF quantization, source, and original model capabilities. No inference for inventory.
2. **Robert builds** one variant from a supported, properly licensed higher-precision source, only if safe resource headroom exists; preserves all originals.
3. **Static artifact qualification:** immutable hash, exact quantizer revision, validity and compatibility. If any check fails, candidate is not registered as runnable.
4. **Staged gateway entry:** keep every candidate **DISABLED** before the actual artifact exists and separate operator deployment approval has been given. Do not edit Router V10 or overwrite original model identifiers.
5. **Controlled real-mission assignment:** when a candidate is ready and approved, it can perform ordinary authorized SSI tasks with automatic **Director/Router fallback** to a known suitable model if the candidate fails.
6. **Notary evidence:** model/digest/quant, original-versus-candidate reference, mission class, actual result (PASS/FAIL/INCONCLUSIVE), latency, cost/resources and micronetwork **identifier only**. No extra tasks for tests and no duplicate inference for benchmarking.
7. **Route learning:** aggregate outcomes by task class, precision, model variant, model runtime and micronetwork. Compare with care: missions are not necessarily equal in difficulty. Require operator review before router changes.
8. **Public information:** publish exact upstream model/version, quantization, observed advantages and unsuitable use cases as qualified, anonymized findings. **Proprietary Router V10/S10, micronetwork, SCC and internal adapter code and private mission payloads remain unpublished.**

The first-series output is **one comparison slot per existing model baseline**. A future published list will count **actually built candidates** separately from proposed targets. The original 13 remain operational no matter how many experimental variants are successfully created.

**Related:** [ROBERT builds / MODEL VPS executes / DIRECTOR orchestrates](SSI_V5_ROBERT_BUILDER_MODEL_VPS_PRODUCTION_R5_20261017.md) · [public model provenance catalog](SSI_V5_MODEL_CATALOG_AND_LIVE_ROUTING.md).


## Planned Director/Robert extensions — 5 additional candidates (NOT BUILT)

The operator clarified that a further **five** smaller or role-specialized candidates for SSI Director and Robert will be designed **later**. These do not have verified exact model identities, licenses, source revisions, quantization choices, checkpoint hashes, or results, and **no artifact has been generated or deployed**. The five slots are reserved only as IDs `DIRECTOR_ROBERT_FUTURE_01`–`_05`, **not names of actual models**, and are not part of the first MICRO-13 build queue.

Each planned slot remains `PLANNED_UNSELECTED` until a specific original model, permissioned source and quantization strategy are selected; then `BUILD_CANDIDATE` after resource preflight; then `BUILT_UNVALIDATED` after a reproducible artifact exists; then `SHADOW_ELIGIBLE` only after interface/security qualification; then `MISSION_EVIDENCE_COLLECTING` when it runs as part of authorized real work; finally `APPROVED_FOR_DISTRIBUTION` only if there is sufficient reviewed real-mission evidence and explicit operational approval. No synthetic benchmark missions and no extra provider calls solely to grade models. Keep Robert's primary missions prioritized.

**Count discipline:** 13 reported originals + **up to** 13 planned new MICRO variants + **up to** 5 planned additional Director/Robert variants. The 18 new entries are **planned, not available**. No count of candidate slots is proof of delivered/verified models. Existing GUI, Router, micronetwork and source implementation stays private.
