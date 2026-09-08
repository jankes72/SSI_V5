# SSI V5 — Predeclared 7-BODY Micronetwork + V10 mechanism-test packages

**Recorded:** `2026-09-08`  
**Status:** `PREDECLARED / HASH-SEALED / NOT YET EXECUTED`  
**Execution gate:** technical-readiness audit + reviewer-interface readiness must pass before any package is executed  
**Executor:** Kilo procedural executor  
**Publication boundary:** these public package records describe frozen experiment protocols, deterministic test vectors/oracles, evidence schemas and public procedural tooling; they do not contain the private SSI/Micronetwork/V10/ISKRA implementation.

## Why these packages are public before execution

These seven packages were generated and hash-sealed before their research outcomes are known. This repository record creates a public, timestamped precommitment to the package identities, frozen inputs, acceptance rules and SHA-256 references before the corresponding BODY runs are executed.

Technical-readiness failures or repairs that occur before research execution do not retroactively change these frozen research contracts. A material contract change requires a new package version and a new hash. Each BODY receives an independent package and independent evidence chain.

## Package registry

| # | Target | Public record | ZIP SHA-256 | Frozen manifest SHA-256 | State |
|---:|---|---|---|---|---|
| EXP-01 | BODY_FROZEN | [`EXP01`](experiment_packages/20260908/EXP01_BODY_FROZEN/PACKAGE_PREDECLARATION.md) | `b1c937739115dc6f312484a826da4309861e66e0dda8954c52c0fdff8616f054` | `d8f4b10be107a3200f916b27913bc1102b5de30337f97941796bef666d8f8a7f` | `NOT_YET_EXECUTED` |
| EXP-02 | BODY ISKRA 1 — NICE | [`EXP02`](experiment_packages/20260908/EXP02_BODY_ISKRA1_NICE/PACKAGE_PREDECLARATION.md) | `ad9085a3476150b5fa3d5fc75e79a65c251b71830f669e5e287cd4f24040ec1d` | `2d5d299711f5d43d8b887a3dfe5c72016a4acdbe681eaeb86a0271a65a557aca` | `NOT_YET_EXECUTED` |
| EXP-03 | BODY ISKRA 2 — GUARDIAN | [`EXP03`](experiment_packages/20260908/EXP03_BODY_ISKRA2_GUARDIAN/PACKAGE_PREDECLARATION.md) | `6b33a6943ded3bc1d5ed81f773a0c20f4d613b2d6e186c3259d31b4abfc2d4d5` | `78021210a51d05a4fa375065835324d373eb016b35e065b03b941aaabce65651` | `NOT_YET_EXECUTED` |
| EXP-04 | BODY ISKRA 3 — JUSTICE | [`EXP04`](experiment_packages/20260908/EXP04_BODY_ISKRA3_JUSTICE/PACKAGE_PREDECLARATION.md) | `2b95f3c2025a812bd83c2a64fef9f75a2fc7bd8133f378ca2cf7be2a7bda6d4a` | `c437ac762a879489601e45b8a3b9407e0fe5d3f886b95ab214d0abd8cf11d2e2` | `NOT_YET_EXECUTED` |
| EXP-05 | BODY ISKRA 4 — EXPLORER | [`EXP05`](experiment_packages/20260908/EXP05_BODY_ISKRA4_EXPLORER/PACKAGE_PREDECLARATION.md) | `bf3cd59450a37d9caa2b4d5d520ddd534a78b33c276622181e21d13ba4e9cccb` | `20004c48a106123c81dbec7cfd4c940a19e6f5a975120829ef3659aed6429696` | `NOT_YET_EXECUTED` |
| EXP-06 | BODY ISKRA 5 — PRAGMATIST | [`EXP06`](experiment_packages/20260908/EXP06_BODY_ISKRA5_PRAGMATIST/PACKAGE_PREDECLARATION.md) | `79972f3eb72ea8998a4f6511cec11934eef535ed3e3a91098831b57165f4c23f` | `697aa41ff65d611e34e86d4b868bfe29522ba8908cb26a90ecfa93a2cce34222` | `NOT_YET_EXECUTED` |
| EXP-07 | BODY ISKRA 6 — SKEPTIC | [`EXP07`](experiment_packages/20260908/EXP07_BODY_ISKRA6_SKEPTIC/PACKAGE_PREDECLARATION.md) | `18ce3ae1a3ebd73d132c4292940a6a950c5177518835001c26679ca64053c844` | `ba832c05e85e99c95ebe4decf2ff32215bf60c2d6f61fc1484b17765d73d2fb1` | `NOT_YET_EXECUTED` |

## Shared frozen test family

All seven packages use the same mechanism-test family so later differences are not explained by changing the experiment contract between BODY lines. The family measures, where the runtime exposes the relevant behavior:

- Micronetwork and competence lifecycle evidence;
- Candidate -> Challenger -> Champion progression under existing thresholds only;
- Router V10 `FULL_FLOW`, `REUSE_TOP1`, `VERIFY_TOPK`, similarity/ambiguity boundaries and route timing;
- deceptive-similarity / false-reuse protection;
- controlled failure, repeated-failure anti-loop and recovery;
- persistence across a declared restart;
- CONTINUUM/Micronetwork/V10 consistency between backend evidence and the live reviewer interface;
- reviewer read-only enforcement;
- CPU/RAM/GPU/VRAM and infrastructure telemetry;
- PASS / FAIL / INCONCLUSIVE with failures, interruptions and restarts preserved.

## Execution order

```text
EXP-01 BODY_FROZEN
-> EXP-02 ISKRA 1 NICE
-> EXP-03 ISKRA 2 GUARDIAN
-> EXP-04 ISKRA 3 JUSTICE
-> EXP-05 ISKRA 4 EXPLORER
-> EXP-06 ISKRA 5 PRAGMATIST
-> EXP-07 ISKRA 6 SKEPTIC
```

Publishing a package record is not execution and does not imply PASS. At the time of this registry, all seven research outcomes remain `UNKNOWN`.

## Private implementation boundary

```text
PUBLIC = frozen protocol identity + vectors/oracles contract + evidence schema + hashes + sanitized outputs
PRIVATE = SSI source + Micronetwork source + V10 implementation + ISKRA implementation + private memory/configuration/paths/secrets
```

The SHA-256 values above precommit the exact generated ZIP artifacts. A later published or reviewer-supplied copy is valid only if its bytes reproduce the recorded digest.