# SSI V5 — Predeclared 7-BODY TRAIN-C -> S3 Package Registry

**Recorded:** `2026-09-09`  
**Status:** `PREPARED / HASH-IDENTIFIED / NOT YET EXECUTED`  
**Packages:** `7 = one independent TRAIN-C package per BODY line`  
**Stage:** `S2 -> TRAIN-C CHILD / APPLIED AUTONOMY -> S3`  
**Future experiment-entry gate:** `S5`

This registry records the prepared TRAIN-C packages before their execution outcomes are known.

## Shared curriculum identity

```text
TRAIN_C_CHILD_APPLIED_AUTONOMY_CURRICULUM_SHA256
= 4f9bb32d9a7f6074357b1f1eb55e539ab0e70e7ccc44bea73b10f2ca916061b5
```

All seven packages use the same 12-module / 60-step curriculum core.

## Package registry

| Package | Target | Steps | ZIP SHA-256 | Manifest SHA-256 | State |
|---|---|---:|---|---|---|
| `SSI_TRAIN01C_BODY_FROZEN_CHILD_APPLIED_AUTONOMY_V1_20260909` | `BODY_FROZEN` | 60 | `ef8a4d5bef4714a636982084b224c6320a7f98d520f081c253270b27f56feac6` | `d1362864a1f04c98ba057dffca3887098efd3b55c011fc39aa651d4097821a75` | `PREPARED_NOT_EXECUTED` |
| `SSI_TRAIN02C_BODY_ISKRA1_NICE_CHILD_APPLIED_AUTONOMY_V1_20260909` | `BODY_ISKRA1_NICE` | 60 | `2087856c502c18ba4a996cb6f9288cba0e8e1aca39d02c3ba9a563077350fee0` | `8c07b606b258ad1a829f782500d3af16d0a63a027dc81d3a0f4d6a62f3d0170d` | `PREPARED_NOT_EXECUTED` |
| `SSI_TRAIN03C_BODY_ISKRA2_GUARDIAN_CHILD_APPLIED_AUTONOMY_V1_20260909` | `BODY_ISKRA2_GUARDIAN` | 60 | `5ce32f26b424e9d3e06d7e2f950e18d9a8066dd9a07c1bee2f08d60d38577e8c` | `39285b97f9f9f8d8d77652b3f699565be47928642aaf4a823daba31c3af73280` | `PREPARED_NOT_EXECUTED` |
| `SSI_TRAIN04C_BODY_ISKRA3_JUSTICE_CHILD_APPLIED_AUTONOMY_V1_20260909` | `BODY_ISKRA3_JUSTICE` | 60 | `5fbb883a0932001b9d3921a889d8f67d1bcea256a7513a5e0c5af97957d4f3a1` | `7839cfb1102c2650e640c1819450747b41132189bdf22ddae444891ba7e77edf` | `PREPARED_NOT_EXECUTED` |
| `SSI_TRAIN05C_BODY_ISKRA4_EXPLORER_CHILD_APPLIED_AUTONOMY_V1_20260909` | `BODY_ISKRA4_EXPLORER` | 60 | `43c7115147aaaa55c6f5b92b0b942a7e6ee239adf258ba06393c04936d7dbaf6` | `49fdda272818e1cbd4a7adc4e7d486eb03a3b1832d97e67726b4fdb52aca74d5` | `PREPARED_NOT_EXECUTED` |
| `SSI_TRAIN06C_BODY_ISKRA5_PRAGMATIST_CHILD_APPLIED_AUTONOMY_V1_20260909` | `BODY_ISKRA5_PRAGMATIST` | 60 | `9fa2c7fc09a67c852e9b1478f731775f53fe425082ebe160893d27e81f6cf603` | `2491e0d4d9f3ed09d778b31dab9b0b0f69ca4b04d3c45e70e8e22548ea3ef04b` | `PREPARED_NOT_EXECUTED` |
| `SSI_TRAIN07C_BODY_ISKRA6_SKEPTIC_CHILD_APPLIED_AUTONOMY_V1_20260909` | `BODY_ISKRA6_SKEPTIC` | 60 | `36f50348d61920181b51589a584080356c3d9812df349c71b16ea10d94655c15` | `90699f1e259bd52d98fa1bd1791e9b3fb0f156f8dbd5f47e319c1e93f32a6e79` | `PREPARED_NOT_EXECUTED` |

## Master local bundle integrity

The seven package ZIPs are also grouped in a local execution bundle:

```text
SSI_7BODY_TRAIN_C_S3_PACKAGES_V1_20260909.zip
SHA256 = ec778258e7eee7eaab9d427a94929d22d51aa0a7fac2ac7d977d0d24e6f860ee
```

The public repository records package identities, hashes, curriculum, methodology and claim boundaries. Private SSI implementation remains outside the public mirror.

## TRAIN-C common structure

Each BODY package contains 12 modules, each executed as:

```text
INSTRUCTION
-> GUIDED_PRACTICE
-> BLIND_FIRST
-> IMMEDIATE_EXACT_REPEAT
-> NEAR_TRANSFER
```

Therefore:

```text
60 steps per BODY
420 declared TRAIN-C steps across seven BODY lines
```

`IMMEDIATE_EXACT_REPEAT` is a speed/reuse measurement only when the preceding `BLIND_FIRST` passed. Otherwise it is classified as recovery/retest and is not counted as an exact-memory speed benchmark.

## Lineage rule

For each BODY line:

```text
identified TRAINED_START_S2
-> TRAIN-C
-> versioned CHILD_S3
```

Historical T0/S1/S2 states remain preserved.

No S3 result is claimed before execution.

## Future maturity ladder

The experiment-entry requirement is now prospectively extended to:

```text
S3
-> TRAIN-D
-> S4
-> TRAIN-E
-> S5
-> held-out mechanism tests
-> 21 cross-domain experiments
```

TRAIN-D/E packages are not yet frozen or claimed.

## Claim boundary

This registry proves only that seven TRAIN-C packages were prepared and hash-identified before execution outcomes were known. It does not prove that TRAIN-C will pass, that all seven S3 states will exist, that S4/S5 will pass, that later experiments will pass, or that any speedup will occur.