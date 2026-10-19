# SSI — bounded-memory experiments R1–R7: measured results and limits

**Date:** 19 October 2026. **Owner:** Paweł Jankiewicz / jankes72.  
**Status:** completed local CPU experiments; experimental prototypes, **not production integration or independent replication**.  
**Disclosure:** results and claim boundaries only. Implementation, tuning, source code, private prompts and detailed traces are retained privately.

## Executive summary

The series demonstrates memory/time trade-offs in synthetic computations and
real-weight-fragment microbenchmarks. Separately, complete public low-bit
27B, 32B and 70B checkpoints each completed three simple text tasks under an
8 GiB RAM limit without a GPU. **The latter used a native inference engine
and file-backed paging; it does not validate an integrated SSI compressed LLM
runtime or show that 70B weights are fully resident in 8 GiB.**

The clearest measured memory result is **95.9% lower process RSS** in one
synthetic attention comparison, with a **12.44× execution-time cost**. A
separate real-weight-fragment optimization ran **1.43–2.17× faster** than its
own earlier microbenchmark baseline while using **more** process RAM.
These are scoped engineering measurements, not full-model performance claims.

Machine-readable results: [public summary](../RESULTS/SSI_MEMORY_R1_R7_PUBLIC_SUMMARY_20261019.json).

## 1. Evidence progression

The R1–R7 labels below belong to this local experiment series. They do not
renumber existing MultiQuant releases, R9.x versions or research directions.

| Stage | Tested scope | Bounded outcome |
| --- | --- | --- |
| R1 | Synthetic BF16 matrix-chain computations | 66 process trials; all final outputs bit-identical to their corresponding resident controls. |
| R2 | The same synthetic matrices under alternative memory budgets | 66 process trials / 198 complete passes; outputs bit-identical to preserved R1 references. |
| LEGO audit | Decomposition and reconstruction audit | Supporting audit retained privately; no inference-quality or speed claim from this audit. |
| R3 | Synthetic tensor-storage prototype and restart behavior | 36 trials / 108 complete passes; 23 functional/fault checks PASS; bounded restart outputs bit-identical. |
| R4 | Synthetic attention/context-storage experiment | 30 trials / 90 complete queries; 33 functional/fault checks PASS; same-arithmetic comparisons bit-identical. Separate dense-attention reference agreed within numerical tolerance. |
| R5 | Five actual public model variants, plus a separate real-weight-fragment microbenchmark | 130 native runs; 35 observation/control pairs had identical generations and first logits. 120 microbenchmark cases with 90 bit-identical nonresident comparisons. Small QA also contained failures and inconclusive cases. |
| R6 | Repeated computations using the same real fragments | 120 cases / 360 bit-identical outputs; 120 local evidence-chain checks. Memory and speed depend on workload. |
| R7 | Complete 27B, 32B and 70B low-bit models | 9/9 simple final checks PASS; zero recorded OOM events; all three final servers closed with exit code 0. |

These counts cover different tests and must not be combined into a single
model-quality success rate. Local evidence-chain checks are not independent attestation.

## 2. Memory savings and their execution costs

Numbers below compare each candidate only with its own workload/control.
RSS is process resident memory, excluding the kernel file cache; it is not
VRAM, total host memory, or the theoretical minimum required by an LLM.
Times are complete operations of the stated microbenchmark, **not seconds per generated token**.

| Scope | Control RSS → candidate RSS | RSS reduction | Control time → candidate time | Cost |
| --- | ---: | ---: | ---: | ---: |
| R3, synthetic matrix chain, batch 1 | 316.30 → 36.93 MiB | 88.3% | 0.4091 → 1.0320 s | 2.52× time |
| R4, synthetic attention, 131,072 positions | 1,055.64 → 43.19 MiB | 95.9% | 0.5693 → 7.0850 s | 12.44× time |

Each value is based on three process medians, each with three complete
operations. Setup is excluded from these loop/query times. The private
reports retain setup-inclusive timings and all repetitions. The shared CPU
host and warmed file cache limit generalization; small differences are not
treated as statistically established improvements.

Lossless storage reduction was about **29.85% for the R3 synthetic BF16 data**
and **14.72% for R4 synthetic context data**. Those percentages exclude
auxiliary indexes/checkpoints and are **not** expected compression ratios
for every model. In R5, the additional reduction on selected **already
quantized real weight data** was only **1.28–2.11%**. No whole-checkpoint R5
compression percentage is claimed.

For R6's dense fragment workload, the conservative optimized variant was
**1.43–2.17× faster** than its own repeated-read baseline, with RSS changing
from **38.1–39.3 MiB to 102.6–115.2 MiB**. This is a speed-for-memory trade-off.
A small-cache variant obtained **zero hits** on that dense workload. Much
larger warm-cache gains occurred in a separate artificial locality test;
they are not predictions of native LLM decoding performance.

## 3. Complete-model feasibility: the separate R7 result

Environment: Linux, **8 GiB cgroup RAM limit**, CPU-only Intel Xeon Platinum
8573C, four inference threads, no system swap, one request at a time, and a
512-token context limit. Model files were verified against publisher-provided
hashes before execution. Three fixed, simple checks covered arithmetic,
context extraction and structured sorting.

| Public checkpoint | File size, decimal GB | Peak process RSS, GiB | Simple checks | Observed short-reply wall time |
| --- | ---: | ---: | ---: | ---: |
| Bonsai 2 27B PQ2_0 | 7.21 | 7.13 | 3/3 | 8.9–83.3 s |
| Qwen2.5-Coder 32B Instruct Q2_K | 12.31 | 7.38 | 3/3 | 72.4–147.5 s |
| Llama 3.1 70B Instruct IQ2_XXS | 19.10 | 7.13 | 3/3 | 186.1–371.6 s |

The 70B point is the **largest tested checkpoint**, not a proven absolute
upper bound or an interactive-performance recommendation. File paging
allows checkpoints larger than resident RAM at a substantial I/O/time cost.
The near-limit RSS values reflect the constrained environment and do not
prove that every weight was resident simultaneously. No matched fully
resident baseline was measured, so **R7 has no claimed percentage RAM saving**.

The Bonsai timing was affected by a concurrent download. The final 70B run
used a different configuration from the smaller checkpoints; an earlier
interrupted attempt is retained as such. Treat these timings as observations,
not a controlled cross-model speed ranking. Three simple checks do not
establish general accuracy, low-bit parity with BF16, robotics ability,
long-context quality, tool use or multi-user serving.

## 4. Relation to SSI and existing research directions

R5 native observation equivalence does not mean every answer was correct.
Its single-token interventions still performed the original computations;
they do not demonstrate compute skipping or a trained skill router.

No experiment here demonstrates a trained multi-model merge, automatic
tensor-to-skill attribution, distillation or native low-bit student training.
The existing [D4/D5 research declaration](SSI_MULTIQ_FIVE_DIRECTIONS_R4_R5_DECLARATION_20261018.md)
therefore retains its training/deployment boundaries. Running an externally
published quantized 70B checkpoint is a different result from creating a
70B-derived small SSI student.

The compressed-weight/context prototypes and R6 were **not connected to a
complete native LLM runtime**. Production SCC, Director, Router and model
promotion are unchanged by these local experiments. The exact i5/GTX 960
machine, GPU/VRAM savings and installed VPS checkpoint digests were not
validated. No numerical result here guarantees operation on that target hardware.

## 5. Evidence access and next validation

The public JSON commits to hashes of eight original private experiment
archives. Hashes bind those artifacts; they do not make this public package
self-contained for implementation-level replication or provide an external
signature. Full code, protocols, measurements, failure/restart tests and
interrupted attempts are preserved for controlled review. Model weights and
large regenerable data are not redistributed in those archives.

The next research step is a **planned** end-to-end native integration and
same-checkpoint comparison on target hardware, measuring correctness,
whole-process/cgroup memory, I/O, latency and throughput under realistic
context sizes. Public claims should advance only after that gate is measured.
