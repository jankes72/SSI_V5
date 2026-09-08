# TEST3 FAILED FIELD AUDIT

Date: 2026-09-02

## Purpose

Determine the semantics of the `failed` field in `TEST3_SUMMARY.json` from the code and the real execution path.

## Finding

The `failed` field was incremented for real unresolved failures, including exceptions, REUSE without a target capability, REUSE without real execution, routing mismatch and UNKNOWN_DECISION.

The old PASS formula checked `incorrect_routing`, `background_failures`, `exceptions`, `reuse_without_capability` and real execution, but **did not check `failed == 0`**.

In the first 100x run, iterations 38, 42 and 50 had `failed=1/1/2` respectively while still reporting `pass=True`.

## Conclusion

This was not a valid "intermediate state" interpretation. `failed` represented a real unresolved failure, so the earlier 100/100 result could not support final closure.

## Contract repair

The PASS condition was strengthened with:

```text
failed == 0
```

The final contract requires:

```text
total == 600
accounted == 600
incorrect_routing == 0
background_failures == 0
exceptions == 0
reuse_without_capability == 0
failed == 0
reuse_real_execution >= 1
```

After the repair, a new 100x run was executed from the beginning. The final run completed with 100/100 PASS, 60,000/60,000 accounted and `failed_total=0`.

The historical incorrect PASS remains part of the lineage rather than being deleted.