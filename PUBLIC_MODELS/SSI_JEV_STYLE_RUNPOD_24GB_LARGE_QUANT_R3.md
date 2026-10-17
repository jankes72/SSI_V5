# SSI V5 — JEV-Style Decision Engine on the Existing 24 GB GPU (R3)

**Date:** 2026-10-17  
**State: CANDIDATE SELECTION & CAPACITY PLAN ONLY. No model installed, quantized, deployed, benchmarked or billed by this change.**  
**Earlier deployment architecture:** [RunPod dual-model queue and CORE24 quantization R2](SSI_RUNPOD_DUAL_MODEL_CORE24_QUANTIZATION_R2.md)

## Corrected objective

Keep the currently published **Bonsai 2 27B R2** as the first model on the existing **RunPod GPU with 24 GB VRAM**. Add **one very capable, strongly quantized larger decision-capable LLM** as the second model, fitting the **same reported 40 GB ephemeral container disk**, with **one model loaded into GPU VRAM at a time**. Use the existing SSI Director/Router V10 controlled durable mission queue, similar to the other RunPod worker that already has three reported models. No new on-demand GPU instance, persistent paid volume or always-on GPU.

**JEV is the behavioral interface reference**, not the actual source weights: TypeSafe's [JEV 1.13](https://openrouter.ai/typesafe/jev-1.13/) offers typed choices for classification/routing. Its hosted weights cannot simply be downloaded, re-quantized or incorporated without licensed access. Our second model will be an openly published **generative LLM** behind an SSI-owned validated structured-decision adapter.

## Concrete candidate sources and published sizes (not installation claims)

| Candidate | Exact public variant and source | GGUF weights | Combined with Bonsai 7.21 GB | Expected trade-off |
|---|---|---:|---:|---|
| **A: maximum large-model experiment** | [bartowski/Llama-3.3-70B-Instruct-GGUF: IQ2_XXS](https://huggingface.co/bartowski/Llama-3.3-70B-Instruct-GGUF/blob/main/Llama-3.3-70B-Instruct-IQ2_XXS.gguf) | **19.10 GB** | **26.31 GB** | 70B with very aggressive quantization; source characterizes IQ2_XXS as low quality. Short context and small concurrency only until proven. License review required. |
| **B: primary quality/speed candidate** | [unsloth/Qwen3.5-35B-A3B-GGUF: Q3_K_M](https://huggingface.co/unsloth/Qwen3.5-35B-A3B-GGUF/blob/main/Qwen3.5-35B-A3B-Q3_K_M.gguf) | **16.8 GB** | **24.01 GB** | 35B total and 3B activated parameters (MoE); potentially attractive decision throughput. Requires recent compatible llama.cpp; performance remains untested in SSI. |
| **B2: higher precision if headroom permits** | [unsloth/Qwen3.5-35B-A3B-GGUF: Q4_K_M](https://huggingface.co/unsloth/Qwen3.5-35B-A3B-GGUF/blob/main/Qwen3.5-35B-A3B-Q4_K_M.gguf) | **21.2 GB** | **28.41 GB** | Higher precision than Q3, but less 24 GB VRAM capacity for runtime/KV overhead. No fit guarantee. |
| **C: dense quality comparator** | [unsloth/Qwen3-32B-GGUF: Q4_K_M](https://huggingface.co/unsloth/Qwen3-32B-GGUF/blob/main/Qwen3-32B-Q4_K_M.gguf) | **19.8 GB** | **27.01 GB** | Dense 32B Q4, potentially less quantization degradation; compute and real mission accuracy not measured. |

Sizes are **published decimal GB figures for specific files**, not measured GPU usage. Bonsai's original weight file is reported as 7.21 GB in [PrismML's upstream repository](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf). A reported compressed SSI Docker archive of only ~2.38 GB does **not** establish that the Bonsai weights are embedded; inspect the R2 image/handler before capacity decisions.

**40 GB disk and 24 GB VRAM are independent constraints.** Container image layers, transient downloads, cache, logs, runtimes and extraction consume disk, while weights loaded on the GPU, CUDA allocations, KV cache and concurrency consume VRAM. All combinations above require a real read-only image/worker inventory and runtime fit measurements before declaring them deployable.

A ~200B dense model at 2 bits/weight has an illustrative ~50 GB **raw weight-bit floor**, excluding quantization overhead, before allowing for Bonsai and container software. Extreme 1-bit variants, MoE/offload or different architectures change the arithmetic but cannot be presumed usable or fast. **Do not promise 200B in 24 GB VRAM**. A larger parameter count with extreme quantization may make worse decisions than a smaller higher-precision model.

## Runtime and serial queue

```text
SSI Director -> Router V10 -> VPS durable job queue
              |
              v
Existing RunPod 24 GB GPU worker, max one GPU-loaded model at a time
              |-- choose Bonsai 27B PQ2_0 -> PrismML-compatible llama.cpp
              |-- choose verified second GGUF -> compatible llama.cpp or Ollama
              |
              v
Validated decision adapter -> canonical SSI decision result
              |
              v
Notary evidence -> Research Memory/SCC/microsegments -> routing calibration
```

Keep the chosen model loaded for an eligible run of queued tasks; switch only when the next authorized mission needs the other model, with starvation/fairness guards. When work is done, scale to zero. GPU jobs must not be launched just for model comparisons or synthetic benchmarks.

The decision adapter exposes typed choices and normalized, reviewable reason codes while preserving Director authority. **Generated self-reported probabilities are NOT calibrated confidence estimates**. Calibrate routing thresholds only from reviewed real mission outcomes; reject disallowed actions independently of the LLM choice. A hosted JEV call can remain an independent decision provider/fallback, separate from the local LLM.

## Safe stages (no new GPU spending during preflight)

1. Read-only inspect active RunPod endpoint, image digest, handler, existing Bonsai runtime, Ollama presence/absence, storage layout, environment, 24 GB card identity and GPU job queue. The historical endpoint may have workers max=0; do **not** silently enable GPU workers.
2. Verify disk's actual writable free bytes and Docker image layers, including whether weights are already present or downloaded on cold start. Do **not** infer capacity from the compressed archive.
3. Review upstream source license and precise immutable GGUF file revisions. **Use published pre-quantized variants to prototype**; making an independently quantized file from the original high-precision checkpoint requires significantly more off-worker disk/RAM and is a separate build task.
4. Pick **one** second model for an R3 image by operator-approved selection; create a new GHCR version rather than altering R2. Prefer B (Qwen3.5 35B-A3B Q3_K_M) as the initial 24 GB deployment candidate; optionally A (Llama 70B IQ2_XXS) as a later, more aggressive large-parameter experiment after capability/headroom is established.
5. Run any initial startup or verification as part of the first authorized **real SSI mission**, not for synthetic benchmarking, with explicit cost/lease limits.
6. During genuine Director/CODEX/Robert tasks log task class, actual decision outcome, time, GPU/VRAM peak, cost and failure. Publish only aggregate anonymized findings and exact model provenance.
7. Promote only if the actual SSI task evidence justifies it, with operator approval and rollback. Keep Bonsai R2 and all other existing workers intact.

**Operational recommendation:** The parameter-maximizing 70B IQ2 variant is worth researching, but the 35B MoE Q3 variant is the safer first engineering choice for one 24 GB GPU. Neither has demonstrated Jev-like quality in SSI yet. No quantization/deployment work has been carried out by this planning document.
