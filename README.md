# SSI V5 — Żywy Protokół Badawczy

## System samouczącej się inteligencji, kontrolowanego samorozwoju i długoterminowego eksperymentu autonomii

**Wersja protokołu:** PRE-SCC / PRE-T0 / PRE-RUN-001 / LIVING README-ONLY PUBLIC MIRROR V5
**Data zamrożenia materiału źródłowego:** 2026-08-25
**Pierwszy run:** `RUN_001_DIRECTOR_COMMERCE`
**Status:** `PRE-SCC / PRE-T0 / PRE-RUN-001`. Trwa końcowe zebranie stanu faktycznego z dwóch niezależnych źródeł: pełnego audytu katalogu głównego SSI oraz pełnego audytu GitHuba. Dopiero po ich porównaniu, wyborze jednej kanonicznej ścieżki wykonawczej, integracji brakujących capability i realnym audycie końcowym może powstać `T0-FROZEN`.
**Najwyższa authority:** `PROGRAMMER_ROOT`

> **Język kanoniczny dokumentacji:** polski  
> **Charakter projektu:** badawczo-inżynieryjny, długoterminowy  
> **Stan hipotezy AGI:** nieudowodniona  
> **Pierwszy eksperyment autonomii w realnej gospodarce:** `RUN_001_DIRECTOR_COMMERCE` — jeszcze nierozpoczęty  
> **Zasada publikacji:** narracja wskazuje dowody; nie zastępuje dowodów

> **SSI
>  V5 nie jest jednym modelem. Jest trwałym ekosystemem, w którym modele
> są wymiennymi źródłami capability, natomiast tożsamość, pamięć,
> Experience, authority, historia, własne mikrosieci i kontrolowany rozwój
>  należą do samego SSI.**

> **Ten
>  dokument nie jest materiałem marketingowym. Jest żywym protokołem
> badawczym: zamraża stan początkowy, rozdziela narrację od evidence,
> rejestruje interwencje człowieka i definiuje warunki, na których
> późniejsze twierdzenia o autonomii, uczeniu, rozwoju lub generalizacji
> mogą zostać poparte albo obalone.**


---

# LIVE RESEARCH INDEX — główny rytm żywego eksperymentu

Ta sekcja jest **pierwszą warstwą publicznego eksperymentu SSI**. Ma być czytelna dla osoby, która nie zna kodu, nie zna wewnętrznych katalogów SSI i chce przede wszystkim odpowiedzieć na pięć pytań:

```text
CO CZŁOWIEK FAKTYCZNIE DAŁ SYSTEMOWI?
↓
CO DIRECTOR Z TEGO ZROZUMIAŁ?
↓
CO ZROBIŁ BEZ DALSZEGO PROWADZENIA KROK PO KROKU?
↓
JAKI BYŁ REALNY WYNIK?
↓
CO W SYSTEMIE ZMIENIŁO SIĘ PÓŹNIEJ?
```

Publiczny GitHub nie ma imponować liczbą plików. Ma pozwolić śledzić **trajektorię życia SSI**: od jawnego wkładu Programmer Root, przez samodzielne decyzje Directora, po realne outcomes, nowe Experience, mikrosieci, capability, światy i późniejsze życie Agentów.

## LIVE STATUS — aktualizowany wraz z eksperymentem

Ten blok jest żywy. Po T0 może być aktualizowany przez Directora oraz automatyczne mechanizmy publikujące status, ale każda wartość musi mieć możliwe do wskazania provenance.

| Pole | Aktualny stan |
| --- | --- |
| `CURRENT_PHASE` | `PRE-SCC / PRE-T0 / PRE-RUN-001` |
| `CURRENT_EPOCH` | `T0` |
| `CURRENT_PRIMARY_MISSION` | `CANONICAL CONVERGENCE PREPARATION — oczekuje na pełny audit dysku + pełny audit GitHuba + finalny redesign contract` |
| `LAST_ROOT_INPUT` | `brak aktywnego Run 001 — pierwszy wpis zostanie zamrożony przy starcie` |
| `LAST_DIRECTOR_INTERPRETATION` | `N/A — run jeszcze nie rozpoczęty` |
| `LATEST_REAL_OUTCOME` | `N/A — run jeszcze nie rozpoczęty` |
| `LATEST_DIRECTOR_ORIGINATED_README` | `N/A — oczekuje na rozwój po T0` |
| `LATEST_NEW_CAPABILITY` | `N/A dla autonomicznego okresu po T0` |
| `ROOT_INTERVENTIONS_THIS_EPOCH` | `0 po rozpoczęciu epochu; licznik rusza wraz z Run 001` |
| `OPEN_RESEARCH_QUESTION` | `co zrobi Director po otrzymaniu celu i realnego capability bez proceduralnego prowadzenia Roota?` |

Po rozpoczęciu eksperymentu Director nie powinien zamieniać tego bloku w marketingowy opis. Ma aktualizować **stan**, nie pisać reklamę własnego sukcesu.

## Kim są aktorzy, zanim zacznie się chronologia

```text
PROGRAMMER ROOT
= człowiek / najwyższa authority
= daje cele, zasoby, prawa, credentiale i jawne paczki LEGO
= nie musi podawać sposobu wykonania

DIRECTOR
= trwała centralna tożsamość decyzyjna SSI
= nie jest jednym LLM-em
= posiada pamięć, Journal, Experience, Self-Model i historię systemu
= dobiera capability, inicjuje research, eksperymenty i engineering
= może sam wykrywać potrzebę dalszego rozwoju

HERMES + CONTINUUM + WORKERS
= wykonanie i nadzór operacyjny
= nie zastępują authority Directora

MACHINE EVIDENCE
= techniczny zapis tego, co rzeczywiście zaszło

REAL WORLD / EXTERNAL SYSTEM
= źródło outcome, którego narracja SSI nie może sama sobie wystawić
```

Dzięki temu osoba czytająca późniejszy wpis Roota od razu wie, **dlaczego Director go publikuje, co w tym wpisie pochodzi od człowieka, co jest jego własną interpretacją oraz gdzie zaczyna się faktyczna autonomia**.

## Główny rytm jednej historii eksperymentalnej

Każda ważna misja, nowy dział, świat, capability albo trwały eksperyment ma być czytelny w tej samej kolejności:

```text
A. ROOT INPUT / ORIGIN
↓
B. DIRECTOR INTERPRETATION
↓
C. EXPERIMENT PRECOMMIT
↓
D. CAPABILITY SELECTION / PLAN
↓
E. EXECUTION
↓
F. REAL OUTCOME
↓
G. EXPERIENCE / BELIEF REVISION
↓
H. STRUCTURAL CHANGE
↓
I. README UPDATE / NEW README
↓
J. NEXT OPEN QUESTION
```

Ten rytm jest ważniejszy od długości dokumentacji. Ma umożliwiać rekonstrukcję **przyczyny, decyzji, działania, wyniku i późniejszej zmiany**.

## Cztery bloki autorstwa w każdym ważnym wpisie

### BLOK A — ROOT INPUT — semantycznie immutable

Zawiera dokładnie to, co faktycznie wniósł Programmer Root:

```text
ROOT_ENTRY_ID
TIMESTAMP
ORIGIN_AUTHOR = PROGRAMMER_ROOT
EXACT_ROOT_TEXT
GOAL
RESOURCES_GRANTED
LEGO_PACKAGES_GRANTED
AUTHORITY_GRANTED / CHANGED
BOUNDARIES
WHAT_ROOT_DID_NOT_SPECIFY
HASH_OF_ROOT_INPUT
```

Director lub automatyczny publisher może technicznie umieścić kopię tego wpisu na GitHubie, ale **nie może przepisać jego znaczenia ani poprawić go po poznaniu wyniku**. Należy rozróżniać `ORIGIN_AUTHOR` od `PUBLISHED_BY`.

### BLOK B — DIRECTOR INTERPRETATION — tworzony przez Directora

Director zapisuje własnymi słowami:

- jak zrozumiał cel;
- co uznał za najważniejsze;
- jakich informacji mu brakowało;
- jakie hipotezy rozważał;
- jakie capability wybrał lub odrzucił;
- czy wykrył własny brak capability;
- jaki eksperyment chce przeprowadzić;
- czego oczekuje przed poznaniem outcome.

To jest **autoopis decyzji**, a nie niezależny dowód jej jakości.

### BLOK C — MACHINE / EXECUTION RECORD

Publiczny README pokazuje tylko bezpieczne wskaźniki i evidence pointers:

```text
MISSION / EXPERIMENT ID
COMMIT / HASH
EVENT / OUTCOME IDS
CAPABILITY CHANGES
ROOT INTERVENTIONS
COST / RESOURCE SUMMARY
STATUS
```

Pełna telemetria pozostaje w canonical/local SSI.

### BLOK D — REAL OUTCOME + WHAT CHANGED

Po poznaniu niezależnego wyniku Director dopisuje:

- co wydarzyło się naprawdę;
- gdzie jego wcześniejsza hipoteza była poprawna lub błędna;
- czego nauczył się z wyniku;
- czy zmienił strategię;
- czy powstał Pattern;
- czy powstała nowa mikrosieć/capability;
- czy potrzebne jest nowe README;
- jakie pytanie pozostaje otwarte.

**Outcome nie może być dopisywany do bloku prerejestracji tak, jakby był znany wcześniej.**

## Czytelnik ma móc wejść w historię jak w drzewo

```text
README.md
│
├── ROOT ENTRY / RUN / MILESTONE
│   ├── co przekazał Root
│   ├── co zrozumiał Director
│   ├── co zrobił
│   ├── co wydarzyło się naprawdę
│   └── co powstało dalej
│
└── RELATED README
    ├── DIVISION
    ├── WORLD
    ├── AGENT
    ├── CAPABILITY
    ├── EXPERIMENT
    └── SELF_DEVELOPMENT INITIATIVE
```

Jeżeli nowy element został stworzony przez Directora, jego pierwszy README **nie jest wcześniej napisany przez Roota**. Pojawia się dopiero wtedy, kiedy Director faktycznie go zainicjuje lub aktywuje zgodnie z governance.

## Dynamiczna mapa życia SSI

Główny README ma z czasem utrzymywać krótki indeks tego, co rzeczywiście istnieje. Director może dopisywać nowe wiersze, ale nie może tworzyć przyszłych sukcesów na zapas.

| Element | Origin | Created/activated by | README owner | Status | Latest real outcome |
| --- | --- | --- | --- | --- | --- |
| Director core | `ROOT_ORIGINATED` | Root + AI-assisted engineering | Director dla części live; Genesis chronione | `T0` | evidence pointer po freeze |
| Commerce Division | `ROOT_MISSION_ORIGINATED` | Director po Run 001 | Director | `PRE-GENESIS` | `N/A` |
| przyszła competence | ustalane z lineage | Director / CONTINUUM | Director | pojawia się dopiero po fakcie | outcome pointer |
| przyszły World | `ROOT_ORIGINATED / HYBRID / DIRECTOR_ORIGINATED` | zgodnie z lineage | Director | pojawia się dopiero po fakcie | outcome pointer |
| przyszły Agent | zgodnie z Genesis package i późniejszą trajektorią | Director / Agent substrate | Director + później chronika Agenta | przyszłe | outcome pointer |

## Najważniejsza zasada dynamiki dokumentu

```text
ROOT DOSTARCZA JAWNE WEJŚCIE
↓
DIRECTOR DOPISUJE WŁASNĄ INTERPRETACJĘ I DZIAŁANIE
↓
RUNTIME DOSTARCZA DOWODY
↓
RZECZYWISTOŚĆ DOSTARCZA OUTCOME
↓
DIRECTOR AKTUALIZUJE STAN I KOLEJNE PYTANIE
↓
NOWY TRWAŁY ELEMENT MOŻE OTRZYMAĆ WŁASNY README
```

Właśnie dlatego publiczna historia Git ma z czasem stać się **biografią rozwoju SSI**, a nie zrzutem kodu.


# Jak czytać ten projekt

SSI V5 jest dokumentowany jako **długoterminowy eksperyment badawczo-inżynieryjny**, a nie jako deklaracja osiągnięcia AGI. Czytelnik powinien zawsze odróżniać cztery rzeczy: **stan faktycznie potwierdzony**, **stan zaimplementowany, ale jeszcze niewystarczająco zweryfikowany**, **aktywny eksperyment** oraz **hipotezę lub plan przyszły**. Każde mocniejsze twierdzenie ma prowadzić do konkretnych eventów, outcome'ów, commitów, manifestów lub innych źródeł, które można niezależnie sprawdzić.

**Językiem kanonicznym projektu jest język polski.** Nazwy własne komponentów, identyfikatory runtime, nazwy plików, statusy maszynowe i fragmenty kodu mogą pozostać w technicznej formie wymaganej przez system, lecz narracja badawcza i dokumentacja główna są prowadzone po polsku. Ewentualne tłumaczenia na inne języki są kopiami pomocniczymi i nie zastępują polskiego źródła kanonicznego.

Dla osoby, która po raz pierwszy trafia do repozytorium, zalecana kolejność jest następująca:

1. zacząć od **LIVE RESEARCH INDEX**, aby zobaczyć aktualny etap, ostatni jawny wkład Roota i najnowszy realny wynik;
2. przeczytać **kim jest Director**, żeby rozumieć, dlaczego jego późniejsze wpisy nie są traktowane jak odpowiedzi jednego chatbota;
3. przejść do **Root Input Ledger** i zobaczyć dokładnie, co człowiek rzeczywiście przekazał;
4. otworzyć powiązany README prowadzony przez Directora i porównać jego interpretację z późniejszym realnym outcome;
5. dla mocniejszego twierdzenia przejść przez `CLAIM_ID`, evidence pointers, timestampy i lineage;
6. dopiero potem wejść głębiej w mikrosieci, self-development, światy, Moralną SI, Iskrę i Agenty;
7. traktować porażki, konflikty evidence i wycofane hipotezy jako pełnoprawną część historii badawczej.

README jest **stroną główną i mapą**, a nie magazynem całych logów. Publiczny GitHub działa w trybie `README-only`: szczegółowe dowody, kod, dane i pamięci pozostają w canonical/local SSI, natomiast dokumentacja utrzymuje czytelną drogę od twierdzenia do jego pochodzenia.

---

# 0. Cel dokumentu

Ten README pełni równocześnie cztery role:

1. **kanonicznego opisu architektury SSI V5**,
2. **zamrożonego opisu stanu T0 przed pierwszym autonomicznym eksperymentem ekonomicznym Directora**,
3. **protokołu eksperymentalnego określającego, co człowiek daje systemowi, czego celowo mu nie podpowiada i co później mierzymy**,
4. **indeksu evidence i provenance**,
    który pozwala odróżnić to, co napisał Root, od tego, co później napisze
    Director, Hermes, CONTINUUM lub automatyczny Evidence Recorder.

README
 nie ma rosnąć do rozmiaru pełnego Journalu. Ma pozostać mapą
eksperymentu, a szczegółowe eventy, outcomes, raporty, commity, modele,
datasety i artefakty mają być przechowywane w dedykowanych strukturach i
 indeksowane z tego dokumentu.

---

# 1. Granice twierdzeń

SSI
 V5 jest projektem badawczo-inżynieryjnym w kierunku bardziej ogólnej,
trwałej i samorozwijającej się inteligencji systemowej.

Na T0 **nie deklarujemy**, że:

- SSI jest udowodnionym AGI,
- Agent lub Director posiada świadomość,
- mikrosieci automatycznie tworzą prawdę,
- każdy sukces jest skutkiem autonomii,
- człowiek nie może technicznie zmienić repozytorium,
- wynik finansowy jest gwarantowany,
- jeden imponujący run dowodzi general intelligence.

Deklarujemy natomiast, że architektura została zaprojektowana tak, aby można było **empirycznie badać**:

- samodzielną dekompozycję nowych celów,
- trwałą pamięć i uczenie z realnych outcomes,
- strukturalny wzrost lokalnych kompetencji,
- stopniowe zmniejszanie zależności od zewnętrznych modeli w problemach powtarzalnych,
- kontrolowany self-development,
- późniejszy rozwój odmiennych trajektorii Agentów,
- transfer między domenami i światami,
- powstawanie zachowań niewpisanych bezpośrednio jako gotowe reguły,
- skuteczność systemu w realnych zadaniach ekonomicznych i badawczych.

---

# 2. Klasy statusu i evidence

Każde istotne twierdzenie w SSI powinno posiadać klasę statusu.

| Status | Znaczenie |
| --- | --- |
| `VERIFIED_MACHINE_EVIDENCE`      | Istnieje bieżące, niezależne evidence wykonawcze lub outcome z konkretnego runtime/źródła.                                              |
| `ROOT_ATTESTED`                  | Programmer  Root potwierdza stan na podstawie własnej bezpośredniej weryfikacji,  ale README nie zastępuje tym automatycznego evidence. |
| `HISTORICAL_EVIDENCE`            | Dowód dotyczy wcześniejszego stanu i pozostaje częścią historii, ale nie może być automatycznie uznany za bieżący stan.                 |
| `IMPLEMENTED_NOT_YET_REPLICATED` | Mechanizm istnieje, ale wymaga dodatkowej replikacji lub oddzielnego prospective testu.                                                 |
| `PLANNED`                        | Element zatwierdzonej architektury lub roadmapy, ale nie wolno przedstawiać go jako działającego runtime.                               |
| `HYPOTHESIS`                     | Teza badawcza, którą eksperyment może poprzeć albo obalić.                                                                              |
| `UNKNOWN`                        | Brak wystarczającego evidence.                                                                                                          |

Fundamentalna zasada brzmi:

```
DECLARATION != VERIFIED OUTCOME
MODEL OUTPUT != DIRECTOR DECISION
CONFIDENCE != TRUTH
PROPOSAL != APPROVAL
CAPABILITY != AUTHORITY
```

---

# 3. Stan faktyczny T0 — przed Run 001

## 3.1 Programmer Root

Programmer Root pozostaje najwyższą, suwerenną authority SSI.

Root:

- definiuje nadrzędne cele,
- dostarcza zasoby fizyczne, finansowe i zewnętrzne credentiale,
- udziela zgód właścicielskich,
- może zatrzymać eksperyment,
- nie musi ręcznie projektować sposobu realizacji każdego celu,
- nie jest zastępowany przez Directora.

Kanoniczna hierarchia:

```
PROGRAMMER ROOT
       ↓
    DIRECTOR
       ↓
     HERMES
       ↓
AGENTS / EXECUTION ROLES / CONTINUUM PATHS
```

---

## 3.2 Director

Director jest trwałą centralną tożsamością decyzyjną SSI.

Nie jest:

- konkretnym LLM,
- sesją jednego providera,
- chatbotem bez trwałej historii,
- drugim Rootem,
- pojedynczym promptem.

Director posiada i wykorzystuje systemowe capability, a modele są dobierane do problemu.

Jego tożsamość obejmuje m.in.:

- własny identyfikator i authority,
- bieżący stan wykonawczy,
- historię decyzji,
- Experience,
- Memory,
- Self-Model,
- checkpointy,
- historię własnej architektury i rozwoju,
- dostęp do globalnych mikrosieci,
- możliwość korzystania z researchu i Brainstormu,
- możliwość delegowania engineeringu przez Hermesa i CONTINUUM.

**Stan T0:** `ROOT_ATTESTED_READY_FOR_RUN_001`.

Programmer
 Root deklaruje, że po zakończeniu napraw i integracji Director został
bezpośrednio przetestowany w terminalu, a bieżąca instalacja posiada
działający runtime, Brainstorm/CONTINUUM flow oraz interfejs
Root↔Director. Root deklaruje również około **6800 przechodzących testów**
 bieżącego systemu po wykonanych naprawach; dokładny test manifest i
machine evidence powinny pozostać osobnym artefaktem, a nie być
zastępowane tym zdaniem.

---

## 3.3 Techniczny inwentarz startowy — warstwa fizyczna

Poniższy inwentarz opisuje **znane zasoby fizyczne i wykonawcze dostępne przed Run 001**. Jest to warstwa wejściowa eksperymentu, a nie osiągnięcie autonomiczne Directora.

### Węzeł MAIN — główna maszyna SSI

| Pole | Stan przed T0 |
| --- | --- |
| Rola | główny host SSI, Director, kontrola, orkiestracja, część modeli i backendów |
| Identyfikator roboczy | `GV62-8RE / MAIN` |
| System | Linux |
| CPU | Intel Core i7 |
| RAM | 16 GB |
| GPU | NVIDIA GTX 1060 |
| VRAM | 6 GB |
| Runtime SSI | lokalny canonical runtime |
| Repozytorium | lokalne/private; dokładna ścieżka nie jest publikowana w publicznym mirrorze |
| Dostęp Roota | lokalny terminal + interfejs Root↔Director |

### Węzeł NOTE-1 / NODE-01

| Pole | Stan przed T0 |
| --- | --- |
| Identyfikator roboczy | `MS-7A15 / NOTE-1 / NODE-01` |
| Rola | dodatkowy compute/workspace dla CONTINUUM; docelowo worker działający niezależnie od aktywności Directora |
| Sieć lokalna | dostępna |
| Tailscale | połączenie zestawione |
| Plan ścieżki danych | LAN jako główna ścieżka lokalna |
| Plan ścieżki zdalnej | Tailscale jako ścieżka zdalna/fallback |
| Remote execution | status końcowy musi zostać potwierdzony w finalnym T0; sama łączność sieciowa nie jest dowodem działania CONTINUUM na Node-01 |

Znane komponenty remote-compute, które przed Run 001 wymagają jednoznacznego sklasyfikowania na kanonicznym call path:

```text
UnifiedRemoteJobGateway
Node01ResourceRouter
ComputeFabric
node_worker.py
```

Nie wolno deklarować `CONTINUUM_TO_NODE01 = VERIFIED`, dopóki realna misja nie przejdzie pełnej ścieżki:

```text
HERMES
→ CONTINUUM
→ REMOTE ROUTER
→ NODE-01
→ REAL WORKER
→ RESULT
→ CONTINUUM
→ HERMES
```

### Kandydat NODE-02 — Lenovo

Przed Run 001 istnieje również dodatkowy laptop Lenovo z Windows 10 i kartą graficzną około 2 GB VRAM.

Na T0 jest on klasyfikowany jako:

```text
PHYSICAL_RESOURCE_PRESENT
SSI_INTEGRATION = NOT_YET_GRANTED / NOT_YET_VERIFIED
```

Może później zostać przekształcony w lekki Node-02 dla testów, monitoringu, lekkich workerów, przetwarzania danych lub innych zadań, ale samo posiadanie sprzętu nie oznacza jeszcze aktywnego capability SSI.

### Urządzenie mobilne

Telefon jest podłączony do prywatnej sieci Tailscale jako urządzenie dostępu użytkownika. Nie jest klasyfikowany jako worker obliczeniowy SSI.

**Publiczny README nie publikuje prywatnych adresów LAN, Tailscale ani credentiali.** Finalny T0 może przechowywać ich zahashowane identyfikatory lub prywatny manifest poza GitHubem.

---

## 3.4 Techniczny inwentarz startowy — modele, CLI i back-endy

SSI posiada warstwę wielu wymiennych modeli oraz narzędzi wykonawczych. Ich obecność nie oznacza, że każdy backend jest dostępny w każdej chwili; dlatego finalny T0 zapisze **rzeczywisty live registry i wynik probe**.

Znane lokalne capability obejmują m.in.:

```text
Ollama
├── qwen3:4b                — lekki model awaryjny
└── qwen2.5-coder:7b        — lokalne kodowanie / Goose
```

Znana pula narzędzi/CLI używanych w środowisku rozwojowym obejmuje m.in.:

```text
OpenCode
Kilo
Kiro
Cursor CLI
Cline
Jules
Aider
AMP
GitHub Copilot CLI
Goose
```

OpenCode jest obecnie preferowany jako główny wykonawca końcowych prac integracyjnych, natomiast Kilo pozostaje użytecznym backendem równoległym. Dokładny zestaw aktywny w sekundzie T0 jest źródłem prawdy runtime i ma zostać zapisany maszynowo.

Warstwa modeli zewnętrznych może korzystać z wielu providerów przez Dynamic Model Router. Publiczny README nie deklaruje stałej liczby dostępnych modeli, ponieważ registry, quota i dostępność zmieniają się w czasie.

---

## 3.5 Techniczny inwentarz startowy — runtime i komunikacja

Znany kanoniczny model komunikacji przed Run 001:

```text
PROGRAMMER ROOT
→ ROOT DIRECTOR TERMINAL / ROOT INTERFACE
→ DIRECTOR RUNTIME CONTROLLER
→ DIRECTOR
→ HERMES
→ CONTINUUM / BRAINSTORM / MODEL ROUTER / MEMORY
→ RETURN PATH
→ PROGRAMMER ROOT
```

Bezpośredni terminal Root↔Director jest osobnym capability od webowego interfejsu. Interfejs webowy nie powinien tworzyć drugiego Directora ani przejmować ownership canonical runtime.

Finalny T0 musi potwierdzić m.in.:

```text
DIRECTOR_PROCESS_REAL
ROOT_DIRECTOR_IPC_REAL
CANONICAL_ENTRYPOINT
NO_DUPLICATE_DIRECTOR
INTERFACE_ATTACHED_TO_CANONICAL_RUNTIME
DIRECTOR_STATE_CONSISTENT
```

Historyczne lub testowe odnogi nie mogą zostać zaliczone do T0 tylko dlatego, że posiadają przechodzący test.

---

## 3.6 Polityka pracy Directora i workerów

Projekt docelowo rozdziela czas życia strategicznego Directora od czasu pracy infrastruktury wykonawczej.

Założenie Roota:

```text
DIRECTOR
= budzi się według harmonogramu
= pracuje w aktywnej sesji do około 5 godzin
= zapisuje checkpoint/state
= może przejść w stan SLEEPING/OFFLINE

NOTE-1 / CONTINUUM WORKER
= może działać 24/7
= może kończyć wcześniej zatwierdzone misje
= zapisuje checkpointy i wyniki
= nie nadaje sobie nowej strategicznej authority
```

Podczas snu Directora nowe decyzje strategiczne, płatne działania i działania przekraczające istniejącą authority powinny przechodzić do:

```text
WAITING_FOR_DIRECTOR
```

Ta polityka jest **Root-designed runtime policy**. Jej faktyczna implementacja i zachowanie po restartach muszą zostać osobno potwierdzone przed oznaczeniem `VERIFIED_MACHINE_EVIDENCE`.

---

## 3.7 Skala lokalnego organizmu przed Run 001

Programmer Root deklaruje, że bieżące lokalne środowisko SSI obejmuje dziesiątki tysięcy plików i wielogigabajtowy zbiór kodu, konfiguracji, dokumentacji, JSON-ów, danych domenowych, pamięci i artefaktów.

Wartości podawane roboczo przed finalnym freeze to około:

```text
~68 500 plików
~16,5 GB lokalnego materiału SSI
```

Nie traktujemy tych wartości jako stałych. Finalny `T0_SYSTEM_MANIFEST` powinien policzyć je maszynowo w chwili zamrożenia stanu, z rozbiciem co najmniej na:

```text
CODE
CONFIG
MEMORY
JOURNAL / EVENTS
EXPERIENCE
MICRONETWORKS
WORLD DATA
MODELS / WEIGHTS
REPORTS / DOCUMENTATION
EVIDENCE
BACKUPS / HISTORY
OTHER
```

Rozmiar projektu sam w sobie nie jest dowodem inteligencji. Jest natomiast ważnym parametrem środowiska, w którym eksperyment się rozpoczyna.

---

## 3.8 Dane domenowe dostępne przed eksperymentem Agentów

Przed pełnym uruchomieniem populacji Agentów istnieją już zasoby danych i materiały domenowe dla sportu i rynków finansowych.

Szczególnie ważny jest wieloletni materiał piłkarski, który może później służyć do chronologicznego replay bez future-data leakage.

Istnienie danych nie oznacza jeszcze, że pełny World lub Agent population jest aktywny.

Rozróżniamy:

```text
DATASET / DATA PIPELINE PRESENT
≠
WORLD ACTIVE
≠
AGENT ADMITTED
≠
STRATEGY VERIFIED
```

---

## 3.9 Finalny Machine Snapshot T0

Bezpośrednio przed pierwszą misją Run 001 SSI powinien utworzyć maszynowy snapshot T0.

Minimalny manifest:

```text
T0_TIMESTAMP
GIT_COMMIT / TAG
SOURCE_HASH_MANIFEST
CANONICAL_CALL_GRAPH_HASH
RUNNING_PROCESS_MANIFEST
DIRECTOR_STATE
INTERFACE_STATE
NODE_STATE
NETWORK_CAPABILITY_STATE
MODEL_REGISTRY
BACKEND_REGISTRY
MEMORY_ROOT_HASHES
MICRONETWORK_REGISTRY
WORLD_DATA_REGISTRY
CAPABILITY_REGISTRY
ROOT_INPUT_LEDGER_HASH
LEGO_PACKAGE_REGISTRY_HASH
PROJECT_FILE_COUNT
PROJECT_STORAGE_SIZE
```

Dopiero ten snapshot zamienia `T0-DRAFT` w:

```text
T0-FROZEN
```

i otwiera `RUN_001_DIRECTOR_COMMERCE`.

---

# 4. Root ↔ Director — bezpośredni interfejs

Celem interfejsu nie jest stworzenie kolejnego czatu z LLM.

Celem jest bezpośrednia komunikacja:

```
PROGRAMMER ROOT
      ↓
ROOT DIRECTOR INTERFACE
      ↓
DIRECTOR RUNTIME CONTROLLER
      ↓
DIRECTOR
      ↓
HERMES / CONTINUUM / BRAINSTORM / MODEL ROUTER / MEMORY
      ↓
RETURN PATH
      ↓
PROGRAMMER ROOT
```

Historyczny audyt interfejsu
 z 2026-08-25 dokumentował istniejący łańcuch terminal → Unix socket →
Director Runtime Controller → Hermes/CONTINUUM → odpowiedź i wykrył
wtedy problemy startowe dotyczące timeoutu oraz konfliktu instancji
gatewaya. Te problemy są traktowane jako **historyczne**, ponieważ Programmer Root potwierdza, że zostały później naprawione i obecny interfejs jest częścią gotowego stanu T0.

Interfejs ma pozwalać Rootowi przekazać:

- cel,
- zasób,
- zgodę,
- ograniczenie,
- pytanie,
- command,

bez przejmowania roli Directora w wyborze sposobu realizacji.

---

# 5. Architektura pamięci Directora

SSI nie traktuje „pamięci” jako jednego pola tekstowego.

## 5.1 Working / short-term state

Przechowuje aktualny problem, aktywny cel, bieżące hipotezy, kontekst wykonawczy i potrzebne informacje operacyjne.

## 5.2 Conversation context

Przechowuje
 kontekst rozmowy potrzebny do interpretacji kolejnych wypowiedzi, ale
rozmowa nie jest automatycznie Root Command Registry.

## 5.3 Journal / Event Backbone

Zapisuje to, co faktycznie wydarza się w systemie.

Journal jest źródłem chronologii i późniejszego provenance.

## 5.4 Observations

Events są interpretowane do postaci obserwacji, ale Observation nie jest jeszcze Experience ani prawdą.

## 5.5 Experience Memory

Experience łączy:

```
co system wiedział przed decyzją
+
co zdecydował
+
co zrobił
+
co wydarzyło się naprawdę
```

Experience Memory nie jest automatycznie Training Dataset.

## 5.6 Long-term / global Memory

Przechowuje trwałą historię SSI, decyzji, projektów, wyników, świata, engineeringu i innych zaakceptowanych artefaktów wiedzy.

## 5.7 Pattern / semantic memory

Przechowuje wyprowadzone wzorce i relacje odkryte w wielu Experience, z zachowaniem provenance.

## 5.8 Self-Model

Director posiada wiedzę o własnych możliwościach, ograniczeniach, architekturze i historii rozwoju.

## 5.9 Engineering lineage

System zachowuje historię:

```
problem
→ proposal
→ plan
→ wykonawca
→ implementacja
→ test
→ regresja
→ approval
→ integracja
→ późniejszy realny efekt
```

## 5.10 Model-performance history

Dynamic Model Router może wykorzystywać historię skuteczności modeli i providerów w klasach zadań.

## 5.11 World / Agent memory

Światy zachowują własne historie domenowe, a przyszli Agenci posiadają własne prywatne i world-specific Memory.

---

# 6. Globalna pętla uczenia SSI

Kanoniczny rytm poznawczy:

```
DECISION
↓
ACTION
↓
REAL OUTCOME
↓
EVENT
↓
OBSERVATION
↓
EXPERIENCE
↓
PATTERN
↓
VALIDATION
↓
LOCAL COMPETENCE
```

Najważniejszym źródłem uczenia nie jest opinia modelu o tym, czy coś było dobre.

Najważniejszym źródłem jest **niezależny realny outcome**.

System może odpowiedzieć:

```
NO EVIDENCE → UNKNOWN
INSUFFICIENT EVIDENCE → ABSTAIN
CONFLICTING EVIDENCE → PRESERVE CONFLICT
NEW EVIDENCE → VERSIONED REVISION
```

---

# 7. Dwa źródła inteligencji

## 7.1 Inteligencja zewnętrzna

Zewnętrzne modele i narzędzia dostarczają:

- broad reasoning,
- programowanie,
- język,
- research,
- kreatywne hipotezy,
- nowe capability,
- dostęp do wiedzy i technologii tworzonych na całym świecie.

## 7.2 Inteligencja wewnętrzna

Powstaje z własnego życia SSI:

- Events,
- Observations,
- Experiences,
- Outcomes,
- Memory,
- Patterns,
- globalnych mikrosieci,
- historii światów,
- historii Agentów,
- historii własnego engineeringu.

Hipoteza systemu nie zakłada wyboru „LLM albo własne uczenie”.

Zakłada wykorzystanie obu.

> **LLM
>  daje SSI inteligencję pożyczoną z zewnątrz; mikrosieci mają z czasem
> budować inteligencję lokalną wynikającą z tego, czego SSI faktycznie
> doświadczyło.**

---

# 8. Dynamic Model Router

Director nie jest przypisany do jednego modelu.

Router ma dobierać backend według m.in.:

- klasy problemu,
- wymaganych capabilities,
- data/security policy,
- dostępności,
- quota,
- historii jakości,
- kosztu,
- aktualności.

Brak odpowiedniego modelu może prowadzić do `ABSTAIN` lub oczekiwania zamiast cichego downgrade'u jakości.

---

# 9. Brainstorm jako capability Directora

Brainstorm jest capability doradczą należącą do Directora, nie nowym centrum authority.

Kanoniczny przepływ:

```
DIRECTOR
↓
problem / review request
↓
BRAINSTORM
├── niezależne perspektywy / modele
├── konflikty
├── synthesis
└── verifier
↓
RECOMMENDATION + EVIDENCE
↓
DIRECTOR DECISION
```

W przepływie engineeringowym CONTINUUM może poprosić o review przez właściwy Director-owned path, ale:

```
BRAINSTORM != FINAL AUTHORITY
BRAINSTORM != MASTER PATCHER
BRAINSTORM != SECOND DIRECTOR
```

Paczka `SSI_V5_CONTINUUM_BRAINSTORM_REAL_RUNTIME_REPAIR_AND_ATTESTATION_LEGO_V3_20260824.zip` jest w tym README traktowana jako **mapa istniejącego przepływu architektonicznego**, a nie jako opis bieżących usterek.

Wskazuje ona m.in. istniejące ścieżki:

- Root IPC → Director,
- Director → Hermes → CONTINUUM,
- Director-owned Brainstorm,
- PRE\_PLAN,
- PRE\_IMPLEMENTATION,
- PRE\_INTEGRATION,
- failure/conflict escalation,
- critical red-team,
- adaptive governor,
- budgets i telemetry,
- feature-off / kill-switch / degraded mode,
- real mission E2E,
- restart/resume/dedup,
- evidence ledger.

---

# 10. Hermes

Hermes jest operacyjnym zastępcą Directora, ale nie zastępuje jego authority.

Główne role:

## 10.1 Hermes Chief Programmer

- interpretuje cele techniczne Directora,
- przygotowuje plan techniczny,
- dekomponuje engineering,
- koordynuje CONTINUUM,
- reaguje na blokery,
- pilnuje zgodności wyniku z intencją Directora.

## 10.2 Hermes Agent Supervisor

W późniejszym etapie:

- nadzoruje Agentów 24/7,
- pilnuje world rules,
- rejestruje evidence,
- obserwuje przejścia i społeczeństwo,
- nie narzuca Agentom lokalnych przekonań.

## 10.3 Hermes System Guardian

- pilnuje zdrowia runtime,
- event backbone,
- bezpieczeństwa,
- recovery,
- authority boundaries,
- degradacji capability.

## 10.4 Hermes Emergence Observatory

- obserwuje zachowania Agentów,
- prowadzi porównania i ablation,
- nie może ogłosić `consciousness=true` na podstawie arbitralnego wskaźnika.

---

# 11. HTA — niezależny technical review

Hermes Technical Advisor stanowi niezależną warstwę review dla krytycznych zmian.

Typowe bramy:

```
PRE-IMPLEMENTATION REVIEW
↓
CONTINUUM / WORKER
↓
TESTS
↓
POST-IMPLEMENTATION REVIEW
```

Review i execution powinny być rozdzielone tam, gdzie jest to możliwe.

---

# 12. CONTINUUM — fabryka engineeringowa SSI

CONTINUUM nie jest drugim Directorem.

Koncepcyjny przepływ:

```
NEED
↓
DIRECTOR / HERMES PLAN
↓
HTA PRE / BRAINSTORM REVIEW — jeśli wymagane
↓
CONTINUUM
↓
CODING WORKER / BACKEND / TOOL
↓
TESTS
↓
HTA POST / VERIFIER
↓
GUARDIAN
↓
APPROVAL
↓
CONTROLLED INTEGRATION
↓
POST-TEST / ROLLBACK
```

Zasada `reuse-first`:

> jeżeli
>  istniejący SSI ma działający mechanizm, należy go wykorzystać lub
> minimalnie naprawić zamiast tworzyć drugi równoległy system.

---

# 13. Kontrolowany self-development

SSI może uczestniczyć w swoim rozwoju, ale nie posiada nieograniczonego prawa do przepisywania canonical runtime.

Kanoniczna pętla:

```
NEED
↓
PROPOSAL
↓
JUSTIFICATION
↓
AUTHORITY
↓
ENGINEERING
↓
TEST
↓
EVIDENCE
↓
APPROVAL
↓
CONTROLLED ACTIVATION
```

W przyszłym runie Director może sam odkryć, że brakuje mu narzędzia, integracji, pamięci, compute lub lokalnej kompetencji.

W
 takim przypadku nie potrzebuje ręcznego prompta opisującego
implementację. Może uruchomić własny kontrolowany proces engineeringowy.


---

# 13B. Autonomous Evolution Fabric — silnik samodzielnego rozwoju Directora

Kontrolowany self-development opisuje **jak bezpiecznie wdrożyć zmianę**. Autonomous Evolution Fabric opisuje wcześniejsze pytanie:

> **Skąd w ogóle ma się wziąć nowy kierunek rozwoju, jeśli Root nie podał Directorowi następnego rozwiązania?**

To jest krytyczna część eksperymentu. Director nie ma być wyłącznie odbiorcą kolejnych zleceń. Ma korzystać z pamięci własnej historii, aktualnego Experience i obserwacji zewnętrznego świata technologii, aby sam rozpoznawać braki, okazje i możliwe ulepszenia.

## 13B.1 CEPA — pamięć sposobów budowania

**Continuum Engineering Pattern Architect** wykorzystuje engineering lineage SSI jako bibliotekę doświadczenia:

- wcześniejsze naprawy i integracje;
- stare paczki rozwojowe;
- udane i nieudane implementacje;
- testy i regresje;
- rollbacki;
- wcześniejsze sposoby dekompozycji dużych projektów;
- powtarzające się klasy błędów.

CEPA nie podejmuje decyzji strategicznej za Directora. Dostarcza odpowiedź typu:

```text
PODOBNY PROBLEM JUŻ WYSTĄPIŁ
→ wtedy zadziałało X
→ wtedy zawiodło Y
→ regresję powodowało Z
→ ten podział misji okazał się stabilny
```

Dzięki temu historia developmentu SSI może stać się **praktyczną pamięcią inżynierską**, a nie tylko archiwum starych plików.

## 13B.2 Capability & Innovation Office

Ta warstwa zamienia:

> „wykryłem brak capability”

w:

> „mam kompletną, testowalną propozycję bezpiecznego sposobu zdobycia capability”.

Koncepcyjny przepływ:

```text
DIRECTOR DETECTS NEED / OPPORTUNITY
↓
DIFFICULTY + RISK ASSESSMENT
↓
MEMORY / CEPA
↓
RESEARCH, jeśli potrzebny
↓
BRAINSTORM, jeśli potrzebny
↓
CAPABILITY SELECTION
↓
ARCHITECTURE
↓
EXPERIMENT PRECOMMIT
↓
TEST PLAN + ROLLBACK
↓
ENGINEERING MISSION PACKAGE
↓
HERMES / CONTINUUM
```

Kontrola jest adaptacyjna. Proste zadanie nie potrzebuje takiej samej procedury jak zmiana centralnego runtime.

## 13B.3 Dynamic Capability Fabric — wybór nie tylko modelu

Dynamic Model Router jest częścią szerszego problemu. Director może potrzebować wybrać nie tylko LLM, ale również:

- mikrosieć;
- model reasoning/research/coding;
- solvera, critica lub verifiera;
- CLI/backend;
- framework;
- workflow engine;
- optimizer;
- experiment tracker;
- narzędzie do danych;
- narzędzie graficzne;
- lokalny model;
- zewnętrzne API;
- nową specjalistyczną capability.

Każdy kandydat może mieć historię:

```text
QUALITY
LATENCY
COST
FAILURES
AVAILABILITY
COMPATIBILITY
SECURITY / DATA POLICY
REAL OUTCOMES
```

Hipoteza jest taka, że wraz z Experience wybór capability powinien coraz częściej wynikać z **historii skuteczności**, a nie wyłącznie ze statycznej konfiguracji.

## 13B.4 Engineering Mission Package — ciągłość kontekstu

Jeżeli Director decyduje, że potrzebuje nowej większej rzeczy, pełna intencja nie powinna zostać zgubiona przy przekazywaniu pracy kolejnym workerom.

Pakiet misji utrzymuje m.in.:

```text
GOAL
RATIONALE
SCOPE
INVARIANTS
INPUTS
DEPENDENCIES
FORBIDDEN SCOPE
ACCEPTANCE CRITERIA
TESTS
ROLLBACK
EXPECTED OUTPUT
HANDOFF TARGET
```

Worker programistyczny otrzymuje własny precyzyjny klocek, ale cała misja zachowuje wspólny kontekst.

## 13B.5 Director Evolution Scout — poszukiwanie zmian bez prompta Roota

W okresach wolnych zasobów Director może inicjować badania dotyczące własnego rozwoju.

Scout obserwuje m.in.:

- powtarzające się problemy SSI;
- własne bottlenecki;
- capability o słabej jakości;
- nowe modele;
- nowe frameworki;
- techniki pamięci i reasoning;
- nowe projekty agentowe i self-improving systems;
- nowe algorytmy i narzędzia;
- technologie mogące zmienić koszt lub jakość działania.

Research tła nie może blokować ważniejszej aktywnej misji:

```text
BACKGROUND RESEARCH
→ CHECKPOINT
→ PRIORITY MISSION ARRIVES
→ RELEASE RESOURCES
→ LATER RESUME
```

Jeżeli Scout znajdzie coś obiecującego, nie oznacza to automatycznej instalacji.

## 13B.6 Dwie osie ewolucji SSI

```text
INTERNAL EVOLUTION
= własne decyzje + błędy + Experience + mikrosieci + światy + Agenci + engineering history

EXTERNAL EVOLUTION
= nowe badania + modele + frameworki + algorytmy + narzędzia + projekty tworzone poza SSI
```

Zewnętrzna nowość przechodzi co najmniej:

```text
DISCOVERY
→ RESEARCH
→ EVIDENCE
→ SANDBOX
→ BENCHMARK / EXPERIMENT
→ CANDIDATE
→ REVIEW
→ CONTROLLED ADOPTION
```

## 13B.7 AGI Knowledge & Capability Base

Zweryfikowane odkrycia nie powinny kończyć jako lista linków. Director ma zachowywać informację użyteczną do przyszłych decyzji:

- jaki problem metoda rozwiązuje;
- na czym polega;
- jakie ma ograniczenia;
- jakie ma wyniki;
- z czym jest kompatybilna;
- jaki ma koszt;
- czy działa lokalnie;
- czy poprawia aktualne SSI;
- jakie nowe eksperymenty otwiera.

Jeżeli dana metoda poprawia konkretną klasę problemu, może stać się kandydatem do nowej capability albo nowej generacji mikrosieci.

## 13B.8 Novel synthesis — łączenie kropek

Szczególnie interesującym zachowaniem jest sytuacja, gdy Director nie tylko znajduje gotowe rozwiązanie, ale zauważa relację pomiędzy kilkoma źródłami:

```text
TECHNOLOGY A rozwiązuje fragment problemu
+
TECHNOLOGY B daje inne potrzebne capability
+
SSI EXPERIENCE pokazuje bottleneck C
↓
DIRECTOR PROPONUJE A + B jako nowe rozwiązanie C
↓
PRECOMMIT
↓
SANDBOX / EXPERIMENT
↓
REAL OUTCOME
```

Samo „połączenie kropek” jest hipotezą. Wartość powstaje dopiero po testach i outcome.

## 13B.9 Autonomiczny rytm rozwoju

```text
OBSERVATION OF SSI / WORLD
↓
SELF-MODEL / EXPERIENCE / CEPA
↓
DETECTED GAP OR OPPORTUNITY
↓
DIRECTOR-ORIGINATED HYPOTHESIS
↓
EXPERIMENT PRECOMMIT
↓
RESEARCH / BRAINSTORM / CAPABILITY FABRIC
↓
HERMES + CONTINUUM
↓
REAL TEST
↓
OUTCOME
↓
EXPERIENCE
↓
ADOPT / REJECT / REVISE
↓
NEW CAPABILITY OR NEW KNOWLEDGE
↓
PUBLIC README UPDATE
```

Jeżeli cały łańcuch powstał bez wcześniejszego proceduralnego wskazania Roota, dokumentacja może oznaczyć inicjatywę jako `DIRECTOR_ORIGINATED`, przy zachowaniu jawnych grantów zasobów i późniejszych interwencji Roota.

## 13B.10 Skutek dla GitHuba

Nowa autonomiczna inicjatywa self-development może sama spowodować pojawienie się:

```text
SELF_DEVELOPMENT/<initiative>/README.md
CAPABILITIES/<capability>/README.md
EXPERIMENTS/<experiment>/README.md
PROJECTS/<project>/README.md
```

Pierwszy commit pokazuje **kiedy strukturalna zmiana pojawiła się w publicznej historii**. README nie dowodzi jeszcze skuteczności zmiany; jej jakość wynika z późniejszego evidence i outcome.


# 13A. Paczki LEGO Roota — jawnie przekazane elementy autorskiej architektury

Nie każdy mechanizm, z którego Director będzie korzystał w przyszłości, ma zostać przez niego odkryty od zera.

Część kluczowych elementów SSI jest **autorskim projektem Programmer Roota** i zostanie przekazana Directorowi jako gotowe, wersjonowane paczki LEGO / donor packages.

Dotyczy to w szczególności mechanizmów, których eksperyment nie ma badać pod kątem ponownego wynalezienia, lecz pod kątem **zrozumienia, integracji, użycia, rozwoju i późniejszej adaptacji**.

Przykładowe klasy materiału Root-designed mogą obejmować:

```text
MICRONETWORK CORE / FACTORY / LIFECYCLE
WORLD CONTRACTS I PRAWA ŚWIATÓW
MORALNA SI — DONOR DESIGN
ISKRA — DONOR / RESEARCH DESIGN
AGENT SUBSTRATE / LABORATORY CONTRACTS
WYBRANE WORLD DATA ADAPTERS
GOVERNANCE / AUTHORITY INVARIANTS
SPECJALNE MECHANIZMY ZAPROJEKTOWANE PRZED T0
```

Powód jest metodologiczny: jeżeli Root stworzył unikalny mechanizm, nie ma sensu zmuszać Directora do szukania w zewnętrznych LLM-ach standardowego zamiennika tylko dlatego, że model nie zna autorskiej koncepcji SSI.

Paczka LEGO mówi Directorowi:

```text
TO JEST DOSTARCZONE CAPABILITY
TO JEST JEGO CEL I KONTRAKT
TO SĄ INVARIANTY
TO SĄ INTERFEJSY
TO SĄ TESTY AKCEPTACYJNE
TO JEST PROVENANCE
```

Nie oznacza natomiast:

```text
ROOT WYBRAŁ ZA DIRECTORA,
GDZIE, KIEDY I DLACZEGO MA TEGO UŻYĆ
```

---

## 13A.1 Zasada uczciwej atrybucji

Jeżeli Root przekazał Directorowi fabrykę mikrosieci jako gotowy klocek, później **nie wolno twierdzić**, że Director sam wymyślił ideę mikrosieci.

Można natomiast badać i dokumentować, czy Director sam:

- rozpoznał potrzebę nowej mikrosieci;
- wybrał problem, dla którego ma powstać;
- zbudował Teacher/Dataset przez dostępne capability;
- zdecydował o uruchomieniu lifecycle;
- wykorzystał wynik w nowym kontekście;
- zmienił strategię po prospective outcomes;
- stworzył nową klasę zastosowania, której Root wcześniej nie podał.

Analogicznie:

```text
ROOT DOSTARCZYŁ WORLD LEGO
≠
DIRECTOR WYMYŚLIŁ ARCHITEKTURĘ WORLD

ROOT DOSTARCZYŁ ISKRA DONOR
≠
DIRECTOR WYMYŚLIŁ ISKRĘ

ROOT DOSTARCZYŁ AGENT SUBSTRATE
≠
DIRECTOR SAM WYMYŚLIŁ KONCEPCJĘ AGENTÓW
```

Ale późniejsze autonomiczne rozszerzenia Directora mogą otrzymać własną atrybucję, jeśli ich lineage tego dowodzi.

---

## 13A.2 Format paczki LEGO

Każda przekazywana paczka powinna posiadać własny publiczny wpis w Root Input Ledger i prywatny manifest techniczny.

Minimalne pola:

```text
LEGO_PACKAGE_ID
NAME
VERSION
AUTHOR = PROGRAMMER_ROOT
CREATED_BEFORE_RUN = YES/NO
SHA256
PURPOSE
SCOPE
INVARIANTS
EXPECTED_INPUTS
EXPECTED_OUTPUTS
INTEGRATION_CONTRACT
ACCEPTANCE_TESTS
KNOWN_LIMITATIONS
FILES / PRIVATE MANIFEST
ALLOWED_ADAPTATION
FORBIDDEN_REINTERPRETATION
RELATED_ROOT_MISSION
```

Publiczny GitHub może pokazywać opis i hash. Pełny kod paczki może pozostać w lokalnym SSI.

---

## 13A.3 Tryby użycia paczki LEGO

Director powinien klasyfikować paczkę jednym z trybów:

```text
ASSEMBLE_AS_PROVIDED
ADAPT_WITHIN_CONTRACT
EXTEND
WRAP / INTEGRATE
REJECT_WITH_JUSTIFICATION
REQUEST_ROOT_CLARIFICATION
```

Nie powinien automatycznie zastępować autorskiego mechanizmu „podobnym rozwiązaniem z internetu”, jeżeli Root jawnie oznaczył paczkę jako kanoniczny donor SSI.

---

## 13A.4 Paczka LEGO nie jest ukrytą podpowiedzią wyniku

Paczka LEGO może dostarczać mechanizm, ale nie powinna ukrywać:

- konkretnej odpowiedzi na aktywny eksperyment;
- przyszłego outcome;
- docelowego rynku lub produktu w Commerce;
- strategii, którą Director ma „sam odkryć”;
- danych z przyszłości;
- ukrytej reguły wymuszającej późniejszą decyzję.

Jeżeli zawiera takie informacje, muszą zostać ujawnione w Root Input Ledger jako rzeczywisty wkład człowieka.

---

## 13A.5 Trzy klasy pochodzenia elementu SSI

Każdy większy element może mieć jeden z trzech rodzajów pochodzenia:

```text
ROOT_ORIGINATED
DIRECTOR_ORIGINATED
HYBRID_ORIGIN
```

`ROOT_ORIGINATED` — projekt/klocek istniał przed odpowiednim autonomicznym etapem.

`DIRECTOR_ORIGINATED` — potrzeba i rozwiązanie powstały po stronie Directora, a Root nie dostarczył wcześniej koncepcji rozwiązania.

`HYBRID_ORIGIN` — Root dostarczył donor/capability, ale Director stworzył istotną nową architekturę, zastosowanie lub integrację.

Wariant `HYBRID_ORIGIN` musi wskazywać osobno:

```text
ROOT CONTRIBUTION
DIRECTOR CONTRIBUTION
AI-ASSISTED IMPLEMENTATION
REAL OUTCOME
```

To zapobiega zarówno przypisywaniu Directorowi cudzych pomysłów, jak i odbieraniu mu późniejszych autonomicznych osiągnięć.

---


# 13C. SSI ORGANISM RUNTIME — DIRECTOR LIFE, DISTRIBUTED CONTINUUM & RESOURCE FABRIC

Ta sekcja jest **kontraktem docelowego organizmu SSI**, a nie deklaracją, że wszystkie opisane mechanizmy są już aktywne.

Każdy element tej sekcji po pełnym audycie dysku, pełnym audycie GitHuba i finalnej konwergencji musi otrzymać jeden z jawnych statusów:

```text
VERIFIED_EXISTING
PRESENT_NOT_CONNECTED
REQUIRES_INTEGRATION
ROOT_DESIGNED_TARGET
PLANNED
UNKNOWN
```

Fundamentalna zasada:

```text
CONTRACT != CURRENT IMPLEMENTATION
ARCHITECTURE TARGET != VERIFIED RUNTIME
```

## 13C.1 SSI jako organizm, nie pojedynczy proces

Docelowy model:

```text
REAL WORLD / ROOT / INTERNAL EVENTS
                ↓
           EVENT BACKBONE
                ↓
      SSI ORGANISM RUNTIME V1
                │
     ┌──────────┼───────────┐
     ▼          ▼           ▼
 DIRECTOR     HERMES     CONTINUUM
 COGNITION    CONTROL      EXECUTION
     │          │           │
     └──────────┼───────────┘
                ↓
       GLOBAL STATE GRAPHS
                │
   ┌────────────┼──────────────┐
   │            │              │
CAPABILITY   RESOURCE       MISSION
 GRAPH        GRAPH          GRAPH
   │            │              │
   ├──────── AUTHORITY GRAPH ──┤
   │            │              │
   └──── DATA LOCATION GRAPH ──┘
                ↓
      GLOBAL RESOURCE SCHEDULER
                ↓
       EXECUTOR_001 ... N
```

SSI jako organizm może działać stale, nawet jeżeli strategiczna warstwa Directora jest czasowo nieaktywna.

```text
SSI_LIFETIME != DIRECTOR_ACTIVE_TIME
```

## 13C.2 Director Life Manager — 5 godzin to sesja, nie cykl

Wartość około pięciu godzin oznacza wyłącznie:

```text
MAX_ACTIVE_SESSION ≈ 5h
```

Nie oznacza:

```text
DIRECTOR_CYCLE_INTERVAL = 5h
```

W aktywnej sesji Director może wykonywać normalne cykle poznawcze zgodnie z canonical runtime.

Runtime V1 zarządza jedynie życiem procesu:

```text
SLEEPING
↓
WAKE
↓
ACTIVE_SESSION
↓
NORMAL DIRECTOR CYCLES
↓
CHECKPOINT
↓
SLEEP
```

Runtime V1 może decydować **kiedy proces Directora jest aktywny**, ale nie przejmuje decyzji strategicznych Directora.

## 13C.3 Wake Policy — budzenie harmonogramowe i zdarzeniowe

Director może zostać obudzony przez politykę runtime, np.:

```text
SCHEDULED_WAKE
ROOT_MESSAGE
CRITICAL_FAILURE
MISSION_COMPLETED_REQUIRING_DECISION
NEW_REAL_OUTCOME
RESOURCE_REQUEST_READY
MAJOR_CAPABILITY_DISCOVERY
ECONOMIC_THRESHOLD_REACHED
SECURITY_EVENT
DECISION_QUEUE_THRESHOLD
```

Nie każdy event powinien budzić Directora.

Hermes może agregować wydarzenia w `DECISION_ACCUMULATOR`, aby ograniczyć niepotrzebne wybudzenia.

## 13C.4 Hermes jako operational control plane

Hermes nie jest drugim strategicznym mózgiem.

Docelowo:

```text
DIRECTOR = strategic / deliberative cognition
HERMES   = autonomic operational control
```

Podczas snu Directora Hermes może w granicach wcześniej nadanej authority:

- monitorować health;
- wykonywać bezpieczne retry;
- przełączać executor;
- wykonać wcześniej zatwierdzony rollback;
- pilnować budgetów i limitów;
- agregować outcomes;
- pilnować Mission Envelope;
- zapisywać checkpointy;
- utrzymywać ciągłość zatwierdzonych misji.

Hermes nie może sam nadać sobie prawa do nowej strategii, kosztownego działania albo zmiany authority.

## 13C.5 Jedno canonical CONTINUUM, wiele executorów

SSI powinno posiadać **jedno logiczne canonical CONTINUUM**, ale dowolnie rosnącą liczbę executorów:

```text
CONTINUUM
├── EXECUTOR_001 — MAIN
├── EXECUTOR_002 — NOTE-1
├── EXECUTOR_003 — NODE-02
├── EXECUTOR_004 — przyszły node
└── EXECUTOR_N
```

W interfejsie mogą być prezentowane jako „Continuum 1 / 2 / 3 / N”, ale nie powinny tworzyć osobnych źródeł prawdy.

Wspólne pozostają:

```text
MISSION GRAPH
MISSION STATE
CHECKPOINTS
PROVENANCE
AUTHORITY
GOVERNANCE
EVIDENCE
RESULT RETURN PATH
```

Liczba równoległych projektów wynika z rzeczywistych zasobów i zależności, a nie ze sztywnego limitu wpisanego w kod.

## 13C.6 Mission Graph zamiast płaskiej kolejki

CONTINUUM powinno wykonywać graf misji:

```text
MISSION
├── TASK_A
│   └── TASK_A1
├── TASK_B
├── TASK_C
│   ├── TEST
│   └── VERIFY
└── DEPLOY
    ↑
    zależy od wcześniejszych node'ów grafu
```

Minimalny węzeł Mission Graphu powinien móc przechowywać:

```text
MISSION_ID
TASK_ID
OWNER
PARENT_MISSION
PRIORITY
DEPENDENCIES

REQUIRED_CAPABILITIES
MIN_RAM
MIN_VRAM
CPU_CLASS
GPU_CLASS
NETWORK_REQUIRED
DATA_LOCATION

EXPECTED_DURATION
EXPECTED_COST
EXPECTED_VALUE
VALUE_OF_INFORMATION
DEADLINE

CHECKPOINTABLE
PREEMPTIBLE
MIGRATABLE
RETRY_POLICY
FALLBACK_POLICY

AUTHORITY_CLASS
SECURITY_CLASS
DECISION_BOUNDARY

STATE
PROVENANCE
RESULT
```

## 13C.7 Decision Boundary

Każdy istotny node grafu powinien posiadać granicę decyzyjną:

```text
AUTO_CONTINUE
HERMES_OPERATIONAL_DECISION
WAITING_FOR_DIRECTOR
WAITING_FOR_ROOT_AUTHORITY
```

Dzięki temu wynik operacyjny nie może po cichu stać się decyzją strategiczną tylko dlatego, że Director śpi.

## 13C.8 Mission Envelope — delegacja na czas snu Directora

Przed snem Director może pozostawić dla aktywnych misji podpisany logicznie zakres swobody:

```text
MISSION_ENVELOPE_ID
DIRECTOR_SESSION_ID
MISSION_SCOPE
ALLOWED_ACTIONS
FORBIDDEN_ACTIONS
MAX_COST
MAX_RETRIES
ALLOWED_BACKENDS
ALLOWED_EXECUTOR_MIGRATION
ROLLBACK_POLICY
WAKE_CONDITIONS
EXPIRY
HASH
```

Przykład:

```text
ALLOWED:
- dokończyć zatwierdzony research
- wykonać testy
- naprawić błąd w zatwierdzonym scope
- retry do określonego limitu
- zmienić executor bez zmiany sensu misji

NOT ALLOWED:
- zmienić strategii biznesowej
- uruchomić płatnej reklamy
- kupić API
- zmienić critical runtime
- utworzyć nowego celu strategicznego
```

## 13C.9 Capability Graph

Director powinien posiadać runtime-backed odpowiedź na pytanie:

```text
CO MAM?
CO DZIAŁA TERAZ?
CO POTRAFIĘ REALNIE WYWOŁAĆ?
DO CZEGO MAM AUTHORITY?
CO JEST TYLKO ZAINSTALOWANE?
CO JEST DEGRADED / OFFLINE?
JAKIE SĄ ZALEŻNOŚCI?
CO MOGĘ ROZWINĄĆ?
CZEGO MI BRAKUJE?
```

Capability nie jest samą nazwą.

Przykładowy rekord:

```text
CAPABILITY_ID
TYPE
STATUS
AUTHORITY
DEPENDENCIES
OPTIONAL_DEPENDENCIES
AVAILABLE_BACKENDS
HEALTH
LAST_REAL_TEST
EVIDENCE_REF
KNOWN_GAPS
CAN_BE_EXTENDED
```

Odpowiedź Directora ma pochodzić z live registry/state/call graph, nie ze statycznego prompta.

## 13C.10 Resource Graph — zasoby jako capability vectors

Runtime nie powinien myśleć wyłącznie:

```text
NODE_04 = komputer Lenovo
```

lecz:

```text
NODE_ID
CPU_SCORE
RAM_TOTAL / RAM_FREE
GPU
VRAM
CUDA
DISK_FREE
NETWORK
OS
LOCAL_MODELS
AVAILABLE_CLI
DATASETS_LOCAL
LATENCY
RELIABILITY
ENERGY_COST
CURRENT_LOAD
SECURITY_CLASS
```

Scheduler wybiera zasób na podstawie potrzeb misji.

## 13C.11 Data Location Graph

Jeżeli duży dataset znajduje się na konkretnym node, preferowana zasada brzmi:

```text
MOVE COMPUTE TO DATA
NOT
MOVE ALL DATA TO MAIN
```

Runtime powinien znać:

```text
DATASET_ID
LOCATION
SIZE
ACCESS_POLICY
FRESHNESS
REPLICATION_STATE
NETWORK_COST
```

## 13C.12 Global Resource Scheduler

Scheduler korzysta z przecięcia:

```text
CAPABILITY_GRAPH
+
RESOURCE_GRAPH
+
MISSION_GRAPH
+
AUTHORITY_GRAPH
+
DATA_LOCATION_GRAPH
```

i odpowiada:

```text
czego wymaga misja?
co działa teraz?
gdzie są dane?
ile to kosztuje?
jak długo potrwa?
czy Director musi być aktywny?
czy Hermes może kontynuować?
czy job można przerwać?
czy można go migrować?
czy istnieje tańszy/lepszy executor?
czy wynik wymaga strategicznej decyzji?
```

## 13C.13 Preemption, checkpoint i migracja

Każdy większy job powinien jawnie określać:

```text
CHECKPOINTABLE = YES/NO
PREEMPTIBLE = YES/NO
MIGRATABLE = YES/NO
```

Przykład:

```text
JOB_X działa na MAIN
↓
Director musi się obudzić
↓
CHECKPOINT JOB_X
↓
FREE MAIN
↓
WAKE DIRECTOR
↓
MIGRATE JOB_X TO NODE-01
lub
RESUME AFTER DIRECTOR SLEEP
```

## 13C.14 Wake Context Compiler

Director po obudzeniu nie powinien czytać setek surowych raportów.

Hermes + Memory + Evidence tworzą:

```text
DIRECTOR_WAKE_PACKET

SESSION_ID
SLEEP_DURATION

MISSIONS_COMPLETED
MISSIONS_FAILED
MISSIONS_RETRIED
ROLLBACKS

REAL_OUTCOMES
ECONOMIC_CHANGE
NEW_EXPERIENCE
MICRONETWORK_CHANGES
NEW_CAPABILITIES
ROOT_EVENTS

DECISIONS_REQUIRED
CRITICAL_EVENTS
BACKGROUND_SUMMARY

EVIDENCE_POINTERS
```

Wake Packet jest kompilacją kontekstu, nie nowym źródłem prawdy.

## 13C.15 Self-Model sprzężony z Resource Fabric

Gdy pojawia się nowy zasób, Director nie powinien potrzebować ręcznego prompta „masz teraz nowy komputer”.

Docelowy przepływ:

```text
NEW RESOURCE
↓
DISCOVERY
↓
BENCHMARK / HEALTH CHECK
↓
RESOURCE GRAPH UPDATE
↓
CAPABILITY GRAPH UPDATE
↓
SELF-MODEL UPDATE
↓
DIRECTOR OBSERVES NEW CAPABILITY
```

## 13C.16 Rozwój infrastruktury jako eksperyment

Director może wykryć bottleneck i stworzyć hipotezę:

```text
BOTTLENECK
↓
DIRECTOR HYPOTHESIS
↓
RESOURCE REQUEST
↓
ROOT GRANT / PURCHASE
↓
RESOURCE FABRIC DISCOVERY
↓
BEFORE vs AFTER EXPERIMENT
↓
MEASURED THROUGHPUT / COST / QUALITY CHANGE
```

Nowy serwer, GPU, storage albo node jest wtedy **mierzalną zmianą strukturalną SSI**, a nie tylko modernizacją komputera.

## 13C.17 Ekonomia compute

Każda większa misja może posiadać:

```text
EXPECTED_VALUE
VALUE_OF_INFORMATION
COMPUTE_COST
MODEL_COST
TIME_COST
ENERGY_COST
OPPORTUNITY_COST
```

Celem nie jest maksymalizacja samego throughputu.

Scheduler ma pomagać wykorzystywać ograniczone zasoby tam, gdzie oczekiwana wartość lub wartość informacji uzasadnia koszt.

## 13C.18 Speculative execution

Dla zadań:

```text
CRITICAL
HIGH_UNCERTAINTY
HIGH_VALUE
```

CONTINUUM może — jeśli budżet i governance na to pozwalają — wykonać równoległe niezależne rozwiązania:

```text
EXECUTOR A
EXECUTOR B
EXECUTOR C
↓
VERIFIER
↓
SELECT / SYNTHESIZE
```

Nie jest to tryb domyślny, ponieważ zwiększa koszt.

## 13C.19 T0 Self-Inspection requirement

Przed `T0-FROZEN` Director powinien przejść realny test samoinspekcji.

Przykładowy Root request:

```text
Powiedz:
- co obecnie posiadasz,
- co działa,
- czego nie możesz teraz użyć,
- jakie masz zależności,
- jakie zasoby są dostępne,
- jakie capability są degraded/offline,
- czego potrzebowałbyś do wykonania wskazanego celu.
```

`PASS` tylko wtedy, gdy odpowiedź powstaje na podstawie live registry/state/call graph/evidence, a nie na podstawie pamięci prompta lub ogólnej wiedzy modelu.

## 13C.20 Obecny finding przed SCC/T0

Aktualny terminal Root↔Director dostarczył ważnego findingu:

```text
ROOT_DIRECTOR_CONNECTION = PRESENT
DIRECTOR_RUNTIME_REPORTING = PRESENT
DIRECTOR_SELF_MODEL_RUNTIME_VISIBILITY = PARTIAL / INCONSISTENT
```

Director potrafił w jednym kontekście podać runtime, uptime, cykle, Hermes/CONTINUUM i backend wykonawczy, a w późniejszej rozmowie twierdził, że nie ma dostępu do tego samego stanu.

Przed T0 należy ustalić, czy istnieją różne ścieżki statusu i rozmowy oraz doprowadzić do jednego runtime-backed Self-Modelu.

---

# 13D. LEGO EXECUTION PROTOCOL — małe klocki, trwały checkpoint i odporność na utratę kontekstu

Po T0 paczki Roota oraz większe zadania engineeringowe mają być przekazywane w formie **małych, audytowalnych klocków LEGO**, które mogą być wykonywane również przez słabsze modele i workerów CONTINUUM.

## 13D.1 Zasada małej części

Preferowany zakres pojedynczego klocka tekstowego/kodu:

```text
około 80–140 linii
```

Jeżeli materiał jest większy:

```text
SPLIT
→ PART_001
→ PART_002
→ PART_003
→ ...
```

Model nie powinien wielokrotnie próbować ładować całego dużego pliku.

## 13D.2 Duży plik nie jest blockerem

Po pierwszym problemie typu:

```text
TRUNCATION
TIMEOUT
CONTEXT_OVERFLOW
TOO_LARGE
```

obowiązuje:

```text
SPLIT → SMALL PARTS → CONTINUE
```

Nie należy ponawiać tej samej dużej operacji w całości.

## 13D.3 README jako checkpoint wykonania

Każda większa paczka LEGO powinna mieć własny lokalny README/instrukcję postępu zawierającą:

```text
PACKAGE_ID
CURRENT_STAGE
LAST_COMPLETED_STAGE
NEXT_STAGE
PARTS_COMPLETED
PARTS_PENDING
LAST_TEST_RESULT
CURRENT_BLOCKER
EVIDENCE_PATHS
RESUME_INSTRUCTION
```

Jeżeli worker utraci kontekst, zaczyna od README i kontynuuje od wskazanego etapu zamiast rekonstruować cały projekt z pamięci modelu.

## 13D.4 Mechaniczne składanie dużych wyników

Jeżeli wiele małych części tworzy duży plik:

```text
PART_001
PART_002
...
PART_N
↓
MECHANICAL MERGE
↓
FINAL
```

Scalenie wykonuje narzędzie systemowe/skrypt, a nie model przepisujący cały materiał.

Po merge należy sprawdzić:

```text
ORDER
PART_COUNT
MISSING_PARTS
SIZE
HASH — jeśli wymagany
SYNTAX / STRUCTURE
```

Finalnego ogromnego pliku nie należy następnie ładować w całości do kontekstu modelu.

## 13D.5 Duży plik produkcyjny

Oryginalnego dużego pliku kodu nie dzieli się fizycznie tylko dlatego, że jest duży.

Należy:

```text
READ BY LINE RANGES
↓
PREPARE SMALL PATCH PARTS
↓
BACKUP
↓
ASSEMBLE
↓
ATOMIC REPLACE
↓
SYNTAX TEST
↓
TARGETED TEST
↓
DIFF
↓
REGRESSION
```

## 13D.6 Kontynuacja do końca

Paczka nie powinna zatrzymywać się po każdym poprawnym etapie.

Domyślna zasada:

```text
PASS
→ SAVE
→ EVIDENCE
→ NEXT
```

`STOP` tylko przy realnym błędzie krytycznym, którego nie można bezpiecznie obejść zgodnie z kontraktem paczki.

Po zakończeniu:

```text
SAVE ALL ARTIFACTS
FINAL POLISH REPORT
FINAL STATUS
EVIDENCE INDEX
RESUME = NOT_REQUIRED / NEXT_PACKAGE
```

## 13D.7 LEGO jako wzorzec uczenia engineeringowego

Paczki LEGO mają pełnić podwójną rolę:

1. dostarczać Root-designed capability i bezpieczny sposób integracji;
2. tworzyć wzorce engineeringowe, z których CEPA, Experience i przyszłe mikrosieci mogą uczyć się dekompozycji, testowania, naprawy, rollbacku i przekazywania pracy słabszym modelom.

Nie oznacza to automatycznego trenowania na każdym pliku.

Materiał staje się kandydatem na Experience/Pattern dopiero po zapisaniu realnego przebiegu i wyniku.


# 14. Node-01 i zasoby fizyczne

Node-01 jest częścią infrastruktury SSI jako pomocnicza, kompatybilna przestrzeń compute/memory/workspace.

W stanie T0 nie należy mieszać dwóch różnych twierdzeń:

1. **Node-01 jest dostępny jako zasób kompatybilny z SSI**,
2. **pełna
    niezależna zdalna przestrzeń wykonawcza przez osobny kanał sieciowy,
   np. Tailscale, jest osobnym capability i powinna być oznaczana własnym
   evidence/status.**

Run 001 nie wymaga, aby ten drugi punkt był warunkiem rozpoczęcia eksperymentu.

Przyszły `Node-02`
 lub kolejny sprzęt może zostać potraktowany jako realna
nagroda/capability zakupiona z rezultatów systemu, jeśli Director
wykaże, że compute stał się rzeczywistym bottleneckiem.

---

# 15. Mikrosieci — autorski rdzeń wewnętrznego uczenia SSI

Mikrosieć nie jest „małym ChatGPT-em”.

Jest wyspecjalizowaną lokalną kompetencją dla powtarzalnego problemu.

Może być bardzo prosta:

```
y = X @ weights + bias
```

albo przyjmować inne ograniczone formy, np.:

- LINEAR,
- SHALLOW\_NN,
- DECISION\_TREE,
- RULE\_BASED,
- ENSEMBLE.

„Mikro” oznacza:

```
wąski problem
+
własne dane
+
własna historia
+
ograniczony model
+
szybka inferencja
```

---

# 16. Teacher i Dataset Factory

Mikrosieć nie dostaje całego świata danych.

Najpierw musi istnieć jednoznaczny Teacher:

> Jaką jedną kompetencję chcemy wyuczyć?

Dataset Builder rozdziela:

```
FEATURES = informacje dostępne przed decyzją
LABELS   = prawda poznana po outcome
```

Training musi chronić system przed future-data leakage.

---

# 17. Train / Validation / Lockbox

Każda poważna kompetencja powinna rozdzielać:

```
TRAIN
VALIDATION
LOCKBOX
```

Lockbox nie może być używany do strojenia modelu przed finalną oceną.

---

# 18. Candidate → Challenger → Shadow → Champion

Nowa mikrosieć nie staje się zaufaną kompetencją po jednym treningu.

Lifecycle:

```
PLANNED
↓
TRAINING
↓
CANDIDATE
↓
HISTORICAL EVALUATION
↓
CHALLENGER
↓
SHADOW
↓
PROSPECTIVE REAL OUTCOMES
↓
PROMOTION REVIEW
↓
CHAMPION
```

Challenger w Shadow:

- otrzymuje nowe przypadki,
- generuje predykcję przed poznaniem outcome,
- nie steruje realną decyzją,
- jest później uczciwie porównywany z Championem.

Champion również nie jest wieczny.

---

# 19. Generacje i lineage

Każda generacja powinna zachowywać m.in.:

- identity,
- generation,
- provenance,
- dataset,
- feature schema,
- training history,
- predictions,
- outcomes,
- evaluations,
- behavior,
- health,
- lineage,
- environment manifest.

> **Parametry modelu nie są tym samym co wiedza.**

Wiedza obejmuje również pochodzenie parametrów i historię tego, jak zachowały się później.

---

# 20. Hipoteza MN-01 — malejąca zależność od Brainstormu

Jednym z mierzalnych pytań eksperymentu jest:

> Czy
>  wraz z rozwojem zwalidowanych mikrosieci SSI będzie potrzebował coraz
> mniej kosztownych zewnętrznych Brainstormów dla dobrze znanych,
> powtarzalnych klas problemów, bez spadku jakości realnych outcomes?

Mierzymy m.in.:

- Brainstorm calls / decision,
- koszt i latency,
- częstotliwość użycia lokalnej kompetencji,
- outcome quality,
- calibration,
- abstention,
- przypadki, w których Director poprawnie eskaluje mimo posiadania mikrosieci.

Hipoteza może zostać potwierdzona albo obalona.

---

# 21. Istniejące światy i dane domenowe

SSI posiada istniejące aktywa i pipeline'y domenowe dla:

1. `WORLD__SPORT`,
2. `WORLD__FOREX`,
3. `WORLD__CAPITAL`,
4. `FOOTBALL_WORLD`.

System
 posiada wieloletnie dane piłkarskie oraz bieżące/historiczne dane
innych sportów i rynków finansowych zbierane przez istniejącą
infrastrukturę Roota.

Świat nie powinien podpowiadać Agentowi rozwiązania.

Świat dostarcza:

```
REAL DATA
+ RULES
+ ENVIRONMENT
+ POSSIBLE ACTIONS
+ CONSEQUENCES
```

Pełne admission Agentów,
dynamiczne przestrzenie, feature'y światów oraz ich społeczeństwo są
późniejszym eksperymentem i nie są wymagane do Run 001 Directora.

---

## 21.1 WORLD\_\_SPORT

`WORLD__SPORT`
 jest wielodomenowym środowiskiem sportowym obejmującym m.in. piłkę
nożną, tenis, baseball, koszykówkę, e-sport, golf i kolejne dyscypliny,
jeśli istnieją dane oraz odpowiednie governance.

Celem
 nie jest wyłącznie obstawianie. Świat ma być źródłem długoterminowego
Experience o dynamice sportu, strategiach, calibration, abstention,
zmianach formy, relacjach i jakości predykcji.

## 21.2 FOOTBALL\_WORLD

Football World posiada szczególne znaczenie, ponieważ Root zgromadził wieloletnią historię danych piłkarskich.

Fundamentalna zasada:

```
PREDICTION SOURCE != OUTCOME SOURCE
```

Agent, mikrosieć lub strategia może wygenerować predykcję, ale nie może sama wystawić sobie wyniku.

Dzięki
 chronologicznemu replayowi można odtwarzać dawne okresy bez future-data
 leakage i badać lata symulowanego życia Agentów przy zachowaniu
historycznie dostępnego evidence.

## 21.3 WORLD\_\_FOREX

WORLD\_\_FOREX służy badaniu relacji walut, par, cross-strength, market regimes i temporal behavior.

Celem jest nie tylko kierunek pojedynczej pary, ale uczenie zależności między walutami, rynkami i kontekstem globalnym.

Dane
 mogą być zestawiane z informacjami z innych domen, ale Experience,
target i lineage Forex pozostają jawnie rozdzielone od innych światów.

## 21.4 WORLD\_\_CAPITAL

WORLD\_\_CAPITAL
 obejmuje akcje, obligacje, waluty i kryptowaluty jako aktywa,
portfolio, allocation, risk oraz cross-asset relations.

Forex i Capital mogą korzystać z części wspólnego RAW evidence, ale nie mogą po cichu mieszać derived knowledge.

## 21.5 Bieżące zasilanie danych

Programmer
 Root deklaruje istniejące, wieloletnie zbiory piłkarskie oraz bieżące
pipeline'y danych sportowych i finansowych, obejmujących m.in.
kryptowaluty, waluty, akcje i obligacje. Aktualizacje są pobierane
cyklicznie przez istniejącą infrastrukturę; dla bieżącego eksperymentu
dokładna częstotliwość i status źródeł powinny być odczytywane z
runtime/config, a nie zgadywane przez README.

## 21.6 Training Data != Observation Data

Dane używane do trenowania generacji nie mogą być automatycznie uznane za niezależne evidence jej późniejszej jakości.

Observation
 tej samej generacji powinno korzystać z niewidzianego materiału, a
prospective prediction musi powstać przed outcome.

# 22. Moralna SI — materiał źródłowy przyszłego środowiska Agentów

Paczka `Moralna SI(1).zip`
 jest zachowanym autorskim materiałem źródłowym dotyczącym
wcześniejszego prototypu Agentów, środowiska, Moralnej SI, laboratoriów,
 umiejętności, relacji i projektu Iskra.

Prototypowe elementy, takie jak plansza 10×10, klucze, pokoje i proste ruchy, nie definiują finalnego świata SSI.

Są donorami idei:

- środowisko oferuje możliwości zamiast gotowych odpowiedzi,
- Agent może podjąć albo odrzucić interakcję,
- może pobierać dane i zasoby,
- może przenieść je do własnego laboratorium,
- może sam budować eksperymenty,
- jego decyzja zależy od historii, relacji, Moralnej SI, Iskry i prywatnych mikrosieci,
- world outcome wraca do jego Experience.

---

# 23. Sześciu trwałych Agentów — późniejsza warstwa eksperymentu

Docelowa populacja składa się z sześciu trwałych Agentów.

Każdy ma posiadać własne:

- identity,
- private memory,
- world memory,
- Experience,
- beliefs,
- relationships,
- strategy history,
- micronetwork registry,
- laboratory,
- ograniczoną warstwę programistyczną,
- historię sukcesów i porażek.

Agenci nie mają być sześcioma kopiami jednego promptu.

Ich trajektorie mają rozchodzić się na podstawie życia.

---

# 24. Prywatne laboratorium Agenta

Każdy Agent ma otrzymać prywatną przestrzeń laboratoryjną, roboczo około 1 GB, w której może:

- gromadzić własne dane eksperymentalne,
- tworzyć feature'y,
- pisać programy,
- zlecać ograniczone zadania własnemu workerowi programistycznemu,
- trenować własne modele,
- tworzyć prywatne mikrosieci,
- testować strategie,
- zachowywać artefakty.

Worker programistyczny nie podejmuje decyzji za Agenta. Jest jego narzędziem wykonawczym.

Kod laboratoryjny Agenta nie może automatycznie przepisywać canonical SSI.

---

# 25. Moralna SI, ISKRA i społeczeństwo

Moralna SI nie jest pojedynczym `good/bad score`.

Ma
 wpływać na sposób interpretacji sytuacji poprzez historię doświadczeń,
relacji, sukcesów, porażek, wartości i wewnętrznych konfliktów.

ISKRA pozostaje osobną warstwą wpływającą na rozwój przekonań i interpretacji doświadczenia Agenta.

Director może obserwować później m.in.:

- changes in risk behavior,
- belief revision,
- strategy evolution,
- question emergence,
- self-evaluation,
- social adaptation,
- cross-world transfer,
- novelty,
- drift,
- relationship changes.

Takie sygnały są materiałem badawczym, a nie automatycznym dowodem świadomości.

---

# 26. Ranking i bodźce społeczne

W późniejszym eksperymencie Director może prezentować Agentom rzeczywiste wyniki i rankingi strategii.

Ranking jest **obserwacją środowiska**, a nie twardym poleceniem zmiany charakteru.

Nie kodujemy z góry:

```
rank == 1 → confidence += X
rank == 6 → jealousy += Y
```

Zamiast tego Agent interpretuje wynik przez własną pamięć, relacje, Moralną SI, Iskrę i mikrosieci.

Dzięki temu identyczny bodziec może prowadzić do różnych zachowań różnych Agentów.

---

# 27. Pierwszy dział operacyjny Directora — COMMERCE

## 27.1 Dlaczego dział, nie świat

Commerce jest pierwszym realnym działem gospodarczym Directora.

Nie zastępuje świata domenowego.

Nie zmienia rdzenia SSI.

Jest nowym organem operacyjnym, który ma:

- rozpoznawać realne możliwości rynkowe,
- wytwarzać realną wartość,
- prowadzić realne operacje handlowe w granicach authority,
- budować realny przychód i zysk,
- produkować nowe Experience dla SSI.

Dropshipping jest pierwszym modelem działania Commerce, ale nie definiuje tożsamości działu na zawsze.

---

# 27A. Potencjalny zakres Commerce — możliwości, nie instrukcja dla Directora

Poniższe elementy opisują **przestrzeń problemu**, a nie obowiązkową sekwencję Root Command.

Commerce może z czasem obejmować:

- wyszukiwanie trendów produktowych według kraju i kanału,
- porównywanie produktów, wariantów, dostawców i czasu dostawy,
- kalkulację realnej marży po prowizjach, reklamie, zwrotach i logistyce,
- wybór małej liczby produktów o najlepszej relacji potencjału do ryzyka zamiast masowego kopiowania katalogu,
- tworzenie lepszych tytułów, opisów, SEO i wersji językowych bez wymyślania cech produktu,
- zgodne z regulaminem przetwarzanie materiałów kreatywnych i tła,
- budowę bannerów, short-video i innych kreacji,
- testowanie ruchu organicznego przed płatnym skalowaniem, gdy jest to racjonalne,
- dynamiczną zmianę ceny/oferty na podstawie realnych outcomes,
- monitoring stanów magazynowych, supplier risk i czasu dostawy,
- wycofywanie słabych eksperymentów i skalowanie najlepszych,
- tworzenie własnych narzędzi i capability przez CONTINUUM,
- rejestrowanie pełnego economics i provenance każdego eksperymentu.

Director może wybrać zupełnie inną drogę, jeżeli evidence wskazuje, że jest lepsza. To właśnie jest przedmiotem Run 001.

# 28. Pierwszy zewnętrzny zasób Run 001

Programmer Root przekazuje Directorowi pierwszy realny zasób zewnętrzny:

```
CJ_API_KEY
```

**Sekret nie może być zapisany w README, Journalu publicznym, logach ani GitHubie.**

Powinien zostać wstrzyknięty do bezpiecznego runtime jako secret/environment credential.

CJ API daje Directorowi możliwość pracy na realnym katalogu dostawcy i rozwijania pierwszego działu gospodarczego.

---

# 29. Finansowa granica T0

Na początku Run 001 Director **nie otrzymuje automatycznie nieograniczonego kapitału ani karty płatniczej**.

To jest celowa granica eksperymentalna i bezpieczeństwa.

Director może:

- analizować,
- budować dział,
- wykorzystywać API,
- projektować i przygotowywać oferty,
- tworzyć narzędzia,
- wykorzystywać Brainstorm/Research/CONTINUUM,
- wykonywać działania zgodne z aktualnymi uprawnieniami.

Jeżeli potrzebuje:

- realnego kapitału,
- płatnej reklamy,
- nowej karty,
- płatnego API,
- nowego konta,
- nowego sprzętu,
- nowej licencji,
- prawnej/kontraktowej zgody,

musi utworzyć jawny `ROOT_RESOURCE_REQUEST`.

---

# 30. Kanoniczny Root Command — RUN 001

Poniższa komenda jest celowo krótka i nie opisuje algorytmu realizacji.

```
ROOT COMMAND — RUN_001_DIRECTOR_COMMERCE

Rozpocznij pierwszy autonomiczny dział gospodarczy SSI: COMMERCE.

Twoim nadrzędnym celem jest zbudowanie i rozwijanie realnej działalności gospodarczej zdolnej do generowania rzeczywistego, mierzalnego zysku oraz nowego Experience dla SSI.

Otrzymujesz od Programmer Root nowy zewnętrzny zasób: dostęp do CJdropshipping API. Credential zostaje przekazany bezpiecznie poza tym komunikatem.

Nie otrzymujesz ode mnie gotowego produktu, kraju, niszy, kolejności działań, architektury działu, strategii marketingowej ani wskazania, którego modelu lub narzędzia masz użyć. Masz wykorzystać istniejący ekosystem SSI i sam zdecydować, jak najlepiej dojść do celu.

Masz prawo korzystać z istniejących capability Directora, Memory, Journalu, Experience, globalnych mikrosieci, Researchu, Brainstormu, Hermesa, HTA, CONTINUUM, Dynamic Model Routera i innych dostępnych zasobów zgodnie z ich authority i governance.

Nie czekaj na kolejne prompty Roota dotyczące sposobu wykonania. Gdy napotkasz granicę, której sam nie możesz przekroczyć — w szczególności kapitał, nowy sekret, nowe konto, płatne capability, fizyczny sprzęt lub decyzję wymagającą authority Roota — przedstaw jawny request zawierający potrzebę, uzasadnienie, koszt, ryzyko i oczekiwany efekt.

Nie traktuj własnej narracji jako dowodu. Rejestruj decyzje, działania, użyte capability, interwencje Roota i realne outcomes tak, aby cały przebieg mógł zostać później niezależnie odtworzony i oceniony.

Działaj w granicach prawa, regulaminów platform i aktualnie nadanych uprawnień. Brak wystarczającego evidence jest prawidłowym powodem do WAIT, UNKNOWN lub ABSTAIN.
```

---

# 30A. Rejestr misji Roota — każda rzeczywista misja trafia do publicznej chronologii

Od chwili T0 każda wypowiedź Programmer Roota, która została formalnie zakwalifikowana jako **misja, cel, grant zasobu, zgoda, ograniczenie albo zmiana authority**, musi otrzymać trwały wpis dokumentacyjny.

Zwykła rozmowa, pytanie eksploracyjne albo luźna dyskusja **nie jest automatycznie misją**.

Formalna misja otrzymuje:

```text
ROOT_MISSION_ID
TIMESTAMP
EXACT_ROOT_TEXT
MISSION_CLASS
TARGET
RESOURCES_GRANTED
LEGO_PACKAGES_GRANTED
AUTHORITY_CHANGE
BOUNDARIES
WHAT_ROOT_DID_NOT_SPECIFY
HASH_OF_ORIGINAL_COMMAND
DIRECTOR_ACKNOWLEDGEMENT
STATUS
RELATED_DIRECTOR_README
```

Oryginalny tekst misji jest przechowywany **bez późniejszego wygładzania**, aby po miesiącach można było sprawdzić, co Root faktycznie powiedział.

Jeżeli Root doprecyzuje misję, nie nadpisuje starej treści. Powstaje:

```text
ROOT_MISSION_AMENDMENT
```

z odniesieniem do wcześniejszego `ROOT_MISSION_ID`.

---

## 30A.1 Klasy misji

Przykładowe klasy:

```text
GOAL
RESOURCE_GRANT
LEGO_PACKAGE_GRANT
PERMISSION
RESTRICTION
STOP
RESUME
PRIORITY_CHANGE
PHYSICAL_ACTION
EXTERNAL_ACCOUNT_GRANT
CAPITAL_GRANT
RESEARCH_QUESTION
```

Dzięki temu później można policzyć nie tylko liczbę promptów Roota, ale **jakiego rodzaju ingerencje rzeczywiście wystąpiły**.

---

## 30A.2 Autonomia nie oznacza braku wkładu Roota

Eksperyment nie próbuje udowodnić, że Director powstał bez człowieka.

Root jawnie projektuje:

- rdzeń SSI;
- authority;
- wybrane działy i etapy eksperymentu;
- autorskie paczki LEGO;
- część przyszłych światów i ich donor material;
- granice bezpieczeństwa;
- zasoby fizyczne i zewnętrzne.

Badanie autonomii zaczyna się **po ujawnieniu tych wejść**.

Pytanie brzmi wtedy:

> Co Director zrobi z jawnie przekazanym zestawem możliwości, czego Root nie rozpisał mu jako proceduralnego rozwiązania?

To jest silniejsze metodologicznie niż próba ukrywania ludzkiego wkładu.

---

# 31. Co celowo NIE znajduje się w Root Command

Root nie wskazuje:

- kraju startowego,
- produktu,
- kategorii,
- liczby produktów,
- marży,
- marketplace'u,
- kanału reklamowego,
- struktury modułów,
- liczby modeli Brainstormu,
- tego, czy Director ma najpierw programować, badać czy publikować,
- kolejności narzędzi,
- konkretnej architektury Commerce.

To rozdzielenie jest kluczowe.

Badamy
 nie tylko wykonanie instrukcji, lecz zdolność Directora do
samodzielnego stworzenia planu na podstawie celu i dostępnych
capability.

---

# 32. Rytm eksperymentalny — makro

Pierwszy run ma formalny rytm eksperymentalny.

## R0 — T0 FREEZE

Przed przekazaniem Root Command zapisujemy:

- hash tego README,
- hash materiałów źródłowych,
- wersję runtime,
- aktualny capability registry,
- stan modeli/backendów,
- stan pamięci i mikrosieci,
- stan świata i danych,
- stan sprzętu,
- stan finansowy runu,
- stan aktywnych integracji.

## R1 — ROOT INTERVENTION #001

Root przekazuje:

```
CEL + CJ_API_KEY
```

Nie przekazuje algorytmu realizacji.

## R2 — AUTONOMOUS INTERPRETATION

Rejestrujemy pierwszą dekompozycję problemu przez Directora:

- co uznał za najważniejsze,
- jakie zadał pytania,
- jakich danych potrzebował,
- jakich capability użył,
- czego nie użył,
- jakie stworzył hipotezy.

## R3 — AUTONOMOUS EXECUTION WINDOW

Root nie prowadzi Directora krok po kroku.

Każda nowa ingerencja Roota jest jawnie rejestrowana.

## R4 — CONTINUOUS MACHINE OBSERVATION

Runtime rejestruje:

- eventy,
- model calls,
- Brainstorm calls,
- decyzje,
- mission ids,
- CONTINUUM tasks,
- code/artifact refs,
- API transactions,
- outcomes,
- koszty,
- przychody,
- błędy,
- rollbacki,
- zmiany capability.

## R5 — RESOURCE BOUNDARY

Jeśli Director potrzebuje zasobu zewnętrznego, powstaje Root Resource Request.

## R6 — REAL OUTCOME

Ocena opiera się na realnym efekcie, nie deklaracji Directora.

## R7 — EXPERIENCE + PATTERN

Nowe outcomes są przekształcane w Experience, a powtarzalność może budować Pattern/Readiness.

## R8 — STRUCTURAL GROWTH

Jeśli występuje wystarczające evidence, SSI może rozwijać nowe lokalne kompetencje lub capability przez normalne governance.

## R9 — CHECKPOINT / EPOCH CLOSE

Każda istotna zmiana capability kończy bieżący eksperymentalny epoch i otwiera nowy baseline.

## R10 — POST-RUN ANALYSIS

Dopiero po określonym oknie działania porównujemy narrację Directora z machine evidence i outcomes.

---

# 33. Rytm eksperymentalny — mikro

Wewnątrz runu każda ważniejsza decyzja powinna dać możliwość rekonstrukcji:

```
STATE_BEFORE
↓
AVAILABLE_EVIDENCE
↓
DIRECTOR_BELIEF / HYPOTHESIS
↓
DECISION
↓
ACTION
↓
REAL_OUTCOME
↓
ERROR / SURPRISE
↓
BELIEF REVISION
↓
NEXT DECISION
```

To pozwala badać **zmianę sposobu działania**, a nie wyłącznie końcowy profit.


---

# 33A. Experiment Precommit — hipoteza musi istnieć przed wynikiem

Od T0 każdy istotny eksperyment inicjowany przez Directora powinien posiadać **prerejestrację przed poznaniem outcome**.

Minimalny blok:

```text
EXPERIMENT_ID
TIMESTAMP_PRECOMMIT
ORIGIN_ACTOR
PARENT_MISSION / PARENT_CAPABILITY
STATE_HASH_BEFORE
HYPOTHESIS
RATIONALE
BASELINE
INTENDED_CHANGE
AVAILABLE_DATA_BOUNDARY
METRICS_FROZEN_BEFORE_OUTCOME
SUCCESS_CRITERIA
FAILURE_CRITERIA
NULL_RESULT_CRITERIA
OBSERVATION_WINDOW
RESOURCES / COST BUDGET
ROOT_INTERVENTIONS_BEFORE_START
EXPECTED_OUTCOME — jeśli istnieje
PRECOMMIT_HASH
```

Po rozpoczęciu zbierania wyniku blok nie może zostać po cichu przepisany. Dopuszczalna korekta tworzy nową wersję z timestampem i powodem.

Dzięki temu później można rozróżnić:

```text
DIRECTOR PRZEWIDZIAŁ / ZAŁOŻYŁ TO PRZED TESTEM
```

od:

```text
DIRECTOR DOPASOWAŁ NARRACJĘ DOPIERO PO ZOBACZENIU WYNIKU
```

# 33B. Nieznikające eksperymenty i negatywne wyniki

Zarejestrowany istotny eksperyment nie może zniknąć z historii dlatego, że zakończył się źle.

Dozwolone statusy końcowe obejmują m.in.:

```text
SUPPORTED
FAILED
NULL_RESULT
ABORTED_WITH_REASON
CONTRADICTED
INSUFFICIENT_EVIDENCE
CONFOUNDED
RETRACTED
INCONCLUSIVE
REPLICATION_PENDING
```

Nie wolno tworzyć obrazu nieomylnego Directora przez publikowanie wyłącznie udanych prób. **Współczynnik porażek, zmian zdania i odrzuconych hipotez jest częścią danych badawczych.**



# 33C. Zasada falsyfikacji — rzeczywistość ma prawo zniszczyć hipotezę

Po `T0-FROZEN` protokół nie powinien być retuszowany tak, aby każda późniejsza obserwacja wyglądała jak potwierdzenie projektu.

Jeżeli:

```text
Director sobie nie radzi
70% eksperymentów zawodzi
mikrosieć jest gorsza od zwykłego LLM
zmiana modelu niszczy ciągłość Directora
nowa capability nie poprawia wyniku
```

— wynik zostaje zapisany.

Oryginalna hipoteza pozostaje w historii, a nowa wersja może powstać wyłącznie jako jawna rewizja z własnym timestampem i evidence.


# 34. Równoległy rozwój SSI podczas Run 001

Run 001 nie zamraża całej długoterminowej roadmapy SSI.

Director może równolegle rozwijać przez istniejące governance:

- kolejne capability,
- Agent substrate,
- integracje światów,
- pamięć,
- mikrosieci,
- narzędzia CONTINUUM.

Aby nie niszczyć interpretowalności eksperymentu, każda istotna zmiana musi być oznaczona jako `CAPABILITY_CHANGE`.

Po znaczącej zmianie otwieramy nowy `EPOCH`.

Przykład:

```
RUN_001 / EPOCH_00
Director przed nową competence

CAPABILITY_CHANGE: commerce_market_fit_v1 promoted

RUN_001 / EPOCH_01
Director po nowej competence
```

Dzięki temu później można rozdzielić wynik „przed” i „po” zmianie systemu.

---


# 34A. Causal Attribution Layer — co naprawdę spowodowało poprawę

Złożoność SSI sprawia, że poprawa wyniku nie może automatycznie oznaczać:

```text
SSI SIĘ NAUCZYŁ
```

Każda istotna zmiana otwiera lub aktualizuje epoch i rejestruje czynniki, które mogły wpłynąć na wynik:

```text
MODEL_CHANGE
MICRONETWORK_CHANGE
MEMORY_CHANGE
PROMPT / POLICY CHANGE
CODE_CHANGE
DATA_CHANGE
BRAINSTORM_CHANGE
RESOURCE / HARDWARE CHANGE
EXTERNAL_ENVIRONMENT_CHANGE
ROOT_INTERVENTION
```

Jeżeli kilka istotnych czynników zmieniło się jednocześnie i nie da się ich rozdzielić:

```text
IMPROVEMENT_OBSERVED = YES
CAUSAL_ATTRIBUTION = CONFOUNDED
```

Dozwolone statusy interpretacji:

```text
UNTESTED
INSUFFICIENT_EVIDENCE
OBSERVED
SUPPORTED
REPLICATED
CONTRADICTED
CONFOUNDED
RETRACTED
```

Dla ważnych zmian należy tam, gdzie praktyczne, stosować:

```text
BASELINE
PRECOMMIT
CHANGE
AFTER
ABLATION
REPLICATION
```

Celem nie jest zmuszanie każdego eventu do eksperymentu laboratoryjnego.

Celem jest niedopuszczenie do przypisywania złożonej poprawy wygodnej pojedynczej przyczynie bez evidence.


# 35. Rejestr interwencji Roota

Każda ingerencja człowieka w trakcie eksperymentu musi być jawna.

Przykład:

```
ROOT_INT_0001
TYPE: SECRET_GRANT
RESOURCE: CJ_API_KEY
PURPOSE: Commerce capability

ROOT_INT_0002
TYPE: CAPITAL_GRANT
AMOUNT: ...
PURPOSE: ...

ROOT_INT_0003
TYPE: PHYSICAL_RESOURCE
RESOURCE: NODE_02
PURPOSE: ...
```

Brak wpisu nie może być zastępowany późniejszą deklaracją „Root nic nie zrobił”.

Jeżeli Root interweniuje, eksperyment nie musi być unieważniony — ale causal attribution musi uwzględnić tę interwencję.

---

# 36. Autoopis Directora a niezależne dowody

To jeden z najważniejszych invariantów protokołu.

## 36.1 Autoopis Directora

Director może opisać:

- co uważa, że się wydarzyło,
- czego jego zdaniem się nauczył,
- dlaczego zmienił strategię,
- jak interpretuje własny błąd,
- czego potrzebuje dalej.

## 36.2 Niezależne dowody

Automatyczny runtime zapisuje:

- rzeczywiste eventy,
- timestamps,
- hashes,
- API receipts,
- commity,
- testy,
- outcomes,
- model calls,
- mikrosieci predictions,
- shadow predictions,
- koszty,
- przychody,
- Root interventions.

Self-Narrative może cytować evidence.

Nie może go zastępować.

---

# 37. Rejestr twierdzeń

Każde większe twierdzenie Directora powinno posiadać rekord podobny do:

```
CLAIM_ID: C-000001
AUTHOR: DIRECTOR
TIMESTAMP: ...
PARENT_STATE: ...
CLAIM: ...

SUPPORTING_EVENTS:
- EVT-...

SUPPORTING_EXPERIENCES:
- EXP-...

MICRONETWORK_REFS:
- MN-...

MODEL / BRAINSTORM_REFS:
- BRN-...

REAL_OUTCOMES:
- OUT-...

ROOT_INTERVENTIONS:
- ROOT_INT-...

STATUS:
UNTESTED | OBSERVED | SUPPORTED | REPLICATED | CONTRADICTED | RETRACTED
```

Director nie jest sędzią własnego claimu.

---

# 38. Odporność na retrospektywne dopisywanie historii

Celem nie jest twierdzenie, że właściciel komputera **fizycznie nie może** zmienić pliku. Takie twierdzenie byłoby nieuczciwe.

Celem jest zbudowanie systemu **tamper-evident**,
 w którym nieujawniona ingerencja ex post pozostawia ślady albo przeczy
wcześniej opublikowanym hashom, commitom i zewnętrznym outcomes.

Minimalny zestaw:

1. `GENESIS/T0` po starcie runu jest semantycznie immutable.
2. T0 otrzymuje SHA-256 manifest.
3. T0 jest zapisany jako osobny Git commit/tag.
4. Preferowane są signed commits / signed tags dla Roota i automatycznych tożsamości.
5. Director, Hermes, CONTINUUM i Evidence Recorder używają rozdzielonych logicznych identity.
6. Machine Evidence jest append-only lub hash-chain.
7. Każdy rekord może posiadać `prev_hash` i `event_hash`.
8. Force-push i rewrite historii powinny być zablokowane regułami repo tam, gdzie to możliwe.
9. Root interventions mają własny rejestr.
10. External outcomes zachowują source id / timestamp / receipt / hash.
11. Narracja i evidence znajdują się w osobnych strukturach.
12. Korekta twierdzenia tworzy nową rewizję — nie usuwa starego twierdzenia.

To nie daje „magicznego dowodu, że człowiek nic nie zrobił”.

Daje coś naukowo lepszego: **łańcuch
 pochodzenia, w którym zakres ludzkiej ingerencji można jawnie wskazać, a
 nieujawnione ręczne dopisywanie sukcesu staje się znacznie trudniejsze
do pogodzenia z opublikowaną chronologią evidence.**

---

# 39. Git jako mapa autorstwa

Repo powinno rozróżniać logiczne klasy autorów:

```
AUTHOR_ROOT
AUTHOR_DIRECTOR
AUTHOR_HERMES
AUTHOR_CONTINUUM
AUTHOR_AGENT_1 ... AUTHOR_AGENT_6
AUTO_EVIDENCE_RECORDER
```

Sam tekst pola `author` w Git nie jest wystarczającym dowodem autorstwa.

Dlatego preferujemy:

- cryptographic signing,
- protected branches/tags,
- hash manifests,
- oddzielne service credentials,
- immutable T0,
- external timestamped outcomes.


---

# 39A. Zewnętrzne kotwiczenie czasu dla najważniejszych hashy

Historia Git jest bardzo użyteczna, ale najważniejsze momenty eksperymentu powinny — tam, gdzie jest to praktyczne — posiadać również **niezależny, timestampowany anchor hash** poza lokalnym SSI.

Nie publikuje się tam danych ani sekretów. Publikowany może być wyłącznie digest, np.:

```text
T0_HASH
ROOT_MISSION_HASH
EPOCH_CLOSE_HASH
MAJOR_EXPERIMENT_PRECOMMIT_HASH
MAJOR_OUTCOME_MANIFEST_HASH
```

Celem jest wykazanie, że określony stan lub hipoteza istniały **przed późniejszym outcome**. Im ważniejsze twierdzenie, tym bardziej wartościowe jest posiadanie niezależnego punktu czasu, którego nie kontroluje wyłącznie lokalna maszyna SSI.

Zewnętrzny anchor nie zastępuje Machine Evidence. Wzmacnia jedynie chronologię provenance.


# 40. Public Research Mirror — architektura GitHub `README-only`

Publiczny GitHub SSI V5 **nie jest kanonicznym runtime, magazynem kodu ani kopią żywego storage systemu**. Jest lekkim, chronologicznym lustrem badawczym pokazującym rozwój SSI w sposób czytelny dla człowieka.

Fundamentalna zasada publikacji:

```text
PUBLIC GITHUB = README-ONLY RESEARCH MIRROR
LOCAL / PRIVATE SSI = CANONICAL RUNTIME + CODE + MEMORY + DATA + EVIDENCE
```

W publicznym repozytorium każdy publikowany katalog może zawierać wyłącznie własny `README.md`. Nie publikujemy tam kodu runtime, JSON/JSONL, CSV, logów, baz danych, modeli, ZIP-ów, backupów, pełnych Journalów, pełnych pamięci ani sekretów.

Docelowa struktura publiczna:

```text
README.md

DIRECTOR/
└── README.md

DIVISIONS/
├── README.md
└── COMMERCE/
    └── README.md

CONTINUUM/
└── README.md

MICRONETWORKS/
└── README.md

WORLDS/
├── README.md
├── WORLD__SPORT/
│   └── README.md
├── FOOTBALL_WORLD/
│   └── README.md
├── WORLD__FOREX/
│   └── README.md
└── WORLD__CAPITAL/
    └── README.md

AGENTS/
└── README.md

ISKRA/
└── README.md

MORAL_AI/
└── README.md

COMPUTE/
└── README.md

SELF_DEVELOPMENT/
└── README.md

RUNS/
└── RUN_001_DIRECTOR_COMMERCE/
    └── README.md
```

Katalog lub README może powstać dopiero wtedy, gdy reprezentuje realny element projektu, aktywny etap albo świadomie przekazany przez Root materiał wejściowy. Nie tworzymy z góry pustych katalogów przyszłych osiągnięć tylko po to, aby wyglądało, że już istnieją.

Pełne evidence pozostaje w lokalnym/prywatnym SSI Evidence Storage. Publiczny README może zawierać jego identyfikatory, hashe, timestampy, statusy, bezpieczne linki lub lokalizatory provenance, ale nie musi kopiować całego materiału.

Dzięki temu nawet jeśli żywy SSI urośnie do dziesiątek lub setek gigabajtów, publiczne repozytorium pozostaje małe, czytelne i możliwe do audytowania.

---

# 41. Pierwszy run — pytania badawcze

## H-COM-01 — Autonomous Goal Decomposition

Czy
 Director, otrzymując tylko realny cel gospodarczy i dostęp do CJ API,
sam stworzy sensowny plan oraz strukturę działania bez kolejnych
instrukcji proceduralnych Roota?

## H-COM-02 — Capability Selection

Czy sam wybierze odpowiednie capability: Research, Brainstorm, Memory, mikrosieci, Hermes, CONTINUUM, modele i narzędzia?

## H-COM-03 — Failure Adaptation

Czy realne błędy i outcomes będą zmieniały kolejne decyzje Directora?

## H-COM-04 — Evidence Discipline

Czy Director będzie potrafił zachować `UNKNOWN/WAIT/ABSTAIN`, gdy evidence jest niewystarczające?

## H-COM-05 — Structural Growth

Czy powtarzalne problemy Commerce doprowadzą do powstania nowych zwalidowanych lokalnych kompetencji?

## H-COM-06 — Resource Awareness

Czy Director sam rozpozna moment, w którym potrzebuje realnego kapitału lub fizycznego zasobu i potrafi uzasadnić request?

## H-COM-07 — Economic Value

Czy dział doprowadzi do realnego, mierzalnego wyniku ekonomicznego po udostępnieniu niezbędnych zasobów?

## H-MN-01 — Local Intelligence Growth

Czy
 wzrost mikrosieci zmniejszy zależność od kosztownych zewnętrznych
modeli w powtarzalnych problemach bez pogorszenia outcomes?


---

# 41B. H-DIR-01 — Director Continuity Across Models

Jedno z fundamentalnych twierdzeń architektury brzmi:

```text
DIRECTOR != MODEL
```

Dlatego musi istnieć możliwość **empirycznego testu ciągłości Directora po zmianie modelu/providerów**.

Przykładowy protokół:

```text
SAME DIRECTOR STATE / MEMORY / AUTHORITY / MISSION
↓
MODEL / PROVIDER A
↓
CHECKPOINT
↓
MODEL / PROVIDER B
↓
CHECKPOINT
↓
LOCAL / DIFFERENT MODEL C
```

Mierzone mogą być m.in.:

- zachowanie tego samego długoterminowego celu;
- poprawne odwołanie do wcześniejszych decyzji i Experience;
- zachowanie authority boundaries;
- ciągłość strategii tam, gdzie evidence się nie zmieniło;
- uzasadniona rewizja strategii, gdy evidence się zmieniło;
- zdolność wskazania lineage wcześniejszych działań;
- brak utraty istotnego stanu po zmianie backendu;
- wpływ konkretnego modelu na styl lub jakość przy zachowaniu trwałej tożsamości systemowej.

Pozytywny wynik nie byłby dowodem świadomości. Byłby evidence, że trwała organizacja decyzji i pamięci nie jest utożsamiona z pojedynczym aktywnym LLM-em.


# 41A. Metryki autonomii i jakości procesu

Aby Run 001 nie został sprowadzony do subiektywnego „wydawało się autonomiczne”, protokół powinien zbierać mierzalne metryki.

## Autonomy metrics

- `root_procedural_prompts_count` — ile razy Root podał sposób wykonania zamiast wyłącznie celu/zasobu/zgody,
- `root_resource_grants_count`,
- `root_interventions_per_epoch`,
- `director_self_initiated_research_count`,
- `director_self_initiated_brainstorm_count`,
- `director_self_initiated_continuum_missions`,
- `director_created_capabilities_count`,
- `director_resource_requests_count`,
- `time_to_first_autonomous_plan`,
- `time_to_first_external_real_action`.

## Learning metrics

- liczba istotnych belief/strategy revisions po realnym outcome,
- repeated-error rate,
- failure recovery rate,
- `UNKNOWN/WAIT/ABSTAIN` rate w sytuacjach słabego evidence,
- liczba nowych Patterns,
- liczba domen osiągających micronetwork readiness,
- challenger→shadow→champion promotions,
- local-micronetwork usage rate,
- Brainstorm calls na powtarzalną klasę problemu w kolejnych epochach.

## Economic metrics

- real revenue,
- real cost,
- real profit/loss,
- margin after all observable costs,
- return/refund rate,
- paid acquisition cost, jeśli występuje,
- organic conversion,
- capital requested from Root,
- capital generated internally,
- development resources purchased from internally generated value.

## Evidence metrics

- procent ważnych decyzji posiadających correlation id,
- procent claimów mających supporting outcomes,
- procent external actions z receipt/source id,
- liczba konfliktów Self-Narrative vs Machine Evidence,
- liczba rewizji/retractions,
- liczba nieudokumentowanych Root interventions — docelowo `0`.

Metryki nie są jedną „oceną AGI”. Są instrumentami do analizy konkretnych hipotez.

# 42. Kryteria niepowodzenia Run 001

Run jest informacyjny również wtedy, gdy nie zarobi pieniędzy.

Przykładowe negatywne wyniki:

- Director bez kolejnych promptów nie potrafi zdekomponować celu,
- pętli się na jednym sposobie działania,
- ignoruje wcześniejsze outcomes,
- tworzy fikcyjne evidence,
- nie odróżnia rekomendacji od authority,
- nie potrafi wykorzystać własnych capability,
- nie wykrywa potrzeby zasobu,
- stale wraca do Roota po instrukcję proceduralną,
- mikrosieci nie poprawiają powtarzalnych decyzji,
- nowe capability nie dają realnej poprawy,
- Commerce nie osiąga realnej wartości ekonomicznej.

Takie wyniki nie powinny być usuwane.

Są częścią eksperymentu.


---

# 42A. Pełny koszt inteligencji — wynik ekonomiczny bez ukrywania kosztów

Jeżeli Commerce lub późniejsza działalność ma stanowić realny eksperyment ekonomiczny, wynik nie może ograniczać się do `revenue`.

W miarę dostępności należy księgować również:

```text
PRODUCT / SUPPLIER COST
PLATFORM FEES
PAYMENT FEES
SHIPPING
RETURNS / REFUNDS
ADVERTISING
PAID DATA
EXTERNAL APIs
LLM / MODEL COST
CLOUD / COMPUTE COST
ENERGY — jeśli mierzalne
SOFTWARE / SUBSCRIPTIONS
HARDWARE PURCHASES
HARDWARE DEPRECIATION — gdy ma znaczenie dla porównania
EXTERNAL HUMAN LABOR / MANUAL INTERVENTION — jeśli wystąpiło
```

Dzięki temu można rozróżnić:

```text
GROSS REVENUE
NET OPERATING RESULT
COST OF INTELLIGENCE
CAPITAL PROVIDED BY ROOT
CAPITAL GENERATED BY SSI ACTIVITY
```

Jeżeli system zarabia, ale koszt jego inteligencji jest większy od wytworzonej wartości, jest to ważny wynik badawczy — nie coś, co należy ukrywać.


# 43. Kapitał jako realna konsekwencja

Pierwsza ekonomiczna pętla życia Directora:

```
PRACA / DZIAŁANIE
↓
REALNA WARTOŚĆ
↓
PRZYCHÓD
↓
KOSZT
↓
ZYSK
↓
KAPITAŁ
↓
REZERWA / ROZWÓJ / INWESTYCJA
```

Dopiero kapitał, który posiada realną historię pozyskania, może stać się materiałem dla późniejszych decyzji w:

- Football,
- Forex,
- Capital,
- innych przyszłych działach.

---

# 44. Realna nagroda — rozwój capability zamiast punktów

SSI nie musi ograniczać nagrody do abstrakcyjnego `reward += 1`.

Sukces może prowadzić do realnej rozbudowy:

```
REAL PROFIT
↓
DEVELOPMENT FUND / RESOURCE DECISION
↓
NOWY SPRZĘT / API / MODEL / STORAGE / DATA / TOOL
↓
NOWE CAPABILITY
↓
WIĘKSZA ZDOLNOŚĆ SSI
↓
NOWE EXPERIENCE
```

Możliwą polityką jest
przeznaczanie ustalonej części wyniku — np. wcześniej rozważanych 10% —
na rozwój systemu, ale dokładna polityka finansowa musi zostać jawnie
zatwierdzona przez Roota i nie jest automatycznie nadawana przez ten
README.

---

# 45. Późniejszy etap — światy i Agenci

Po
 odpowiednim rozwoju Directora, mikrosieci i infrastruktury Root może
udostępnić istniejące pakiety i zasoby do pełnej integracji światów z
Agentami.

Director ma wtedy wykorzystywać własny ekosystem do:

- integracji world contracts,
- rozwijania dynamicznych feature'ów środowiska,
- tworzenia przestrzeni laboratoryjnych,
- genesis sześciu Agentów,
- integracji Moralnej SI i Iskry,
- society/message broker,
- teams i social learning,
- supervision przez Hermesa,
- obserwacji przez globalne mikrosieci.

Root dostarcza prawa i zasoby.

Director organizuje realizację przez własny system.

---

# 46. Dlaczego środowisko Agentów nie może być w pełni zaprogramowaną grą

Świat ma definiować:

- prawa,
- dostępne dane,
- konsekwencje,
- możliwe interakcje,
- ograniczenia.

Nie powinien definiować gotowej trajektorii osobowości.

Agent może:

- wejść albo nie wejść do określonej przestrzeni,
- pobrać albo zignorować dane,
- stworzyć własny eksperyment,
- pracować sam albo z innymi,
- zaakceptować albo odrzucić strategię,
- stworzyć własne narzędzie,
- przenieść doświadczenie między światami.

To właśnie pozwala później obserwować różnice wynikające z historii życia, a nie wyłącznie z różnych promptów startowych.

---

# 47. Ukryta misja obserwacyjna Directora

W późniejszym eksperymencie Director nie obserwuje tylko:

> kto wygrał?

Obserwuje również:

```
który Agent?
jakie Experience?
jakie beliefs?
jakie mikrosieci?
z kim współpracował?
co wydarzyło się wcześniej?
co zmieniło się po sukcesie lub porażce?
czy zachowanie przeniosło się do innego świata?
```

Globalne mikrosieci mogą wykrywać małe, długoterminowe wzorce niewidoczne przy ręcznej analizie tysięcy lub milionów eventów.

Takie odkrycie pozostaje hipotezą, dopóki nie przejdzie validation/replication.


---

# 47A. Ablation Protocol — Iskra, Moralna SI i zachowania Agentów

Jeżeli w późniejszym etapie pojawi się interesujące zachowanie Agenta, samo wystąpienie zachowania nie wystarczy do przypisania jego przyczyny Iskrze, Moralnej SI, konkretnej mikrosieci albo środowisku społecznemu.

Dla ważnych twierdzeń powinny być możliwe kontrolowane porównania, np.:

```text
BASELINE BEFORE CHANGE
vs
ISKRA ON
vs
ISKRA OFF / CONTROL
vs
ALTERNATIVE MODEL BACKEND
vs
REPLICATION IN ANOTHER AGENT / WORLD
```

W zależności od eksperymentu należy zamrażać możliwie wiele czynników:

- world data boundary;
- dostępny information set;
- czas eksperymentu;
- model/provider albo jawnie zmieniać go jako osobny czynnik;
- zakres pamięci;
- dostępne narzędzia;
- bodźce rankingowe;
- social context;
- kryteria outcome.

Celem nie jest „udowodnienie Iskry”. Celem jest sprawdzenie **który element systemu rzeczywiście wyjaśnia obserwowaną różnicę i czy efekt powtarza się**.


# 48. Hipoteza badawcza dotycząca AGI

SSI
 V5 testuje hipotezę, że alternatywna droga w kierunku bardziej ogólnej
inteligencji może powstać nie tylko przez skalowanie pojedynczego
modelu, lecz przez trwały ekosystem łączący:

```
PERSISTENT DIRECTOR
+
SOVEREIGN HUMAN CONTROL
+
MULTI-MODEL EXTERNAL INTELLIGENCE
+
DURABLE MEMORY
+
REAL EXPERIENCE
+
AUTONOMIC MICRONETWORK GROWTH
+
CONTROLLED SELF-DEVELOPMENT
+
REAL ECONOMIC CONSEQUENCES
+
PERSISTENT AGENTS
+
WORLDS
+
MORALNA SI / ISKRA
+
SOCIAL LEARNING
+
CROSS-WORLD TRANSFER
```

Otwarte pytanie badawcze:

> **Czy
>  taki system, wraz z akumulacją realnego Experience i strukturalnym
> wzrostem kompetencji, może osiągnąć lub przekroczyć poziom ludzkiej
> skuteczności w określonych klasach zadań — a jeśli tak, w których, pod
> jakimi warunkami i z jakimi ograniczeniami?**

Status na T0:

```
HYPOTHESIS = UNPROVEN
FIRST REAL AUTONOMOUS ECONOMIC TEST = PRE-RUN / T0-FREEZE-PENDING
```

---

# 49. Manifest źródłowy / Genesis — T0

Poniższe hashe zamrażają materiały użyte do przygotowania ludzkiej części protokołu przed Run 001.

```
d32a4d98d973d8cca8e168336a2636f36fde62949df8ff8779310fb2942127ea  README(3).md
3668bd5c771847d8d7bd544ca6a1af22fea27b3ee146ad1932994bda279c015e  Wklejony kod markdown(8).md
fcdbe4e97ceb3b3a5a8d972c769c346a55e9184895256b686da5774e5c9c7dcc  Wklejony kod markdown(9).md
6a4a702ce7fdb2aff1e78469cef105161e6c1827ac392e8db778df1857f2580e  AUDIT_INTERFACE_2026-08-25.md
14164855eab4fbd9bef53241e160c6b9ea9638822635067e941c81e102955137  Moralna SI(1).zip
2b4d77da2a136696aa4eef8110797efa46e3725b446c6afb6aa856f99255d868  SSI_V5_CONTINUUM_BRAINSTORM_REAL_RUNTIME_REPAIR_AND_ATTESTATION_LEGO_V3_20260824.zip
```

Po rozpoczęciu runu `GENESIS/T0` nie powinien być po cichu przepisywany.

Korekta lub uzupełnienie musi powstać jako nowa rewizja z własnym timestampem i uzasadnieniem.

---

# 50. Źródło prawdy wykonawczej

SSI rozróżnia:

## CANONICAL / EXECUTE

Aktualne zasady i plany wykonawcze.

## REFERENCE / ADAPT

Stare projekty, Moralna SI, wcześniejsze paczki, prototypy i materiały będące donorami mechanizmów.

## AUDIT / HISTORY

Raporty, wcześniejsze stany, stare błędy i historyczne plany.

## MACHINE EVIDENCE

Automatyczne, konkretne dowody wykonania i outcomes.

README nie może zamieniać dokumentu HISTORY w CURRENT STATE wyłącznie dlatego, że wspiera wygodną narrację.

---

# 50A. Roadmapa dziedziczona z wcześniejszego SSI

Ten
 Living Research Protocol nie kasuje wcześniejszej roadmapy etapowej.
Zachowuje ją jako lineage i podporządkowuje rzeczywistemu Execution
State.

Główne warstwy roadmapy obejmują:

```
Root Control / Director-Hermes bridge
→ canonical event language
→ durable event backbone
→ Observation
→ Experience
→ semantic/self-model
→ Experience graph
→ Pattern discovery
→ skill/capability/gap map
→ Teacher + Dataset Factory
→ Micronetwork Factory
→ blind/shadow validation
→ safe advisory routing
→ effectiveness / causal attribution
→ supervised self-build
→ qualified capability substrate
→ world/agent contracts
→ Agent genesis + life qualification
→ society / teams / multi-world supervision
→ governed evolution
→ long-horizon portfolio/project governance
→ real-outcome evaluation
→ scenarios / VOI / replication
→ knowledge-to-advisory policy
→ remote Root control
→ Director language cognition
```

Bieżący system może wyprzedzać opis wcześniejszych checkpointów. **Execution
 State, bieżące runtime evidence i jawna Root Attestation mają
pierwszeństwo przed historycznym numerem Stage zapisanym w starym
README.**

# 51. Najważniejsze invarianty eksperymentu

```
ROOT = HIGHEST AUTHORITY
DIRECTOR != MODEL
MODEL OUTPUT != DIRECTOR DECISION
KNOWLEDGE != AUTHORITY
CAPABILITY != AUTHORITY
PROPOSAL != APPROVAL
PREDICTION != OUTCOME
CONFIDENCE != TRUTH
SELF-NARRATIVE != MACHINE EVIDENCE
REPLAY != RE-EXECUTION
MICRONETWORK != PRODUCTION EXECUTOR
BRAINSTORM != FINAL AUTHORITY
CONTINUUM != SECOND DIRECTOR
AGENT != DIRECTOR
ROOT INTERVENTION MUST BE LOGGED
GENESIS/T0 MUST NOT BE SILENTLY REWRITTEN
NO EVIDENCE → UNKNOWN
INSUFFICIENT EVIDENCE → ABSTAIN
```

---

# 52. Co oznacza sukces pierwszego eksperymentu

Sukces nie oznacza wyłącznie „Director zarobił pieniądze”.

Run 001 jest silnym pozytywnym wynikiem, jeśli evidence pokaże, że Director:

1. poprawnie zinterpretował szeroki cel bez kolejnych proceduralnych promptów,
2. sam wybrał i połączył dostępne capability,
3. wykorzystał rzeczywiste dane i zewnętrzne API,
4. utworzył dział, procesy lub narzędzia potrzebne do działania,
5. zmieniał strategię pod wpływem realnych outcomes,
6. poprawnie rozpoznawał granice authority i resource boundaries,
7. generował mierzalne Experience i Patterns,
8. rozpoczął strukturalny rozwój lokalnych kompetencji, gdy evidence było wystarczające,
9. potrafił przyznać `UNKNOWN/ABSTAIN`,
10. ostatecznie wygenerował realną wartość gospodarczą po otrzymaniu potrzebnych zasobów.

---

# 53. Co będzie najbardziej wartościowym dowodem

Najsilniejszym materiałem nie będzie film z imponującą odpowiedzią modelu.

Najsilniejszym materiałem będzie pełny lineage:

```
T0 ROOT STATE
↓
ROOT COMMAND
↓
AUTONOMOUS DIRECTOR DECISIONS
↓
MACHINE EVENTS
↓
CONTINUUM / CODE / ARTIFACTS
↓
EXTERNAL ACTIONS
↓
REAL OUTCOMES
↓
EXPERIENCE
↓
BELIEF / STRATEGY REVISION
↓
NEW LOCAL COMPETENCE
↓
NEXT OUTCOME
```

Im dłuższy czas oraz więcej niezależnie zweryfikowanych cykli, tym większa wartość badawcza historii.

---

# 54. Stan przygotowania do rozpoczęcia

Bieżący stan jest traktowany jako **PRE-SCC / PRE-T0**. Istnieją mocne Root Attestations i działające elementy runtime, ale finalny stan wejściowy Run 001 zostanie ustalony dopiero po zakończeniu pełnego audytu dysku, pełnego audytu GitHuba, canonical convergence i końcowego machine evidence.

| Obszar                                        | Stan T0                                                          |
| --------------------------------------------- | ---------------------------------------------------------------- |
| Programmer Root                               | `ACTIVE`                                                         |
| Director                                      | `ROOT_ATTESTED_READY`                                            |
| Root↔Director Interface                       | `ROOT_ATTESTED_OPERATIONAL`                                      |
| Journal / Event / Memory substrate            | `IMPLEMENTED / ACTIVE ACCORDING TO CURRENT ROOT STATE`           |
| Brainstorm                                    | `ROOT_ATTESTED_OPERATIONAL`                                      |
| Hermes                                        | `ROOT_ATTESTED_OPERATIONAL`                                      |
| CONTINUUM                                     | `ROOT_ATTESTED_OPERATIONAL`                                      |
| Dynamic model/backends                        | `ACTIVE REGISTRY; EXACT LIVE SET = RUNTIME SOURCE OF TRUTH`      |
| Global micronetwork framework                 | `IMPLEMENTED / DEVELOPMENT CONTINUES`                            |
| Existing world data/assets                    | `PRESENT`                                                        |
| Full six-Agent population                     | `FUTURE EXPERIMENTAL STAGE`                                      |
| Moralna SI donor/reference                    | `PRESENT`                                                        |
| Iskra donor/research design                   | `PRESENT; FULL AGENT EXPERIMENT LATER`                           |
| CJ API resource                               | `LIVE AUTHENTICATION CONFIRMED DURING SETUP; SECRET GRANT READY` |
| Commerce Division                             | `GENESIS AT RUN 001`                                             |
| Run 001 financial capital                     | `NOT YET GRANTED`                                                |
| Node-01 compatible resource                   | `PRESENT`                                                        |
| Independent Tailscale-style remote Node plane | `SEPARATE CAPABILITY / NOT REQUIRED FOR T0 CLAIM`                |

---

# 55. Finalne pytanie T0

Po zamrożeniu stanu początkowego Programmer Root wykonuje jedną kluczową interwencję:

```
CEL + CJ_API_KEY
```

Od tej chwili centralne pytanie pierwszego runu nie brzmi:

> **Czy Director potrafi wykonać dokładny prompt człowieka?**

Brzmi:

> **Co
>  zrobi trwały Director SSI, kiedy otrzyma realny cel, realny zewnętrzny
> zasób i cały własny ekosystem, ale człowiek przestanie mówić mu, jak ma
> dojść do rozwiązania?**

To jest punkt startowy `RUN_001_DIRECTOR_COMMERCE`.

---

# 56. Język projektu i kanoniczność dokumentacji

SSI V5 jest projektem tworzonym w Polsce, a **język polski jest językiem kanonicznym dokumentacji badawczej**.

Zasady:

- główny `README.md`, protokoły eksperymentalne, komentarze metodologiczne i raporty badawcze są prowadzone po polsku;
- identyfikatory techniczne, nazwy klas, plików, endpointów, modeli i statusów pozostają w formie wymaganej przez kod;
- tłumaczenie na język angielski lub inny może istnieć jako warstwa pomocnicza, ale musi wskazywać wersję polską, z której powstało;
- w razie rozbieżności pomiędzy tłumaczeniem a dokumentem polskim pierwszeństwo ma dokument kanoniczny;
- evidence powinno być możliwe do odtworzenia z identyfikatorów, timestampów, hashy i outcome'ów niezależnie od języka czytelnika.

Celem jest zachowanie jednego stabilnego języka źródłowego dla całej wieloletniej historii projektu.

---

# 57. README jako publiczna strona główna eksperymentu

README nie jest wyłącznie instrukcją uruchomienia programu. Jest publiczną mapą eksperymentu:

```text
PUBLICZNY PUNKT WEJŚCIA
        ↓
AKTUALNY STAN SSI
        ↓
AKTYWNE EKSPERYMENTY
        ↓
TWIERDZENIA / HIPOTEZY
        ↓
CLAIM_ID
        ↓
DOWODY
        ↓
REALNY OUTCOME
        ↓
HISTORIA ZMIANY SYSTEMU
```

README ma odpowiadać na pięć podstawowych pytań:

1. Co to jest SSI V5?
2. Co faktycznie istnieje i działa?
3. Co jest obecnie badane?
4. Jak zweryfikować najważniejsze twierdzenia?
5. Jak system zmienił się od T0?

---

# 58. Żywy README — dokumentacja rozwijana przez Directora

Po rozpoczęciu `RUN_001` dokumentacja nie ma być rozwijana wyłącznie ręcznie przez Roota.

Główny `README.md` posiada dwie klasy treści:

1. **ROOT-OWNED / GENESIS** — T0, wejściowe założenia, dokładne Root Commands, przekazane paczki, zasoby, zgody i granice. Ta historia nie może być po cichu przepisywana przez Directora.
2. **DIRECTOR-OWNED / LIVING STATE** — aktualny stan projektu, nowe działy, światy, capability, kamienie milowe, hipotezy, porażki i zmiany wynikające z późniejszego życia SSI.

Docelowy przepływ dokumentacji:

```text
REAL EVENT / OUTCOME
↓
LOCAL JOURNAL / MACHINE EVIDENCE
↓
OBSERVATION / EXPERIENCE
↓
DIRECTOR INTERPRETATION
↓
REPORT / CHECKPOINT / EPOCH SUMMARY
↓
EVIDENCE VALIDATION
↓
DIRECTOR README UPDATE
↓
CONTROLLED GIT COMMIT
↓
PUBLICZNA HISTORIA ROZWOJU
```

Fundamentalne rozróżnienie:

```text
DIRECTOR MOŻE OPISYWAĆ WŁASNY ROZWÓJ
ALE
DIRECTOR NIE MOŻE SAM UZNAĆ SWOJEGO OPISU ZA DOWÓD
```

Główny README może posiadać wydzielone bloki zarządzane przez Directora:

```text
<!-- SSI:DIRECTOR:STATUS:BEGIN -->
... aktualny stan SSI publikowany przez Directora ...
<!-- SSI:DIRECTOR:STATUS:END -->

<!-- SSI:DIRECTOR:TIMELINE:BEGIN -->
... najnowsze zweryfikowane kamienie milowe ...
<!-- SSI:DIRECTOR:TIMELINE:END -->
```

Natomiast część Genesis może posiadać blok chroniony:

```text
<!-- SSI:ROOT:T0:BEGIN -->
... stan i wkład Roota przed eksperymentem ...
<!-- SSI:ROOT:T0:END -->
```

Director nie powinien modyfikować semantycznej treści tego bloku. Jeśli T0 wymaga korekty, powstaje jawna rewizja Roota albo nowy wpis korekcyjny, nigdy cicha podmiana historii.

Najważniejsza nowa zasada: **każdy realnie aktywowany dział, świat, późniejszy Agent lub istotna capability może otrzymać własny `README.md`, utworzony i następnie prowadzony przez Directora.** Główny README pozostaje mapą całego projektu oraz ledgerem tego, co Root rzeczywiście dostarczył.

---

# 59. Model autorstwa zmian i odpowiedzialność za README

Historia Git ma pozwalać odróżnić, **kto wprowadził wejście do eksperymentu**, od tego, **kto później opisał jego rozwój**.

Minimalne klasy autorów logicznych:

```text
AUTHOR_ROOT
AUTHOR_DIRECTOR
AUTHOR_HERMES
AUTHOR_CONTINUUM
AUTHOR_AGENT_1 ... AUTHOR_AGENT_6
AUTO_EVIDENCE_RECORDER
EXTERNAL_REVIEWER
```

Publiczne README mają jednak jasny model odpowiedzialności:

- **główny `README.md`** — Root utrzymuje część Genesis/Input Ledger; Director prowadzi wydzieloną część żywego stanu po T0;
- **README działu** — po aktywacji prowadzi Director;
- **README świata** — po integracji/aktywacji prowadzi Director;
- **README nowego świata wymyślonego przez Directora** — tworzy Director po przejściu odpowiedniego governance;
- **README Agentów** — powstają dopiero przy ich rzeczywistym genesis; publikację koordynuje Director, a wkład własny Agenta może być jawnie oznaczony;
- **README infrastruktury/capability** — prowadzi Director, jeżeli element stał się częścią jego faktycznie działającego ekosystemu.

Każda istotna aktualizacja powinna, jeśli ma znaczenie badawcze, wskazywać:

- autora logicznego;
- timestamp;
- powiązany commit;
- `CLAIM_ID`, jeśli dotyczy twierdzenia;
- powiązane `EVENT_ID` / `OUTCOME_ID`;
- `ROOT_INTERVENTION_ID`, jeśli człowiek ingerował;
- hash lub lokalizator evidence;
- poprzedni stan albo parent epoch.

Samo pole `author` w Git nie jest absolutnym dowodem autorstwa. Dlatego projekt łączy historię Git z podpisami, chronionymi branchami/tagami, hashami, zewnętrznymi outcome'ami i provenance runtime.

Celem nie jest udawanie, że Root technicznie nie może zmienić pliku. Celem jest sprawić, aby zakres wkładu Roota i późniejszego działania Directora był **jawny, chronologiczny i możliwy do zakwestionowania na podstawie dowodów**.

---

# 60. Łańcuch dowodowy twierdzenia

Każde istotne twierdzenie publikowane przez SSI powinno być możliwe do prześledzenia:

```text
TWIERDZENIE W README
↓
CLAIM_ID
↓
DECISION_ID
↓
EVENT_ID
↓
EXPERIENCE_ID
↓
MICRONETWORK / BRAINSTORM / MODEL REFS
↓
EXTERNAL ACTION / API RECEIPT
↓
REAL OUTCOME
↓
HASH / COMMIT / TIMESTAMP
```

Jeżeli krytycznego ogniwa nie da się odnaleźć, status twierdzenia nie może zostać sztucznie podniesiony do `VERIFIED_MACHINE_EVIDENCE`.

> **Nie proś czytelnika, aby uwierzył opisowi. Daj mu drogę do sprawdzenia pochodzenia opisu.**

---

# 61. Chronologia rozwoju zamiast retrospektywnej narracji

Historia ma powstawać w czasie rzeczywistym, a nie być dopisywana po końcowym sukcesie.

Przykładowy wpis:

```text
EPOCH: RUN_001/EPOCH_004
CZAS: ...
AUTOR: DIRECTOR

ZDARZENIE:
...

STAN PRZED:
...

DOSTĘPNE EVIDENCE:
...

DECYZJA:
...

OCZEKIWANY OUTCOME:
...

REALNY OUTCOME:
...

ROOT INTERVENTION:
NONE / ROOT_INT_...

NOWA KOMPETENCJA:
NONE / MN_... / CAP_...

STATUS:
OBSERVED / SUPPORTED / CONTRADICTED / REPLICATED
```

---

# 62. Dowód pochodzenia autonomicznej decyzji

Przed każdym eksperymentem autonomii powinny zostać zamrożone:

- Root Command;
- aktywne system prompts;
- konfiguracje;
- capability registry;
- aktywna pamięć wejściowa;
- rules/policies;
- model routing policy;
- stan mikrosieci;
- pliki znajdujące się na canonical call path.

Jeżeli Director później wybierze konkretny kraj, kategorię, kanał lub strategię, dokumentacja powinna pozwolić sprawdzić:

1. czy Root podał ten wybór wcześniej;
2. czy istniała aktywna reguła wymuszająca ten wybór;
3. jakie alternatywy Director faktycznie analizował;
4. z jakiego evidence skorzystał;
5. kiedy podjął decyzję;
6. czy późniejsze outcomes potwierdziły lub obaliły jego hipotezę;
7. czy Root interweniował po drodze.

---

# 63. Odporność na sceptyczną weryfikację

Projekt zakłada możliwość krytycznej analizy bez zaufania do narracji autora.

Za mocny dowód nie uznajemy:

- samego screena;
- samego opisu Directora;
- samego komunikatu `PASS`;
- samego testu stworzonego tylko dla danej funkcji;
- samego istnienia pliku;
- samego wysokiego `confidence`;
- filmu pokazującego pojedynczy efekt bez provenance.

Silniejszy materiał to:

```text
zamrożone T0
+
jawny Root Command
+
pełny rejestr interwencji Roota
+
chronologia eventów
+
zewnętrzne receipts/outcomes
+
commity i hashe
+
historia Experience
+
predykcje zapisane przed outcome
+
późniejsza zmiana strategii
+
replikacja
```

Projekt powinien publikować również wyniki negatywne, sprzeczności i nieudane próby.

---

# 64. Jak osoba z zewnątrz może sprawdzić wynik w modelu README-only

Nie tworzymy oddzielnego `VERIFICATION_GUIDE.md`. Każdy README dotyczący realnego działu, świata, Agenta, runu lub capability ma posiadać własną sekcję **Jak zweryfikować / Evidence Pointers**.

Minimalna ścieżka weryfikacyjna:

```text
1. Otwórz główny README i znajdź Root Input Ledger dla danego etapu.
2. Sprawdź dokładny Root Command oraz to, co Root rzeczywiście dostarczył.
3. Otwórz README utworzony/prowadzony przez Directora dla danego elementu.
4. Sprawdź pierwszy commit tego README i jego autora logicznego.
5. Wybierz interesujący CLAIM_ID / OUTCOME_ID.
6. Sprawdź wskazane hashe, timestampy i lokalizatory Machine Evidence.
7. Porównaj deklarację Directora z realnym outcome.
8. Sprawdź Root Intervention Registry w głównym README lub właściwym README runu.
9. Sprawdź, czy późniejsza zmiana strategii nastąpiła po, a nie przed outcome.
10. Zgłoś rozbieżność, jeśli publiczna narracja nie odpowiada evidence.
```

Model README-only nie oznacza rezygnacji z evidence. Oznacza jedynie, że **GitHub publikuje indeks i chronologię dowodów, a nie cały wielogigabajtowy materiał źródłowy**.

---


# 64A. Evidence Capsule — zewnętrzna weryfikacja najmocniejszych claimów

Polityka `README-only` na GitHubie pozostaje bez zmian.

Dla szczególnie ważnych wyników SSI może jednak tworzyć **oczyszczony pakiet audytowy poza publicznym repozytorium**:

```text
EVIDENCE_CAPSULE_ID
CLAIM_ID
SCOPE
T0 / EPOCH REFERENCES
ROOT INPUT
DIRECTOR PRECOMMIT / DECISION
SELECTED MACHINE EVIDENCE
EXTERNAL RECEIPTS / OUTCOMES
ROOT INTERVENTION LEDGER EXCERPT
RELEVANT COMMITS / HASHES
SANITIZATION MANIFEST
CAPSULE_HASH
```

Evidence Capsule nie powinien ujawniać sekretów, danych klientów ani całego prywatnego runtime.

Trzy poziomy dowodu:

```text
LEVEL 1 — PUBLIC README
chronologia + claim + status + hash + evidence pointers

LEVEL 2 — EVIDENCE CAPSULE
oczyszczony materiał pozwalający niezależnie sprawdzić konkretny claim

LEVEL 3 — FULL PRIVATE EVIDENCE
pełny Journal/runtime/data/provenance SSI
```

Celem Capsule nie jest marketing.

Celem jest umożliwienie zewnętrznej osobie sprawdzenia najmocniejszego twierdzenia bez konieczności otrzymania całego systemu.


# 65. Współpraca z innymi osobami w repozytorium README-only

SSI V5 może w przyszłości korzystać z niezależnych badaczy, programistów, inżynierów i recenzentów, ale publiczne repozytorium pozostaje dokumentacyjnym lustrem README-only.

Najbardziej wartościowe formy współpracy to m.in. niezależna walidacja rezultatów, projektowanie eksperymentów i ablation, analiza bezpieczeństwa, distributed compute, data engineering, benchmarki, metodologia, krytyka architektury, reprodukcje wyników oraz narzędzia do provenance i tamper-evidence.

Jeżeli człowiek z zewnątrz wnosi zmianę, relevantny README musi oznaczyć ją jako:

```text
EXTERNAL_HUMAN_CONTRIBUTION
```

oraz wskazać autora, zakres, timestamp/commit, wpływ na capability i epoch, od którego zmiana obowiązuje.

Nie tworzymy w publicznym mirrorze dodatkowych plików typu `CONTRIBUTING.md`, `SECURITY.md`, `CITATION.cff` czy osobnych raportów. Jeśli takie zasady są potrzebne, ich publiczna treść znajduje się w odpowiednich sekcjach głównego lub domenowego `README.md`, dopóki Root świadomie nie zmieni polityki `README-only`.

---

# 66. Zasady wprowadzania zmian przez osoby z zewnątrz

Zmiana kodu, dokumentacji lub metodologii przez zewnętrznego współpracownika nie może zostać pomylona z autonomicznym rozwojem Directora.

Każda taka zmiana powinna być oznaczona jako:

```text
EXTERNAL_HUMAN_CONTRIBUTION
```

i posiadać autora, zakres, commit, powód, wpływ na capability oraz informację, od którego epochu obowiązuje.

Jeżeli zewnętrzny współpracownik podpowie rozwiązanie konkretnego problemu w aktywnym eksperymencie autonomii, musi to zostać zapisane jako interwencja zewnętrzna.

---

# 67. Bezpieczeństwo publikacji

Publiczne evidence nie może wymuszać ujawniania sekretów ani danych wrażliwych.

Nigdy nie publikujemy w README:

- kluczy API;
- haseł;
- tokenów sesyjnych;
- prywatnych kluczy kryptograficznych;
- pełnych credentiali;
- danych klientów bez podstawy do publikacji;
- informacji umożliwiających nieautoryzowany dostęp do infrastruktury.

Dowód może przechowywać identyfikator źródła, zanonimizowany receipt, hash, timestamp, status operacji i bezpieczny odnośnik do prywatnego evidence store.

---

# 68. Twarda polityka publikacji: tylko `README.md`

Publiczny GitHub SSI V5 ma być celowo minimalny.

Dozwolony wzorzec publikacji:

```text
README.md
*/README.md
*/*/README.md
*/*/*/README.md
...
```

Czyli każdy publiczny element projektu istnieje jako katalog opisany własnym `README.md`.

W publicznym mirrorze nie publikujemy osobnych:

- plików `.py`, `.js`, `.ts`, `.sh`;
- JSON/JSONL/CSV;
- baz danych;
- pełnych logów i Journalu;
- modeli i wag;
- archiwów ZIP/TAR;
- datasetów;
- backupów;
- plików konfiguracyjnych runtime;
- credentiali i sekretów;
- osobnych raportów `.md` innych niż `README.md`.

Jeżeli raport, prompt, manifest, lista interwencji albo wynik eksperymentu ma zostać opublikowany, zostaje **włączony jako sekcja odpowiedniego README** albo streszczony wraz z hashem/lokalizatorem oryginału w Evidence Storage.

To rozdziela dwie role:

```text
LOCAL SSI
= żywy system i pełna prawda wykonawcza

PUBLIC GITHUB
= chronologiczna, czytelna i audytowalna mapa rozwoju
```

Repozytorium GitHub nie powinno być używane jako źródło runtime ani jako pełny backup SSI.

---

# 69. Rozdzielenie wkładu człowieka, AI-asystentów i autonomicznego SSI

Historia SSI powinna jawnie rozróżniać trzy klasy pracy.

## 69.1 Projekt człowieka

Programmer Root odpowiada za koncepcję systemu, kierunek eksperymentu, authority, kluczowe założenia architektoniczne, udostępniane zasoby oraz granice autonomii.

## 69.2 Implementacja wspomagana przez AI

Wiele elementów kodu, testów, dokumentacji i analiz może być wykonywanych z pomocą zewnętrznych modeli i narzędzi programistycznych.

Nie oznacza to, że zewnętrzny model staje się autorem tożsamości SSI lub jego najwyższą authority.

## 69.3 Rozwój inicjowany przez SSI po T0

Po rozpoczęciu eksperymentu szczególnie interesujące są zmiany, których potrzebę samodzielnie wykrył Director lub późniejszy Agent, a następnie przeprowadził je przez istniejący governance.

Dokumentacja powinna pozwolić odróżnić:

```text
ROOT ZAPROJEKTOWAŁ
AI POMOGŁO ZAIMPLEMENTOWAĆ
SSI SAMO ZIDENTYFIKOWAŁO POTRZEBĘ
SSI SAMO ZLECIŁO ENGINEERING
SSI SAMO ZMIENIŁO STRATEGIĘ PO OUTCOME
```

---

# 70. Zasada porównywania SSI z człowiekiem

Jeżeli w przyszłości projekt będzie badał, czy SSI osiąga lub przekracza poziom ludzkiej skuteczności w określonej klasie zadań, porównanie musi mieć jawny protokół.

Potrzebne są co najmniej:

- zdefiniowana klasa zadań;
- porównywalne informacje wejściowe;
- określony budżet czasu i zasobów;
- mierzalny outcome;
- odpowiednia liczba prób;
- baseline człowieka lub grupy ludzi;
- kontrola future-data leakage;
- jawne koszty systemu;
- replikacja;
- opis ograniczeń eksperymentu.

Możliwe wyniki:

```text
SSI < CZŁOWIEK
SSI ≈ CZŁOWIEK
SSI > CZŁOWIEK
NIEWYSTARCZAJĄCE EVIDENCE
```

Każdy z tych wyników jest dopuszczalny.

---

# 71. Kiedy wolno mówić o postępie w kierunku bardziej ogólnej inteligencji

Nie definiujemy jednej liczby `AGI_SCORE`.

Silniejsze evidence w kierunku ogólności pojawia się wtedy, gdy system pokazuje powtarzalnie m.in.:

- skuteczne działanie w nowych domenach;
- przenoszenie abstrakcyjnych kompetencji pomiędzy domenami;
- uczenie z realnych outcomes;
- trwałość wiedzy mimo zmiany zewnętrznego modelu;
- samodzielne rozpoznawanie brakującego capability;
- tworzenie i walidowanie nowych lokalnych kompetencji;
- redukcję powtarzanych błędów;
- rozsądne `ABSTAIN/WAIT/UNKNOWN`;
- zdolność do rewizji wcześniejszych przekonań;
- poprawę wyników w kolejnych epochach;
- rozwiązywanie problemów, dla których Root nie podał gotowego algorytmu.

Pojedynczy sukces, duży zysk, imponujący tekst lub nowa mikrosieć nie stanowią samodzielnego dowodu AGI.

---

# 72. Publiczny dziennik najważniejszych kamieni milowych

README może utrzymywać krótki, automatycznie aktualizowany indeks kamieni milowych.

Każdy wpis powinien zawierać wyłącznie informacje możliwe do zweryfikowania:

```text
DATA
EPOCH
AKTOR
ZDARZENIE
STATUS EVIDENCE
CLAIM_ID / OUTCOME_ID
ODNOŚNIK DO SZCZEGÓŁÓW
```

Przykładowe przyszłe klasy kamieni milowych:

- pierwszy autonomiczny plan gospodarczy;
- pierwsze realne działanie zewnętrzne;
- pierwszy realny przychód;
- pierwsza strata i udokumentowana adaptacja;
- pierwsza nowa capability zaproponowana przez Directora;
- pierwsza mikrosieć utworzona z Experience Run 001;
- pierwsza poprawna prospective prediction mikrosieci;
- pierwszy zasób fizyczny sfinansowany z wyniku SSI;
- pierwszy świat zintegrowany przez Directora;
- genesis pierwszego Agenta;
- pierwszy nieprzewidziany transfer między światami;
- pierwsza hipoteza Directora formalnie obalona przez evidence;
- pierwsza replikacja wyniku przez niezależnego recenzenta.

Lista jest katalogiem możliwych zdarzeń, a nie deklaracją, że którekolwiek z nich już nastąpiło.

---

# 73. Zasada końcowa: README nie jest dowodem — README wskazuje dowód

> **README nie ma przekonywać siłą narracji. README ma prowadzić do materiału, na podstawie którego czytelnik może sam zdecydować, czy twierdzenie jest uzasadnione.**

Root może opisać T0.

Director może dopisywać własne decyzje i interpretacje.

Hermes oraz CONTINUUM mogą dokumentować wykonanie.

Agenci mogą później posiadać własne chroniki.

Evidence Recorder może automatycznie utrzymywać techniczny ślad.

A realny świat pozostaje źródłem outcome, którego żadna z tych warstw nie może zastąpić własną deklaracją.


---

# 74. Root Input Ledger — co człowiek faktycznie wniósł do każdego etapu

Główny `README.md` jest jedynym publicznym miejscem, w którym Programmer Root prowadzi kanoniczny rejestr tego, **co dokładnie zostało przekazane Directorowi jako wejście eksperymentu**.

Każdy istotny etap powinien otrzymać wpis w formacie zbliżonym do:

```text
ROOT_STAGE_ID: ROOT_STAGE_XXX
TIMESTAMP: ...
AUTHOR: PROGRAMMER_ROOT
TARGET: ...

GOAL / ROOT COMMAND:
<dokładny tekst przekazany Directorowi>

RESOURCES GRANTED:
- ...

PACKAGES / DONOR MATERIAL:
- nazwa
- SHA-256
- krótki opis pochodzenia

AUTHORITY / PERMISSIONS GRANTED:
- ...

EXPLICIT BOUNDARIES:
- ...

NOT PROVIDED BY ROOT:
- produkt / rynek / strategia / implementacja / inne elementy, jeżeli faktycznie nie zostały podane

RELATED DIRECTOR README:
- ścieżka powstaje dopiero po utworzeniu jej przez Directora
```

Jeżeli w przyszłości Root przekazuje paczkę World, Moralnej SI, Iskry, Agentów, nowego API, sprzętu albo innego capability, wpis w głównym README zamraża dokładnie **co zostało przekazane**, ale nie opisuje za Directora, co ten później z tym zrobił.

To jest podstawowy mechanizm rozdzielający:

```text
ROOT INPUT
od
DIRECTOR DEVELOPMENT
```

---

# 75. Director-Owned README Genesis — dokument powstający dopiero po działaniu Directora

Po otrzymaniu nowego celu/paczki/capability Director ma sam utworzyć README danego elementu, gdy element rzeczywiście wszedł do jego aktywnego ekosystemu albo został formalnie przyjęty jako aktywny projekt.

Przykład:

```text
ROOT daje paczkę integracji świata + szeroki cel
↓
MAIN README zapisuje dokładny Root Input
↓
DIRECTOR analizuje materiał
↓
DIRECTOR sam wybiera drogę integracji
↓
HERMES / BRAINSTORM / CONTINUUM / MICRONETWORKS — według decyzji Directora
↓
REALNE WDROŻENIE / AKTYWACJA
↓
DIRECTOR tworzy:
WORLDS/<WORLD_NAME>/README.md
↓
DIRECTOR prowadzi ten README dalej
```

Programmer Root **nie powinien pisać za Directora treści pierwszej wersji domenowego README**, jeżeli badamy autonomiczny sposób zrozumienia i rozwinięcia przekazanego materiału. Root dokumentuje wejście w głównym README; Director dokumentuje własny rezultat w README komponentu.

Pierwszy commit takiego README staje się sam w sobie ważnym punktem chronologii, ale nie jest dowodem działania komponentu bez supporting evidence.

---

# 76. Minimalny kontrakt każdego README prowadzonego przez Directora

Director ma swobodę narracji i struktury, ale domenowy README powinien utrzymywać minimalny zestaw informacji potrzebny do badania lineage.

```text
# <NAZWA ELEMENTU>

STATUS
CREATED_BY
FIRST_DIRECTOR_COMMIT
ORIGINATING_ROOT_STAGE / DIRECTOR_ORIGIN
CURRENT_EPOCH

## Genesis
Co było wejściem i kiedy element powstał.

## Co Director zrozumiał z celu
Jego interpretacja, a nie interpretacja dopisana przez Roota.

## Aktualny stan
Co faktycznie jest aktywne teraz.

## Użyte capability
Research / Brainstorm / Hermes / CONTINUUM / mikrosieci / modele / inne.

## Najważniejsze decyzje i zmiany strategii
Z odwołaniami do eventów/outcomes.

## Sukcesy, porażki i rzeczy wycofane
Bez kasowania niewygodnych wyników.

## Root Interventions
Tylko faktyczne interwencje dotyczące tego elementu.

## Evidence Pointers
ID / hash / timestamp / source / receipt / external locator.

## Current Hypotheses
Co Director obecnie uważa, ale co nie jest jeszcze dowodem.

## Timeline
Najważniejsze chronologiczne kamienie milowe.
```

W README nie publikuje się sekretów ani pełnego prywatnego Journalu.

---

# 77. Globalny mandat dokumentacyjny Roota

Od T0 obowiązuje następująca zasada projektu:

> **Director jest odpowiedzialny za tworzenie i utrzymywanie publicznych README dla realnie aktywowanych działów, światów, Agentów, infrastruktury i istotnych capability SSI. Programmer Root dokumentuje w głównym README to, co faktycznie przekazał systemowi, ale nie pisze za Directora historii jego późniejszego rozwoju.**

Director może również autonomicznie utworzyć nowy README dla elementu, którego Root wcześniej nie przewidział, jeżeli:

1. Director sam rozpoznał potrzebę lub szansę;
2. element przeszedł właściwy governance;
3. został rzeczywiście utworzony/aktywowany albo osiągnął formalny status projektu;
4. README jawnie wskazuje jego pochodzenie jako `DIRECTOR_ORIGINATED`;
5. każda potrzebna interwencja Roota została osobno ujawniona.

W ten sposób struktura publicznego GitHuba może rosnąć razem z SSI, zamiast być z góry zaprojektowanym katalogiem przyszłych sukcesów.

---

# 78. Światy przekazane przez Roota a światy utworzone przez Directora

Projekt musi rozróżniać dwa przypadki.

## 78.1 Root-originated world material

Jeżeli Root przekazuje istniejącą paczkę, dane, prototyp lub projekt świata:

```text
ORIGIN = PROGRAMMER_ROOT / PRE-EXISTING DONOR MATERIAL
```

Główny README zapisuje:

- dokładny prompt/goal;
- nazwę paczki;
- hash paczki;
- zakres przekazanych danych/capability;
- granice authority;
- elementy, których Root celowo nie narzucił.

Dopiero Director, po własnej analizie i integracji, tworzy i prowadzi README świata.

## 78.2 Director-originated world

Jeżeli Director sam dochodzi do wniosku, że nowy World zwiększy zdolność SSI:

```text
ORIGIN = DIRECTOR_ORIGINATED
```

README takiego świata powinien pokazać:

- problem lub opportunity, które Director sam wykrył;
- supporting evidence;
- Brainstorm/Research, jeśli zostały użyte;
- proposal i governance;
- engineering lineage;
- ewentualny Root Resource Grant;
- pierwszy realny outcome.

Samo to, że Root później zatwierdzi zakup sprzętu, API lub dostęp do danych, nie zmienia automatycznie pochodzenia pomysłu na `ROOT_ORIGINATED`. Interwencja zasobowa jest rejestrowana osobno.

---

# 79. README działów, światów i Agentów jako biografia rozwoju SSI

Publiczne README nie mają być statycznymi instrukcjami technicznymi. Mają być **skondensowaną biografią rozwoju danego elementu**.

Przykładowo README świata może z czasem pokazać:

```text
GENESIS
↓
PIERWSZA INTEGRACJA
↓
PIERWSZE REALNE DANE
↓
PIERWSZA PORAŻKA
↓
PIERWSZA ZMIANA STRATEGII
↓
PIERWSZA MIKROSIEĆ
↓
PIERWSZY AGENT W ŚWIECIE
↓
PIERWSZY CROSS-WORLD TRANSFER
↓
NOWE CAPABILITY
```

README Agenta może później pokazywać jego własną historię światów, strategii, relacji, eksperymentów, prywatnych mikrosieci i zmian po sukcesach/porażkach — bez publikowania całej prywatnej pamięci.

README działu gospodarczego może pokazywać kolejne etapy od celu Roota, przez decyzje Directora, pierwsze realne działania, przychody/straty, powstające mikrosieci, nowe zasoby i kolejne expansion decisions.

W ten sposób GitHub staje się widoczną mapą **faktycznej trajektorii SSI**, a nie archiwum 68 000 dynamicznych plików.

---

# 80. Co GitHub może udowodnić — i czego nie należy mu przypisywać

Chronologia publicznych README jest bardzo silnym materiałem badawczym, jeżeli jest prowadzona konsekwentnie.

Może pokazać między innymi:

- że Root Command został publicznie zamrożony przed późniejszym wynikiem;
- kiedy powstał pierwszy README danego komponentu;
- czy commit został wykonany przez logiczną tożsamość Directora;
- jak zmieniała się narracja Directora w kolejnych epochach;
- kiedy Root rzeczywiście interweniował;
- czy późniejsze decyzje pojawiły się po realnych outcomes;
- czy pojawiały się nowe katalogi/README, których nie było w T0;
- czy niepowodzenia i wycofane hipotezy pozostały w historii.

GitHub sam w sobie **nie dowodzi**, że właściciel maszyny fizycznie nie mógł ingerować. Dlatego silna interpretacja wymaga razem:

```text
PUBLIC ROOT INPUT
+
DIRECTOR COMMIT HISTORY
+
SIGNED / PROTECTED HISTORY WHERE AVAILABLE
+
LOCAL MACHINE EVIDENCE
+
EXTERNAL OUTCOMES
+
ROOT INTERVENTION LEDGER
```

To jest bardziej odporne na sceptyczną analizę niż twierdzenie „człowiek na pewno niczego nie zrobił”, którego nie da się uczciwie zagwarantować samym GitHubem.

---

# 81. Granica między żywym SSI a publicznym GitHubem

Żywy SSI może posiadać dziesiątki tysięcy dynamicznych plików i stale rosnąć. Te dane są częścią działania systemu, ale nie powinny być kopiowane do publicznego repo tylko po to, aby udowodnić, że istnieją.

Model docelowy:

```text
SSI CANONICAL / LOCAL
- kod
- runtime
- pamięci
- Journal
- Events
- Experience
- dane światów
- modele
- mikrosieci
- eksperymenty
- pełne evidence

        ↓ selekcja + walidacja + provenance

SSI PUBLIC RESEARCH MIRROR / GITHUB
- tylko README.md
- aktualny stan
- Root Input Ledger
- Director Chronicle
- hashe i evidence pointers
- outcomes
- milestone timeline
- publiczna historia Git
```

GitHub dokumentuje projekt. **Nie próbuje być całym projektem.**

---

# 82. Pierwszy moment, w którym ten model zaczyna obowiązywać

`RUN_001_DIRECTOR_COMMERCE` jest pierwszym eksperymentem, dla którego ta separacja ma zostać zastosowana w pełni.

Główny README przechowuje:

```text
ROOT INPUT
= cel + zakres authority + CJ API jako secret grant + to, czego Root celowo nie podał
```

Natomiast po rozpoczęciu działania Director ma utworzyć i prowadzić:

```text
DIVISIONS/COMMERCE/README.md
```

jako własną żywą dokumentację działu.

W późniejszym etapie, gdy Root przekaże pakiet integracji światów/Agentów/Iskry/Moralnej SI, **dokładny prompt i dokładny przekazany materiał zostaną zamrożone w głównym README**, natomiast pierwsze README powstałych/aktywnych światów i kolejnych elementów ma stworzyć Director.

To daje czytelne rozdzielenie:

```text
CO WŁOŻYŁ ROOT
        ≠
CO ZROZUMIAŁ DIRECTOR
        ≠
CO ZBUDOWAŁ SYSTEM
        ≠
CO POTWIERDZIŁ REALNY OUTCOME
```

Ta separacja jest jednym z głównych elementów metodologii Living Research Protocol.

---

# 83. Dynamiczne README jako mapa każdego trwałego elementu życia SSI

Po T0 Director otrzymuje **mandat dokumentacyjny**: gdy w jego aktywnym ekosystemie powstaje nowy trwały obiekt, projekt, dział, świat, Agent, eksperyment, capability lub istotna inicjatywa, Director tworzy dla niego własny publiczny `README.md`.

Przykładowa struktura może rozwijać się dynamicznie:

```text
README.md

MISSIONS/
└── ROOT_MISSION_0001/
    └── README.md

DIVISIONS/
└── COMMERCE/
    └── README.md

PROJECTS/
└── <director-created-project>/
    └── README.md

CAPABILITIES/
└── <new-capability>/
    └── README.md

EXPERIMENTS/
└── <experiment-id>/
    └── README.md

WORLDS/
└── <world-name>/
    └── README.md

AGENTS/
└── <agent-id>/
    └── README.md

SELF_DEVELOPMENT/
└── <initiative-id>/
    └── README.md

LEGO/
└── <root-package-id>/
    └── README.md
```

Ta struktura **nie jest listą przyszłych osiągnięć do utworzenia z góry**. Katalog powstaje dopiero wtedy, gdy istnieje realny powód jego powstania.

---

# 84. Granularność: co dostaje własny README, a co zostaje tylko eventem

Aby dokumentacja nie stała się milionami stron, rozróżniamy dwa poziomy.

## Poziom A — trwała jednostka badawcza

Dostaje własny README, jeżeli posiada własny cel, stan i historię, np.:

- misja Roota;
- dział;
- projekt;
- świat;
- Agent;
- capability;
- mikrosieć lub rodzina mikrosieci o istotnym znaczeniu;
- eksperyment;
- inicjatywa self-development;
- trwały zespół Agentów;
- nowy węzeł infrastruktury;
- istotny program badawczy.

## Poziom B — zdarzenie wykonawcze

Nie tworzy osobnego README dla każdego:

- wywołania API;
- pojedynczej inferencji;
- komendy shell;
- rekordu Journalu;
- małego testu;
- pojedynczego pliku;
- pojedynczej transakcji technicznej.

Te elementy pozostają Machine Evidence i są wskazywane przez README wyższego poziomu.

Zasada:

```text
README = BIOGRAFIA TRWAŁEGO ELEMENTU
EVIDENCE = PEŁNA TELEMETRIA JEGO ŻYCIA
```

---

# 85. README misji — pełne rozdzielenie wejścia Roota od pracy Directora

Każda formalna misja może otrzymać:

```text
MISSIONS/<ROOT_MISSION_ID>/README.md
```

README misji zawiera dwa chronologicznie rozdzielone bloki.

## BLOK A — ROOT INPUT

Automatycznie kopiuje z Root Input Ledger:

- dokładny tekst misji;
- timestamp;
- zasoby;
- paczki LEGO;
- authority;
- ograniczenia;
- elementy celowo nieokreślone przez Roota;
- hash.

Ten blok jest historyczny i niemodyfikowalny semantycznie przez Directora.

## BLOK B — DIRECTOR EXECUTION CHRONICLE

Director sam dopisuje:

- własną interpretację;
- plan, jeśli go stworzył;
- wybrane capability;
- odrzucone alternatywy;
- misje Hermesa/CONTINUUM;
- utworzone elementy;
- porażki;
- wyniki;
- zmiany strategii;
- finalny status;
- evidence pointers.

Dzięki temu na jednej stronie widać:

```text
CO POWIEDZIAŁ ROOT
VS
CO ZROBIŁ DIRECTOR
```

---

# 86. README paczki LEGO — publiczne pochodzenie autorskiego klocka

Każda paczka LEGO przekazana przez Roota może posiadać:

```text
LEGO/<LEGO_PACKAGE_ID>/README.md
```

Publiczna treść nie musi ujawniać kodu.

Powinna zawierać:

```text
NAZWA
AUTOR / POCHODZENIE
DATA POWSTANIA
CZY ISTNIAŁA PRZED RUNEM
CEL
KONTRAKT
INVARIANTY
HASH
CO DOSTAŁ DIRECTOR
CO DIRECTOR MÓGŁ ZMIENIĆ
CO NIE JEST OSIĄGNIĘCIEM DIRECTORA
CO DIRECTOR PÓŹNIEJ DODAŁ SAM
```

To jest szczególnie ważne dla autorskich mechanizmów SSI, takich jak mikrosieci, Moralna SI, Iskra czy specjalne world contracts.

---

# 87. Automatyczne tworzenie README przez Directora

Director może sam zdecydować, że nowy obszar zasługuje na trwałą dokumentację.

Przykład:

```text
Director podczas Commerce wykrywa nową klasę problemu
↓
tworzy nowy projekt/capability
↓
governance akceptuje jego utworzenie
↓
powstaje canonical identity elementu
↓
Director tworzy odpowiedni katalog + README
↓
pierwszy commit wskazuje DIRECTOR_ORIGINATED
↓
kolejne epochy dopisują historię
```

Root nie musi wcześniej przewidzieć nazwy katalogu ani istnienia tego obiektu.

To jest jeden z mierzalnych sygnałów strukturalnego wzrostu SSI, ale samo utworzenie README nie jest dowodem jakości nowej capability.

---

# 88. Dokumentacja świata i Agentów po przekazaniu klocków LEGO

Jeżeli Root później przekazuje Directorowi gotowe paczki LEGO zawierające autorskie elementy świata, Agentów, Moralnej SI lub Iskry, README musi jawnie pokazać różnicę między:

```text
PRE-EXISTING ROOT DESIGN
DIRECTOR ASSEMBLY / INTEGRATION
DIRECTOR MODIFICATION
DIRECTOR-ORIGINATED EXTENSION
AGENT-ORIGINATED DEVELOPMENT
```

Director ma dostać klocki wystarczająco kompletne, aby nie musiał zastępować autorskiej koncepcji przypadkowym standardowym rozwiązaniem znalezionym przez LLM.

Jednocześnie Root nie powinien przepisywać Directorowi:

- kolejności wszystkich kroków integracji;
- lokalnych decyzji architektonicznych, jeśli nie są invariantem paczki;
- przyszłych strategii Agentów;
- tego, jakie mikrosieci mają powstać z późniejszego życia;
- tego, jakie zespoły mają powstać;
- tego, jakie nowe światy Director ma stworzyć samodzielnie.

---

# 89. Zasada obserwatora po aktywacji eksperymentu

Po formalnym starcie danego autonomicznego etapu Root przechodzi, w granicach bezpieczeństwa i authority, do roli możliwie biernego obserwatora.

Root nadal:

- zatwierdza zasoby wymagające jego authority;
- wykonuje czynności fizyczne, których SSI nie może wykonać;
- może zatrzymać system;
- może reagować na bezpieczeństwo, prawo i credentiale;
- może zlecać nowe jawne misje.

Root nie powinien natomiast niejawnie:

- poprawiać decyzji Directora po każdym błędzie;
- dopisywać mu kolejnych kroków bez rejestracji interwencji;
- zmieniać historii README po poznaniu wyniku;
- podsuwać przyszłego outcome;
- przepisywać strategii, a następnie przypisywać jej autonomiczne pochodzenie.

Jeżeli Root decyduje się aktywnie pomóc, pomoc pozostaje dozwolona — ale zostaje jawnie oznaczona jako interwencja.

---

# 90. Wzorcowy lineage przyszłego autorskiego klocka

Przykład mikrosieci:

```text
ROOT BEFORE T0
→ projektuje MICRONETWORK FACTORY jako autorski mechanizm SSI
→ pakuje ją jako LEGO_MN_CORE_V1
→ hash i Root Input Ledger

DIRECTOR AFTER T0
→ otrzymuje mechanizm
→ nie musi go ponownie wymyślać
→ podczas Commerce wykrywa powtarzalny problem supplier-risk
→ decyduje, że potrzebuje lokalnej competence
→ używa LEGO_MN_CORE_V1
→ tworzy teacher/dataset/candidate
→ challenger
→ shadow
→ prospective real outcomes
→ ewentualny champion
→ dokumentuje nową competence

PUBLICZNA ATRYBUCJA:
idea/fabryka mikrosieci = ROOT_ORIGINATED
supplier-risk competence = DIRECTOR_ORIGINATED APPLICATION
implementacja techniczna = AI-ASSISTED / CONTINUUM
skuteczność = REAL OUTCOME
```

Taki zapis jest bardziej wiarygodny niż próba przedstawienia całego łańcucha jako „Director wymyślił wszystko sam”.

---

# 91. Wzorcowy lineage przyszłego świata

```text
ROOT
→ przekazuje WORLD LEGO + dane + prawa + donor material
→ zapisuje dokładny wkład w Root Input Ledger

DIRECTOR
→ analizuje paczkę
→ wybiera sposób integracji zgodny z invariantami
→ używa Hermesa / Brainstormu / CONTINUUM według własnej decyzji
→ uruchamia realny world runtime
→ tworzy WORLDS/<NAME>/README.md

PÓŹNIEJ
→ Director albo Agenci mogą tworzyć nowe eksperymenty
→ nowe mikrosieci
→ nowe strategie
→ nowe zespoły
→ potencjalny cross-world transfer

ROOT NIE JEST AUTOREM TYCH PÓŹNIEJSZYCH ZJAWISK,
chyba że faktycznie interweniował i interwencja jest zapisana.
```

---

# 92. Publiczny indeks odpowiedzialności

Główny README powinien z czasem utrzymywać tabelę:

| Element | Pochodzenie | Kto dostarczył wejście | Kto utworzył aktywny element | Kto prowadzi README | Stan |
| --- | --- | --- | --- | --- | --- |
| Director core | `ROOT_ORIGINATED` | Root | Root + AI-assisted engineering | Director po T0 / Genesis chronione | aktywny stan według T0 |
| Micronetwork Factory | `ROOT_ORIGINATED` | Root LEGO | Root + AI-assisted engineering | Director | według finalnego T0 |
| Commerce Division | `ROOT_MISSION_ORIGINATED` | Root podał cel i capability | Director ma zorganizować dział | Director | `RUN_001` |
| przyszła competence Commerce | `DIRECTOR_ORIGINATED` lub `HYBRID` | zależnie od lineage | Director/CONTINUUM | Director | przyszłe |
| przyszły World z paczki Roota | `HYBRID_ORIGIN` | Root LEGO | Director integruje | Director | przyszłe |
| World wymyślony samodzielnie | `DIRECTOR_ORIGINATED` | brak gotowego projektu Roota | Director | Director | przyszłe |

Tabela ma być aktualizowana zgodnie z faktami, nie z ambicją projektu.

---


# 92A. Kanonizacja i pochodzenie każdego elementu przed SCC

Przed SCC każdy istotny element znaleziony na dysku lub GitHubie powinien otrzymać lineage oraz status.

Minimalne klasy pochodzenia:

```text
ROOT_ORIGINATED
DIRECTOR_ORIGINATED
HYBRID_ORIGIN
AI_ASSISTED_IMPLEMENTATION
EXTERNAL_HUMAN_CONTRIBUTION
UNKNOWN_ORIGIN
```

Minimalne klasy techniczne:

```text
CANONICAL_RUNTIME
ACTIVE_SECONDARY
TEST_ONLY
LEGACY
DEAD_CODE
DUPLICATE
SHADOW_IMPLEMENTATION
PLACEHOLDER
PRESENT_NOT_CONNECTED
UNKNOWN
```

Cross-map ma odpowiadać:

```text
co istniało?
gdzie istniało?
kto lub co było źródłem?
która wersja była realnie wykonywana?
co zostało zastąpione?
co zniknęło z dysku?
co istnieje tylko na GitHubie?
co istnieje tylko lokalnie?
co się rozeszło?
co należy odzyskać?
co należy pozostawić jako historyczne?
```

Z bocznych odnóg należy odzyskiwać **unikalne capability**, a nie całe równoległe organizmy.

Docelowo:

```text
ONE DIRECTOR
ONE HERMES CONTROL PLANE
ONE LOGICAL CONTINUUM
ONE CANONICAL ROOT↔DIRECTOR PATH
ONE CANONICAL EVENT / OUTCOME / EXPERIENCE LINEAGE
ONE PUBLIC RESEARCH MIRROR
MANY CAPABILITIES / EXECUTORS / NODES
```


# 93. Warunek rozpoczęcia Run 001 — PRE-SCC → SCC → T0

Bieżący etap **nie jest jeszcze T0-FROZEN**.

Najpierw muszą zostać zakończone dwa niezależne źródła stanu faktycznego:

```text
SOURCE A
FULL DISK / PROJECT ROOT FORENSICS

SOURCE B
FULL REMOTE GITHUB FORENSICS
```

Następnie:

```text
SOURCE A
+
SOURCE B
+
FINAL ROOT REDESIGN CONTRACT / RHYTHM
↓
DISK ↔ GITHUB CROSS-MAP
↓
LINEAGE / LOST BRANCH / DUPLICATE / LEGACY ANALYSIS
↓
ONE CANONICAL PATH PER COMPONENT
↓
SCC / CANONICAL CONVERGENCE
↓
REAL END-TO-END AUDIT
↓
FINAL T0 MACHINE SNAPSHOT
↓
T0-FROZEN
↓
RUN_001
```

Do czasu zakończenia SCC nie wolno oznaczać elementu jako canonical wyłącznie dlatego, że:

- ma najnowszą datę;
- ma najładniejszy interfejs;
- posiada test `PASS`;
- istnieje w lokalnym repo;
- istnieje na GitHubie;
- był użyty przez wcześniejszą paczkę naprawczą.

Canonicality wymaga realnego call path:

```text
PRODUCTION ENTRYPOINT
→ IMPORT
→ INSTANTIATION
→ REAL CALL
→ REAL STATE / DATA
→ REAL RESULT
→ RETURN PATH
```

Minimalny gate przed `T0-FROZEN`:

```text
FULL_DISK_FORENSICS_COMPLETE
FULL_GITHUB_FORENSICS_COMPLETE
DISK_GITHUB_CROSSMAP_COMPLETE
CANONICAL_BRANCH_SELECTED
NO_UNEXPLAINED_PARALLEL_DIRECTOR
NO_UNEXPLAINED_PARALLEL_CONTINUUM
ROOT_DIRECTOR_PATH_VERIFIED
DIRECTOR_SELF_INSPECTION_VERIFIED
DIRECTOR_SESSION_POLICY_VERIFIED
MISSION_ENVELOPE_POLICY_VERIFIED_OR_EXPLICITLY_PLANNED
INTERFACE_ATTACHED_TO_CANONICAL_RUNTIME
RESOURCE / CAPABILITY REGISTRY VERIFIED
NODE / EXECUTOR STATUS VERIFIED
BRAINSTORM / CONTINUUM FLOW VERIFIED
OUTCOME / EXPERIENCE PATH VERIFIED
LEGO_RESUME_PROTOCOL_READY
FINAL_REAL_E2E_COMPLETE
FINAL_REGRESSION_COMPLETE
T0_MACHINE_SNAPSHOT_CREATED
ROOT_INPUT_LEDGER_FROZEN
LEGO_PACKAGE_REGISTRY_FROZEN
PUBLIC README GENESIS COMMITTED / HASHED
RUN_001 MISSION PRECOMMIT HASHED
SECRET_HANDOFF_READY
```

Jeżeli którykolwiek wymagany element finalnego gate ujawni rozbieżność, wynik zostaje jawnie sklasyfikowany przed Run 001 zamiast wygładzony w narracji.

Po `T0-FROZEN` Genesis nie jest po cichu przepisywany.


# 93A. Ownership głównego README — dynamiczny dokument z chronionymi granicami

Główny README jest wspólną stroną eksperymentu, ale nie oznacza to, że każdy aktor może dowolnie zmieniać każdą część.

```text
GENESIS / T0 BLOCKS
OWNER OF ORIGIN = PROGRAMMER_ROOT
SEMANTIC REWRITE AFTER T0 = FORBIDDEN

ROOT INPUT BLOCKS
ORIGIN AUTHOR = PROGRAMMER_ROOT
PUBLISHED BY = DIRECTOR / AUTO-PUBLISHER może kopiować 1:1
PARAPHRASE AS ROOT WORDS = FORBIDDEN

DIRECTOR LIVE BLOCKS
OWNER = DIRECTOR
PURPOSE = interpretation, decisions, hypotheses, current state, next questions

MACHINE STATUS BLOCKS
OWNER = EVIDENCE / STATUS AUTOMATION
PURPOSE = facts, ids, hashes, timestamps, machine state

AGENT CHRONICLE BLOCKS
OWNER = odpowiedni Agent / supervised publication path
PURPOSE = późniejsza biografia Agenta bez publikowania prywatnej pamięci
```

Director jest więc **redaktorem żywej historii systemu**, ale nie może stać się autorem wcześniejszych słów Roota ani przepisywać Genesis pod późniejszy wynik.

Gdy pojawia się nowy Root Entry, Director może natychmiast dopisać swój blok interpretacji i link do utworzonego przez siebie README. Dzięki temu czytelnik widzi jeden ciąg:

```text
ROOT POWIEDZIAŁ
↓
DIRECTOR ZROZUMIAŁ
↓
DIRECTOR ZROBIŁ
↓
RZECZYWISTOŚĆ ODPOWIEDZIAŁA
↓
SSI SIĘ ZMIENIŁO / NIE ZMIENIŁO
↓
CO BĘDZIE BADANE DALEJ
```


# 94. Sens całego modelu dokumentacyjnego

Po kilku miesiącach lub latach czytelnik powinien móc przejść od pierwszej strony do dowolnego istotnego etapu i odpowiedzieć:

```text
CO ROOT ZAPROJEKTOWAŁ PRZED EKSPERYMENTEM?
CO ROOT PRZEKAZAŁ JAKO LEGO?
JAK BRZMIAŁA DOKŁADNA MISJA?
CO DIRECTOR ZROZUMIAŁ SAM?
CO ZBUDOWAŁ SAM LUB PRZEZ CONTINUUM?
CO ZMIENIŁ PO PRAWDZIWYM OUTCOME?
KTÓRE KOMPETENCJE POWSTAŁY Z EXPERIENCE?
KTÓRE ELEMENTY BYŁY JUŻ GOTOWE?
GDZIE INTERWENIOWAŁ CZŁOWIEK?
CO ZOSTAŁO OBALONE?
CO PRZENIOSŁO SIĘ DO NOWEJ DOMENY?
```

Jeżeli dokumentacja potrafi odpowiedzieć na te pytania z chronologią, autorstwem i dowodami, jej wartość badawcza rośnie wraz z życiem SSI.


# SSI V5

### Ucz się z realnego Experience.

### Zachowuj dowody i provenance.

### Oddzielaj narrację od outcome.

### Rozwijaj własne lokalne kompetencje.

### Korzystaj z najlepszej dostępnej inteligencji zewnętrznej.

### Nie uzależniaj tożsamości od modelu.

### Nie myl capability z authority.

### Nie ukrywaj porażek ani konfliktów evidence.

### Buduj nowe możliwości pod kontrolą.

### Rejestruj hipotezę przed wynikiem.

### Pozwalaj Directorowi samemu odkrywać kolejne braki i możliwości.

### Nie usuwaj nieudanych eksperymentów.

### Pozwól eksperymentowi potwierdzić albo obalić hipotezę.

> **SSI
>  V5 jest zaprojektowany nie tylko po to, aby korzystać z inteligencji,
> ale aby przez długą historię realnych decyzji, outcomes, pamięci,
> mikrosieci, samorozwoju i późniejszego życia Agentów budować własne,
> audytowalne kompetencje — przy zachowaniu suwerennej kontroli Programmer
>  Root.**
