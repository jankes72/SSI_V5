> **SUPERSEDED RESOURCE DESIGN (2026-10-17):** The user clarified the actual infrastructure. **Do not treat the two-student R1 resource placement below as an approved deployment.** The current architecture is [RunPod 24 GB Dual-Model Serial Queue + CORE24 13-Model Quantization R2](SSI_RUNPOD_DUAL_MODEL_CORE24_QUANTIZATION_R2.md): keep Bonsai 27B and one additional model on **one** on-demand 24 GB GPU, with serial loading; independently quantize the 13 already-installed small models on the **always-on CORE24 VPS**. No new GPU or persistent paid storage. Training/quantizing two new students remains a separate future proposal, not the currently authorized resource change.

# SSI V5 — Two Compact Decision Students (R1 Design)

**Date:** 2026-10-17  
**Status:** **PLANNED — NOT TRAINED / NOT QUANTIZED / NOT DEPLOYED**  
**Purpose:** Make real SSI decisions faster and cheaper without replacing SSI's Director, knowledge storage, mission safety constraints, or existing model routes.

## Two independent candidates, one decision contract

| Candidate | Larger model / teacher source | Student objective | Default hardware target | Status |
|---|---|---|---|---|
| **SSI-DECISION-B27-MICRO** | Bonsai 2 27B (`PQ2_0` package R2), plus approved real SSI mission outcomes | Task/routing decisions; target small pretrained student, **~0.5B–3B parameters**, quantized only after training/qualification | Always-on SSI CORE24 VPS (or another measured available local placement) | Planned |
| **SSI-DECISION-200B-LITE** | Operator-reported “200B” model: **exact publisher, model ID, revision, license and access route still unverified** | A stronger, task-specific student, **~7B–8B parameters at Q4-class precision**, subject to measured accuracy and VRAM | One reserved logical model slot on the **24 GB VRAM GPU** server | Planned |

**Other GPU/server resources:** Operator reports three models on another server. Do not move, replace, disable, or copy these models as part of this design. Verify actual GPU allocation, loaded models, concurrency and free VRAM before attempting deployment.

### Critical technical distinction

This is **task-specific distillation or fine-tuning**, **not** “quantize the 200B model directly into 7B”. Quantization reduces numerical precision but does not remove ~96% of a large model's parameters. At one bit per parameter, a dense 200B model alone requires ~25 GB decimal just for parameter bits, before overhead; one-bit inference would need a suitable execution engine and may degrade quality. A usable student is a **different, already-small base model** trained/adjusted using permitted outputs, verified real SSI decisions and task outcomes.

**Possible starting points, not chosen models:** verify compatible open-licensed ~1.5B/3B student for MICRO and ~7B/8B student for LITE. Match to the exact source model's output format and actual available execution libraries. The Bonsai ternary format is specialized; do not assume its GGUF can be fine-tuned using generic LoRA, or that ordinary GGUF quantize produces a useful small decision model.

### Shared typed decision API (proposal)

```json
{
  "mission_id": "<canonical SSI mission id>",
  "task_class": "software_patch",
  "options": ["local_coder", "gpu_coder", "escalate"],
  "decision": "local_coder",
  "confidence": 0.76,
  "reason_codes": ["SUPPORTED_SKILL", "LOW_EXPECTED_COST"],
  "model_id": "<exact trained student revision>",
  "evidence_ref": "<redacted or internal evidence id>"
}
```

The router checks allowed options, access policy, capacity, remaining budget, provider availability and mission requirements **independently**. The decision student **advises**; Director remains the mission owner. On uncertainty or unsupported choice, preserve the existing full-router path and normal fallback behavior.

## Production-only evidence pipeline

1. Real Director/CODEX/Robert mission enters the ordinary authorized execution queue.
2. SSI Router V10 selects a currently eligible model; no extra inference calls for benchmark purposes.
3. Notary and task checkpoints record selected model identity, actual cost/latency/resources, resulting decision and **verified mission outcome**.
4. Keep SSI knowledge and durable memory in microsegments, Research Memory, SCC and the original systems. Do not shift canonical knowledge into a student's weight file.
5. Periodically extract **sanitized and permission-checked** task/decision/outcome pairs. Filter leaked secrets, customer data and proprietary code; remove ambiguous/failed teacher outputs unless reliably labeled as counterexamples.
6. Only when a sufficient usable corpus exists and the original teacher/output terms permit it, train lightweight student adapters (e.g. LoRA/QLoRA where supported by the chosen base model). Training itself runs in a scheduled maintenance window or on separately permitted capacity and **must not interrupt production GPU jobs**.
7. Export/quantize the resulting student only after verifying runtime compatibility. Measure the **real model's full GPU footprint** including runtime, KV cache, batch and concurrency against actual GPU headroom.
8. Deploy **behind a feature flag**: start with passive routing advice if it requires no extra paid model call, then cautious operator-approved promotion after evidence from real mission execution.
9. Publish source provenance, student license, variant hashes, aggregate success/cost/latency, failure conditions and reproducible **sanitized** examples. Do not publicize any private mission data.

### No synthetic model benchmark campaign

All performance data come from actual useful SSI work. No task is executed again by another LLM simply to win a comparison. Historical real outcomes may be re-scored offline **without new LLM inference**. Account for varying task difficulty and selection bias: side-by-side live outcome counts are not automatically apples-to-apples causal comparisons.

### R1 acceptance gates

- [ ] Identify the exact “200B” teacher. Record canonical upstream URL, parameter count, whether MoE/dense, version, output rights and whether it is downloaded or accessed through API.
- [ ] Inspect the 24 GB GPU host: GPU model, total/free VRAM under **production load**, competing model use, scheduling policy, cache/KV reserve.
- [ ] Confirm Bonsai 27B's **actual** weight and inference runtime (GHCR manifest accessibility is already verified, GPU inference not yet verified).
- [ ] Choose two legally usable small student foundation models and explicit adapter licenses.
- [ ] Define decision schema and original SSI mission outcome labels.
- [ ] Capture enough real task records with useful feedback; reject unlabeled successes and inconclusive outcomes.
- [ ] Build initial student training configurations **offline**, without altering deployed models or private SSI repositories.
- [ ] Deploy one candidate on a GPU only if **free VRAM and concurrency policy are verified**.
- [ ] Use real SSI missions to establish strengths, weak cases and “do not use for” rules before making public claims.

## VRAM planning (not hardware measurements)

| Student proposal | Rough Q4 model-weight size | Practical interpretation |
|---|---|---|
| 1.5B–3B student | ~1–2.5 GB | Good low-resource candidate if routing tasks remain simple |
| 7B–8B student | ~4–6 GB | Primary proposed additional model for the 24 GB GPU host |
| 14B student | ~8–11 GB | Optional fallback **only if sufficient real GPU headroom** and accuracy justify it |

Running inference uses additional memory for context, KV cache, runtime, batching and parallel requests. The actual model weights can also be larger than these estimates, depending on architecture and quantization type. A “fourth slot” is not proof that another model will fit concurrently.

**Potential source references:** [Bonsai 27B public container](https://github.com/users/jankes72/packages/container/package/ssi-bonsai27), [Hugging Face bitsandbytes LoRA/QLoRA documentation](https://huggingface.co/docs/transformers/quantization/bitsandbytes). Exact teacher and student URLs remain **PENDING**, and should never be invented.

**Operational principle:** two independent small specialists, one SSI decision contract, existing Router V10 in control; no new always-on GPU and no disruption to the three models on the other server.
