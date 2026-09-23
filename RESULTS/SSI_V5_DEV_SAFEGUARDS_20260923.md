# SSI V5 — safeguards informed by DEV feedback — 23 September 2026

**Scope:** implemented software controls and local regression evidence. External pilot readiness remains **false**.

## Attribution and requirement mapping

The [DEV discussion](https://dev.to/jankes72/building-an-evidence-first-multi-agent-system-720-paired-missions-rollback-and-strict-claim-3n5h) supplied concrete challenges. Hamid Ahmadian proposed alteration, deletion and forged-protocol tests, plus signed sequencing and separately controlled keys. Listwright proposed negative controls, explicit untested status and retention of contradictory source views. Raju Dandigam asked for a frozen manifest and partner-verifiable evidence. These were review suggestions, not audits, endorsements or demonstrations of a breach.

| Requirement | Implemented response | Verified scope / open boundary |
|---|---|---|
| Detect altered evidence | Ed25519 signatures over sequenced records linked to the previous record, registered protocols and report hashes | Local cryptographic verifier exercised on controlled fixtures |
| Detect removal | Sequence/previous-record checks; comparison against an independently retained head where supplied | Interior deletion detected; tail truncation needs a trusted head |
| Reject fabricated acceptance | Protocol registration and result binding | Unregistered-protocol PASS rejected in the fixture test |
| Separate signing authority | Optional separate-UID custodian path | Actual two-UID socket/key isolation test skipped here; operator separation not demonstrated |
| Check that metrics can change | Opposing inputs through actual aggregation functions and acceptance-rule parsing | All 30 curriculum rule sets covered; this is aggregation testing, not execution of S12–S40 |
| Expose missing measurements | UNTESTED for absent/inapplicable/unexercised signals | Does not default missing evidence to zero or PASS |
| Preserve disagreements | Retain each view and classify unresolved disagreement as INCONCLUSIVE | Synthetic conflicting-view and stage-audit tests passed |
| Freeze experiment identity | Register protocol, requirements, baseline/candidate, seed and repetitions before execution | Partner signature and complete independent recomputation remain unestablished |

## Tampering tests: five attempts, five detected

The original three challenges were supplemented with tail truncation and source-report alteration. A valid baseline chain was accepted first. The [machine-readable attack report](SSI_V5_EVIDENCE_ATTACK_TESTS_20260923.json) records:

| Controlled attack | Actual rejection | Detected |
|---|---|---|
| Change FAIL to PASS and recompute the content hash | SIGNATURE_INVALID | Yes |
| Delete an earlier record | CHAIN_SEQUENCE_GAP | Yes |
| Submit a fabricated PASS for an unregistered protocol | UNREGISTERED_PROTOCOL | Yes |
| Truncate the tail while retaining the trusted head | TRUSTED_HEAD_MISMATCH | Yes |
| Modify a referenced source report | REPORT_CHANGED | Yes |

These are verifier tests on isolated data, not attacks conducted by Hamid and not a demonstrated historical SSI compromise. Application-level append-only handling and signatures do not make a store invulnerable to an administrator controlling both storage and the signing key. The actual run remains LOCAL_DEVELOPMENT; external timestamping is NOT_CONFIGURED. No external notary or independent key custody is claimed.

## Negative controls found a real limitation

The measurement checks cover more than 180 metric checks across the 30 actual curriculum rule sets using opposing synthetic records. Separate positive/negative controls exercise 67 variants through unchanged validators. These numbers describe different test layers and must not be added to the 210 training cases or treated as flights.

S40's native evaluator records `lab_access_revoked=True` unconditionally. Its aggregation can respond to synthetic input, but that does not prove access revocation occurred. The new control labels the actual `access_revoke_verified` guard **UNTESTED** and blocks paid S40 acceptance until a measurable revocation path is supplied. This unresolved issue is preserved rather than bypassed to complete the curriculum. Independent LLM judgment also remains UNTESTED in the deterministic guard-control suite.

## Release evidence and chronology

The R3 ZIP entrypoint completed with **105 passing tests and one skipped test out of 106** in nine suites. Tests cover source/integrity checks, rollback, event flow, budget reservations, signed evidence, training variants, measurement controls, captured failures and shared LAB diagnostics. The [test summary](SSI_V5_LAB_RND_R3_TEST_SUMMARY_20260923.json) and [per-test list](../evidence/S11_20260923/release_test_results.json) disclose the skipped separate-UID custodian test.

The [previous S11 run](SSI_V5_S11_FULL_RESULTS_20260923.md) completed before these R3 changes. Its outcomes remain 197 PASS, 12 INCONCLUSIVE and 1 FAIL. The uploaded run did not contain a measurement-controls report. Offline safeguards testing cannot retroactively certify that run or establish external pilot readiness. The new package has been delivered, with operator installation and the next training result awaiting evidence.
