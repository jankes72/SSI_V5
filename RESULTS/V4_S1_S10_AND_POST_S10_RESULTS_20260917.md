# SSI V4 — complete S1-S10 + post-S10 software-domain results

**Date:** 2026-09-17  
**Run ID:** `RUN_20260917T024400_DCD7FD`  
**Trace root:** `TRACE_5EE50008986B`  
**Status:** COMPLETE / PASS

## Executive result

A complete V4 training run progressed through S1 -> S10 with all required stage barriers completed. The final S10 state records all seven BODY lines as PASS, consolidation PASS, regression PASS, rollback not required, and advancement allowed.

```text
FINAL_STAGE = S10
COMPLETE = true
CONSOLIDATION = PASS
REGRESSION = PASS
ROLLBACK = NOT_REQUIRED
ADVANCE_ALLOWED = true
```

## BODY results

```text
BODY_FROZEN = PASS
ISKRA1      = PASS
ISKRA2      = PASS
ISKRA3      = PASS
ISKRA4      = PASS
ISKRA5      = PASS
ISKRA6      = PASS
```

## Training order observed

The run followed the intended staged structure:

```text
S1: ISKRA1-6 train independently
    -> consolidation + promotion + bridge

S2-S10:
    BODY_FROZEN first
    -> ISKRA1-6
    -> stage barrier
    -> consolidation + promotion + bridge
    -> regression verification
    -> continue only on PASS
```

Every stage S1-S10 reached PASS under the same run ID.

## Runtime retry evidence

The orchestration also exercised its transient runtime recovery path without converting transient unavailability into a false failure.

Observed retries included:

```text
S2  ISKRA4: PREFLIGHT RETRY 1/5 - RUNTIME OFFLINE -> recovered -> PASS
S10 ISKRA5: PREFLIGHT RETRY 1/5 - RUNTIME OFFLINE -> recovered -> PASS
```

These events are retained as positive fail-closed/recovery evidence: the runner did not silently bypass the runtime check, and the stage advanced only after the runtime became available and the BODY completed successfully.

## Consolidation / promotion / bridge

For every training stage, the orchestration recorded:

```text
CONSOLIDATION + PROMOTION + BRIDGE = PASS
```

The final S10 descendant was accepted only after regression verification.

## Final BODY_FROZEN reload verification

The final promoted BODY_FROZEN reload recorded:

```text
reload_verify.ok = true
expected_count = 144
loaded_count = 144
artifact_count = 4
complete_accounting = true
loader = MicronetworkSystem.reload
fresh_process = true
```

This is the final accounting check for the promoted skill state in this run.

## Evidence volume

The sanitized public evidence builder found:

```text
training JSON files = 229
PASS-status JSONs = 76
FAIL-status JSONs = 0
OTHER JSONs = 153
```

`OTHER` means metadata/state/report records without a top-level PASS/FAIL status; it does not mean failure.

Stage-related file hits in the sanitized evidence tree:

```text
S1  = 63
S2  = 37
S3  = 35
S4  = 36
S5  = 36
S6  = 36
S7  = 37
S8  = 30
S9  = 30
S10 = 159
```

These counts are evidence-file references, not counts of independent training cases.

# Post-S10 domain experiments

After the completed training/consolidation run, the trained V4 BODY_FROZEN provenance was carried into two software-domain transfer harnesses.

## Drone software lab

```text
status = PASS
scenario_count = 6
```

Scenarios recorded in the final result:

1. `unit_loss_hole`
2. `urban_link_blackspot`
3. `gnss_memory_zone`
4. `battery_critical`
5. `wind_corridor`
6. `route_blocked`

The drone evidence records progressive competence-family availability across the scenario sequence, including concepts such as space takeover, blackspot memory, GNSS-denied recovery, battery handover, wind-corridor avoidance and counterfactual rerouting.

The public domain harness explicitly preserves a simulation-only boundary. It does not claim physical drone validation.

## Humanoid software lab

```text
status = PASS
scenario_count = 15
```

Scenarios:

```text
H00 H01 H02 H03 H04
H05 H06 H07 H08 H09
H10 H11 H12 H13 H14
```

The final record includes baseline versus post-consolidation outcomes. One visible example is H00:

```text
before_state = STABLE
baseline_outcome = HARD_STOP
post_consolidation_outcome = RUNNING
post_state = STABLE
```

The humanoid harness is software-domain evidence only and does not claim physical humanoid validation.

## Combined post-S10 count

```text
6 drone scenarios
+ 15 humanoid scenarios
= 21 post-S10 software-domain scenarios
```

## Provenance hashes retained in the final record

The final result records BODY_FROZEN provenance hashes for the state used by the domain harnesses, including:

```text
micronetwork_artifacts SHA256 = 5286fbb46954672d30065f5c811335d1f3f72bccdced2d6eea3c52314f62e3ea
micronetwork_candidates SHA256 = fb420adca7ef4cdf56ebcdce5aa8813f3a73958828643f6f9e005c5cf10c095f
CONTINUUM SHA256 = 9feff7630ffae92fe6abdf5dfafe5d774eb6dac71d83b6adeb6f22fed8d929cf
```

The candidate provenance record contains 144 candidate files; the CONTINUUM provenance record contains 71 files.

# Claim boundary

This publication supports the narrow engineering claim that:

- this V4 run completed S1-S10 under one run ID;
- all required BODY results at S10 were PASS;
- stage consolidation/promotion/bridge completed;
- final regression passed;
- rollback was not required;
- the promoted Frozen reload accounted for 144/144 expected items;
- the post-S10 drone and humanoid software harnesses returned PASS for 6 and 15 scenarios respectively.

It does **not** establish:

- physical drone performance;
- physical humanoid performance;
- independent external replication;
- universal superiority of V4 over V1/V2/V3;
- universal cross-domain transfer;
- production readiness;
- AGI or consciousness.

## Public/private boundary

The public repository intentionally excludes the private `DESCENDANTS/` tree, proprietary implementation source, local database state, executable ROOT internals and secrets. The public evidence layer contains sanitized results, counts, hashes, provenance and claim boundaries only.
