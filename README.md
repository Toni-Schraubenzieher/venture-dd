# Kensho DD — Due Diligence Plugin for Claude Code

Kritischer VC-Analyst fuer Startup-Bewertung. 6-Session-Workflow mit automatischer Datenextraktion, Cross-Referencing, Web-Recherche und branchenspezifischen Vertical-Modulen.

## Installation

```bash
claude plugin add https://github.com/Toni-Schraubenzieher/kensho-dd
```

## Usage

Navigate to a deal's data room folder (containing PDFs, Decks, Spreadsheets) and run:

```
/dd
```

The workflow automatically detects the state and guides through 6 sessions:

1. **Legal & Vertraege** — Gesellschaftsvertrag, SHA, CLAs, Kundenvertraege
2. **Investments & Cap Table** — CLAs, Cap Table, Conversion-Szenarien
3. **Produkt, Markt & Financials** — Produkte, Marktgroesse, Unit Economics, Financial Model
4. **Cross-Referencing** — Two-Phase Widerspruchs-Analyse mit eigenen Berechnungen
5. **Deep Analysis & Conviction** — Web-Recherche, Gruender-Verifikation, Top-5-Risiken
6. **DDQ** — Gruender-Befragung & Re-Assessment

## Vertical-Module

Branchenspezifische Module erhoehen die Analysetiefe:

- `hardware-robotics` — Hardware-Startups, Robotik, Autonome Systeme
- `space-logistics` — Space, Satelliten, Orbital-Logistik

Eigene Verticals erstellen: Siehe `skills/dd/references/verticals/_template.md`

## Features

- Automatische Data Room Erkennung und Kategorisierung
- Parallele Subagent-Extraktion fuer grosse Data Rooms
- Bias-Prevention: Eigene Berechnungen, aktive Suche nach Gegenbeweisen
- Branchenadaptive Recherche-Queries und Benchmarks
- Investment Memo und Absage-Mail Generierung

## Sprache

Alle Outputs auf Deutsch. Web-Recherche Queries auf Englisch.
