---
name: defense-ai-software
label: Defense & National Security AI Software (inkl. ISR/Intelligence-Processing, C2, Data Fusion, Autonomy Software, Mission Software)
description: Startups die Software/AI-Modelle an Verteidigungs-, Nachrichtendienst- oder Sicherheitsbehoerden verkaufen — direkt oder ueber Primes. Kein Hardware-Primaerprodukt.
keywords: [defence, defense, national security, military, ISR, SIGINT, COMINT, ELINT, HUMINT, IMINT, GEOINT, OSINT, MASINT, intelligence, TPED, PED, processing and exploitation, targeting, C2, C4ISR, battle management, situational awareness, data fusion, sensor fusion, order of battle, EOB, mission software, autonomy software, electronic warfare, dual-use, NATO, MOD, DoD, FVEY, TAK, ATAK, STANAG, TRL, JOSCAR, DASA, DSTL, DIANA, EDF, SBIR, security clearance, List X, accreditation, air-gap, classified, export control, ITAR, EAR]
---

# Vertical: Defense & National Security AI Software

## Kontext
Defense-Software wird nicht von einem Budget-Halter gekauft, sondern von einer Beschaffungsbuerokratie — der Nutzer, der Entscheider und der Zahler sind drei verschiedene Organisationen mit unterschiedlichen Anreizen. Der eigentliche Todesstreifen ist nicht der erste Vertrag, sondern **Pilot → Program of Record**: Innovationsbudgets (DASA, DIANA, SBIR, Experimentiertoepfe) sind vergleichsweise leicht zu gewinnen und versiegen zuverlaessig, waehrend die echte Beschaffungslinie einen anderen Prozess, andere Entscheider und 24-48 Monate braucht. Die haeufigsten Investoren-Fehler: (1) Grants, OTAs und Innovation-Contracts als ARR werten, (2) aggregierte TRL-Claims akzeptieren statt pro Komponente UND pro Einsatzumgebung zu disaggregieren, (3) anonymisierte Kunden ("ein NATO-Mitgliedsstaat", "eine multinationale Verteidigungsorganisation") als verifizierte Traction akzeptieren, wo OPSEC als Verifikations-Blocker instrumentalisiert wird, (4) den Accreditation-/Clearance-Graben unterschaetzen — ein Produkt, das nicht in der klassifizierten Enklave laufen darf, ist im ernsthaften Use Case heute nicht lieferbar, (5) Commodity-Modell-Bausteine (ASR, Uebersetzung, Entity-Extraction, Graph) fuer einen Moat halten, (6) konflikt-gekoppelte Traction linear in Friedenszeiten extrapolieren. Gute Deals haben ein Program of Record oder einen benennbaren Pfad dorthin, belegten Accreditation-Status, proprietaere Domaenendaten mit sauberer Rechtekette, und mindestens eine Person mit echtem Beschaffungszugang im Kernteam.

## Extraction Focus Areas (Session 3)
- **Kunden-Konkretisierung & Anonymisierungsgrad:** Pro Kunde die tatsaechlich beschaffende Entitaet erfassen (z.B. "UK MOD Strategic Command", "DSTL", "DASA Project X", "NATO NCIA", "BAES als Prime fuer Programm Y") vs. Marketing-Wording. Anonymisierungsgrad als eigenes Feld extrahieren — nicht stillschweigend uebernehmen
- **Vertragsform pro Kunde:** Grant / Innovation-Contract (DASA, DIANA, SBIR, EDF) / OTA / Pilot-PO / Framework / **Program of Record** / Subcontract unter Prime. Plus: Laufzeit, Gesamtvolumen, Jahreswert, Kuendigungsrechte, Verlaengerungsoptionen, Exklusivitaet
- **Klassifizierungsstufe pro Deployment:** Unclassified / OFFICIAL / OFFICIAL-SENSITIVE / SECRET / NATO SECRET. Dazu: Air-Gap ja/nein, wer betreibt (Kunde vs. Startup), Accreditation-Status (nicht begonnen / in Arbeit / erteilt), ATO-Datum
- **Clearance-Inventur:** Welche Person haelt welche Clearance (SC / DV / NATO SECRET / aequivalent), Facility Clearance (List X o.ae.), Staatsangehoerigkeiten und Wohnsitz-Historie des Teams gegen die Clearance-Anforderungen der Zielmaerkte
- **TRL disaggregiert:** Pro Komponente UND pro Umgebung (Lab / repraesentativ / Feld / operationell-akkreditiert). **Nie einen aggregierten Produkt-TRL uebernehmen** — siehe `taxonomies.md` TRL-Disaggregation
- **Modell-Provenienz:** Pro Modell: eigene Weights / Fine-Tune auf welchem Base-Model (Lizenz!) / API-Call an Dritte. Bei API-Abhaengigkeit pruefen, ob das im klassifizierten oder air-gapped Netz ueberhaupt funktioniert — sonst faellt der Deployment-Claim
- **Trainingsdaten-Provenienz & Rechtekette:** Operative Kundendaten (vertragliche Nutzungsrechte schriftlich?), synthetische Daten, oeffentliche Korpora, Konflikt-Daten. Darf das Startup Kundendaten zur Modellverbesserung nutzen und die Ergebnisse an andere Kunden verkaufen?
- **Interop-Status:** TAK (ATAK/WinTAK/CivTAK), STANAG-Familie (4559 CSD, 4774/4778 Labelling, 4609), Link-16, NATO NVG, C2-Bestandssysteme (SitaWare, Delta, Maven Smart System). Pro Integration: demonstrated / deployed / zertifiziert
- **Export-Control-Klassifikation:** UK ECO 2008 Rating, EU 2021/821 Annex I, US EAR/ITAR-Beruehrung (auch ueber Komponenten und US-Personal), eingesetzte Kryptografie (Cat 5 Part 2)
- **Non-dilutive Funding:** Pro Grant: Betrag, Status (beantragt/bewilligt/ausgezahlt), IP-Konsequenzen, Match-Funding-Pflicht, Government Purpose Rights
- **Personal & Betrieb in Konfliktgebieten:** Standorte, Wehrpflicht-Exposure der Mitarbeiter, Business-Continuity, IP-Ownership-Kette ueber Landesgrenzen

## Cross-Referencing Checks (Session 4)
- [ ] **Kunden-Konkretisierung:** Laesst sich zu mindestens einem Kunden die beschaffende Entitaet benennen — notfalls muendlich unter NDA gegenueber dem Investor? Wenn zu **keinem** Kunden eine konkrete Entitaet benannt wird, ist das ein Signal, kein OPSEC
- [ ] **"Paying customer" quantifizieren:** Jahreswert pro Kunde. Ein GBP 30k-Pilot und ein GBP 3M-Programm sind beide "paying customers" — die Zaehlweise im Deck gegen die Vertragswerte stellen
- [ ] **Pilot-Purgatory-Quote:** Anzahl gestarteter Pilots vs. Anzahl in Folgevertraege konvertierter, ueber Zeit. Ohne Konversionen ist die Pipeline ein Karussell
- [ ] **TRL-Claim vs. Deployment-Evidenz:** TRL 9 heisst operationell im Zielsystem qualifiziert — nicht Lab-Demo, nicht Exercise, nicht Feldversuch. Gegen die tatsaechliche Einsatz-Evidenz stellen
- [ ] **Accreditation vs. behaupteter Use Case:** Wenn der Use Case klassifizierte Daten verarbeitet, das Produkt aber keine Accreditation fuer diese Stufe hat, ist der behauptete Kundennutzen **heute nicht lieferbar**. Diskrepanz explizit dokumentieren
- [ ] **Clearance-Deckung vs. Zielmarkt:** Nationalitaeten/Wohnsitze gegen die Regeln des Zielmarkts (UK SC verlangt i.d.R. mehrjaehrigen Aufenthalt, DV mehr, einzelne Programme sole nationality). Sperrt die Teamzusammensetzung den adressierten Markt?
- [ ] **Exercise ≠ Operation:** "deployed on exercise" ist Marketing-faehig, aber kein Beschaffungssignal. Beide Kategorien getrennt fuehren
- [ ] **Prime-Abhaengigkeit:** Wenn ein Prime der Kanal ist — wer haelt die Endkunden-Beziehung, gibt es Exklusivitaet, kann der Prime die Faehigkeit nachbauen oder das Startup gegen einen Wettbewerber austauschen?
- [ ] **Grant-Revenue-Trennung:** Werden Grants/Innovation-Contracts im Revenue ausgewiesen? Kommerzielles Revenue separat rechnen
- [ ] **Budgetlinie vs. Innovationstopf:** Existiert eine echte Beschaffungslinie fuer diese Kategorie beim Kunden, oder wird aus Experimentierbudget bezahlt? Letzteres hat eine Halbwertszeit
- [ ] **Konflikt-Kopplung:** Welcher Anteil von Traction und Pipeline haengt an einem aktiven Konflikt? Waffenstillstands-Szenario durchspielen
- [ ] **Modell-Abhaengigkeit vs. Deployment-Umgebung:** Frontier-API-Abhaengigkeit im Stack vs. Air-Gap-/On-Prem-Claim — beides gleichzeitig geht nicht
- [ ] **Modell-Lizenzlage:** Viele Open-Weights-Lizenzen schliessen militaerische Nutzung explizit aus. Pro Base-Model die Lizenz gegen den tatsaechlichen Einsatz pruefen
- [ ] **Zertifikats-Huerde einordnen:** JOSCAR-*Registrierung*, NVIDIA Inception, Cyber Essentials (Basic) sind niedrigschwellig und keine Beschaffungsqualifikation. Gegen echte Qualifikationen (List X, ATO, Framework-Aufnahme, DSP) abgrenzen

## Unit Economics Calculations (Session 4 Phase 2)
1. **Echter ACV pro Kunde:** Gesamtvertragswert / Laufzeit in Jahren, Grants und Innovation-Contracts separat ausgewiesen. Summe gegen die im Deck genannte "paying customers"-Zahl stellen
2. **Program-of-Record-Rueckwaertsrechnung:** Ziel-ARR / realistischer PoR-ACV = benoetigte Programme. Benoetigte Programme / konservative Pilot→PoR-Konversion (10-20 %) = benoetigte Pilots. Mal Sales-Cycle = benoetigte Jahre. Gegen Runway und Team-Kapazitaet stellen
3. **Compute- & Deployment-COGS:** Training-GPU + Inferenz + bei On-Prem/Air-Gap die ausgelieferte Hardware und der Field-Support. Wer zahlt die Edge-Hardware? Echte Gross Margin rechnen, **nicht** SaaS-Standard 85 % annehmen
4. **Accreditation- & Clearance-Kosten:** Kosten UND Dauer fuer Facility Clearance, Personen-Clearances und ATO gegen die Runway stellen. Dieser Posten fehlt in Modellen fast immer und ist gleichzeitig Cash- und Zeit-Blocker
5. **Konzentrations-Risiko doppelt:** Groesster Endkunde als % des Revenue UND groesster Kanal (Prime/Integrator) als % — beide separat. >30 % ist bei fruehen Defense-Deals normal, dauerhaft >50 % ist strukturell
6. **Non-dilutive-Abhaengigkeit:** Grants als % der Gesamtfinanzierung. Hoher Anteil kann Validierung (Stärke) oder fehlenden kommerziellen Pull (Schwaeche) bedeuten — ueber die kommerziellen Vertraege aufloesen

## Research Blocks (Session 5, Bloecke 2-4)

### Block 2: Beschaffung, Regulierung & Budgetlinien
Web-Recherche (Englisch):
- Verteidigungshaushalte der Zielmaerkte und **konkrete Programm-/Budgetlinien** fuer diese Faehigkeitskategorie — nicht "Defense-AI-Markt CAGR" (die Zahl ist fuer die Beschaffungsrealitaet wertlos)
- Beschaffungsvehikel und typische Vertragsgroessen: DASA, DSTL, UK Defence Innovation, NATO DIANA + NATO Innovation Fund, EDF/EDIP/ASAP, nationale Innovationsagenturen, DIU/SBIR im US-Fall
- Export-Kontrolle und Investment-Screening: UK Export Control Order 2008, EU 2021/821, ITAR/EAR, UK NSI Act und EU-FDI-Screening — Auswirkung auf zulaessige Investoren-Struktur **und spaetere Exit-Faehigkeit**
- Accreditation-Regime, Dauer und Kosten: MOD Secure by Design, JSP 604/440, NCSC-Guidance, NATO-Akkreditierung, US ATO/RMF
- Politische Zyklen: Defence Reviews, Regierungswechsel, Eskalations-/Waffenstillstands-Szenarien in den relevanten Theatern
- Wie kaufen Behoerden Software: Perpetual vs. Subscription vs. Enterprise Agreement; darf der Kunde SaaS im klassifizierten Bereich ueberhaupt beschaffen?

### Block 3: Kunden, Programme & Referenz-Verifikation
Web-Recherche:
- **Oeffentliche Vertragsdatenbanken** nach dem Startup UND nach jedem Wettbewerber durchsuchen: UK Contracts Finder, Find a Tender, TED, USASpending/FPDS, NATO NCIA-Ausschreibungen, nationale Vergabeportale
- Programs of Record in der Kategorie: wer haelt sie, Laufzeitende, naechster Recompete — das ist das eigentliche Zeitfenster fuer einen Angreifer
- Referenz-Verifikation: genannte Exercises (Name, Datum, Teilnehmer oeffentlich?), Prime-Partnerschaften (Pressemitteilungen beider Seiten), Supplier-Register (JOSCAR/Hellios), Framework-Listungen
- Beschaffungsweg der Zielorganisation: Entscheider, typische Dauer Pilot→Vertrag, wer hat Budgethoheit
- Bestandssysteme im Feld beim Zielkunden und der realistische Abloese- oder Ergaenzungspfad
- Wettbewerber-Funding und -Vertragslage (nicht nur Funding — Vertraege sind das haertere Signal)

### Block 4: Technologie, Modell-Landschaft & Replizierbarkeit
Web-Recherche:
- State of the Art fuer die Kernfaehigkeit und **wo genau er versagt** (z.B. bei ASR/Translation: Whisper-Klasse, SeamlessM4T, kommerzielle Anbieter — Versagen bei Noise, Low-Resource-Sprache, Domaenen-Slang, Codewoertern). Genau dort muesste der Moat liegen
- Open-Weights-Landschaft und **Lizenzlage fuer militaerische Nutzung** — viele Lizenzen schliessen sie aus
- Domaenen-Datensaetze: existieren oeffentliche oder lizenzierbare Korpora fuer diese Domaene? Wenn ja, ist der behauptete Datenmoat schwaecher als dargestellt
- Interop-Huerde real bewerten: TAK-Oekosystem, STANAG-Familie, Link-16, NATO NVG — ist die Integration ein Moat oder ein Wochenendprojekt?
- **Replikations-Schaetzung:** Team + Zeit + Kosten fuer eine vergleichbare Faehigkeit. Was davon kann ein Prime, Palantir, Anduril oder Helsing als Feature nachschieben — und in welchem Zeitfenster?

## Risk Framework
1. **Pilot Purgatory:** Pilots konvertieren nicht in Programs of Record. Innovationsbudget ist nicht Beschaffungsbudget, und der Uebergang hat andere Entscheider
2. **Accreditation-Graben:** Ohne Akkreditierung fuer die Zielklassifizierung ist der Kern-Use-Case nicht lieferbar. Dauer und Kosten werden systematisch unterschaetzt
3. **Clearance-/Nationalitaets-Gate:** Die Teamzusammensetzung kann den adressierten Markt strukturell sperren — unabhaengig von der Produktqualitaet
4. **Feature-vs-Company bei Commodity-Modellen:** ASR, Uebersetzung, Entity-Extraction und Graph-Darstellung sind weitgehend Commodity. Der Moat muss in Domaenendaten, Akkreditierung, Integrationstiefe oder Workflow-Lock-in liegen — pruefen, nicht annehmen
5. **Prime-/Kanal-Abhaengigkeit:** Der Prime kontrolliert die Endkundenbeziehung, kann Konditionen diktieren, nachbauen oder ersetzen
6. **Konflikt-Kopplung:** Traction, die an einem aktiven Konflikt haengt, ueberlebt einen Waffenstillstand selten in derselben Dringlichkeit und Beschaffungsgeschwindigkeit
7. **Export-Control- und FDI-Bremse:** Export-Kontrolle limitiert die adressierbaren Maerkte; NSI Act / FDI-Screening kann Investoren blockieren und den spaeteren Exit-Kaeuferkreis einschraenken
8. **Sovereignty-Fragmentierung:** Jede Nation will nationale Loesungen und Datenhoheit — das zerlegt den adressierbaren Markt und multipliziert die Deployment-Kosten pro Land
9. **Budgetlinien-Risiko:** Eine Faehigkeitskategorie ohne eigene Beschaffungslinie wird aus versiegenden Experimentiertoepfen bezahlt
10. **Data-Rights-Falle:** Ohne vertragliche Rechte an operativen Kundendaten laesst sich der eigene Datenmoat nicht aufbauen. Behoerden fordern zunehmend Government Purpose Rights
11. **Key-Person / Bus-Factor:** Domaenenwissen und Beschaffungszugang haengen oft an einer einzigen Person — Split nach `taxonomies.md` Bus-Factor-Regel
12. **Reputations- und Ethik-Risiko:** Fehlklassifikation mit Targeting-Bezug. Der EU AI Act nimmt militaerische Nutzung aus, aber LP-Restriktionen und Reputationsrisiko bleiben
13. **Cross-Border-Struktur:** Entitaeten, Personal oder IP-Ownership in Konfliktlaendern koennen westliche Beschaffung, Clearances und die Exit-Faehigkeit erschweren

## Benchmarks
- **Typische Seed-Runde (Defense Software EU/UK):** USD 3-8M — 2025/26 durch Sektor-Hype nach oben verzerrt
- **Pre-Money Seed:** USD 12-35M, stark vertragslage-abhaengig; ohne konvertierte Mehrjahresvertraege am unteren Ende
- **Sales Cycle:** 12-24+ Monate Pilot → Vertrag; echte Programm-Beschaffung 24-48 Monate
- **Pilot → Program-of-Record-Konversion:** historisch niedrig — konservativ 10-20 % ansetzen, hoehere Annahmen begruenden lassen
- **Typische Innovation-Contract-Groessen:** DASA Phase 1 GBP 100-300k, NATO DIANA ~EUR 100k + Follow-on, SBIR Phase I USD 100-250k / Phase II USD 1-2M
- **ARR fuer Series A (Defense Software):** USD 1-3M aus **kommerziellen** Mehrjahresvertraegen; Grants nicht mitzaehlen
- **Gross Margin:** 60-80 % — On-Prem-/Air-Gap-Deployment, Field-Support und Accreditation druecken gegenueber dem SaaS-Standard
- **Non-dilutive-Anteil (gesund):** 20-40 % der Gesamtfinanzierung; deutlich darueber ohne kommerzielle Vertraege = fehlender Pull
- **Kundenkonzentration:** bei fruehen Deals sind >30 % normal; dauerhaft >50 % eines Kunden oder Kanals ist strukturell
- **Clearance-Timelines:** UK SC Wochen bis Monate, DV 6-12 Monate; List X Facility Clearance mehrere Monate bis ueber ein Jahr
- **Team-Signal:** mindestens eine Person mit echtem Beschaffungszugang (ex-Militaer, MOD/Behoerde, Prime) im Kernteam — nicht nur im Advisory Board
