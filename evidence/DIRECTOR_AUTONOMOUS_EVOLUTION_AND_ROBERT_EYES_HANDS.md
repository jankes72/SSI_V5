# SSI V5 — Director Autonomous Evolution + ROBERT Eyes/Hands

**Status:** `ARCHITECTURE / HISTORICAL_EVIDENCE / ROOT_ATTESTED`  
**Data:** `2026-08-29`  
**Zakres:** samorozwój Directora, research/capability discovery, ROBERT jako wykonawcze oczy i ręce, lineage od wcześniejszego SSI do obecnej migracji Organism Core

---

## 1. Dlaczego ten dokument istnieje

Publiczny opis SSI nie może redukować ROBERTA do testowego runtime ani Directora do warstwy podejmującej decyzje.

W późniejszej architekturze SSI istnieje dodatkowy ważny mechanizm:

```text
DIRECTOR
-> obserwuje własny stan i ograniczenia
-> może wykryć brak capability lub nową możliwość
-> uruchamia research / engineering
-> korzysta z wykonawczych oczu i rąk
-> testuje propozycję
-> zapisuje outcome i Experience
-> przyjmuje / odrzuca / poprawia zmianę
```

Jest to osobna oś rozwoju systemu i powinna pozostać widoczna po migracji do neutralnego `SSI ORGANISM CORE`.

---

## 2. Autonomous Evolution Fabric

W starszej dokumentacji SSI opisano `Autonomous Evolution Fabric` jako odpowiedź na pytanie:

```text
Skąd ma się wziąć nowy kierunek rozwoju,
jeśli Programmer Root nie poda Directorowi następnego rozwiązania?
```

Założenie jest następujące:

Director nie ma być wyłącznie odbiorcą instrukcji implementacyjnych. Ma korzystać z:

- własnego Self-Modelu;
- aktualnego Experience;
- historii systemu;
- engineering lineage;
- obserwacji zewnętrznego świata technologii;
- researchu i wielomodelowej analizy;
- dostępnych narzędzi i backendów;

aby samodzielnie wykrywać:

- braki capability;
- ograniczenia obecnego designu;
- nowe technologie;
- nowe integracje;
- możliwe usprawnienia;
- okazje do syntezy kilku istniejących rozwiązań.

Nie oznacza to prawa do niekontrolowanego przepisywania canonical runtime.

---

## 3. CEPA — pamięć sposobów budowania

`Continuum Engineering Pattern Architect (CEPA)` ma wykorzystywać historię engineeringową SSI jako pamięć wcześniejszych sposobów rozwiązywania problemów.

Przykładowe źródła:

- wcześniejsze naprawy;
- integracje;
- stare paczki rozwojowe;
- udane i nieudane implementacje;
- regresje;
- rollbacki;
- sposoby dekompozycji dużych projektów;
- powtarzające się klasy błędów.

CEPA nie zastępuje Directora jako decydenta. Ma dostarczać pamięć typu:

```text
PODOBNY PROBLEM JUŻ WYSTĄPIŁ
-> wtedy zadziałało X
-> wtedy zawiodło Y
-> regresję powodowało Z
-> taki podział misji był stabilny
```

Dzięki temu self-development nie zaczyna każdego problemu od zera.

---

## 4. Kanoniczny rytm samorozwoju

Historycznie projekt opisywał następujący przepływ:

```text
OBSERVATION OF SSI / WORLD
-> SELF-MODEL / EXPERIENCE / CEPA
-> DETECTED GAP OR OPPORTUNITY
-> DIRECTOR-ORIGINATED HYPOTHESIS
-> EXPERIMENT PRECOMMIT
-> RESEARCH / BRAINSTORM / CAPABILITY FABRIC
-> HERMES + CONTINUUM / ENGINEERING
-> REAL TEST
-> OUTCOME
-> EXPERIENCE
-> ADOPT / REJECT / REVISE
-> NEW CAPABILITY OR NEW KNOWLEDGE
-> PUBLIC HISTORY UPDATE
```

Bezpieczna aktywacja pozostaje osobnym kontraktem:

```text
NEED
-> PROPOSAL
-> JUSTIFICATION
-> AUTHORITY
-> ENGINEERING
-> TEST
-> EVIDENCE
-> APPROVAL
-> CONTROLLED ACTIVATION
```

`DIRECTOR_ORIGINATED` oznacza pochodzenie inicjatywy, nie nieograniczoną authority.

---

## 5. ROBERT jako Eyes / Hands / Browser / wykonawczy interfejs do świata

ROBERT nie jest wyłącznie donorem mechanizmów dla Organism Core.

W architekturze SSI pełni również rolę wykonawczego ciała, przez które Director może — zgodnie z authority i permission gates — uzyskać dostęp do narzędzi i środowiska komputerowego.

Historyczne artefakty obejmują lekki węzeł `director-node` opisany jako `EYES/HANDS`, z zależnościami m.in. Playwright i DBus.

Warstwa Eyes/Hands została projektowana wokół capability takich jak:

- screenshot;
- screen state;
- browser interaction;
- app/window targeting;
- mouse;
- keyboard;
- dry-run;
- audit trail;
- permission gates.

W docelowym układzie daje to przepływ:

```text
DIRECTOR DETECTS NEED
        ↓
ROBERT / EYES / HANDS / BROWSER
        ↓
WEB / DOCUMENTATION / GITHUB / PUBLIC TECHNICAL SOURCES
        ↓
CANDIDATE TECHNOLOGY / IDEA / TOOL
        ↓
DIRECTOR + CEPA + RESEARCH / CROSS-REVIEW
        ↓
PROPOSAL
        ↓
CONTINUUM / ENGINEERING
        ↓
SANDBOX / TEST / EVIDENCE
        ↓
ADOPT / REJECT / REVISE
```

Sam fakt znalezienia technologii nie czyni jej częścią canonical SSI.

---

## 6. Research nie jest tym samym co automatyczna instalacja

Director może korzystać z internetu, dokumentacji, repozytoriów i innych publicznych źródeł jako wejścia badawczego.

Zasada pozostaje:

```text
FOUND ONLINE
!=
VERIFIED
!=
SAFE TO INTEGRATE
!=
APPROVED
```

Nowa technologia powinna przejść przez:

- provenance;
- ocenę zgodności z istniejącą architekturą;
- reuse-first check;
- sandbox;
- test kontraktowy;
- test integracyjny;
- regresję;
- rollback plan;
- evidence;
- authority gate.

---

## 7. Novel synthesis — Director może łączyć kilka technologii

Jedną z ważniejszych hipotez nie jest samo znajdowanie gotowych bibliotek, ale łączenie kilku źródeł w rozwiązanie własnego problemu.

```text
TECHNOLOGY A rozwiązuje fragment problemu
+
TECHNOLOGY B daje inne potrzebne capability
+
SSI EXPERIENCE pokazuje bottleneck C
        ↓
DIRECTOR PROPONUJE A + B jako rozwiązanie C
        ↓
PRECOMMIT
        ↓
SANDBOX / EXPERIMENT
        ↓
REAL OUTCOME
```

Dopiero wynik testu może zamienić syntezę z hipotezy w użyteczną capability.

---

## 8. Związek z obecną migracją Organism Core

Obecna migracja ROBERTA do neutralnego core nie oznacza, że system dopiero teraz otrzymuje self-development, research albo Eyes/Hands.

Celem migracji jest wydzielenie mechanizmów wspólnych z działających i wcześniej projektowanych struktur, aby następnie użyć ich w czystszej architekturze:

```text
STARSZY SSI / DIRECTOR
-> ROBERT / HARDENING / CONTROLLED TESTING
-> SSI ORGANISM CORE
-> ROBERT BODY
-> REBUILT DIRECTOR BODY
-> AGENT BODY
```

Po przebudowie Director powinien odzyskać swoją wcześniejszą funkcję strategicznego obserwatora i inicjatora self-development, lecz na neutralnym, testowalnym substrate.

---

## 9. Historia testów musi pozostać chronologiczna

W publicznych materiałach istnieją zarówno wcześniejsze raporty pokazujące niepełne wiring i FAIL na części E2E, jak i późniejsze raporty naprawcze deklarujące przejście kolejnych etapów i pełnych regresji.

Nie należy usuwać wcześniejszych porażek.

Prawidłowa interpretacja:

```text
EARLIER FAILURE
-> REPAIR
-> LATER VALIDATION
```

nie:

```text
EARLIER FAILURE NEVER EXISTED
```

To jest zgodne z zasadą SSI, że Git ma być biografią rozwoju, a nie retrospektywnie wygładzonym opisem sukcesów.

---

## 10. Samodzielny rozwój projektu i uczciwa atrybucja

SSI V5 jest rozwijane niezależnie przez Pawła Jankiewicza jako autora nadrzędnej architektury i `PROGRAMMER_ROOT`.

Publiczna historia Git pokazuje formalizację architektury od root commit `MSDI AI v0.01 - start projektu` z 2026-07-19 oraz kolejne publiczne etapy: SSI Core, Data World, V2, SSI V5, CONTINUUM, SSI_V5_MASTER i publiczny research mirror.

Nie oznacza to, że wszystkie dane domenowe, Football World, wcześniejsze modele lub doświadczenie powstały w tym krótkim okresie. Te elementy mają wcześniejszą historię.

Jednocześnie niezależny rozwój SSI nie oznacza przypisywania sobie cudzych koncepcji. Źródłowa idea Moralnej AI / Iskry została osobno przypisana wcześniejszemu projektowi brata autora, a adaptacja tej idei do SSI ma własne lineage.

Zasada:

```text
INDEPENDENT SSI ENGINEERING
!=
CLAIM OF INVENTING EVERY SOURCE IDEA
```

---

## 11. Granice twierdzeń

Ten dokument nie twierdzi, że:

- Director ma dziś nieograniczony autonomiczny dostęp do internetu;
- każdy element Eyes/Hands jest aktywny w każdej konfiguracji runtime;
- każda znaleziona technologia jest automatycznie instalowana;
- self-development może ominąć authority;
- wcześniejsze raporty FAIL są unieważnione przez późniejsze PASS;
- samo istnienie pętli self-development dowodzi AGI;
- każda przyszła capability będzie Director-originated.

Twierdzenie jest węższe:

**SSI posiada zaprojektowaną i częściowo zaimplementowaną architekturę, w której Director może wykrywać własne braki, inicjować kontrolowany research i engineering, a ROBERT/Eyes/Hands stanowią wykonawczy interfejs do narzędzi oraz świata technologii. Obecna migracja ma zachować te mechanizmy i przenieść je na czystszy, neutralny substrate.**
