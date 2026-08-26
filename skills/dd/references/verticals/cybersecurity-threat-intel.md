---
name: cybersecurity-threat-intel
label: Cybersecurity & Threat Intelligence (inkl. Security Data Platforms, SOC Tooling, Attack Surface Management)
description: Startups die Security-Daten, Threat Intelligence, Detection/Response-Tooling oder Security-Infrastruktur als Produkt/API/Plattform anbieten
keywords: [cybersecurity, threat intelligence, CTI, SOC, SIEM, SOAR, EDR, XDR, MSSP, DNS, BGP, WHOIS, OSINT, attack surface, ASM, dark web, malware, vulnerability, security data, infrastructure intelligence, passive DNS, IOC, threat feed, agentic security, MCP, DFIR, incident response]
---

# Vertical: Cybersecurity & Threat Intelligence

## Kontext
Der Cybersecurity-Markt ist extrem fragmentiert (3.000+ aktive Vendors), Buyer sind CISOs/SOC-Leads mit ausgepraegter Tool-Fatigue und Konsolidierungsdruck — Point Solutions werden zunehmend durch Plattform-Bundles (Microsoft, CrowdStrike, Palo Alto) verdraengt. Daten-/Intel-Anbieter leben von Provenienz, Freshness und Vertrauen: ein einziger oeffentlicher Attribution-Fehler kann die Reputation zerstoeren. Die haeufigsten Investoren-Fehler: (1) "proprietaere Daten" akzeptieren, die grossteils aus oeffentlichen Quellen aggregiert sind (RIPE RIS, RouteViews, CT-Logs, WHOIS), (2) Partnership-/Integrations-Logos als Traction werten statt zahlende Kunden, (3) das Feature-vs-Company-Problem unterschaetzen (Incumbents koennen die Faehigkeit als Feature nachbauen), (4) Enterprise-Security-Sales-Cycles (6-12+ Monate) in der ARR-Rampe ignorieren. Gute Deals haben verifizierbare zahlende Kunden, eine klare Antwort auf "warum koennen Incumbents das nicht einfach kopieren", und Datenquellen mit sauberer Lizenz-/Rechtslage.

## Extraction Focus Areas (Session 3)
- **Datenquellen-Provenienz:** Pro Quelltyp klassifizieren: public/free (RIPE, RouteViews, CT-Logs, WHOIS), lizenziert (kommerzielle Feeds — welche, zu welchen Terms, Re-Distribution erlaubt?), proprietaere Eigen-Collection (eigene Sensoren, Scanner, Honeypots). Der Moat liegt fast nie in public Daten.
- **Daten-Metriken-Zaehlweise:** Was genau wird gezaehlt — Nodes, Edges, Records, Events, "Data Points"? Ueber alle Materialien (Deck, Website, Docs) konsistent?
- **API-/Performance-Claims:** req/s, Latenz (p50 vs. p99, gemessen wo?), Uptime-SLA, Rate Limits, Benchmark-Methodik (load-tested vs. production)
- **Integrations-Status:** Pro Integration: signed vs. live vs. announced vs. "shipping". Marketplace-Listings (Splunkbase, Azure Marketplace, CrowdStrike Store) sind oeffentlich verifizierbar
- **Revenue-Mix:** OEM/Embedded vs. Channel/MSSP vs. Direct Enterprise vs. Self-Serve/PLG. Usage-based vs. Subscription. Wer kontrolliert bei OEM das Volumen?
- **Kundensegmente:** Enterprise SOC, MSSP, CTI-Team, Government/CERT, AI-/Agentic-Workflows — pro Segment: Anzahl, Status (paying/pilot/PoC/design partner)
- **Detection-/Scoring-Claims:** False-Positive-Raten, Erklaerbarkeit, unabhaengige Validierung (MITRE ATT&CK Evals, Testberichte)?
- **Compliance & Datenresidenz:** SOC2, ISO 27001, GDPR-Basis fuer Verarbeitung (WHOIS-Daten!), Datenstandort, Sanktions-Screening
- **Eigene Security-Posture:** Security-Anbieter sind Hochwert-Ziele. Bug-Bounty, Pentests, Incident-Historie?

## Cross-Referencing Checks (Session 4)
- [ ] **Daten-Zaehlweise konsistent:** "X Milliarden Datenpunkte" im Deck vs. Nodes/Edges auf Website vs. Docs. Nodes+Edges summieren ist Inflation — dokumentieren
- [ ] **Partnership vs. Revenue:** Jedes Logo klassifizieren: zahlender Kunde / OEM mit Billing live / signed ohne Revenue / Design Partner (unbezahlt) / MOU / "in Gespraechen". Nur die ersten zwei sind Traction
- [ ] **OEM- vs. Direct-Pricing-Kannibalisierung:** Unterbietet der OEM-Preis (pro Call/Seat) das Direct-Enterprise-Pricing? Kann der OEM-Partner zum Wettbewerber im eigenen Zielsegment werden?
- [ ] **Pricing vs. Markt-Benchmarks:** Listenpreise gegen vergleichbare Anbieter (Threat-Intel-Feeds, Enrichment-APIs) stellen. Zu billig = Commodity-Signal, zu teuer = Adoption-Risiko
- [ ] **CLV/CAC vs. Sales-Motion:** Blended CLV/CAC zerlegen: passt der blended Wert zur behaupteten Enterprise-Motion, oder dominiert Self-Serve-Low-End die Annahmen?
- [ ] **ARR-Projektion vs. Sales Cycle:** Enterprise-Security-Deals brauchen 6-12+ Monate. Traegt die projizierte Rampe dem Rechnung oder unterstellt sie PLG-Geschwindigkeit im Enterprise-Segment?
- [ ] **Benchmark-Claims vs. Methodik:** Performance-Zahlen (req/s, Latenz) — synthetischer Load-Test oder Production-Traffic? Methodik-Dokument angefordert?
- [ ] **Vergleichstabellen-Fairness:** Wird Produkt gegen DB-Technologie (z.B. Neo4j) statt gegen echte Wettbewerber verglichen? Aepfel-Birnen-Vergleiche dokumentieren

## Unit Economics Calculations (Session 4 Phase 2)
1. **OEM-Revenue-Durchrechnung:** Preis pro Call/Unit x realistisches Volumen des Partners = impliziter Jahres-Revenue. Gegen die im Deck genannten OEM-Erwartungen ($/Monat) stellen — wie viele Calls muessten die Endkunden absetzen?
2. **ARR-Rampe rueckwaerts:** Ziel-ARR / durchschnittlicher ACV = benoetigte Kundenzahl. Benoetigte Kunden / (12 / Sales-Cycle-Monate) = benoetigte parallele Pipeline. Realistisch bei aktueller GTM-Mannschaft?
3. **Data-COGS:** Lizenzkosten fuer kommerzielle Feeds + Collection-Infrastruktur (Server, Bandbreite, Storage) + Datenverarbeitungs-Compute / Revenue. Echte Gross Margin berechnen, nicht Software-Standard-85% annehmen
4. **Segment-CLV-Zerlegung:** Blended CLV nach Segmenten (Enterprise / Integration / Self-Serve) aufloesen. Welches Segment traegt das Modell wirklich? Churn-Annahme pro Segment plausibel?
5. **Konzentrations-Risiko:** Groesster Kunde/Partner als % des Revenue (aktuell und in der Projektion). >30% = strukturelles Risiko

## Research Blocks (Session 5, Bloecke 2-4)

### Block 2: Markt, Regulierung & Konsolidierung
Web-Recherche (Englisch):
- Threat-Intelligence-Marktgroesse und CAGR (aktuelle Analysen 2024-2026, mehrere Quellen — Gartner/Fortune/MarketsandMarkets divergieren stark)
- M&A-Landschaft: Recorded Future/Mastercard ($2.65B), Mandiant/Google ($5.4B), RiskIQ/Microsoft — was zahlen Acquirer, wofuer (Daten, Kunden, Team)?
- EU-Regulierung als Tailwind: NIS2-Umsetzungsstand, DORA (Finanzsektor), Cyber Resilience Act — schaffen sie Budget fuer diese Produktkategorie?
- CISO-Budget-Trends: Konsolidierung vs. Best-of-Breed, Anteil Threat Intel am Security-Budget
- Venture-Funding-Umfeld Cybersecurity EU vs. US: Runden, Bewertungen, aktive Spezialfonds

### Block 3: Kunden & Nachfrage-Validierung
Web-Recherche:
- Wie kaufen SOCs/MSSPs Threat Intel ein: Feeds vs. Plattform vs. Enrichment-API? Typische Vertragsgroessen und Beschaffungswege
- Churn-Treiber bei Threat-Intel-Abos: warum kuendigen Kunden (Datenqualitaet, Ueberlappung mit Gratis-Quellen, Budget)?
- Review-Portale: Gartner Peer Insights, G2 fuer die Kategorie und die genannten Wettbewerber — was loben/kritisieren echte Nutzer?
- Referenz-Verifikation: genannte Partner/Kunden extern belegen (Pressemitteilungen, Marketplace-Listings, Case Studies, gemeinsame Webinare)
- Agentic-SOC-Adoption: Wie real ist die Nachfrage nach MCP-/AI-Agent-Anbindung heute? Wer bezahlt dafuer bereits?

### Block 4: Technologie, Datenquellen & Replizierbarkeit
Web-Recherche:
- Graph-DB-Landschaft: Neo4j, TigerGraph, Memgraph, ArangoDB, Kuzu, Amazon Neptune — was leisten sie bei Multi-Hop-Traversal heute wirklich (Benchmarks)? Ist "custom Graph-Engine" notwendig oder Marketing?
- Passive-DNS- und Infrastruktur-Daten-Anbieter mit Preisen: DomainTools/Farsight DNSDB, SecurityTrails, Validin, Silent Push, Censys, Shodan, Team Cymru, zetalytics
- Oeffentlich verfuegbare Quellen inventarisieren: RIPE RIS, RouteViews, CAIDA, CT-Logs, OpenINTEL, Common Crawl — wie viel des Datenbestands ist damit replizierbar?
- MCP-/AI-Integration der Wettbewerber: wer hat bereits MCP-Server, LLM-Integrationen, Agent-APIs geshippt? (Zeitvorsprung real?)
- Replikations-Schaetzung: Team + Zeit + Infra-Kosten, um einen vergleichbaren Datenbestand aufzubauen — was davon ist in 12-18 Monaten mit $5M nachbaubar?

## Risk Framework
1. **Daten-Commoditisierung:** Grosser Teil der Datenbasis stammt aus oeffentlichen/kaeuflichen Quellen. Der Moat muss in Collection-Tiefe, Historie, Verknuepfung oder Query-Layer liegen — pruefen, nicht annehmen
2. **Incumbent-Feature-Risiko:** Censys, Shodan, DomainTools, Recorded Future koennen Graph-Traversal und MCP-Anbindung als Feature nachschieben. Zeitfenster abschaetzen
3. **Single-OEM-/Channel-Konzentration:** Ein dominanter OEM-Partner = Klumpenrisiko bei Revenue UND Distribution; Partner kann Konditionen diktieren oder selbst bauen/kaufen
4. **Datenquellen-Lizenzrisiko:** Scraping/ToS-Verstoesse, WHOIS-GDPR-Problematik, Re-Distribution-Verbote in Feed-Lizenzen — kann Kern-Datenquellen ueber Nacht wegnehmen
5. **Trust-/Attribution-Risiko:** Ein oeffentlicher False-Positive mit Schadenfolge (falsche Sanktions-Zuordnung, falsches Takedown) zerstoert die Glaubwuerdigkeit des Scorings
6. **Plattform-Konsolidierung:** CISO-Budgets wandern zu Bundles (Microsoft E5, CrowdStrike, Palo Alto). Point-Solution-Budgets werden zuerst gestrichen
7. **Performance-Claim-Fragilitaet:** Sub-ms/Hochlast-Claims aus synthetischen Benchmarks halten Production-Last oft nicht stand; SLA-Bruch bei OEM-Partnern eskaliert sofort
8. **Dual-Use/Sanktions-Compliance:** Infrastruktur-Intelligence ueber sanktionierte Entitaeten, Export-Kontrolle, Government-Kunden — Compliance-Aufwand und Reputationsrisiko
9. **Key-Person Datenpipeline:** Collection- und Graph-Engine-Know-how konzentriert sich oft auf 1-2 Personen. Bus-Factor pruefen
10. 🔴 **Zyklizitaet des Sicherheitsbudgets:** Geht es einem Kunden schlecht, wird **zuerst** am Software- und Sicherheitsbudget gespart — kontraintuitiv und trotzdem die Regel. Net Retention und Reduktionsrechte in den Vertraegen deshalb getrennt nach Segment erheben, nicht blended

## Benchmarks
- **Typische Seed-Runde (Cybersecurity EU):** EUR 3-8M; US-Vergleich $5-15M
- **Pre-Money Seed (EU Cyber):** EUR 10-30M, stark traction-abhaengig; Daten-/API-Plays am unteren Ende ohne nachgewiesene ARR
- **Gesunde Gross Margins (Security Data/API):** 70-85% bei Eigen-Collection; jede kommerzielle Feed-Lizenz drueckt die Marge
- **Enterprise Security Sales Cycle:** 6-12+ Monate (Enterprise/Government), 3-6 Monate (MSSP/OEM-Nachzug), Tage-Wochen (Self-Serve). 🔴 **Bei vorhandener Bestandsloesung verlaengert sich der Eintritt auf den naechsten Vertragsauslauf beim Wettbewerber** — dann 12-18+ Monate, und der Zyklus wird nicht nur laenger, sondern exponentiell. Zu erheben: was ist heute im Einsatz, und wann laeuft es aus?
- **NRR (gut):** >110%; Logo-Churn Self-Serve deutlich hoeher als Enterprise
- **ARR fuer Series A (Security SaaS):** $1-2M+ mit 2-3x YoY-Wachstum
- **OEM-/Embedded-Anteil (gesund):** <40% des Revenue von einem Partner; darueber Klumpenrisiko
- 🔴 **LOI-Konversion Enterprise:** **10-20 %** materialisieren sich in kommerzielle Kontrakte; typisch 18-24 Monate bis zum Fuss in der Tuer. Ein LOI ohne Umwandlungsklausel ist keine Pipeline
- 🔴 **Zahlungsbereitschaft nach Unternehmensgroesse:** sechsstellige ACVs tragen erst bei Grosskonzernen (DAX/MDAX-Klasse). Der gehobene Mittelstand kauft off-the-shelf im Bereich **20-30K/Jahr** und zahlt keine Enterprise-Preise, auch bei erheblichem eigenem Umsatz. **Haben wollen es alle, zahlen will es die Mittelschicht nicht**
- 🔴 **Commercial-Lead-Hire:** in Cyber sind die brauchbaren Profile Ex-CISOs oder Leute von den Kategoriefuehrern; Gesamtpakete **Richtung 500K**. Das Problem ist nicht das Finden, sondern das Bezahlen — **pruefen, ob die Personalplanung den Hire traegt, den der Vertriebsplan voraussetzt**
- **Threat-Intel-Preis-Referenzen:** Enrichment-APIs $10-50K/Jahr (Team-Lizenzen), Enterprise-Plattformen $100-500K/Jahr (Recorded Future obere Spanne), Feeds einzeln $5-30K/Jahr
