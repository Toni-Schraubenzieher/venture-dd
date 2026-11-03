---
description: "DD Active Deal — Input-Triage fuer neu eingehende Materialien (Email/Call/WhatsApp/Confidential-Forward)"
---

# DD Active Deal — Input Ingest

Du bist im **Active-Deal-Modus**: der Intake-DD ist abgeschlossen, der Fonds hat zu investieren entschieden, und der Deal läuft aktiv. Ein neuer Input ist eingegangen (Email, Meeting-Call, WhatsApp-Thread, Customer-Korrespondenz, Investor-Korrespondenz, weitergeleitetes vertrauliches Material). Deine Aufgabe: diesen Input **triagieren und sauber ins Workspace propagieren**, ohne Exclusion-Regeln und Confidentiality-Grenzen zu verletzen.

**Sprache:** Deutsch für interne Files (Meeting-Notes, Memory, Internal-Report). Englisch für externes Investor-Memo.

**Referenzen, die geladen werden:**
- `${CLAUDE_PLUGIN_ROOT}/methoden/taxonomies.md` (Fallback `~/.claude/dd-methoden/taxonomies.md`) (Pilot-Stage, Team-Status, Evidence-Level usw.)
- `${CLAUDE_PLUGIN_ROOT}/methoden/rationality-audit.md` (Fallback `~/.claude/dd-methoden/rationality-audit.md`) (Hidden-Risk-Check, Exclusion-Check)
- Workspace-lokale `exclusion-rules.md` (falls vorhanden)
- Workspace-lokale Memory-Datei (`~/.claude/projects/*/memory/project_<deal>_round.md`)

---

## Phase 0: Bootstrap-Check (Erster-Lauf-Erkennung)

Prüfe ob der Workspace bereits Active-Deal-Struktur hat:

```
02_meetings/              # Meeting-Notes-Ordner
exclusion-rules.md        # Per-Projekt Exclusion-Liste
report/internal/          # Interner DD-Report-Folder
```

**Falls 02_meetings/ fehlt:** Erster Lauf. Bootstrap durchführen:
1. `02_meetings/` anlegen
2. `exclusion-rules.md` im Workspace-Root anlegen mit Template-Inhalt. **Existiert sie schon** (seit /dd v1.25.0 entsteht sie bei der ersten vertraulichen Quelle, auch vor der Entscheidung), bleibt ihr Inhalt stehen und nur der Kopf unten wird ergaenzt:
   ```markdown
   # Exclusion Rules (External Memo Build Blocker)

   Diese Terms duerfen NICHT im externen Investor-Memo (report/*-for-investors.md) vorkommen.
   Der build-docx.py-Hook greppt vor jedem Build und blockiert bei Treffern.
   Override nur mit `--override --reason "<text>"` und dokumentierter Begruendung.

   # Format: Ein Term pro Zeile, Kommentare mit #

   # Beispiel:
   # <Co-Investor>
   # <co-investor>
   ```
3. User fragen: *"Es gibt noch keine Exclusion-Regeln in diesem Workspace. Welche Namen / Entities duerfen NICHT im externen Investor-Memo auftauchen? (z.B. Co-Investor-Namen waehrend Pitch, NDA-Personen)"*. User-Antworten in `exclusion-rules.md` einpflegen.
4. Wenn `report/build-docx.py` existiert: Exclusion-Hook-Pattern einbauen (siehe `${CLAUDE_PLUGIN_ROOT}/templates/exclusion-hook-snippet.py`, Fallback `~/.claude/dd-templates/exclusion-hook-snippet.py`).

**Falls alles vorhanden:** Weiter zu Phase 1.

---

## Phase 1: Input-Typ-Identifikation

Frage den User (oder erkenne aus Kontext):

> Welcher Input wird gerade triagiert?
> 1. **Email (weitergeleitet vom Founder / Co-Investor / Kunde)**
> 2. **Meeting-Notes (Call- / Video-Call-Protokoll)**
> 3. **WhatsApp-Thread**
> 4. **Customer-Korrespondenz (direkt vom Kunden)**
> 5. **Investor-Korrespondenz (Co-Investor / Pipeline-Investor)**
> 6. **Confidential Forward (NDA-sensitive)**
> 7. **Sonstiges (bitte beschreiben)**

Je nach Typ gelten leicht unterschiedliche File-Templates (s. Phase 3).

---

## Phase 2: Klassifikations-Frage (AskUserQuestion)

Frage via `AskUserQuestion`, welche Klassifikation der Input traegt:

- **Internal** — Nur intern nutzbar, keine externen Bezuege
- **Internal — NDA-only** — Vertraulich, nur intern, kein externer Bezug ohne NDA
- **External-referenceable (dezent, ohne Namen)** — Externe Referenz moeglich, aber anonymisiert
- **External-full-text-shareable** — Volltext kann extern verwendet werden

Die Klassifikation bestimmt die **Usage-Matrix** im File-Header und ob der Input in Phase 4 ins externe Memo flieszen darf.

---

## Phase 3: File-Erstellung in `02_meetings/`

Erzeuge eine neue Datei: `02_meetings/YYYY-MM-DD_<slug-topic>.md`

**Naming-Konvention:**
- Datum im ISO-Format (aus dem Input-Datum, nicht heute)
- Slug aus Teilnehmern + Topic, kurz und sprechend (z.B. `2026-04-10_<name>-<fonds>-feedback-call`, `2026-04-17_<behoerde>-<name>-email`)

**Template-Struktur** (deutsch, angepasst an Input-Typ):

```markdown
# [Title: Sprechend — z.B. "Meeting Notes: <Name> (<Fonds>) - <Deal> Tech-Expert Feedback"]

| Feld | Wert |
|---|---|
| Datum | [YYYY-MM-DD, ggf. + Uhrzeit] |
| Teilnehmer | [Namen + Rolle, je Seite] |
| Kanal | [Email / WhatsApp / Video Call / In-Person / etc.] |
| Klassifikation | [aus Phase 2] |
| Kontext | [1 Satz: warum ist dieser Input relevant?] |

---

## Zusammenfassung
[3-5 Zeilen: die zentrale Aussage, die aus dem Input entsteht]

## Detaillierte Inhalte
[Volltext-Uebernahme bei Emails / WhatsApp. Bei Meetings: strukturierte Notizen nach Gespraechs-Abschnitten.]

## Interpretations-Block (fuer den internen Gebrauch)
[Was folgt daraus? Welche Claims / Risiken / Evidenz-Punkte veraendern sich? Welche Framing-Entscheidungen stehen an?]

## Verwendung (Usage Matrix)
| Zweck | Erlaubt? |
|---|---|
| Internes Memory updaten | [Ja/Nein] |
| Internal DD-Report erweitern | [Ja/Nein, inkl. Name-Nennung?] |
| Investor-facing Memo (externe Version) referenzieren | [Nein / Dezent ohne Namen / Volltext / nur mit NDA] |
| Spezifische Investoren muendlich erwaehnen | [Ja/Nein, bei wem?] |
| Volltext shareable | [Nein / Nur nach NDA / Ja] |

## Related Files
[Cross-Links zu vorherigen Meeting-Notes, Memo-Abschnitten, internem Report]
```

**Wichtig:**
- Bei NDA-only-Klassifikation: auffaelliger Warning-Block oben (`🔒 CONFIDENTIAL — NDA-only`)
- Bei externen Email-Forwards: Original-Absender-Block vor dem Interpretations-Block, Forwarding-Kontext separat

---

## Phase 4: Propagations-Entscheidungsbaum

Nachdem die Meeting-Note geschrieben ist, arbeite diesen Baum ab. Jeder Zweig kann unabhaengig greifen.

### 4.1 Memory-File-Update

Pruefe: hat sich einer der folgenden Zustaende geaendert?

- **Round-Construction:** Neue Ticket-Groesse / neuer Investor-Status / Term-Sheet-Status
- **Pilot-Status:** Neuer Pilot / Stage-Wechsel / neuer Kunde
- **Team:** Neuer Hire / geaenderte Rolle / ausgeschiedene Person
- **Entity-Struktur:** Incorporation-Fortschritt / IP-Assignment-Status
- **Legal Warnings:** Neue Flags (CLA-Risiko, Regulatorisches, Compliance)

Falls ja: Memory-File gezielt updaten (keine pauschale Neufassung — `Edit`-Operations auf relevante Sektionen). Date-Stamp im Header aktualisieren ("Status as of YYYY-MM-DD").

### 4.2 Internal-DD-Report-Update

Pruefe: gibt es neue Datenpunkte, die den internen Report erweitern?

- **Neue Risiken** oder neue Facetten bestehender Risiken → Top-5-Risiko-Tabelle und/oder entsprechender Abschnitt
- **Mitigations-Updates** fuer bestehende Risiken (z.B. Schreiben von externer Autoritaet, das Risiko partiell entschaerft)
- **Externer Expert-Input** (positiv ODER negativ) → eigener "Update [Datum] — Externer Input"-Abschnitt, symmetrische Darstellung (Positiv-Validierung + Push-Back + Gegenantworten)

### 4.3 External-Memo-Update

**Check 1 (Gate):** Ist die Klassifikation mindestens "External-referenceable"? Falls "Internal" oder "Internal — NDA-only" → ueberspringen. Memory und Internal-Report sind die Ende-Stationen.

**Check 2 (Framing-Entscheidung):** Wenn Input externalisiert werden soll, **welche Sektionen sind betroffen?**

| Input-Inhalt | Typischerweise betroffene Sektionen |
|---|---|
| Neuer Kunde / Pilot-Stage-Wechsel | 5.3 Active Pilots, 5.4 Defense Validation, 7.3 Defense Sales, 9 Milestones |
| Neue Expert-Validierung | 5.2 Third-Party Reviews |
| Neue Regulatorische / Markt-Info | 3.2 Regulatory Pressure, 6 Market & Competitive |
| Team-Veraenderung | 1 Exec Summary (Team-Tabelle), 2.3 Team Expansion, 2.4 Advisory Board |
| Entity / Legal | 2.1 Corporate Structure, 4.5 Open Technical Questions (IP-Assignment) |

**Check 3 (AskUserQuestion fuer Judgment-Calls):** Bei jeder sensitiven Framing-Frage muss der User entscheiden — nicht der Assistant. Beispiele:

- Soll ein confidential-forward Inhalt (z.B. Name eines Generals) namentlich oder dezent ("Senior Authority, available on request under NDA") externalisiert werden?
- Soll eine operational-dependency-Aussage (z.B. Kapazitaets-Grenze) ueberhaupt ins externe Memo?
- Soll ein externer Expert-Einwand als explizites Risiko in Section 4.5 oder dezent in 5.2/5.3 eingebettet werden?

Formuliere die Fragen mit 2–3 Optionen je Frage, jeweils mit Description der Trade-Offs.

**Check 4 (Edit-Durchfuehrung):** Edits gezielt per `Edit`-Tool. Kein Memo-Rewrite.

### 4.4 Taxonomie-Anwendung

Beim Schreiben neuer Memo-Passagen: `taxonomies.md` beachten.
- Neue Pilots → Pilot-Stage explizit benennen
- Neue Reviews → Evidence-Level explizit benennen
- Neue Team-Rollen → Team-Status-Taxonomie strikt anwenden

### 4.5 Memo-Rebuild + Exclusion-Check

Falls externes Memo editiert wurde:
1. Exclusion-Preflight: `exclusion-rules.md` lesen, Source-Markdown greppen, bei Treffern **stopp** und User informieren.
2. `python3 report/build-docx.py` ausfuehren.
3. Bei Erfolg: Bestaetigung + Pfad zum neuen .docx.

---

## Phase 5: Completion-Checklist

Vor Abschluss dem User zurueckmelden:

```
Triage-Report fuer [Input]:

✓ File erstellt: 02_meetings/YYYY-MM-DD_<topic>.md
✓ Klassifikation: [X]
[+/–] Memory-File aktualisiert: [ja, Sektion X / nein]
[+/–] Internal-DD-Report aktualisiert: [ja, Abschnitt X / nein]
[+/–] External-Memo aktualisiert: [ja, Sektionen X, Y / nein, weil intern]
[+/–] Exclusion-Check: [gruen / rot bei Term X]
[+/–] Memo rebuild: [erfolgreich / skipped]

Offene Folge-Entscheidungen fuer User:
- [...]
```

---

## Anti-Patterns (nicht tun)

- **Kein Memo-Update ohne Klassifikations-Check.** NDA-only-Material darf nicht versehentlich extern landen.
- **Kein automatischer Edit bei Judgment-Calls.** Sensitive Framings muessen per `AskUserQuestion` bestaetigt werden.
- **Kein Memory-Rewrite.** Gezielte `Edit`-Operations, nie den Volltext neu schreiben.
- **Keine Plural-Formen ohne Count** beim Memo-Update. Siehe `rationality-audit.md` §2.
- **Keine Superlative ohne Evidenz** bei neuen Memo-Passagen. Siehe `rationality-audit.md` §1.
- **Nie den Exclusion-Hook mit `--override` benutzen, ohne dass der User den Grund explizit freigegeben hat.**

---

## Was am Ende einheitlich ist

Egal welcher Input-Typ: es gibt genau **einen** Meeting-Note-File in `02_meetings/` als primaeres Artefakt pro Input. Alle weiteren Propagationen (Memory, Internal-Report, External-Memo) referenzieren diese Datei. So bleibt der Audit-Trail intakt und jede spaetere Session kann rekonstruieren, wo eine Information herkam.
