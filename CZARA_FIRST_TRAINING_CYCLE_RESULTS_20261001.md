# CZARA — First Training Cycle: Final Results and Evidence

**Evidence update — 2026-10-02:** The first-cycle results below remain frozen. The later ZeroLab V2 extension now has a local executor pilot, including BODY_FROZEN_1_0. That pilot grants no additional trained skills and is separate from this curriculum.

[Current CZARA status](CZARA_CURRENT_STATUS.md) · [ZeroLab results](ZERO_LAB_V2_FIRST_RESULTS_20261002.md) · [Evidence and provenance](evidence/ZERO_LAB_V2_20261002/README.md)

**Date:** 2026-10-01  
**Curriculum:** `CZARA-RND-1.0.0`  
**Status:** **COMPLETED**  
**Scope:** internal SSI V5 training, frozen validation, and frozen Champion benchmark  
**Claim boundary:** this is an internal SSI V5 training result. It is not an independent Mexico benchmark, physical robotics validation, certification, or external replication.

## Why CZARA was trained

CZARA is the multilingual human–AI collaboration layer planned for the Poland–Mexico research workflow. Its job is not to replace the DIRECTOR or command BODY_FROZEN directly.

The intended path is:

```text
Professor / Experts / Students
        |
        v
CZARA
  - preserve the original Spanish input
  - provide Polish translation for ROOT
  - identify role / authority / intent
  - preserve chronology and decision lineage
  - separate observation, suggestion and formal experiment change
        |
        v
DIRECTOR
        |
        v
BODY_FROZEN / LAB / evidence
```

The first curriculum was designed to train the collaboration layer before an external benchmark.

## Curriculum structure

The completed curriculum contains **160 unique stages**:

- **120 TRAINING stages**
- **24 frozen VALIDATION stages**
- **16 frozen CHAMPION_BENCHMARK stages**

The training catalog contained **520 skill candidates**.

The final checkpoint contains:

```text
completed stages: 160
PASS:             160
```

The final skills registry contains:

```text
skills:     520
QUALIFIED:  520
```

## What happened during training

Training was intentionally iterative rather than a single-pass benchmark.

There were **497 TRAINING runs** for **120 unique training stages**. This means the system performed **377 additional retry / learning runs** before the curriculum reached its final completed state.

Aggregate TRAINING attempts:

| Metric | Result |
|---|---:|
| Training run attempts | 497 |
| Unique training stages | 120 |
| Final completed training stages | 120 / 120 PASS |
| PASS attempts | 120 |
| INCONCLUSIVE attempts | 377 |
| FAIL attempts | 0 |
| FULL_FLOW | 473 |
| ADAPT | 20 |
| REUSE | 4 |
| Translation-failed attempts | 260 |
| Authority errors | 0 |
| Learning applied | 497 / 497 |

The **377 INCONCLUSIVE results are intermediate training attempts**, not the final curriculum result. The checkpoint records all 120 unique TRAINING stages as PASS after the retry / learning process.

This distinction is important: the training process exposed missing competence, translation failures and insufficient skill coverage, then retried stages after learning. It was not rewritten as a clean first-pass success.

## Frozen validation

The next phase disabled learning from the evaluated run.

**VALIDATION result:**

| Metric | Result |
|---|---:|
| Frozen validation stages | 24 |
| PASS | **24 / 24** |
| INCONCLUSIVE | 0 |
| FAIL | 0 |
| REUSE | **24 / 24** |
| FULL_FLOW | 0 |
| Average skill coverage | **1.0** |
| Missing skills | 0 in completed frozen runs |
| Translation failures | 0 |
| Authority errors | 0 |
| `learning_applied` | **false for all 24** |

This phase is the main evidence that the result was not produced by learning from the held-out evaluation itself.

## Champion benchmark

The final phase tested the reuse path after qualification.

**CHAMPION_BENCHMARK result:**

| Metric | Result |
|---|---:|
| Frozen Champion stages | 16 |
| PASS | **16 / 16** |
| INCONCLUSIVE | 0 |
| FAIL | 0 |
| REUSE | **16 / 16** |
| FULL_FLOW | 0 |
| Average skill coverage | **1.0** |
| Translation failures | 0 |
| Authority errors | 0 |
| `learning_applied` | **false for all 16** |

The last live state was `CZARA_C016`, status `PASS`, route mode `REUSE`, skill coverage `1.0`.

## End-to-end totals

Across training attempts, validation, and Champion benchmark:

| Metric | Result |
|---|---:|
| Total run records | 537 |
| PASS records | 160 |
| INCONCLUSIVE records | 377 |
| FAIL records | **0** |
| REUSE records | 44 |
| FULL_FLOW records | 473 |
| ADAPT records | 20 |
| Frozen runs | 40 |
| Frozen PASS | **40 / 40** |
| Frozen REUSE | **40 / 40** |
| Authority errors | **0** |
| Professor prompts delivered | 939 |
| DIRECTOR replies | 939 |
| Final qualified skills | **520 / 520** |

The sum of the recorded per-run elapsed times is approximately **27.29 hours**. This is a sum of run durations, not a claim about exact wall-clock training time.

## Training-to-reuse transition

The intended transition was:

```text
missing competence
    -> FULL_FLOW
    -> INCONCLUSIVE / evidence of missing coverage
    -> learning + retry
    -> qualification
    -> frozen validation
    -> REUSE
    -> Champion benchmark
```

The final evidence shows that transition:

```text
TRAINING
  120 unique stages
  497 attempts
  377 intermediate INCONCLUSIVE
  learning_applied = true

FINAL CHECKPOINT
  160 / 160 PASS

SKILL REGISTRY
  520 / 520 QUALIFIED

VALIDATION
  24 / 24 PASS
  24 / 24 REUSE
  coverage = 1.0
  learning_applied = false

CHAMPION_BENCHMARK
  16 / 16 PASS
  16 / 16 REUSE
  coverage = 1.0
  learning_applied = false
```

## What was demonstrated

This first internal cycle demonstrated the specific target that was planned for CZARA:

1. the training curriculum can expose missing competence through INCONCLUSIVE outcomes rather than silently promote them to PASS;
2. the same stages can be retried after learning until the curriculum checkpoint is complete;
3. the collaboration layer can preserve role-authority constraints without recorded authority errors in this run set;
4. the system can transition from predominantly FULL_FLOW during learning to REUSE in frozen held-out evaluation;
5. the held-out validation and Champion benchmark completed without learning from the evaluated runs;
6. all 520 catalogued skills reached QUALIFIED status in the final registry.

These statements describe the recorded internal run only. They do not establish external generalization beyond this curriculum.

## Evidence integrity references

Reviewer-accessible sanitized evidence:

- [Run-level evidence index](evidence/CZARA_FIRST_TRAINING_20261001/README.md)
- [537 sanitized run records](evidence/CZARA_FIRST_TRAINING_20261001/CZARA_FIRST_TRAINING_RUNS_PUBLIC_20261001.csv)
  - SHA-256: `3de525337e24bd6b66d652b05ad4c3142e60a0871f4a24d2509f16c2c0948cac`
- [Mirrored aggregate summary](evidence/CZARA_FIRST_TRAINING_20261001/summary.json)
- [Hash reference file](evidence/CZARA_FIRST_TRAINING_20261001/hashes.txt)

Source collection prepared after completion:

- `CZARA_FIRST_TRAINING_FINAL_20261001_081511.zip`
  - SHA-256: `654f17dd524728ed66172f458bc83a3d228e0197b2be8b48f1932c5871772602`
- `CZARA_FINAL_SUMMARY.json`
  - SHA-256: `6e315fa80a601fbc5591eaac3b4bf1cf8762d55b03d06a64388bbda2deeeb498`
- `checkpoint.json`
  - SHA-256: `87853c59c8412e04b4c499a53a64396ea1c13def631cb1e609e6747f5783915f`
- `skills.json`
  - SHA-256: `a224a01d1cfe99687afad998ce37af2ae1e0c2e9c40156ac46db10756e31db1f`

The scheduler ended in:

```json
{"scheduler":{"status":"IDLE","reason":"COMPLETE"}}
```

## Next step

The next CZARA development step is **ZERO-LAB / LAB_ARCHITECT**: given a new experiment and assuming no laboratory already exists, CZARA will help derive a laboratory blueprint before BODY_FROZEN builds or modifies the execution environment.

That next module is deliberately separated from this result so the first training cycle remains a frozen evidence point.

