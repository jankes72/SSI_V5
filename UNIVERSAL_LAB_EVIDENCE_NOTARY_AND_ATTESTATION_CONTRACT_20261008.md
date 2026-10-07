# SSI Universal Lab — Evidence, Digital Signature and Independent Notary/Attestation Contract — 2026-10-08

**Status:** `PREREGISTERED R5+ EVIDENCE HARDENING TARGET / NOT YET CLAIMED AS INDEPENDENTLY ATTESTED`  
**Scope:** Universal Lab live research sessions, Director/CZARA/Shadow events, Router decisions, BODY_FROZEN receipts, ZeroLab validation and partner-safe session export.  
**Architecture rule:** this document specifies the evidence/notary contract. The current structural map remains [SSI V5 — C4 Architecture](SSI_V5_C4_ARCHITECTURE.md).  
**Historical continuity:** this contract carries forward SSI V5 evidence-hardening requirements already preregistered before S20 and influenced by external DEV review.

## 1. Why this contract exists

Universal Lab is intended to turn a research meeting into an inspectable SSI session rather than a conventional video call. For that claim to remain meaningful, the meeting evidence must not depend only on the same runtime that produced the result.

The target is therefore:

```text
LIVE UNIVERSAL LAB SESSION
-> append-only event/evidence records
-> monotonic sequence
-> previous-record hash
-> local digital signature
-> executor/verifier permission separation
-> independent signing/notary authority where external attestation is claimed
-> final session manifest
-> partner-safe export
```

A local hash chain can establish internal consistency. It must **not** be described as independent attestation unless a signing/notary authority separated from the executor/operator has actually attested the relevant records or manifest.

## 2. Universal Lab evidence objects

Where the real backend emits the relevant event, the session evidence should bind:

- session ID and session version;
- participant identity/role;
- original transcript text and translation;
- timestamp and monotonic sequence number;
- Director interaction ID;
- bounded CZARA/Shadow event type;
- Router V10 route decision and timing;
- selected Micronetwork/Champion reference where disclosure is permitted;
- BODY_FROZEN task ID and receipt reference;
- ZeroLab protocol ID, protocol hash and method hash;
- PASS / FAIL / INCONCLUSIVE verdict;
- evidence record ID;
- previous-record hash;
- current-record hash;
- local signing identity;
- external attestation state;
- final manifest hash.

Raw private prompts, credentials, provider secrets, chain-of-thought and reconstructive proprietary internals remain outside the partner-safe evidence package.

## 3. Session chronology

Universal Lab should preserve one auditable event chronology:

```text
participant message / transcript
-> translation (when needed)
-> Director/CZARA context event
-> Router decision
-> optional Shadow proposal
-> Director review
-> host approval where required
-> BODY_FROZEN task
-> ZeroLab execution / validation
-> verdict
-> evidence record
-> signature / attestation state
```

The frontend must not fabricate missing backend events, timestamps, route IDs, confidence values or evidence receipts.

## 4. Append-only hash-chain contract

Target per-record integrity fields:

```text
session_id
sequence
event_id
event_type
actor
timestamp
payload_hash
previous_record_hash
record_hash
signature
signing_key_id
attestation_state
```

Required properties:

1. sequence is monotonic within the declared chain;
2. every record after the first binds the previous record hash;
3. signed/hash-dependent fields are declared before measured use;
4. a later correction creates a new record/version and does not rewrite committed history;
5. FAIL and INCONCLUSIVE remain in the chain;
6. a cosmetic field may be excluded only if that exclusion was declared before the result.

## 5. Executor, verifier and notary separation

Target authority model:

```text
EXECUTOR
= produces action/result

VERIFIER
= checks the declared protocol/result

LOCAL SIGNER
= signs the committed local evidence record

INDEPENDENT NOTARY / ATTESTATION AUTHORITY
= externally attests the record/manifest when independent attestation is claimed
```

No single role should silently collapse all four authorities when the public claim uses words such as **independent**, **externally attested**, **partner-signed** or **notarized**.

The external signer/notary should not rely on private SSI execution authority to rewrite the already committed evidence.

## 6. Partner-signed/frozen manifest option

For an external research session or benchmark, Universal Lab should support a frozen manifest before execution when practical.

The manifest may bind:

- session/benchmark identity;
- SSI version and target actors;
- protocol version;
- acceptance criteria;
- disclosed inputs and constraints;
- expected evidence schema;
- negative control definition;
- notary/signing policy;
- allowed degraded-mode behavior.

A partner signature on the frozen manifest is useful evidence that the criteria existed before the outcome was known. It is not, by itself, validation of the final result.

## 7. Evidence-chain adversarial tests

Before an externally attested Universal Lab session is claimed, the verifier suite should include at least:

1. committed-record mutation;
2. deletion of an earlier record;
3. fabricated PASS using an unregistered protocol;
4. previous-hash-only mutation;
5. missing-sequence test;
6. duplicate sequence;
7. out-of-order record insertion;
8. signature mismatch;
9. wrong signer/key ID;
10. tampered final manifest;
11. negative control changing a declared field outside the signed payload.

Expected behavior:

```text
hash/signature-dependent mutation
-> REJECT for the chain-specific reason

missing/out-of-order sequence
-> REJECT for sequence discontinuity

unregistered-protocol PASS
-> REJECT

declared cosmetic negative-control mutation
-> chain remains valid
```

The test report should preserve **why** a record was rejected, not only that it was rejected.

## 8. Notary/signing outage state machine

Universal Lab inherits the preregistered SSI notary outage policy:

```text
NOTARY_AVAILABLE
-> EXTERNALLY_ATTESTED

NOTARY_UNAVAILABLE
-> LOCAL_COMMITTED
-> PENDING_EXTERNAL_ATTESTATION
-> bounded append-only queue

BUFFER LIMIT REACHED
-> DEGRADED_SAFE_MODE
```

In `DEGRADED_SAFE_MODE`:

- STOP is allowed;
- PAUSE is allowed;
- SAFE_STATE is allowed;
- silent promotion to `EXTERNALLY_ATTESTED PASS` is prohibited;
- dropping the oldest pending evidence is prohibited;
- overwriting pending evidence is prohibited;
- ordinary new externally-claimed mission authority is blocked unless explicitly preregistered otherwise.

Parameters to freeze before an externally attested run include:

```text
notary_timeout_s
buffer_max_records
buffer_max_bytes
buffer_max_age_s
buffer_limit_action
allowed_actions_when_degraded
backfill_policy
external_pass_requires_attestation = true
drop_oldest = false
overwrite = false
```

## 9. Required outage/backfill tests

At minimum:

- notary offline at session start;
- notary lost mid-session;
- reconnect with partially filled buffer;
- buffer limit reached;
- reboot with pending buffer;
- backfill after reconnect;
- duplicate backfill;
- out-of-order backfill;
- tampered buffered record;
- local signer available but external attestation unavailable;
- external attestation received for an old manifest after a newer session version exists.

## 10. Universal Lab partner-safe export

The final shareable package should be able to contain:

```text
SESSION MANIFEST
+ transcript / translation
+ Director interactions
+ bounded CZARA/Shadow events
+ Router decisions/timings
+ BODY task receipts
+ ZeroLab protocol/results
+ PASS/FAIL/INCONCLUSIVE history
+ evidence hashes
+ local signature metadata
+ external attestation metadata when available
+ verification instructions
```

The export should state one of the following explicitly:

- `LOCAL_HASH_LINKED`
- `LOCALLY_SIGNED`
- `PENDING_EXTERNAL_ATTESTATION`
- `EXTERNALLY_ATTESTED`

These states must not be conflated.

## 11. Current implementation boundary — 2026-10-08

Current public evidence supports:

- SSI evidence/provenance concepts and historical hash/evidence hardening;
- preregistered signed append-only and notary separation requirements;
- preregistered notary outage and buffer-limit policy;
- ZeroLab V2 bounded evidence flow;
- Universal Lab installed R3 baseline and R5 evidence/export design.

Current public evidence does **not** yet establish:

- a live independent notary signing Universal Lab records;
- a production signing-key infrastructure;
- completed partner-signed Universal Lab manifests;
- completed end-to-end externally attested R5 meeting;
- independent external validation merely because a local hash chain exists.

## 12. DEV review provenance and attribution

This contract is a direct continuation of evidence-hardening questions raised publicly in DEV discussions and already attributed in the repository.

### Hamid Ahmadian

Material review themes already recorded by SSI include:

- executor should not be the only authority attesting its own success;
- mutable evidence remains vulnerable even with a verifier;
- use append-only signed evidence;
- separate signing authority from executor/operator where independent attestation is claimed;
- test mutation, deletion and forged PASS;
- bind previous-record hash and monotonic sequence;
- prove the reason for rejection;
- define external notary outage behavior;
- define behavior when the unsigned-attestation buffer fills.

### Raju Dandigam

The repository also records feedback around a frozen partner-signed manifest and independently recomputable evidence boundary.

### Listwright

The repository records feedback around negative controls and explicit `UNTESTED` classification when a metric cannot demonstrate an opposite outcome.

Attribution is not endorsement, authorship of SSI, implementation validation or an independent audit.

## 13. Related records

- [Pre-S20 observability and evidence hardening preregistration](SYSTEM/SSI_V5_PRE_S20_OBSERVABILITY_AND_EVIDENCE_HARDENING_PREREGISTRATION_20260929.md)
- [External review feedback and attribution](EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md)
- [Universal Lab installed state and R5 boundary](SYSTEM/SSI_UNIVERSAL_LAB_STATUS_20261007.md)
- [Universal Lab partner meeting start](UNIVERSAL_LAB_MEETING_START_HERE_20261007.md)
- [ZeroLab V2 first results](ZERO_LAB_V2_FIRST_RESULTS_20261002.md)

Public DEV context:

- Building an evidence-first multi-agent system: 720 paired missions, rollback, and strict claim boundaries
- Before the GitHub Release: Two Isolated Zero Labs for CZARA and SSI V5 Final
- Universal Lab: turning an AI research meeting into a live, inspectable experiment on modest hardware

## Final claim boundary

This document freezes the **intended Universal Lab evidence/notary contract before the externally attested result exists**.

It does not claim that the independent notary layer is already deployed. When that layer becomes live, the repository should publish the concrete signer/notary identity boundary, key/protocol version, adversarial test results, outage/backfill test results and at least one verifiable session manifest before using the claim `EXTERNALLY_ATTESTED`.
