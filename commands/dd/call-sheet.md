---
description: "DD — Call-Sheet bauen oder fortschreiben (Call 1, Call 2, Co-Investor, Referenz, Person), mit Lesarten und Pruefskript"
argument-hint: "[1|2|N] [Vorname] [de|en|beide]"
---

# DD — Call-Sheet

Baut oder schreibt ein vorlesbares Call-Sheet fort. Argumente: `$ARGUMENTS` (Call-Nummer, Gespraechspartner, Sprache). Fehlt etwas, aus Akte, Kalender und letzter Nachricht ableiten statt fragen.

**Verbindliche Methode:** `${CLAUDE_PLUGIN_ROOT}/methoden/call-sheet.md` (Fallback `~/.claude/dd-methoden/call-sheet.md`). Vor dem Schreiben vollstaendig lesen.

## Ablauf

1. **Akte lesen:** `CLAUDE.md`, `analysis/00-prior.md`, `report/dd-report.md` bzw. `report/case-briefing.md`, `analysis/themen-primer.md`, `analysis/research-notes.md`, vorige Call-Auswertungen, ein vorhandenes Sheet zu diesem Call (dann fortschreiben, nicht neu anlegen)
2. **Termin pruefen** nach `call-sheet.md` §0: Kalender und Mail, gebuchte Laenge, Gaeste, Zeitzone. Kein Termin → „Termin offen“, 60-Minuten-Pool. Verschoben → Quellen neu abziehen
3. **Sprache** nach der letzten Nachricht der Gegenseite; offen oder weiterer Teilnehmer → beide Fassungen
4. **Sheet** nach `call-sheet.md` §2–§9: Call 1 mit „If asked: how I read the case“ und dem Blockgeruest §3; Call 2 und folgende nach §4; andere Gespraechspartner nach §5
5. **Lesarten-Datei** nach §10
6. **Pruefskript** laufen lassen, Treffer beheben, erneut laufen lassen:
   ```bash
   python3 -I ${CLAUDE_PLUGIN_ROOT}/scripts/check-call-sheet.py analysis/ddq-questions-<name>.md --call 1 --exclusions exclusion-rules.md
   # Fallback: python3 -I ~/.claude/dd-scripts/check-call-sheet.py …
   ```
   `--exclusions` nur, wenn die Datei existiert; `--call 1` nur fuer Call 1
7. Die inhaltliche Checkliste aus §11 selbst pruefen
8. `CLAUDE.md`: Zeile `6a` (bzw. Call N) auf ERLEDIGT, Termin in den Startup-Kontext. Haken `vor-call` der Haus-Schicht
9. **Check-in:** Minutenzeile, Zahl der Fragen je Block, was bewusst in „If there's time left“ oder ins schriftliche Follow-up gewandert ist, Ergebnis des Pruefskripts
