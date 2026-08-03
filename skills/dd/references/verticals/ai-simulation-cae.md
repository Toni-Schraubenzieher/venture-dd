---
name: ai-simulation-cae
label: AI-native Simulation & CAE (Surrogatmodelle, GPU-Solver, generatives Design, Simulations-Plattformen)
description: Startups die Ingenieurssimulation beschleunigen oder ersetzen — neuronale Surrogate, GPU-native Solver, differenzierbare Physik, automatisches Meshing, Design-Optimierungs-Loops — und das als Software an Engineering-Organisationen verkaufen
keywords: [CAE, CFD, FEA, FEM, simulation, simulationssoftware, solver, multiphysics, multiphysik, thermal, thermisch, heat transfer, waermeuebertragung, conjugate heat transfer, aerodynamics, aerodynamik, RANS, LES, DNS, turbulence, mesh, meshing, vernetzung, surrogate, surrogatmodell, neural operator, FNO, DeepONet, PINN, physics-informed, differentiable physics, differenzierbare physik, physics AI, foundation model physics, generative design, topology optimization, topologieoptimierung, design space exploration, digital twin, digitaler zwilling, GPU-accelerated, OpenFOAM, SU2, Ansys, Fluent, Icepak, Simcenter, Flotherm, StarCCM, COMSOL, Abaqus, Altair, Cadence Celsius, engineering software, PLM, CAD]
---

# Vertical: AI-native Simulation & CAE

## Kontext
In der Ingenieurssimulation ist das verkaufte Gut nicht Geschwindigkeit, sondern **Vertrauen**: Simulationsergebnisse gehen in Design-Freigaben, Zertifizierungsdossiers und Lieferantenspezifikationen ein. Ein Werkzeug, das 1000x schneller ist, dessen Zahl aber im Design-Review nicht verteidigt werden kann, hat den Wert null — das erklaert, warum diese Kategorie eine lange Liste gut finanzierter Firmen und sehr wenig Enterprise-Umsatz hat. Die haeufigsten Investorenfehler: (1) **Speedup-Faktoren als Produktwert lesen** — fast jeder Claim vergleicht Ungleiches (Open-Source-CPU-Solver gegen eigene GPU-Implementierung, oder ein trainiertes Surrogat auf In-Distribution-Geometrie gegen einen vollstaendigen Solve); die drei Zahlen, auf die es ankommt — Baseline, Hardware, **Accuracy** — fehlen in der Schlagzeile meist alle drei. (2) **Surrogat und Solver verwechseln** — zwei verschiedene Produkte mit verschiedenen Risikoprofilen: ein Surrogat ist schnell, aber nur innerhalb seiner Trainingsverteilung gueltig; ein GPU-Solver ist allgemein, aber sein Vorteil ist durch Hardware gedeckelt, die die Incumbents ebenfalls haben. Wer beides behauptet, hat meist keines validiert. (3) **Pilot als Umsatzsignal** — in CAE heisst "Pilot" fast immer, dass ein F&E-Ingenieur Budget fuer einen Vergleich bekommen hat; der Weg zur Lizenz fuehrt ueber die Methodenabteilung und die IT, nicht ueber den begeisterten Ingenieur. (4) **Den Sign-off-Graben unterschaetzen** — bevor ein neues Verfahren in eine Entscheidung einfliessen darf, laeuft beim Kunden eine interne Validierungskampagne; die beginnt *nach* dem technischen Beweis und ist der eigentliche Sales Cycle. (5) **Incumbent-Bundling ignorieren** — Ansys, Siemens, Cadence, Altair und Dassault liefern AI- und GPU-Features in eine Suite, die der Kunde bereits besitzt und validiert hat. (6) **NVIDIA als Partner lesen statt als Plattformrisiko** — PhysicsNeMo/Modulus, Omniverse und der CUDA-X-Stack druecken genau diesen Layer Richtung Gratis-Bibliothek; eine Inception-Mitgliedschaft ist kostenlos und sagt nichts. Gute Deals haben einen Accuracy-Claim mit Fehlerbalken gegen einen oeffentlichen Referenzfall, mindestens ein **bezahltes** Deployment jenseits des Pilots mit einer Methodenabteilung als Sponsor, Integration in die bestehende CAD/PLM-Kette des Kunden, und jemanden im Team, der Simulationsmethodik in einer grossen Engineering-Organisation verantwortet oder verkauft hat.

## Extraction Focus Areas (Session 3)
- **Produktklasse trennen (Pflicht):** Surrogat/neuronaler Operator · GPU-nativer Solver · Optimierungs-/Design-Loop · Meshing/Preprocessing · Full-Stack-Plattform. Pro Komponente: gebaut / in Arbeit / Roadmap. **Decks zeigen die Plattform, ausgeliefert wird meist eine Komponente.**
- **Benchmark-Methodik woertlich extrahieren:** Testcase (oeffentlich und reproduzierbar?), Baseline-Solver samt Version, Baseline-Hardware **vs.** eigene Hardware, Zellzahl/Mesh-Groesse, Physik (RANS/LES/konjugierte Waermeuebertragung/transient), Konvergenzkriterium, **Accuracy-Metrik gegen Referenz oder Experiment**, Definition der Wall-Time (inkl. oder exkl. Meshing, Setup, Training). *Speedup ohne Accuracy ist keine Zahl.*
- **Trainingsdaten-Herkunft und -Kosten:** Wie viele Solves, auf wessen Hardware, wessen Geometrien? Kundendaten (Nutzungsrechte schriftlich?), eigene Solves (Compute-Kosten = versteckte COGS), oeffentliche Datensaetze. Darf das trainierte Modell bei anderen Kunden eingesetzt werden?
- **Generalisierungs-Grenze:** Fuer welche Geometrieklassen, Randbedingungen und Kennzahlbereiche gilt das Modell? Was passiert ausserhalb — Fehler, Warnung, oder **still falsches Ergebnis**? Gibt es eine Unsicherheitsschaetzung pro Vorhersage?
- **Physik-Abdeckung pro Anwendungsfall:** Konduktion / Konvektion (natuerlich vs. erzwungen) / Strahlung / konjugierte Waermeuebertragung / Phasenwechsel / stationaer vs. transient / gekoppelt elektro-thermisch. Breite Thermal-Claims kollabieren oft auf "stationaere erzwungene Konvektion an einfacher Geometrie".
- **Integrationstiefe:** CAD-Formate (natives Parasolid/STEP/JT vs. nur STL), PLM/PDM-Anbindung, Skript-/API-Zugang, On-Prem vs. Cloud. Enterprise-Engineering ist ueberwiegend On-Prem oder Private-Cloud — SaaS-only scheitert regelmaessig an IT, Datenhoheit und Exportkontrolle.
- **Kunden-Konkretisierung:** Pro Logo: welche Abteilung (F&E-Innovationsgruppe vs. Methodenabteilung vs. produktverantwortliches Team), wer haelt das Budget, bezahlt/unbezahlt, Vertragsform (kostenloser PoC / bezahlter PoC / Pilot-PO / Rahmenvertrag / Produktionslizenz), Laufzeit, Verlaengerungsstatus. **Ein Zitat eines begeisterten Ingenieurs ist kein Kunde.**
- **Sign-off-Status:** Darf ein Ergebnis des Tools heute in eine Freigabeentscheidung einfliessen? Falls nein: was fehlt (interne Validierungskampagne, Methodenfreigabe, Norm/Zertifizierung) und wie lange dauert das beim Kunden?
- **Preis- und Lizenzmodell:** Seats vs. Solver-Token/HPC-Credits vs. Usage vs. Modell-Integrations-NRE. Welche Linie ist im Financial Model? CAE-Kunden sind an Seat+Token gewoehnt — jede Abweichung braucht eine Begruendung.
- **Compute-COGS:** GPU-Stunden pro Kundenauftrag, Trainings- vs. Inferenzkosten, wer traegt sie. Bei "usage-based" ist die Bruttomarge die Kernfrage, nicht der Umsatz.
- **Team-Zusammensetzung:** Wer hat Solver-Entwicklung gemacht, wer ML, wer **CAE-Vertrieb oder Methodik in einer grossen Engineering-Organisation**? Die dritte Kompetenz fehlt fast immer und ist die verkaufsentscheidende.

## Cross-Referencing Checks (Session 4)
- [ ] **Speedup selbst zerlegen, nicht diskutieren:** Hardware-Faktor (Baseline-CPU-Knoten vs. eigene GPU nach oeffentlichen Peak-Zahlen) x Solver-Baseline-Faktor (Open-Source vs. bester kommerzieller Solver) x Methodenfaktor (Surrogat statt Solve). Erst der Rest ist Innovation. Praxis: aus dreistelligen Faktoren werden gegen den besten kommerziellen GPU-Solver haeufig einstellige.
- [ ] **Baseline-Fairness:** Ist die Baseline ein Open-Source-Solver (SU2, OpenFOAM) auf CPU? Dann ist der Vergleich gegen das, was der Kunde tatsaechlich einsetzt (Fluent, Star-CCM+, Flotherm, Icepak, Flow360), **nicht gefuehrt**. Nachfordern.
- [ ] **Mehrere Speedup-Zahlen im selben Material:** Misst jede Zahl Solver oder Surrogat? Ist eine Trainingszeit amortisiert oder ausgeblendet? Widerspruch explizit aufloesen, nicht mitteln.
- [ ] **Positionierung Deck vs. Website vs. Doku:** Nischen-Claim ("thermal-first", "nur fuer X") gegen die eigene Aussendarstellung pruefen. Ein Nischen-Claim im Deck bei generischer Website ist ein Segmentierungs-Widerspruch, kein Detailfehler — und trifft die Differenzierung im Kern.
- [ ] **Wettbewerbsmatrix gegen Realitaet:** Jeden als "general purpose" oder "validation only" abgetanen Wettbewerber einzeln pruefen. Thermal-native Incumbent-Produkte (Flotherm, FloEFD, Icepak, Celsius, 6SigmaDCX) und AI-Thermal-Startups (Diabatix, ToffeeX) werden regelmaessig falsch einsortiert. **Jede Einordnung muss zitierbar belegt sein.**
- [ ] **ACV gegen CAE-Realitaet:** Behaupteten Account-Wert gegen tatsaechliche Seat- und Suite-Preise stellen. Siebenstellige Accounts existieren — bei Anbietern mit jahrzehntelanger Validierungshistorie und breiter Physik-Abdeckung.
- [ ] **Pilot→Lizenz-Konversion:** Welche Rate und welchen Zeitraum unterstellt das Model? Gegen den Sign-off-Graben beim Kunden stellen, nicht gegen die Begeisterung im Pilot.
- [ ] **Grants vs. Revenue:** Sind Foerdermittel als Umsatz gebucht? Getrennt ausweisen. Grant-Bewilligung ist extern validiert, der Antragsinhalt bleibt Founder-Behauptung.
- [ ] **Pilot-Herkunft vs. Team-Historie:** Stammen Pilotkunden aus dem frueheren Arbeitgeber eines Gruenders? Warme Leads sind wertvoll, aber keine Marktvalidierung — und die Konzentration ist ein eigenes Risiko.
- [ ] **Compute-COGS im Model:** Ist GPU-Kost hinterlegt, oder ist Usage-Umsatz als reine Marge modelliert? Startup-Credits (Inception, AWS Activate) laufen aus — mit Listenpreisen rechnen.
- [ ] **Roadmap-Breite vs. Teamgroesse:** Differenzierbare Physik, Foundation-Modell, automatisches Meshing und GPU-Solver sind je ein eigenes Forschungsprogramm. Anzahl Personen gegen Anzahl offener Forschungsfronten stellen.
- [ ] **Inhouse-Substitution:** Betreibt der Zielkunde eigene Solver-Entwicklung? Viele Grosskonzerne haben Inhouse-Codes und Methodenabteilungen — das ist ein Substitutionsrisiko, kein Kunde.

## Unit Economics Calculations (Session 4 Phase 2)
1. **Speedup-Zerlegung:** Gesamtfaktor ÷ Hardware-Faktor ÷ Solver-Baseline-Faktor = verbleibender Methodenfaktor. Diese Zahl ist die eigentliche Technologie-Aussage.
2. **Amortisierter Surrogat-Vorteil:** (Trainings-Solves x Kosten je Solve + Trainingskosten) ÷ Anzahl Inferenzen im Projekt + Inferenzkosten, gegen die Kosten direkter Solves. Bei wenigen Auswertungen je Geometrie ist ein Surrogat oekonomisch **negativ**.
3. **Compute-Bruttomarge:** (Usage-Umsatz − GPU-Kost) ÷ Usage-Umsatz, zu Cloud-Listenpreisen.
4. **Effektiver ACV:** Seats x Seat-Preis + Token/Usage + Integrations-NRE — gegen den behaupteten Account-Wert.
5. **Pilot→Lizenz-Trichter:** Anzahl Pilots x eigene Konversionsannahme x ACV. Rate selbst setzen (siehe Benchmarks), nicht uebernehmen.
6. **Runway bis zum naechsten harten Beweis:** Cash ÷ Burn gegen die Zeit bis zur **ersten bezahlten Produktionslizenz** — nicht bis zum naechsten Pilot.
7. **Ersatzkostenrechnung des Kunden:** Was zahlt der Kunde heute fuer dieselbe Antwort (Lizenz + HPC + Ingenieurstunden)? Der erzielbare Preis liegt darunter — nicht beim behaupteten Wert der Zeitersparnis.

## Research Blocks (Session 5, Bloecke 2-4)

### Block 2: Markt, Beschaffung & Adoptionsbremsen
Web-Recherche (Englisch):
- Reale CAE-Marktzahlen aus mehreren Analystenquellen. TAM-Zahlen in Decks mischen regelmaessig "engineering software" (inkl. CAD/PLM/EDA) mit CAE — beides trennen
- Wie CAE tatsaechlich beschafft wird: Rahmenvertraege, Multi-Year-Suiten, Token-Pools; wer entscheidet (Methodenabteilung, IT, Einkauf) und in welcher Reihenfolge
- V&V- und Normbindung im Zielsegment (ASME V&V 10/20/40, Aero-Zulassung, IEC/UL im Elektrobereich, VDA/AIAG in Automotive) — was blockiert die Einfuehrung eines neuen Verfahrens konkret
- On-Prem- und Datenhoheitsanforderungen bei Industriekunden; Exportkontrolle bei Aero-/Defense-Geometrien
- Historie der Kategorie: welche AI-CAE-Firmen haben belegbaren Umsatz erreicht, welche wurden uebernommen und zu welchem Preis, welche sind trotz hoher Finanzierung stehengeblieben — und woran

### Block 3: Kunden, Kaufverhalten & Preis-Benchmarks
Web-Recherche:
- Wer kauft im Zielsegment tatsaechlich (Firmen, Abteilungen)? Wie konzentriert ist die Nachfrage?
- Publizierte Seat- und Suite-Preise der Incumbents; typische Token-/HPC-Credit-Modelle
- Oeffentlich belegte, **bezahlte** AI-CAE-Deployments bei Tier-1-Industrieunternehmen — Primaerquellen (namentliche Case Studies, Konferenzvortraege von Kundenseite), nicht Anbieter-Marketing
- Typische Sales-Cycle-Laengen und Pilot→Lizenz-Konversion in Engineering-Software
- Welche Zielkunden betreiben eigene Solver-Entwicklung oder starke Methodenabteilungen (Substitutionsrisiko)

### Block 4: Technologie- und Benchmark-Verifikation
Web-Recherche:
- Publizierte Referenzergebnisse des genannten Testcases (Workshop-Proceedings, NASA/AIAA-Datensaetze, Validierungsdatenbanken). Accuracy-Claim dagegen pruefen — oder die Luecke **als Luecke** ausweisen statt zu schaetzen
- Publizierte Performance kommerzieller GPU-Solver (Fluent GPU, Flow360, Simcenter, Cadence Millennium) als faire Baseline
- Stand der Forschung zu neuronalen Operatoren und Surrogaten: bekannte Generalisierungsgrenzen, Out-of-Distribution-Verhalten, Fehlerschaetzung. Primaerliteratur, keine Blogposts
- Reifegrad differenzierbarer CFD und automatischen Meshings — wo steht das Feld, wer betreibt es produktiv
- NVIDIA-Stack (PhysicsNeMo/Modulus, Omniverse, cuDSS/AmgX): welche Teile der Wertschoepfung wandern in kostenlose Bibliotheken?
- Patentlage der Incumbents in AI-gestuetzter Simulation; Freedom-to-Operate

## Risk Framework
1. **Benchmark-Inflation:** Jeder Faktor >10x gegen den besten **kommerziell verfuegbaren** Solver ist bis zum Beweis eine Messdefinitions-Frage. Ein Founder, der die Wettbewerbszahl unaufgefordert selbst nennt, ist ein starkes Positivsignal — auch wenn der Faktor dabei schrumpft.
2. **Stiller Fehler:** Der gefaehrlichste Fehlermodus in CAE ist nicht der Absturz, sondern die plausible falsche Zahl. Ein Surrogat ohne Fehlerschranke und ohne Out-of-Distribution-Erkennung ist im Sign-off-Workflow nicht einsetzbar — unabhaengig von seiner Geschwindigkeit.
3. **Sign-off-Graben:** Der eigentliche Sales Cycle beginnt **nach** dem technischen Beweis, mit der Validierungskampagne des Kunden. Financial Models unterstellen fast immer den technischen Zeitpunkt als Vertragszeitpunkt.
4. **Incumbent-Bundling:** Ansys, Siemens, Cadence, Altair und Dassault liefern AI-/GPU-Features in bereits gekaufte und validierte Suiten. Das Startup muss gut genug sein, um einen neuen Lieferanten, eine neue Validierungskampagne und eine neue Budgetposition zu rechtfertigen.
5. **Plattformrisiko NVIDIA:** Der GPU-Solver- und Physics-AI-Layer wandert schrittweise in kostenlose Bibliotheken. Was heute Differenzierung ist, kann in 24 Monaten Infrastruktur sein.
6. **Pilot-Falle:** Innovationsbudgets sind leicht zu gewinnen und versiegen zuverlaessig. Produktionsbudgets haben andere Entscheider, andere Prozesse und andere Zeitraeume.
7. **Forschungsfronten-Ueberdehnung:** Differenzierbare Physik, Foundation-Modelle, automatisches Meshing und GPU-Solver gleichzeitig — bei kleinem Team heisst das, dass keines davon fertig wird.
8. **Integrations-Insel:** Ohne Anbindung an CAD/PLM und die bestehende Toolkette bleibt jedes Ergebnis ein Demo-Artefakt, das niemand weiterverarbeiten kann.
9. **Compute-Marge:** Usage-basierter Umsatz mit durchgereichten GPU-Kosten ist Umsatz ohne Marge. Bei Startup-Credits wird das erst nach deren Auslaufen sichtbar.
10. **Inhouse-Substitution:** Grosskonzerne mit eigener Solver-Entwicklung bauen nach, statt zu kaufen — und haben die Domaenendaten dafuer.
11. **Domaenen-Vertriebsluecke:** Ein Team aus Solver- und ML-Leuten ohne jemanden, der Simulationsmethodik in einer grossen Engineering-Organisation verantwortet hat, verkauft an den falschen Ansprechpartner.

## Benchmarks
*Groessenordnungen zur Kalibrierung — im konkreten Deal ueber Block 3 verifizieren, nicht ungeprueft zitieren.*
- **Pre-Seed (EU/UK, Prototyp, unbezahlte Pilots):** ~0,5-2,5 Mio GBP/EUR
- **Seed (erste bezahlte Deployments):** ~3-10 Mio EUR
- **Series A:** erst mit belastbarem ARR aus Produktionslizenzen, nicht aus Pilots
- **Kommerzielle CFD-/Thermal-Seats:** hoher vierstelliger bis mittlerer fuenfstelliger Betrag p.a. je Seat, abhaengig von Suite und Parallelisierung; HPC-/Solver-Token separat
- **Realistische Erst-ACVs fuer ein Startup:** fuenfstellig bis niedrig sechsstellig. Siebenstellige Accounts sind Incumbent-Territorium und brauchen eine sehr gute Begruendung
- **Sales Cycle Enterprise-Engineering:** ~9-24 Monate von Erstkontakt bis Produktionslizenz; Validierungskampagne beim Kunden zusaetzlich ~6-18 Monate
- **Pilot→bezahlte Lizenz:** realistisch im niedrigen einstelligen bis niedrigen zweistelligen Prozentbereich. Modelle mit >50 % sind zu hinterfragen
- **Gutes Signal:** Accuracy-Claim mit Fehlerbalken gegen einen oeffentlichen Referenzfall; bezahlte Lizenz mit einer Methodenabteilung als Sponsor; Integration in die bestehende Toolkette; ein Founder, der die faire Baseline selbst nennt
- **Schwaches Signal:** Inception-/Startup-Programme, Grants, unbezahlte PoCs, Kundenzitate im Konjunktiv ("can help", "shows promise"), Logo-Walls ohne Vertragsform
