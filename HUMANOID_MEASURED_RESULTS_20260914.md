# SSI V5 — Humanoid Measured Results — 2026-09-14

**Status:** `EXECUTED SOFTWARE BENCHMARK / MEASURED RESULTS`

These values come from executed humanoid software-domain scenarios. They are not illustrative presentation values.

## Benchmark scope

```text
H00-H14 scenario family
baseline + consolidated paths
30 measured scenario runs
13/13 humanoid self-tests PASS
```

Representative measured simulator-clock events:

```text
H00 hard stop = 2.90 s simulation time
H00 PASS_AFTER_LEARNING = 11.46 s simulation time
H01 RECOVERING = 0.14 s simulation time
H01 FALL = 0.34 s simulation time
H13 FALL -> STABILIZED = 0.08 s simulation time
```

In H01, the first forced slip produced a fall. The retry retained experience, selected `PREEMPTIVE_SLIP_PREP`, and completed without the corresponding fall observed in the first attempt.

This provides a measured before/after software-domain result:

```text
ATTEMPT 1 -> FALL
EXPERIENCE RETAINED
ATTEMPT 2 -> PREEMPTIVE PREPARATION -> NO CORRESPONDING FALL
```

## Timing interpretation

`simulation time` is the actual timestamp/interval produced by the executed simulator. It must not be re-labelled as physical humanoid response or stand-up time.

Python wall-clock/test execution time is a separate quantity and should not be mixed with simulated motion time.

## Claim boundary

Supported: measured software-state timing, before/after retained-experience behavior, executed scenario/self-test evidence.

Not claimed: physical humanoid timing equivalence, production robotics readiness, complete biomechanical fidelity or universal superiority over physical humanoid controllers.

See also:

- [`PUBLIC_SHOWCASE_AND_MEASURED_DOMAIN_TRANSFER_EVIDENCE_20260914.md`](PUBLIC_SHOWCASE_AND_MEASURED_DOMAIN_TRANSFER_EVIDENCE_20260914.md)
- [`HUMANOID_DOMAIN_TRANSFER_RND_STATUS_20260914.md`](HUMANOID_DOMAIN_TRANSFER_RND_STATUS_20260914.md)
