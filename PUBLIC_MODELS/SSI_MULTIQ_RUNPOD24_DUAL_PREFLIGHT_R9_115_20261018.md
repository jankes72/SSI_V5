# SSI MultiQuant D4 — RunPod 24 GiB dual-resource preflight R9.115

**Prepared:** 2026-10-18. **Status:** `READ_ONLY_TOOL_PREPARED / WAITING_FOR_REAL_RUNPOD_ACCOUNT_RESULT`.

This note supersedes the earlier narrower R9.114 account-inspection scope, **not** its historical audit logs. No GPU has been started, no existing Bonsai model or serverless image changed, no weights downloaded or benchmark run, and no inference-server/Router promotion has occurred.

**Important resource distinction:** The user's 24 GiB GPU resource may be a RunPod **Serverless endpoint**, rather than a persistent RunPod **Pod**. The two REST v2 inventories are disjoint:
- `GET /v2/pods` — Pod allocations, status, nominal disk, GPU class.
- `GET /v2/serverless` — serverless endpoints, GPU pools (including 24 GiB pools), worker scaling and ephemeral container-disk allocations.

An audit of Pods alone cannot prove that a 24 GiB serverless endpoint does not exist. The new private R9.115 toolkit makes GET-only calls to both endpoints, supports pagination and emits sanitized findings. **Locally reproduced tests:** `17/17 PASS` (tool behaviour on synthetic cases, **not** account connectivity).

**Next decision gate:** Determine whether the 24 GiB resource is POD or SERVERLESS_ENDPOINT; inspect the *actual* disk free space, persistence, loaded model placement, cost/worker policy and compatible runtime. A stopped Pod must not be started without budget authorization. A Serverless endpoint cannot be treated as a persistent SSH Pod or safely repurposed by unapproved file writes to ephemeral container storage.

**Tentative same-checkpoint baseline:** `Qwen3.5-35B-A3B-IQ4_XS.gguf` (~19.70 decimal GB published by bartowski; current compatibility and real fit not yet checked), followed by published `IQ2_M` (~12.96 GB) or `IQ2_XS` (~11.69 GB) as CPU 16 GiB comparison candidates. These externally quantized GGUFs are **references**, not results of SSI's own fragment-wise quantizer. Keep the pre-existing Bonsai model intact and load no more than one test model at a time if/when approved.

**Source / limits:** https://docs.runpod.io/api-reference-v2/pods/list-pods · https://docs.runpod.io/api-reference-v2/serverless/list-serverless-endpoints · https://huggingface.co/bartowski/Qwen_Qwen3.5-35B-A3B-GGUF

**SSI-wide MultiControl decision:** [Global architecture R1](../SYSTEM/SSI_MULTICONTROL_GLOBAL_ARCHITECTURE_DECISION_R1_20261018.md): global read-only-by-default control service, not MultiQuant-owned, status `PLANNED / GLOBAL_SSI / SHADOW_ONLY`.

**Current real account state:** `UNKNOWN`. No use of RunPod credentials or local machine access is claimed by this public note.


## Operator R9.115 account-inventory evidence and R9.116 next gate — 2026-10-18

**Observed directly in operator-provided sanitized MSI stdout**, not by live account access in this publication:
- R9.115 completed read-only `GET /v2/pods` and `GET /v2/serverless`. **No GPU started; no model downloaded.**
- One **A40 48 GiB Pod**, declared container disk **30 GB**, status `EXITED`. **Excluded by operator** from this experiment.
- Five Serverless endpoints, two with a **possible 24 GiB pool**: **ordinal #1** declares **40 GB container disk**, `workersMin=0`, `workersMax=0`; **ordinal #5** declares **30 GB container disk**, `workersMin=0`, `workersMax=1`. Ordinals are relative to that particular API response, **not stable endpoint identities**. Other endpoints advertise 48 GiB pool classes and are excluded from this experiment.
- **No network volumes were reported for either 24 GiB endpoint**. Neither image contents, loaded Bonsai weights nor **actually free internal disk** were checked. Max worker count does not prove any worker is currently running or available.
- The 19.70 GB published Qwen3.5-35B-A3B IQ4_XS file plus **historically referenced, but not currently verified installed** 7.21 GB Bonsai weights totals **26.91 GB**, excluding OS/container, libraries, KV caches, logs, temporary staging and image layers. A 30 GB configured disk would nominally leave **3.09 GB** for everything else and is **not approved for same-container staging based on this arithmetic**; a 40 GB allocation remains unverified as well.
- **R9.116 prepared** to read only `GET /v2/serverless` and report sanitized **image-family clues and hashed image-reference fingerprints** for the two 24 GiB entries. New R9.116 utility passed **22/22 synthetic local tests**, but **has not yet been run against the user's live account**, and no stored-model detection is claimed.

**Current gate**: `WAITING_FOR_24GB_IMAGE_IDENTITY_AND_REAL_FREE_DISK`. No production changes, no RunPod GPU billing authorized by the R9.115/R9.116 read-only steps. The SSI-wide MultiControl ownership decision remains `PLANNED / GLOBAL_SSI / SHADOW_ONLY`; the audit does not imply an operational native SCC binding.


## Dashboard identification of 24 GiB endpoints — operator screenshot text, 2026-10-18

A subsequent **operator-provided RunPod dashboard excerpt** resolves the *display-name* identities of the two 24 GiB Serverless entries from the earlier account inventory. No live GPU start or endpoint API request was made by this publication:

| 24 GiB endpoint | Allocated container disk (prior API inventory) | Worker settings (prior API inventory) | Evidence scope |
| --- | --- | --- | --- |
| `SSI-BONSAI2-27B` | 40 GB | min=0; max=0 | Endpoint **name** indicates Bonsai 27B. Does **not** prove weights exist inside the image; scaling currently disabled. |
| `ssi-qwen38-27b-flex-r1` | 30 GB | min=0; max=1 | Endpoint **name** indicates Qwen 27B Flex. Model checkpoint/revision, quant, actual loaded weights, GPU and internal free disk remain unverified. |

The screenshot labels **0/1 Running**, **0 Queued**, **1 Idle** on the 24 GiB Qwen endpoint and **0/0 Running**, **0 Queued**, **0 Idle** on Bonsai. Dashboard caption **"Running" is a counter label**, not evidence that active inference is occurring. RunPod's 2026-10-15 Serverless pricing documentation explicitly states that a **scaled-down worker shown as Idle in the console is not billed for GPU compute**. GPU compute billing covers startup, execution and pre-scale-down waiting; container disk/storage charges can remain separate. Inspect health and actual billing metrics rather than interpreting the dashboard's 'Idle' counter as a live billed worker. Source: RunPod Serverless billing documentation, https://docs.runpod.io/serverless/pricing.

**Current decision:** two existing endpoint identities are known, but the real image contents, snapshot/disk occupancy, exact Qwen 27B checkpoint, and possibility of adding a third model have **not** been verified. Preserve **both** existing endpoint configurations. Evaluate an existing 27B baseline *first*, subject to separately authorized billed requests; only then decide whether Qwen3.5-35B-A3B IQ4_XS deserves a separately versioned image deployment. R9.116 remains **read-only image-definition preflight**; status `WAITING_FOR_IMAGE_CONTENT_AND_REAL_FREE_DISK`. All 48 GiB endpoints and the stopped A40 Pod are excluded.


## Operator-executed R9.116 image-identity audit (2026-10-18)

**Operator-provided real MSI run:** archive `SHA256SUMS.txt` verification reported `DOBRZE` for 5/5 files; `bash TEST_OFFLINE.sh` gave **22/22 PASS**. The only remote operation in `01_SERVERLESS_24GB_IMAGE_PREFLIGHT.py` was **GET /v2/serverless**; no GPU start, inference, download or endpoint mutation.

| Endpoint (operator dashboard display name; do not publish IDs) | GPU pool metadata | Disk allocated | Workers min/max | Image reference SHA256 prefix | Image/environment model hints | Real weights verified |
| --- | --- | ---: | --- | --- | --- | --- |
| `SSI-BONSAI2-27B` | `ADA_24` | 40 GB | 0/0 | `5ecfc965db3d` | `BONSAI` | **NO** |
| `ssi-qwen38-27b-flex-r1` | `AMPERE_24` | 30 GB | 0/1 | `143fc5c9fa1d` | none found in inspected image/model env fields | **NO** |

The different model-hint results cannot prove that Qwen weights are missing: no container image was inspected or inference performed. These are endpoint-template fingerprints, **not weights SHA256**. `gpu_pool_24_codes` are RunPod GPU pool class codes and cannot be interpreted as measured available CUDA VRAM.

**Remaining blockers:** actual Qwen checkpoint, handler input/output schema, available runtime GPU memory, stored model provenance, container free disk, actual worker health and any per-second idle expense are not verified. Do not claim successful installation, model quality or 35B headroom. **Next safe step:** authenticated read-only **GET /v2/{endpoint_id}/health** for the *two* existing 24 GiB Serverless endpoints (documented by RunPod), then request separately cost-authorized minimal model inference with the actual handler contract. No /run or /runsync was called in R9.116.

**Current gate:** `R9_116_ACCOUNT_IMAGE_PREFLIGHT_PASS / RUNTIME_MODEL_UNVERIFIED`; `WAITING_FOR_ENDPOINT_HEALTH_AND_HANDLER_CONTRACT`.


## Operator-provided R9.117 health gate and existing GitHub provenance — 2026-10-18

**Scope:** operator executed two authenticated, read-only `GET /health` requests on the **existing** two 24 GiB Serverless endpoints. Neither endpoint was modified; no `/run`, `/runsync`, model download or new GPU job was submitted by the audit.

| Existing endpoint | Health request | Workers running | Workers idle | Jobs in progress | Jobs queued | Jobs completed | Jobs failed |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `ssi-qwen38-27b-flex-r1` | RECEIVED | 0 | 1 | 0 | 0 | **2** | **0** |
| `SSI-BONSAI2-27B` | RECEIVED | 0 | 0 | 0 | 0 | **0** | **0** |

**Evidence interpretation:** `GET /health` proves endpoint health API availability and reports counters, **not** that either model's real weights loaded, two correct inferences occurred, the model identity is correct, or model output quality passed. The lifetime/context of the `completed` counter was not examined. The `idle` worker count does not itself prove a billed warm worker. No actual VRAM or container free disk readings were made.

**GitHub provenance cross-check:** [SSI model catalog](SSI_V5_MODEL_CATALOG_AND_LIVE_ROUTING.md) already lists Qwen 27B **`SOURCE_PENDING`** and Bonsai 27B R2 with the public pinned GHCR manifest `sha256:d60d0caafcffde6aa783a351273ea43b5ee0a5e0948a036c785616ba77b90d48` from [Bonsai deployment R2](SSI_BONSAI_2_27B_R2.md). It does **not** provide a Qwen 27B exact checkpoint, quantization, model-handler contract or verified prior inference payload. The repository documents plans for an optional Qwen3.5-35B-A3B comparison, but this model was **not** installed by R9.117.

**Next gate:** determine Qwen's exact source revision, container/handler build and permitted request/response schema, preferably from archived build manifests, Dockerfiles and private logs on MSI without activating GPU; preserve private details. Then request explicit cost approval if a **single** narrowly bounded real inference is still necessary. Never overwrite Bonsai, Qwen or their endpoint settings. The 48 GiB resources remain excluded.

**Status:** `R9_117_HEALTH_READ_ONLY_PASS / QWEN_MODEL_RUNTIME_UNVERIFIED / WAITING_FOR_HANDLER_AND_PROVENANCE`.
