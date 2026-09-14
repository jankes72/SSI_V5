# SSI V5 — Drone Measured Results — 2026-09-14

**Status:** `EXECUTED SOFTWARE BENCHMARK / MEASURED RESULTS`

These are measured values from executed software-domain runs. They are not illustrative presentation numbers.

## Benchmark scope

```text
11 drone scenarios
4 execution profiles: FAST / PARTIAL / FULL / MAX-SAFETY
```

Representative measured flow costs:

```text
route_blocked
FAST 12.265 ms
PARTIAL 17.394 ms
FULL 22.300 ms
MAX 30.105 ms

multi_fault
FAST 21.835 ms
PARTIAL 30.966 ms
FULL 39.700 ms
MAX 53.595 ms
```

Scoped comparative post-consolidation result:

```text
median speedup ~= 1.384x
median flow-cost reduction ~= 27.76%
```

A `wind_corridor` PASS→FAIL post-consolidation regression was also observed and preserved. This result is intentionally public because it demonstrates that consolidation is not assumed beneficial and must pass a regression gate.

A measured public-demonstrator consolidation hook executed in `0.147 ms`, with competence-pool availability changing from `6/5/5` to `8/8/8`. This timing is specifically the software-demonstrator hook and is not claimed to represent complete production Router S10 global-consolidation latency.

## Timing interpretation

`flow_cost_ms` and wall-clock values are actual runtime measurements from executed software tests. They are not physical-aircraft response times.

## Claim boundary

Supported: measured software flow-depth differences, measured scoped consolidation effects, preserved regression evidence.

Not claimed: certified physical flight performance, universal consolidation benefit, universal superiority over existing UAV systems.

See also:

- [`PUBLIC_SHOWCASE_AND_MEASURED_DOMAIN_TRANSFER_EVIDENCE_20260914.md`](PUBLIC_SHOWCASE_AND_MEASURED_DOMAIN_TRANSFER_EVIDENCE_20260914.md)
- [`DRONE_DOMAIN_RND_COLLABORATION_STATUS_20260914.md`](DRONE_DOMAIN_RND_COLLABORATION_STATUS_20260914.md)
