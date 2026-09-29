# SSI V5 — Pre-S20 observability and evidence hardening preregistration — 29 September 2026

**Status:** `PREREGISTERED CHANGE SET / NOT YET CLAIMED AS PASSED`  
**Purpose:** freeze the intended controls before the next core-training continuation.  
**Planned sequence:** S19 consolidation -> S20-S40 -> WEB01-WEB24.

> This document records what will be changed and what must pass before continuation. It is not evidence that these controls have already passed.

## 1. Goals

The next SSI continuation must answer five engineering questions without introducing new measurement-induced behavior:

1. Is a validated Micronetwork/Champion actually selected and executed, or merely present in the catalog?
2. When does a case actually enter Full Flow?
3. Which provider/model/fallback path produced the final answer?
4. Do BODY_FROZEN and ISKRA1..ISKRA6 fail the same cases for the same reasons?
5. Is a failure attributable to capability, laboratory design, model/routing choice, infrastructure, or instrumentation?

## 2. Observability non-interference gate

New routing telemetry must be passive.

Required A/B gate:

```text
A = execution with routing observer disabled
B = matched execution with routing observer enabled

required:
mission lifecycle A == B
routing decision A == B
case verdict A == B
snapshot contract A == B
consolidation state transition A == B

allowed difference:
B contains additional observer evidence
```

If the observer changes any execution or consolidation decision, continuation is blocked.

## 3. Per-case routing evidence V2

Each new case should retain, where available:

```text
stage_id
case_id
actor
verdict
failed_acceptance_rule
failure_class
failure_reason

micronetwork_lookup
micronetwork_id
champion_available
champion_id
champion_selected
champion_executed
champion_result

exact_reuse
full_flow_entered
escalation_reason

provider
model
fallback_level
attempt_count

collective_used
consultation_count
consolidation_count
```

Unknown facts must remain unknown rather than inferred from PASS/FAIL or from repeated text markers.

## 4. Canonical routing states

Future evidence should distinguish:

```text
CHAMPION_NOT_AVAILABLE
CHAMPION_AVAILABLE_NOT_SELECTED
CHAMPION_SELECTED
CHAMPION_EXECUTED
CHAMPION_SUCCEEDED
CHAMPION_FAILED

EXACT_REUSE_HIT
EXACT_REUSE_MISS
MICRONETWORK_COMPLETION
FULL_FLOW_ENTERED
PROVIDER_FALLBACK
FINAL_ROUTE_RECORDED
```

A catalog state `CHAMPION` is not equivalent to an execution claim.

## 5. Cross-actor failure analysis

For each matched case, retain a seven-actor matrix:

```text
BODY_FROZEN | ISKRA1 | ISKRA2 | ISKRA3 | ISKRA4 | ISKRA5 | ISKRA6
```

Post-run analysis should classify patterns such as:

- `SHARED_FAILURE` — most/all actors fail the same case/rule;
- `ACTOR_SPECIFIC_FAILURE` — one actor diverges;
- `MODEL_CORRELATED_FAILURE` — failures correlate with provider/model;
- `ROUTE_CORRELATED_FAILURE` — failures correlate with a routing path or Champion;
- `STOCHASTIC_MODEL_OR_ROUTE_FAILURE`;
- `LAB_DESIGN_SUSPECT`;
- `CAPABILITY_GAP`;
- `INFRASTRUCTURE_FAILURE`;
- `INSTRUMENTATION_REGRESSION`.

These labels are diagnostic classes, not automatic causal proof. Causal claims require matched controls.

## 6. Evidence-chain adversarial suite informed by external review

The pre-S20 verifier suite will include:

1. committed-record mutation;
2. deletion of an earlier record;
3. fabricated PASS with an unregistered protocol;
4. previous-hash-only mutation;
5. missing-sequence test;
6. negative control changing a field explicitly outside the signed/hash-dependent payload.

Expected behavior:

```text
hash-dependent mutation -> REJECT for the chain-specific reason
missing sequence -> REJECT for sequence discontinuity
unregistered protocol PASS -> REJECT
negative-control cosmetic mutation -> chain remains valid
```

The negative-control field must be explicitly defined as outside the signed payload. A field cannot be relabeled “cosmetic” after a result is known.

## 7. Signed append-only / authority boundary

Target evidence contract:

```text
append-only local chain
+ monotonic sequence
+ previous-record hash
+ digital signature
+ executor/verifier permission separation
+ signing/notary authority separated from the executor where externally claimed
```

Local consistency alone must not be described as independent external attestation.

## 8. Notary/signing outage and buffer-limit policy

The outage path must be frozen before an external benchmark.

Target state machine:

```text
NOTARY_AVAILABLE
-> externally attested record

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
- silent promotion to `EXTERNALLY_VERIFIED PASS` is prohibited;
- dropping the oldest evidence is prohibited;
- overwriting pending evidence is prohibited;
- ordinary new mission authority is blocked unless explicitly preregistered otherwise.

Parameters to freeze:

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

Required tests include:

- notary offline at start;
- notary lost mid-mission;
- reconnect with partially filled buffer;
- buffer limit reached;
- reboot with pending buffer;
- backfill after reconnect;
- duplicate backfill;
- out-of-order backfill;
- tampered buffered record.

## 9. Consolidation gate

A stage may advance only when:

```text
execution_complete = true
-> verified subset prepared
-> no genuinely active blocking mission
-> SNAPSHOT response valid for 7/7 actors
-> each response actor == expected actor
-> each response transaction == expected transaction
-> Director/body consolidation checks complete
-> journal.status = COMMITTED
```

Historical `MIGRATED_HOLD` state may remain visible but must not be silently converted into an active mission or deleted to make a gate pass.

FAIL and INCONCLUSIVE case outcomes remain preserved; they are not infrastructure errors by themselves.

## 10. Continuous continuation target

After all pre-S20 gates pass:

```text
S19 consolidation COMMITTED
-> S20
-> S21
-> ...
-> S40
-> S40 consolidation COMMITTED
-> WEB01
-> ...
-> WEB24
```

The run should continue through task-level FAIL/INCONCLUSIVE outcomes where the declared training policy permits, while integrity, runtime, transaction, or unsafe-state failures remain hard stops.

## 11. Final diagnostic report

After S40/WEB24, the report should measure:

- hardest stages and cases;
- actor-by-actor failure overlap;
- acceptance rules most often failed;
- model/provider correlations;
- exact reuse count;
- Micronetwork completion count;
- Champion available/selected/executed/succeeded/failed counts;
- Full Flow count;
- provider fallback count;
- whether reuse reduced Full Flow without reducing verified quality;
- whether the same weaknesses recur in WEB training;
- whether instrumentation changed behavior in A/B non-interference tests.

## 12. Claim boundary

Until executed evidence exists, this document does **not** claim:

- that the new observer is non-interfering;
- that Champion execution occurs;
- a measured exact-reuse percentage;
- a measured Full Flow percentage;
- that S19 consolidation has committed;
- that S20-S40 has completed;
- that WEB01-WEB24 has completed;
- independent external attestation;
- physical-system validation.
