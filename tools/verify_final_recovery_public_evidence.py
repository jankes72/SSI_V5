#!/usr/bin/env python3
"""Offline consistency checks for the operator-reported stopped continuation."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "evidence/SSI_FINAL_RECOVERY_20261002T181736Z"


def check(condition, label):
    if not condition:
        raise ValueError(label)


def verify():
    def read(name):
        return json.loads((PACK / name).read_text(encoding="utf-8"))

    manifest = read("publication_manifest.json")
    check(set(manifest["files"]) == {"operator.log", "cases.csv", "case_events.json", "summary.json"},
          "Unexpected export file set")
    for name, expected in manifest["files"].items():
        check(hashlib.sha256((PACK / name).read_bytes()).hexdigest() == expected, "Hash mismatch: " + name)
    summary = read("summary.json")
    history = read("case_events.json")
    log = (PACK / "operator.log").read_text(encoding="utf-8")
    with (PACK / "cases.csv").open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    extracted = []
    current = None
    for line in log.splitlines():
        match = re.match(r"\[CASE_REQUEST\] (\S+)", line)
        if match:
            current = {"request_id": match[1], "candidate_events": [], "training_events": []}
        match = re.match(r"\[NATIVE_CANDIDATE\] (\d+) evaluation=(\S+) ci=(\S+)", line)
        if match:
            current["candidate_events"].append(dict(candidate=int(match[1]), evaluation=match[2], ci=match[3]))
        match = re.match(r"\[TRAINING_EVENT\] (\S+) action=(\S+) decision=(\S+) reasons=(.*)", line)
        if match:
            current["training_events"].append(dict(event=match[1], action=match[2], decision=match[3], reasons=json.loads(match[4])))
        match = re.match(r"\[CASE_DONE\] (\S+) (\S+) (\S+) (.*)", line)
        if match:
            current.update(actor=match[1], case_id=match[2], status=match[3], reported_flags=match[4])
            extracted.append(current)
    check(extracted == history, "Event history differs from terminal transcript")
    check(len(rows) == len(history) == summary["closed_cases"] == 7, "Case count mismatch")
    for row, event in zip(rows, history):
        for key in ["actor", "case_id", "status", "request_id", "reported_flags"]:
            check(row[key] == event[key], "CSV mismatch: " + key)
        check(row["run_id"] == summary["run_id"], "CSV run identity mismatch")
        check(int(row["candidates_observed"]) == len(event["candidate_events"]), "Candidate count mismatch")
        check(row["final_event"] == event["training_events"][-1]["event"], "Event label mismatch")
        check(row["final_decision"] == event["training_events"][-1]["decision"], "Decision mismatch")
        check(json.loads(row["final_event_reasons"]) == event["training_events"][-1]["reasons"], "Reasons lost")
    check(summary["counts"] == {"PASS": 4, "INCONCLUSIVE": 3, "FAIL": 0}, "Unexpected summary counts")
    check(Counter(r["status"] for r in rows) == Counter(summary["counts"]), "CSV counts differ")
    check(summary["status"] == "STOPPED_INFRASTRUCTURE" and
          "[DOMAIN_BATCH_RESULT] STOPPED_INFRASTRUCTURE {'INCONCLUSIVE': 3, 'PASS': 4}" in log,
          "Infrastructure stop missing or relabeled")
    check(summary["run_id"] in log and summary["plan_id"] in log, "Run/plan identity mismatch")
    check(summary["command_limit"] == 622 and "--limit 622" in log, "Limit mismatch")
    check(summary["queue_before_observed"] == 614 and "[KOLEJKA] pozostalo=614;" in log and
          summary["queue_after_derived"] == 614 - len(rows), "Queue observation/arithmetic mismatch")
    last = history[-1]
    check(last["actor"] == "ISKRA6" and last["case_id"] == "S20-01-01" and last["status"] == "INCONCLUSIVE", "Final case mismatch")
    check(last["training_events"][0]["reasons"] == ["LAB_OUTPUT_MISMATCH"], "First-candidate failure lost")
    check(last["training_events"][-1]["reasons"] == ["NO_CANDIDATE_GENERATED", "INVALID_WORKER_JSON"], "Final stop reasons lost")
    check("[LAB_FLOW] ISKRA6 S20-01-01 STOP_RUN pending=3" in log, "STOP_RUN not preserved")

    previous_pack = ROOT / "evidence/ZERO_LAB_V2_20261002"
    with (previous_pack / "final_case_results.csv").open(encoding="utf-8", newline="") as stream:
        previous = list(csv.DictReader(stream))
    previous_summary = json.loads((previous_pack / "public_summary.json").read_text(encoding="utf-8"))
    check(previous_summary["final_training_batch"]["plan_id"] == summary["plan_id"], "Cross-run plan differs")
    keys = [(r["actor"], r["case_id"]) for r in previous + rows]
    check(len(keys) == len(set(keys)) == 14, "Overlapping published case sets")
    aggregate = summary["cumulative_published_recovery"]
    check(aggregate["closed_cases"] == 14 and aggregate["counts"] == {"PASS": 9, "INCONCLUSIVE": 5, "FAIL": 0}, "Aggregate mismatch")
    check(Counter(r["status"] for r in previous + rows) == Counter(aggregate["counts"]), "Aggregate differs from CSVs")
    check(summary["whole_queue_complete"] is False and summary["full_stage_acceptance"] is False and
          summary["automatic_stage_consolidation"] is False and summary["zero_lab_execution_for_these_cases_proven"] is False,
          "Scope boundary changed")
    check(summary["paid_cost_usd"] is None and summary["model_calls"] is None, "Unknown usage relabeled")
    check(summary["provenance"]["raw_run_json_available"] is False and summary["provenance"]["original_signatures_verified"] is False,
          "Unavailable original evidence relabeled")
    check(summary["provenance"]["sanitized_sha256"] == manifest["files"]["operator.log"], "Provenance hash differs")
    print("PASS: stopped continuation export agrees with terminal chronology and both case sets.")
    print("Latest: 4 PASS / 3 INCONCLUSIVE / 0 FAIL; STOPPED_INFRASTRUCTURE.")
    print("Public export consistency only; not original signature verification or independent replication.")


if __name__ == "__main__":
    try:
        verify()
    except (ValueError, KeyError, TypeError, OSError) as exc:
        raise SystemExit("FAIL: " + str(exc))
