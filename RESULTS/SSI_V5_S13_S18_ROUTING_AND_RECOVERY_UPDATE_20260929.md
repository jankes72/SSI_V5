# SSI V5 — S13-S18 routing evidence and crash-recovery update — 2026-09-29

**Repository role:** sanitized public evidence/review mirror.  
**Run:** `RUN_20260926T064644Z_793783ad`  
**Evidence boundary:** software/runtime evidence only. Physical validation and independent external replication are not claimed.

## Executive summary

The current public training front is no longer S12. The available evidence shows six completed core-training stages, **S13 through S18**, with **1,260 unique case executions** across BODY_FROZEN and ISKRA1..ISKRA6.

```text
completed unique cases = 1,260
PASS                   = 1,197  (95.00%)
INCONCLUSIVE           =    53  ( 4.21%)
FAIL                   =    10  ( 0.79%)

routing provenance present = 1,260 / 1,260
micronetwork_used          = 1,260 / 1,260
v10_used                   = 1,260 / 1,260
collective_used            = 1,260 / 1,260

automatic_champion=true    = 0 / 1,260
champion_route_used        = 0 / 1,260
no_automatic_champion=true = 1,260 / 1,260
```

The routing audit counts each unique `(stage_id, actor, case_id)` once. Repeated nested marker occurrences are not treated as additional executions, and PASS/FAIL is not used to infer routing.

## Stage results

| Stage | Executed | PASS | INCONCLUSIVE | FAIL | PASS rate | Cross-consolidation |
|---|---:|---:|---:|---:|---:|---|
| S13 | 210/210 | 203 | 6 | 1 | 96.67% | COMMITTED |
| S14 | 210/210 | 208 | 1 | 1 | 99.05% | COMMITTED |
| S15 | 210/210 | 175 | 31 | 4 | 83.33% | COMMITTED |
| S16 | 210/210 | 209 | 1 | 0 | 99.52% | COMMITTED |
| S17 | 210/210 | 206 | 2 | 2 | 98.10% | COMMITTED |
| S18 | 210/210 | 196 | 12 | 2 | 93.33% | COMMITTED |
| **Total S13-S18** | **1,260/1,260** | **1,197** | **53** | **10** | **95.00%** | **6 committed consolidations** |

The weaker stage is S15; unresolved and failed outcomes remain preserved rather than being relabeled PASS.

Recorded consolidation transactions:

```text
S13 = CC_51716af604ada40b0883bb97e17f2b11
S14 = CC_e96219d84ce62b3be3a1291f886c13f4
S15 = CC_0463d78c35fd7205c5698a158c4749ac
S16 = CC_da1b0d45ab78211bd2a495a2a4bbf671
S17 = CC_bdf546a680d35897ea45de4117544afe
S18 = CC_10ec6aed61774b7a060c9e8a0674abd0
```

## What the routing evidence proves

For all **1,260 completed S13-S18 cases**:

- `routing_provenance_present=true`
- `micronetwork_used=true`
- `v10_used=true`
- `collective_used=true`

This supports the bounded claim that Micronetwork/V10 participation is present in the recorded runtime path for every completed S13-S18 case.

Provider Gateway usage was recorded in **1,199 / 1,260 cases (95.16%)**.

## What the routing evidence does not yet prove

The current case receipts do **not** contain a canonical per-case final route decision that separates:

```text
EXACT / TOP-1 REUSE
MICRONETWORK-ONLY COMPLETION
FULL-FLOW ESCALATION
CHAMPION EXECUTION
```

The unique-case audit therefore classifies all completed S13-S18 cases as:

```text
MICRONETWORK_V10_USED_ROUTE_UNRESOLVED = 1,260 / 1,260
```

This is intentional. The audit does not convert repeated `FULL_FLOW`, cache or Champion text markers into execution counts.

Automatic Champion execution is specifically **not** claimed. The completed case evidence records:

```text
automatic_champion=false    = 1,260 / 1,260
no_automatic_champion=true  = 1,260 / 1,260
champion_route_used         = 0 / 1,260
```

## S19 interruption and recovery boundary

S19 was interrupted after BODY_FROZEN produced **30 case files**:

```text
BODY_FROZEN S19
PASS         = 14
INCONCLUSIVE = 16
FAIL         = 0
```

After the host interruption, 15 existing S19/BODY_FROZEN case files were present but their CASE attestations had not yet been appended to the signed evidence stream.

The recovery procedure:

1. limited recovery to the explicit `S19/BODY_FROZEN` boundary,
2. appended attestations for those already-existing case files,
3. preserved the original case contents and PASS/INCONCLUSIVE status,
4. rechecked evidence coverage,
5. sealed the source run as interrupted.

No failed or inconclusive result was promoted to PASS.

**No successful post-recovery ISKRA1 S19 execution is claimed in this publication.**

## Additional implementation changes verified before restart

The recovery work also added or verified the following internal controls:

- unique-case routing audit instead of repeated-marker counting;
- new runtime telemetry field for future cases, intended to record the effective routing path (`routing_execution`);
- continuation support prepared for resuming S19 from `ISKRA1 / S19-01-01` while preserving the prior BODY_FROZEN evidence;
- application hash synchronization after the controlled training-code patch;
- Pocket Micro integrity pins resynchronized without modifying raw LEGO Pocket data, native model weights, Champion state or qualification state;
- Pocket Micro checker returned `READY`;
- SSI Doctor returned `READY_FOR_BOOT` with all seven BODY/ISKRA actor sockets present;
- WEB LEGO preflight remained `READY`.

Observed WEB preflight state:

```text
lego_items  = 126
templates   = 15
stages      = 24
cases       = 192
runtimes    = 7/7
data_policy = SYNTHETIC_ONLY
```

The configured roadmap remains:

```text
resume S19 from ISKRA1
-> S20 ... S40
-> require S40 execution_complete
-> require S40 consolidation COMMITTED
-> WEB01 ... WEB24
```

The S40 -> WEB01 live transition has not yet occurred and is not claimed here.

## Machine-readable public summary

See:

- [SSI_V5_S13_S18_ROUTING_PUBLIC_SUMMARY_20260929.json](SSI_V5_S13_S18_ROUTING_PUBLIC_SUMMARY_20260929.json)

The local full unique-case audit used for this public summary has:

```text
file = SSI_ROUTING_UNIQUE_CASES_RUN_20260926T064644Z_793783ad_20260929T000415Z.json
size = 2,300,390 bytes
sha256 = d34bab75ae416af4c896c1beffe4be9d237b38d4f0385402c86d6b1f15edd6c1
```

The public repository publishes the compact summary and bounded claims rather than proprietary/reconstructive runtime internals.

## Claim boundary

This evidence supports claims about recorded **software/runtime training execution, routing provenance, consolidation and recovery controls**.

It does not establish:

- physical drone or robot performance,
- physical safety,
- production readiness,
- independent external replication,
- automatic Champion execution,
- a measured percentage of exact-reuse vs full-flow routing,
- AGI or consciousness.
