# SSI V5 — Public Model Sources, Exact Variants & Real-Mission Calibration

**Status:** Living public index · **First edition:** 2026-10-17  
**Scope:** Model and variant references used or prepared for SSI V5, plus evidence-based guidance for end users.  
**Related release:** [SSI Bonsai 2 27B R2](SSI_BONSAI_2_27B_R2.md) · [GHCR image](https://github.com/users/jankes72/packages/container/package/ssi-bonsai27)

> **Important distinction:** The links below are **verified public upstream model pages or provider catalogs**, NOT proof of the exact URL originally downloaded by SSI. The operator's earlier inventory reports installed model families, approximate quantizations and sizes, but most **installed tag/digest/file revision details remain to be extracted from the real runtime**. Do not infer an exact installed build from a similar model page.

## The promise to readers

For **every model variant**, we intend to publish:
1. The **official source link** and author, together with the exact download page or API route used by SSI once verified.
2. The **actual SSI model ID**, **release/revision**, **quantization format** (e.g. Q3_K_M, Q4_K_M, Q8_0, PQ2_0, FP16), file or Ollama manifest digest when available.
3. The **execution route** (VPS Ollama, RunPod image/endpoint, external API), plus actual tested CPU/RAM/GPU/VRAM characteristics.
4. **Best uses, weaker uses, and uses to avoid**, derived from anonymized, verified **real SSI tasks** rather than promotional assertions or stand-alone tests.
5. Measured outcome, latency, error modes, actual cost per successful task, evidence count, last observation date and uncertainty.

**There are NO invented scores or completed comparisons in this index.** In the tables, *Intended domain* describes upstream specialization or expected role, **not** a measured SSI result. No quantization applies to remote API calls unless the API provider explicitly reports it.

### Evidence labels

- **OPERATOR_REPORTED:** Previous SSI installation/run report; real inventory/immutable digest may still be missing.
- **UPSTREAM_VERIFIED:** Official publisher/catalog link confirmed; not necessarily the source of SSI's specific local files.
- **RUNTIME_VERIFIED:** Exact model ID and digest obtained from SSI's active runtime or build manifest.
- **MISSION_VERIFIED:** Real mission result backed by evidence and reviewed.
- **SOURCE_PENDING:** Public model family known, exact original download URL/quantization unknown.

## A. SSI CORE24 — 13 reported installed variants (24/7 VPS)

The following **13 entries** come from the operator's SSI CORE24 installation report. Sizes and quantization bands are *reported*, not fresh host measurements. The specific tags shown under **upstream candidates** are helpful for locating the model, **not assertions about the exact file SSI downloaded**.

| # | Reported variant / size | Public upstream source (and possible tag) | Exact installed tag / digest | Intended domain (NOT a ranking) |
|---|---|---|---|---|
| 1 | Hermes 3B, Q4; ~2.0 GB | [Ollama Hermes3 3B](https://ollama.com/library/hermes3:3b) | PENDING | General dialogue, tool-oriented assistance |
| 2 | Hermes 8B, Q4; ~4.9 GB | [Ollama Hermes3 8B](https://ollama.com/library/hermes3:8b) | PENDING | General dialogue and agent workflows |
| 3 | Qwen2.5-Coder 1.5B, Q4; ~986 MB | [Ollama Qwen2.5-Coder 1.5B](https://ollama.com/library/qwen2.5-coder:1.5b) | PENDING | Small code edits, autocomplete candidates |
| 4 | Qwen2.5-Coder 3B, Q4; ~1.9 GB | [Ollama Qwen2.5-Coder 3B](https://ollama.com/library/qwen2.5-coder:3b) | PENDING | Coding tasks and local code assistance |
| 5 | Qwen2.5-Coder 7B, Q4; ~4.7 GB | [Ollama Qwen2.5-Coder 7B](https://ollama.com/library/qwen2.5-coder:7b) | PENDING | Code generation, repair and analysis |
| 6 | Qwen3 1.7B, Q4; ~1.4 GB | [Ollama Qwen3 1.7B](https://ollama.com/library/qwen3:1.7b) | PENDING | Small general inference tasks |
| 7 | Qwen2.5-Coder 7B, Q3; ~3.8 GB | [Ollama Qwen2.5-Coder Q3 variants](https://ollama.com/library/qwen2.5-coder/tags) (e.g. [7B Instruct Q3_K_M](https://ollama.com/library/qwen2.5-coder:7b-instruct-q3_K_M)) | PENDING — Q3 subtype unverified | Code with a reduced memory footprint |
| 8 | Hermes 8B, Q3; ~4.0 GB | [Ollama Hermes3 quantized tags](https://ollama.com/library/hermes3/tags) | PENDING — Q3 subtype unverified | General assistant under tighter memory |
| 9 | DeepSeek-Coder 6.7B, Q4; ~4.1 GB | [Ollama DeepSeek-Coder quantized tags](https://ollama.com/library/deepseek-coder/tags) (possible [6.7B Instruct Q4_K_M](https://ollama.com/library/deepseek-coder:6.7b-instruct-q4_K_M)) | PENDING — exact Q4/instruct revision unverified | Code-oriented inference |
| 10 | Qwen3.5 4B, Q4; ~3.3 GB | [Ollama Qwen3.5 4B Q4_K_M](https://ollama.com/library/qwen3.5:4b-q4_K_M) | PENDING | General, multimodal-capable model family |
| 11 | Liquid LFM2.5 8B-A1B, Q4; ~5.2 GB | [Ollama LFM2.5 8B-A1B Q4_K_M](https://ollama.com/library/lfm2.5:8b-a1b-q4_K_M) | PENDING | Tool calls and agent interactions |
| 12 | Liquid D1 3B; ~3.7 GB | [Ollama D1 3B](https://ollama.com/library/d1:3b) | PENDING — precision unverified | Structured decisions, NOT free-form chat |
| 13 | Tev1 0.8B; ~833 MB | [Ollama Tev1 0.8B](https://ollama.com/library/tev1:0.8b) | PENDING — published tag may be Q8_0, actual install unverified | Structured decisions, NOT free-form chat |

**Useful source distinction:** A Q4 label alone is not sufficient to identify the exact build; Q4_0, Q4_K_S and Q4_K_M may differ materially. The upstream listing can also change later. Record SSI's **own digest** before assigning a definitive quantization. For example, an Ollama page listing a Q4_K_M tag does not prove the host runs that tag.

## B. Prepared RunPod model endpoints (not all proven ready)

An endpoint or image is not the same as a working model. **The exact source filenames and quantizations for four endpoints are not yet available from the shared evidence**; do not guess based on their informal names.

| Reported deployment | Public source reference | Exact original source/revision | Intended workload |
|---|---|---|---|
| Bonsai 2 27B R2, project-reported PQ2_0 | [Official PrismML 27B GGUF weights](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf) · [SSI public GHCR image](https://github.com/users/jankes72/packages/container/package/ssi-bonsai27) | GHCR `r2` manifest digest `sha256:d60d0caafcffde6aa783a351273ea43b5ee0a5e0948a036c785616ba77b90d48`; internal weight file/revision PENDING | Candidate for general/agentic work; inference test pending |
| Qwen 27B (endpoint label) | [Qwen publisher](https://huggingface.co/Qwen) — **family only** | SOURCE_PENDING: specific 27B model, file and precision | Inference use not yet evidenced |
| Llama 70B (endpoint label) | [Meta Llama publisher](https://huggingface.co/meta-llama) — **family only** | SOURCE_PENDING: generation, revision and quantization | Larger-model route, capability pending |
| Qwen 35B Q8 (endpoint label) | [Qwen publisher](https://huggingface.co/Qwen) — **family only** | SOURCE_PENDING: base/instruct variant and Q8 format | Larger quantized model route |
| Qwen Coder 80B (endpoint label) | [Qwen publisher](https://huggingface.co/Qwen) — **family only** | SOURCE_PENDING: identify exact model; label alone insufficient | Code-oriented GPU route |

**Bonsai weight-size caveat:** The upstream 27B GGUF lists roughly **7.21 GB for PQ2_0** weights, whereas the local compressed SSI Docker archive was operator-reported at **2.38 GB**. This discrepancy alone does *not* establish whether the Docker image embeds or downloads the weights. Inspect the image filesystem and startup configuration before calling it fully self-contained.

The project describes **two on-demand GPU resources** shared with CODEX; the multiple GHCR/RunPod endpoint labels above are not evidence of five simultaneously rented GPUs.

## C. OpenRouter decision APIs and Luna

API routes are **not files to download**. Public pages identify the service and requested model ID. Model weights/quantization are not necessarily disclosed.

| SSI route | Official API model page | Exact identity from configuration | Intended interface (not a tested outcome) |
|---|---|---|---|
| JEV 1.13 | [TypeSafe Jev 1.13](https://openrouter.ai/typesafe/jev-1.13) | Historical route: `typesafe/jev-1.13` — verify active SSI configuration | Typed classification/routing decisions, not prose generation |
| Liquid D1 via OpenRouter | [Liquid D1](https://openrouter.ai/liquid/d1) | Historical route: `liquid/d1` — verify active SSI configuration | Typed decisions; distinct from locally installed `d1:3b` |
| KEV 4B | [Jared Palmer Kev 4B](https://openrouter.ai/jaredpalmer/kev-4b) | Historical route: `jaredpalmer/kev-4b` — verify active SSI configuration | Typed decisions, not general chat |
| Luna 2 (project alias) | [GPT-5.6 Luna on OpenRouter](https://openrouter.ai/openai/gpt-5.6-luna) | Historical route: `openai/gpt-5.6-luna` — verify whether `Luna 2` maps to this revision | Generation and reasoning; separate from the 3 decision-only routes |
| Other configured OpenRouter models | [OpenRouter catalog](https://openrouter.ai/models) | PENDING: read registered model IDs; at least one provider account exists | Role determined by exact API model |

**Don't confuse the classes:** A decision model returning typed probabilities should be judged on selection quality for actual missions, not on whether it can generate a code patch or long chat response. A model that does not implement a required interface is **not an eligible choice for that class of SSI task**; that is a design constraint, not an observed failure.

## D. Other shared paid model APIs

| Source | Public provider page | What SSI reports | Exact live API ID / precision |
|---|---|---|---|
| Together AI | [Together model library](https://www.together.ai/models) | DeepSeek V4 Flash, GPT-OSS 120B and other models were discussed/configured | PENDING: provider IDs, versioned aliases, call evidence |
| Groq | [Groq supported models](https://console.groq.com/docs/models) | SSI provider access | PENDING |
| OpenAI API | [OpenAI model documentation](https://developers.openai.com/api/docs/models) | SSI provider access | PENDING |
| Other paid providers | PENDING, from actual provider registry | Operator reports **at least 8 funded API accounts in total**, each with at least $10 credit | PENDING; avoid inventing provider names, model IDs or balances |

**Credit balances are not benchmark costs and are never published with credentials.** API endpoints may point to updated weights behind a stable alias; snapshot actual returned version and invocation date whenever possible.

## E. The user's main goal: “use here / use with caution / do not use here”

**Real SSI missions are the ONLY evaluation data.** No separately commissioned synthetic benchmark runs. Results of actual authorized missions with SSI CODEX, Director, Robert and real decision flows are collected as evidence while completing useful work.

Every evaluated variant will eventually have a readable *decision card*:

| Required field | Publication rule |
|---|---|
| **Works particularly well for** | Real successful task classes, minimum evidence count and relevant setup |
| **Works less reliably for** | Actual errors, low confidence, timeouts, excessive VRAM or cost in real work |
| **Avoid for** | Repeated verified failures OR inherent interface mismatch; precise conditions and alternatives |
| **Price/performance** | Per completed actual SSI task, separated for VPS fixed cost, API tokens, and GPU billing |
| **Version and source** | Exact pinned tag/revision/digest + official external link |
| **Evidence** | Date, task class, anonymized verifiable result, sample size, notes about uncertainty |

No model gets a green/negative verdict just because it is large, small, expensive, cheap or heavily quantized. Quantizations of the same base model are **separate entries**. 16 GB, 24 GB, 48 GB hardware comparisons require the **actual GPU and VRAM** to be recorded; these are capacity classes, not quantization names.

### Proposed card example (TEMPLATE; no implied findings)

```text
Model: [verified family / variant / precision / pinned digest]
Original source and author: [URL]
Used by SSI: [provider/VPS and actual runtime/model ID]
Works particularly well for: NOT ENOUGH REAL SSI MISSION DATA YET
Works less reliably for: NOT ENOUGH REAL SSI MISSION DATA YET
Avoid for: documented interface mismatch only; other conclusions pending
Real missions observed: 0 publicly published / unknown internal count
Median latency / successful mission cost: pending
Latest evidence UTC: pending
```

## F. Calibration policy and privacy

**Production mission → evidence → calibration → validated router suggestion.** SSI's durable knowledge lives in microsegments, Research Memory, SCC and associated modules; an LLM is a replaceable reasoning/inference component.

- Do **not** rerun useful tasks across models solely to generate comparison scores.
- Record task category, selected model+precision+digest, hardware, latency, token usage, verified outcome and bill **during normal execution**.
- Track selection bias and unequal task difficulty; do not claim that comparing unrelated live tasks is a controlled head-to-head test.
- Treat `FAIL` and `INCONCLUSIVE` separately; sample sizes and uncertainty must remain visible.
- Keep routing, authorization, human approval, cost limits, rollback and recovery intact. Optimizations must not jeopardize real missions.
- Publish only sanitized, aggregate findings and public source URLs; **never** publish customer/project code, private prompts, company documents, memories, credentials, private network topology or privileged server addresses.

### Updating exact provenance (without extra inference tests)

To complete each row from existing manifests and operator reports, collect **metadata only**: installed model ID, pinned digest, quantization as returned by `ollama show` or build metadata, original Dockerfile/source manifest link, trusted artifact hash, and (for APIs) registered provider model slug. This is read-only inventory, **not an additional model benchmark**.

**Next milestone:** reconcile all operator-reported models against installed manifests; only then replace `PENDING` with exact downloaded revisions and attach real-mission performance evidence.


## Planned compact decision students

A separate R1 architecture plan covers two **not-yet-trained** models: **SSI-DECISION-B27-MICRO** and **SSI-DECISION-200B-LITE**, both driven by verified outcomes from real SSI missions. The latter is intended for a spare logical slot on a **24 GB VRAM** GPU without disturbing the three models on the other server; the exact “200B” teacher identity and measured GPU headroom remain unverified. **[Read the deployment and distillation plan](SSI_DECISION_STUDENTS_24GB_R1_PLAN.md).**


## Current infrastructure clarification (2026-10-17)

The current accepted operational design is **[RunPod 24 GB Dual-Model Serial Queue + CORE24 Quantization R2](SSI_RUNPOD_DUAL_MODEL_CORE24_QUANTIZATION_R2.md)**. It replaces the speculative two-student hardware placement: Bonsai 27B and a second compact model are to share the **same** on-demand 24 GB VRAM GPU/disk via a task queue and alternating model load. Separately, the 13 already-installed Q3/Q4 and specialized small models on the always-on 4vCPU/16GB CORE24 VPS enter a per-variant quantization audit. No new weights, runtime changes or inference runs are claimed by this documentation update.
