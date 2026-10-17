# SSI V5 — RunPod 24 GB Dual-Model Queue + CORE24 Quantization R2

**Date:** 2026-10-17  
**Status:** ARCHITECTURE & READ-ONLY AUDIT PLAN — **NOT DEPLOYED; NO GPU/LLM CALLS PERFORMED**  
**Supersedes the resource allocation proposed in** [the preliminary two-student R1 design](SSI_DECISION_STUDENTS_24GB_R1_PLAN.md).

This correction is based on historical October 17 SSI operator reports. It must be reconciled with live server and RunPod metadata before applying changes.

## The two separate computers must not be confused

| Scope | Existing resources reported | New work |
|---|---|---|
| **RunPod serverless, 24 GB VRAM GPU** | Bonsai 2 27B PQ2_0 image `ghcr.io/jankes72/ssi-bonsai27:r2`, 40 GB **ephemeral** container disk, GPU class `ADA_24`, endpoint previously `bfitqawet4mz3w`, workers min/max 0/0. Image manifest public; GPU inference **unverified**. | Keep existing Bonsai; add **one more model on the same worker's storage**; use a single GPU **alternately** via a durable cross-mission queue, like the parallel RunPod project's dynamic queue. Do **not** rent a second GPU or buy a persistent network volume. |
| **CORE24 VPS, always on** | Debian 12, 4 vCPU, 16 GB system RAM, ~120 GB SSD, Ollama; 13 **already quantized** model variants reported, ~71 GiB free at last inventory. | Inventory and prepare **additional, explicitly versioned smaller quantizations** where supported, without overwriting originals or blocking SSI CODEX operations. |
| **Other RunPod GPU resource** | Three model slots reported on a separate on-demand GPU worker. | Keep its queue, models and deployment untouched. Share SSI's overarching scheduling policies, not an assumed physical disk. |

**Runtime correction:** PrismML states that its Bonsai `PQ2_0` and `PTQ1_0` GGUF files require the PrismML fork of `llama.cpp`; stock Ollama cannot run them. The Bonsai R2 history indicates a custom PrismML llama.cpp image. Whether Ollama is additionally installed in the *actual* RunPod image has not yet been verified and must not be assumed.

### RunPod storage and GPU budget

- Official upstream Bonsai PQ2_0 language weights **7.21 GB**; official PTQ1_0 weights **5.95 GB**. PQ2_0 remains the preserved existing R2 release. PTQ1_0 may be investigated as an **additional future variant**, not an automatic replacement.
- Second model: **exact 200B-class teacher identity is not yet verified**. A full dense 200B model cannot sensibly be treated as a small model simply by renaming/quantizing it. If the second model is meant to be a task-specific small derivative, that derivative must first actually exist and its weights, runtime and license must be verified. An existing smaller model can be deployed instead while that project is pending **only by operator direction**.
- Design for a second model of approximately **7B–8B Q4 (~4–6 GB weights as a rough planning allowance)**. Estimate *full disk* use, image layers, downloaded weights, temporary extraction, logs and caches against **40 GB**. Weights on disk may differ from compressed Docker archive size. Verify the R2 image: the previously reported **~2.38 GB archive is smaller than the official 7.21 GB weight file** and therefore should not be assumed to embed the full model without inspection.
- During inference permit **one GPU-loaded model at a time**. Full VRAM use includes kernels, context/KV cache and runtime overhead; verify after normal real mission inference.
- Ephemeral container disk is **wiped on worker scale-down**. Two models must be baked into a **new image R3** or available from verified public sources with predictable first-boot restoration. Paid persistent volume is expressly excluded. RunPod's built-in Hugging Face cached-model field **supports one model per endpoint**, so it does not by itself solve hosting two cached model artifacts. Possible R3: bake both eligible files into one image; or bake one and safely fetch the other on start. Do not alter public R2.
- Preserve no always-on GPU: on activation target **min workers = 0, max workers = 1**, idle TTL tuned to the normal SSI mission burst; **currently reported max=0**, which prevents work until deliberately activated after tests. No cost-increasing changes without an auditable review.

### Queue state machine

**Canonical durable mission queue is on SSI's VPS**, not solely on an ephemeral GPU worker. Both this 24 GB RunPod worker and the other RunPod resource can consume assigned tasks under SSI's existing mission IDs and budgeting.

```text
NEW / READY
  -> ROUTER_SELECTS_MODEL + COST/CAPABILITY_GUARDS
  -> QUEUED_FOR_RUNPOD_24GB
  -> WAITING_FOR_WORKER (worker scale-up only after activation)
  -> ENSURE_MODEL_ON_DISK
  -> UNLOAD_PREVIOUS_MODEL_IF_REQUIRED
  -> LOAD_SELECTED_MODEL_TO_VRAM
  -> RUN_MISSION_TASK (one at a time per worker)
  -> NOTARY_EVIDENCE + COST + LATENCY + QUALITY/FAILURE
  -> CHECKPOINT_COMPLETE / RETRY_WITH_BOUNDS / ESCALATE
  -> IF_QUEUE_HAS_JOBS: KEEP_WORKER, choose next fairly
  -> IF_QUEUE_EMPTY: IDLE_TIMER -> SCALE_TO_ZERO
```

- Batch nearby requests for the same model when safe, while bounding starvation of the other model and observing the original mission priority.
- Dedupe by canonical mission ID/idempotency key, use a lease and ack to ensure crashes do not silently lose or repeatedly execute paid work.
- Failure during switch must release VRAM/process correctly and return a recoverable result to the VPS queue.
- No API keys in public logs; internal authorization/tenant isolation stays in the SSI gateway.
- Use PrismML llama.cpp for Bonsai and a separate inference engine such as Ollama **only if the second model actually needs and supports it**. Keep both behind one authenticated worker handler.
- Automatic retry, scheduling and autoscaling apply to useful, authorized missions only — **not to synthetic benchmark traffic**.

## CORE24 24/7: all 13 small installed variants enter the quantization inventory

The following variant families and approximate quantization states are from operator-reported history. Each is assessed individually: **all 13 are in scope**, but new lower-bit versions are produced only when the source, architecture and licensing permit it. Preserve originals until real SSI mission results justify adopting a smaller one.

| # | Reported model | Existing quantization (reported) | R2 conversion work |
|---|---|---|---|
| 1 | Hermes 3B | Q4 | Check original source and optional compatible Q3/Q2 candidate |
| 2 | Hermes 8B | Q4 | Check original source, Q3 already elsewhere, optional Q2 candidate |
| 3 | Qwen2.5-Coder 1.5B | Q4 | Decide whether compression is worth reduced decision/code accuracy |
| 4 | Qwen2.5-Coder 3B | Q4 | Source-verified Q3/Q2 candidate if compatible |
| 5 | Qwen2.5-Coder 7B | Q4 | Compare pre-existing Q3; only consider further quantization if needed |
| 6 | Qwen3 1.7B | Q4 | Check architecture, compatible lower-bit source |
| 7 | Qwen2.5-Coder 7B | Q3 | Already compressed; never assume Q2 is advantageous |
| 8 | Hermes 8B | Q3 | Already compressed; original higher-precision source required for safe new conversion |
| 9 | DeepSeek-Coder 6.7B | Q4 | Source-verified Q3/Q2 candidate |
| 10 | Qwen3.5 4B | Q4 | Check GGUF compatibility and exact revision |
| 11 | Liquid LFM2.5 8B-A1B | Q4 | Verify supported llama.cpp/Ollama quantizers for this architecture |
| 12 | Liquid D1 3B | To verify | Special decision-model interface: verify supported weight format before conversion |
| 13 | Tev1 0.8B | To verify | Special decision-model interface: verify format; extra compression may not pay off |

**Important:** `Q4` and `Q3` alone are not exact precision levels. Record `Q4_K_M`, `Q3_K_M` and precise digests from `/api/tags` and `/api/show` before computing variants. Ollama's documentation says it **does not quantize imported GGUF during import**; prepare correct GGUF files with a compatible quantizer before `ollama create`. Converting already-low-bit weights again may degrade accuracy and should not be treated as equivalent to quantizing an original source.

### Read-only preflight: commands to run **on CORE24 VPS** only

```bash
ollama list
ollama ps
df -h /
free -h
```

For exact model metadata use the Ollama local API: `GET http://127.0.0.1:11434/api/tags` and `POST http://127.0.0.1:11434/api/show` with the exact `model` value. Avoid pasting public output containing secrets or private filenames. These calls list metadata and **do not request inference**.

### Allowed quantization process (future deployment stage)

1. Read-only inventory of all 13 models, file hashes, true quantization, licenses, CPU/RAM/disk free, active worker reservations and real SSI routing references.
2. Map each to its official downloadable higher-precision source or existing fully compatible pre-quantized weights. Prefer *source quantization* rather than Q4-to-Q2 requantization.
3. Prepare one candidate at a time in a staging area, not all source weight files simultaneously. Refuse conversion if temporary disk/RAM limits cannot be met.
4. Register candidate under a **new** tag, e.g. `ssi-coder-7b-q3:trial`. Do not overwrite any installed model tag or modify existing router aliases.
5. Initial validation consists of format integrity and first **real approved mission** with evidence, not an artificial LLM benchmark. Compare similar mission categories over time, explicitly recognizing selection bias.
6. Calibrate Router V10 using mission success, fail/inconclusive, quality, response times, real costs and system constraints. Promotion is operator-approved and reversible.
7. Publish only the source links, exact licensed version/quantization, and **aggregated** performance observations from real SSI tasks — no private memory, proprietary code, server addresses or raw prompts.

### Guardrails and completion state

- **NO ACTIONS EXECUTED ON RUNPOD OR CORE24** by this document.
- **NO NEW MODEL TRAINED OR QUANTIZED** by this document.
- Existing GHCR Bonsai R2 remains public and unchanged; the second worker model and dual-handler require a separately versioned R3 artifact.
- No additional GPU lease, active worker 1, paid persistent storage, or change to the three models on the other GPU.
- Next necessary evidence is exact CORE24 `ollama list`/quantization metadata and RunPod R2 worker image/handler content and 24 GB hardware memory report. Do not make paid GPU calls merely to audit if static manifests suffice.

### Technical source references

- [PrismML Bonsai 2 27B GGUF + forked runtime](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)
- [PrismML known issues: stock Ollama incompatible with PTQ1_0/PQ2_0](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf/blob/main/KNOWN_ISSUES.md)
- [RunPod endpoint settings / worker scaling](https://docs.runpod.io/serverless/endpoints/endpoint-settings)
- [RunPod cached-model limitations](https://docs.runpod.io/serverless/endpoints/model-caching)
- [RunPod Serverless storage and lifecycle](https://docs.runpod.io/serverless)
- [Ollama importing GGUF and quantization](https://docs.ollama.com/import)
- [Ollama FAQ: `keep_alive`, queue and concurrent model loads](https://docs.ollama.com/faq)
