#!/usr/bin/env python3
"""Verify this public export's consistency, not private runtime authenticity."""
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "evidence" / "ZERO_LAB_V2_20261002"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(name):
    return json.loads((PACK / name).read_text(encoding="utf-8"))


def verify():
    manifest = read_json("publication_manifest.json")
    files = manifest["files"]
    require(set(files) == {"public_summary.json", "pilot_terminal_report.json",
                           "final_case_results.csv", "final_resume_operator.log"},
            "Unexpected manifest file set")
    for name, expected in files.items():
        actual = hashlib.sha256((PACK / name).read_bytes()).hexdigest()
        require(actual == expected, "Export hash mismatch: " + name)

    summary = read_json("public_summary.json")
    pilot = read_json("pilot_terminal_report.json")
    log = (PACK / "final_resume_operator.log").read_text(encoding="utf-8")
    with (PACK / "final_case_results.csv").open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))

    extracted = re.findall(r"^\[CASE_DONE\] (\S+) (\S+) (PASS|INCONCLUSIVE|FAIL) .*", log, re.M)
    require(extracted == [(r["actor"], r["case_id"], r["status"]) for r in rows],
            "CSV outcomes differ from terminal transcript")
    require(len(rows) == len({(r["actor"], r["case_id"]) for r in rows}) == 7,
            "Expected seven unique actor/case outcomes")
    counts = Counter(r["status"] for r in rows)
    expected_counts = {"PASS": 5, "INCONCLUSIVE": 2, "FAIL": 0}
    require({k: counts[k] for k in expected_counts} == expected_counts, "Unexpected case counts")
    batch = summary["final_training_batch"]
    require(batch["counts"] == expected_counts and batch["case_count"] == len(rows),
            "Summary case counts differ")
    require(batch["status"] == "DOMAIN_BATCH_COMPLETE" and
            "[DOMAIN_BATCH_RESULT] DOMAIN_BATCH_COMPLETE {'INCONCLUSIVE': 2, 'PASS': 5}" in log,
            "Missing completed-batch evidence")
    require(all(r["run_id"] == batch["run_id"] for r in rows) and batch["run_id"] in log
            and batch["plan_id"] in log, "Run/plan identity mismatch")
    require(batch["queue_before"] == 621 and "[KOLEJKA] pozostalo=621;" in log and
            batch["queue_after_derived"] == batch["queue_before"] - len(rows), "Queue arithmetic mismatch")

    candidate_counts = []
    mismatch_flags = []
    current_count = 0
    mismatch = False
    for line in log.splitlines():
        if line.startswith("[CASE_REQUEST]"):
            current_count = 0
            mismatch = False
        match = re.match(r"\[NATIVE_CANDIDATE\] (\d+) ", line)
        if match:
            current_count = max(current_count, int(match.group(1)))
        if line.startswith("[TRAINING_EVENT]") and "LAB_OUTPUT_MISMATCH" in line:
            mismatch = True
        if line.startswith("[CASE_DONE]"):
            candidate_counts.append(current_count)
            mismatch_flags.append(str(mismatch).lower())
    require(candidate_counts == [int(r["candidates_observed"]) for r in rows], "Candidate history mismatch")
    require(mismatch_flags == [r["lab_mismatch_observed"] for r in rows], "Mismatch history lost")
    require(all(r["final_reason"] == "rnd_lab_comparison_not_verified" for r in rows
                if r["status"] == "INCONCLUSIVE"), "Unresolved reasons lost")

    actors = {"BODY_FROZEN_1_0", "BODY_FROZEN"} | {"ISKRA" + str(i) for i in range(1, 7)}
    results = pilot["pilot"]["results"]
    require(len(results) == 8 and {r["actor"] for r in results} == actors, "Pilot actor set differs")
    require(len({r["experiment_id"] for r in results}) == 8, "Duplicate pilot experiment")
    require(all(r["status"] == "PASS" and re.fullmatch(r"[a-f0-9]{64}", r["receipt_sha256"])
                for r in results), "Pilot verdict or hash format invalid")
    ready = pilot["readiness"]
    require(ready["status"] == "READY" and ready["models_called"] == 0, "Readiness boundary changed")
    require(len(ready["runtimes"]) == 9 and {r["actor"] for r in ready["runtimes"]} == actors | {"DIRECTOR_FINAL"},
            "Readiness actor set differs")
    require(all(r["status"] == "READY" and r["version"] == summary["zero_lab"]["version"]
                for r in ready["runtimes"]), "Runtime version/readiness mismatch")
    for item in [pilot["pilot"], summary["zero_lab"]["pilot"]]:
        require(item["training_pass"] is False and item["models_called"] == 0 and
                item["scope"] == "DEMONSTRATION_LOCAL_DATA_ONLY", "Pilot claim boundary changed")
    require(summary["zero_lab"]["pilot"]["counts"] == {"PASS": 8, "INCONCLUSIVE": 0, "FAIL": 0},
            "Pilot summary counts differ")
    tests = summary["resume_offline_tests"]
    require(tests["passed"] == tests["total"] == 19 and tests["models_called"] == 0 and
            tests["transport"] == "SYNTHETIC" and "Ran 19 tests in 7.523s" in log and
            "\nOK\n" in log, "Offline test summary mismatch")
    require(batch["model_calls"] is None and batch["paid_cost_usd"] is None, "Unknown batch usage relabeled")
    require(batch["automatic_stage_consolidation"] is False and batch["full_stage_acceptance"] is False and
            batch["zero_lab_execution_for_these_cases_proven"] is False, "Batch claim boundary changed")
    provenance = summary["provenance"]
    require(provenance["independently_reverified_signed_run"] is False and
            provenance["raw_run_json_available"] is False and
            pilot["provenance"]["receipt_hashes_independently_recomputed"] is False,
            "Unavailable provenance relabeled as verified")
    require(provenance["sanitized_final_transcript_sha256"] == manifest["files"]["final_resume_operator.log"],
            "Transcript provenance hash mismatch")
    print("PASS: public export hashes and transcript/CSV counts agree.")
    print("ZeroLab pilot: 8 PASS; Final batch: 5 PASS / 2 INCONCLUSIVE / 0 FAIL.")
    print("This check does not verify original runtime signatures or independently reproduce the experiments.")


if __name__ == "__main__":
    try:
        verify()
    except (ValueError, KeyError, OSError, TypeError) as exc:
        raise SystemExit("FAIL: " + str(exc))
