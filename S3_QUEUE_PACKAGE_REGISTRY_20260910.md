# SSI V5 — One ZIP per BODY S3 Queue Registry

**Recorded:** `2026-09-10`  
**Status:** `PREPARED / HASH-IDENTIFIED / LOCAL EXECUTION ARTIFACTS`  
**Scope:** `7 BODY lines / sequential training to S3`

This registry records the seven local queue archives prepared to reduce repeated package discovery and executor overhead during the sequential training program.

The public repository records the queue identities and SHA-256 values only. The executable/local ZIP payloads are not published here because this repository is an evidence mirror rather than a proprietary source-code distribution.

| Order | BODY | Queue ZIP | SHA-256 | Authorized stages |
|---:|---|---|---|---|
| 01 | BODY_FROZEN | `SSI_S3_QUEUE_01_BODY_FROZEN_ONE_ZIP_V1_20260910.zip` | `1f3da18544d322ef1723d91858944090baa02b6677836ce82298485f0ad88737` | TRAIN-B -> S2 -> TRAIN-C -> S3 |
| 02 | ISKRA1 NICE | `SSI_S3_QUEUE_02_ISKRA1_NICE_ONE_ZIP_V1_20260910.zip` | `070894d16cebcd3ff44971f2df465c305cc79260cfc7e44a218fa76a533d6e4f` | TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 |
| 03 | ISKRA2 GUARDIAN | `SSI_S3_QUEUE_03_ISKRA2_GUARDIAN_ONE_ZIP_V1_20260910.zip` | `e9261eeeebe165c99091b88a077ad2439e46ccfc5a33339c33004dde69046137` | TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 |
| 04 | ISKRA3 JUSTICE | `SSI_S3_QUEUE_04_ISKRA3_JUSTICE_ONE_ZIP_V1_20260910.zip` | `f63e920b764d280d96798a34a3b6e50880ec1d971de8aa2749b31adc06142458` | TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 |
| 05 | ISKRA4 EXPLORER | `SSI_S3_QUEUE_05_ISKRA4_EXPLORER_ONE_ZIP_V1_20260910.zip` | `886f3a5908b4d5901d961b909a51065b9bd73db04653a8ab155a37feb02038e6` | TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 |
| 06 | ISKRA5 PRAGMATIST | `SSI_S3_QUEUE_06_ISKRA5_PRAGMATIST_ONE_ZIP_V1_20260910.zip` | `28a971ad7a08e2a5838b99fb6e89586601c3bb704f95f7928ff4f4b39d858807` | TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 |
| 07 | ISKRA6 SKEPTIC | `SSI_S3_QUEUE_07_ISKRA6_SKEPTIC_ONE_ZIP_V1_20260910.zip` | `a22ffcbd14dc4e2970eb5a1929d261209cd9175ca7b534cc1b484c6fa2206a7c` | TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 |

## Execution order

```text
BODY_FROZEN -> S3
then ISKRA1 -> S3
then ISKRA2 -> S3
then ISKRA3 -> S3
then ISKRA4 -> S3
then ISKRA5 -> S3
then ISKRA6 -> S3
```

The queue is sequential by BODY. A later BODY is not intended to start merely because the current BODY completed only one phase.

## Local blocker rule

For a BODY-local FAIL, INCONCLUSIVE or ambiguous local critical error, preserve evidence, mark that BODY/stage BLOCKED or INCOMPLETE, perform no silent repair, and move to the next BODY.

## Global blocker rule

If the problem threatens integrity or comparability of later runs — for example package/hash mismatch, shared runtime corruption, evidence persistence failure, wrong BODY mapping or disclosure/security failure — stop the entire queue and preserve evidence.

## Public disclosure boundary

Only sanitized evidence, package identities/hashes, stage results, safe state hashes, measured timings/routes and claim boundaries may be published. Proprietary source code, private prompts, credentials, secrets and reconstructive runtime internals remain private.

See [`BODY_S3_TRAINING_START_HERE_20260910.md`](BODY_S3_TRAINING_START_HERE_20260910.md).