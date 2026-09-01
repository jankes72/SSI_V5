# Contributing to SSI V5

SSI V5 is a public research mirror. The most useful contributions are not generic endorsements, but reproducible observations that strengthen or falsify specific claims.

## What is especially valuable

Please open a GitHub Issue for:

- independent reproductions of published tests;
- methodology problems or hidden assumptions;
- false-reuse cases;
- blind-retry / failure-loop cases;
- anti-loop and recovery tests;
- adversarial or distribution-shift cases;
- persistence / replay / restart failures;
- Candidate -> Challenger -> Champion lifecycle inconsistencies;
- micronetwork duplication, stale competence or regression;
- comparisons with related state of the art;
- cases where a public claim is broader than the available evidence.

## Minimum useful report

Whenever possible include:

```text
COMMIT / VERSION
TEST_ID
ENVIRONMENT
PRE_STATE
INPUT / TASK
ROUTE_SELECTED
ACTION
OBSERVED_OUTCOME
EXPECTED_OUTCOME
FAILURE_SIGNATURE (if applicable)
NEW_EVIDENCE
REPRODUCTION_STEPS
LOG / MACHINE EVIDENCE
```

For learning-path or replay experiments, also include the relevant event IDs, snapshot IDs and state hashes when available.

## Evidence policy

SSI V5 follows this research chain:

```text
CLAIM
-> IMPLEMENTATION
-> TEST
-> MACHINE EVIDENCE
-> FAILURE / ROOT CAUSE
-> REPAIR
-> RETEST
-> CURRENT CLAIM BOUNDARY
```

A failed test is not considered embarrassing data to remove. If it is relevant to the research history, it should remain visible together with the diagnosis, repair and later retest.

## Security and private implementation

Do not post credentials, API keys, private runtime secrets, personal data or proprietary implementation details in public Issues.

The public repository is intended to expose research claims, architecture, chronology and evidence. It does not imply that every internal implementation detail must be public.

## Where to start

- [START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md)
- [GRANT_REVIEWER_FAQ.md](GRANT_REVIEWER_FAQ.md)
- [CURRENT_TRUTH_INDEX.md](CURRENT_TRUTH_INDEX.md)
- [V10_PREDICTIVE_ROUTING.md](V10_PREDICTIVE_ROUTING.md)
- [evidence/README.md](evidence/README.md)

Thank you for testing the project critically and reproducibly.
