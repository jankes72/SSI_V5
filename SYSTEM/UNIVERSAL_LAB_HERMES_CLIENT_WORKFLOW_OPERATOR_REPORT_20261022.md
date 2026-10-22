# Universal Lab: Hermes first contact and client research workflow

**Date:** 22 October 2026 (Europe/Warsaw).  
**Evidence class:** author/operator report and architecture clarification.  
**Publication:** the author explicitly authorized publication of these details on the public SSI GitHub.  
**Scope:** existing visitor-facing and meeting functions as reported by the operator; future model replacement and resource-isolation choices are identified separately. This note includes no new independent runtime, latency, isolation or client-delivery test.

## Polski — istniejący przebieg obsługi

Autor SSI opisuje istniejącego Hermesa na stronie wejściowej przed logowaniem do Universal Lab. Hermes odpowiada na pytania o SSI, wskazuje odpowiednie materiały oraz umożliwia złożenie prośby o dostęp tymczasowy lub dane logowania wraz z opisem projektu i oczekiwanej pomocy. Złożenie prośby i faktyczne przyznanie dostępu to osobne kroki.

Moduł Hermesa działa bezpośrednio na komputerze Dyrektora. Według operatora przeznaczono na niego osobny budżet RAM, aby ograniczyć wpływ obsługi odwiedzających na pozostałe działania Dyrektora. Docelowy mechanizm izolacji — kontener z odpowiednią polityką swapu albo inny moduł — pozostaje do wyboru. Ta deklaracja nie jest pomiarem twardego limitu systemowego ani dowodem całkowitego braku zakłóceń.

Po uzyskaniu dostępu partner może spotkać się z Pawłem w Universal Lab, korzystając z kamery i tłumaczenia. Operator opisuje równoległą pracę Czary w Shadow: podczas rozmowy o potrzebach klienta przygotowywany lub prowadzony jest eksperyment/benchmark dopasowany do omawianego problemu. Wyniki i przygotowana propozycja rozwiązania mogą zostać omówione jeszcze podczas spotkania. Status propozycji, rzeczywistego wykonania i wyniku ocenionego według kryteriów pozostaje rozróżniony dla konkretnego przypadku.

Po spotkaniu operator może wysłać informacje z benchmarku e-mailem i uzgodnić dalsze wdrożenie w projekcie klienta. Opisuje to dostępny przebieg pracy, a nie potwierdzenie wysłania konkretnego raportu lub zakończenia konkretnego wdrożenia klienta.

## Plan własnego modelu i jawne ograniczenia

Docelowo Hermesa ma zastąpić własny, mały model SSI wyspecjalizowany do pytań o projekt, przygotowany przez destylację i optymalizację pamięci. Ten model zastępczy nie jest tu ogłaszany jako już wytrenowany lub wdrożony. Interfejs ma pokazywać faktycznie używany model, aby odwiedzający wiedział, z czym rozmawia i co sprawdza.

Publiczny punkt kontaktu może odpowiadać wolniej. Operator opisuje szybszą ścieżkę pracy po zalogowaniu; ta nota nie zawiera porównania liczbowego opóźnień ani gwarancji czasu odpowiedzi. Mały rozmiar modelu i docelowa jakość odpowiedzi wymagają własnych pomiarów.

## Status table

| Area | Reported current function or future goal | Evidence boundary |
| --- | --- | --- |
| First-contact Hermes | Existing SSI question answering and links before Universal Lab login | Author/operator report; no fresh external reachability test or live service URL published here |
| Hosting and RAM | Module on the Director's computer with a RAM budget set aside | No RAM amount, enforced OS limit or non-interference benchmark established by this note |
| Final isolation | Container/swap policy or another module is under consideration | Open implementation choice; not an installed design established here |
| Visitor performance | Public responses may be slow; a faster logged-in path is described by the operator | No quantified latency comparison or SLA |
| Model transparency | Display the actual serving model | Interface goal; no exact installed revision/digest inferred |
| Own SSI student | Task-specialized replacement after distillation and memory optimization | Planned; student training, quality and deployment not established here |
| Access requests | Project/need description and request for temporary or account access | Request is separate from authorization and account issuance |
| Meeting | Camera conversation and translation in Universal Lab after access | Existing workflow described by the operator; no new partner/audio acceptance test in this publication |
| CZARA Shadow | Client-specific experiment or benchmark prepared/run alongside discussion | Keep proposal, execution and validated-result status explicit |
| Follow-up | Operator can email benchmark information and discuss implementation | Capability/workflow, not proof of a particular email delivery or client deployment |

## Workflow for an outside reader

1. **Ask about SSI:** use the first-contact assistant and follow its project-information links.
2. **Describe the need:** explain the project, problem and expected assistance; request the relevant temporary or account access.
3. **Meet in Universal Lab:** discuss requirements with the SSI author using camera and translation after access is granted.
4. **Inspect parallel research:** CZARA Shadow prepares/runs the problem-specific experiment as the discussion supplies requirements.
5. **Review the outcome:** compare benchmark findings and the prepared solution proposal with the actual requirements and acceptance criteria.
6. **Receive follow-up:** the operator can email benchmark information and agree on the specifically qualified implementation work.

This is the author's account of his existing environment and intended client use. It does not promise a completed solution to every possible problem during one meeting or universal support for every service, hardware target or task domain.

## Relationship to other SSI records

- [A16 installation and prepared explanations](../RESULTS/UNIVERSAL_LAB_DIRECTOR_A16_PROGRESS_20261012.md) describes the distinct narrator/conversation layer, its installation/HTTP readiness and its dated live-test boundaries. It is not a runtime receipt for this first-contact module.
- [A16 PL/EN knowledge catalog](../KNOWLEDGE/SSI_DIRECTOR_A16_PL_EN_20261012.md) contains authored explanations. Its Hermes knowledge-generation topic must not be conflated with the visitor-facing assistant.
- [Canonical architecture](../SSI_V5_C4_ARCHITECTURE.md) retains the Director, BODY, CZARA/Shadow, Router and Research Memory responsibilities. The older 12 October public web-Director declaration has its own delivery scope and remains historical evidence.
- [Evidence and Notary contract](../UNIVERSAL_LAB_EVIDENCE_NOTARY_AND_ATTESTATION_CONTRACT_20261008.md) distinguishes provenance from task correctness. This operator report adds no independent attestation.
- [MultiQuant D1–D5](../PUBLIC_MODELS/SSI_MULTIQ_FIVE_DIRECTIONS_R4_R5_DECLARATION_20261018.md) remains the reference for separate student/distillation and model-optimization research boundaries.

Public disclosure covers roles, workflow, status and research goals. Private source, model recipes, operational addresses, client data, credentials and internal RAM configuration remain unpublished.
