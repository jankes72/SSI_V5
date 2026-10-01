# CZARA First Training Cycle — Public Run-Level Evidence — 2026-10-01

**Curriculum:** `CZARA-RND-1.0.0`  
**Status:** COMPLETE  
**Scope:** sanitized internal run-level evidence for the first CZARA training cycle.

## Reviewer entry

Start with:

1. [Final human-readable result](../../CZARA_FIRST_TRAINING_CYCLE_RESULTS_20261001.md)
2. [Machine-readable aggregate summary](../CZARA_FIRST_TRAINING_CYCLE_PUBLIC_SUMMARY_20261001.json)
3. [Sanitized run-level CSV](CZARA_FIRST_TRAINING_RUNS_PUBLIC_20261001.csv)
4. [Hashes](hashes.txt)
5. [Historical S120 checkpoint](../../RESULTS/CZARA_RND_1_0_0_TRAINING_CHECKPOINT_S120_20260930.md)

## Final counts

```text
TOTAL RUN RECORDS = 537

TRAINING
  unique stages = 120
  attempts = 497
  PASS attempts = 120
  INCONCLUSIVE attempts = 377
  FAIL attempts = 0
  learning_applied = true for 497/497

VALIDATION
  frozen stages = 24
  PASS = 24/24
  REUSE = 24/24
  coverage = 1.0
  learning_applied = false

CHAMPION_BENCHMARK
  frozen stages = 16
  PASS = 16/16
  REUSE = 16/16
  coverage = 1.0
  learning_applied = false

FINAL CHECKPOINT = 160/160 PASS
FINAL QUALIFIED SKILLS = 520/520
AUTHORITY ERRORS = 0
```

The 377 INCONCLUSIVE records are preserved intermediate training/retry attempts. They are not relabelled as PASS. The final checkpoint separately records the completed status of the 120 unique training stages plus the 40 frozen stages.

## Sanitization

The public CSV intentionally omits:

- local filesystem paths;
- private runtime paths;
- raw prompts / private memory;
- credentials / endpoints;
- private implementation details.

It retains fields sufficient to independently recount the published aggregate:

```text
run_id
stage_id
phase
block
status
route_mode
skill_coverage
qualified_skills_used
missing_skills
translations_ok
professor_prompts_delivered
director_replies
authority_errors
elapsed_s
frozen
learning_applied
evidence_id
```

## Claim boundary

This evidence supports the recorded internal CZARA curriculum only. It does not establish an independent Mexico benchmark, external replication, physical robotics validation, safety certification or production readiness.
