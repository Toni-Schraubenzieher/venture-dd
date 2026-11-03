---
description: "DD — Partner-Memo: neutraler, vollstaendiger Stand des Falls fuer einen Partner oder ein Gremium, das ihn noch nicht kennt"
argument-hint: "[Empfaenger]"
---

# DD — Partner-Memo

Empfaenger: `$ARGUMENTS` (fehlt er, ist es der Partner, der den Fall noch nicht kennt).

**Verbindlicher Standard:** `### Partner-Memo` im Methodik-Kern von `${CLAUDE_PLUGIN_ROOT}/commands/dd.md` (Fallback `~/.claude/commands/dd.md`), dazu `### Sprache in Dokumenten, die das Haus verlassen`.

## Ablauf

1. **Alles lesen, was die Akte hat:** Quellen, Extraktion, Analysen, Report, alle Call-Transkripte und Auswertungen, Mails. Das Memo gibt den vollstaendigen Stand wieder, nicht den Report in kurz
2. **Gliederung:** abholen (worum es geht, warum der Fall auf dem Tisch liegt) → verstehen (was sie bauen, fuer wen, wie, mit wem) → Details nach Bereichen, jede Aussage mit Quelle als Fussnote
3. **Neutral halten:** keine Conviction-Zahl, keine Empfehlung, kein Vergleich mit anderen Faellen des Fonds, kein Bewertungs-Benchmark. Vor der Ausgabe danach greppen
4. **Vertrauliches pruefen:** gegen `exclusion-rules.md`, falls vorhanden; 🔒-Quellen nur so, wie es die Akte erlaubt
5. Ausgabe `report/memo-<empfaenger>-DATUM.md`; Format, Vorlage und Begleitmail nach Haken `memo` der Haus-Schicht. Die Begleitmail als Volltext im Chat, nichts wird versendet
6. Zeile in der Workflow-Tabelle der `CLAUDE.md`
