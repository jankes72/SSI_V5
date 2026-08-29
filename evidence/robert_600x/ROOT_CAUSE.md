# ROBERT 600X — ROOT CAUSE

## LAST_GOOD_TRANSITION

`NO_MATCH -> CANDIDATE`

## FIRST_BAD_TRANSITION

`CANDIDATE -> EVIDENCE ACCUMULATION -> ELIGIBILITY -> CHALLENGER (repeated / replay)`

## ROOT_CAUSE_DUPLICATION

`robert/micronetworks.py:170` — `promote_challenger()` lacked idempotency guard. It wrote CHALLENGER status unconditionally, so repeated calls on the same candidate created duplicate persistent writes and duplicate promotion events.

`robert/micronetworks.py:276` — `add_experience_to_candidate()` lacked deduplication by `experience_id`. Blind append caused duplicate Experience records on retry/replay.

`robert/runtime.py:241` — `_feedback_for()` called `promote_eligible_candidates()` unconditionally after every mission outcome, including retries and replays.

## ROOT_CAUSE_REPLAY

`robert/micronetworks.py:315` — `check_candidate_eligibility()` used `candidate.get("evidence", {})`. When a candidate JSON had `"evidence": null`, `.get()` returned `None` because the key existed, so `evidence.get("experiences", [])` raised:

`AttributeError: 'NoneType' object has no attribute 'get'`

`robert/micronetworks.py:68` — `reload()` stored raw `d.get("evidence")` without normalizing `None` to `{}`.

## NONE_SOURCE

Candidate files containing `"evidence": null` were loaded by `reload()` and stored as `None` in `self.candidates`. During replay/reload, `check_candidate_eligibility()` called `.get()` on that `None` value.
