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


## R9.118 operator decision — replace 24 GiB Bonsai endpoint's model with a pinned Qwen 35B baseline (2026-10-18)

**Approved target change, NOT execution evidence:** The operator decided to **retire Bonsai as the deployed model on the existing 24 GiB/40 GB `ADA_24` Serverless endpoint**, replacing its experimental workload with a **single, version-pinned Qwen3.5-35B-A3B IQ4_XS reference** (~19.70 GB published GGUF). Existing Qwen 27B Flex on a *different* 24 GiB/30 GB endpoint and all 48 GiB resources must remain untouched.

**Model selection rationale:** A 35B MoE model is large enough for high-capacity 24 GiB GPU evaluation and also has a feasible *but quality- and CPU-performance-unverified* direct low-bit comparison on 16 GiB RAM: `IQ2_M` ~12.96 GB or `IQ2_XS` ~11.69 GB. It is **not** asserted to be the mathematically largest possible model that could fit 24 GiB at any quantization; larger 70B+ low-bit models are excluded at this gate because they do not yield a defensible direct-on-16-GiB same-model comparison with runtime and quality margin. GPU *VRAM* and container-disk capacity are separate budgets.

**Safe transition:** Back up **private** endpoint configuration locally with mode 0600 and preserve `ghcr.io/jankes72/ssi-bonsai27:r2` and its historical GHCR digest. Do not delete the RunPod endpoint (deletion can discard job history). Stage a **new image/tag** containing *only* `Qwen3.5-35B-A3B-IQ4_XS.gguf` with its exact HF repo commit and LFS SHA256 verified. Verify actual GPU fit, startup and disk usage before permitting billable inference; preserve reversible configuration. The multi-quant Hugging Face repository must **not** be installed via RunPod's unfiltered model caching because it can fetch all variant files. Deployed `Bonsai` image and checkpoint are historical reference only, **not the new quantization source**.

**Research integrity:** The Qwen IQ4_XS GGUF is a third-party reference, not SSI's own quantizer output. Any new SSI native quantization, fragment processing or distillation must preserve provenance to higher-precision source weights outside this 40 GB temporary container. Comparing IQ4_XS vs IQ2_M from the **same Qwen checkpoint** is an initial *published-quantization control*, not proof of SSI algorithmic advantage. The authoritative global MultiControl ownership decision still applies.

**Private R9.118 tooling prepared:** read-only backup script, exact HF GGUF/revision/LFS-source pin checker, guarded build-command generator, *unbuilt* one-GGUF RunPod worker Docker draft, and a billable test requiring explicit separate arming. **26/26 synthetic offline tests passed**. Neither backup/HF scripts nor worker image were executed on MSI or RunPod by this documentation update; no model downloaded, GPU started, endpoint changed, or old image deleted.

**Status:** `OPERATOR_REPLACEMENT_APPROVED / R9_118_PREPARED / NO_RUNPOD_MUTATION / WAITING_FOR_BACKUP_SOURCE_PIN_BUILD_GPU_FIT`.

Sources: https://huggingface.co/Qwen/Qwen3.5-35B-A3B ; https://huggingface.co/bartowski/Qwen_Qwen3.5-35B-A3B-GGUF ; https://docs.runpod.io/serverless/endpoints/model-caching ; https://docs.runpod.io/serverless/endpoints/overview .


## R9.119 — revised baseline: unquantized Qwen3.5-9B BF16 (operator decision) — 2026-10-18

**LATEST OPERATOR DECISION; supersedes R9.118 model choice only.** Preserve historic R9.118 acceptance notes and no-production-change claims. Use the **official unquantized `Qwen/Qwen3.5-9B` BF16 checkpoint** as the **first executable same-model quantization reference** on the **existing 24 GiB Serverless GPU endpoint formerly assigned to Bonsai (40 GB container disk allocation)**; retain Bonsai's GHCR R2 image digest, endpoint rollback settings, historical logs and separate Qwen 27B 24 GiB/30 GB endpoint. The earlier Qwen3.5-35B-A3B IQ4_XS image plan is **not authorized as current first rollout**. 35B+ is a future fragment-processing direction, not the first raw BF16 GPU baseline.

Published `Qwen3.5-9B` BF16 GGUF variant is ~18.4 decimal GB; official Transformers safetensors BF16 checkpoint is the source of truth for SSI quantization, not a pre-quantized GGUF. The 24 GiB-class card **may fit for short context, one concurrent request**, but GPU runtime/KV/vision allocations, model revision, effective GPU memory and real disk free are **NOT MEASURED**. The nominal 40 GB Serverless container disk may still be too small if model files are duplicated in Docker layers, downloaded again on worker start or staging data remains; no permanent network volume is configured. Use SHA-pinned staged downloads, bounded disk budgeting and a new reversible image tag, not mutation or deletion of Bonsai image.

Research plan: record unquantized BF16 output/latency/mission quality first, then independently produce Q8/Q6/Q4/Q3/Q2 candidate variants from that exact source checkpoint and compare on held-out SSI mission evidence. Qualify any 16 GiB RAM CPU variant **only after measured RAM/CPU/quality**, and do not assume quantization shrinks parameter count. Global LEGO MultiControl remains planned/read-only shadow. No paid GPU start, image build/deployment, downloads, testing, Champion promotion or changes to production are documented here.

**Status:** `R9_119_DECISION_RECORDED / UNQUANTIZED_BF16_REFERENCE_SELECTED / INSTALLATION_PENDING / GPU_FIT_UNVERIFIED`.

Official model: https://huggingface.co/Qwen/Qwen3.5-9B ; public GGUF BF16 size reference: https://huggingface.co/bartowski/Qwen_Qwen3.5-9B-GGUF .

## R9.120 — implement original Qwen3.5-9B BF16 using existing SSI queue, keep Bonsai (2026-10-18)

**Latest operator clarification:** Implement **only the official unquantized `Qwen/Qwen3.5-9B` Safetensors/BF16** as the first MultiQuant baseline. Do **not** download/deploy Qwen35B IQ4, and do **not** create a new GPU task queue or router. Keep the existing SSI queue, Router V10 and user requirement of **one VRAM-loaded model at a time per 24 GB GPU**. Preserve Bonsai 2 27B and the separate Qwen 27B Flex endpoint until actual 40 GB container-image/handler compatibility has been checked. This third logical model is **not evidence of a third physical GPU**.

**R9.120 private execution package prepared:** `SSI_MULTIQ_QWEN35_9B_BF16_R9_120_20261018.zip` (provided privately to the operator, not published in this repository). Contains: (1) read-only HF official checkpoint revision + exact size inspection, (2) guarded GET-only RunPod Bonsai endpoint inventory and **private 0600 backup**, (3) file-name inventory of existing SSI queue/installers under `~/SSI_V5` and `~/Pobrane`, (4) explicitly armed ~19 GB original BF16 MSI-only download with LFS checks, and (5) Safetensors header dtype verification. Software unit tests **20/20 PASS locally**, source syntax and SHA256 manifest verified. **No RunPod endpoint changed, no GPU started, no Qwen weights downloaded by the assistant.**

**Critical gate:** the 40 GB Serverless allocation is *container disk*, not free storage and not VRAM. Keeping Bonsai and Qwen9B physically in one worker image is **NOT VERIFIED**: heavyweight runtimes, CUDA layers, Docker layers and conversion staging may exceed 40 GB. Serverless scratch is ephemeral. Before any deploy, inspect the existing worker handler and Docker image, then reuse the current model-selection/queue protocol (no synthetic replacement), prepare reversible versioned image only if actual container fit and Qwen3.5 compatibility are established. Otherwise explicitly report blocked without deleting Bonsai. A 24 GiB GPU may fit the 9B BF16 short-context text model, but real inference VRAM remains unmeasured.

**State:** `R9_120_PRIVATE_TOOLKIT_READY / ORIGINAL_BF16_SELECTED / MODEL_DOWNLOAD_OPERATOR_GATED / RUNPOD_DEPLOYMENT_PENDING`.

Source: https://huggingface.co/Qwen/Qwen3.5-9B ; https://docs.runpod.io/serverless/endpoints/overview .


## R9.121 — operator R9.120 failures and non-destructive source-pin repair (2026-10-18)

**User-provided MSI log:** R9.120 `sha256sum -c` passed for the ten original package files; `TEST_OFFLINE.sh` was **20/20 PASS**. Read-only preflight `01_PREFLIGHT_BF16_AND_BONSAI.py` stopped with a collapsed `HTTPERROR`, so the required `~/.local/share/ssi_multiquant/r9120_qwen9b/CURRENT_PIN.json` was never written. Authorized download `02_DOWNLOAD_ORIGINAL_BF16.py`, stage check `04_VALIDATE_STAGE.py`, and Safetensors dtype check `05_VERIFY_BF16_TENSORS.py` consequently stopped with `FILENOTFOUNDERROR`. **No model weights were downloaded and neither RunPod nor SSI queue was changed.**

**Independent code defect:** The original R9.120 synthetic fixture expected `model-00001-of-00002.safetensors`, but official Qwen3.5-9B actually publishes `model.safetensors-00001-of-00004.safetensors` etc. (four shards, 19,306,310,880 bytes historically observed). Its original `extract_manifest` requires `model-` prefix or singular `model.safetensors`, so it would reject real four-shard filenames even if the HTTP request succeeded. The original code also made source pinning depend unnecessarily on RunPod endpoint metadata.

**R9.121 private patch (operator handoff):** `SSI_MULTIQ_QWEN9B_PIN_FIX_R9_121_20261018.zip` adds an independent, GET-only Hugging Face source pinner `06_R9121_RECOVER_PIN.py` using the real shard naming and pinned SHA, and independent GET-only Bonsai endpoint private backup `07_R9121_RUNPOD_BACKUP_READONLY.py`. The latter may fail without blocking the former. Error reports now preserve the failing **phase** and sanitized HTTP status code, without leaking credentials, private endpoint configuration or raw API responses. The patch adds **8/8 offline test PASS** and checks sha256 for its own artifacts. It does not overwrite R9.120. Existing R9.120 authorized 19 GB MSI downloader/validators are reused after the new pinned manifest exists.

**Operational limits:** RunPod private backup is still required before *any actual image update*; staging on MSI is not deploying a model. Do not start GPU workers, delete Bonsai, or alter existing SSI mission queue during source recovery. `Qwen/Qwen3.5-9B` remains selected but GPU fit, dual-runtime/disk fit, and real inference quality have not yet been demonstrated.

**Status:** `R9_120_FAILURE_DIAGNOSED / R9_121_OFFLINE_8_OF_8_PASS / SOURCE_PIN_RETRY_PENDING / NO_GPU_OR_RUNPOD_MUTATIONS`.

## R9.122 — verified original Qwen3.5-9B source staged on MSI (operator log, 2026-10-18)

**REAL OPERATOR SUCCESS; no GPU inference claimed.** On MSI `jankes72-GV62-8RE`, operator ran R9.120 `02_DOWNLOAD_ORIGINAL_BF16.py`, `04_VALIDATE_STAGE.py`, and `05_VERIFY_BF16_TENSORS.py` after R9.121 source-pin repair. Hugging Face downloaded the official **unquantized `Qwen/Qwen3.5-9B`** at pinned commit **`c202236235762e1c871ad0ccb60c8ee5ba337b9a`**, staged under `~/SSI_MULTIQ_MODELS/Qwen3.5-9B-BF16-c20223623576`. The **4/4 Safetensors weight shards** total **19.306 decimal GB**, with **4/4 SHA-256 verified**. Header inspection counted **727 BF16 and 48 F32 tensors** (mixed unquantized tensor dtypes are not low-bit quantization). The scripts reported `ORIGINAL_MODEL_STAGED_ON_MSI`, `WEIGHT_SHARDS_PRESENT`, and `UNQUANTIZED_BF16_SOURCE_HEADERS_VERIFIED`, respectively.

**Boundaries:** This is valid checkpoint/source-integrity evidence; **no actual model inference or accuracy benchmark** was performed, GPU use = 0, RunPod image built = false, endpoint modified = false. Neither a dual-model 40 GB Serverless image nor a reversible deployment was built. The separate Qwen 27B endpoint and Bonsai remain untouched; the existing SSI queue is the required integration path, not a new implementation.

**Next gate:** read-only **Bonsai configuration backup** using `07_R9121_RUNPOD_BACKUP_READONLY.py` (if not already recorded) and static inventory of the existing private RunPod MSI installer/source archive(s) and actual handler. Confirm runtime compatibility, disk image size and reversible rollout before any RunPod modification or billed GPU run. Do not download the ~19.3 GB source weights again; reuse the verified MSI files.

**Status:** `R9_122_REAL_BF16_SOURCE_STAGED_AND_SHA_VERIFIED / GPU_DEPLOYMENT_PENDING`.



## R9.123 — Bonsai endpoint backup confirmed, original SSI worker archives located (operator MSI output, 2026-10-18)

**Verified actual operator log:** `07_R9121_RUNPOD_BACKUP_READONLY.py` returned `BONSAI_BACKUP_OK` for existing Bonsai `ADA_24` GPU pool, **40 GB allocated container disk**, workers min/max **0/0**, `backup_stored_private=true`, **0 GPU jobs**, **0 remote mutations**. Private backup is on the MSI and must not be published. The baseline source directory `~/SSI_MULTIQ_MODELS/Qwen3.5-9B-BF16-c20223623576` was confirmed to exist with **4 Safetensors files** (previously independently SHA-256 verified).

**Existing source/installer discovery, not duplicate implementation:**

- `~/Pobrane/SSI_BONSAI27_RUNPOD_SERVERLESS_R1_20261017.zip` contains existing `worker.py`, `contract.py`, `Dockerfile`, `requirements.txt`, `README_PL.md` and worker contract tests.
- `~/Pobrane/SSI_RUNPOD_SERVERLESS_MSI_R1_20261015.zip` contains the existing MSI-side RunPod adapter `install.py`, `payload/ssi_runpod_llm/client.py`, `native.py`, `validation.py`, plus tests and historical evidence.
- `~/Pobrane/SSI_RUNPOD_MSI_ZRODLA_20261016T063951Z_c79e74_PRIVATE.zip` and `...T064012Z_ba806f_PRIVATE.zip` contain `sources/ROOT/SSI_MODULES/SSI_UNIVERSAL_CONTROL_V1/worker.py`.
- `~/Pobrane/SSI_GPU_QWEN38_GOTOWE_20261015.zip` includes historical model metadata. **These file-name-only discoveries do not prove that an installed runtime already supports Qwen3.5-9B or a dual-format model switch.** Nothing was modified.

**R9.123 private artifact prepared:** `SSI_MULTIQ_R9_123_REUSE_RUNPOD_20261018.zip` reads only selected members of the above local archive ZIPs, uses Python AST static signatures, emits redacted metadata (file hashes/sizes, function names, Dockerfile instruction counts, boolean model/queue/runtime feature indicators) and runs **8/8 local synthetic offline tests**. No credentials, source code, raw configs, GPU job requests, installation or remote mutations are included.

**Next gate:** run read-only R9.123 archive inspection on MSI; identify existing RunPod worker/queue entrypoints and actual runtime constraints. Reuse the existing SSI mission queue, **one VRAM-loaded model at a time**, and **never overwrite or delete Bonsai until a verified, reversible versioned image fits 40 GB container disk**. Preserve the separate Qwen27B endpoint.

**Status:** `R9_123_BONSAI_BACKUP_OK / BF16_4_SHARDS_PRESENT / EXISTING_INSTALLER_DISCOVERED / WORKER_CONTRACT_INSPECTION_PENDING / NO_GPU_CHANGE`.


## R9.123 actual MSI static ZIP audit — 2026-10-18

**Operator evidence from R9.123, not inference:** package `sha256sum -c` passed; **8/8 offline tests PASS**. Source checkpoint `Qwen/Qwen3.5-9B` pinned `c202236235762e1c871ad0ccb60c8ee5ba337b9a`: **4 shards / 19,306,310,880 bytes**, index/config/pin found, MSI free disk measured **164.49 decimal GB**; **3 private Bonsai backups** found. All five input ZIPs passed integrity checks. `gpu_jobs=0`, `runpod_api_requests=0`, `remote_modifications=0`.

**Critical integration discovery:** Existing Bonsai R1 `worker.py` and `Dockerfile` show PrismML/llama.cpp and RunPod serverless; both static scanners reported **no Qwen-support or multi-model selection/sequential unload**. `contract.py` has `create_chat_payload`/`normalize_chat_response`, and the worker has `handler`, `ensure_started`, `_post_completion`. Existing Bonsai `requirements.txt` lists only `huggingface_hub` and `runpod`. MSI adapter R1 already has `RunpodLLM`, `NativeAdapter`, `RequestValidation`, mission/queue references and an `install.py` with `rollback`, but static inspection did **not** prove a ready dual-model handler or actual queue behavior in production. The similarly named `SSI_UNIVERSAL_CONTROL_V1/worker.py` is a distinct SSI control component; do not confuse it with the GPU inference `worker.py`.

**Implementation requirement:** Reuse existing queue and contracts (no new queue), maintain model-request serialization and strict teardown before second model loads, preserve single GPU-loaded model. Qwen3.5-9B BF16 requires a model-architecture-compatible runtime not present in Bonsai's archived requirements; cannot safely claim drop-in compatibility. A 40 GB allocated container disk is not verified free space and heavy extra CUDA/Transformers layers may exceed the budget. The archived Dockerfile and worker source must be reviewed **as code** before deriving minimal patch; a filename/static-signal audit is insufficient. Private source archives remain on MSI and must not be pushed publicly. Official RunPod Cached Models docs (last modified Aug 7 2026) still state one cached model per endpoint and cached-model paths require custom worker integration.

**Next step:** receive only the existing 10 KB Bonsai Serverless ZIP and 109 KB SSI MSI adapter ZIP (or minimally scoped source extract) for precise compatibility diff and guarded, reversible image build with preserved Bonsai; no weights, tokens, or endpoint backup should be uploaded. Status `R9_123_REAL_STATIC_PASS / HANDLER_PATCH_REQUIRED / SOURCE_CODE_REVIEW_PENDING / NO_RUNPOD_CHANGES`.
