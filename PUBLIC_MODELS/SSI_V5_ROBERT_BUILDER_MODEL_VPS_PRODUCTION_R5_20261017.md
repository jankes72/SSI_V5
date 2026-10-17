> **HOST ASSIGNMENT SUPERSEDED — 2026-10-17:** The owner subsequently clarified that **the first 13 SSI MultiQuant decision-aware variants should be built on the existing 24/7 MODEL VPS**, with strict low-resource, one-at-a-time, non-disruptive controls and a STOP when high-precision weights exceed actual headroom. Robert receives metadata and model-comparison evidence; the **five Robert model slots are future plans only**. Do not execute the Robert-only instructions further down as the current plan. **[Current SSI MultiQuant R7](SSI_MICRO13_DECISION_AWARE_MULTIQ_R7_20261017.md)**. No models were deployed by this correction.

# SSI V5 — Director Offline Micro R5: Robert builds, Model VPS executes

**Decision date:** 2026-10-17  
**Status:** Infrastructure-role decision and private-tooling preparation; **no model quantized, trained, transferred or deployed by this publication**.  
**Supersedes:** [R4 model work on CORE24](SSI_CORE24_CPU_DECISION_MICRO_R4.md) and the CORE24-quantization part of [R2 RunPod/CORE24 plan](SSI_RUNPOD_DUAL_MODEL_CORE24_QUANTIZATION_R2.md).

## Correct allocation of responsibilities

| Server | Operational role | Model-micro work that is permitted |
|---|---|---|
| **SSI DIRECTOR VPS** | Mission planning, routing and authorization, orchestration and evidence policy | Can request builds and later consume model performance metrics; **does not perform model quantization** |
| **SSI ROBERT VPS** | Existing 24/7 4-vCPU/16-GB-RAM CPU-only server, in the user's migration design | **Exclusive build/preparation location:** analyze imported metadata, stage authorized high-precision sources, run compatible CPU quantization (one job at a time if memory allows), create immutable trial weights/checksums, analyze permitted real-mission telemetry |
| **SSI MODEL VPS (24/7)** | Existing 13 Ollama model variants and inference for SSI agents | **No quantization, no distillation or training.** Can export minimal read-only model metadata. **Only approved completed models** are staged and used for genuine SSI work after separate rollout/rollback approval |
| **RunPod GPUs** | Other independent on-demand SSI inference workloads | **Not used** for this micro-model preparation project |

The current source model inventory is still based on **13 reported** model/quantization entries. Exact live tags, hashes and runtime health must be verified. Existing models remain untouched and available. These servers might have independent secondary missions; the builder must yield CPU/RAM to Robert's own high-priority mission processing.

## Operational pipeline

1. **Inventory-only on MODEL VPS:** read local Ollama `/api/tags`, `/api/show` model metadata, and `/api/ps` to identify existing variants and quantization. The inventory includes no model text generation, weights, credentials or proprietary SSI code. Privately and securely pass only required metadata to Robert.
2. **Build preflight on ROBERT:** verify actual host identity, ~4 vCPU / 16 GB RAM (total, not spare), CPU-only, free RAM/disk, existing Robert queue load and permitted source licenses; prevent running jobs on the model VPS or RunPod.
3. **Trial candidate planning on ROBERT:** for each of the 13 reported variants, propose `MICRO` and `NANO` where compatible, recording **exact source revision, architecture, tensor format and source hash**. 13 x 2 = **26 candidate jobs**, not 26 guaranteed results.
4. **One CPU conversion on ROBERT at a time:** require compatible high-precision GGUF and local quantizer; keep old weights untouched and use new immutable names. Q3/Q4 -> Q2 blind requantization is prohibited. Unsupported models (e.g. special System One APIs) receive explicit manual-compatibility holds. If RAM/CPU/disk requirements are not met, **block rather than outsource to RunPod or a paid provider**.
5. **Private artifact handoff:** once a trial file has passed format-integrity validation, operator approves stage/install of the **finished** model on the MODEL VPS. Preserve 13 originals, preexisting production model tags, existing models' residency/scheduling and SSI routing rules. No auto-promote.
6. **Genuine mission evaluation:** existing Director/CODEX/Robert missions use qualified model candidates; Notary records outcome, latency, resource use, errors, task/micro-network profile. No synthetic benchmarking or duplicate paid traffic. Use real evidence with sample counts and selection-bias caveats.
7. **Public model documentation:** publish upstream source, exact approved quantization/model digest, memory and speed measurements and aggregate anonymized **good for / weaker for / avoid for** findings. **Never publish private SSI Router code, micronetwork logic, SCC implementation, raw mission payloads or sensitive server data.**

### Why a large checkpoint cannot always be quantized on Robert

The ROBERT VPS has only ~16 GB **total** system RAM and 4 vCPU and also runs essential services. A quantization input can require more temporary memory and disk than the eventual small output. A trained or distilled 3B model is **not** created by simply calling GGUF quantization on a 27B or 200B teacher. Any job too large for actual Robert headroom remains **BLOCKED_ON_ROBERT_RESOURCES**. No hidden fallback to the model server.

### Private builder (not in this public repository)

The private **SSI_DIRECTOR_OFFLINE_MICRO_R3_ROBERT_BUILD_20261017** toolkit supersedes R2. It separates read-only source inventory from Robert-only build actions, requires explicit operator pinning of the Robert build host, produces disabled jobs by default, and leaves the production model server unchanged. The private ZIP/source must not be uploaded to this public repository.

**One-sentence rule:** **SSI ROBERT prepares; SSI MODEL VPS runs; SSI DIRECTOR decides; evidence calibrates; GitHub reports anonymized findings.**


## First cohort decision (2026-10-17): MICRO-13

The first planned cohort is **one smaller quantization candidate per existing reported MODEL VPS Ollama baseline** (13 proposed additions, **zero completed/installed** at this publication). The prioritized list, System One limitations for D1/Tev1, source-checkpoint requirements, admission policy, and real-mission calibration contract are documented in **[SSI MICRO-13 — paired baseline and candidate selection](SSI_MICRO13_BASELINE_TO_CANDIDATES_R6_20261017.md)**. The corresponding **private** R4 staging toolkit is not published to this repository. A disabled gateway manifest is not proof of model compilation or a live routing integration.
