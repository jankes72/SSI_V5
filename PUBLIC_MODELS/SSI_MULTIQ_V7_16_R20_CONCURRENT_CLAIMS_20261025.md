# SSI MultiQuant V7.16 R20 — Isolated concurrent worker claims

**Date:** 2026-10-25  
**Evidence:** operator-provided CORE24 terminal output  
**Outcome:** **10/10 PASS** in an isolated synthetic SQLite test

## What passed

1. Prior R19 source memory, checkpoint receipts, and context checked.
2. Two concurrently started workers competed for one step; only one obtained a successful claim.
3. A single synthetic effect was recorded for that completed step inside the local test ledger transaction.
4. Replay of the completed step did not duplicate the receipt.
5. A changed plan reference was refused.
6. A changed context reference was refused.
7. Process termination after a committed claim left no committed test effect.
8. A still-active claim blocked a competing worker.
9. A manually expired test claim was reclaimed with a newer generation; stale prior ownership was rejected by a fencing check.
10. Ledger integrity held and earlier R19 evidence remained unchanged.

**Output markers:** `CLAIMS: 2`, `SYNTHETIC_EFFECTS: 2`, `R20_RESULT: 10/10 PASS`.

These totals represent **two different synthetic test steps**, not two executions of one step.

## Evidence boundary

This checks an isolated SQLite row-claim pattern and synthetic effects *inside the same SQLite transaction*. It **does not** demonstrate exactly-once delivery for external API calls, emails, real-world actions or other processes/services. Lease expiry was injected manually; no clock-drift, real network partition, distributed lock authority, host power loss, or production service failover was tested. The original SSI worker/router was not activated. The two 4 GiB memory capacity declarations are not production-enforced disk quotas; no LLM KV-cache offload or 70B acceleration was measured.

At publication time, the central migration checkpoint still reports `MIGRATION_IN_PROGRESS_NOT_PRODUCTION_ACCEPTED`, unverified authoritative Director SCC parser, and staged/disabled Robert worker. These statuses are not changed by R20.

## Proposed R21

Test independent **synthetic** missions in concurrent processes sharing a local ledger, verify no cross-mission receipt collision, and demonstrate that a stuck claim in one mission does not stop another. Test fail-closed plan/context mismatches and stale-claim reclamation; preserve earlier R20 evidence.

Related: [R19](SSI_MULTIQ_V7_16_R19_STEP_RESUMPTION_20261025.md), [migration checkpoint](../RESULTS/SSI_MIGRATION_CHECKPOINT_20261025.md), [coordination handoff](SSI_MULTIQ_MIGRATION_ASYNC_HANDOFF_R1_20261025.md).

**Publication limit:** only results, caveats and links, never private scripts, implementation details, secrets, source-code, customer data, or model weights.
