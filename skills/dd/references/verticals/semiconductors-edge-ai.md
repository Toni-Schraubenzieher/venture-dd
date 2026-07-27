---
name: semiconductors-edge-ai
label: Semiconductors & Edge-AI-Silizium (inkl. Neuromorphic, RF, Photonics, ASIC/IP)
description: Startups die eigene Chips designen — Beschleuniger, Sensor-Frontends, RF/Photonik, neuromorphe Prozessoren — und diese als Silizium verkaufen oder als IP lizenzieren
keywords: [semiconductor, semiconductors, chip, chips, silicon, ASIC, SoC, IC, wafer, foundry, tape-out, tapeout, node, CMOS, analog, mixed-signal, RF, photonics, neuromorphic, spiking, SNN, in-memory computing, edge AI, NPU, accelerator, TOPS, IP core, RTL, PDK, MPW, MEMS, RRAM, memristor, halbleiter, prozessor]
---

# Vertical: Semiconductors & Edge-AI-Silizium

## Kontext
Chip-Startups sind die kapitalintensivste und langsamste Deep-Tech-Klasse: Von der ersten Idee bis zum Umsatz vergehen typisch 5-8 Jahre, Design-Win-Zyklen bei OEMs dauern 12-24 Monate und Revenue kommt erst 1-2 Jahre NACH dem Design-Win. Die drei haeufigsten Investorenfehler: (1) **Ein Tape-out wird als Produktreife gelesen** — ein funktionierender MPW-Shuttle-Chip ist ein Forschungsergebnis, kein qualifiziertes Produkt; zwischen beiden liegen Yield, DFT, Temperaturqualifikation, PPAP und oft ein kompletter Redesign. (2) **Benchmark-Claims werden ungeprueft uebernommen** — bei Silizium ist fast jede Effizienzzahl ein Vergleich ungleicher Workloads, Systemgrenzen oder Prozessknoten. (3) **Das Geschaeftsmodell bleibt unentschieden** — Chip-Sales und IP-Licensing haben voellig verschiedene Kapitalprofile, Margen und Comparables; wer beides gleichzeitig behauptet, hat meist keines validiert. Gute Deals haben vermessenes Silizium, mindestens einen bezahlten Design-Win oder NRE-Vertrag und ein Team, in dem jemand schon einmal ein Design **in Serienproduktion** gebracht hat.

## Extraction Focus Areas (Session 3)
- **Silizium-Status pro Chip:** Simuliert / Emuliert (FPGA) / MPW-Shuttle-Tape-out / Full-Mask-Tape-out / qualifiziert. Wie viele Tape-outs bisher, welche Revisionen, welche Bugs gefunden? First-Silicon-Success oder mehrere Spins?
- **Foundry & Prozessknoten:** Welche Foundry, welcher Node, welcher PDK-Zugang (direkt / ueber Broker / ueber Europractice/IMEC/CMP)? Bei Spezialprozessen (RRAM/PCM/eNVM, FD-SOI, BCD, GaN, Photonik): ist der Prozess bei mehreren Foundries verfuegbar oder Single-Source?
- **Analoge/mixed-signal Spezifika:** Wo werden Gewichte/Zustaende gespeichert (Floating-Gate, RRAM/PCM, Kondensator+Refresh, SRAM)? Retention, Drift, Endurance? Wie wird Device-Mismatch kompensiert — Design, Trimming, Per-Die-Kalibrierung im Test, On-Chip-Learning? **Kalibrierungsaufwand pro Die ist ein direkter COGS-Treiber.**
- **Benchmark-Methodik (Pflicht, woertlich extrahieren):** Welche Task, welcher Datensatz, welche Accuracy, welches SNR, welche Temperatur, welche Versorgungsspannung, welcher Prozessknoten? Was ist in der Leistungsangabe enthalten (Leckstrom, Bias, Referenzen, Clock, IO, Memory-Retention) und was ist ausgeschlossen?
- **Systemgrenze:** Chip-Leistung vs. Systemleistung. Bei Sensor-Frontends: was zieht der Sensor selbst, das Interface, der Wake-Pfad, der nachgelagerte SoC? Die Systemersparnis ist fast immer deutlich kleiner als die Chip-Ersparnis.
- **Die-Groesse, Yield, Packaging:** mm2, erwarteter Die-per-Wafer, Yield-Annahme, Package-Typ, Testzeit pro Die (ATE-Sekunden = Kosten), DFT/Scan-Abdeckung
- **Qualifikation:** Temperaturbereich (Consumer/Industrial/Automotive AEC-Q100 Grade), ESD/Latch-up, JEDEC-Reliability, Zertifizierungsbedarf. Was ist erreicht, was fehlt, welche Timeline?
- **Toolchain/SDK:** Compiler, Quantisierung, Modell-Import (ONNX/TFLite), Simulator, Hardware-in-the-Loop. Wie viele externe Entwickler haben damit je etwas gebaut? Bei exotischen Architekturen (SNN, analog, photonic) ist die Toolchain oft der eigentliche Adoption-Blocker.
- **Design-Win-Pipeline:** Pro Kunde: Stufe (Erstkontakt / Eval-Kit / Evaluation laeuft / NRE bezahlt / Design-Win / in Produktion), Volumenprognose, SOP-Datum. **Eval-Kit-Anfrage ist kein Design-Win.**
- **Geschaeftsmodell:** Chip-Sales (ASP, Volumen, Distributor) vs. IP-Licensing (Lizenzgebuehr, Royalty pro Unit, NRE) vs. Chiplet vs. Hybrid. Welches ist im Financial Model modelliert?
- **IP & Herkunft:** Patente (erteilt vs. angemeldet vs. Prioritaet), Erfinder, Inhaber. Bei Uni-Spin-outs: **Assignment oder Lizenz?** Welche Universitaet, welche Konditionen, welche Reach-through-Rechte? Third-Party-IP im Design (PHY, SerDes, Standardzellen, Memory-Compiler) und dessen Lizenzkosten.
- **NRE- und Maskenkosten:** Was hat der bisherige Tape-out gekostet, was kostet der naechste? Full-Mask-Set nach Node.

## Cross-Referencing Checks (Session 4)
- [ ] **Silizium-Status vs. Kommunikation:** Wird "silicon-validated" / "in production" konsistent verwendet? Abgleich Website vs. Deck vs. Presse vs. Messbericht. Was genau wurde auf Silizium gemessen und was ist extrapoliert?
- [ ] **Benchmark-Workload-Aequivalenz:** Vergleicht der Effizienz-Claim dieselbe Aufgabe wie der Wettbewerber? Modellgroesse, Accuracy, Datensatz, Node gegenpruefen. Ein Trigger-/VAD-Stage gegen eine volle Inferenz-Engine zu stellen ist der haeufigste Trick.
- [ ] **Chip-Budget vs. System-Budget:** Chip-Leistungsangabe gegen realistisches Systembudget rechnen (Sensor + Bias + Interface + Wake-Pfad). Wie gross ist die Ersparnis auf Board-Ebene wirklich?
- [ ] **Kalibrierung vs. COGS:** Falls Per-Die-Kalibrierung noetig: Testzeit x ATE-Kostensatz gegen den ASP rechnen. Bei Cent-ASPs kann Testkosten das Geschaeftsmodell allein killen.
- [ ] **Design-Win-Zyklus vs. Revenue-Rampe:** Erste Revenue im Model gegen realistischen Zyklus pruefen (Eval 3-6 Mon → Design-in 6-12 Mon → Qualifikation 3-6 Mon → SOP). Passt die Rampe oder unterstellt sie einen Zyklus, den die Branche nicht kennt?
- [ ] **Geschaeftsmodell-Konsistenz:** Pitch sagt IP-Licensing, Model rechnet Stueck-Margen (oder umgekehrt)? Royalty-Annahmen gegen reale Vergleichswerte (Arm/Ceva/Cadence-Groessenordnung)?
- [ ] **Tape-out-Kosten im Plan:** Sind die naechsten Maskensaetze, MPW-Slots, PDK-Lizenzen, EDA-Tool-Kosten (oft 6-stellig p.a.) und Packaging-NRE im Model? EDA-Lizenzen werden fast immer vergessen.
- [ ] **Node-Abhaengigkeit:** Ist das Design an einen Spezialprozess oder eine einzelne Foundry gebunden? Was kostet eine Portierung in Zeit und Geld?
- [ ] **Team vs. Produktionsanspruch:** Hat jemand im Team ein Design bis Serienproduktion und Qualifikation begleitet? Forschungs-Tape-outs zaehlen nicht.
- [ ] **Incumbent-Integrations-Risiko:** Kann ein Sensor-/Komponenten-Incumbent (MEMS-, Mikrofon-, Bildsensor-, RF-Hersteller) die Funktion selbst integrieren oder zukaufen? Historisch ist das der haeufigste Exit-Killer fuer Sensor-Compute-Startups.
- [ ] **Patent- vs. Produkt-Deckung:** Decken die Patente tatsaechlich den verkauften Chip ab oder nur eine Vorgaengerarbeit aus der Uni-Zeit?

## Unit Economics Calculations (Session 4 Phase 2)
1. **Die-Kosten:** Waferpreis / (Dies-pro-Wafer x Yield) = Kosten pro Good Die. Dies-pro-Wafer aus Die-Groesse und 300mm/200mm-Wafer ableiten, nicht uebernehmen.
2. **All-in COGS pro Chip:** Good-Die-Kosten + Packaging + Test (ATE-Sekunden x Kostensatz, inkl. Kalibrierung) + Yield-Loss nach Package + Logistik. Gegen den behaupteten ASP stellen.
3. **Bruttomarge realistisch:** (ASP - All-in COGS) / ASP. Fabless-Halbleiter gesund: 50-65%. Unter 40% ist das Modell fraglich, ueber 75% meist nur bei IP-Licensing.
4. **NRE-Amortisation:** (Maskensatz + Designkosten + EDA + IP-Lizenzen) / erwartete Lifetime-Stueckzahl = NRE-Anteil pro Chip. Bei kleinen Volumina dominiert das alles andere.
5. **Break-even-Volumen:** Fixkosten p.a. / Bruttogewinn pro Chip = jaehrlich noetige Stueckzahl. Gegen die Design-Win-Pipeline stellen — ist die Zahl ueberhaupt erreichbar?
6. **IP-Licensing-Variante:** (Anzahl Lizenznehmer x Lizenzgebuehr) + (Royalty pro Unit x Volumen). Realistisch sind wenige Lizenznehmer pro Jahr und lange Vertragszyklen — Modelle mit zweistelligen Lizenznehmerzahlen in Jahr 3 sind Fantasie.
7. **Runway bis naechster Beweis:** Cash / Burn gegen die Zeit bis zum naechsten harten Meilenstein (naechstes Tape-out, erster bezahlter Design-Win, Qualifikation). Reicht das Geld, um den Case zu VALIDIEREN, nicht nur um zu ueberleben?

## Research Blocks (Session 5, Bloecke 2-4)

### Block 2: Markt, Industriepolitik & Regulierung
Web-Recherche (Englisch):
- TAM/SAM des konkreten Chip-Segments, aktuelle Analystenzahlen (2024-2026), Stueckzahlen statt nur Dollar
- Industriepolitik: EU Chips Act, US CHIPS Act, IPCEI Microelectronics, nationale Halbleiterprogramme — welche Toepfe sind fuer ein Startup dieser Groesse real zugaenglich?
- Non-dilutive: EIC Accelerator (bis 2,5 Mio EUR Grant + 10 Mio EUR Equity), EIC Pathfinder, Eurostars, nationale F&E-Foerderung. Antragsstatus des Startups pruefen
- Exportkontrolle: Dual-Use-Verordnung, ITAR/EAR-Beruehrung, Wassenaar-Listen bei Hochleistungs-/RF-/Krypto-Silizium
- Foundry-Kapazitaet und Preistrends am Zielknoten, geopolitische Abhaengigkeit (Taiwan/China-Exposure)

### Block 3: Kunden, Design-Wins & Nachfrage-Validierung
Web-Recherche:
- Wer sind die realen Abnehmer im Zielsegment (OEMs, Modulhersteller, Tier-1s)? Wie konzentriert?
- Typische Beschaffungs- und Qualifikationszyklen im Zielsegment. Wer entscheidet, wie lange dauert es?
- ASP-Benchmarks vergleichbarer Bauteile — was zahlt der Markt heute pro Funktion?
- Oeffentliche Design-Wins der Wettbewerber: Wer ist wo drin? Welche Produkte sind gelauncht?
- Adoption-Barrieren: Second-Source-Anforderung (viele OEMs kaufen nicht Single-Source), Langzeitverfuegbarkeits-Zusagen (10-15 Jahre), Toolchain-Umstellungskosten beim Kunden

### Block 4: Silizium-Benchmarks & Technologie
Web-Recherche:
- Publizierte Leistungszahlen der Wettbewerber aus **Primaerquellen** (Datenblaetter, ISSCC/VLSI/Hot-Chips-Papers, MLPerf Tiny), nicht aus Sekundaerartikeln
- Akademischer State of the Art: gibt es publizierte Arbeiten, die den Claim bereits erreichen oder uebertreffen? Wer forscht daran?
- Bekannte Failure-Modes der gewaehlten Technologie (z.B. Mismatch/Drift bei Subthreshold-Analog, Retention bei RRAM, thermische Stabilitaet bei Photonik)
- IP-Landschaft: Patente der Wettbewerber und der grossen Player. Freedom-to-Operate-Risiko
- Historie: welche Startups haben denselben Ansatz schon versucht und woran sind sie gescheitert? Uebernahmen und deren Preise als Exit-Referenz

## Risk Framework
1. **Tape-out != Produkt:** Vermessenes Erst-Silizium ist ein Forschungsergebnis. Bis zum qualifizierten, testbaren, yield-optimierten Produkt liegen typisch 1-3 weitere Spins und 18-36 Monate.
2. **Benchmark-Inflation:** Effizienz-Claims vergleichen fast immer ungleiche Workloads, Systemgrenzen oder Prozessknoten. Jeder Faktor >10x gegenueber kommerziell verfuegbarem Silizium ist bis zum Beweis eine Messdefinitions-Frage.
3. **Analog-/Mixed-Signal-Fluch:** Device-Mismatch, PVT- und Temperaturempfindlichkeit, Weight-Drift. Loesungen (Per-Die-Kalibrierung, On-Chip-Learning) kosten Flaeche, Testzeit und Geld — genau dort, wo Volumen-Oekonomie entsteht.
4. **Design-Win-Zyklus:** 12-24 Monate bis zum Design-Win, Revenue 1-2 Jahre spaeter. Startups unterschaetzen das systematisch; das Financial Model ist der Lackmustest.
5. **Toolchain-Adoption:** Exotische Architekturen scheitern haeufiger an fehlender Software-Ergonomie als an Silizium. Wenn kein externer Entwickler ohne Handhaltung etwas bauen kann, ist das Produkt nicht verkaufsfaehig.
6. **Single-Source-Prozess:** Bindung an einen Spezialprozess oder eine Foundry ist ein existenzielles Risiko — sowohl fuer Verfuegbarkeit als auch fuer OEM-Kunden, die Second Source verlangen.
7. **Incumbent-Integration:** Sensor-, Mikrofon-, Bildsensor- und RF-Incumbents integrieren Compute vertikal oder kaufen es zu. Das Zeitfenster zwischen Startup-Beweis und Incumbent-Antwort ist kurz.
8. **Kapitalintensitaet:** Jeder Spin kostet Maskensatz + Zeit. Chip-Startups sterben typisch nicht am Markt, sondern zwischen zwei Tape-outs am Cash.
9. **Uni-IP-Herkunft:** Bei Spin-outs ist die Kernfrage Assignment vs. Lizenz. Eine Lizenz mit Reach-through, Feld-Beschraenkung oder Kuendigungsrecht ist ein Deal-Breaker-Kandidat und wird oft erst in der Legal-DD sichtbar.
10. **Produktionserfahrung im Team:** Forschungs-Tape-outs und Serienproduktion sind verschiedene Berufe. Fehlt jemand mit Volumen-Erfahrung, ist der Weg zum Produkt deutlich laenger als geplant.

## Benchmarks
- **Typische Pre-Seed (EU, vor Silizium):** 1-3 Mio EUR
- **Typische Seed (EU, mit vermessenem Erst-Silizium):** 4-12 Mio EUR; US 8-20 Mio USD
- **Pre-Money Seed:** 10-30 Mio EUR (EU), 20-50 Mio USD (US) — Silizium-Nachweis und bezahlte Design-Wins sind die Haupttreiber
- **Series A:** typisch erst mit mehreren Design-Wins oder erster Serienlieferung; 15-40 Mio EUR
- **Gesunde Bruttomarge fabless:** 50-65% (Chip-Sales); IP-Licensing deutlich hoeher, aber mit viel kleinerer Basis
- **Zeit Erst-Tape-out → qualifiziertes Produkt:** 18-36 Monate, 1-3 Spins
- **Design-Win-Zyklus:** 12-24 Monate; Revenue 1-2 Jahre nach Design-Win
- **Full-Mask-Set (Groessenordnung):** 28nm ~1-2 Mio USD, 40/65nm ~300-800k USD, 130/180nm ~100-300k USD; MPW-Shuttle-Slots ab ~10-100k EUR
- **EDA-Toolchain:** 100-500k EUR p.a. fuer ein kleines Analog-/Digital-Team (Startup-Programme reduzieren, aber eliminieren das nicht)
- **Gutes Signal:** bezahltes NRE oder Design-Win-Vertrag statt Eval-Kit-Anfragen; publizierte Messung auf einer anerkannten Konferenz (ISSCC/VLSI) statt nur Marketing-Zahlen
