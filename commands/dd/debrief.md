---
description: "DD — Call einarbeiten: Transkript ablegen, Namen begradigen, Auswertung, Einschaetzung, Follow-up-Entwurf"
argument-hint: "[Transkript oder Pfad]"
---

# DD — Debrief nach einem Call

Der User hat einen Call gefuehrt und gibt das Transkript (eingefuegt oder als Datei: `$ARGUMENTS`), oft mit ein paar eigenen Saetzen dazu. Diese Saetze sind seine Einschaetzung und stehen in der Auswertung im Wortlaut.

**Verbindliche Methode:** `${CLAUDE_PLUGIN_ROOT}/methoden/call-nachbereitung.md` (Fallback `~/.claude/dd-methoden/call-nachbereitung.md`). Im Active Deal Mode (Pfad D) stattdessen `/dd:ingest`.

## Ablauf

1. **Akte lesen:** `CLAUDE.md`, das Call-Sheet und die Lesarten dieses Calls, `analysis/00-prior.md`, `report/dd-report.md` (Contingency-Liste)
2. **Transkript ablegen** nach Methode §1: Sprecher rekonstruieren, Namen gegen Ablage, CRM, Mail und Kalender pruefen, Korrekturtabelle, offene Punkte als nummerierte Frageliste an den User
3. **Auswertung** `analysis/call-N-auswertung.md` nach Methode §2, in der dortigen Reihenfolge
4. **Spuren** auf Investoren, Vorrunden und Angels sofort als ❗-Zeile im Chat
5. **Akte nachziehen:** betroffene Extraktionsdateien und Report fortschreiben (anhaengen, nicht rueckwirkend glaetten); `CLAUDE.md` nach Methode §3 (Call-Zeile, Status, Conviction und Top-5 ueberschreiben)
6. **Im Chat:** die Einschaetzung in drei bis fuenf Saetzen, dann der Follow-up-Entwurf als Volltext (offene Gate-Fragen als eigener Absatz), dann zugesagte Intros als eigene Entwuerfe. Nichts wird versendet
7. Haken `nach-call` der Haus-Schicht; Check-in mit den naechsten Schritten
