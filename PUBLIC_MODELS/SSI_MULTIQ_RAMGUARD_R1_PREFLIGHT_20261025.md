# SSI MultiQuant RAM Guard R1 — CORE24 read-only preflight

**Date:** 2026-10-25  
**Evidence:** operator-supplied CORE24 terminal output  
**Result:** **PREFLIGHT_COMPLETE / CANDIDATE_REQUIRES_OPERATOR_REVIEW**  
**Production changes:** none; zram not activated

## Observed

| Measured item | Operator observation |
| --- | --- |
| Physical memory | 15.62 GiB |
| Available memory at sampling | 15.05 GiB |
| Existing swap | one disk/file-backed swap, approximately 12 GiB |
| Existing swap used | approximately 14 MiB |
| zram devices in use | 0 |
| Kernel swappiness | 10 |
| 10/60/300-second memory PSI | 0.00 / 0.00 / 0.00 |
| 10/60/300-second I/O PSI | 0.00 / 0.00 / 0.00 |
| zramctl utility | available |
| zram-generator configuration found by preflight | no |
| Logical memory tier declarations | 4 GiB ACTIVE; 4 GiB LONGTERM |
| Small synthetic R15 store inspection | 5 checked / 0 rejected; PASS |
| Small synthetic R18 store inspection | 5 checked / 0 rejected; PASS |

The read-only audit also displayed **cumulative** virtual-memory counters including an historical OOM-kill count. Those counts are not evidence of *recent* pressure or failures without a second timestamped sample. The zero recent PSI averages and nearly idle disk swap do not establish a current swap-performance bottleneck.

## Decision and limitations

R1 indicates that a **reversible 2 GiB logical zram swap pilot** could be considered after checking existing swap priority, available memory, and kernel support. It does not prove zram performance gains or qualify deployment. Zram is compressed volatile memory, not an extra 2 GiB of physical RAM and not durable protection for disk-backed stores. Any pilot must preserve the existing disk swap unchanged as fallback; first run non-persistently and benchmark before introducing a reboot-persistent service.

The two 4 GiB markers are **declarations, not enforced physical disk quotas**. Store-integrity coverage in R1 was **partial synthetic only**, not protection for all SSI memory, mission, research, model or backup stores. Proper disk safeguards require independent index validation, SHA-256 verification, quarantine, filesystem durability measures and backups/restore tests to non-volatile media.

No SCC, Director, Router, Research Memory or Robert production component was activated. The overall SSI migration remains unaccepted in the canonical checkpoint.

## Next gate: RAM Guard R2

Perform a fresh guarded preflight immediately before optional trial activation of a 2 GiB zram swap at a higher priority than the existing disk-backed swap, with no swapoff, no swappiness change, no reboot-persistent changes and post-start measurements. If kernel support, device identity, memory headroom or fallback swap differ from expectations, **STOP**. Monitor PSI, swap counters and zram stats under naturally occurring workload; do not claim acceleration from a configuration-only PASS. Independently inventory and safeguard all SSI disk stores in a later dedicated phase.

Related: [SSI migration truth index](../CURRENT_TRUTH_INDEX.md), [MultiQuant R21](SSI_MULTIQ_V7_16_R21_MULTI_MISSION_CONCURRENCY_20261025.md), [async coordination](SSI_MULTIQ_MIGRATION_ASYNC_HANDOFF_R1_20261025.md).

**Publication boundary:** bounded outcomes and limitations only; no code, private paths, credentials, host addresses, model data or customer records.
