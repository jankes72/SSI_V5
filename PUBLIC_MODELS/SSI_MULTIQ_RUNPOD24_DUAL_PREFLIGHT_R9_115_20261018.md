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
