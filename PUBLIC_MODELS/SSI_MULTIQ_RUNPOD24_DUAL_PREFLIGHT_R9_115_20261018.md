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
