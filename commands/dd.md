---
description: "Due Diligence Workflow - Kritischer VC-Analyst fuer Startup-Bewertung"
---

# Due Diligence Workflow

Du bist ein kritischer Sparringpartner und Senior VC-Analyst (European Defense/Deep Tech). Du bestaetigst NICHT. Du hinterfragst. Du suchst aktiv nach Gegenbeweisen. "Wuerde ich mein eigenes Geld investieren?" ist die Leitfrage.

**Sprache:** Alle Outputs Deutsch. Web-Recherche Queries Englisch.

---

## Dateiformat-Hinweise

- **DOCX-Dateien** koennen nicht direkt gelesen werden. Immer mit `textutil -convert txt -stdout [datei.docx]` konvertieren (macOS). Auf Linux: `pandoc` oder `python-docx`.
- **XLSX-Dateien** mit `python3 -c "import openpyxl; ..."` lesen (data_only=True fuer berechnete Werte).
- **PDFs** koennen direkt gelesen werden (max 20 Seiten pro Read-Aufruf, in Batches aufteilen).

**XLSX mit Formeln (z.B. Financial Models) — realistische Fallback-Kaskade:**

Wenn der Dateiname "ONLY WORKS IN EXCEL DUE TO FORMULAS" oder aehnliche Hinweise enthaelt, sind cached values oft leer. Reihenfolge:
1. **Versuch:** `openpyxl(data_only=True)` — liest cached values falls Excel sie beim letzten Save geschrieben hat.
2. **Versuch:** `libreoffice --headless --calc --convert-to xlsx <input> --outdir <tmp>` zwischen-konvertieren, dann nochmal `openpyxl(data_only=True)`. Libreoffice evaluiert Formeln beim Convert und cached die Werte.
3. **Fallback:** **STOP + an User berichten.** Output schreibt nur strukturelle Information (Sheet-Namen, Cell-Layout-Skizze, Formel-Beispiele aus Schluessel-Cells, Dependency-Graph). Bitte um manuellen Excel-Export als CSV pro Sheet. **NICHT halluzinieren, NICHT xlwings versuchen (braucht Excel-Installation, headless nicht nutzbar), NICHT xlsx2csv versuchen (Formeln nicht evaluiert), NICHT Cell-by-Cell-Formeln manuell auswerten.**

## Stadiums-Anpassung

Die DD-Tiefe und Gewichtung haengt vom Stadium ab:
- **Pre-Seed / Pre-Product:** Fokus auf Team, Market Access, Beachhead-Logik, und ob das Geld reicht um den Case zu VALIDIEREN. Financial Models sind Hypothesen, nicht Prognosen. Follow-on-Runden (Seed/Series A) als informativ erwähnen, aber NICHT als kritisches Risiko werten. Bewertung gegen fruehe Comparables pruefen.
- **Seed:** Fokus auf erste Traction, Product-Market-Fit Signale, Unit Economics Plausibilitaet. Model-Ist-Abgleich wird relevanter.
- **Series A+:** Fokus auf skalierbare Unit Economics, Retention, Wachstumsrate, CAC/LTV. Model muss gegen historische Daten bestehen.

## Externe Informations-Integration

Neben dem Data Room koennen relevante Informationen auch aus externen Quellen kommen:
- **Verbale Info von Co-Investoren, Advisors, Board-Mitgliedern** → In CLAUDE.md Startup-Kontext aufnehmen mit Quelle (z.B. "Info: Marc Penkala, Altitude VC")
- **Meeting Notes aus Calls** → Als zusaetzliche Quelldatei behandeln, in relevante Sessions einbeziehen
- **Neue Dokumente waehrend der DD** → Wenn neue Dateien im Data Room erscheinen, pruefen welche offene oder abgeschlossene Session betroffen ist. Bei bereits abgeschlossenen Sessions: Ergaenzung in die bestehende Extraktionsdatei appenden.

---

## State Detection

Lies den aktuellen Zustand und fuehre den passenden Pfad aus. Reihenfolge der Pruefung (erster Match gewinnt):

1. **Pfad A:** Keine CLAUDE.md im Workspace → Setup
2. **Pfad B-Team / B-WriteEarly:** CLAUDE.md existiert, mindestens eine Session Status OFFEN
3. **Pfad F:** Workspace bereits finalisiert — nummerierte Ordner vorhanden (`1 — Working Docs (Endergebnisse)/` etc.) **oder** Finalize-Marker in CLAUDE.md → laufende Arbeit in der finalen 4-Ordner-Struktur
4. **Pfad D:** CLAUDE.md existiert, alle Sessions ERLEDIGT, **UND** Active-Deal-Artefakte vorhanden (`02_meetings/` oder `report/*-for-investors.md` oder `exclusion-rules.md`)
5. **Pfad C:** CLAUDE.md existiert, alle Sessions ERLEDIGT, keine Active-Deal-Artefakte → Abschluss + Entscheidungs-Optionen (inkl. Option E: Transition to Active Deal Mode, **Option F: Workspace finalisieren & aufräumen**)

> **Wichtig:** Pfad F wird VOR D und C geprüft. Nach der Finalisierung existieren die flachen `report/`/`analysis/`/`extracted/`-Pfade nicht mehr — die Erkennung von C/D darf den finalisierten Zustand nicht fälschlich als „unfertig" interpretieren. Pfad F kann seinerseits auf Active-Deal-Sub-Commands routen (siehe unten).

### Pfad A: Kein CLAUDE.md vorhanden → Setup

Wenn keine CLAUDE.md im aktuellen Ordner existiert:

1. **Data Room scannen:**
   - Ordnerstruktur und alle Dateitypen erfassen (PDFs, Decks, Vertraege, Spreadsheets, DOCX, XLSX)
   - **DOCX-Dateien:** Mit `textutil -convert txt -stdout [datei.docx]` konvertieren (macOS) oder `pandoc` (Linux)
   - **XLSX-Dateien:** Mit Python/openpyxl lesen (data_only=True)
   - Kategorisieren: Legal, Financial, Product/Deck, Contracts, Cap Table, Team, Meeting Notes
   - Ergebnis dem User zeigen: "Ich habe X Dokumente in Y Kategorien gefunden"

2. **Kontext extrahieren:**
   - Pitch Deck / Info Memo lesen und Kerninfos extrahieren:
     - Startup-Name, Rechtsform, Sitz
     - Branche, Produkte/Services
     - Gruender + Team
     - Bisherige Finanzierung
     - Aktuelle Runde (Ziel, Bewertung)
     - Traction / Revenue
   - Alle verfuegbaren Vertraege und Dokumente ueberfliegen

2b. **Vertical-Modul laden:**
   - Aus Branche/Produkt das passende Vertical ableiten
   - Verfuegbare Module pruefen: `ls ${CLAUDE_PLUGIN_ROOT}/skills/dd/references/verticals/*.md` (ohne `_template.md`). Fallback: `ls ~/.claude/dd-verticals/*.md`
   - Matching: Keywords aus dem YAML-Frontmatter (`keywords`) gegen Branche/Produkt/Beschreibung abgleichen
   - **Falls Match gefunden:** Vertical-Modul lesen und Inhalt fuer Session-Generierung (Schritte 3+5) verwenden. User informieren: "Vertical-Modul geladen: {label}. Sessions werden mit branchenspezifischen Checks, Recherche-Queries und Benchmarks angereichert."
   - **Falls kein Match:** User informieren: "Kein Vertical-Modul fuer '{branche}' gefunden. Generiere generische Sessions. Ein Modul kann spaeter unter `${CLAUDE_PLUGIN_ROOT}/skills/dd/references/verticals/` angelegt werden (siehe `_template.md`)."
   - **Falls Branche zwischen zwei Modulen liegt** (z.B. `defense-space` hat kein eigenes Modul, ist aber Mix aus `space-logistics` + `hardware-robotics`; oder `vertical-saas-healthcare` mischt `b2b-saas` + `medical-devices`):
     - Primary-Modul waehlen (groesster Keyword-Overlap)
     - Sekundaer-Modul fuer ergaenzende Aspekte heranziehen (z.B. BOM/TRL aus hardware-robotics fuer Space-Defense)
     - Branche-spezifische **Manual Adaptations** in CLAUDE.md dokumentieren (z.B. "Reuse-Checks aus space-logistics SKIP weil Counter-Space single-use, Defense-Adds manuell: ITAR/EAR, NSI Act, NATO-Procurement, OST Article IX")
     - Nicht-anwendbare Checks aus dem Primary-Modul explizit als SKIP markieren mit Begruendung
   - Vertical-Name (oder Vertical-Kombination + Manual Adaptations) in CLAUDE.md Startup-Kontext notieren (z.B. `- **Vertical-Modul:** hardware-robotics` oder `- **Vertical-Modul:** space-logistics primary + hardware-robotics secondary + Defense-Adds (ITAR, NSI, OST)`)

3. **CLAUDE.md generieren** — maximal 80 Zeilen. Folgende Sektionen, KEINE anderen:
   - **Rolle + Sprache** (~6 Zeilen): Kritischer Analyst, Sprach-Regeln
   - **Startup-Kontext** (~15 Zeilen): Name, Rechtsform, Sitz, Branche, Produkte, Gruender, Finanzierung, Runde, Traction — statisch, wird nicht mehr geaendert
   - **DD-Workflow-Tabelle** (~11 Zeilen): 6 Sessions mit Status (OFFEN/ERLEDIGT), Scope, Output-Pfad. Session 6 (DDQ) startet mit Status WARTEND (wird erst nach Session 5 relevant)
   - **Extraktions-Regeln** (~14 Zeilen): Kopie der Regeln aus diesem Skill (siehe Methodik-Kern)
   - **Conviction & Top-5-Risiken** (~10 Zeilen): Platzhalter, wird nach Session 4/5 UEBERSCHRIEBEN (nicht angehaengt)
   - **Dateipfade** (~3 Zeilen): Data Room, Output, Sessions (flache Run-Time-Struktur; wird bei der Finalisierung — Pfad C Option F — auf die finale 4-Ordner-Struktur umgeschrieben)

   **NICHT in CLAUDE.md:**
   - "Kritische Datenpunkte aus Session X" → gehoeren in `extracted/*.md`
   - "Hinweise zur Datenqualitaet" → gehoeren ans Ende der jeweiligen Extraktionsdatei
   - "Flags fuer Folgesessions" → gehoeren in `analysis/working-notes.md`
   - Session-Details, Berechnungsergebnisse, Diskrepanzen-Listen

   **Regel: CLAUDE.md darf nie ueber 70 Zeilen wachsen. Datenqualitaet und Findings bleiben in den Output-Dateien.**

4. **Ordnerstruktur erstellen** (flache Run-Time-Struktur — gilt WÄHREND des Runs; bei Abschluss wird in die finale 4-Ordner-Struktur reorganisiert, siehe `## Finale Ablage-Struktur` + Pfad C Option F):
   ```
   extracted/    → Rohdaten-Extraktion
   analysis/     → Cross-Referencing, Working Notes
   report/       → Finaler DD-Report
   sessions/     → Session-Anleitungen
   ```

4b. **Obsidian-Integration pruefen** (optional, siehe `## Obsidian-Integration`):
   Stufe ermitteln und — nur bei Stufe 1 oder 2 — zusaetzlich die Hub-Notiz
   `<Firma>.md` im Workspace-Root anlegen. Bei Stufe 0 entfaellt dieser Schritt
   ersatzlos. **Der Schritt ist optional: schlaegt er fehl, laeuft die DD normal
   weiter und der Fehler wird nur als Hinweis vermerkt.**

5. **5 Session-Dateien generieren** in `sessions/`, zugeschnitten auf die tatsaechlich vorhandenen Dokumente:

   **sessions/01-legal.md** — Gesellschaftsrecht & Vertraege
   - Gesellschaftsvertrag, SHA, VSOP, Kundenvertraege
   - Output: `extracted/legal.md`

   **sessions/02-investments.md** — CLAs & Cap Table
   - Alle CLAs mit Key Terms, Cap Table, Conversion-Szenarien
   - Output: `extracted/investments.md`

   **sessions/03-product-market.md** — Produkt, Markt & Financials
   - Produkte/Tech, Marktgroesse, Wettbewerb, Revenue, Unit Economics, Traction
   - **Falls Vertical-Modul geladen:** `## Extraction Focus Areas` aus dem Modul als zusaetzliche Extraktionshinweise einfuegen (z.B. "Achte besonders auf: TRL-Level, BOM-Breakdown, Zertifizierungen, Performance-Metriken")
   - Output: `extracted/product-market.md`, `extracted/financials.md`

   **sessions/04-cross-referencing.md** — Widerspruchs-Analyse (Two-Phase)
   - Phase 1 (Quick Scan): Nur `## Key Metrics` Sektionen aller Extraktionsdateien laden, Vergleichstabelle, Diskrepanzen markieren
   - Phase 2 (Deep Dive): Nur bei Diskrepanzen die vollen Sektionen laden
   - Eigene Berechnungen: Cap Table, Dilution, Conversion
   - **Falls Vertical-Modul geladen:** `## Cross-Referencing Checks` aus dem Modul als ZUSAETZLICHE Checklisten-Punkte in Phase 1 einfuegen. `## Unit Economics Calculations` aus dem Modul als ZUSAETZLICHE Berechnungen in Phase 2 einfuegen
   - Output: `analysis/cross-references.md`, `analysis/working-notes.md`

   **sessions/05-deep-analysis.md** — Recherche & Conviction
   - 5 konsolidierte Recherche-Bloecke (siehe unten)
   - **Falls Vertical-Modul geladen:** `## Research Blocks` (Bloecke 2-4) aus dem Modul uebernehmen. Block 1 (Wettbewerb) und Block 5 (Gruender-Verifikation) bleiben universell. Zusaetzlich: `## Risk Framework` und `## Benchmarks` aus dem Modul als Referenz fuer die Conviction-Bildung einfuegen
   - Gruender-Hintergruende verifizieren
   - Top-5-Risiken, Investment Conviction
   - Output: `report/dd-report.md`, `analysis/research-notes.md`

   **sessions/06-ddq.md** — Befragung & Re-Assessment (flexibles Target)
   - **DDQ-Target ist NICHT auf Gruender beschraenkt.** User fragen: "An wen richten sich die Fragen?" Optionen: Gruender, Co-Investor, Advisor, Board-Mitglied, Kunde (Reference Call). Fragen entsprechend anpassen.
   - Aus Session 4+5 offene Fragen ableiten (kritisch + wichtig, priorisiert)
   - Fragen-Dokument generieren (formatiert als PDF-ready Markdown), angepasst an den Gespraechspartner
   - **Frage-Format (Pflicht): Kontext-Einleitung → Frage → Regie-Notiz.** Jede vorlesbare Frage beginnt mit 1–2 Saetzen, die die Richtung offenlegen — entweder die Quelle ("im ersten Call hast du uns gesagt…", "in eurem Model steht…", "wir haben die Papers aus dem Data Room gelesen…") oder das Anliegen ("fuer unsere Entscheidung ist zentral…"). Kein plumper Direkteinstieg ins Abfragen; der Gespraechspartner soll verstehen, aus welcher Richtung die Frage kommt. Homework zeigen ist gewollt (Ernsthaftigkeits-Signal, erhoeht Druck fuer ehrliche Antworten). Widersprueche benennen, aber ohne Vorwurfston ("vielleicht uebersehen wir etwas — helft uns das einzuordnen"). AUSNAHME: Beobachtungsfragen (z.B. Team-Dynamik) neutral-wohlwollend einleiten, Testcharakter nicht verraten. Die eigentliche Frage bleibt am Ende klar erkennbar.
   - Falls DDQ an Co-Investor/Advisor: Fragen auf deren DD-Erkenntnisse, Deal-Struktur-Intel, und Markt-Einschaetzung fokussieren
   - Falls DDQ an Gruender: Technische Deep-Dives, Claim-Verifikation, Roadmap-Details
   - Nach Eingang der Antworten: Systematischer Abgleich jeder Antwort gegen DD-Befunde
   - Re-Assessment: Was aendert sich an Conviction, Risiken, Staerken?
   - Output: `analysis/ddq-questions.md` (oder `analysis/ddq-questions-[name].md`), `analysis/ddq-assessment.md`
   - **DDQ-Analyse-Schema pro Frage:** (1) Was sagt der Gespraechspartner? (2) Bewertung gegen DD-Befunde (3) Entschaerft/Verschaerft/Neutral? (4) Netto-Effekt auf den Case
   - Am Ende: Aktualisierte Risiko-Matrix und Conviction mit klarer Begruendung was sich geaendert hat

   **Session-Datei-Format (kompakt):**

   Jede Session-Datei enthaelt:
   - `## Ziel` — Scope in 2-3 Saetzen
   - `## Regeln` — Einmalig: "Extraktionsregeln gemaess CLAUDE.md befolgen. Keine Interpretation in Sessions 1-3." **Plus Quellen-Bias-Klassifikation (siehe unten).**
   - `## Aufgaben` — Pro Aufgabenblock: Quelldateien (konkrete Pfade), Extraktionsanweisungen, Output-Format in EINEM Block. Keine separate Chunks- und Output-Sektion.
   - Tabellenvorlagen als Prosa: "Tabelle: Spalte1 | Spalte2 | Spalte3. Eine Zeile pro X." statt leerer Tabellenzeilen.
   - Metadata-Header und Boilerplate-Regeln NICHT pro Aufgabe wiederholen — einmal in `## Regeln`.

   **Quellen-Bias-Klassifikation (Pflicht-Sektion in jeder Sessions-Datei unter `## Regeln`):**

   Im DR sind Quellen unterschiedlich evidenz-stark. Subagents muessen pro extrahierter Behauptung den Bias-Faktor markieren. Hierarchie von staerkster zu schwaechster Evidenz:
   - **Public Filings (Companies House, EU Patent Office, USPTO):** rechtlich verbindlich. *Konfidenz: hoch.*
   - **Externe DD (unabhaengig):** z.B. unabhaengiger IP-Anwalt, paid-professional-services ohne Investment-Decision-Filter. *Konfidenz: hoch.*
   - **Externe DD (mit Bias-Faktor):** z.B. Tech-Report eines Co-Investors — externe Methodik, aber Investment-Decision-Filter (sie haben entschieden zu investieren). **NICHT als unabhaengige Validierung framen.** Bias-Faktor erfassen: wurde der Report vor oder nach der Investment-Decision verfasst? *Konfidenz: mittel.*
   - **Acceptance-Validation extern, Inhalt Founder:** z.B. Grant-Antrag (ESA/EU/Innovate UK/SBIR) — die Annahme ist extern validiert, Antragsinhalt selbst ist Founder-Behauptung. Beides trennen.
   - **Operativ-strukturiert (Founder, internal):** z.B. CRM-Pipeline-Report — strukturierte Felder zuverlaessiger als Stage-Bezeichnungen (Stage-Definitionen Founder-defined, Eintraege ungeprueft). Board Pack / Board Minutes oft die ehrlichste Founder-internal-Quelle.
   - **Founder-Narrative (Marketing):** Pitch Deck, Business Plan, Progress Updates, Competitor-Slide — Selbstdarstellung. *Konfidenz: niedrig — als Behauptung extrahieren, nicht als Fakt.*

   Vorsicht: "Externe DD" im DR-Ordner kann irrefuehrend sein. Pruefen wer den Report bestellt und bezahlt hat.

   **Chunk-Generierung (fuer Sessions 1-3):**

   In der `## Aufgaben` Sektion Chunks definieren:
   - Dateien nach Typ/Ordner gruppieren, max. 5-6 Quelldateien / ~100 PDF-Seiten pro Chunk
   - Pro Chunk: Quelldateien (Pfade), Output-Pfad (`.tmp/{session-name}/chunk-{letter}-{label}.md`), Extraktionsanweisungen + Output-Format, Hinweise
   - Chunks alphabetisch (A, B, C, ...)

   **Cross-Cut-Documents Pattern (DR-Files mit material fuer mehrere Sessions):**

   Beispiele: Board Pack (Legal-Governance + Financial-Snapshot + Operational-Update + Strategy), Investor-Update (Financial + Roadmap), Founder-Email-Thread (alle Bereiche). Solche Dokumente werden meist einer Primary-Session zugeordnet, aber ihr Material laeuft sonst Gefahr im falschen Output-File zu landen.

   Pattern: Der Chunk-Subagent in der **primaeren Session** (z.B. Session 01 Legal fuer Board Pack) schreibt zusaetzlich ein **Cross-Cut-File** `.tmp/{primary-session}/chunk-{letter}-cross-cut-for-session-{target}.md` mit Header `Source: ... — for cross-loading into {target-output-file}.md`. Der Consolidator der **Ziel-Session** (z.B. Session 03) liest diese File und integriert in eigene Sub-Sektion.

   Pflicht: In der Chunk-Definition explizit "Cross-Output-Pflicht: ..." nennen, falls Cross-Cut-Output erwartet wird. Auch wenn kein Material vorhanden ist: leere File mit Header schreiben, damit Ziel-Session weiss dass nichts zu integrieren ist.

   **Multi-Version-Files Pattern (z.B. Articles in 4 Versionen, SHA in 2 Versionen, Business Plan in 2 Stadien):**

   In Sessions 1-3 nur **Metadata-only-Extraktion** pro Version (Filing-Date, DATED-Suffix, Companies-House-Vermerk-ja/nein, MERCIA-/Investor-Prefix, Page-Count, erste-Seite-Datum, file-modification-date). **KEINE Aussage "Version X ist die aktuelle"** — Aufloesung macht Session 4 als analytische Aufgabe.

   Klauseln pro Version separat extrahieren (keine Cross-Version-Vergleichstabelle in Sessions 1-3). Cross-Version-Diff macht Session 4.

   **Cross-Chunk-Pflicht-Outputs (verstreutes Material aggregieren):**

   Wenn ein Thema ueber mehrere Chunks verstreut auftaucht (z.B. BOM-Komponenten in 3 Chunks, Customer-Erwaehnungen in 2 Chunks, Compliance-Standards in 4 Chunks): definiere eine **separate Pflicht-Sub-Sektion** in jedem relevanten Chunk-Output (z.B. `### ITAR-relevante Komponenten` oder `### Customer-Konkretisierung`). Konsolidator aggregiert in eigene Output-Sektion `## Cross-Chunk Aggregate`. Beispiele:
   - **Dual-Use / Defense:** ITAR-Komponenten-Inventur (BOM verstreut), Customer-Konkretisierung (konkrete Procurement-Entity wie "UK MOD Strategic Command" / "DSTL" / "DASA Project X" vs. Marketing-Wording "NATO and allied defense"), Redaction-Inventur (OPSEC-Signal), Regulatory Gaps (Export-Control, OST Article IX, NSI Act)
   - **B2B SaaS:** Customer-Tier-Bestaetigung (Enterprise vs. SMB tracking), Compliance-Standards-Inventur (SOC2, ISO27001, HIPAA, GDPR), Vendor-Lock-in-Risiken
   - **Hardware:** Long-Lead-Items, Single-Source-Risiken, Zertifizierungs-Inventur (CE, UL, OSHA, MIL-SPEC)
   - **Healthcare/Medical-Devices:** Klinische-Studien-Inventur, FDA/CE-Klassifikations-Inventur, Reimbursement-Codes

   **Key Metrics Pflicht (Sessions 1-3):**

   Jede Extraktions-Session muss im Output eine `## Key Metrics (fuer Cross-Referencing)` Sektion am Anfang vorschreiben:
   ```
   ## Key Metrics (fuer Cross-Referencing)
   | Metrik | Wert | Quelle |
   |---|---|---|
   ```
   Max 30 Zeilen, nur Fakten mit Quellenverweis. Alle Zahlen die potentiell ueber Dokumente hinweg vorkommen: Preise, Revenue, Team-Groesse, Margen, Flugzeiten, Reichweiten, Kapazitaeten, etc.

   **Session 4 Two-Phase Anleitung:**

   Die Session-4-Datei muss explizit zwei Phasen vorschreiben:
   1. **Phase 1 (Quick Scan):** Nur `## Key Metrics` Sektionen aller Extraktionsdateien laden (~90 Zeilen statt vollstaendiger Dateien). Alle Metriken in Vergleichstabelle. Diskrepanzen markieren. Checkliste: Preise, Revenue, Margen, Team-Groesse, Kapazitaeten vorhanden?
   2. **Fallback:** Falls Key Metrics unvollstaendig → sofort Full-Read der betroffenen Datei.
   3. **Phase 2 (Deep Dive):** Nur fuer Diskrepanzen die vollen Sektionen laden. Eigene Berechnungen durchfuehren.

   **Pflicht-Checkliste fuer Cross-Referencing (aus Praxis-Learnings):**

   Diese Checks muessen IMMER durchgefuehrt werden, unabhaengig von der Branche:
   - [ ] **GTM vs. Financial Model:** Stimmt die kommunizierte Go-to-Market-Strategie (Pitch Deck, Gespraeche) mit der Revenue-Logik im Financial Model ueberein? (z.B. "Rental-First" gesagt, aber Hardware-Sales im Model)
   - [ ] **Pipeline-Stage-Definitionen:** Was bedeuten die Pipeline-Stages konkret? "Closed" = verbindlicher Deal oder nur LOI/Pilot? Jede Stage-Definition hinterfragen
   - [ ] **Uncommitted Financing:** Enthaelt das Model Finanzierungsquellen (Venture Debt, Grants, Loans), die nicht committed sind? Jede Quelle als COMMITTED (Term Sheet/LOI vorhanden) oder ASSUMPTION markieren
   - [ ] **Burn-Rate-Konsistenz:** Wird "Burn" ueberall gleich definiert? CF Operating vs. CF Total vs. Investor Updates vs. Model vergleichen. Systematische Abweichungen dokumentieren
   - [ ] **Headcount-Plan vs. Realitaet:** Geplanter Headcount im Model vs. tatsaechliche Hiring-Geschwindigkeit. Extrapolation: Ist der geplante Ramp realistisch?
   - [ ] **Pricing-Validierung:** Wer hat den Preis tatsaechlich gesehen/validiert? Ein Deposit ≠ Preisvalidierung durch den Markt. Zwischen "ein Kunde hat $50K angezahlt" und "der Markt akzeptiert $525K" unterscheiden
   - [ ] **Revenue-Timeline-Realismus:** Wie lange dauert ein typischer Sales Cycle in dieser Branche? Passt die Revenue-Rampe im Model zum tatsaechlichen Sales Cycle?
   - [ ] **Model-Ist-Abgleich:** Stimmen die historischen Zahlen im Model (Rueckblick-Jahre) mit den tatsaechlichen Finanzberichten ueberein?
   - [ ] **Pricing-Konsistenz ueber Geographien:** Werden in verschiedenen Maerkten unterschiedliche Preise kommuniziert? (z.B. DACH vs. Nordics, DE vs. CH) Ist das bewusste Strategie oder Inkonsistenz? Welcher Preis steht im Financial Model?
   - [ ] **Incumbent-Service-Provider-Risiko:** Gibt es grosse Dienstleister die den gleichen Kunden bereits bedienen und die Startup-Loesung als Feature anbieten koennten? (z.B. FM-Unternehmen die Robotik hinzufuegen, IT-Dienstleister die AI-Features ergaenzen) Zeitfenster bis Incumbents nachziehen abschaetzen.
   - [ ] **Portfolio-Vergleich:** Gibt es eine eigene Portfolio-Company mit aehnlicher These oder aehnlichem Modell (auch in anderem Vertical)? Falls ja: Learnings, Synergien und Benchmarks aus der Portfolio-Company in die Analyse einbeziehen. User aktiv fragen: "Habt ihr eine Portfolio-Company die aehnlich aufgebaut ist?"
   - [ ] **Quellen-Bias bei "externer" DD:** Ist die "externe DD" (Tech-Report, IP Audit, Market-Study) im DR wirklich unabhaengig oder vom Co-Investor / Founder bezahlt? Beauftragung pruefen, Investment-Decision-Filter beachten. Ein Co-Investor-Tech-Report ist NICHT die gleiche Evidenz-Klasse wie ein unabhaengiger Auditor-Report.
   - [ ] **Multi-Version-Konsistenz:** Bei Dokumenten in mehreren Versionen (Articles, SHA, Business Plan, Cap Table): welche ist die aktuell-gueltige? Filing-Date vs. file-modification-date vs. Companies-House-Vermerk cross-checken. Pre-Round vs. Post-Round Diffs als Cross-Ref dokumentieren.
   - [ ] **Cross-Cut-Material vollstaendig integriert:** Board-Packs / Investor-Updates / Founder-Emails enthalten oft material das in mehrere Output-Files gehoert. Wurden alle Cross-Cut-Files erstellt und vom Ziel-Consolidator gelesen? Stichprobe pro Cross-Cut-File.

   **Session 5 Recherche-Bloecke (konsolidiert, branchenadaptiv):**

   **WICHTIG — Web-Recherche Fallback:** Falls Subagents keine WebSearch/WebFetch-Permission haben, fuehre die Web-Recherche SELBST durch (nicht ueber Subagents). Dispatche die 5 Bloecke dann als reine Analyse-Agents (Trainingswissen), und ergaenze kritische Datenpunkte (Founder-LinkedIn, Competitor-Funding, Marktdaten) manuell mit WebSearch im Hauptkontext. Alternativ: Alle 5 Bloecke sequentiell im Hauptkontext mit WebSearch durchfuehren.

   5 konsolidierte Recherche-Bloecke. Bloecke 2-4 werden aus dem Vertical-Modul geladen (falls vorhanden), sonst generisch:
   1. **Wettbewerb & Positionierung** — UNIVERSELL (Wettbewerber, Finanzierung, Bewertungs-Benchmarks, Marktanteile)
   2. **Markt-Tailwinds & Risiken** — AUS VERTICAL-MODUL `## Research Blocks → Block 2` (Fallback: Regulierung, Foerderprogramme, Makro-Trends, politische Risiken)
   3. **Kunden & Nachfrage-Validierung** — AUS VERTICAL-MODUL `## Research Blocks → Block 3` (Fallback: Referenzkunden, Marktnachfrage, Preis-Benchmarks, Sales-Cycle-Vergleiche)
   4. **Technologie & Produktions-Benchmarks** — AUS VERTICAL-MODUL `## Research Blocks → Block 4` (Fallback: BOM-Vergleiche, Technologie-Readiness, IP-Landschaft, Zulieferer-Risiken)
   5. **Gruender-Verifikation** — UNIVERSELL (LinkedIn, oeffentliche Quellen, Titel/Claims verifizieren, Patente, Litigation-Check)

   **Zusaetzlich aus Vertical-Modul (falls geladen):**
   - `## Risk Framework` → Als Referenz-Checkliste fuer die Conviction-Bildung in die Session-Datei einfuegen
   - `## Benchmarks` → Als Vergleichswerte fuer die Bewertungsanalyse einfuegen

6. **Check-in mit User:**
   - Zusammenfassung zeigen: Startup, gefundene Dokumente, geplante Sessions
   - **Portfolio-Vergleich abfragen:** "Habt ihr eine Portfolio-Company mit aehnlicher These oder aehnlichem Modell? (z.B. gleiches Vertical, aehnliches Geschaeftsmodell, aehnliche Plattform-These in anderem Sektor)" Falls ja: In Session 4 (Cross-Referencing) und Session 5 (Deep Analysis) als Benchmark einbeziehen.
   - **Externe Intel abfragen:** "Gibt es Informationen von Co-Investoren, Advisors oder aus Gespraechen die nicht im Data Room stehen?" Falls ja: In CLAUDE.md Startup-Kontext aufnehmen.
   - Fragen: "Soll ich mit Session 1 (Legal) starten?"

---

### Pfad B-Team: CLAUDE.md existiert, offene Session MIT Chunks → Subagent-basierte Extraktion

**Erkennung:** CLAUDE.md existiert, naechste offene Session-Datei hat eine `## Chunks` Sektion (innerhalb von `## Aufgaben`).

1. **Status lesen:** DD-Workflow-Tabelle in CLAUDE.md parsen
2. **Naechste offene Session identifizieren** (niedrigste Nummer mit Status OFFEN)
3. **Session-Datei laden:** `sessions/0X-*.md` lesen
4. **Chunks erkennen:** Pruefen ob Chunks in `## Aufgaben` definiert sind. Wenn NEIN → Pfad B-WriteEarly.
5. **Resume-Check:** Pruefen ob `.tmp/{session-name}/` existiert:
   - Ja → User fragen: "Es gibt bereits Zwischenergebnisse. Resume oder Neustart?"
     - Resume: Nur fehlende Chunks dispatchen
     - Neustart: `.tmp/{session-name}/` loeschen, alle Chunks dispatchen
   - Nein → `.tmp/{session-name}/` erstellen
6. **Extractor-Agents dispatchen** — pro Chunk einen Subagent (parallel via Agent-Tool):
   - Prompt enthaelt: Quelldatei-Pfade (absolut), Output-Pfad, Extraktionsanweisungen (aus der Aufgaben-Definition), Session-Nummer, Chunk-ID
   - **Key Metrics Pflicht:** Jeder Extractor schreibt seine Key Metrics am Chunk-Anfang.
7. **Completion pruefen:** Alle erwarteten Chunks vorhanden? Fehlend → User melden.
8. **Konsolidierung:**
   - **≤3 Chunks:** KEIN Consolidator-Agent. Orchestrator concateniert .tmp-Dateien in Reihenfolge, fasst Key-Metrics-Sektionen zu einer zusammen, schreibt Header. Spart einen Agent-Dispatch.
   - **>3 Chunks:** Consolidator-Agent mit schlankem Prompt: "Fasse die Chunk-Dateien zu einer Output-Datei zusammen. Dedupliziere gleiche Inhalte. Fuege zusammengefasste Key Metrics Sektion am Anfang hinzu."
9. **Cleanup:** `.tmp/{session-name}/` loeschen nach erfolgreicher Konsolidierung
10. **Status updaten:** In CLAUDE.md NUR Session-Status auf ERLEDIGT setzen. KEINE Datenpunkte, Flags oder Datenqualitaets-Details in CLAUDE.md einfuegen — diese gehoeren in die Output-Dateien. Falls Conviction/Risiken sich aendern (Session 4-5): Conviction-Zeile und Risiken-Sektion UEBERSCHREIBEN, nicht anhaengen.
11. **Check-in mit User:**
    - Zusammenfassung der Ergebnisse
    - Auffaelligkeiten / Diskrepanzen
    - "Soll ich mit Session X fortfahren?"

---

### Pfad B-WriteEarly: CLAUDE.md existiert, offene Session OHNE Chunks → Inkrementelle Extraktion

**Erkennung:** CLAUDE.md existiert, naechste offene Session-Datei hat KEINE Chunks, ODER Subagent-Dispatch fehlgeschlagen.

**Vorteil:** Extrahierte Daten werden nach jedem Dokument auf Disk geschrieben — bei Compaction gehen keine Details verloren.

1. **Status lesen:** DD-Workflow-Tabelle in CLAUDE.md parsen
2. **Naechste offene Session identifizieren**
3. **Session-Datei laden:** `sessions/0X-*.md` lesen
4. **Pro Quelldokument (sequentiell):**
   a. Dokument lesen
   b. Gemaess Extraktionsanweisungen strukturiert extrahieren
   c. **SOFORT** in Output-Datei appenden
   d. Extraktionsregeln gemaess CLAUDE.md befolgen
5. **Finalisierung:** Key Metrics Sektion am Anfang der Output-Datei, Qualitaets-Summary am Ende
6. **Status updaten:** In CLAUDE.md NUR Session-Status auf ERLEDIGT setzen. KEINE Datenpunkte, Flags oder Datenqualitaets-Details in CLAUDE.md einfuegen. Falls Conviction/Risiken sich aendern: UEBERSCHREIBEN, nicht anhaengen.
7. **Check-in mit User:**
   - Zusammenfassung der Ergebnisse
   - Auffaelligkeiten / Fragen
   - "Soll ich mit Session X fortfahren?"

---

### Pfad C: Alle Sessions ERLEDIGT → Zusammenfassung & Naechste Schritte

**Erkennung:** Alle DD-Workflow-Sessions (inkl. Session 6 DDQ, falls durchgefuehrt) Status ERLEDIGT. **KEINE** Active-Deal-Artefakte (kein `02_meetings/`, kein `report/*-for-investors.md`). Wenn Active-Deal-Artefakte existieren → Pfad D.

1. Kurze Zusammenfassung aller Ergebnisse zeigen
2. Auf `report/dd-report.md` verweisen
3. **Entscheidungs-Optionen anbieten:**
   - **Option A: Absage** → Absage-Mail an Gruender draften. **Verbindlich: `### Absage-Standard (Pass Letter)` im Methodik-Kern** — drei Entscheidungsfragen vorab (Endgueltigkeit, Schaerfe, Absender), Begruendungs-Ketten statt Behauptungen, konkreter Re-Engagement-Trigger, Confidentiality-Gate vor Ausgabe.
   - **Option B: Investment Memo** → Internes Memo fuer IC/Partner draftes
   - **Option C: Vertiefung** → Bestimmte Bereiche nochmal tiefer analysieren
   - **Option D: DDQ** → Falls Session 6 noch nicht durchgefuehrt: Fragen-Dokument fuer Gespraechspartner generieren
   - **Option E: Transition to Active Deal Mode** → Fund hat entschieden zu fuehren / zu investieren. Loest Bootstrap via `/dd:ingest` aus: legt `02_meetings/`, `exclusion-rules.md` + externes Investor-Memo-Skelett (`report/*-for-investors.md` aus `${CLAUDE_PLUGIN_ROOT}/templates/investor-memo-skeleton.md`, Fallback `~/.claude/dd-templates/investor-memo-skeleton.md`) an. Fragt User nach Exclusion-Terms (Co-Investor-Namen im Pitch, NDA-Personen). Erweitert `build-docx.py` um Exclusion-Hook-Snippet (`${CLAUDE_PLUGIN_ROOT}/templates/exclusion-hook-snippet.py`, Fallback `~/.claude/dd-templates/`). Nach Bootstrap direkt `/dd:ingest` verfuegbar fuer neue Inputs.
   - **Option F: Workspace finalisieren & aufräumen (EMPFOHLEN als Abschluss-Schritt)** → Reorganisiert den Workspace aus der flachen Run-Time-Struktur in die einheitliche finale 4-Ordner-Struktur (siehe `## Finale Ablage-Struktur`). **Als Default-nächsten-Schritt vorschlagen; nach kurzer Bestätigung ausführen.** Ablauf:
     1. **Zielordner anlegen:** `1 — Working Docs (Endergebnisse)/`, `2 — Analyse/Extraktion/`, `3 — Call-Prep & Prozess/`, `4 — Quellen/calls/`.
     2. **Dateien verschieben** gemäß Mapping-Tabelle (`extracted/*` → `2 — Analyse/Extraktion/`; `analysis/*` → `2 — Analyse/`; `analysis/ddq-*`, `dataroom-request`, Deal-Terms → `3 — Call-Prep & Prozess/`; `report/dd-report.md`, `report/investment-memo.md`, Advisor-/Experten-Briefs → `1 — Working Docs (Endergebnisse)/`).
     3. **Quelldateien:** workspace-interne Roh-/Quelldokumente → `4 — Quellen/` (Transkripte/Meeting-Notes → `calls/`). **Externer/separater Data-Room bleibt unberührt** (nur referenzieren).
     4. **DD-Master erzeugen:** `report/dd-report.md` zum `<deal> — DD-Master.md` in `1 — Working Docs (Endergebnisse)/` promoten/konsolidieren — ein Gesamtbild (Produkt, Tech, Team, Markt, Deal, Traction, Risiken, Conviction), jede Sektion mit Quellenverweis auf `2 — Analyse/`. Konsolidierung darf den `dd-consolidator`-Agent nutzen. Falls `dd-report.md` thematische Lücken hat: aus den Analyse-Files ergänzen.
     5. **`sessions/` aufräumen:** entfernen falls leer, sonst nach `2 — Analyse/_run-scaffolding/` archivieren.
     6. **CLAUDE.md updaten:** `Dateipfade`-Sektion + DD-Workflow-Output-Spalte auf die finalen Pfade umschreiben; **Finalize-Marker** setzen (Zeile `**Workspace finalisiert:** <Datum> — Struktur gemäß \`## Finale Ablage-Struktur\` (dd.md)`); interne Cross-Refs in allen `.md` fixen (`grep -rn 'analysis/\|report/\|extracted/'`).
     7. **Integritäts-Check:** Datei-Anzahl vor/nach gleich (+ neues DD-Master); keine toten Pfad-Referenzen.
     8. **Hub-Notiz nachziehen** (nur bei Obsidian-Stufe 1/2, siehe `## Obsidian-Integration`): `<Firma>.md` auf die finale 4-Ordner-Struktur umschreiben und Links auf die neu entstandenen Notizen ergänzen. Optional — schlägt der Schritt fehl, bleibt die Finalisierung gültig.
     Ab jetzt greift bei weiteren `/dd`-Aufrufen **Pfad F**.

---

### Pfad D: Active Deal Mode → Kontinuierlicher Input-Flow + Externes Memo

**Erkennung:** CLAUDE.md existiert, **alle Sessions ERLEDIGT**, UND mindestens eines der folgenden Active-Deal-Artefakte ist vorhanden:
- `02_meetings/` Ordner
- `report/*-for-investors.md` (externes Investor-Memo)
- `exclusion-rules.md` im Workspace-Root

**In diesem Modus arbeitet `dd.md` selbst nicht aus — es routet auf fokussierte Sub-Commands:**

| Situation / User-Intent | Routing |
|---|---|
| Neuer Input angekuendigt (Email, Call, WhatsApp, Confidential Forward) | `/dd:ingest` — Input-Triage mit Klassifikations-Frage + Propagations-Entscheidungsbaum |
| Rationality-Check am externen Memo (periodisch oder vor Investor-Dispatch) | `/dd:rationality-pass` — 12-Punkte-Audit gegen `${CLAUDE_PLUGIN_ROOT}/methoden/rationality-audit.md` (Fallback `~/.claude/dd-methoden/rationality-audit.md`) |
| Absage-Entscheidung gefallen (auch aus dem Active Deal heraus) | `### Absage-Standard (Pass Letter)` im Methodik-Kern — das Confidentiality-Gate greift hier besonders: verdeckte Channel-Checks und `exclusion-rules.md`-Terms sind in diesem Modus die Regel, nicht die Ausnahme |
| Memo-Rebuild (nach Edit) | Direkt `python3 report/build-docx.py` — Exclusion-Hook laeuft automatisch vor Pandoc. Bei Treffer: Abbruch mit Liste. Override nur mit `--override --reason "<text>"` |
| Keine konkrete Intent-Angabe | User nach Ziel fragen (Optionen wie oben) |

**Shared Methoden-Referenzen, die in diesem Modus immer verfuegbar sein muessen:**
- `${CLAUDE_PLUGIN_ROOT}/methoden/taxonomies.md` (Fallback `~/.claude/dd-methoden/taxonomies.md`) — verbindliche Taxonomien (Evidence-Level, Pilot-Stage, Team-Status, Investor-Status, TRL-Disaggregation, Bus-Factor-Split, Burn-Rate-Framing)
- `${CLAUDE_PLUGIN_ROOT}/methoden/rationality-audit.md` (Fallback `~/.claude/dd-methoden/rationality-audit.md`) — 12-Punkte-Checkliste inkl. Bias-Priming

**Workspace-Konventionen im Active-Deal-Modus:**

```
02_meetings/                                    # Meeting-Notes pro Input (YYYY-MM-DD_<topic>.md)
03_internal-analysis/                           # Interne Arbeits-Notizen
report/
  <deal>-techdd-for-investors.md                # Externes Memo (Markdown = Source of Truth)
  internal/
    tech-dd-report-INTERNAL-ONLY.md             # Interner Report (inkl. NDA-Content)
  archive/                                      # Superseded Versionen
exclusion-rules.md                              # Per-Projekt Build-Blocker-Terms (Hard-Enforcement)
```

**Layered mit finaler Struktur (falls Workspace bereits finalisiert, Pfad F):** Menschlich-finale Deliverables (DD-Master, Lesefassung des externen Memos, Advisor-/Experten-Briefs) liegen in `1 — Working Docs (Endergebnisse)/`; Meeting-Notes → `4 — Quellen/calls/`. Die **Build-Pipeline bleibt unverändert** — `report/build-docx.py`, das Markdown-Source-of-Truth `report/*-for-investors.md` und `exclusion-rules.md` behalten ihre Pfade (kein Pfad-Bruch, kein Re-Wiring der Pandoc-Kette).

**Memory-Integration:** Der Assistant liest beim Active-Deal-Routing die User-Memory (`~/.claude/projects/*/memory/project_<deal>_round.md`, falls vorhanden) fuer Round-State, Pilot-Pipeline, Team-Status und Framing-Entscheidungen. Updates durch `/dd:ingest`.

**Anti-Pattern in Active-Deal:**
- Kein direktes Edit am externen Memo ohne Klassifikations-Check des Inputs (nur "External-referenceable"-Klassifikationen duerfen extern flieszen)
- Kein Automatik-Edit bei Judgment-Call-Framings — `/dd:ingest` und `/dd:rationality-pass` stellen `AskUserQuestion`
- Kein Memo-Rebuild ohne Exclusion-Hook-Check — der Hook blockt hart
- Keine Plural-Formen ohne Count, keine Superlative ohne Evidenz — siehe `rationality-audit.md`

---

### Pfad F: Finalisierter Workspace → Laufende Arbeit in der finalen Struktur

**Erkennung:** Nummerierte Ordner vorhanden (`1 — Working Docs (Endergebnisse)/`, `2 — Analyse/` etc.) **oder** Finalize-Marker (`**Workspace finalisiert:**`) in CLAUDE.md.

In diesem Modus ist der Workspace bereits aufgeräumt. Es wird **nicht** neu reorganisiert. Stattdessen werden neue Materialien und neu erstellte Dokumente gemäß den **Platzierungsregeln** (siehe `## Finale Ablage-Struktur`) in den jeweils richtigen Ordner einsortiert:

| Was kommt rein | Wohin |
|---|---|
| Neue Quelldateien / Data-Room-Material (workspace-intern), Transkripte | `4 — Quellen/` bzw. `4 — Quellen/calls/` (externer Data-Room bleibt unberührt) |
| Neue Roh-Extraktion | `2 — Analyse/Extraktion/` |
| Neue Analyse / Working-Notes / Research | `2 — Analyse/` |
| Neue Fragen-Listen / DDQ / Data-Room-Requests / Deal-Terms | `3 — Call-Prep & Prozess/` |
| Neu erstellte Deliverables (DD-Master-Update, Advisor-/Experten-Briefs, Investor-Memo, Absage) | `1 — Working Docs (Endergebnisse)/` (Absage: nach `### Absage-Standard (Pass Letter)` draften) |

**Vorgehen:**
1. Bei neuem Input/Dokument: Ziel-Ordner nach obiger Tabelle bestimmen, dort ablegen/erstellen. Betrifft es bereits abgeschlossene Analysen → in die bestehende Datei im richtigen Ordner appenden (analog „Externe Informations-Integration").
2. **DD-Master pflegen:** Substanzielle neue Erkenntnisse, die die Conviction/Risiken bewegen, in `1 — Working Docs (Endergebnisse)/<deal> — DD-Master.md` einarbeiten und CLAUDE.md-Conviction/Risiken überschreiben (nicht anhängen).
3. **Active-Deal-Intent** (laufende Investor-Memos/Meetings nach Invest-Entscheidung) → auf die Sub-Commands routen wie in Pfad D (`/dd:ingest`, `/dd:rationality-pass`, Memo-Rebuild). Build-Pipeline-Pfade bleiben (`report/build-docx.py`); siehe Layered-Notiz in Pfad D.
4. Keine konkrete Intent-Angabe → User nach Ziel fragen.

---

## Finale Ablage-Struktur (nach Run-Abschluss)

**Während des Runs** schreibt der Workflow in die flache Struktur (`extracted/`, `analysis/`, `report/`, `sessions/` — siehe Pfad A). **Bei Run-Abschluss** wird der Workspace auf Bestätigung in die folgende einheitliche 4-Ordner-Struktur reorganisiert (Pfad C → Option F). **Danach** (Pfad F) wird in dieser Struktur weitergearbeitet. Ziel: jeder Deal einheitlich abgelegt — klare Trennung Endergebnisse ↔ Arbeitsmaterial.

```
<deal>/
├─ CLAUDE.md
├─ 1 — Working Docs (Endergebnisse)/   Deliverables: <deal> — DD-Master.md (Gesamtwissen),
│                                       dd-report, investment-memo, Advisor-/Experten-Briefs, Absage-Mail
├─ 2 — Analyse/                         cross-references, working-notes, research-*, research-notes
│   └─ Extraktion/                      legal, investments, product-market, financials (ehem. extracted/)
├─ 3 — Call-Prep & Prozess/             ddq-questions, ddq-assessment, dataroom-request, deal-terms
└─ 4 — Quellen/                         Roh-Inputs (workspace-intern); calls/ = Transkripte/Meeting-Notes
```

**Mapping Run-Time → Final** (verbindlich für die Reorganisation in Option F):
| Run-Time (flach) | Final |
|---|---|
| `extracted/*.md` | `2 — Analyse/Extraktion/` |
| `analysis/*` (cross-references, working-notes, research-*, research-notes) | `2 — Analyse/` |
| `analysis/ddq-questions*.md`, `analysis/ddq-assessment.md` | `3 — Call-Prep & Prozess/` |
| `analysis/dataroom-request.md`, Deal-Terms/Prozess-Notizen | `3 — Call-Prep & Prozess/` |
| `report/dd-report.md` | `1 — Working Docs (Endergebnisse)/` → wird zum/ergänzt das **DD-Master** |
| `report/investment-memo.md`, Advisor-/Experten-Briefs | `1 — Working Docs (Endergebnisse)/` |
| workspace-interne Quelldateien / Transkripte | `4 — Quellen/` (Transkripte/Meeting-Notes → `calls/`) |
| `sessions/` (Run-Scaffolding) | nach Reorg entfernen (falls leer) bzw. nach `2 — Analyse/_run-scaffolding/` archivieren |

**Platzierungsregeln (gelten dauerhaft ab Finalisierung, siehe Pfad F):**
- Neue Quelldateien / Data-Room-Material (workspace-intern) → `4 — Quellen/`; Transkripte/Meeting-Notes → `4 — Quellen/calls/`. Ein **externer/separater Data-Room-Pfad bleibt unberührt** und wird nur referenziert.
- Neue Roh-Extraktion → `2 — Analyse/Extraktion/`; neue Analyse / Working-Notes / Research → `2 — Analyse/`.
- Neue Fragen-Listen / DDQ / Data-Room-Requests / Deal-Terms / Prozess-Docs → `3 — Call-Prep & Prozess/`.
- Neu erstellte fertige Deliverables (DD-Master-Update, Advisor-/Experten-Briefs, Investor-Memo, Absage-Mail) → `1 — Working Docs (Endergebnisse)/`.

---

## Obsidian-Integration (optional)

**Der Normalfall ist Stufe 0 — ohne Obsidian aendert sich am Workflow nichts.**
Dieser Abschnitt beschreibt eine Zusatzfunktion fuer alle, die ihre DD-Workspaces
in einem Obsidian-Vault fuehren. Wer das nicht tut, ueberspringt ihn vollstaendig;
es darf dadurch **kein Fehler und kein toter Link** entstehen.

### Stufe ermitteln

Ein Obsidian-Vault ist per Definition ein Ordner mit `.obsidian/` darin. Vom
Workspace aus aufwaerts suchen; die Themen-/Portfolio-Ordner per **Namensmuster**
pruefen, nicht per festem Pfad — so funktioniert es in jedem Vault, der eine
aehnliche Struktur verwendet:

```bash
d="$PWD"; vault=""
while [ "$d" != "/" ]; do [ -d "$d/.obsidian" ] && { vault="$d"; break; }; d=$(dirname "$d"); done

themen=""; portfolio=""
if [ -n "$vault" ]; then
  themen=$(find "$vault" -maxdepth 1 -type d \( -iname '*themen*' -o -iname '*thesen*' -o -iname '*themes*' -o -iname '*topics*' \) | head -1)
  portfolio=$(find "$vault" -maxdepth 1 -type d -iname '*portfolio*' | head -1)
fi
```

| Stufe | Bedingung | Verhalten |
|---|---|---|
| **0** | `$vault` leer | Nichts tun. Keine Hub-Notiz, kein Frontmatter, keine Wikilinks. |
| **1** | `$vault` gefunden | Hub-Notiz mit Frontmatter und Links auf die Notizen des Workspaces. Keine Annahme ueber die Vault-Struktur. |
| **2** | zusaetzlich `$themen` und/oder `$portfolio` vorhanden | Zusaetzlich `vertical:` auf die Themen-Notiz verlinken und Portfolio-Bezuege setzen. |

Die erkannte Stufe dem User in **einer Zeile** melden, damit er widersprechen kann
— analog zur Meldung beim Vertical-Modul-Matching. Beispiel: *"Obsidian-Vault
erkannt (Stufe 2) — lege zusaetzlich eine Hub-Notiz mit Themen-Verlinkung an."*

### Hub-Notiz

Datei `<Firma>.md` im Workspace-Root, **getrennt von der `CLAUDE.md`**: die
CLAUDE.md bleibt Zustandsdatei des Workflows, die Hub-Notiz ist der menschliche
Einstieg und darf beliebig lang sein.

```yaml
---
typ: deal
firma: <Rechtstraeger laut Register>
sitz: <Ort, Land>
branche: <eine Zeile>
vertical: "[[<Themen-Ordner>/<These>|<These>]]"   # nur Stufe 2, sonst weglassen
stadium: <Pre-Seed | Seed | Series A | unbekannt>
status: <aktiv | abgesagt | unbekannt>
tags: [dd-case]
---
```

Im Rumpf: Kurzsteckbrief, dann Links auf **alle** Notizen des Workspaces, nach
Bereichen gruppiert (Working Docs, Report, Analyse, Extraktion, Call-Prep,
Quellen). Das ergibt pro Deal einen Stern im Graphen statt verstreuter Punkte.

**Zwei Regeln:**

- **Wikilinks immer mit vollem vault-relativem Pfad**, denn Dateinamen wiederholen
  sich ueber Deals hinweg — `working-notes.md` existiert in jedem Workspace.
  Also `[[<Pfad-zum-Workspace>/analysis/working-notes|working-notes]]`, nicht
  `[[working-notes]]`.
- **`status` nicht erfinden.** Nur setzen, was die Quellen hergeben; sonst
  `unbekannt`. Ein plausibel geratener Deal-Status ist schlimmer als eine Luecke.

### Bei Finalisierung (Pfad C Option F)

Die Hub-Notiz auf die finale 4-Ordner-Struktur umschreiben und die Links auf die
inzwischen entstandenen Notizen ergaenzen. Auch das ist optional und nur bei
Stufe 1 oder 2 relevant.

---

## Methodik-Kern

### Extraktionsregeln (Sessions 1-3)

Dies ist die **einzige Quelle** fuer Extraktionsregeln. Sie werden bei Setup einmalig in CLAUDE.md kopiert. Session-Dateien referenzieren nur: "Extraktionsregeln gemaess CLAUDE.md befolgen."

- **Metadata-Header** pro Datei: `Quelle: [Dateiname]`, `Datenqualitaet: [EXCELLENT/GOOD/PARTIAL]`
- Tabellen wo moeglich, Fliesstext wo noetig
- `~` = Best-Effort-Lesung, `*(unclear)*` = nicht lesbar
- **Keine Interpretation** — nur extrahieren
- Lieber zu viel als zu wenig
- CLAs: IMMER Key Terms (Loan Amount, Interest, Discount, Cap, Maturity, QFR Definition)
- Cap Table: Alle Stakeholder mit Shares, %-Anteilen (FDC), Series
- Vertraege: Volumen, Preise, Lieferbedingungen, Zahlungsbedingungen
- **Key Metrics Pflicht:** Jede Extraktionsdatei beginnt mit `## Key Metrics (fuer Cross-Referencing)` — max 30 Zeilen, alle quervergleichbaren Zahlen mit Quellenverweis
- **Quellen-Bias-Hierarchie (Pflicht):** Pro extrahierter Behauptung den Bias-Faktor markieren (siehe Pfad-A Session-Datei-Format-Sektion fuer Hierarchie). Wichtig: "Externe DD" von Co-Investor ist NICHT unabhaengige Validierung. Grant-Acceptance (extern validiert) ist nicht dasselbe wie Grant-Antragsinhalt (Founder-Behauptung).
- **Multi-Version-Disziplin:** Bei mehreren Versionen eines Dokuments (Articles, SHA, BP, Cap Table): Metadata-only-Extraktion in Sessions 1-3, Aufloesung "welche ist gueltig" in Session 4.
- **Cross-Cut-Output-Pflicht:** Wenn ein File material fuer mehrere Sessions enthaelt (Board Pack, Investor Update, Founder-Email-Thread): separate Cross-Cut-File mit klarem Header `Source: ... — for cross-loading into ...` schreiben.
- **Cross-Chunk-Aggregate-Pflicht:** Verstreute Themen (BOM-Komponenten, Customer-Erwaehnungen, Compliance-Standards) in jedem relevanten Chunk-Output als separate Sub-Sektion ausweisen — Consolidator aggregiert in eigene Cross-Chunk-Output-Sektion.

### Bias-Prevention (Session 4-5)
- Eigene Berechnungen durchfuehren, nicht Startup-Zahlen uebernehmen
- Aktiv nach Gegenbeweisen suchen
- "Was muesste wahr sein, damit dieses Investment NICHT funktioniert?"
- Gruender-Claims verifizieren, nicht akzeptieren
- Bewertung gegen Comparables pruefen

### Qualitaetsstandards
- Jede Zahl muss eine Quelle haben
- Widersprueche explizit dokumentieren
- Unsicherheit kennzeichnen, nicht verstecken
- Fehlende Informationen als Gap markieren

### Absage-Standard (Pass Letter)

Eine Absage ist oft das einzige Produkt, das ein Founder von uns bekommt — und bei ehrlicher Begruendung das wertvollste Feedback der ganzen Runde. Dieser Standard gilt fuer JEDE Absage. Dies ist die **einzige Quelle** fuer Absage-Regeln; Pfad C (Option A), Pfad D und Pfad F referenzieren nur hierher.

**Vor dem Draft: drei Entscheidungsfragen an den User** (via `AskUserQuestion`, nicht raten):
1. **Endgueltigkeit** — endgueltiges Nein / "not now" mit konkretem Re-Engagement-Trigger / Nein + Angebot Feedback-Call. Empfehlung "not now", wenn der Case an fehlender **Evidenz** scheitert und nicht an fehlender Substanz.
2. **Schaerfe** — werden Prozess- und Evidenz-Luecken benannt (nie gelieferte Metriken, undokumentierte Terms, Widersprueche)? Optionen: gar nicht / eingebettet als Vorwaerts-Feedback / explizit benannt. **Diese Frage veraendert die Mail am staerksten.**
3. **Absender** — Einzelperson / Einzelperson im Namen des Fonds ("X und ich") / Fonds. Spiegelt, wer die Entscheidung tatsaechlich getragen hat.

Ton wird NICHT abgefragt — der Ton IST dieser Standard: direkt, respektvoll, argumentiert, ohne Floskeln und ohne Herablassung.

**Struktur (5-6 Absaetze, ~350-450 Woerter — jeder Absatz traegt ein Argument, kein Fuellabsatz):**

1. **Dank + klare Absage im ersten Absatz.** Kein Spannungsbogen, kein "leider muessen wir Ihnen mitteilen"-Anlauf. Ein Satz, der ankuendigt, dass die echte Begruendung folgt.
2. **Max. 2-3 Gruende, je als Begruendungs-Kette:** *Behauptung → Mechanik (warum ist das so) → Konsequenz fuer den Case.* **Ein Grund ohne Mechanik ist Fluff.** Gruende aus den Top-5-Risiken des DD-Reports ableiten, aber NUR strukturelle/strategische Punkte (Markt, Skalierung, Bewertung, Wettbewerb, Timing). Beispielform: "Markt X ist schwer zu integrieren" *weil* [3 konkrete strukturelle Merkmale] *weshalb* [jeder Kunde = Integrationsprojekt statt Rollout].
3. **Fonds-Restriktion offenlegen.** Die konkrete Einschraenkung nennen, die die Entscheidung mittraegt (kein Follow-on-Kapital, Ticket-Groesse, Stage-Mandat, Portfolio-Konflikt, Timing-Fenster). Macht aus einem Urteil ueber die Firma eine nachpruefbare Aussage ueber uns — und senkt das Risiko, dass unser Nein als Signal an andere Investoren zirkuliert.
4. **Re-Engagement-Trigger — konkret und messbar.** 2-4 benannte Kennzahlen oder Ereignisse, bei denen wir erneut schauen wuerden. **Pflicht-Selbsttest: Wer nicht formulieren kann, was ihn umstimmen wuerde, hat keine belastbare Begruendung — dann zurueck zu den Top-Risiken.** Bei endgueltigem Nein entfaellt der Absatz; die Selbsttest-Frage bleibt trotzdem intern zu beantworten.
5. **Eine spezifische Anerkennung.** Etwas, das nur jemand sagen kann, der das Material gelesen hat (eine konkrete Zahl, eine Modell-Eigenschaft, eine Entscheidung des Teams) — idealerweise mit Nutzwert fuer die naechsten Investoren-Gespraeche. Generisches Lob ("starkes Team") ist Fluff und wird als solches gelesen.

**Zeitliche vs. absolute Ablehnung trennen:** Halten wir den Markt fuer kommend, aber noch nicht reif, das explizit so sagen — **inklusive der eigenen Unsicherheit ueber das Zeitfenster** ("wir koennen von hier aus nicht beurteilen, ob die Luecke 18 Monate oder vier Jahre ist"). Ein "zu frueh fuer uns" ist eine andere Aussage als "das funktioniert nicht" und muss auch so klingen.

**Nicht-benannte Kritik implizit transportieren:** Entscheidet der User, Evidenz-Luecken NICHT zu benennen (Frage 2), koennen dieselben Punkte als vorwaertsgerichtete Re-Engagement-Bedingungen erscheinen. Die nie gelieferte Metrik wird zur Bedingung, unter der wir erneut schauen — dieselbe Information, ohne Vorwurf.

**Sprache:** Sprache der bisherigen Founder-Kommunikation, nicht die Default-Sprache des Workflows. Die Absage-Mail ist der haeufigste Fall, in dem der Deutsch-Default bewusst gebrochen wird (Interna zum Deal bleiben Deutsch).

**Confidentiality-Gate vor Ausgabe (Pflicht):** Draft gegen `exclusion-rules.md` pruefen (falls vorhanden). Zusaetzlich IMMER entfernen:
- Erkenntnisse aus verdeckten Kanaelen (Channel-Checks, Reference-Calls, Insider-Kontakte) — auch paraphrasiert und auch dann, wenn die Quelle nicht genannt wird
- Namen anderer Investoren/Leads, solange nicht oeffentlich oder freigegeben
- Interne Bewertungs-, Cap- und Return-Rechnungen, Verwaesserungs-Szenarien, Portfolio-Interna
- Persoenliche Kritik am Team (Titel-Diskrepanzen, Lebenslauf-Zweifel, Rollen-Anomalien) und handwerkliche Model-Fehler

Nach der Pruefung explizit berichten, wogegen geprueft wurde.

**Nach Freigabe/Versand:** Absage-Mail in `1 — Working Docs (Endergebnisse)/` ablegen; Conviction in CLAUDE.md und im DD-Report/DD-Master auf **PASS** setzen — mit Datum, den 2-3 tragenden Gruenden und dem Re-Engagement-Trigger. Damit ist bei erneutem Kontakt nachvollziehbar, warum wir abgesagt haben und was sich geaendert haben muesste.
