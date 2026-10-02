# SSI V5 — Data Management and Reproducibility Framework — 2026-10-01

**Latest Final follow-up:** [4 PASS / 3 INCONCLUSIVE, followed by an infrastructure stop](../RESULTS/SSI_FINAL_RECOVERY_STOP_20261002.md). This later run supersedes the first batch as the latest core-runtime observation; the earlier result remains preserved.

**Evidence update — 2026-10-02:** The new ZeroLab pack includes sanitized terminal evidence, a case CSV, transcribed pilot receipt references and export hashes. Public CI checks consistency of those exports; original runtime receipts and the signed Final run bundle were not independently reverified for this publication.

[Current CZARA status](../CZARA_CURRENT_STATUS.md) · [ZeroLab results](../ZERO_LAB_V2_FIRST_RESULTS_20261002.md) · [Evidence and provenance](../evidence/ZERO_LAB_V2_20261002/README.md)

**Purpose:** proposal-ready baseline for research data, evidence and reproducibility.

## Data classes

SSI project data should be classified at creation:

1. **Public evidence** — sanitized results intended for repository/publication.
2. **Internal technical evidence** — detailed logs, private runtime state, prompts/configuration.
3. **Partner confidential data** — supplied under agreement.
4. **Personal data** — human-participant or identifiable information.
5. **Security-sensitive data** — credentials, network details, vulnerabilities or operational security information.
6. **Synthetic data** — generated training/evaluation material.
7. **Physical experiment data** — sensor traces, video, telemetry, incident logs.

## FAIR-oriented practice

Where lawful and compatible with IP/security constraints:

- use stable schemas;
- retain version/run identifiers;
- document provenance;
- provide machine-readable summaries;
- publish metadata even when raw data cannot be public;
- state access restrictions and reasons;
- preserve negative and superseded results;
- use persistent repository references for public artefacts.

## Reproducibility package

A strong benchmark package should include:

```text
VERSION / COMMIT
CONFIGURATION ID
TASK / DATASET VERSION
ACCEPTANCE CRITERIA
BASELINE
RANDOMNESS / SEED POLICY
MODEL / PROVIDER ID WHERE DISCLOSABLE
RUN ID
RAW OR SANITIZED EVIDENCE
AGGREGATE
HASHES
FAILURE / RETRY HISTORY
ENVIRONMENT
REPRODUCTION INSTRUCTIONS
CLAIM BOUNDARY
```

## Frozen evaluation rule

For official validation:

- evaluation cases are frozen;
- scoring rules are frozen;
- learning from the evaluated run is disabled unless the protocol explicitly measures online learning;
- any post-result learning creates a new state/version;
- re-test results are not used to erase the original result.

## Retention

The final project DMP should define:

- minimum retention period;
- storage location;
- backup strategy;
- encryption requirements;
- access roles;
- deletion rules for personal/confidential data;
- preservation rules for public scientific evidence.

## Public/private publication firewall

```text
PUBLIC
= sanitized protocols
+ aggregates
+ selected run-level evidence
+ hashes/provenance
+ limitations

RESTRICTED
= proprietary source
+ raw private prompts/memory
+ credentials/endpoints
+ partner confidential data
+ personal data
+ reconstructive security-sensitive details
```

## Integrity controls

Recommended controls:

- SHA-256 references for published artefacts;
- aggregate-to-run-level recount;
- schema validation;
- duplicate/missing-run detection;
- chain/order checks where applicable;
- negative controls for tamper detection;
- CI verification for public evidence packs.

## External replication

A replication partner should receive enough information to reproduce the agreed claim but not necessarily all proprietary implementation.

Possible replication modes:

1. black-box service/API;
2. controlled executable/container;
3. supervised on-site run;
4. source-assisted replication under agreement;
5. independent benchmark against the public protocol.

The mode should be declared in the resulting publication/report.

## Current implementation

The CZARA first-cycle public evidence already includes:

- machine-readable aggregate;
- sanitized run-level CSV;
- SHA-256 references;
- explicit internal-only claim boundary.

The repository adds CI-based aggregate verification as a next reproducibility control.

## DMP items to finalize per grant

- data controller/processor roles;
- legal basis for personal data;
- consent/ethics requirements;
- repository choice;
- open-data exceptions;
- licences for published datasets;
- retention period;
- costs of storage/curation;
- post-project stewardship.

