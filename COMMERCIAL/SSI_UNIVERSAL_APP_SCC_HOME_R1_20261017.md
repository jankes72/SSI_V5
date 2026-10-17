# SSI Universal App + SCC — język misji dla inteligentnego domu (R1)

**Data:** 2026-10-17  
**Status:** SPECYFIKACJA INTEGRACJI / PLAN. **Brak wdrożonego sterowania sprzętem poprzez SCC.**  
**Źródła projektu:** [SCC A27 — stan faktyczny i składnia](../SCC_BLOCKS_MISSION_LANGUAGE_AND_AMNEZJA3_ATTRIBUTION_20261014.md), [SSI Universal App R1](SSI_UNIVERSAL_APP_SMART_HOME_MULTIQ_R1_20261017.md), [kanoniczna architektura SSI V5 C4](../SSI_V5_C4_ARCHITECTURE.md).

## Cel biznesowy

Klient kupuje SSI Universal App, loguje się **raz**, podaje marki i modele posiadanych urządzeń, paruje je przy użyciu dozwolonych metod, a następnie zwykłym językiem mówi, co chce osiągnąć. SCC ma zapisywać **cel i kryteria** w kanonicznej, wersjonowanej reprezentacji, a zatwierdzone adaptery urządzeń mają wykonywać dopiero **osobno autoryzowane** czynności. Pamięć konfiguracji domu i doświadczeń pozostaje we własnych modułach SSI (Research Memory, mikrosieci, SCC), nie w pamięci kontekstowej konkretnego LLM.

**Przykład komunikatu klienta:** „Codziennie wieczorem chcę 21 stopni w salonie, odkurzacz niech sprząta, kiedy nikogo nie ma, a SSI niech mnie głosowo informuje o problemach”.

**Stan zamierzony:** urządzenia i ich możliwości są wykryte, powiązane z pomieszczeniami i kontami; klient zatwierdza reguły; lokalny Home Edge Hub utrzymuje harmonogram, stan i powiadomienia **bez konieczności kontaktu z płatnym LLM**.

## Co potrafi SCC A27 już dziś (zakres udokumentowany)

Udokumentowany, autorowo zgłoszony A27 z 2026-10-14 zapewnia:
- parsowanie, walidowanie i kanonizację **deklaratywnego celu** misji oraz deterministyczny zapis do istniejącego kontraktu `ssi.mission.goal.r1` / `ssi.mission.intent.r1`;
- wersję strategii, zadanie/projekt, domenę, wejście, cel, referencję kontekstu SHA-256, kryterium akceptacji, ograniczenie liczby kroków i flagę walidacji;
- podgląd **liniowych propozycji planu**, integrację z już istniejącymi Operations / Research Memory i jawne zgłaszanie brakujących zdolności.

W podanym raporcie SCC wykonano **22 testy Pythona i 10 asercji JavaScript** bez dostawców LLM; zakres wykonawczy Championów pozostawał **wyłączony**, a dowody semantycznego wykonania niezwiązane. Parser **odrzuca** składnię imperatywną, warunki i równoległe programy; nie wolno traktować ich jako obecnej funkcji SCC. Żadna udana walidacja tekstu SCC **nie oznacza**, że komenda została wysłana do urządzenia.

### Przykładowa istniejąca deklaracja SCC dla domu (ilustracja, nie gotowa misja)

```text
SSI_MISJA 1
PROJEKT "home_example"
ZADANIE "evening_temperature_goal"
STRATEGIA "home_comfort"
WERSJA_STRATEGII "v1"
DOMENA "smart_home"
WEJSCIE "Salon ma 19 C; termostat jest sparowany; wlasciciel chce 21 C"
CEL "Ustal dozwolony plan osiagniecia 21 C w salonie i potwierdz jego wykonanie"
KONTEKST_SHA256 "0000000000000000000000000000000000000000000000000000000000000000"
KRYTERIUM "living_room_21c_confirmed_v1"
MAKS_KROKOW 16
PELNA_WALIDACJA false
KONIEC
```

To demonstracja **obsługiwanej postaci składni**, nie plik wykonywalny przez domową instalację: `home_example`, `smart_home`, kryterium, uprawnienia i rzeczywisty hash nie są tu skonfigurowane. Zero-hash jest atrapą wyłącznie do przykładu. Utworzenie rzeczywistej misji wymaga prawdziwego kontekstu, rejestracji projektu/zadania, właściwych umów walidacyjnych i adaptera urządzenia. Zapis nie zawiera składni zegara/warunku ani nie uruchamia ogrzewania.

## Planowany most Universal App -> SCC -> Home Edge

```text
Uzytkownik (tekst lub glos / STT)
  -> Intent Parser (lokalna regulka lub dobrany przez SSI MultiQuant LLM)
  -> Rejestr domu: identyfikatory urzadzen, pokoje i rzeczywiste mozliwosci
  -> A27 SCC: kanoniczna deklaracja celu + walidacja + kontrakt planowania
  -> Home Plan Translator (NOWY, PLANOWANY adapter; nie rozszerzenie parsera na slepo)
  -> Human approval + policy engine + allowed-action schema
  -> Deterministyczny harmonogram i adapter Matter/HA/Zigbee/vendor
  -> ACK + odczyt stanu + test warunku koncowego
  -> Lokalna pamiec, dziennik dowodow, komunikat przez TTS
```

Przy braku parowania, uprawnienia, wspieranej funkcji lub prawdziwego potwierdzenia stanu system ma zwracać `NEEDS_PAIRING`, `NEEDS_APPROVAL`, `UNSUPPORTED`, `PENDING_CONFIRMATION`, `FAILED` itp. **Nie wolno komunikować sukcesu na podstawie samego polecenia LLM**.

### Projektowany kontrakt pośredni HOME-ACTION v0 — NIE JEST składnią SCC A27

```json
{
  "schema": "ssi.home.action.proposal.v0",
  "mission_id": "ssi-mission-placeholder",
  "home_id": "home-placeholder",
  "actor_role": "owner",
  "scc_goal_ref": "goal-digest-placeholder",
  "device_id": "climate.living_room",
  "capability": "climate.set_temperature",
  "arguments": {"celsius": 21},
  "preconditions": ["paired", "online", "policy_allows", "not_conflicting"],
  "approval": "required_by_policy",
  "expected_observation": {"attribute": "target_temperature", "celsius": 21},
  "idempotency_key": "mission-action-placeholder",
  "state": "PROPOSED"
}
```

Kontrakt jest nową **propozycją schematu**, nie działającym endpointem. Potrzebne są: prawdziwe identyfikatory urządzeń i właściciela, mapowanie możliwości, podpisany adapter, autoryzacja, okres ważności, retry bounds i późniejszy odczyt rzeczywistego stanu. Nie wolno klientowi przekazywać nazw wewnętrznych misji innych gospodarstw.

## Jak SCC pomoże w realnych urządzeniach

| Sprzęt klienta | Cel zapisany przez SCC | Planowane odpowiedzialne wykonanie | Warunek sukcesu |
|---|---|---|---|
| Oświetlenie | Komfort / oszczędzanie energii | Lokalna scena przez sprawdzony adapter | Odczyt stanu światła |
| Grzejniki i klimatyzacja | Określona temperatura, brak konfliktu | Home scheduler, limits, priorytety urządzeń | Zgodny odczyt zadanej temperatury, nie fikcyjny pomiar otoczenia |
| Odkurzacz | Sprzątanie pod nieobecność domowników | Autoryzowany harmonogram dostępnego robota | Robot potwierdza wykonanie lub konkretny błąd |
| Kosiarka | Bezpieczne wykonywanie pracy | Adapter zgodny z producentem + jego blokady bezpieczeństwa | Stan zadania i brak zgłoszonych alarmów; brak obchodzenia zabezpieczeń |
| Brama | Otwarcie w zatwierdzonym kontekście | Osobna autoryzacja właściciela, lokalny kontroler, czujnik położenia | Czujnik potwierdza stan; głos sam nie otwiera bramy |
| Kamery | Sprawdzenie zdarzenia | Uprawnienia do strumienia / zdarzeń, bez domyślnego wysyłania obrazu do chmury | Potwierdzone zdarzenie, a nie zgadywanie |
| Mikrofony i głośniki | Rozumienie pytań i odpowiedź głosowa | Wake word/STT i TTS na edge, jawne zezwolenia | Odpowiedź oparta na potwierdzonym stanie |

**Zasada bezpieczeństwa:** SCC i LLM określają cele/propozycje, a deterministyczna warstwa Home Edge **odpowiada za faktyczne komendy**. Odrębne lokalne sterowniki odpowiadają za procedury awaryjne. Nieautoryzowany lub niejednoznaczny zamiar musi zostać odrzucony albo skierowany do człowieka.

## SCC i MultiQuant: jak skorzystamy na oszczędzaniu pamięci

SCC umożliwia przetwarzanie prostych, już opisanych czynności bez każdorazowego pytania chmurowego LLM. Dla złożonych poleceń SSI MultiQuant może wybrać lokalny skwantyzowany model, ale tylko jeśli jego implementacja wspiera urządzenie i obowiązują bezpieczne ograniczenia obliczeniowe. Ta sama intencja, format celu i kontrakt adaptera pozostają stabilne przy zmianie modelu. **Nie przenosimy urządzeń, sekretów, zapisów użytkownika ani wiedzy o domu do publicznych wag LLM.**

SCC pozwala też stopniowo rozwijać skille urządzeń jako wersjonowane konstrukcje: `rozpoznaj stan -> zaproponuj akcję -> zweryfikuj uprawnienia -> wykonaj -> potwierdź -> zapamiętaj dowód`. To opis **docelowego przepływu**, nie istniejąca obsługa warunków SCC.

## Precyzyjny plan rozszerzeń SCC HOME

| Etap | Rozszerzenie | Warunek uznania za gotowe |
|---|---|---|
| **H0** | Zgodność kontraktu A27 w osobnym kontekście klienta | Parser działa na kanonicznych celach; zero rzeczywistych komend |
| **H1** | Rejestr typowanych urządzeń i ich możliwości | Odrzucone są akcje, których sprzęt nie obsługuje |
| **H2** | Translator planu SCC na `ssi.home.action.proposal.v0` | Autoryzacja i potwierdzenie wymaganych działań |
| **H3** | Deterministyczne lokalne `jeżeli / kiedy / harmonogram` **poza składnią A27** | Testowana kontrola warunków i brak samoczynnego obejścia polityki |
| **H4** | Home Edge voice, lokalna pamięć, stany wykonania i Notariusz | Prawdziwe domowe zadania + evidence, bez fałszywych potwierdzeń |
| **H5** | Ewentualna nowa wersja języka SCC z operacjami, warunkami i równoległością | Nowy parser, jawny numer wersji i zgodność z istniejącymi misjami |

Nie dokładamy nieudokumentowanych słów kluczowych do `SSI_MISJA 1`. Reguły czasowe są najpierw realizowane przez lokalny scheduler; rozszerzenie języka SCC wymaga osobnego wydania.

### Prywatność i wykorzystanie doświadczeń

Dane z realnych misji w domu mogą zasilać kalibrację adapterów, mikrosieci i model selection tylko przy adekwatnej zgodzie klienta i w granicach obowiązującej polityki. Dane osobowe, podgląd kamer, próbki głosu, lokalizacje domów i hasła nie są publicznym materiałem treningowym. Publikowane wyniki mogą zawierać tylko anonimowe, zagregowane statystyki skuteczności i błędów integracji.

## Uznanie autorstwa

Język SCC jest rozwijany w SSI V5 przez Pawła Jankiewicza; inspiracje i wybrane mechanizmy konstrukcji pochodzą z projektu [Awareness autorstwa amnezja3](https://github.com/amnezja3/awareness). Szczegółowy opis wkładu i źródeł: [SCC language record](../SCC_BLOCKS_MISSION_LANGUAGE_AND_AMNEZJA3_ATTRIBUTION_20261014.md). Nie przedstawiamy Awareness jako sterownika smart home ani udostępnionego runtime'u Universal App.
