# SSI MultiQuant FSE-01 — P1B runtime/limit discovery

**Date:** 2026-10-25  
**Evidence:** operator-supplied CORE24 terminal output, reviewed without remote access  
**Status:** `FSE_P1B_READ_ONLY_DISCOVERY_COMPLETE / INFERENCE_ENGINE_AND_MODEL_LIMIT_UNRESOLVED`  
**Changes:** none reported; model not launched  
**Related:** [FSE-01 kickoff](SSI_MULTIQ_FSE01_FIRST_PRODUCT_REAL_HARDWARE_KICKOFF_R1_20261025.md), [P1 hardware preflight](SSI_MULTIQ_FSE01_P1_CORE24_READONLY_PREFLIGHT_20261025.md), [BF16 baseline](BENCHMARKS/SSI_MULTIQ_B1_BF16_RESULTS_20261025.md).

## Operator-observed service status

| Service class | ActiveState | `MemoryMax` bytes | `MemorySwapMax` |
| --- | --- | ---: | --- |
| Ollama inference daemon | active | `infinity` | `infinity` |
| SSI CORE24 API service | active | `419430400` (400 MiB) | `infinity` |
| SSI CORE24 worker service | active | `471859200` (450 MiB) | `infinity` |

**Interpretation:** The 400 MiB and 450 MiB cgroup memory limits belong to **API and worker processes**, not to the 70B inference job. The currently active Ollama daemon has no configured `MemoryMax` limit in its unit. Neither the daemon nor the API/worker limits establish the historical experimental `MemoryMax=8 GiB / MemorySwapMax=8 GiB` configuration on any currently running 70B model invocation.

## Discovery

- In the pre-specified bounded search locations, no `llama-cli`, `llama-server`, or `llama-bench` files were returned.
- The checked candidate source repositories did not provide a Git HEAD revision. **This is not a global search**; llama.cpp may exist elsewhere, in a container, in a private build tree, or not be presently installed.
- There is no evidence that the historical llama.cpp commit `9d1878a` remains the current runnable binary.
- The output includes the operator SSH shell's cgroup, **which cannot be used as a proxy for the model's service unit**.
- `MODEL_EXECUTION=NO`, `PRODUCTION_CHANGES=NONE`, `FSE_P1B_STATUS=READ_ONLY_DISCOVERY_COMPLETE`.

## Gate result

**`P1_ENVIRONMENT_PARTIAL_PASS`**: the physical CORE24 hardware and the 19,097,389,632 B GGUF were observed at P1; zram and disk swap active, no pressure at that moment. The service inventory exists.

**`P1B_ENGINE_CGROUP_IDENTITY_PENDING`**: no runnable engine location, current llama.cpp commit, pinned GGUF provenance, direct model cgroup or verified model prompt parity. **`FSE_P2_NOT_STARTED`.**

## Next step: P1C read-only inspection

1. Check limited additional application locations, registered packages/containers and local model inventory; avoid recursive whole-disk search.
2. Record exact executable path or report `ENGINE_NOT_LOCATED` without assuming broken system.
3. Inspect only safe unit properties (`MainPID`, `ControlGroup`, `MemoryMax`, `MemorySwapMax`) and available software versions; **never publish environment variables, credentials, port bindings or operational endpoint identifiers**.
4. Only after locating an actual executable, arrange a separate bounded model process with explicit 8 GiB memory + swap controls for a pilot, subject to operator scheduling and no interference with the running API/worker.
5. The initial M01 pilot must measure actual RAM, swap, zram, CPU, I/O, latency, prompt/token hashes and error status. Do not run 96 requests by default.

**Neither inference quality nor MultiQuant performance is evaluated by P1B.** The full BF16 baseline is complete but CPU IQ2 B1 and genuine enabled/disabled MultiQuant ablation remain pending.

**Publication boundary:** generalized service classes and measured limits only. Private paths, SSH addresses, shell cgroup identifiers and raw operator logs stay outside the public repo.
