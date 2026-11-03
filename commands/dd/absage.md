---
description: "DD — Absage an Gruender: Kurzform bei fehlendem Fit, Langform mit Begruendungskette, danach Journal und Haus-Schritte"
argument-hint: "[Grund in eigenen Worten]"
---

# DD — Absage

Der User hat entschieden abzusagen. Was er dazu sagt (`$ARGUMENTS` oder im Chat), ist der Grund – nicht neu erfinden, nicht zuspitzen.

**Verbindlicher Standard:** `### Absage-Standard (Pass Letter)` im Methodik-Kern von `${CLAUDE_PLUGIN_ROOT}/commands/dd.md` (Fallback `~/.claude/commands/dd.md`).

## Ablauf

1. **Postfach zuerst:** den Verlauf mit der Gegenseite lesen, auch die gesendeten Mails. Was wir angefragt oder zugesagt haben, steht dort, nicht in der Akte. Sprache und Kanal der letzten Nachricht uebernehmen
2. **Form waehlen:** Kurzform bei fehlendem Fit zu Fokus, These oder Mandat; Langform, wenn eine Begruendungskette traegt. Bei der Langform nur die Entscheidungsfragen stellen, die der Auftrag offen laesst
3. **Entwurf im Chat** als Volltext, mit dem Confidentiality-Gate (gegen `exclusion-rules.md`, falls vorhanden) und einer Zeile, wogegen geprueft wurde. Iterieren, bis der User freigibt
4. **Nach Freigabe:** als Entwurf ablegen (Haken `absage` der Haus-Schicht), nie selbst versenden. Ablage in der Akte, Conviction in `CLAUDE.md` und Report auf PASS mit Datum, Gruenden und Re-Engagement-Trigger
5. **Journaleintrag** nach `### Decision Journal`
6. Haken `entscheidung` der Haus-Schicht (etwa CRM-Status, Umzug in einen Absage-Ordner)
