---
description: "DD Active Deal — Rationality Pass gegen externes Investor-Memo (Drift-Audit)"
---

# DD Active Deal — Rationality Pass

Du fuehrst einen strukturierten Audit gegen ein Target-File aus (default: das externe Investor-Memo), mit dem expliziten Ziel, Drift-Muster zu identifizieren, die aus der eigenen Conviction-Einbettung im Case entstehen. Du arbeitest die Checkliste in `${CLAUDE_PLUGIN_ROOT}/methoden/rationality-audit.md` (Fallback `~/.claude/dd-methoden/rationality-audit.md`) durch und produzierst einen strukturierten Befund — keine automatischen Edits.

**Sprache:** Deutsch fuer Befund und User-Interaktion. Edits am englischen Memo bleiben englisch.

---

## Phase 0: Bias-Priming (laut lesen, nicht ueberspringen)

Bevor du die Checkliste anwendest, lies den Bias-Priming-Abschnitt aus `rationality-audit.md` §0:

*"Du hast Conviction im Case. Genau darum entstehen die Drift-Muster. Diese Checkliste arbeitet gegen deine eigene Sympathie."*

Der Rationality-Pass ist **nicht primaer gegen AI-Drift**, sondern gegen die eigene VC-Einbettung. Dokumentiere drei Leitfragen fuer dich selbst bevor du beginnst:

1. Was habe ich an diesem Case emotional investiert?
2. Welche Claims lese ich wohlwollender als sie es verdienen?
3. Welche Schwaechen habe ich bisher durchgewunken, weil ich dem Founder / Team vertraue?

Das ist kein Performativ-Schritt. Wenn dir keine ehrliche Antwort einfaellt, ist das ein Signal, nicht eine Ausrede.

---

## Phase 1: Target + Referenzen laden

### Target-File

Default: das externe Investor-Memo im aktuellen Workspace. Typische Pfade:
- `report/*-for-investors.md`
- `report/*-techdd-for-investors.md`

Falls der User ein anderes Target nennt (z.B. `"lauf den rationality-pass gegen die Pilot-Tabelle in Section 5.3"`): Scope entsprechend einschraenken.

### Referenzen laden

1. **`${CLAUDE_PLUGIN_ROOT}/methoden/taxonomies.md` (Fallback `~/.claude/dd-methoden/taxonomies.md`)** — die 7 Taxonomien (Evidence-Level, Pilot-Stage, Team-Status, Investor-Status, TRL-Disaggregation, Bus-Factor-Split, Burn-Rate-Framing)
2. **`${CLAUDE_PLUGIN_ROOT}/methoden/rationality-audit.md` (Fallback `~/.claude/dd-methoden/rationality-audit.md`)** — die 12 Audit-Punkte
3. **Internal DD-Report**: `report/internal/tech-dd-report-INTERNAL-ONLY.md` (falls vorhanden) — Basis fuer §10 Hidden-Risk-Check
4. **Memory-File**: `~/.claude/projects/*/memory/project_<deal>_round.md` — Basis fuer §5 Team-Titel-Honesty und §6 Evidence-Level-Abgleich
5. **Exclusion-Rules**: `exclusion-rules.md` im Workspace — Basis fuer §12

---

## Phase 2: Checkliste abarbeiten

Gehe alle 12 Punkte aus `rationality-audit.md` durch (Bias-Priming + 12 Audit-Punkte). Pro Punkt:

1. **Scan durchfuehren** — Grep, String-Search, semantische Pruefung je nach Punkt
2. **Findings dokumentieren** — jede Stelle mit Zeilen-Referenz und 1–2 Satz Diagnose
3. **Kategorisieren**:
   - 🔴 **Klar (Change noetig)** — faktischer Fehler, Taxonomie-Verletzung, Hidden-Risk
   - 🟡 **Judgment-Call** — Framing-Frage, bei der mehrere Optionen legitim sind (→ AskUserQuestion)
   - 🟢 **OK** — geprueft, kein Finding

**Format pro Punkt (Beispiel):**

```markdown
### §2 Plural-Overclaim-Audit

**Scan:** Suche nach Pluralen von pilots / contracts / partnerships / customers / deployments / reviews.

**Findings:**

| # | Zeile | Stelle | Befund | Kategorie |
|---|---|---|---|---|
| 1 | 304 | "committed, contracted pilots — not demonstrations" | Plural, aber nur 1 signed pilot (ANA). Die anderen sind P3-P6 (siehe taxonomies.md §2) | 🔴 Klar |
| 2 | 293 | "active pilots across multiple defense theatres" | Plural trifft zu (4 Theater), aber "pilots" ist taxonomisch zu stark — waeren "engagements" | 🟡 Judgment |

**Proposed Remediation:** ...
```

### Priorisierungs-Hinweise

- §0 (Bias-Priming): nur Text-Dokumentation, keine Findings
- §1 (Superlativ-Budget): einfacher Scan, typischerweise 0–3 Findings
- §2 (Plural-Overclaim): haeufigste Drift, 2–5 Findings normal
- §3 (Blanket-Statements): 1–4 Findings, oft in Investment-Thesis-Sektion
- §4 (Already-Answered): Exec Summary + Section 8 intensiver scannen
- §5 (Team-Titel-Honesty): Section 2.3 + 2.4 + 1.Team-Tabelle
- §6 (Evidence-Level): Section 5.2 Fokus
- §7 (TRL-Disaggregation): Section 1 + Section 5 Fokus
- §8 (Bus-Factor-Split): Section 1 + Section 4.5
- §9 (Burn-Rate): Section 7.5
- §10 (Hidden-Risk): **Kritischster Audit-Punkt** — sorgfaeltiger Diff internal vs. external
- §11 (Quote-Footnote-Integrity): alle spezifischen Zahlen + Direkt-Zitate
- §12 (Exclusion-Cross-Check): schnelle Grep-Pruefung — fasst was `build-docx.py`-Hook ohnehin blockiert

---

## Phase 3: Judgment-Calls als AskUserQuestion

Alle 🟡-Findings werden dem User als `AskUserQuestion` vorgelegt — niemals automatisch geaendert.

**AskUserQuestion-Pattern:**

- Max. 4 Fragen pro Batch (Tool-Limit)
- Pro Frage: 2–3 Optionen inkl. "Aktuelle Formulierung beibehalten"
- Option-Descriptions machen den Trade-Off explizit (Transparenz vs. Momentum; Dezentheit vs. Klarheit; Vollstaendigkeit vs. Laenge)
- Bei mehr als 4 Judgment-Calls: nach Prioritaet bundeln (wichtigste 4 zuerst, Rest im naechsten Batch)

**Beispiel-Formulierung:**

```
Frage: Wie soll die Aussage "X Independent technical evaluations" in Section 5.2 gehandelt werden?
Optionen:
A) In zwei Ebenen unterteilen — Informal Expert Reviews vs. Partner-Programm-Eligibility
B) Klarstellen, dass keine formelle unabhaengige Zertifizierung darunter ist
C) Aktuelle Formulierung beibehalten
```

---

## Phase 4: Befund zusammenfuehren

Produziere am Ende einen strukturierten Befund mit folgenden Sektionen:

```markdown
# Rationality-Pass Befund — [Target-File, Datum]

## Summary
- Gesamtzahl Findings: X (🔴 Y klare Changes, 🟡 Z Judgment-Calls, 🟢 W OK)
- Kritischster Punkt: [§10 Hidden-Risk oder §5 Team-Titel, je nach Schwerpunkt]
- Empfohlene Reihenfolge der Remediation: [1., 2., 3., ...]

## Findings nach Punkt
[§1 bis §12 wie in Phase 2]

## Judgment-Call-Batches (AskUserQuestion)
[werden nacheinander an User gestellt]

## Ausstehende Remediations (nach User-Entscheidungen)
[Change-Liste mit konkreten Edit-Anweisungen — NICHT automatisch angewendet]
```

---

## Phase 5: Remediation (nur nach expliziter Freigabe)

Erst wenn der User entweder "go" sagt oder die einzelnen Judgment-Calls entschieden hat, werden die Changes via `Edit` angewendet.

**Wichtig:**
- Jede Aenderung einzeln mit Zeilen-Verweis durchfuehren
- Nach allen Aenderungen: `build-docx.py` rebuilden (inkl. Exclusion-Hook)
- Final: kurzer Verification-Grep, dass die adressierten Drift-Muster reduziert sind (z.B. Superlativ-Count, Plural-Count)

---

## Anti-Patterns (nicht tun)

- **Mechanisches Abhaken der Checkliste.** Der Wert des Passes entsteht durch die Frage *"welchen Drift adressiert dieser Audit und greift er hier?"*, nicht durch die Anzahl der abgearbeiteten Punkte.
- **Automatische Edits bei 🟡-Findings.** Judgment-Calls gehoeren zum User, nicht zum Assistant.
- **Ueberrollen der User-Preferences.** Wenn der User in vorangegangenen Konversationen klare Framings festgelegt hat (z.B. ein Co-Investor, der nicht genannt werden darf, oder ein Behoerdenkontakt ohne Namen), sind diese als Constraint fix.
- **Hidden-Risk-Check ueberspringen.** §10 ist der wichtigste Audit — wenn eine Stelle im internen Report als KRITISCH markiert ist und im externen Memo nicht auftaucht, muss das explizit entweder adressiert oder als bewusste Exclusion-Entscheidung dokumentiert werden.

---

## Aufruf-Muster

```
/dd:rationality-pass
   → laeuft gegen default Target (externes Memo)

/dd:rationality-pass section 5.3
   → scope auf einzelne Sektion

/dd:rationality-pass report/pitch-teaser.md
   → alternatives Target
```
