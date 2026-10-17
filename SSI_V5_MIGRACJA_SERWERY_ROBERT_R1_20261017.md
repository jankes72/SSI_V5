# SSI V5 — migracja na serwery 24/7 (R1: ROBERT jako pierwszy)

**Data ustalenia:** 17 października 2026 r.  
**Rodzaj dokumentu:** publiczny plan migracyjny i kryteria odbioru, bez instrukcji dostępowych.  
**Status:** PLAN / AUDYT W TOKU / BRAK POTWIERDZONEGO PRZEŁĄCZENIA PRODUKCYJNEGO.  
**Źródło architektury:** [kanoniczny model C4 SSI V5](SSI_V5_C4_ARCHITECTURE.md). Ten dokument nie zastępuje ani nie duplikuje diagramów C4.

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
| Rodzina lekkich modeli MICRO/NANO przygotowywana przez Roberta | Zatwierdzony zakres prac: odniesienie do 13 zgłoszonych wariantów na serwerze modeli; 13 propozycji lekkich rodzin i maksymalnie 26 zadań kandydackich MICRO/NANO. **Brak potwierdzenia, że modele zostały już zbudowane lub wdrożone.** |

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

### 1.6. DODATKOWE ZADANIE — SSI ROBERT jako budowniczy 13 lekkich modeli

**Decyzja z 17 października 2026 r. — zatwierdzony kierunek rozwoju, nie wynik wdrożenia.** Obok własnych misji Robert otrzymuje rolę **SSI Micro/Nano Model Builder**: przygotowuje lekkie modele do pracy offline i CPU oraz może udostępniać już zakwalifikowane warianty innym agentom SSI, ale wyłącznie gdy ma wolne zasoby.

- **Punkt wyjścia:** na osobnym serwerze inferencyjnym zgłoszono 13 wariantów modeli. Należy potwierdzić ich rzeczywiste identyfikatory, architekturę, licencje, źródła wag, sumy i dostępność bez zmiany działającej usługi.
- **Zakres planu:** przygotować **13 odpowiadających im lekkich wariantów bazowych / rodzin specjalistów**, z możliwością rozpatrzenia wersji `MICRO` i `NANO` dla każdej — **maksymalnie 26 kandydackich zadań**, nie 26 zagwarantowanych plików modeli. Część modeli źródłowych może nie nadawać się do lokalnej konwersji.
- **Dwie odrębne techniki:** kwantyzacja zmniejsza reprezentację wag, **nie liczbę parametrów**; zbudowanie nowego mniejszego specjalisty wymaga doboru małego modelu bazowego i ewentualnej odrębnej, dozwolonej adaptacji lub destylacji. Nie przedstawiamy kwantyzacji dużego modelu jako stworzenia nowego 1B–3B.
- **Miejsce budowania:** prace przygotowawcze i możliwe operacje CPU wykonuje **VPS ROBERT**, nie serwer obsługujący 13 modeli i nie serwer Dyrektora. Ciężkie checkpointy, brak RAM, brak zgodności formatu lub licencji oznaczają `BLOCKED_ON_ROBERT_RESOURCES`, a nie niejawne przekierowanie do płatnego GPU.
- **Produkcja:** istniejące 13 modeli na serwerze modeli pozostaje nietknięte. Tylko ukończone, sprawdzone i osobno zatwierdzone warianty mogą trafić do puli produkcyjnej; nie ma automatycznego awansu ani nadpisywania oryginałów.
- **Powiązanie ze skillami:** prywatna wiedza SSI nadal pozostaje w Research Memory, mikrosieciach, SCC i rejestrach kompetencji. Publiczny kontener z modelem nie jest nośnikiem prywatnej pamięci SSI.

Nie należy wnioskować z przygotowania narzędzi, że 13 nowych małych modeli już działa. Każdy wariant przechodzi etapy `PROPOSED` → `RESOURCE_CHECKED` → `BUILT` → `VALIDATED` → `APPROVED` → `DEPLOYED` → `LIVE_VERIFIED`, z dowodami dla każdego przejścia. Stan początkowy do potwierdzenia prywatnym audytem: `PROPOSED`.

### 1.7. SSI Adaptive Model Pool — wolne zasoby Roberta pracują dla całego SSI

**Priorytet zawsze mają misje Roberta i jego usługi krytyczne.** Udostępnianie lekkich modeli i przygotowywanie kolejnych wariantów to praca pomocnicza, dopuszczana wyłącznie przy zmierzonym zapasie CPU, RAM i dysku.

1. Router SSI z Dyrektorem sprawdza uprawnienia, klasę zadania, obciążenie i dostępność zakwalifikowanych modeli — lokalnych u Roberta, na serwerze modeli lub u innych zatwierdzonych dostawców.
2. Robert może uruchomić zabezpieczony, izolowany kontener/API małego modelu dla siebie lub Dyrektora tylko przy odpowiednim zapasie zasobów. Kontenery mają limity pamięci i CPU; pierwszeństwo misji Roberta może ograniczyć usługę pomocniczą lub przekierować ruch do innego zatwierdzonego modelu.
3. Nowe konwersje odbywają się **pojedynczo**, z kontrolą pamięci szczytowej, miejsca na dysku, licencji, kolejki i bez kosztownych wywołań modeli. Dla prac przekraczających dostępne zasoby obowiązuje bezpieczna blokada.
4. **Badanie odbywa się podczas rzeczywistej pracy SSI:** nie duplikujemy misji i nie generujemy osobnych płatnych zapytań dla benchmarku. Notariusz IT i Evidence zapisują identyfikator wersji/kwantyzacji, rodzaj zadania, udział mikrosieci, czas, koszty, wykorzystanie zasobów i zweryfikowany wynik.
5. **Notariusz zapisuje i weryfikuje fakty; Dyrektor i Router decydują** o zmianie modelu, eskalacji, fallbacku i późniejszej kalibracji. Niepewny wynik nie staje się automatycznie nową regułą routingu.
6. Utrata dostępności lekkiego modelu Roberta nie może zatrzymać misji innych agentów: Router stosuje dostępny zatwierdzony model lub jawny stan oczekiwania zgodny z uprawnieniami, bez powtarzania skutkowych operacji.

**Wymóg izolacji:** pakiet modeli pomocniczych jest zdegradowalny; usługi krytyczne VPS Roberta muszą działać bez niego. Raport pojemności zawiera osobno przestrzeń na źródła, wagowe artefakty próbne, pliki tymczasowe, kontenery, cache, rezerwy i pamięć operacyjną. Wielkości niezmierzone pozostają `UNKNOWN`.

Szczegóły uzgodnionego rozdziału obowiązków i granic testów opisano już publicznie w [Robert Builder / Model VPS R5](PUBLIC_MODELS/SSI_V5_ROBERT_BUILDER_MODEL_VPS_PRODUCTION_R5_20261017.md); nie przenosimy do GitHuba prywatnych narzędzi i konfiguracji.

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

Zadanie budowy lekkich modeli na VPS ROBERT dodaje osobne wymagania na dysk (źródła, pliki tymczasowe, warianty próbne, rollback) i chwilowe obciążenie CPU/RAM. Limitów nie wyznacza się na podstawie samej pamięci całkowitej VPS; punktem odniesienia jest wolny zapas **podczas zwykłych misji**. Plan nie rezerwuje z góry miejsca na wszystkie 26 kandydatów.

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
| R8 — Micro/Nano builder (zadanie dodatkowe) | Rozpoznanie 13 źródeł, dobór maks. 26 kandydatów, pojedyncze budowanie na wolnych zasobach ROBERT i stopniowe wdrażanie zaakceptowanych wariantów. | Pomiar realnego zapasu, zgodność licencji, test jakości, brak wpływu na rdzeń, odrębna zgoda na instalację i `LIVE_VERIFIED` dla każdej wersji. |

### Minimalny scenariusz akceptacyjny

Użytkownik loguje się raz do Universal Lab. Dyrektor zatwierdza misję i jej budżet. Robert przygotowuje materiał techniczny i dowody. CODEX otrzymuje zatwierdzone zadanie, wykonuje implementację i testy, zwraca wynik. Robert i Charlie raportują przebieg; Dyrektor zamyka misję po weryfikacji. Wylogowanie, zmiana uprawnień, utrata sieci i wyłączenie lokalnego węzła nie mogą otworzyć obejścia autoryzacji ani wywołać podwójnego wykonania.

## 7. Warunki bezpieczeństwa i publikacji

Ten dokument **nie stanowi zgody na migrację**, instalację, zmianę tras, restart, publikację kodu czy uruchomienie płatnych modeli. Weryfikacja na rzeczywistych serwerach wymaga odrębnego, kontrolowanego procesu. Stan `OFFLINE_TESTED` nigdy nie jest dowodem `LIVE_VERIFIED`.

Prywatne dokumenty wdrożeniowe mogą zawierać niezbędne adresy, tajne manifesty i konfiguracje dostępu, ale **nie wolno ich kopiować do publicznego GitHuba**.

---

**Powiązane publiczne dokumenty:** [Architektura C4](SSI_V5_C4_ARCHITECTURE.md) · [Robert — stan prac i ograniczenia dowodowe](ROBERT/README.md) · [Zasady publikacji i ochrony informacji](CONTRIBUTING.md).
