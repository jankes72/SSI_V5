# SSI V5 — Start Here for Grant and Technical Reviewers

**Updated:** 2026-09-06  
**Frozen common baseline:** `T0 / BODY_FROZEN / PRE-ISKRA / 2026-09-05`  
**Current experimental state:** `6 independent BODY ISKRA T0 variants / START_STATE_VALIDATED`  
**Latest closed validation test:** `TEST 5 / DEVELOPMENT_VALIDATED`

The key distinction is now:

```text
TEST 5
= latest closed validation of a scoped local SSI BODY control/integration path

BODY_FROZEN T0 / 2026-09-05
= immutable common experimental origin

BODY ISKRA 6X / 2026-09-06
= six independent descendants from the same T0
+ explicit different initial value/emotion states
+ sanitized start-state evidence
+ 48/48 group start-state QA PASS
```

## 1. Current public experimental state — BODY ISKRA 6X

Primary entry:

[`BODY_ISKRA_6X_T0.md`](BODY_ISKRA_6X_T0.md)

Sanitized evidence:

[`evidence/BODY_ISKRA_6X_T0_20260906/`](evidence/BODY_ISKRA_6X_T0_20260906/)

Recorded current state:

```text
AGENTS = 6
PRIVATE ARTIFACT PER AGENT = 1832 files
PYTHON FILES PER AGENT = 616
DELTA VS BODY_FROZEN PER AGENT = +51 total files / +29 Python files
START-STATE QA PER AGENT = 8/8 PASS
GROUP START-STATE QA = 48/48 PASS
VERIFIED NEW EXPERIENCES AT T0 = 0 per agent
PENDING NEW EXPERIENCES AT T0 = 0 per agent
```

Six independent start variants now exist:

1. NICE
2. GUARDIAN
3. JUSTICE
4. EXPLORER
5. PRAGMATIST
6. SKEPTIC

Each public record includes the complete sanitized initial beliefs, initial emotions, cognitive start state, inventory counts, QA status and private-artifact SHA256 reference.

## 2. Frozen origin — BODY_FROZEN T0

The common origin remains unchanged:

[`BODY_FROZEN_T0_PRE_ISKRA.md`](BODY_FROZEN_T0_PRE_ISKRA.md)

```text
DATE = 2026-09-05
BODY_FROZEN = 1781 files / 587 Python files retained privately
CONTINUUM = CLOSED
23/23 CONTINUUM tests PASS
22/22 main scenarios PASS
19/19 E2E closure PASS
26/26 final guard PASS
ACTIVE_FAILURES = 0
INVARIANT_VIOLATIONS = 0
OPEN_BLOCKERS = 0
```

BODY_FROZEN is preserved as the immutable comparison control. The six BODY ISKRA artifacts are descendants, not rewrites of T0.

## 3. What is already established vs still prospective

**Established / sanitized evidence available:**

- six independent private BODY ISKRA artifacts exist;
- they share the same frozen BODY_FROZEN origin;
- each has a separately recorded initial state;
- each has `1832 / 616` inventory counts;
- each passed `8/8` start-state QA;
- group start-state QA is `48/48 PASS`;
- each starts the new experiment with zero verified new longitudinal experiences.

**Not yet claimed:**

- long-run behavioral divergence;
- superiority of one Iskra over another;
- emergence of stable social coalitions or conflicts;
- improved competence due specifically to Iskra;
- AGI, consciousness or production readiness.

Those require prospective longitudinal evidence.

## 4. Latest closed validation — TEST 5

```text
STAGE_12 = SUPERSEDED
STAGE_13_AUDIT_RETEST = PASS
TEST5_ACCEPTANCE = 29/29 PASS
ROOT_CONTROL = 111/111 PASS
ROOT_RUNTIME_BRIDGE = 338/338 PASS
ROBERT_STABLE = 46/46 PASS
TOTAL = 524/524 PASS
OPEN_BLOCKERS = 0
```

TEST 5 remains the latest closed validation milestone. BODY ISKRA 6X is a new recorded experimental start state, not a replacement label for TEST 5 and not automatically TEST 6.

## 5. Public/private boundary

```text
PUBLIC
= sanitized evidence
+ agent labels
+ initial beliefs/emotions
+ inventory counts
+ QA results
+ SHA256 references
+ claim boundaries

PRIVATE
= SSI source code
+ private file tree
+ implementation-level architecture
+ runtime/configuration
+ raw memory/user data
+ proprietary integration internals
```

The public mirror remains evidence-only.

## 6. Recommended reading order

1. [`BODY_ISKRA_6X_T0.md`](BODY_ISKRA_6X_T0.md)
2. [`evidence/BODY_ISKRA_6X_T0_20260906/README.md`](evidence/BODY_ISKRA_6X_T0_20260906/README.md)
3. [`BODY_FROZEN_T0_PRE_ISKRA.md`](BODY_FROZEN_T0_PRE_ISKRA.md)
4. [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md)
5. [`evidence/TEST5_FINAL_CONVERGENCE_20260903.md`](evidence/TEST5_FINAL_CONVERGENCE_20260903.md)
6. [`V10_PREDICTIVE_ROUTING.md`](V10_PREDICTIVE_ROUTING.md)
7. [`GRANT_REVIEWER_FAQ.md`](GRANT_REVIEWER_FAQ.md)
8. [`evidence/README.md`](evidence/README.md)

SSI V5 should be evaluated as an evidence chain: BODY_FROZEN T0 -> six recorded BODY ISKRA start states -> future controlled longitudinal comparisons.