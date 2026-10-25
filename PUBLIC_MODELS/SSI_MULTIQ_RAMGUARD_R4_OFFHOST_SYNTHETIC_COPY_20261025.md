# SSI MultiQuant RAM GUARD R4 — verified off-host copies of two synthetic stores

**Date:** 2026-10-25  
**Evidence:** operator's MSI terminal output  
**Result:** `TWO_SYNTHETIC_STORES_VERIFIED_OFFHOST`

## Observed facts

- Two tiny synthetic stores from earlier R15 and R18 were checked on CORE24: **5 records each, both PASS**.
- The MSI operator's script reported **12 transferred and verified files**, totaling **24,960 bytes**.
- The copy was held on MSI, a different host from CORE24.
- Readback checks: **SQLite PASS**, **SHA-256 PASS**.
- Source unchanged: `CORE24_SOURCES_MODIFIED: NO`.
- No production changes: `PRODUCTION_CHANGES: NONE`.
- Terminal end marker: `RAMGUARD_R4_COMPLETE`.

## Strict scope and limits

The first verified off-host copies in this RAM GUARD series apply to **two small synthetic stores only**. They are **not** a disaster-recovery backup of CORE24, not proof of protection for all SSI databases, and not a restorable snapshot of the live mission/agent runtime. Operator output indicates MSI readback and SQLite checks; no simulated loss of the original VPS and no application-level recovery test was performed. This does not change the incomplete all-node backup/migration status.

RAM Guard R2's 2 GiB logical zram swap is a separate temporary runtime pilot, not a nonvolatile store and not an additional 2 GiB of physical RAM; neither R3 nor R4 proves speed improvement.

## Important independent research milestone

The latest separate public 70B study added a `BF16_BASELINE_SMOKE_PASS_POD_STOPPED` result for the original Meta Llama 3.1 70B Instruct on two A100 GPUs. It supplies a pinned model revision and saved output of one simple prompt, **not a quality benchmark**. The CPU 70B IQ2_XXS experiments and GPU BF16 baseline are run on different hardware, therefore their raw inference times must not be interpreted as an optimization speedup.

See [BF16 baseline and CPU report](SSI_MULTIQ_V7_70B_8G_PUBLIC_RESULTS_20261025.md), [RAM Guard R3](SSI_MULTIQ_RAMGUARD_R3_PASSIVE_METRICS_AND_TEST_BACKUP_20261025.md), [migration checkpoint](../RESULTS/SSI_MIGRATION_CHECKPOINT_20261025.md).

## Next gated step

**RAM GUARD R5:** read-only inventory of actual SSI store sources and their data-dependency/backup requirements, with no deletion, mutation or assumption that small synthetic coverage represents whole-SSI protection. In parallel, **MultiQuant baseline comparison** needs a fixed shared test corpus, pinned tokenizer/prompt, common decoding parameters, separate timing for download/load/prefill/generation, model identity/manifest and answer scoring; only then can BF16-vs-quantized quality comparisons begin. RunPod GPU is stopped and should not be started until the experiment and budget are approved.

**Publication boundary:** bounded outcomes and limitations only; no source code, host addresses, private file paths, secrets, model weights or customer data.
