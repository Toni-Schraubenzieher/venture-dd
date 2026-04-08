---
name: space-logistics
label: Space Logistics & Re-Entry (Transport, Orbital Services, In-Space Manufacturing)
description: Startups im Bereich Weltraum-Transport, Re-Entry-Vehicles, Orbital Assembly, In-Space Servicing oder Space Manufacturing
keywords: [space, orbital, satellite, reentry, re-entry, launch, ESA, CNES, NASA, heatshield, GNC, LEO, GEO, microgravity, rideshare, deorbit, capsule, payload, TPS, thermal protection, ITAR, EAR, dual-use, space logistics, in-orbit, OTV]
---

# Vertical: Space Logistics & Re-Entry

## Kontext
Space-Startups kombinieren Hardware-Risiken (lange Entwicklungszyklen, hohe BOM) mit regulatorischen Risiken (Export-Kontrolle, Dual-Use) und extremer Abhaengigkeit von Launch-Infrastruktur. Die haeufigsten Fehler: (1) Pipeline-Zahlen vermischen near-term-faehige Produkte mit Moonshot-Fahrzeugen die Series-B+-Funding erfordern, (2) Reuse-Annahmen im Financial Model sind physikalisch unbewiesen, (3) Non-Dilutive Funding (ESA/CNES/NASA Grants) wird im Model als gesichert behandelt obwohl nur beantragt. Gute Deals haben Flight Heritage (mindestens einen erfolgreichen Flug), ein klares Near-Term-Revenue-Vehicle, und >30% Non-Dilutive-Anteil an der Gesamtfinanzierung als Qualitaetssignal.

## Extraction Focus Areas (Session 3)
- **Fahrzeug-Roadmap:** Alle Fahrzeug-Generationen mit Status (Konzept / Entwicklung / Gebaut / Geflogen). Klare Trennung: Was generiert near-term Revenue vs. was erfordert weitere Funding-Runden?
- **Tech-Moat:** Was ist proprietaer? (GNC/Autopilot, Heatshield/TPS, Propulsion, Software). Was basiert auf oeffentlich gefoerderter Entwicklung? IP-Eigentumsrecht klaeren
- **Flight Heritage:** Was ist tatsaechlich geflogen? Unter welchen Bedingungen? Maiden Flight Success/Failure Details. Unabhaengige Berichterstattung (nicht nur Startup-eigene)
- **Reuse-Status:** Wie oft wurde ein Fahrzeug tatsaechlich wiederverwendet? Reuse-Target vs. physikalisch bewiesene Zyklen. Welche Komponenten muessen nach jedem Flug ersetzt werden?
- **Non-Dilutive Funding:** Alle Grants/Contracts einzeln: Quelle (ESA/CNES/NASA/EU/National), Betrag, Status (gewonnen/beantragt/geplant), Bedingungen, IP-Implikationen
- **Export-Kontrolle:** Dual-Use-Klassifizierung, ITAR/EAR-Relevanz (US-Komponenten?), nationale Export-Regulierung (BAFA/DGA), formale Strategie vorhanden?
- **Launch-Abhaengigkeit:** Welche Launch Provider? Rideshare vs. Dedicated? Kosten pro Launch? Vertragsstatus? Backup-Optionen?
- **Customer Segments:** Pharma/Biotech (Microgravity), Defense, Scientific, Commercial — welche Segmente sind near-term adressierbar?

## Cross-Referencing Checks (Session 4)
- [ ] **Build-Kosten: Hardware-only vs. All-in:** Financial Model zeigt oft nur Hardware-BOM. Tatsaechliche Mission Cost = Hardware + Assembly/Test + Launch + Ground Ops + Recovery + Refurbishment. Delta quantifizieren
- [ ] **Pipeline nach Fahrzeug-Generation aufschluesseln:** Welcher Anteil der kommunizierten Pipeline erfordert welches Fahrzeug? Near-term (aktuelles Vehicle) vs. Moonshot (Series-B+-Vehicle) trennen. LOIs fuer nicht-existierende Produkte separat ausweisen
- [ ] **Non-Dilutive: Gewonnen vs. Beantragt vs. Angenommen:** Jede Non-Dilutive-Quelle im Financial Model klassifizieren als COMMITTED (Vertrag unterschrieben), APPLIED (eingereicht), oder ASSUMPTION (nur geplant). Model-Sensitivity ohne ASSUMPTION-Quellen berechnen
- [ ] **Launch-Kosten: Model vs. Markt:** Angenommene Launch-Kosten im Model vs. aktuelle Rideshare-Preise (Transporter, Bandwagon, Exolaunch, D-Orbit). Trend: Preise sinken, aber Verfuegbarkeit ist Bottleneck
- [ ] **Reuse im Financial Model vs. Physik:** Bei wie vielen Reuses rechnet das Model? Wie viele sind physikalisch bewiesen? Model-Sensitivity bei 50% der angenommenen Reuses berechnen
- [ ] **Revenue-Timeline vs. Fahrzeug-Readiness:** Wann steht das Revenue-generierende Fahrzeug bereit? Passt die Revenue-Rampe im Model zum realistischen Entwicklungszeitplan?
- [ ] **Grants-Abhaengigkeit:** Welcher Anteil des Runway kommt aus Non-Dilutive? >50% = hohes Risiko bei Grant-Verzoegerungen

## Unit Economics Calculations (Session 4 Phase 2)
1. **Mission Cost (all-in):** Hardware Build (BOM + Assembly + Test) + Launch (Rideshare/Dedicated + Integration) + Ground Ops (Mission Control, Tracking) + Recovery (Schiff/Bergung, falls applicable) + Refurbishment (Post-Flight Inspektion, Komponenten-Tausch) = Total Mission Cost
2. **Revenue/Mission vs. Mission Cost:** Bei verschiedenen Reuse-Szenarien (1x, 3x, 5x, 10x). Ab welcher Reuse-Anzahl wird die Mission profitabel?
3. **Break-Even Reuse-Anzahl:** Mission Cost * N_reuses vs. Revenue * N_reuses + Hardware_Build (einmalig). Aufloesung nach N
4. **Near-Term vs. Moonshot Economics separat:** Nicht vermischen. Near-Term-Vehicle hat andere Kosten/Revenue als Moonshot
5. **Runway mit/ohne Non-Dilutive:** Seed-Funding allein → wie viele Monate? Mit committed Non-Dilutive → wie viele Monate? Mit allen angenommenen Non-Dilutive → wie viele Monate? Sensitivitaet zeigen
6. **Cost per kg to orbit/from orbit:** Startup-Claim vs. Wettbewerber vs. aktuelle Marktpreise. Trend-Analyse

## Research Blocks (Session 5, Bloecke 2-4)

### Block 2: Defense Budgets, Space Policy & Regulatory
Web-Recherche (Englisch):
- EU Space & Defense Budgets 2025-2030: EDF (European Defence Fund), Horizon Europe Space, IRISS, ESA InCubed+
- Nationale Foerderprogramme: CNES (Frankreich), DLR (Deutschland), ASI (Italien), UK Space Agency — aktuelle Calls und Budgets
- NASA Commercial LEO Destinations Programme Status (CLD)
- Export-Kontrolle: ITAR/EAR fuer Space-Komponenten, EU Dual-Use Regulation (2021/821), nationale Besonderheiten (BAFA, DGA)
- Space Sustainability Regulierung: ESA Zero Debris Charter, FCC 5-Year Deorbit Rule, EU Space Law Developments
- Verteidigungsanwendungen: Welche NATO/EU-Programme adressieren Space Logistics? Budget-Trends?

### Block 3: Markt-Validierung & Nachfrage
Web-Recherche:
- ISS Decommissioning Timeline (aktueller Stand, NASA/Roscosmos Agreements) und Auswirkungen auf Microgravity-Nachfrage
- Commercial LEO Destinations Status: Starlab (Voyager/Airbus), Vast Haven-2, Axiom Station — wer fliegt wann?
- Microgravity Demand: Welche Pharma/Biotech-Unternehmen investieren tatsaechlich? (Merck, Eli Lilly, etc.) Revenue aus In-Space Manufacturing — real oder nur F&E?
- Return-from-Orbit Demand: Wer braucht Downmass? Pharma (Kristallisation), Materials Science, Defense (Surveillance Payload Return)?
- Pricing Benchmarks: Was zahlen Kunden aktuell fuer Downmass ($/kg)? SpaceX Dragon, Varda, Outpost Comparables
- Sample Return Market: Pharma bereit fuer $50K-200K/kg? Oder nur $5K-20K/kg wie bei terrestrischen Expresslogistik-Vergleichen?

### Block 4: Technologie & Launch-Benchmarks
Web-Recherche:
- Starship Launch-Kosten: Aktueller Stand (nicht Musk-Versprechen). Wann realistisch fuer kommerzielle Rideshare verfuegbar?
- Rideshare Pricing Trends 2024-2026: SpaceX Transporter/Bandwagon, RocketLab, Exolaunch, D-Orbit
- Ceramic/Ablative Heatshield Technologie: Stand der Technik, Anbieter, Kosten, Reuse-Faehigkeit
- GNC (Guidance, Navigation, Control) fuer Re-Entry: Wer hat was demonstriert? Wie proprietaer ist das?
- Re-Entry Vehicle Build-Kosten: Vergleich Varda, Outpost, Space Forge — was kostet ein vergleichbares Fahrzeug?
- Payload Recovery Success Rates: Historische Daten fuer Capsule/Vehicle Recovery (SpaceX Dragon, Soyuz, etc.)

## Risk Framework
1. **Reuse Unbewiesen:** Das gesamte Business Model basiert auf Mehrfach-Nutzung, aber physikalisch wurde bisher 0 oder wenige Reuses demonstriert. Material-Degradation (Heatshield, Struktur) ist nicht linear vorhersagbar
2. **Launch-Abhaengigkeit:** Kein eigener Launch → abhaengig von Rideshare-Verfuegbarkeit und -Preisen. Verzoegerungen beim Launch Provider (Starship, Ariane 6) kaskadieren direkt auf Revenue-Timeline
3. **Pipeline-Irrefuehrung:** Gesamtpipeline mischt near-term (aktuelles Vehicle) mit Moonshot (Series-B+-Vehicle). Die "Pipeline" kann 80%+ nicht-adressierbar sein. Immer nach Fahrzeug-Generation aufschluesseln
4. **Export-Kontrolle (Dual-Use):** Re-Entry-Technologie ist inhaerent dual-use. Ohne formale Export-Control-Strategie drohen: Kundenverlust (Defense-Kunden ohne Clearance), Compliance-Verstoesse, Investoren-Abschreckung
5. **Non-Dilutive-Abhaengigkeit:** ESA/CNES Grants finanzieren oft 30-60% der Entwicklung. Grant-Verzoegerungen (3-12 Monate typisch) koennen Cash-Crunches ausloesen. Grants haben IP-Bedingungen die spaetere Monetarisierung einschraenken koennen
6. **Starship-Timing:** Viele Space-Startup-Business-Cases holen ihre Moonshot-Revenue aus dem "Starship-Zeitalter" (guenstige Launches, grosse Payloads). Wenn Starship spaeter kommt oder teurer bleibt: Moonshot-Economics kollabieren
7. **Fahrzeug-Generationswechsel:** Revenue-Modell erfordert Sprung von Demo/Small Vehicle auf Production Vehicle. Dieser Sprung ist in der Raumfahrt historisch mit 2-5x Zeitverzoegerung und 2-3x Kostenueberschreitung verbunden
8. **Regulatory Freeze-Risk:** Ein einzelner Fehlschlag (z.B. unkontrollierter Re-Entry, Debris-Vorfall) kann regulatorische Shutdowns fuer die gesamte Branche ausloesen

## Benchmarks
- **Typische Seed-Runde (Space, Europa):** EUR 5-10M
- **Pre-Money Seed (Europa):** EUR 15-40M, abhaengig von Flight Heritage
- **Non-Dilutive als Qualitaetssignal:** >30% der Gesamtfinanzierung aus Grants/Contracts = stark, <15% = schwach
- **Flight Heritage Premium:** Maiden Flight Success = Top 5% der Space Startups weltweit. Erhoeht Bewertung um ~30-50% vs. Pre-Flight
- **Revenue/kg Downmass (aktuell):** $50K-200K/kg (Premium, Pharma). $10K-50K/kg (Standard, Materials)
- **Mission Cost Benchmarks:** Kleine Capsule (20-50kg): $1-3M. Mittlere (100-200kg): $3-8M. Grosse (500kg+): $10M+
- **Reuse Break-Even:** Bei 3-5 Reuses typischerweise break-even auf Mission-Ebene (ohne Amortisation der Entwicklung)
- **Typische Entwicklungszeit Demo→Production Vehicle:** 3-5 Jahre (optimistisch), 5-8 Jahre (realistisch)
