# SSI V5 — migracja na serwery 24/7 (R1: ROBERT jako pierwszy)

**Data ustalenia:** 17 października 2026 r.  
**Rodzaj dokumentu:** publiczny plan migracyjny i kryteria odbioru, bez instrukcji dostępowych.  
**Status:** PLAN / AUDYT W TOKU / BRAK POTWIERDZONEGO PRZEŁĄCZENIA PRODUKCYJNEGO.  
**Źródło architektury:** [kanoniczny model C4 SSI V5](SSI_V5_C4_ARCHITECTURE.md). Ten dokument nie zastępuje ani nie duplikuje diagramów C4.
**Uzupełnienie ewidencji:** 17 października 2026 r. — sprawdzono bieżący plik migracji, publiczne zapisy szkoleń Roberta i aktorów oraz nadrzędną decyzję modeli R7; brak pełnego audytu prywatnych baz i serwerów.

> **Ochrona informacji:** w publicznym repozytorium nie umieszczamy kodu produkcyjnego, adresów serwerów, nazw hostów, prywatnych tras, portów usług, konfiguracji tuneli, kluczy, tokenów, haseł, zrzutów baz danych, pamięci agentów, materiałów klientów ani raportów mogących ujawnić te dane. Szczegółowe manifesty migracji, backupy i poświadczenia pozostają w prywatnym magazynie SHARE.

## 1. PRIORYTET PIERWSZY — SSI ROBERT

### 1.1. Rola Roberta

Robert jest odrębnym agentem technicznym i wykonawczym SSI V5, a **nie drugim Dyrektorem**. Otrzymuje misje w ramach centralnej organizacji SSI, przygotowuje ich wykonanie, prowadzi eksperymenty techniczne i automatyzacje, zbiera dowody i przekazuje materiały do wyspecjalizowanego SSI CODEX. Decyzje organizacyjne, zakres dostępu do projektów oraz zatwierdzenia działań i budżetu pozostają po stronie Dyrektora i istniejących zasad SSI.

### 1.2. Co już istnieje, a czego jeszcze nie potwierdzono

| Obszar | Stan dowodowy na rozpoczęcie migracji |
| --- | --- |
| Robert API i Robert Control Center (RCC) | Prywatny odczyt lokalnego węzła wykazał aktywne usługi; brak potwierdzenia pracy na VPS. |
| Mission Navigator, nawigacja GUI, Vision, Research Memory, Memorize i Notariusz IT | Istnieją moduły i wyniki eksperymentów o ograniczonym zakresie; pełna, samodzielna realizacja wieloetapowych misji wymaga odbioru. |
| Mosty do Dyrektora / Universal Lab | Istnieją lokalne integracje; ich funkcjonalność po przeniesieniu usług wymaga testów między serwerami. |
| Przekazywanie propozycji misji do CODEX | Opracowano kontrakt i adaptery, w tym obsługę przyjmowania propozycji; pełny przepływ trzech ról wymaga weryfikacji live. |
| Jedno logowanie Universal Lab / delegacja do RCC | Kod i testy offline zostały przygotowane; **nie jest to jeszcze potwierdzone produkcyjne SSO**. |
| Playwright uruchamiany serwerowo, trwała kolejka, recovery po awarii | Wymagane na docelowym VPS; aktualny status i komplet zależności muszą zostać ustalone audytem. |
| Lokalne GUI oparte na Wayland/PipeWire i urządzeniach wejściowych | Zdolność lokalnego rozszerzenia, a nie zależność krytyczna VPS. |
| SSI MultiQuant MICRO-13 i modele przyszłe | Według najnowszego R7: pierwsze 13 kandydatów na serwerze pełniącym rolę MODELS, wyłącznie po kontroli zasobów; 5 dodatkowych slotów Robert/Director to plan. **0 nowych wag i 0 aktywacji potwierdzonych w opublikowanym R7.** |

**Zasada dowodowa:** `CODE_READY`, `OFFLINE_TESTED`, `INSTALLED` i `LIVE_VERIFIED` to różne stany. Brak dowodu oznacza `UNKNOWN`, a nie `PASS`.

### 1.3. Niezbędny zakres ROBERT VPS 24/7

Na własnym serwerze Robert musi działać samodzielnie, nawet gdy lokalny komputer jest wyłączony. Zakres obowiązkowy:

1. Rdzeń Roberta, API, panel raportów RCC i zarządzanie cyklem misji.
2. Planowanie etapów, wykonanie, trwała kolejka, checkpointy, wznowienie i recovery.
3. Pamięć operacyjna, Research Memory, rejestr sprawdzonych skilli i niezbędne mikrosieci.
4. Serwerowa automatyzacja przeglądarki przez Playwright, z izolacją sesji i bez zależności od fizycznego monitora.
5. Notariusz IT: bieżące Evidence, identyfikowalność działań, zapis i weryfikacja wyników.
6. Uwierzytelniona komunikacja z Dyrektorem, sekretarką Charlie, Universal Lab i SSI CODEX.
7. Kontrolowany dostęp do modeli lokalnych lub zewnętrznych przez wspólny router i limity kosztów; nie zakłada się instalacji ciężkiego GPU na VPS.
8. Nadzór nad stanem usług, ograniczanie ponownych wykonań, kontrola błędów i raportowanie postępu.

### 1.4. Trzy klasy zdolności

| Klasa | Zasada | Przykłady |
| --- | --- | --- |
| `SERVER_NATIVE` | Działa na VPS bez lokalnego komputera. | Kolejka, pamięć operacyjna, serwerowy Playwright, API, komunikacja agentów, notariusz. |
| `LOCAL_EXTENSION` | Wymaga świadomie udostępnionego lokalnego węzła. | Fizyczny ekran, mysz, klawiatura, lokalny pulpit, aplikacje desktopowe. |
| `HYBRID` | Działa na VPS; lokalny węzeł tylko rozszerza możliwości. | Vision przez API z opcjonalnym lokalnym obrazem, wybrane skille, analizy archiwów. |

Jeśli misja wymaga niedostępnego lokalnego pulpitu, **tylko ona** przechodzi do stanu `WAITING_FOR_NODE01`. Nie wstrzymuje to rdzenia Roberta, Dyrektora, CODEX-a ani pozostałych misji.

### 1.5. Co pozostaje lokalnie

Fizyczna obsługa GNOME/Wayland, PipeWire, monitorów i urządzeń wejściowych, lokalne aplikacje, pełne archiwa, historyczne paczki, nieaktywne benchmarki, dodatkowe skille i duże dane. Nie wolno pozostawić ukrytej zależności krytycznego procesu VPS od dostępności tych zasobów. Audyt ma wykrywać odwołania do Waylanda, PipeWire, monitora, wejścia i lokalnych profili przeglądarki.

### 1.6. MICRO-13 / MultiQuant R7 — aktualna decyzja o miejscu budowy

**Korekta z 17 października 2026 r.:** wcześniejsza propozycja R5/R6, w której Robert był wyłącznym miejscem kwantyzacji pierwszej trzynastki, została **zastąpiona przez R7**. Nie wolno wydawać poleceń według starej lokalizacji prac.

- Na serwerze pełniącym rolę **SSI MODELS** zgłoszono **13 istniejących wariantów Ollama**; ich rzeczywiste tagi, sumy i obciążenie pozostają do odczytu live.
- **13 kandydackich wariantów MICRO** jest zaplanowanych; w dokumencie R7: **0 potwierdzonych nowych plików wag i 0 nowych wdrożeń**. Nie muszą powstać wszystkie, jeśli brakuje zgodnych źródeł, zasobów albo sensownej poprawy.
- Pierwszą trzynastkę **można budować na SSI MODELS VPS wyłącznie po bezpiecznym preflight CPU/RAM/dysku** i bez przerwania bieżącej inferencji. Gdy nie ma zasobów lub licencji: `RESOURCE_BLOCKED`, bez niejawnej migracji pracy na Roberta czy płatne GPU.
- **Pięć dodatkowych slotów dla Roberta i Dyrektora** pozostaje `PLANNED_UNSELECTED` / `NOT_BUILT` / `NOT_APPROVED`. Ich przyszłe przygotowanie jest odrębną decyzją, z osobnym preflight i zgodą.
- **Robert** analizuje metadane/kwalifikację modeli, wykorzystuje dopuszczone warianty podczas prawdziwych misji, współprowadzi ewidencję kompetencji i porównania z kontrolowaną pomocą notariusza. Może udostępniać zatwierdzone małe modele z wolnych zasobów tylko jako odłączalną usługę pomocniczą, bez gwarancji stałej dostępności.
- **Dyrektor z Routerem V10** wybiera modele, sprawdza uprawnienia, budżet i eskalację. **Notariusz** poświadcza prawdziwe dowody, a nie nadaje uprawnień do promocji modelu.
- Wyniki pochodzą z **rzeczywistych, autoryzowanych misji**. Bez podwójnego płatnego wnioskowania i bez sztucznych konkursów jako warunku uruchomienia.

Kwantyzacja nie zmniejsza liczby parametrów modelu; distylacja/adaptacja małego studenta to osobny proces. Modele, mikrosieci, Research Memory, SCC i reguły Routera pozostają odrębnymi zasobami.

**Liczby według R7:** `13 baseline (operator-reported) + 13 MICRO (planned, 0 built) + 5 future Robert/Director (planned, 0 built)`. Dawne `13 × MICRO/NANO = do 26` jest koncepcją historyczną, **nie obowiązującą kolejką produkcyjną**.

Źródło aktualnej decyzji: [SSI MultiQuant R7](PUBLIC_MODELS/SSI_MICRO13_DECISION_AWARE_MULTIQ_R7_20261017.md). Źródła wcześniejszego planu: [MICRO-13 R6](PUBLIC_MODELS/SSI_MICRO13_BASELINE_TO_CANDIDATES_R6_20261017.md) i [Robert Builder R5](PUBLIC_MODELS/SSI_V5_ROBERT_BUILDER_MODEL_VPS_PRODUCTION_R5_20261017.md), z zachowaną chronologią.

### 1.7. SSI Adaptive Model Pool — praca Roberta podczas rzeczywistych misji

Własne zadania Roberta, jego kolejka, pamięć, Playwright, notariusz i recovery mają **pierwszeństwo** przed mikro-modelem pomocniczym. Wolna moc CPU nie jest obietnicą dostępności zasobów ani zgodą na instalację.

1. Uprawniony Router sprawdza aktualnie dostępne, zaakceptowane modele na odpowiednich węzłach. Nie zakłada dodatkowego, czwartego fizycznego VPS: **SSI MODELS jest rolą serwerową**, a faktyczne współlokowanie z innymi usługami w istniejącej infrastrukturze trzeba zmierzyć.
2. Jeśli po preflight pozostał zapas CPU/RAM, Robert może **opcjonalnie** serwować kwalifikowaną małą inferencję przez uwierzytelniony API i izolowany kontener z limitami. Tę usługę można wyłączyć lub ograniczyć bez awarii głównego Roberta.
3. Każda autoryzowana misja zapisuje wersję modelu, kategorię, użyty zakres mikrosieci/kompetencji, wynik `PASS/FAIL/INCONCLUSIVE`, zasoby, koszt i przyczynę fallbacku. Nie ujawnia surowej prywatnej treści zadania.
4. Trzeba odróżniać skuteczność **model_only** od wyniku **model + Router + mikrosieci + narzędzia SSI**. Wynik kompozycji nie potwierdza samodzielnej kompetencji danego LLM.
5. Notariusz dokumentuje, weryfikator ocenia wynik, a Dyrektor/Router podejmują decyzję o dalszym użyciu lub eskalacji. Promocja modelu lub skilla nigdy nie wynika automatycznie z samego zapisu.
6. Niedostępność pomocniczego modelu nie blokuje zadań: Router wybiera inny dozwolony zasób albo jawny stan oczekiwania, bez powtórnego wykonania operacji o skutkach ubocznych.

## 2. Pozostałe role SSI na osobnych VPS

**SSI DIRECTOR:** centralna organizacja misji i kanoniczne identyfikatory projektu/zadania/misji, istniejące role i ACL, kontrola budżetu, decyzje, Universal Lab, obsługa centralnego logowania i przekazywanie uprawnień. Sekretarka Charlie wspiera planowanie, komunikację i bieżącą koordynację; nie zastępuje autoryzacji Dyrektora.

**SSI CODEX:** niezależny wykonawca programistyczny. Otrzymuje zatwierdzone zadania i materiały techniczne, planuje implementację, tworzy i testuje projekty, przygotowuje pakiety i zwraca raporty z dowodami. Jego działanie produkcyjne nie może zależeć od włączonego lokalnego komputera.

Lokalne komputery pozostają opcjonalnymi rozszerzeniami i archiwami. **Wyłączenie któregokolwiek z nich nie może zatrzymywać trzech serwerów.**

## 3. Jedno logowanie, bez anonimowego dostępu

- Jedyną standardową bramką logowania człowieka jest **Universal Lab na serwerze DIRECTOR**.
- Uprawniony użytkownik otwiera Roberta (RCC, misje, raporty) i CODEX bez drugiego formularza hasła.
- Backend Roberta i backend CODEX wymagają sprawdzonej, krótkotrwałej delegacji: odbiorca, użytkownik, projekt, operacja, identyfikator żądania, wygaśnięcie i aktualne ACL.
- Operacje wrażliwe i zatwierdzenie długiego transferu wymagają ponownej kontroli uprawnień. Wylogowanie, cofnięcie ACL lub zablokowanie konta unieważniają możliwość nowych operacji.
- Nie przekazujemy hasła, centralnego cookie ani kluczy maszynowych do przeglądarki, modeli lub między usługami jako substytutu autoryzacji użytkownika.
- **Nie wyłącza się starej ścieżki logowania RCC**, dopóki centralna delegacja i testy trzech systemów nie uzyskają statusu `LIVE_VERIFIED`. Żaden wariant docelowy nie otwiera anonimowego RCC.

## 4. Zachowanie mostów i komunikacji między węzłami

- Zachowujemy zgodne kontrakty, kanoniczne identyfikatory misji, uprawnienia, kolejność zdarzeń, historię i kanały zwrotne Evidence.
- Istniejące połączenia Tailscale oraz uwierzytelnione mosty SSH/API pozostają działające podczas przygotowania migracji. Ich nowe odpowiedniki serwer–serwer sprawdza się równolegle, zanim nastąpi przełączenie.
- Nie zakładamy, że sam dostęp do prywatnej sieci oznacza prawo do wykonania misji.
- Router kieruje zadania według klasy zdolności, stanu usługi i uprawnień. Nie wolno tworzyć zależności, w której ścieżka DIRECTOR–ROBERT–CODEX wymaga pośrednictwa wyłączonego komputera lokalnego.
- Zewnętrzne modele i zasoby GPU są wspólne przez kontrolowane interfejsy, ale mają odrębne liczniki, limity i zgody. Kolejka grupuje zadania i eliminuje zbędne uruchomienia; brak potwierdzenia wykonania nie uruchamia automatycznego duplikatu.
- Długotrwałe zadania wymagają trwałego stanu, idempotencji, potwierdzeń i odporności na utratę połączenia.

## 5. Audyt pojemności i zakres przenoszenia

Przed kopiowaniem czegokolwiek mierzymy faktyczne rozmiary aktywnego kodu, bibliotek, baz operacyjnych, pamięci, skilli, mikrosieci, kontenerów, środowisk Python i obrazów Playwright Chromium. Osobno wykazujemy dane pozostające lokalnie. Nie sumujemy podwójnie hardlinków i katalogów zagnieżdżonych.

Bilans VPS rozdziela: produkcyjny rdzeń po deduplikacji, środowisko wykonawcze, przestrzeń roboczą, rezerwę na nowe skille, przyrost pamięci, aktualizacje, backup i realnie dostępną pojemność po systemie plików. **Wartości niezmierzone pozostają `UNKNOWN`.**

Zgodnie z R7 pierwsze 13 kandydatów MICRO wymaga osobnego bilansu **SSI MODELS VPS**: źródło, plik tymczasowy, wynik, rollback i zapas CPU/RAM podczas zwykłych misji. ROBERT VPS planuje jedynie opcjonalną pulę zatwierdzonych małych modeli i pięć przyszłych slotów, a nie obowiązkowe budowanie pierwszej trzynastki. Nie rezerwujemy miejsca na niezbudowane wagi ani nie przyjmujemy, że zgłoszone 16 GB RAM jest w całości wolne.

Szczegółowe pomiary hostów, manifesty pakietów i mapowanie ścieżek nie są publikowane w tym repozytorium; trafiają wyłącznie do prywatnego SHARE. Publiczny dokument przedstawia zakres i granice twierdzeń, nie prywatną infrastrukturę.

## 6. Kolejność prac i bramki odbiorowe

| Faza | Działanie | Warunek przejścia |
| --- | --- | --- |
| R1 — Inventory | Odczyt aktualnych procesów, wersji, plików, rozmiarów i zależności. | Raport pomiarów + `UNKNOWN` dla braków, bez zmian produkcji. |
| R2 — Dependency split | Oznaczenie `SERVER_NATIVE` / `LOCAL_EXTENSION` / `HYBRID`. | Brak krytycznych odwołań VPS do lokalnego pulpitu. |
| R3 — Parallel readiness | Przygotowanie odizolowanego środowiska VPS, bez przełączania produkcji. | Health, stan danych, backup, odtwarzanie i rollback potwierdzone. |
| R4 — Central auth | Kontrolowane połączenie SSO DIRECTOR z RCC i CODEX. | Testy ACL, sesji, logout, cofnięcia praw i izolacji projektów. |
| R5 — Agent bridges | Test komunikacji i zwrotu wyników między trzema VPS. | Autoryzowana misja, zgodne identyfikatory, Evidence i brak duplikacji. |
| R6 — Failure tests | Odłączenie opcjonalnych lokalnych zasobów w kontrolowanym teście. | Serwery nadal wykonują misje; lokalna misja przechodzi w `WAITING_FOR_NODE01`. |
| R7 — Cutover | Przełączenie dopiero po akceptacji wszystkich wcześniejszych bramek. | `LIVE_VERIFIED`, uzgodniona procedura rollback i podpisany wynik odbioru. |
| R8 — MultiQuant / MICRO-13 (aktualne R7) | Inwentaryzacja 13 zgłoszonych bazowych modeli; do 13 kandydatów MICRO na roli SSI MODELS, wyłącznie przy potwierdzonych zasobach; osobno pięć przyszłych slotów Robert/Director. | Każda konwersja ma licencję, hash, pomiar, rollback, zgodę i własny stan; 0 nowych modeli nie może być przedstawiane jako 13 gotowych. |

### Minimalny scenariusz akceptacyjny

Użytkownik loguje się raz do Universal Lab. Dyrektor zatwierdza misję i jej budżet. Robert przygotowuje materiał techniczny i dowody. CODEX otrzymuje zatwierdzone zadanie, wykonuje implementację i testy, zwraca wynik. Robert i Charlie raportują przebieg; Dyrektor zamyka misję po weryfikacji. Wylogowanie, zmiana uprawnień, utrata sieci i wyłączenie lokalnego węzła nie mogą otworzyć obejścia autoryzacji ani wywołać podwójnego wykonania.

## 7. Warunki bezpieczeństwa i publikacji

Ten dokument **nie stanowi zgody na migrację**, instalację, zmianę tras, restart, publikację kodu czy uruchomienie płatnych modeli. Weryfikacja na rzeczywistych serwerach wymaga odrębnego, kontrolowanego procesu. Stan `OFFLINE_TESTED` nigdy nie jest dowodem `LIVE_VERIFIED`.

Prywatne dokumenty wdrożeniowe mogą zawierać niezbędne adresy, tajne manifesty i konfiguracje dostępu, ale **nie wolno ich kopiować do publicznego GitHuba**.

## 8. Rejestr szkoleń i misji Roberta przed migracją

**Cel:** przenieść **tożsamość, historię kompetencji i ciągłość misji Roberta**, nie tylko aktualny proces HTTP. Ta lista ma charakter publicznego indeksu *udokumentowanych linii rozwojowych*, a nie spisu wszystkich prywatnych zadań lub pełnej bazy skilli. Rozmiary i aktywny stan należy potwierdzić w prywatnym SHARE.

| Linia szkoleniowa / misja | Udokumentowane wyniki i granice | Wymaganie migracji |
| --- | --- | --- |
| **Canonical ROBERT / TEST 1–5** | Zapisana ciągłość Roberta; TEST 5 po niezależnym audycie: **29/29 akceptacji, 524/524 regresji**, w tym 46/46 ROBERT Stable. To wynik **lokalnego, określonego kontraktu**, nie akceptacja nowego VPS. | Zachować tożsamość, starsze porażki, poprawki, historię regresji i wersje stanu. |
| **Idempotencja i odporność Micronetworks / Robert (600x)** | Po wcześniejszych FAIL: **600/600**, brak duplikacji końcowego stanu, dodatkowo 50 pomyślnych replay. W tym historycznym odczycie 125 kandydatów, 31 challengerów, 5195 doświadczeń; **nie są to aktualne liczniki produkcyjne**. | Nie dublować Experience, promocji i skutków misji przy restartach, imporcie i retransmisji. |
| **Router V10 — Test 1/2/3** | Test 3: **600 przypadków**, 534 `REUSE_TOP1`, 66 `VERIFY_TOPK`, 100/100 znanych przypadków poprawnych, 57,61 s wobec 126,65 s pełnej ścieżki Test 2. Ograniczony test routingu, nie dowód całodobowej dostępności na VPS. | Zachować kontrakty trybów routingu i kanonicznego silnika mikrosieci; testować odtwarzalność decyzji. |
| **Naprawa i zamknięcie migracji mikrosieci** | Poprawiono błędną definicję PASS, zachowano pierwotne FAIL; **100/100** powtórzeń po naprawie oraz **20/20** restartów w zadanym zakresie; jeden kanoniczny silnik. | Nie tworzyć równoległego registry/engine ani nie przenosić starych błędnych reguł jako aktualnych. |
| **Desktop MicroSpace / Vision** | Kod i lokalne obserwacje Vision V5; zmiana obrazu **35,5461%**; nie jest to dowód semantycznego rozpoznania przycisku. | Klasyfikować zależne od GUI sterowanie jako `LOCAL_EXTENSION`, ewentualne API Vision jako `HYBRID`. |
| **Memorize / Notariusz lokalny V6** | Jedna lokalna podpisana obserwacja we wskazanym wyniku; w tym teście **0 nowych zatwierdzonych kompetencji pulpitu**. | Zachować pochodzenie, łańcuch dowodów i rozdział: podpis ≠ poprawność działania. |
| **Mission Navigator V9** | Misja badawcza **10/10 waypointów**, **24 podpisane zdarzenia**, offline, **0 akcji GUI, 0 modeli i 0 sieci**. | Przenieść plan/checkpointy i schemat dowodów, nie przypisywać pełnej autonomii GUI. |
| **GUI V9R1 / ręce Roberta** | Ostatni opisany preflight zatrzymał się na `STOP_NOT_DELL_ONLY` przed wykonaniem akcji; wcześniejsze warianty miały inne reguły ekranów. Pierwsza misja wysłania wiadomości nie ma potwierdzonego pełnego odbioru. | Fizyczny ekran, Wayland/PipeWire, klawiatura/mysz nie mogą blokować VPS; tylko wyraźnie uprawnione lokalne misje. |
| **RCC / Mission Control R10** | Przygotowane funkcje przeglądu, podglądu i lokalnych misji; historyczna aktywność RCC/API nie potwierdza przeniesienia na VPS. | Zachować historię, ACL, identyfikatory, sesje migracyjne i interfejs bez drugiego logowania po potwierdzonym SSO. |
| **Technology Radar** | Lokalny raport: **13/13 testów adaptera**, odczyt źródeł MAVSDK/Nav2/asyncua i **3 obserwacje**. To nie są trzy zakwalifikowane skille. | Rejestrować źródło, wersję, licencję, ocenę adaptera i status kwalifikacji. |
| **Szkolenie napraw z archiwum** | Katalogowanie, LEGO Decomposer, diagnoza, reprodukcja, poprawka, regresja, konsolidacja — **program rozwojowy**, brak dowodu ukończenia całości. | Oryginalne wielkie archiwum pozostaje prywatnie/lokalnie; na VPS wyłącznie aktywne, kwalifikowane minimum i indeksy. |
| **SCC/BLOCKS A27** | Deklaratywna notacja misji i testy **22 Python + 10 JS**; nie są dowodem generalnego wykonawcy języka ani ukończonej integracji z Robertem. | Zachować wersjonowane schematy celu i zgodność z organizacyjnym ID misji; brak cichej zmiany gramatyki. |
| **Luna Navigator / Radar / długa misja chat–ZIP–instalacja** | Uzgodniony upgrade z 15 października: **PLANNED / NOT DEPLOYED** w źródłowym raporcie. | Testy etapów: rozmowa → odpowiedź → odbiór artefaktu → instalacja → sprawdzenie → raport, z ochroną przed podwójnym efektem. |
| **Roberta integracja z SSI CODEX, Charlie i SSO** | Przygotowane kontrakty, adaptery i testy offline; pełna produkcyjna misja między trzema systemami nie jest dowiedziona samą paczką. | Odbiór na VPS obejmuje kanoniczne ID, autoryzację, round-trip, dowód wykonania, obsługę błędów i rollback. |
| **Modelowe szkolenia MICRO-13 (R7)** | 13 nowych kandydatów + 5 przyszłych rezerw; **0 zbudowanych i 0 uruchomionych** w opublikowanym statusie R7. | Osobna rola budowy na SSI MODELS i rola korzystania/ewidencji w Robercie, nigdy zamiast rdzenia misji. |

**Źródła historyczne:** [ciągłość Roberta](ROBERT_CANONICAL_CONTINUITY_VS_EXPERIMENTAL_RESET_20260906.md), [TEST 5](evidence/TEST5_FINAL_CONVERGENCE_20260903.md), [600x](evidence/ROBERT_IDEMPOTENCY_REPLAY_STRESS_600X_2026-08-31.md), [Router V10](evidence/ROBERT_V10_HYBRID_ROUTER_TEST3_20260901.md), [zamknięcie migracji mikrosieci](evidence/MICRONETWORK_MIGRATION_FINAL_LINEAGE_20260902.md), [Robert — desktop, Radar i trening napraw](ROBERT/README.md), [plan Luna/SCC](ROBERT/PLANNED_SCC_LUNA_NAVIGATOR_RADAR_UPGRADE_20261015.md), [SCC A27](SCC_BLOCKS_MISSION_LANGUAGE_AND_AMNEZJA3_ATTRIBUTION_20261014.md).

**Ważna granica:** wyniki S1–S40, siedmiu BODY, Zero Lab, świata piłki i innych laboratoriów są **osobnymi programami SSI**. Ich dane i skille nie stają się automatycznie osobistymi osiągnięciami Roberta. [Wyniki siedmiu BODY / S1–S10](RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md) zachowują swoją tożsamość, własne kryteria i historię.

## 9. Jak Robert korzysta z mikrosieci, kompozytów i pamięci

Docelowa ścieżka jest następująca:

```text
KONTEKST ORGANIZACJI / MISJA SCC / UPOWAŻNIENIA DYREKTORA
→ ROUTER V10: warunki, wersje, koszt, klasy SERVER_NATIVE/HYBRID/LOCAL_EXTENSION
→ KOMPETENCJE: kanoniczne mikrosieci i BLOCKS Pocket / META-BLOCKS
→ REUSE / VERIFY / FULL FLOW / NOWY KANDYDAT (według faktycznych bramek)
→ WYKONAWCA: ROBERT, CODEX lub inny jawnie uprawniony aktor
→ WERYFIKATOR I TEST: PASS / FAIL / INCONCLUSIVE
→ EVIDENCE + NOTARIUSZ + CONTINUUM
→ RESEARCH MEMORY / CEPA: doświadczenie wersjonowane i przypisane do aktora
→ CANDIDATE → CHALLENGER → CHAMPION (tylko przez istniejącą kwalifikację)
```

- Nie wolno utożsamiać **dostępnego wspólnego skilla** z **kompetencją osobiście nabytą przez Roberta**. Transfer zapisuje dawcę, odbiorcę, wersję, dowód, decyzję konsolidacji i test docelowego użycia.
- Champion jest przypisany do określonego zadania, przejścia, wersji i warunków; nie jest wykonawcą uniwersalnym. Pozostają dotychczasowe zasady promocji, bez nowego arbitralnego progu liczby zapytań.
- **BLOCKS Pocket, META-BLOCKS, LEGO Decomposer, mikro-sieci i kompozyty** mają własne schematy oraz walidatory. Dostępność katalogu nie dowodzi gotowości konkretnego adaptera ani pełnej ścieżki wykonania.
- **Research Memory P3A** zostało opisane jako zainstalowany czytnik kwalifikacji, ale automatyczny wybór native Champion przez Router V10 **nie był wtedy włączony**. Nie wolno podczas migracji traktować tej luki jako ukończonego połączenia. [Granice Research Memory](RESULTS/UNIVERSAL_LAB_RESEARCH_MEMORY_PROGRESS_20261009.md).
- Każde doświadczenie ma zachować projekt, właściciela/aktora, zadanie, źródłową wersję mikrosieci, wynik, porażki i naprawy, co najmniej referencję do dowodu oraz kontrolę idempotencji. Nie przepisujemy ani nie resetujemy historycznych checkpointów bez procedury odtworzenia.

## 10. Macierz aktorów — kto pozostaje odrębny po migracji

**Kontrola kompletności:** wszystkie niżej wymienione role muszą zostać odnalezione w prywatnej inwentaryzacji; wskazanie w publicznym planie **nie dowodzi** obecności ich uruchomionego kodu na którymkolwiek VPS. Nie każdy aktor jest procesem: część to osobne tożsamości, modele doradcze, laboratoria albo usługi wspólne.

| Aktor / komponent | Odpowiedzialność oraz granica uprawnień | Obowiązek migracyjny |
| --- | --- | --- |
| **Dyrektor SSI / Director Final** | Nadrzędne planowanie, delegowanie i zatwierdzanie misji, polityka dostępu i kosztów. | Serwer DIRECTOR jako centrum autoryzacji i kanonicznych ID, bez zależności od MSI. |
| **Dyrektor Charlie (R&D Director)** | Opracowuje i przydziela techniczne misje po konsultacji z Dyrektorem SSI; **nie jest sekretarką**. | Zachować osobną tożsamość, uprawnienia, historię delegacji i kontrakty. |
| **Sekretarka Charlie / Assistant Charlie** | Komunikacja, organizowanie materiałów i statusów, śledzenie pracy i przekazywanie wyników; brak samodzielnej zgody na GPU, wydanie czy zmianę ACL. | Zachować sesje w Universal Lab, dostęp zgodny z rolą, dialogi, kolejkę powiadomień i powiązania misji. |
| **SSI ROBERT** | Odrębny wykonawca techniczny: misje, Navigator, Playwright, Radar, pamięć i Evidence. | Własny VPS 24/7 z trwałą pamięcią operacyjną i niezależnością od NODE-01. |
| **SSI CODEX** | Niezależny wykonawca oprogramowania, testów i pakietów. | Serwerowy runtime i projekty z kontrolą dostępu; odbiór misji i wyników niezależny od Lenovo. |
| **BODY_FROZEN** | Osobny trwały runtime SSI Final i jego własna kwalifikacja kompetencji. | Zachować wersję/tożsamość; nie włączać bez decyzji jego prywatnej pamięci do Roberta. |
| **ISKRA1–ISKRA6 (sześć odrębnych agentów)** | Własne stany, badania i ścieżki kwalifikacji; nie jeden wspólny worker. | Sześć rejestrów własności, pamięci i dowodów; transfer wyłącznie po jawnej konsolidacji. |
| **CZARA / Shadow** | Niezależna, równoległa warstwa eksperymentów, propozycji i analiz. | Nie jest obowiązkową blokującą ścieżką misji Dyrektora; zachować rozdzielność wyników. |
| **Director_Czary** | Odrębny koordynator protokołów badawczych Czary. | Nie scalać z Dyrektorem SSI ani Dyrektorem Charlie. |
| **BODY_FROZEN_1.0** | Odrębny wykonawca w badawczej linii Czary. | Nie utożsamiać z BODY_FROZEN ani nie kopiować pamięci bez dowodu. |
| **Dodatkowa Luna: Navigator / Radar / prompty misji** | Planowany model wspomagający, inny niż kontekst Flow/Full Flow; **nie jest Dyrektorem ani weryfikatorem wyniku**. | Zachować status `PLANNED`, osobny budżet i test rzeczywistej integracji. |
| **JEV / modele System One (Tev1, D1)** | Ograniczone interfejsy decyzji i typowane propozycje; nie zastępują autoryzacji Routera/Dyrektora. | Zachować interfejsy i możliwość fallbacku bez utożsamiania modelu z aktorem zarządzającym. |
| **Hermes / nauczyciele, modele i kanały** | Zasoby laboratoriów i pomocy w misjach; źródło porównania lub przygotowania materiałów. | Dokumentować wersje i zakres dostępu; nie przenosić wszystkich nauczycieli jako obowiązkowego runtime Roberta. |
| **Universal Lab / Operations / SSI Navigator** | Interfejs i operacyjny rejestr misji, nie osobny decydent. | Jedno logowanie przez DIRECTOR, wspólny kontrakt i zachowane role użytkowników. |
| **Zero Lab / laboratoria domenowe** | Oddzielne środowiska badań i walidacji. | Udostępniane przez rejestr adapterów; offline nie zatrzymuje głównej misji. |
| **Router V10, mikrosieci, Research Memory, CEPA, CONTINUUM, Notariusz** | Wspólna infrastruktura wyboru kompetencji, pamięci, recovery i dowodów, a **nie kolejne osoby/aktorzy**. | Zachować kanoniczny registry, wersjonowanie, idempotencję i autorytet wyników. |

[Źródło rozdziału tożsamości i aktorów](SSI_V5_C4_ARCHITECTURE.md#container-ownership-and-separation) · [Zasady delegacji Charlie / Roberta](ROBERT/PLANNED_SCC_LUNA_NAVIGATOR_RADAR_UPGRADE_20261015.md#5-director-roles-and-task-delegation) · [Współpraca z ISKRA i laboratoriami](ROBERT/README.md#7-laboratories-iskra-agents-and-competence-flow).

## 11. Wymagany prywatny manifest ciągłości — bez publikowania danych

Przed przełączeniem z lokalnego środowiska na VPS należy sporządzić **w prywatnym SHARE** rozdzielny, rzeczywiście zmierzony katalog:

1. **RUNTIME:** nazwa, rola, faktyczna wersja i uruchomiona kopia, właściciel stanu, zależności, klasy zdolności, CPU/RAM/dysk, kontrola po restarcie.
2. **MISJE:** bieżące/pending, `mission_id`, `project_id`, etap, autoryzacja, kolejka, próby, idempotency key, powiązane skutki, checkpoint i reguła bezpiecznego wznowienia.
3. **SZKOLENIA / RESEARCH:** każda ukończona seria, wersja, kryteria, wynik, FAIL/INCONCLUSIVE, stan kwalifikacji, zachowany dowód i właściwy aktor.
4. **SKILLE / MIKROSIECI / KOMPOZYTY:** kanoniczne identyfikatory, wersje, źródło, Champion/Challenger/Candidate, własność, zależności od modelu i hosta, zgodność z Router V10/SCC, hash manifestu, migracja lub archiwum.
5. **PAMIĘĆ / DOWODY:** Research Memory, Memorize, CEPA, Notariusz, CONTINUUM, historia dialogów i historii napraw, łańcuch podpisów, zasady retencji, integralność snapshotu.
6. **AKTORZY:** odrębny namespace/tożsamość, uprawnienia, odbiorcy delegacji, nieprzeniesione historie i jawne, zatwierdzone transfery kompetencji.
7. **MOSTY:** Tailscale/SSH/API/Universal Lab/CODEX/Charlie — publicznie tylko kontrakt i wynik bramki; rzeczywiste endpointy i poświadczenia wyłącznie w sekretnym magazynie.
8. **MODELE:** weryfikowane lokalne tagi/digesty, architektura, licencja, przydział zasobów, status MICRO-13 R7, wersja planowana/built/deployed i zgodność z urządzeniem docelowym.
9. **PRÓBY ODTWORZENIA:** snapshot, suma, backup, próba przywrócenia, porównanie rekordów i sygnatur, plan rollback i brak blokady po wyłączeniu lokalnych komputerów.

**Warunek wyjścia z audytu:** dla każdej krytycznej pozycji wskazać `LIVE_VERIFIED` albo uzasadnione `BLOCKED/UNKNOWN`; nie ogłaszać ukończonej migracji na podstawie samych istniejących archiwów czy testów offline. **Nie przenosić danych klientów, profili sesji i sekretów do publicznego GitHuba.**

## 12. Odbiór ciągłości Roberta i wszystkich aktorów po przeniesieniu

| Test odbiorowy | Sprawdzany rezultat |
| --- | --- |
| **Tożsamość i memoria** | Po restarcie działa ten sam kanoniczny ROBERT, bez wyzerowania jego historiografii misji, skilli i dowodów. |
| **Mikrosieci i kwalifikacja** | Wyniki V10 / Candidate–Challenger–Champion są odczytywane, zgodne z wersją, bez nowych duplikatów; brak cichej aktywacji niekwalifikowanego skilla. |
| **Pełna misja end-to-end** | Dyrektor → delegacja Charlie/Robert → autoryzowany CODEX → wynik → weryfikacja → Evidence/Notariusz → status w Universal Lab. |
| **Jedno logowanie** | Panel Roberta i CODEX bez dodatkowego hasła po sprawdzonej delegacji; odwołanie ACL/logout blokują nowe operacje. |
| **Żadna rola nie jest połączona przez przypadek** | Osobne tożsamości Dyrektor SSI, Dyrektor Charlie, sekretarka Charlie, Robert, CODEX, BODY_FROZEN, ISKRA1–6 oraz CZARA-scope. |
| **Opcjonalny NODE-01** | Odłączenie lokalnego GUI wstrzymuje tylko wskazaną misję w `WAITING_FOR_NODE01`; pozostałe misje i VPS-y nadal działają. |
| **Playwright serwerowy** | Autoryzowana misja przeglądarkowa działa na VPS bez Waylanda, monitora i sesji użytkownika NODE-01. |
| **Recovery / Notariusz** | Brak podwójnej wysyłki/instalacji, poprawne checkpointy, ciągłość podpisów i uczciwe `INCONCLUSIVE`, gdy brak potwierdzenia efektu. |
| **Laboratoria i Shadow** | Niedostępność Czary/Zero Lab nie blokuje podstawowej ścieżki Dyrektora; wyniki badań nie stają się automatycznie wynikami produkcyjnymi. |
| **MICRO-13 R7** | Krytyczna usługa modeli nie jest przerywana przez konwersję; potencjalny brak zasobów to `RESOURCE_BLOCKED`, a Robert nadal ma własny priorytet misji. |

Nie są to testy już wykonane na VPS, lecz **konieczne warunki odbioru**. Dopóki prywatne raporty nie potwierdzają pełnego stanu, każda odpowiednia pozycja pozostaje `UNKNOWN` albo `PLANNED`.

---

**Powiązane publiczne dokumenty:** [Architektura C4](SSI_V5_C4_ARCHITECTURE.md) · [Robert — stan prac i ograniczenia dowodowe](ROBERT/README.md) · [Zasady publikacji i ochrony informacji](CONTRIBUTING.md).
