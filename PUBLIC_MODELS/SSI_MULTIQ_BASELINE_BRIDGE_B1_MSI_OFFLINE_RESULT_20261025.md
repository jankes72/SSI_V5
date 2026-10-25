# SSI MultiQuant BASELINE BRIDGE B1 — MSI offline suite preparation

**Date:** 2026-10-25  
**Evidence:** operator-supplied MSI terminal output  
**Verdict:** `SUITE_FROZEN_REFERENCE_ARCHIVE_PENDING`  
**Execution mode:** `MSI_OFFLINE / NO_GPU / NO_NETWORK / NO_MODEL_LOAD`

## Observed result

- The operator first attempted to copy a nonexisting TXT copy to PY; **that shell copy failed**, but an existing Python file **successfully ran**. The failed copy is not evidence of a failed Python test.
- Reference family: `meta-llama/Llama-3.1-70B-Instruct`.
- Pinned reference model revision: `1605565b47bb9346c5515c34102e054115b4f98b`.
- Historical baseline report: public commit `e540ba601368d36c86296ef2c4a7b60b3fa2ee80`.
- Suite count: **32 cases**.
- Locally generated **canonical JSON array** SHA-256: `8d9ee566d99f95d6f068b877c73d0f077207d5ff3cb8770ef64a1f913d71d553`.
- Offline archive lookup: `REFERENCE_ARCHIVE: NOT_FOUND_IN_DEFAULT_PATHS`; `BASELINE_ARCHIVE_STATUS: REFERENCE_ARCHIVE_NOT_FOUND_ON_MSI`.
- No benchmark inference was executed: `BENCHMARK_RUN: NO`.
- No production changes: `PRODUCTION_CHANGES: NONE`.
- Final marker: `BASELINE_BRIDGE_B1_COMPLETE`.

**Interpretation:** B1 has successfully frozen/generated the exact evaluation suite and its canonical fingerprint. The previously recorded one-question BF16 reference exists in public evidence, but **the original private RunPod archive was not present at the paths checked by the offline script**. This is an archive-location/verification gate, not a failed model inference or proof of lost data. The user can supply its local path with `--reference-zip` once located; do not rerun paid GPUs just to bypass path lookup.

## Shared-task file on GitHub

The exact public **JSONL encoding** of the 32 cases is [here](BENCHMARKS/SSI_MULTIQ_B1_SUITE_32_20261025.jsonl). Its independently checked file SHA-256 is `7122063baa94f744588a2405d140ea6e26c2941ee8ff7f7dcd199602e58158e8`. The JSONL hash differs from B1's canonical JSON array hash **because they hash different serializations**. This is expected; the two values must not be mechanically compared as if they identified the same bytes.

Instructions for the second model/CPU operator and honest price/latency/resource comparisons: [benchmark protocol](BENCHMARKS/SSI_MULTIQ_70B_BF16_IQ2_AND_MODULES_PROTOCOL_B1_R1_20261025.md); [issue #4](https://github.com/jankes72/SSI_V5/issues/4).

## Scope and next step

1. Locate the old operator-generated private baseline ZIP, possibly on another computer or attached archive drive, verify it with B1's read-only `--reference-zip` mode. Preserve the original and never publish its private contents.
2. If archive is not locally available, record `REFERENCE_ARCHIVE_PENDING` and continue only with tasks that do not require original reference readback. The single-question BF16 evidence remains in its earlier report.
3. The 32-case **BF16 GPU**, **CPU plain IQ2** and **same-hardware MultiQuant enabled** runs have **not** been completed. No validated quality/time/cost advantage exists from B1.

**Publication boundary:** bounded test result and identifiers only; no program code, private logs, filesystem locations, model weights, credentials or raw operator data.
