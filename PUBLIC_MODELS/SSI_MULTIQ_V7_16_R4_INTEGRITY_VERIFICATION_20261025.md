# SSI MultiQuant V7.16 R4 — Public integrity verification report

Date: 2026-10-25
Status: **3/3 post-run integrity observations verified**; full 5-test R4 rerun not confirmed.

## Verified read-only inspection of existing synthetic sandbox

| Synthetic record | Tier | Pinned | Integrity check |
|---|---|---:|---|
| context_a | long-term | yes | CORRUPTED — detected |
| context_b | long-term | no | PASS |
| context_c | active | no | PASS |

The synthetic record `context_a` had an indexed expected length of 4096 bytes, while its stored file was 9 bytes. The read-only integrity verification distinguished this damaged item from two intact items.

## Scope and limitations

- Evidence comes from operator-provided output of a read-only check against an **existing synthetic test sandbox**.
- This confirms **detection**, not repair or restoration of damaged data.
- Earlier end-to-end R4 test steps were not all independently observed in this verification; **do not claim a new R4 5/5 PASS**.
- The two planned 4 GiB stores remain logically budgeted and are not yet integrated with the prototype or a live SSI workload.
- No native 70B model KV-cache disk offload, speedup, memory reduction, or production readiness is established.
- Source code, scripts, internal architecture, credentials, and optimization know-how are intentionally omitted.

Next: test fail-closed retrieval and protected checkpoint handling, then controlled recovery from an independently verified copy.
