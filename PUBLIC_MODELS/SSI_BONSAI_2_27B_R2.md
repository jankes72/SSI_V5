# SSI Bonsai 2 27B — Docker / RunPod Edition R2

**Maintainer:** [jankes72](https://github.com/jankes72)  
**Published container:** [GHCR: ssi-bonsai27](https://github.com/users/jankes72/packages/container/package/ssi-bonsai27)  
**Image:** `ghcr.io/jankes72/ssi-bonsai27:r2`  
**Status:** Public container manifest verified; independent runtime and security qualification pending  
**Documentation date:** 2026-10-17

> **Scope:** This is a third-party model deployment/package effort. It is **not** a claim to have designed or trained the underlying Bonsai 2 27B model. SSI's private agent runtimes, memories, credentials, datasets, and internal modules are not part of the intended public release. Full image-layer audit is not yet complete.

## What we prepared

- A custom Docker container image for a Bonsai 2 27B deployment, identified in the project as a PQ2_0 quantized variant.
- A build workflow on an Ubuntu MSI development machine; local build logs and a compressed Docker archive exist, but are not part of this public documentation.
- A tagged release `r2` in GitHub Container Registry (GHCR).
- A RunPod Serverless endpoint configuration, with `minWorkers=0`, `maxWorkers=0`, an `ADA_24` GPU class target and a 40 GB temporary disk. This records endpoint provisioning **without claiming successful model inference**.
- Read-only public registry verification on 2026-10-17: anonymously obtained a pull-scoped registry token, then fetched the `r2` manifest using an authenticated registry request. HTTP **200** returned.

**Observed GHCR manifest digest:**  
`sha256:d60d0caafcffde6aa783a351273ea43b5ee0a5e0948a036c785616ba77b90d48`

A successful manifest request does not establish that every image layer is downloadable, that the model weights are embedded, or that the container runs successfully on a target GPU.

## Obtain the image

```bash
docker pull ghcr.io/jankes72/ssi-bonsai27:r2
```

For a pinned reference:

```bash
docker pull ghcr.io/jankes72/ssi-bonsai27@sha256:d60d0caafcffde6aa783a351273ea43b5ee0a5e0948a036c785616ba77b90d48
```

Docker Engine access is required locally. An adequate GPU and runtime dependencies may be required to *run* the image; verified end-user run commands, exposed API routes, driver/CUDA requirements, and RAM/VRAM measurements are **pending**. Do not assume that downloading alone yields a ready endpoint.

## Verified status vs. open questions

| Area | Status | Evidence or caveat |
|---|---|---|
| Container tag published to GHCR | Verified | Package page and `r2` tag |
| Anonymous registry manifest access | Verified | HTTP 200 with anonymous pull-scope token |
| Manifest digest | Verified | SHA256 above |
| Local compressed Docker archive | Operator-reported | ~2.38 GB archive on MSI |
| RunPod endpoint creation | Operator-reported | Endpoint configured with workers 0/0 |
| Full public layer download | Not tested | Do not infer from manifest access |
| Model weight completeness | Not tested | Image content inspection pending |
| GPU loading and inference | Not tested | No independently verified generated response |
| Reproducible install for end users | Not tested | Runtime startup command and dependencies pending |
| Image security / secret scanning | Incomplete | Outer archive filename check only; layer/content scanning pending |
| Redistribution rights | Pending review | Confirm weights, inference runtime, base image, and component licenses |

## Evaluation programme

This is a **living, evidence-based test record**. Failures will be published alongside successful results. No benchmark numbers are reported until reproducible measurements exist.

### Test environment template

| Field | Value |
|---|---|
| Test ID and date | PENDING |
| Image digest | PENDING |
| Host OS | PENDING |
| GPU and VRAM | PENDING |
| Driver / CUDA or runtime | PENDING |
| CPU and RAM | PENDING |
| Model and quantization verified in runtime | PENDING |
| Context length / batch size | PENDING |
| Prompt set and reproducible settings | PENDING |

### Benchmark register

| Test area | Measurement | Result | Evidence |
|---|---|---|---|
| Cold start and image setup | time to ready, download sizes | NOT TESTED | — |
| GPU fit | VRAM peak, OOM frequency | NOT TESTED | — |
| Generation performance | prefill, output tokens/s, p50/p95 latency | NOT TESTED | — |
| Polish / English / multilingual | accuracy and failure examples | NOT TESTED | — |
| Reasoning and instruction following | fixed task suite, reproducibility | NOT TESTED | — |
| Coding | unit tests passed, patch correctness | NOT TESTED | — |
| JSON / structured outputs | schema success rate | NOT TESTED | — |
| Long context | recall accuracy, truncation, stability | NOT TESTED | — |
| Safety and refusal behavior | defined evaluation suite | NOT TESTED | — |
| Concurrent requests | throughput, errors, resource usage | NOT TESTED | — |
| Reliability | restarts, memory leaks, failures | NOT TESTED | — |
| RunPod cost | actual metered cost / completed request | NOT TESTED | — |

### Strengths — evidence required

*No performance strengths have been established yet.* For each future strength include test ID, comparison baseline, raw measurement, configuration, and limitations.

### Weaknesses — evidence required

*No performance weaknesses have been established yet.* We will document incorrect answers, quality degradation from quantization, slowdowns, failed starts, out-of-memory errors, dependency incompatibilities, and other observed issues with reproducible examples.

### Known release limitations (not model-quality judgments)

1. Public download and execution have not yet been end-to-end validated.
2. RunPod model startup, inference and API compatibility are not yet verified.
3. The public image has not completed a full internal layer/secret/license audit.
4. Hardware requirements cannot yet be claimed as measured simply from GPU class selection.
5. Image tag `r2` is mutable; use the pinned digest for reproducible tests.

## How to report results

Use a structured entry:

```text
Test ID:
UTC date:
Test environment and image digest:
Prompt/task and evaluation method:
Expected result:
Observed result:
Pass / Fail / Inconclusive:
Latency / throughput / VRAM / cost:
Logs or reproducible evidence (redacted):
Known confounders:
```

Do not publish API keys, private IPs, credentials, proprietary code, private prompts, personal data, or machine-specific session information. Prefer reproducible synthetic test prompts.

## Next release gates

1. Inspect and scan actual image layers, container configuration and history for confidential materials.
2. Verify all applicable redistribution licenses and notices.
3. Confirm anonymous download of the **full image**.
4. Validate startup on a supported GPU and record working deployment instructions.
5. Publish test scripts, reproducible benchmark evidence, strengths, weaknesses, and changelog.
6. Only then mark the release as end-user validated.

## Relationship to SSI V5

The Docker image is an optional external inference engine candidate for SSI's model router. Publication of this package does **not** disclose or release private SSI V5 modules or project data. Successful integration with SSI's router is a separate acceptance task.


## SSI V5 — multi-model real-world evaluation programme (planned)

**Scope expansion — 2026-10-17.** SSI will benchmark not only this Bonsai release but the model collection actually available to the project, using **real SSI CODEX, Director and Robert tasks** as well as controlled tests. The operator estimates roughly 20 or more model variants, but the **exact inventory is not yet verified**.

This is a **documentation and comparison programme**, not a plan to upload every third-party model to GHCR. For models sourced elsewhere, we will link to their **official upstream model pages**, preserving authorship, licenses, versions and original download locations after verification. No model weight redistribution is implied.

### Hardware and quantization comparison

Record actual hardware rather than assuming that “16 / 24 / 48” always refers to GPU VRAM. Planned comparison classes include **16 GB, 24 GB and 48 GB** environments where available; measure whether each is RAM, VRAM or both. Distinguish full-precision and quantized variants (e.g., Q2/PQ2, Q3, Q4, Q8 and larger precision formats **only when actually present**). Never infer a precision, fit, memory footprint, or speed from a filename alone.

For every verified variant, log:
- Canonical model name, parameter count, upstream author, official link, license and model revision/digest;
- Quantization type / file format / execution engine and whether the model weights are local, on an existing VPS, external API, or RunPod;
- Actual download source and verified file hash (exclude private mirror tokens);
- CPU, system RAM, GPU model, VRAM, environment and runtime versions;
- On-disk bytes, runtime RAM/VRAM peak, cold-start time, tokens/sec, input/output latency, failures, estimated or metered costs;
- Reasoning, coding, multilingual (including Polish), instruction-following, long-context and structured-output behavior;
- Real SSI mission outcomes, passed tests, regressions, task suitability and observed weaknesses;
- Evidence ID, repeat count, confounding factors, limitations and **PASS / FAIL / INCONCLUSIVE / NOT TESTED**.

### Real SSI work as benchmark evidence

The primary application benchmark will use anonymized/reproducible real workflows: SSI CODEX repository analysis, code generation, patch validation and tests; Director task planning, routing and recovery; Robert browser automation and evidence creation. Results must separate **model ability** from orchestration, tools, retrieval and hardware effects. Private SSI code, repositories, user data, memories and credentials must never be published.

### Living comparison register

| Variant / family | Source link | Precision / runtime | Tested on 16 GB | Tested on 24 GB | Tested on 48 GB | SSI mission result | Strengths | Weaknesses |
|---|---|---|---|---|---|---|---|---|
| Bonsai 2 27B (SSI Docker R2) | Verify upstream | PQ2_0 (project-reported) | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | TBD | TBD |
| Qwen family (exact variants pending inventory) | Pending | Pending | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | TBD | TBD |
| Llama family (exact variants pending inventory) | Pending | Pending | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | TBD | TBD |
| Other installed or downloaded variants | Pending inventory | Pending | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | TBD | TBD |

Additional models will be added **only after** an inventory provides evidence they are actually present and identifies a legitimate source. Different quantizations of one base model will be tracked as separate **variants**, while the parent family is counted only once when summarizing distinct models.

### Evaluation publication rules

1. No fabricated scores, undocumented “best model” claims, or extrapolation between GPU configurations.
2. Publish both useful results and failed tests, including OOMs, unsupported runtimes, inaccurate answers, and unstable performance.
3. Separate measured observations, operator reports, and forecasts.
4. Link external models instead of republishing their weights unless licensing and publication have been reviewed.
5. Publish only redacted evidence and benchmarks safe to disclose.
6. Update this register whenever a real test finishes; a model without tests remains **NOT TESTED**.
