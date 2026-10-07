# SSI V5 — External review feedback and attribution — 29 September 2026

This record identifies external review comments that materially changed SSI V5 requirements. It exists to preserve attribution and chronology.

**Important boundary:** feedback attribution is not authorship of SSI V5, endorsement of SSI V5, independent validation, or a claim that the reviewer audited the private implementation.

## Amnezja / @amnezja3 (Mikael) — early CZARA co-creator / seed contributor

**Author/operator attribution — added 2026-10-08.**

Paweł Jankiewicz identifies **Amnezja / [@amnezja3](https://github.com/amnezja3) (Mikael)** as an early co-creator of the CZARA direction. According to the author/operator chronology, Amnezja **seeded the initial idea and performed the first connection/integration step that brought CZARA into the SSI work**, after which Paweł developed, expanded and integrated CZARA into the broader SSI V5 research programme, including its later training, Director_Czary, ZeroLab and Universal Lab paths.

Attribution boundary:

- this credit concerns the **origin / early connection of CZARA**, not authorship of the whole SSI V5 system;
- Paweł remains the author/operator responsible for the later architecture, implementation, training programme, integration and published claims;
- this repository update does not independently verify Amnezja / [@amnezja3](https://github.com/amnezja3) (Mikael)'s exact GitHub handle/profile, so no profile URL is invented here;
- the author identifies Amnezja as his GitHub follower and early collaborator; that follower relationship is recorded here as author-supplied provenance, not as a GitHub-API verification claim.

A more exact profile link or dated technical artifact can be added later without changing this historical attribution.

## Hamid Ahmadian — DEV Community feedback

Discussion:
https://dev.to/jankes72/building-an-evidence-first-multi-agent-system-720-paired-missions-rollback-and-strict-claim-3n5h

Hamid Ahmadian's comments materially influenced the evidence-hardening work and the pre-benchmark protocol.

| Date | Review concern / suggestion | SSI response |
|---|---|---|
| Sep 20 | Self-attestation risk: the executor should not be the only authority attesting its own success | Explicit executor/verifier separation requirement and stricter claim boundary |
| Sep 21 | Mutable evidence remains vulnerable even with an independent verifier | Append-only signed evidence and separated signing authority added as requirements |
| Sep 22 | Adversarial tests should include committed-record mutation, deletion, and forged PASS using an unregistered protocol | Dedicated evidence attack tests and protocol binding |
| Sep 22 | Hash chain should include previous-record hash and monotonic sequence; signing key should not be controlled by the executor/operator where independent attestation is claimed | Hash-chain/signing design requirement |
| Sep 23 | Do not only prove “rejected”; prove **why** it was rejected — isolate previous-hash mismatch and missing sequence | Chain-specific causal controls added to the next verifier suite |
| Sep 23 | External notary/signing availability is a real design decision in a physical UAV context | Explicit offline-notary state machine and backfill requirement |
| Sep 28 | Add a **negative control** that changes something the chain should not flag | Pre-S20 negative-control test preregistered |
| Sep 28 | Define behavior when the unsigned-attestation buffer fills | Buffer-limit / DEGRADED_SAFE_MODE policy and tests preregistered |

### Why this contribution is visible in the repository

The feedback did not merely result in a thank-you note. It changed the planned verification contract:

```text
PASS/FAIL evidence
-> independent-verifier question
-> append-only signed chain
-> adversarial mutation/deletion/forgery
-> chain-specific causal controls
-> negative control
-> notary outage behavior
-> buffer-limit safe mode
```

For that reason, the current hardening preregistration explicitly credits the external review that led to these requirements.

## SSI author/operator responsibility

The SSI V5 author remains responsible for:

- architecture and implementation decisions;
- selecting the concrete policy used after review feedback;
- code changes;
- test execution;
- interpretation of results;
- publication and claim boundaries.

A reviewer suggestion is not treated as evidence that an implementation is correct.

## Other external feedback

The DEV discussion also contains useful feedback from other participants, including:

- Raju Dandigam — frozen partner-signed manifest and independently recomputable evidence boundary;
- Listwright — negative controls for metrics and explicit `UNTESTED` classification when a metric cannot demonstrate an opposite outcome.

Those contributions remain separately attributed and are not reassigned to Hamid.

## Related current documents

- [S19 observability incident and pre-S20 status](RESULTS/SSI_V5_S19_OBSERVABILITY_INCIDENT_AND_PRE_S20_STATUS_20260929.md)
- [Pre-S20 observability and evidence hardening preregistration](SYSTEM/SSI_V5_PRE_S20_OBSERVABILITY_AND_EVIDENCE_HARDENING_PREREGISTRATION_20260929.md)
- [DEV safeguards record](RESULTS/SSI_V5_DEV_SAFEGUARDS_20260923.md)
- [Mexico pre-benchmark R&D protocol](MEXICO_PREBENCHMARK_RND_PROTOCOL_20260928.md)
