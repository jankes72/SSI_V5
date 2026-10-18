# SSI MultiQuant R9.126 — original Qwen3.5-9B BF16 reproducible reference

Date: 2026-10-18. **Status: BUILD/PUBLICATION PENDING, GPU INFERENCE NOT TESTED.** This page documents preparation and release gates, not a claim of successful deployment. Proprietary SSI runtime, Router V10, queue, credentials, datasets and micro-networks remain private.

## Existing evidence

- **Official model:** [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B), Apache-2.0, pinned upstream revision `c202236235762e1c871ad0ccb60c8ee5ba337b9a`.
- **MSI checkpoint:** Operator physically downloaded and checked **4/4 Safetensors shards, total 19,306,310,880 bytes**; header inventory counted 727 BF16 and 48 F32 tensors. This is an **original unquantized** checkpoint (not a low-bit student). No GPU inference implied.
- **Bonsai GHCR image:** `ghcr.io/jankes72/ssi-bonsai27:r2` — public manifest observed in earlier evidence, actual GPU inference **not verified**. Its 40 GB disk RunPod endpoint and private configuration backup are preserved.
- **R9.125 dual-model worker:** 28/28 synthetic/offline unit tests PASS; Docker build on MSI failed at container Ubuntu APT network download stage. No successful Docker/GPU inference, no runtime fit evidence.

## R9.126 private builder handoff

Archive supplied privately to the operator: `SSI_MULTIQ_QWEN9B_BF16_GHCR_BASELINE_R9_126_20261018.zip`. **16/16 local offline unit tests PASS**; no full image built and no image pushed. It prepares a **standalone baseline worker**, rather than a replacement for SSI queue or the unverified dual-runtime hot-switch. Clean public-model-only source uses vLLM v0.17.0 pinned Docker image digest, RunPod SDK v1.12.0, text-only mode and source weights pinned to exact Qwen upstream commit. No private SSI code or mission content is included.

Two **proposed, not existing** GHCR tags under the same namespace as Bonsai:

- `ghcr.io/jankes72/ssi-qwen35-9b-bf16:r1-full-candidate` — optional FULL baked original ~19.3 GB weights; four layers separately, to respect GitHub Container Registry 10 GB **per layer** rule. Requires isolated builder with **>=90 GB** free Docker storage, plus time and publication credentials. Runtime/40GB-disk fit **unverified**. Block push for RunPod 40 GB deployment if local unpacked image size >=32 GB, leaving provisional 8 GB runtime headroom. Even <32GB is **not** GPU-fit proof.
- `ghcr.io/jankes72/ssi-qwen35-9b-bf16:r1-thin-candidate` — full runtime/handler **without** embedded weights; pinned official upstream checkpoint would download at cold start. Downloading 19.3 GB each cold start may be impractical without compatible RunPod model caching, which needs independent validation.

GHCR also has a 10-minute per-layer upload timeout, so a full image may fail cloud publication despite four sub-10GB layers. Initial visibility is generally **private**; only mark public after verifying image contents, upstream attribution/license and actual artifact digest. Never overwrite the existing Bonsai tag or change the public SSI code policy just to build a container.

## Evidence-based comparisons — no fictional quality scores

The primary **Qwen3.5-9B BF16 original** vs **SSI quantized derivative of this same pinned 9B checkpoint** will compare only verified, anonymized actual authorized SSI missions. Groups: Director planning/recovery, SSI CODEX coding/tests, Robert text summaries/classification, multilingual PL/EN/ES/DE/FR, instruction-following and context quality. Store paired hashed mission IDs and user-reviewed rubric results (0..1), exact quantization/hardware/context settings, latency, output tokens, memory and real spend; private supporting inputs/outputs do **not** enter public GitHub. Different CPU/GPU hardware confounds latency and VRAM comparisons: report hardware-specific speed/cost separately. A 1.5B quantized Qwen model or Bonsai27B is a **cross-model** comparison, not proof of low-bit loss from this 9B baseline.

Initial result grid:

| Subject | Checkpoint verified | Image published | GPU quality measured | Strengths | Weaknesses |
|---|---|---|---|---|---|
| Qwen3.5-9B original BF16 | YES, operator 4/4 SHA-256 | **NO** | **NO** | NOT TESTED | NOT TESTED |
| Same 9B quantized derivative | NO (candidate pending) | **NO** | **NO** | NOT TESTED | NOT TESTED |
| Bonsai2-27B PQ2_0 | Original model source referenced, GHCR R2 manifest observed | R2 manifest yes | **NO** | NOT TESTED | NOT TESTED |

**Next gate:** isolated build host, pinned full image build/upload, record GHCR immutable digest and real unpacked image size, verify 24GB VRAM and 40GB ephemeral disk during a controlled RunPod job, then gather natural SSI mission evidence. Separate image tags do **not** implement two models hot-swapping in one already-running container. Existing mission queue and Router V10 stay unchanged.

Refs: [Qwen official repository](https://huggingface.co/Qwen/Qwen3.5-9B/tree/c202236235762e1c871ad0ccb60c8ee5ba337b9a), [vLLM Qwen3.5-9B recipe](https://github.com/vllm-project/recipes/blob/main/models/Qwen/Qwen3.5-9B.yaml), [GHCR official limits](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry), [SSI Bonsai R2 record](SSI_BONSAI_2_27B_R2.md), [RunPod R9.115–R9.125 operator evidence](SSI_MULTIQ_RUNPOD24_DUAL_PREFLIGHT_R9_115_20261018.md).
