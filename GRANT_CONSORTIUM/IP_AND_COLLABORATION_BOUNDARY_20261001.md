# SSI V5 — IP and Collaboration Boundary — 2026-10-01

**Latest Final follow-up:** [4 PASS / 3 INCONCLUSIVE, followed by an infrastructure stop](../RESULTS/SSI_FINAL_RECOVERY_STOP_20261002.md). This later run supersedes the first batch as the latest core-runtime observation; the earlier result remains preserved.

**Evidence update — 2026-10-02:** The ZeroLab public release contains architecture, sanitized terminal evidence and an export-consistency checker. It does not publish the private runtime implementation or change the background-IP/access boundary described below.

[Current CZARA status](../CZARA_CURRENT_STATUS.md) · [ZeroLab results](../ZERO_LAB_V2_FIRST_RESULTS_20261002.md) · [Evidence and provenance](../evidence/ZERO_LAB_V2_20261002/README.md)

**Purpose:** make the public/private and background/foreground boundary understandable before consortium negotiations.  
**Status:** planning statement, not a substitute for a consortium agreement, NDA, licence or legal advice.

## Core principle

```text
PUBLIC EVIDENCE != PUBLIC OWNERSHIP OF SSI IMPLEMENTATION
OBSERVE != CONTROL
COLLABORATION != TRANSFER OF BACKGROUND IP
```

The repository is public so that partners can inspect research claims, evidence and methodology. Proprietary implementation is intentionally not fully disclosed.

No open-source licence is granted by this repository unless a specific file or component explicitly states one. Public availability should not be interpreted as permission to reconstruct, commercialize, sublicense or redistribute proprietary SSI implementation.

## Proposed background IP

Subject to final legal confirmation, SSI background should include pre-project assets such as:

- SSI architecture and private source code;
- DIRECTOR, BODY_FROZEN and ISKRA runtime design;
- Router V10 / S10 implementation details;
- micronetwork / BLOCKS internals;
- private scoring, thresholds and feature construction;
- private prompts, memory, configuration and development procedures;
- existing LAB/evidence tooling;
- CZARA implementation existing before the funded project;
- existing domain/world adapters and private integration code;
- prior datasets or evidence packs where rights permit.

Background remains with its original owner unless explicitly licensed or transferred by signed agreement.

## Proposed foreground classification

New project results should be classified when created, not left ambiguous.

Possible categories:

1. **SSI-specific foreground** — improvements inseparable from proprietary SSI internals.
2. **Joint foreground** — genuinely co-created results where contributions cannot reasonably be separated.
3. **Partner-specific foreground** — target-system adapters, datasets or methods created solely by another partner.
4. **Open research outputs** — agreed reports, benchmark specifications, schemas, sanitized evidence or publications.
5. **Restricted outputs** — security-sensitive, confidential, personal-data or commercially sensitive materials.

Ownership and access rights must be fixed in the consortium agreement for the selected project.

## Access-right model

A practical collaboration can use four levels:

### Level A — public reviewer

May access sanitized public documentation and evidence.

### Level B — controlled research partner

May access agreed experiment interfaces, shared datasets, benchmark material and sanitized logs.

### Level C — integration partner

May receive narrowly scoped APIs/adapters or controlled binaries required for integration under contract.

### Level D — private implementation access

Only if separately negotiated and necessary. It is not the default condition for collaboration.

## External benchmark protection

An external benchmark should preserve independence:

- partner-held unseen cases may remain hidden from SSI until the official run;
- acceptance criteria are frozen before scoring;
- test data are not silently incorporated into training before the frozen score;
- any post-benchmark learning is recorded separately;
- re-validation uses a declared version and state.

## Publication and attribution

Before publication, partners should agree:

- which results are publishable;
- embargo periods if needed;
- attribution and authorship criteria;
- disclosure of negative results;
- protection of confidential implementation details;
- whether code, data, evidence or only aggregate metrics are released.

External feedback may be credited as feedback provenance without implying endorsement, validation or co-ownership.

## Commercial pathway

Possible later commercial arrangements include:

- paid R&D / benchmark services;
- integration licence;
- field-specific licence;
- hosted/service access;
- project-specific adaptation;
- joint exploitation of agreed foreground.

None is automatically granted by participation in a research benchmark.

## Items to freeze before proposal signature

- legal owner/applicant of SSI background;
- exact background list;
- required access rights during the project;
- access rights after the project;
- joint ownership procedure;
- publication review period;
- confidential-information handling;
- security-sensitive output handling;
- licensing principles for exploitation;
- treatment of improvements to SSI background.

## Claim boundary

This file documents the intended negotiation position. The final grant agreement, consortium agreement and signed partner contracts control the legal relationship.

