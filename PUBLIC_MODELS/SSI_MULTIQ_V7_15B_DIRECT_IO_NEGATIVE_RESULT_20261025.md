# SSI MultiQuant V7.15-B — Direct I/O negative experiment

**Date:** 2026-10-25  
**Status:** FAIL / OOM_KILL; evidence retained.  
**Disclosure:** measurements and conclusions only. No internal source code, optimization algorithms, infrastructure addresses, secrets, or proprietary implementation details.

## Experimental question
Can a standard Direct I/O model-loading mode improve Llama 3.1 70B IQ2_XXS inference with the same 8 GiB memory cgroup limit used in prior successful mmap baselines?

## Conditions
CPU-only Llama 3.1 70B Instruct GGUF (IQ2_XXS; approximately 19.1 GB file), 4-vCPU class host, 8 GiB memory cgroup limit, 8 GiB swap cgroup limit, same short arithmetic task and explicit Llama 3.1 conversation template. The distinguishing setting was the existing llama.cpp Direct I/O loading mode. This was a standard engine option, **not** a proprietary SSI optimization.

## Observed result
- Unit termination: **oom-kill**.
- Main process: **killed (SIGKILL)**.
- Wall time: **3 min 38.813 s** (~218.81 s).
- Accumulated CPU time: **48.128 s**.
- Systemd summary: **15.8G I/O read, 8.0G I/O written** (units as reported by systemd).
- Monitoring samples: **98**.
- Wrapper exit status: **1**.
- **No completed answer**; experiment failed.

The I/O summary alone does **not** establish which bytes came from model weights or swap activity. Cgroup memory events, swap and pressure metrics, and storage attribution need to be examined before assigning causality. This result demonstrates failure of this tested Direct I/O configuration, **not** universal inferiority of Direct I/O.

## Context: prior mmap baseline
A previous controlled mmap run V7.13 using the same short task and 8 GiB memory cgroup limit generated the correct answer `4`, completed in **127.310 s**, and exited successfully. Its sampled cgroup `io.stat` counter increased by **70.466 GiB** over the monitored window. Its I/O counter interpretation remained subject to reconciliation with the systemd service summary.

## Decision and next validation
1. Do not automatically rerun Direct I/O or raise memory limits.
2. Preserve the failed-run evidence and inspect `memory.events`, `memory.stat`, swap, and I/O counters before choosing a new candidate.
3. Keep standard mmap as the proven functional reference for this short task under the tested conditions.
4. Continue work toward reproducible comparisons with multiple trials and explicit safeguards.

**No speedup or product qualification is claimed.**
