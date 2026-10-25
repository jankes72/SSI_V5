# SSI MultiQuant RAM Guard R2 — temporary zram pilot on CORE24

**Date:** 2026-10-25  
**Evidence:** operator-provided remote terminal output  
**Verdict:** `PILOT_ACTIVE_NONPERSISTENT` — controlled configuration change confirmed, **performance gain not yet measured**

## Observed activation

| Field | Result |
| --- | --- |
| R2 guarded preflight | PASS |
| Logical zram capacity | 2 GiB (kernel-reported active swap 2,097,148 KiB) |
| zram device | first zram device |
| zram swap priority | 100 |
| Existing disk/file-backed swap | preserved; one fallback present |
| swappiness | unchanged at 10 |
| Available RAM at preflight | 15.05 GiB |
| zram pages used at first reading | 0 KiB |
| Boot-persistent changes | none |
| Production services restarted | no evidence of any |

Operator markers: `DISK_SWAP_FALLBACK_PRESERVED: YES`, `SWAPPINESS_UNCHANGED: YES`, `ZRAM_USED_NOW_KIB: 0`, `R2_STATUS: PILOT_ACTIVE_NONPERSISTENT`, `RAMGUARD_R2_PILOT_COMPLETE`.

## Meaning and limits

This confirms that the 2 GiB **logical capacity** compressed-RAM swap was activated in the current host session with higher priority than existing disk swap. It does **not add physical RAM**. Zero zram usage at the observation point means there was no evidence yet of improved throughput, faster I/O or reduced disk swap traffic. A priority advantage matters only when pages are swapped under memory pressure; compression consumes RAM and CPU.

The pilot configuration **does not persist automatically after reboot**. No automated disable/rollback or reboot-survival test is claimed. The existing disk swap remains available as fallback. Real benchmarking requires before/after workload measurements including zram mm_stat, swap I/O counters and memory/I/O pressure; comparisons must be under matched loads and should avoid destabilizing memory on shared VPS.

**Disk-store integrity coverage remains incomplete.** Zram is volatile memory and cannot replace checksums, SQLite integrity checks, coherent snapshots or restorable backups. Earlier R1 inspected two tiny synthetic stores only; the logical 4 + 4 GiB capacity declarations are not enforced disk quotas.

The SCC/Director migration status remains separate, and R22 concurrency work is not completed or superseded by RAM Guard.

## Next phase

**R3:** non-destructive runtime observation of active zram and fallback swap, baseline checks on known tiny synthetic stores, and creating separately verifiable small test-store copies on persistent storage. Preserve previous evidence; do not touch live databases or interpret an idle sample as a performance gain. Inventory additional stores before claiming comprehensive protection.

See [RAM Guard R1 preflight](SSI_MULTIQ_RAMGUARD_R1_PREFLIGHT_20261025.md), [current migration checkpoint](../RESULTS/SSI_MIGRATION_CHECKPOINT_20261025.md), [async coordination](SSI_MULTIQ_MIGRATION_ASYNC_HANDOFF_R1_20261025.md).

**Public policy:** evidence and limitations only, without scripts, code, operational host paths, credentials, model weights, client data or private algorithms.
