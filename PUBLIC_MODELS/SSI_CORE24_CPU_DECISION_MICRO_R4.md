# SSI V5 — JEV-Style CPU Decision Micro on CORE24 (R4)

**Date:** 2026-10-17  
**Status:** DESIGN ONLY — NOT TRAINED / NOT QUANTIZED / NOT INSTALLED. No inference, GPU, training or provider calls were made.  
**Owner of final decisions:** SSI Director, through Router V10 and existing access, budget and recovery controls.

> **Confirmed target constraint (operator instruction):** This small specialized decision model must fit and run on the **existing SSI CORE24 always-on VPS with 4 vCPU and 16 GB of system RAM, CPU ONLY**, alongside SSI's existing Ollama and 13 reported installed variants. It is NOT the 24 GB VRAM RunPod and cannot assume any GPU. This CPU-targeted student is separate from the earlier proposal to store a second large model alongside Bonsai on the on-demand RunPod GPU.

## What is being built?

A **small, task-specialized and quantized local decision model**, serving functions *similar to* JEV (structured routing choices), but controlled by SSI. It will advise the SSI Director and Router V10 about model/provider selection, budget-aware escalation, delegating to SSI CODEX/Robert, tool/skill selection and error recovery.

**It is not a copy of JEV weights**, which are only a behavior/interface reference. **It is not a 70B or 200B model “quantized into 3B.”** Quantization reduces bits per parameter, not the parameter count. To create a 3B student using decisions of a 27B or ~200B teacher, select an already small permitted foundation model and use **distillation/task adaptation** from properly permissioned, verified **real SSI mission records**. The exact “200B” teacher remains unidentified and cannot be named as a training source until confirmed.

SSI canonical knowledge continues to reside in microsegments, Research Memory, SCC and other durable stores, **not** solely in model weights.

## CPU-only capacity and shortlist — proposals, NOT measured benchmarks

| Candidate size | Plausible Q4 weight budget | Role and caveat |
|---|---:|---|
| **1.5B Q4** | ~1 GB | Light fallback for CPU routing, if output quality suffices |
| **3B Q4** | ~2 GB | **Primary student target**: balance headroom and decision capacity |
| **7B–8B Q4** | ~4–6 GB | Higher capability candidate only if RAM headroom and real mission latency justify it |
| **14B Q4** | ~8–11 GB | Not a default for this existing 16 GB CPU-only VPS; likely disruptive or slow |

The full loaded resident size also includes runtime and KV cache; CPU speed on 4 vCPU may be limiting even when weights fit in 16 GB. Do not allocate all host RAM to the student. Existing SSI CORE24 services, OS, concurrent missions and Ollama-loaded models take priority. Model disk size, RAM use and 24/7 availability are distinct measurements.

**First preference:** choose a verified, redistribution-compliant small model architecture with structured JSON output support; adapt to SSI's typed decision schema. Quantize from compatible higher-precision weights **after** adaptation using a matching GGUF/Ollama engine or another supported CPU runtime. Do not blindly requantize an already Q4/Q3 GGUF and claim equal quality.

## Integration: one conservative decision interface

```json
{
  "mission_id": "<existing canonical id>",
  "task_class": "software_patch",
  "allowed_options": ["core24_local_coder", "core24_local_decider", "defer_to_director"],
  "suggested_choice": "local_coder",
  "reason_codes": ["HAS_LOCAL_SKILL", "COST_BOUND"],
  "model_revision": "<pinned student version>",
  "evidence_ref": "<internal mission evidence id>"
}
```

Model-produced confidence is not automatically reliable: probability calibration comes from accumulated observed mission outcomes. The Router independently validates choice against **actual capabilities, task restrictions, user authority, privacy, budgets, provider availability and system health**. Unknown or invalid decisions fall back to the existing router/Director. A misbehaving student must not stop live SSI missions.

## Live-only training and calibration

1. Preserve the existing 13 model tags, Ollama setup, routing state, budgets and mission queue; take only **read-only inventory** of disk, installed quantizations, actual free RAM under usual load, and active processes.
2. During useful Director/CODEX/Robert missions, Notary logs evidence of selected actions and actual outcomes. No duplicate model calls or stand-alone benchmark requests.
3. Curate redacted, licensable task/decision/outcome examples for **separate, later training**. Reject missing, uncertain or unverifiable labels.
4. **CPU-only location is mandatory:** training, quantization, evaluation and inference for this offline-micro project must run **only on the existing 4 vCPU / 16 GB RAM CORE24 VPS**, during operator-approved low-load maintenance. If training or quantization needs more RAM/disk/time than this VPS can safely provide, mark it **NOT_FEASIBLE_ON_CORE24** and defer; **no RunPod, paid external LLM/GPU, other VPS or local computer fallback**. Check training/data and license terms before any work.
5. Quantize the resulting small student to an exact pinned type such as `Q4_K_M` **only if the chosen architecture and runtime support it**. Record hash, source/license, quantizer revision and actual model file size.
6. Integrate behind a feature flag, start with non-authoritative recommendations during **real authorized SSI work**, without extra cost-generating calls solely for comparisons.
7. Record outcome, latency, memory and budget data in normal mission telemetry; promote/rollback only by operator approval. Publish only anonymized aggregate findings and reproducible public-safe model-source links.

## Read-only preflight — run **only on SSI CORE24 VPS**

```bash
printf '\n== RAM ==\n'; free -h
printf '\n== CPU ==\n'; lscpu | grep -E '^(CPU\\(s\\)|Model name|Architecture):'
printf '\n== DISK ==\n'; df -h /
printf '\n== OLLAMA INSTALLED ==\n'; ollama list
printf '\n== OLLAMA LOADED NOW ==\n'; ollama ps
```

This preflight doesn't download weights, load a model, restart a service, consume GPU time, or run a benchmark. It cannot reveal all instantaneous process memory budgets; detailed process/peak tracking is a subsequent read-only audit if needed.

## Relationship to the existing RunPod queue

**Different, independent plan:** [RunPod 24 GB dual-model queue and all CORE24 quantizations](SSI_RUNPOD_DUAL_MODEL_CORE24_QUANTIZATION_R2.md). The on-demand RunPod may separately retain Bonsai 27B and a second large quantized model *on disk*, loaded into 24 GB GPU VRAM one at a time. [Large-GPU candidate study](SSI_JEV_STYLE_RUNPOD_24GB_LARGE_QUANT_R3.md) remains a **separate optional candidate exploration**, not the deployment target for this CPU micro model. The other RunPod worker's three model slots are unchanged.

**R4 acceptance gate:** no model selection, quantization or placement until the real CORE24 free-RAM/process inventory is reviewed. The 16 GB number is physical/virtual system RAM, not 16 GB spare capacity.


## CPU-only resource lock — operator clarification (2026-10-17)

The user explicitly restricts **ALL computational activity of the Director Offline Micro model-preparation project** to the **existing always-on SSI CORE24 4-vCPU/16-GB-RAM CPU-only VPS**. This includes read-only inventory, source preparation, compatible quantization, locally feasible adaptation, eventual inference and analysis of actual SSI mission results. Existing external RunPod resources remain a **different, separate SSI project**, not a fallback for this one. The 13 originals and other CORE24 services must remain functional.

The private **SSI_DIRECTOR_OFFLINE_MICRO_R2_CORE24_CPU** toolkit has CPU-only environment restrictions, refuses detected GPU/RunPod execution, requires resource headroom and owner approval, uses a single conversion job, and never automatically downloads or calls remote models. The source archive is **private and NOT present in GitHub**. A plan to produce 13 variants and 26 candidates is **not evidence** that model conversion has been completed. If an original high-precision checkpoint is too large for CORE24, the corresponding build is blocked rather than outsourced. Published small source-licensed quantizations can be considered separately without misrepresenting them as SSI-produced quantizations.
