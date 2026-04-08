---
name: hardware-robotics
label: Hardware & Robotics (inkl. Construction Automation, Industrial Automation)
description: Startups die physische Produkte, Roboter oder autonome Systeme entwickeln und verkaufen, vermieten oder als Service anbieten
keywords: [robotics, hardware, autonomous, manufacturing, BOM, robot, vehicle, machine, construction, automation, industrial, assembly, sensor, actuator, mechatronics, cobot, drone, AGV, AMR]
---

# Vertical: Hardware & Robotics

## Kontext
Hardware-Startups haben fundamental andere Risikoprofile als Software: Produktentwicklung dauert Jahre statt Monate, Skalierung erfordert Kapital fuer BOM und Produktionsinfrastruktur, und ein fehlgeschlagenes Produkt kann nicht einfach "gepatcht" werden. Die haeufigsten Fehler: (1) BOM-Kosten werden systematisch unterschaetzt, (2) der Sprung vom Prototyp zur Serienproduktion wird trivialisiert, (3) Gross Margins werden nur auf Hardware-Ebene berechnet statt all-in (Deployment, Support, Warranty). Gute Deals haben TRL 6+ mit echten Field Deployments und mindestens einen zahlenden Kunden.

## Extraction Focus Areas (Session 3)
- **TRL-Assessment:** Aktueller Technology Readiness Level pro Produkt. Wie viele Prototypen gebaut? Wo eingesetzt? Unter welchen Bedingungen (kontrolliert vs. real-world)?
- **BOM-Breakdown:** Hauptkomponenten mit Einzelpreisen, Zulieferer, Lead Times. Wo sind Single-Source-Abhaengigkeiten?
- **Manufacturing Readiness:** Eigene Fertigung vs. Contract Manufacturing? Produktionspartner identifiziert? Kapazitaetsplanung?
- **Supply Chain:** Long-Lead-Items identifizieren (Roboterarme, Spezial-Sensoren, Batterien, Custom PCBs). Lieferzeiten? Alternative Quellen?
- **Zertifizierungen:** CE, UL, OSHA, SIL-Level, ISO 13849 — was ist erforderlich, was ist erreicht, was fehlt? Timeline bis Zertifizierung?
- **Performance-Metriken:** Cycle Time, Throughput, Precision/Toleranzen, Intervention Rate, Damage Rate, Uptime/MTBF, autonome Betriebsdauer
- **Deployment-Prozess:** Wie wird das Produkt beim Kunden installiert? Wie lange dauert es? Wer macht es? Was kostet es?
- **Service/Support-Modell:** Remote Monitoring? On-site Support? Ersatzteil-Logistik? SLA-Bedingungen?
- **Generationswechsel:** Falls Nachfolge-Produkt geplant: Was aendert sich? Wie abwaertskompatibel? Kannibalisiert es das bestehende Produkt?

## Cross-Referencing Checks (Session 4)
- [ ] **BOM Model vs. Realitaet:** BOM-Kosten im Financial Model vs. tatsaechliche Komponentenpreise (falls dokumentiert). Delta-Analyse: Welche Positionen fehlen? (Gehaeuse, Kabel, Verpackung, Shipping oft vergessen)
- [ ] **Prototype-Kosten vs. Production-Annahmen:** Wie viel kostete der letzte Prototyp tatsaechlich? Wie realistisch ist die angenommene Kostenreduktion bei Serienproduktion?
- [ ] **Production Target vs. Headcount:** Kann das Team X Units/Jahr mit der geplanten Mannschaft tatsaechlich bauen, deployen und supporten?
- [ ] **Performance-Trend:** Verbessern sich die Kernmetriken (Cycle Time, Throughput, Intervention Rate) ueber die Deployments hinweg oder stagnieren sie?
- [ ] **Unit Economics all-in:** Marge NICHT nur auf Hardware-Ebene (Revenue - BOM), sondern all-in: BOM + Assembly + Testing + Shipping + Deployment + Training + Support + Warranty + Overhead. Oft schrumpft die Marge von 50% auf 15-25%
- [ ] **Customer ROI Plausibilitaet:** Startup-eigene ROI-Berechnung nachrechnen. Welche Annahmen stecken drin? Werden reale Kundenkosten (Downtime, Umstellung, Training) beruecksichtigt?
- [ ] **Revenue-Modell-Konsistenz:** Hardware-Verkauf vs. Rental vs. RaaS vs. Subscription — wird im Pitch etwas anderes kommuniziert als im Financial Model modelliert?

## Unit Economics Calculations (Session 4 Phase 2)
1. **All-in Unit Cost:** BOM + Assembly/Test + Shipping/Logistics + Deployment/Installation + Customer Training + Year-1 Support + Warranty Reserve = Tatsaechliche Kosten pro Unit
2. **All-in Gross Margin:** (Revenue pro Unit - All-in Unit Cost) / Revenue pro Unit. Vergleich mit Startup-Claim
3. **Break-Even Units:** Fixed Costs (Payroll + Rent + Overhead) / Gross Profit pro Unit = Minimum Units fuer Profitabilitaet
4. **Customer ROI (unabhaengig nachgerechnet):** Einsparung (Labor + Fehlerkosten + Downtime-Reduktion) - Kosten (Kauf/Miete + Betrieb + Training) = Jaehrlicher Netto-Benefit. Payback Period berechnen
5. **Recurring Revenue Ratio:** Recurring (Software, Service, Consumables) / Total Revenue pro Unit. Ziel: >30% fuer nachhaltige Margen
6. **Production Ramp Feasibility:** (Target Units * Avg Build Time) / (Available Engineers * Working Hours) = Kapazitaetsauslastung. >80% = unrealistisch bei Startup-Chaos

## Research Blocks (Session 5, Bloecke 2-4)

### Block 2: Branchenspezifischer Markt & Regulierung
Web-Recherche (Englisch):
- TAM/SAM des spezifischen Anwendungsbereichs (Construction Automation, Warehouse Robotics, etc.) — aktuelle Marktanalysen (2024-2026)
- Foerderprogramme und Steuererleichterungen (z.B. ITC, Section 48, CHIPS Act, EU Green Deal)
- Labor Shortage im Zielmarkt: Wie gross ist der Fachkraeftemangel wirklich? Lohn-Trends?
- Regulatorische Huerden: Welche Zertifizierungen/Zulassungen sind branchenspezifisch erforderlich?
- Pilotprojekt-Erfahrungen: Gibt es oeffentliche Case Studies von Wettbewerbern oder aehnlichen Deployments?

### Block 3: Kunden & Nachfrage-Validierung
Web-Recherche:
- Kundenstruktur im Zielmarkt: Wer sind die Top-10 Abnehmer? Wie konzentriert ist der Markt?
- Typische Beschaffungs-Cycles: Wie lange dauert es von Erstgespraech bis PO? (6-18 Monate bei Enterprise Hardware typisch)
- Preis-Benchmarks: Was zahlen Kunden fuer vergleichbare Loesungen? (manuell, semi-automatisiert, Wettbewerber)
- Referenzkunden: Gibt es oeffentliche Testimonials oder Case Studies von den genannten Pipeline-Kunden?
- Adoption Barriers: Was hielt Kunden bisher von Automation ab? (Kosten, Risiko, Change Management, Union-Widerstand)

### Block 4: Produktions-Benchmarks & Technologie
Web-Recherche:
- BOM-Benchmarks fuer vergleichbare Systeme (Roboterarme, autonome Fahrzeuge, Sensor-Suites): Was kosten die Komponenten bei Stueckzahl 10/50/100?
- Fertigungs-Benchmarks: Wie lange brauchen vergleichbare Hardware-Startups fuer den Sprung Prototyp → Serie? (Typisch: 18-36 Monate)
- Batterie/Energie-Benchmarks: Kosten pro kWh, Ladezyklen, Degradation
- Software-Stack: Ist die Autonomie-Software State-of-the-Art oder proprietaer? Vergleich mit Open-Source (ROS2, Nav2)
- IP-Landschaft: Patente der Wettbewerber in diesem Bereich. Freiheitsanalyse-Risiko?

## Risk Framework
1. **Product-Market Gap:** Produkt existiert nur als Prototyp/Konzept, aber Financial Model modelliert Serienprodukt-Revenue. Immer fragen: "Was genau muss noch gebaut werden, und wie lange dauert das realistisch?"
2. **BOM-Eskalation:** Hardware-BOM steigt fast immer zwischen Prototyp und Serie (Compliance-Anforderungen, Qualitaetssicherung, Verpackung/Shipping). Typische Ueberraschungen: +20-40% gegenueber Prototyp-BOM
3. **Hardware-Skalierung:** Der Sprung von 3 → 30 Units ist organisatorisch und finanziell eine andere Welt. Erfordert: Supply Chain Management, QA-Prozesse, Lager, Logistik. Oft unterschaetzt
4. **Supply Chain Single Points of Failure:** Ein kritischer Zulieferer mit 6+ Monaten Lead Time kann die gesamte Produktion blockieren
5. **Zertifizierungs-Timeline:** CE/UL/SIL-Zertifizierung dauert 6-18 Monate und kann Redesign erfordern. Oft nicht im Zeitplan
6. **Field Reliability:** Kontrollierte Demo ≠ Real-World-Performance. MTBF (Mean Time Between Failures) aus Demos extrapolieren ist riskant
7. **Key Engineer Dependency:** Bei 5-15 FTEs ist der Ausfall eines Lead Engineers existenzbedrohend. Wissenstransfer? Dokumentation?
8. **Rental/RaaS Cash-Drag:** Falls Geschaeftsmodell Rental/RaaS: Hohe Upfront-Investition (BOM), Revenue-Erkennung ueber Monate/Jahre. Cash-Flow-Negative auch bei "profitablen" Unit Economics

## Benchmarks
- **Typische Seed-Runde (Hardware/Robotics):** $5-15M bei TRL 6-7 mit Field Deployments
- **Pre-Money Seed:** $15-40M (US), EUR 10-25M (EU)
- **Gesunde Gross Margins (all-in):** 30-50% bei Serienproduktion, 15-25% in fruehen Batches
- **BOM-Reduktion Gen1→Gen2:** 25-40% typisch bei 5-10x Stueckzahl
- **Typische Zeit Prototyp→Serie:** 18-36 Monate (mit Zertifizierung)
- **Customer Payback Period (gut):** <24 Monate
- **Intervention Rate (gut):** <5% der Zyklen erfordern menschlichen Eingriff
- **Field Deployment Success Rate (gut):** >90% der Deployments abgeschlossen wie geplant
