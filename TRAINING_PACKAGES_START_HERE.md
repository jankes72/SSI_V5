# SSI V5 — Pre-Experiment Training Packages

**Recorded:** `2026-09-08`  
**Status:** `PREDECLARED / HASH-SEALED / NOT YET EXECUTED`

SSI V5 now has a predeclared preparation stage between technical readiness and the later mechanism/cross-domain experiments.

The stage contains **14 independent training packages**:

```text
7 BODY lines
x
2 training phases per BODY
=
14 packages
```

Training phases:

```text
A — FOUNDATION
programming + debugging + planning + evidence + checkpoint/resume + resource-aware execution

B — LEGO / MICRONETWORK / V10 PRACTICUM
composition + reuse + verification + false-reuse protection + anti-loop + recovery + persistence + route-cost measurement
```

Canonical methodology:

- [`PREEXPERIMENT_TRAINING_PROGRAM_20260908.md`](PREEXPERIMENT_TRAINING_PROGRAM_20260908.md)

Canonical package/hash registry:

- [`PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md`](PREDECLARED_14BODY_TRAINING_PACKAGES_20260908.md)

Shared curriculum integrity references:

```text
FOUNDATION = 61a3069ce68d19c64d4ae7c5ebc730d04283d81b2e534f487c3fd5063d9b75b8
PRACTICUM  = abc3eccc4e19849f2d3b3be5b1a4d2752377b6024225f0da8d7d54f4ebafc7ce
```

The same curriculum core is used across all seven independent BODY lines. Training writes to versioned descendants (`FOUNDATION_S1` then `TRAINED_START_S2`); historical T0 states remain preserved.

The exact later experiment vectors are excluded from training. Training teaches general mechanisms and skills, not the held-out answers.

Timing evidence records the route actually reported by the runtime and compares, where genuinely observed and comparable, `FULL_FLOW`, `VERIFY_TOPK`, `REUSE_TOP1`, LEGO/composition and recovery costs together with correctness and hardware/model context.

The previously predeclared EXP-01 ... EXP-07 hashes remain historical precommitments and are not silently rewritten by this training stage. A post-training run must identify the exact S2 start-state hash; if that materially changes a frozen experiment input, the experiment receives a new version/hash.

Public package records contain no private SSI, Micronetwork, Router V10 or ISKRA implementation source. The generated ZIPs were scanned before publication for private paths, Tailscale/LAN IP patterns, credential signatures and private BODY-layout names; the scan found no matches.
