# SSI MultiQuant V7.16 R17 — verified-donor recovery on isolated synthetic copies

**Date:** 2026-10-25  
**Operator-observed result:** **10/10 PASS**  
**Scope:** `ISOLATED_RECOVERY / VERIFIED_DONOR`  
**Production changes:** none

## Reported checks

| Check | Result |
| --- | --- |
| Known-good donor's five synthetic records passed checksum verification | PASS |
| Corrupted synthetic record detected | PASS |
| Corrupted record reconstructed using verified donor bytes | PASS |
| Original corrupted bytes retained in quarantine | PASS |
| Missing record reconstructed from verified donor | PASS |
| Corrupt donor rejected without modifying missing target | PASS |
| Index metadata conflict rejected without changes | PASS |
| Orphan test object preserved for manual review | PASS |
| Repeating recovery of an already-correct record made no changes | PASS |
| Prior R16 evidence unchanged; recovered test copies verified | PASS |

Final operator output: `R17_RESULT: 10/10 PASS`; `RECOVERY: CORRUPTED_AND_MISSING_RESTORED`; `QUARANTINE: PRESERVED`; `UNRESOLVED_CONFLICTS: BLOCKED`.

## What this establishes

The isolated experimental recovery routine can identify and repair the two specified classes of synthetic damage (a corrupted indexed record and a missing indexed record) from a **previously validated donor copy**. It retains corrupted bytes and refuses to guess when the donor checksum or index metadata is inconsistent. An already valid item is left unchanged. Previous R16 data were preserved within the script's monitored snapshot.

## Evidence limits

- This is a small synthetic fixture, not production SSI disaster recovery, live Research Memory, current SCC, or a complete backup/restore of any VPS.
- No simulated concurrent writers, real power loss, crash during replacement, fsync of parent directories, cross-filesystem transaction, or storage-medium failure was validated.
- The test uses a separate experimental recovery routine; it does not establish that the underlying original storage library natively implements automatic recovery or enforces the planned 4 GiB + 4 GiB quotas.
- The test does not qualify native LLM KV-cache offload, 70B acceleration, or model response quality.
- The latest available public migration checkpoint continues to identify Director's native SCC parser as unverified and overall migration as not production-accepted.

## Next experimental milestone

**R18:** test cross-process continuity and idempotent checkpoint replay for small, independent synthetic missions, preserving immutable earlier evidence and avoiding any production restart. Keep mission receipt semantics separate from the model's context bytes; label the test `SHADOW / SYNTHETIC`.

See [R16 failure detection](SSI_MULTIQ_V7_16_R16_FAULT_DETECTION_20261025.md), [R15 capacity control](SSI_MULTIQ_V7_16_R15_DUAL_TIER_QUOTA_20261025.md), and [migration exchange handoff](SSI_MULTIQ_MIGRATION_ASYNC_HANDOFF_R1_20261025.md).

**Public reporting contains only outcomes and limitations; no private source code, infrastructure details, secrets, customer records or proprietary algorithms.**
