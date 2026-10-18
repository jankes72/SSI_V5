# SSI BLOKS — plan i punkt wznowienia (18.10.2026)

Status: dokument kierunkowy. Migracja produkcyjna: NOT_READY.

## Trzy rownolegle obszary
1. **BLOKS Warehouse**: katalogowanie historycznych zasobow, rodowod, warianty, integralnosc, kwalifikacja, zaleznosci i bezpieczny reuse.
2. **BLOKS MultiControl Global**: wspolny mechanizm kontroli kompozycji dla Dyrektora, CODEX-a, Roberta, mikrosieci, MultiQuant i laboratoriow. Tryb SHADOW_ONLY: kontroluje, proponuje i zglasza HOLD, ale nie wykonuje misji ani nie modyfikuje rejestrow.
3. **SCC Integration**: zgodne polaczenie z istniejacym natywnym jezykiem SCC, parserem i kontraktami, bez zastapienia ich nowym systemem.

## Trwale ustalenia
- Nowa nazwa **BLOKS**; dawne nazwy zostaja tylko w historycznych artefaktach dla kompatybilnosci.
- Mikrosieci powstaly przed LEGO Decomposer/Pocket/META; tamte mechanizmy sluzyly odkrywaniu, rozkladowi, kwalifikacji i ponownemu wykorzystaniu.
- Zachowujemy historyczne ID oraz wszystkie warianty. ID bez hasha moze byc niejednoznaczne; wowczas HOLD zamiast automatycznego wyboru.
- Identyczna nazwa symbolu lub wspolny projekt nie potwierdza krawedzi zaleznosci; trzeba sprawdzic import, definicje, pochodzenie i kontrakt.
- Rejestry Championow mikrosieci, Pocket i MultiQuant pozostaja oddzielne, bez domniemanego mapowania i automatycznych promocji.
- Dyrektor odpowiada za misje i decyzje; CODEX i Robert maja odrebne role. MultiControl nie zastępuje Routera, SCC, notariusza ani autoryzacji.
- Cel migracji: niezalezne serwery Dyrektor, CODEX, Robert; lokalne maszyny jako opcjonalne rozszerzenia. Chronimy prywatne archiwa i kod.
- Publiczny GitHub: dokumentacja kierunkowa, wyniki zbiorcze i dowody bez kodu prywatnego, sekretow lub inwentarzy.

## Udokumentowany stan R9.121
- 15417 rekordow historycznego magazynu, 15415 unikalnych ID; dwa ID maja po dwa odrebne warianty.
- Dwa magazyny: indeksy identyczne SHA-256; 15417/15417 plikow indeksowanych poprawnych w kazdym (audyt R9.118).
- 7146 rekordow z zaleznosciami, razem 24249 wpisow; w tym 10832 prostych nazw symboli.
- R9.121: 6561 pojedynczych kandydatow ze wspolnego projektu, 1946 wielokrotnych, 2325 bez wspolnego projektu, 16 bez zgodnej nazwy. To kandydaci, NIE potwierdzone polaczenia.
- Produkcyjny binding natywnego SCC: NIEPOTWIERDZONY.
- Gate produkcyjny: NOT_READY.

## Najblizszy krok
R9.122: Warehouse bada statycznie definicje i importy; MultiControl waliduje propozycje i warianty offline; SCC Integration bada kontrakty i punkty integracji. Wymagane testy, shadow-parity, dowody, kontrola uprawnien, rollback i jawna decyzja przed wdrozeniem.

**Punkt wznowienia:** kontynuowac trzy tory rownolegle, nie przepisywac historycznych danych i nie uznawac wyniku shadow za wdrozenie produkcyjne.
