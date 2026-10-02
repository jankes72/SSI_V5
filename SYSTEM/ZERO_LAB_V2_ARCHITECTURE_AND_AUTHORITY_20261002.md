# ZeroLab V2 — architecture, authority and consolidation boundaries

**Date:** 2026-10-02  
**Version:** `SSI_ZERO_LAB_V2_20261002`  
**Basis:** reviewed private V2 implementation and operator runtime output. This document publishes architecture at a safe level; proprietary source and private runtime state remain private.

ZeroLab provides a common engine for versioned local software experiments in CZARA and SSI Final. It binds a research question, hypothesis, test inputs, acceptance criteria and candidate method to an execution record. V2 is a bounded implementation of part of the earlier [LAB_ARCHITECT research design](../CZARA_ZERO_LAB_LAB_ARCHITECT_MODULE_20261001.md).

## Research workflow

1. The professor or local operator introduces the experiment through the selected Director's chat/command path.
2. The Director identifies the objective and hypothesis. The chosen BODY checks input completeness and supported execution resources. A draft with missing inputs remains incomplete.
3. The lead researcher defines or revises the versioned protocol, including criteria and permission for shadow work. Candidate methods are recorded separately.
4. The selected executor runs an authorized method using a supported local adapter and records its result against the protocol and method identities.
5. Czara can observe translated expert proposals for a focused experiment and prepare shadow work where permission exists.
6. After reviewing the evidence, the professor/operator may select a shadow direction. Selection creates a new main branch with a new execution; the previous shadow remains in the record.

Protocol revision creates a new version. An instruction inside model output cannot itself grant authority or silently change frozen criteria.

## Actors and scopes

| Scope | Coordination | Execution | State boundary |
|---|---|---|---|
| CZARA | Czara research-context layer and Director_Czary | Canonical BODY_FROZEN_1_0 | Separate experiment scope |
| FINAL | Independent Director_Final | Final BODY_FROZEN and ISKRA1–ISKRA6 | Separate experiment scope |

BODY_FROZEN_1_0 and Final BODY_FROZEN are distinct runtime identities. The two Directors remain distinct. Shared ZeroLab storage separates experiment scopes and event chains; sharing that store does not merge memories or transfer identity.

The reported capacity policy assigns one slot to each scope's group under a shared USD 6/day budget. This is a resource-control setting, not evidence of learning or consolidation.

## What V2 can execute

| Component | Implemented scope | Observed evidence in this publication |
|---|---|---|
| Record transformation adapter | Bounded operations over supplied local records | 8/8 executor demonstration PASS |
| Native micronetwork adapter | Uses an existing installed artifact and explicit input vectors | Available in reviewed source; this pilot does not establish its performance |
| Input-completeness checks | Missing protocol fields, unsupported resources and incomplete execution inputs remain explicit | Implemented; broad adversarial coverage is not inferred from readiness |
| Model-assisted planning | Proposes a method under the existing protocol; live access is explicitly enabled | Not exercised by the zero-model pilot |
| Physical equipment | Requires an appropriate separately integrated adapter | No physical adapter or physical validation established here |

V2 does not turn arbitrary generated source code into an executable laboratory. Dynamic assembly stays within supported local operations and adapters. Installed skill/procedure entries describe available operations; installation alone grants no learned-skill qualification.

## Main and shadow authority

The professor/operator controls the main protocol, focus and main execution. An expert proposal can initiate shadow work only within the existing authorization. Students and translated statements do not acquire elevated authority by content alone.

The observer path requires a successfully translated eligible expert statement, a focused experiment and permission for shadow work. Shadow results remain separate from the main result. A successful shadow is not copied into a main PASS record; approved promotion executes the selected method again.

The full professor-chat → BODY input check → experiment → observed expert proposal → shadow → approved main revision sequence remains an end-to-end validation target. The first pilot confirms a narrower local command/execution route.

## Evidence and consolidation

The ZeroLab store records protocol/method identities, executor receipts and local hash-chain integrity information. A local hash chain is not an external signature, independent audit or external replication. The public pilot hashes in this release are operator-reported references; original receipt files are not included.

| Mechanism | Current boundary |
|---|---|
| ZeroLab execution | Local experiment receipt; not an automatic training grade |
| Selected S20-S26 recovery runner | No automatic stage consolidation and no full-stage acceptance |
| Ordinary full-stage SSI Final runner | Separate verified-subset consolidation path into Final BODY_FROZEN and Director_Final |
| Director_Czary access to Final hints | Read-only contextual use is possible in the reviewed integration; not bidirectional consolidation |
| Global consolidation across both scopes | Not established by this release or the first results |

The regular Final consolidation implementation distinguishes retained verified knowledge from retraining weights or transferring core identity. None of these distinctions makes the eight executor pilot a shared learning event.

See [first results](../ZERO_LAB_V2_FIRST_RESULTS_20261002.md) and the [public evidence pack](../evidence/ZERO_LAB_V2_20261002/README.md).
