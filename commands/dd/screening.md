---
description: "DD — Listen-Screening: viele One-Pager oder eine Event-Liste vorsortieren, A-Liste mit Begruendung, Gesamtliste als Notiz"
argument-hint: "[Ordner oder Datei]"
---

# DD — Listen-Screening

Eine Liste vorsortieren: `$ARGUMENTS` (Ordner mit One-Pagern, PDF-Tabelle mit Links, Event-Export). Fehlt das Argument, den aktuellen Ordner nehmen.

**Verbindliche Methode:** `${CLAUDE_PLUGIN_ROOT}/methoden/auftragsarten.md`, Abschnitt 4 (Fallback `~/.claude/dd-methoden/auftragsarten.md`). Recherche-Griffe aus `outside-in-recherche.md`.

## Ablauf

1. **Haus-Schicht lesen:** Haken `fondsparameter` (Ticket, Bewertungsrahmen, Thesen) und ein hauseigenes Screening-Raster, falls genannt
2. **Liste erfassen:** alle Firmen mit Name, Kurzbeschreibung, Land, Runde, Links (auch Link-Annotationen in PDFs). Anzahl melden
3. **Je Firma** Website und ein, zwei Primaerquellen; Gruenderprofil mit Quelle; Urteil A/B/C mit Grund. Portfolio-Ueberschneidung nur als Info-Zeile
4. **Bei vielen Firmen** in Pakete aufteilen und parallel pruefen; die Breitensuche nur einem Agent geben (WebSearch-Budget der Session)
5. **Im Chat:** die A-Liste mit je einem Satz, warum, danach B mit der fehlenden Tatsache
6. **Notiz** `screening-DATUM.md` im Ordner der Liste: Gesamttabelle mit Urteil, Grund, Quelle je Firma
7. Auf Wunsch fuer einzelne A-Firmen direkt `/dd` mit dem Material starten (Pfad A0)
