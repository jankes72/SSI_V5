# SSI MultiQuant R5 — read-only CORE24 inventory (bounded scope)

**Date:** 2026-10-25  
**Source:** operator-provided terminal output; no independent server-side inspection by this reviewer  
**Result:** `READ_ONLY_INVENTORY_COMPLETE` / `SCAN_STATUS: COMPLETE_WITHIN_ROOT`  
**Scope:** exactly one MultiQuant project tree on CORE24, **not the entire SSI installation**  
**Changes to production:** none

## Reported observations

| Metric | Result |
| --- | ---: |
| Scanned entries | 299 |
| Directories | 110 |
| Regular files | 189 |
| Symlinks | 0 |
| SQLite-like database candidates by extension | 29 |
| SQLite sidecar file candidates | 2 |
| Logical bytes (all files) | **19,098,148,698 B** |
| Logical bytes deduplicated by inode | **19,098,148,698 B** |
| Allocated bytes deduplicated by inode | **19,098,755,072 B** |
| Scan errors / truncated | **0 / false** |
| One known local 70B IQ2_XXS GGUF file | **19,097,389,632 B** |
| Other small files and evidence combined, by difference | **759,066 B** |
| Filesystem free bytes at sampling | **33,703,673,856 B** |
| Filesystem total bytes at sampling | **126,605,975,552 B** |
| 2 GiB zram swap active | **Yes**, priority 100 |
| Disk-backed swap fallback active | **Yes**, priority -2 |
| Runtime/ACTIVE and ARCHIVE dependencies verified | **No** |
| Director 80 GB package fit proven | **No** |

The GGUF file accounts for nearly all logical bytes in the scanned tree (approximately **99.996%**). The count of 29 candidate databases is based on names/extensions; **their contents, runtime purpose and safety were not audited in R5**. The measured project-tree size is not a system-wide installation size, an ACTIVE-size estimate, or proof that the model file can safely be removed or archived. The GGUF remains an experimental asset requiring explicit dependency review.

## Boundaries and interpretation

- R5 used metadata-only, read-only traversal; no file contents, private source code, database rows or proprietary algorithms were read.
- Physical allocated bytes use inode-based deduplication **within this one scan**; no cross-host, cross-snapshot or semantic duplicate analysis was performed.
- The SSI Director migration's proposed 80 GB budget is a separate installation and requires a full dependency-closed manifest, environment/runtime/data plus OS/container overhead and growth reserve; this CORE24 scan cannot qualify it.
- This result does not establish current native SCC, Router, Research Memory, Notary or executor integration.
- RAM Guard zram metrics describe a temporary compressed swap pilot and do not prove faster performance.
- No source moves, deletions, database modifications, registry promotions or paid model executions occurred.

## Gate to proceed

1. Keep every scanned group **UNRESOLVED** until the migration owner supplies the dependency-linked ACTIVE / ARCHIVE / UNRESOLVED manifest; retain evidence and model-asset provenance.
2. Confirm which executable model/service actually uses the 70B GGUF and which stores are necessary at runtime; do not infer this from file size.
3. Use a fixed paired-task benchmark protocol for BF16 GPU reference, IQ2_XXS plain CPU inference, and a separate **same-hardware, same-model** MultiQuant ablation. Only the ablation can test whether MultiQuant modules improve time or resource use beyond baseline.
4. The recent BF16 70B smoke test is one question; no matched multi-task benchmark results exist yet.

Related: [BF16 baseline report](SSI_MULTIQ_V7_70B_8G_PUBLIC_RESULTS_20261025.md), [RAM Guard R4](SSI_MULTIQ_RAMGUARD_R4_OFFHOST_SYNTHETIC_COPY_20261025.md), [migration ACTIVE/ARCHIVE handoff](../RESULTS/SSI_MIGRATION_MULTIQ_CORE_ARCHIVE_HANDOFF_R1_20261025.md).

**Public release boundary:** generalized observations and limitations only. Raw manifest, absolute host paths, software implementation, credentials, customer data, and raw evidence are private.
