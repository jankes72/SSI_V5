# SSI V5 — UAV and permanent R&D laboratories — 23 September 2026

**Status:** private software implementation documented; R3 integration locally tested and delivered. **No post-installation report, physical vehicle integration or external pilot completion is established by this update.**

The permanent laboratory connects training failures to reproducible R&D work. BODY_FROZEN owns registered experiments; DIRECTOR retains its separate core, runtime, memory and lifecycle. The public repository exposes results and review documents, not execution controls or proprietary implementation.

## Capability and deployment matrix

| Area | Implemented capability | Evidence / current limit |
|---|---|---|
| Training LAB | Native evaluation, bounded graph execution, independent review requirements and retained unresolved outcomes | Previous S11 has 210 recorded cases; 13 unresolved |
| Permanent R&D | Registered baseline/candidate comparisons with hypothesis, requirements, seed, repetitions and immutable protocol identity | Local CPU comparison tests; expert judgments remain separate from training grades |
| R3 shared diagnostics | Block/operation/test context, bounded failing-input evidence, duplicate-candidate detection and replay fixtures | Thirty actual rejected reports replayed without changing grades; registered R&D integration tested offline |
| UAV bench | Deterministic 2-D kinematic comparison of baseline and candidate controllers | Software properties only; not aerodynamic fidelity, autopilot SIL/HIL or physical flight evidence |
| External expert workspace | Observer/expert roles, reviews, credential revocation, software stop and optional presence heartbeat | Implemented access paths; no completed external session established here |
| Tailscale access | Intended private transport for authorized expert access to the lab | Deployment/ACL connectivity and an external partner session remain to be verified |
| Four-domain registry | Four configurable domain slots plus a demo scope | A registry is not four validated physical models; each domain needs its own protocol |
| Physical drones/humanoids | Physical mode rejected when no adapter is configured | PHYSICAL_ADAPTER_NOT_CONFIGURED; no fleet-control or hardware-stop validation claimed |
| Evidence sharing | Experiment summaries available to seven BODY lines and the independent DIRECTOR | Separate consumer state; no automatic memory/weight merging or Champion promotion |

## What R3 adds to training and R&D

The same bounded diagnostics layer observes the unchanged comparison interpreter in an isolated worker. On an execution error it retains the failing test, block, operation, limited input context and preceding trace. Declaration failures identify the relevant field; locality diagnostics retain strict metadata requirements; fault diagnostics expose disagreement with supplied observations.

An unchanged rejected candidate is recognized after canonicalization, even if whitespace or key order differs. The previous deterministic rejection and its origin remain visible, without rerunning the same LAB or calling the reviewer for that duplicate. This does not remove the cost of already generated answers. A changed candidate can use remaining attempts within existing time, tier and cost limits.

A failed candidate can become an actor/task-bound R&D regression fixture with source hashes. Replay produces a new comparison result while preserving the historical failure. It never assigns a desired PASS in advance or bypasses native evaluation and required review. The original native evaluator and R&D interpreter were not modified in R3.

## Controlled expert experiment

1. Agree the domain, unseen problem, baseline, acceptance criteria and inconclusive policy before execution.
2. Register the frozen protocol and its input/version bindings. A changed protocol requires a new experiment.
3. Execute within the declared software scope; retain measured output, failures and diagnostics.
4. Allow an authorized expert to observe, submit a separate review or stop the software experiment.
5. Verify evidence integrity and report PASS, FAIL, INCONCLUSIVE or STOPPED without rewriting history.
6. Evaluate any transfer or deployment under its own target-specific conditions.

The workspace can support an external UAV research collaboration, including the planned Mexico collaboration, but no university endorsement, named partner approval or executed external pilot is asserted. No private correspondence or partner data is published.

The software stop acts on the experiment executor; it has not been shown to stop a physical vehicle. Tailscale connectivity alone does not supply a hardware driver or hardware safety interlock. Physical experiments require their own integrated adapter, measured behavior, expert control and evidence.

## Relation to LEGO and earlier domain results

LEGO Pocket retains candidates and provenance; Pocket Micro keeps qualified derived packages; META-LEGO supplies compatibility and evidence metadata. The previous preflight checked one qualified package for seven actors, without proving the whole catalog executable. R3 adds no automatic promotion or unrestricted cross-BODY consolidation.

The earlier [LEGO and Director-connected architecture](LEGO_POCKET_META_LEGO_AND_DIRECTOR_LABS_20260922.md) and [Dual Mother software results](../RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md) retain their original scope and dates. The new small UAV bench is a different harness. Historical humanoid software results do not demonstrate physical humanoid deployment. The [Football World](../RESULTS/FOOTBALL_WORLD_IMPLEMENTATION_BOUNDARY_20260922.md) still needs its own complete data/outcome validation.

## Verified release boundary

[R3 validation](../RESULTS/SSI_V5_LAB_RND_R3_TEST_SUMMARY_20260923.json): 105 PASS, one SKIPPED, zero paid model calls in the suite. Model responses and native integration paths use explicit offline fixtures where identified. Existing lab/access capabilities were reported in the [earlier release](../RESULTS/SSI_V5_LAB_AND_S11_CONTINUATION_20260922.md); its 165-test count belongs to that different release, not R3.

The delivered R3 budget is 6 USD per day shared across all seven BODY. Existing spend and uncertain reservations are retained. No measured savings or provider account balance is inferred. Installation on the target machine, live expert access, independent key custody and physical pilots remain separately verifiable milestones.
