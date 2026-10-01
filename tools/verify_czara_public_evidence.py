#!/usr/bin/env python3
import csv
import json
import math
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "evidence" / "CZARA_FIRST_TRAINING_20261001"
CSV_PATH = PACK / "CZARA_FIRST_TRAINING_RUNS_PUBLIC_20261001.csv"
SUMMARY_PATH = ROOT / "evidence" / "CZARA_FIRST_TRAINING_CYCLE_PUBLIC_SUMMARY_20261001.json"

def as_bool(value):
    v = str(value).strip().lower()
    if v in {"true", "1", "yes"}:
        return True
    if v in {"false", "0", "no", ""}:
        return False
    raise ValueError(f"invalid boolean: {value!r}")

def fail(msg):
    print(f"[FAIL] {msg}")
    sys.exit(1)

def check(label, actual, expected, tol=None):
    if tol is None:
        ok = actual == expected
    else:
        ok = math.isclose(float(actual), float(expected), rel_tol=0, abs_tol=tol)
    if not ok:
        fail(f"{label}: actual={actual!r} expected={expected!r}")
    print(f"[PASS] {label}: {actual}")

with SUMMARY_PATH.open(encoding="utf-8") as f:
    summary = json.load(f)

with CSV_PATH.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

required = {
    "run_id","stage_id","phase","status","route_mode","skill_coverage",
    "translations_ok","professor_prompts_delivered","director_replies",
    "authority_errors","elapsed_s","frozen","learning_applied"
}
if not rows:
    fail("CSV has no rows")
missing = required - set(rows[0])
if missing:
    fail(f"CSV missing required columns: {sorted(missing)}")

run_ids = [r["run_id"] for r in rows]
if len(run_ids) != len(set(run_ids)):
    fail("duplicate run_id detected")
print(f"[PASS] unique run_id count: {len(run_ids)}")

status = Counter(r["status"] for r in rows)
route = Counter(r["route_mode"] for r in rows)
phase = Counter(r["phase"] for r in rows)

check("run_records.total", len(rows), summary["run_records"]["total"])
check("run_records.pass", status["PASS"], summary["run_records"]["pass"])
check("run_records.inconclusive", status["INCONCLUSIVE"], summary["run_records"]["inconclusive"])
check("run_records.fail", status["FAIL"], summary["run_records"]["fail"])
check("run_records.route_mode.full_flow", route["FULL_FLOW"], summary["run_records"]["route_mode"]["full_flow"])
check("run_records.route_mode.adapt", route["ADAPT"], summary["run_records"]["route_mode"]["adapt"])
check("run_records.route_mode.reuse", route["REUSE"], summary["run_records"]["route_mode"]["reuse"])

authority_errors = sum(int(r["authority_errors"]) for r in rows)
professor_prompts = sum(int(r["professor_prompts_delivered"]) for r in rows)
director_replies = sum(int(r["director_replies"]) for r in rows)
elapsed = sum(float(r["elapsed_s"]) for r in rows)

check("run_records.authority_errors", authority_errors, summary["run_records"]["authority_errors"])
check("run_records.professor_prompts_delivered", professor_prompts, summary["run_records"]["professor_prompts_delivered"])
check("run_records.director_replies", director_replies, summary["run_records"]["director_replies"])
check("run_records.summed_elapsed_seconds", elapsed, summary["run_records"]["summed_elapsed_seconds"], tol=0.02)

training = [r for r in rows if r["phase"] == "TRAINING"]
validation = [r for r in rows if r["phase"] == "VALIDATION"]
champion = [r for r in rows if r["phase"] == "CHAMPION_BENCHMARK"]

check("training.run_attempts", len(training), summary["training"]["run_attempts"])
check("training.unique_stages", len({r["stage_id"] for r in training}), summary["training"]["unique_stages"])
check("training.pass", sum(r["status"]=="PASS" for r in training), summary["training"]["attempt_status"]["pass"])
check("training.inconclusive", sum(r["status"]=="INCONCLUSIVE" for r in training), summary["training"]["attempt_status"]["inconclusive"])
check("training.fail", sum(r["status"]=="FAIL" for r in training), summary["training"]["attempt_status"]["fail"])
check("training.learning_applied_true", sum(as_bool(r["learning_applied"]) for r in training), summary["training"]["learning_applied_true"])
check("training.full_flow", sum(r["route_mode"]=="FULL_FLOW" for r in training), summary["training"]["route_mode"]["full_flow"])
check("training.adapt", sum(r["route_mode"]=="ADAPT" for r in training), summary["training"]["route_mode"]["adapt"])
check("training.reuse", sum(r["route_mode"]=="REUSE" for r in training), summary["training"]["route_mode"]["reuse"])

for name, rows_phase, expected in [
    ("validation", validation, summary["validation"]),
    ("champion_benchmark", champion, summary["champion_benchmark"]),
]:
    check(f"{name}.runs", len(rows_phase), expected["runs"])
    check(f"{name}.pass", sum(r["status"]=="PASS" for r in rows_phase), expected["pass"])
    check(f"{name}.inconclusive", sum(r["status"]=="INCONCLUSIVE" for r in rows_phase), expected["inconclusive"])
    check(f"{name}.fail", sum(r["status"]=="FAIL" for r in rows_phase), expected["fail"])
    check(f"{name}.reuse", sum(r["route_mode"]=="REUSE" for r in rows_phase), expected["reuse"])
    check(f"{name}.full_flow", sum(r["route_mode"]=="FULL_FLOW" for r in rows_phase), expected["full_flow"])
    check(f"{name}.frozen", sum(as_bool(r["frozen"]) for r in rows_phase), expected["frozen"])
    check(f"{name}.learning_applied_false", sum(not as_bool(r["learning_applied"]) for r in rows_phase), expected["learning_applied_false"])
    avg_cov = sum(float(r["skill_coverage"]) for r in rows_phase) / len(rows_phase)
    check(f"{name}.avg_skill_coverage", avg_cov, expected["avg_skill_coverage"], tol=1e-9)

check("unique_stages.training", len({r["stage_id"] for r in training}), summary["unique_stages"]["training"])
check("unique_stages.validation", len({r["stage_id"] for r in validation}), summary["unique_stages"]["validation"])
check("unique_stages.champion_benchmark", len({r["stage_id"] for r in champion}), summary["unique_stages"]["champion_benchmark"])
check("unique_stages.total", len({r["stage_id"] for r in rows}), summary["unique_stages"]["total"])

if summary["final_checkpoint"]["completed"] != summary["unique_stages"]["total"]:
    fail("summary final_checkpoint.completed does not match unique_stages.total")
if summary["final_checkpoint"]["pass"] != summary["unique_stages"]["total"]:
    fail("summary final_checkpoint.pass does not match unique_stages.total")

print("\nCZARA public evidence aggregate verification: PASS")
