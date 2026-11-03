# Call-Sheets – vorlesbare Gesprächsleitfäden

Einzige Quelle für jedes Dokument, das im Gespräch vorgelesen wird: Call 1 und Call 2 mit den
Gründern, Gespräche mit Co-Investoren, Advisors, Referenzen und Personen. `dd.md` (Pfad A0
Zeile `6a`, Session 6) und `/dd:call-sheet` verweisen nur hierher.

**Warum es diese Datei gibt:** Die Regeln standen bis v1.24.0 in Session 6, die erst nach der
Deep Analysis drankommt. Call 1 findet aber fast immer vor jedem Data Room statt. Deshalb wurde
der Auftrag für das Call-1-Sheet in einem Quartal rund fünfzehnmal von Hand nachgereicht, immer
mit demselben Wortlaut, und die Einleitungsregel musste dreimal neu verlangt werden.

---

## 0. Vor dem Schreiben

- **Termin prüfen, nicht aus der Akte übernehmen.** Kalender und Mail lesen: Datum, Uhrzeit,
  Zeitzone, gebuchte Länge, Plattform, Gästeliste mit Zusagen. Kalender- und Mailzeiten kommen
  oft in UTC und werden in Ortszeit umgerechnet. Die gebuchte Länge gilt, auch wenn mündlich „eine
  Stunde“ gesagt wurde. Die Akten-`CLAUDE.md` kennt keine Absagen und keinen Wechsel des
  Gesprächspartners. „Stattgefunden“ wird nur mit Beleg eingetragen
- **Kein Termin im Kalender:** das Sheet wird trotzdem gebaut, Kopf „Termin offen“, Pool
  60 Minuten. Sobald ein Termin steht, wird es vorher frisch gezogen: Quellen neu abrufen, Länge
  und Gäste aus dem Kalender übernehmen
- **Verschobener Call:** Website, LinkedIn und Register neu abziehen. Was sich geändert hat, wird
  zur Einleitung einer Frage
- **Mehrere Calls am selben Tag:** Tagesablauf-Tabelle mit Uhrzeiten in den Kopf
- **Vorlesen oder frei sprechen?** Diese Datei regelt das vorlesbare Sheet: ganze, sprechbare
  Sätze. Ein Text, aus dem frei gesprochen wird (Partner-Briefing, Weekly), bekommt Stichpunkte in
  Kategorien und keine ausformulierten Absätze
- **Sprache:** die Sprache der Gründerkommunikation, gemessen an der letzten Nachricht. Ist sie
  offen oder kommt ein weiterer Teilnehmer mit anderer Sprache dazu, gibt es zwei Fassungen
  (`…-en.md`, `…-de.md`). Die Lesarten bleiben in der Arbeitssprache der Akte
- **Zitierbar und nicht zitierbar trennen.** Zitierbar ist, was die Gegenseite selbst
  veröffentlicht oder geschickt hat, dazu Register und öffentliche Meldungen. Nicht zitierbar sind
  DNS, Zertifikatslogs, Wayback-Funde, Profilaggregatoren, private Details und jede vertrauliche
  Quelle (🔒). Begriffe aus 🔒-Quellen stehen in `exclusion-rules.md` im Workspace-Root, schon vor
  jeder Investmententscheidung; das Prüfskript greppt dagegen
- **Erst Unterlagen, dann Technik-Call.** Wird ein technischer Mitgründer vorgestellt und es liegt
  noch nichts vor, zuerst fragen, was vorab geschickt werden kann

## 1. Dateien

- `analysis/ddq-questions-<vorname>[-call-N].md` – vorlesbar
- `analysis/ddq-questions-<vorname>[-call-N]-lesarten.md` – nicht vorlesen, Regie und Deutung
- Bei Obsidian-Stufe ≥ 1 mit Frontmatter `typ: call-prep`, `deal:`, `datum:`, `quelle: dd`

## 2. Aufbau des vorlesbaren Sheets

In dieser Reihenfolge und sonst nichts:

1. `# <Firma> – Call N with <Namen>`
2. **Terminzeile:** Wochentag, Datum, Uhrzeit mit Zeitzone · Plattform · Kalenderslot · Gäste mit Zusage
3. **Minutenzeile:** *„About 60 minutes of questions, answers included: 48 in blocks 1–8, 12 under
   'If there's time left' · Case summary if asked ~2 min (≈ 270 words), on top“*
4. Tagesablauf-Tabelle, nur bei mehreren Calls am Tag
5. **`## If asked: how I read the case`** – Standard für Call 1. Gibt die Selbstdarstellung der
   Firma wieder (Deck, Website, Nachricht) in der Folge Positionierung, Problem, Produkt, Ergebnis,
   erster Markt, Team, Plan und Runde. Keine Wertung, keine eigene Marktsicht, und nichts, was die
   Antwort einer späteren Frage vorwegnimmt – vor allem nicht die Gap-Frage. Herkunft in erster
   Person („as I read it on slide 2“). 200–300 Wörter. Genutzt wird sie nur, wenn die Gegenseite
   fragt; sie zählt nicht zum Fragenbudget und endet mit ihrem letzten Inhaltssatz, ohne
   Übergabesatz
   - Eine **Sicht-Passage** (unsere Sicht auf Markt und Technologie, wo wir zustimmen, was wir
     beobachten) gibt es nur auf ausdrücklichen Wunsch. Dann steht sie ebenfalls außerhalb des
     Budgets, kündigt sich nicht an („Let me tell you how we see …“) und beginnt mit dem Befund selbst
6. Blöcke `## N. <Thema> (~M min)` mit den Fragen
7. `## If there's time left (~M min)`
8. `## Numbers to hand` – Tabelle `Topic | Number | Source`, die einzige Stelle für Ziffern

## 3. Blockgerüst Call 1

Call 1 soll klären, ob der Case für uns interessant ist, Sinn ergibt und attraktiv ist. Deshalb
Substanz zuerst, Runde und Prüffragen zuletzt.

| # | Block | Was er klärt |
|---|---|---|
| 1 | **The gap** | Welche Lücke sie gesehen haben und woher – erlebt oder abgeleitet |
| 2 | **The product (today)** | Was es heute tut, wer es benutzt, was gebaut und was geplant ist |
| 3 | **Technology and integration** | Worauf es aufbaut, wie es beim Kunden integriert wird, was eigene Technik und was Baseline ist, ob vor dem Umsatz eine Lizenz oder Zulassung nötig ist. Fragen nach Kompetenz im Team, die an der Technik hängen, gehören hierher und nicht in einen Teamblock. Ist der CTO im Call, kommt hier die Tiefe hin |
| 4 | **Who wants this** | Wer zahlt, aus welchem Budget, welcher ökonomische Mehrwert sich in einer Zahl zeigt, die der Kunde selbst misst, warum dieser Markt zuerst, wie sie hineinkommen, wer die ersten Kunden sind |
| 5 | **Pricing** | Abrechnungseinheit, Preis, Bezugsgröße. Immer ein zweites Mal fragen |
| 6 | **Who else builds this** | Zuerst ohne Namen („How do you draw the map?“), dann Startups und Scale-ups, Plattformen und Incumbents („Why doesn't X just build it?“), andere Technologien, Übernehmer („Which of them needs this most?“), und was mit jedem Kunden schwerer zu kopieren wird |
| 7 | **Rollout and vision** | Ausrollen, nächste Produkte, die große Version (was darauf aufbaut, wie die Verträge wachsen), warum jetzt. Daran entscheidet sich, ob der Fall groß werden kann oder eine solide Position bleibt |
| 8 | **Company and round** | Einzeiler: Gesellschaft, Runde, Lead, Instrument, wer schon dabei ist. Geschlossene Prüffragen zu Werdegang und IP stehen hier |

Regeln für die Auswahl:

- **Hauptfragen offen.** Die Herkunft steht in einem Satz, ohne die Antwort mitzuliefern. Unsere
  Befunde – Wettbewerber, Preise, frühere Arbeitgeber, einzelne Website-Funktionen – stehen als
  vorformulierte Nachfragen darunter. Ein Sheet, dessen Hauptfragen aus der Recherche starten,
  ist ein Prüf-Sheet und lenkt jede Antwort
- **Den Werdegang früh nur offen fragen**, als Nachfasser zur Gründungsgeschichte („What did you do
  before?“). Die geschlossene Prüffrage gehört in Block 8
- **Kleinprüfungen nicht in Call 1:** Lebenslaufdaten, Förderfähigkeit, Grants, Konsortialrechte,
  Formalia. Sie stehen in den Lesarten unter „Schriftlich im Follow-up oder in Call 2“
- **Gate-Fragen in Call 1 hinten, aber abgesichert:** eine Uhrzeit-Marke in den Lesarten, ab der
  Block 8 als Einzeiler drankommt, auch mitten in einem anderen Block. Fragen die Gründer nach
  den nächsten Schritten, ist das die letzte sichere Stelle. Was offen bleibt, geht im Follow-up
  schriftlich raus, als eigener Absatz. **Hat die Gegenseite schon einmal vorzeitig aufgelegt,
  oder ab Call 2, stehen die Gate-Fragen vorn**
- **Keine Standard-VC-Fragen** („What's your moat?“, „How big is the TAM?“). Die brauchbaren
  Formen stehen in `kommerzielle-pruefung.md` („Die Fragen für den Call“) und in den Kohärenz-Checks
  in `dd.md`: „Isn't that just a feature?“, „What does this look like in a year?“, „Why doesn't the
  category leader do it?“
- **Klingt nach einem Investor, der sich eingelesen hat** und Technik versteht, nicht nach
  vorgeführter Klugheit: keine gestapelten Fachbegriffe, keine Fangfragen
- **Vergleiche treffen die richtige Nachbarschaft.** Ein Präzedenzfall aus einer Nachbarkategorie
  nur mit ausgesprochener Kette, warum er übertragbar ist
- **Vermutung und eigener Schluss als geschlossene Frage**, nicht als Feststellung: „Is that the
  same one?“ statt „ich kann von außen nicht erkennen, ob …“. Einem Gründer hinzuschreiben, was
  sein Geschäft ist, wirkt belehrend; als Frage lässt es ihm Zustimmung, Widerspruch oder
  Korrektur, und jede davon ist ein Datenpunkt
- **Statusworte zerlegen.** „Secured“, „agreed“, „committed“ werden nicht übernommen, sondern in
  Stufe, fehlenden Unterschriftsschritt und Bedingung zerlegt

## 4. Blockgerüst Call 2 und folgende

1. **Offene Gate-Fragen** (Runde, Bewertung, Instrument, Lead, Cap Table)
2. **Technik-Vertiefung**, wenn der technische Gesprächspartner dabei ist, auf Wunsch zuerst
3. **Anspruch gegen Beleg:** eigene Behauptungen und die der Wettbewerber nebeneinander (*„X says it
   already corrects this automatically. Where do you differ?“*), und ob es Schmerz oder
   Nice-to-have ist (*„Are customers running down your door?“*)
4. Was aus Call 1 und den Unterlagen offen ist, abgeleitet aus der Contingency-Liste des Reports
5. **Reine Auskunftsfragen gehören nicht ins Sheet.** Zahlen, Dokumente und Formalia gehen per
   Mail vor oder nach dem Call. Der Call bleibt für das, was Erklärung braucht

## 5. Andere Gesprächspartner

- **Co-Investor, Advisor, Board:** ihre DD-Erkenntnisse, Deal-Struktur, Marktsicht. Besonders
  ergiebig: warum sie einen vergleichbaren Fall nicht gemacht haben
- **Referenz-Call:** Nutzung, Kaufentscheidung, Budget, Alternativen, was fehlt. Protokolle für den
  Umlauf nach `call-nachbereitung.md`
- **Personen-Gespräch:** Werdegang · was jetzt · Thema ·
  wie wir helfen können

## 6. Frage-Format

**Einleitung → Frage → Anschlussfragen.** Die Einleitung hat drei Teile und sonst nichts:

- **Herkunft in der ersten Person** – woher wir es haben, gesprochen als eigene Handlung: „I read on
  your website…“, „I went through your deck…“, „On slide 9 I saw…“, „I checked Companies House…“,
  „On our first call you said…“, „You wrote to me…“. **Das Dokument ist nie Subjekt.** „Slide 6
  says…“, „Your deck says…“, „Companies House lists…“ klingen nach Aktenvortrag; die Gegenseite soll
  hören, dass hier jemand gelesen hat. Ein „So“ vor der fetten Frage ist eine natürliche Brücke
- **Fakt** – was dort steht, in einem Satz
- **Schluss** – was daraus folgt oder wo es sich mit etwas anderem reibt

Dann die Frage, fett, am Ende klar erkennbar. Das Homework zeigt sich in der Herkunft von selbst;
kein Satz darüber. Format je Frage: `**N.M** <Einleitung> **<Frage>?**`, darunter zwei bis vier
Anschlussfragen als Stichpunkte.

**Verboten im vorlesbaren Sheet:** Metasätze über das Gespräch · Kommentare zu den eigenen Fragen
(„keine Frage kommt aus dem Nichts“, „ich will dich nicht überführen“, „als Freund der These“) ·
Höflichkeitsvorspann („kurz, warum das bei uns gelandet ist“, „stop me wherever I've got something
wrong“) · Beteuerungen („ehrlich gesagt“, „honestly“, „for what it's worth“, „ich frage nur“) ·
Übergabesätze („That's our view going in. Now I'd like yours.“). Eine Sorge wird benannt, nicht
angekündigt: *„A and B already ship this. Why would an operator switch to you?“* statt *„jetzt
muss ich eine kritische Frage stellen“*.

Widersprüche benennen, aber ohne Vorwurfston („maybe we're missing something – help us place
this“). Ausnahme: Beobachtungsfragen (etwa zur Team-Dynamik) neutral-wohlwollend einleiten, den
Testcharakter nicht verraten.

## 7. Satzregeln für jeden vorlesbaren Satz

- so, wie ein Mensch spricht, ohne eingeschobene Nebensätze; lieber zwei kurze Sätze
  (höchstens 25 Wörter, Median 12–14). Zu kurz (Median 7) klingt abgehackt
- kein Gedankenstrich, kein Semikolon
- Beträge in Worten („about fifty thousand pounds a year“), Ziffern nur in „Numbers to hand“
- keine Pronomen für Dritte, deren Pronomen nicht bekannt sind; stattdessen den Namen wiederholen
- jede fette Frage hat eine Einleitung, **auch unter „If there's time left“ und in der Runde**
- eine Anschlussfrage mit neuem Gegenstand wird Hauptfrage mit eigener Einleitung; Stichpunkte
  bleiben für Nachfragen zum selben Gegenstand

## 8. Umfang und Minuten

Das Sheet ist ein **Fragenpool**, aus dem im Gespräch gewählt wird. Die Fragen allein tragen die
Slotlänge, **die Antworten der Gegenseite eingerechnet**. Die Fallzusammenfassung steht im Sheet,
zählt aber nicht mit; im Kopf wird sie separat ausgewiesen und in Wörtern gemessen (~140 W/Min).

- Blockminuten nach Zahl und Tiefe der Fragen schätzen, nicht von der Slotlänge herunterteilen.
  Eine Frage, auf die erzählt oder erklärt wird, braucht 3–5 Minuten, eine Zahl oder ein Ja/Nein
  1–2. Augenmaß reicht
- Was über die Slotlänge hinausgeht, steht unter „If there's time left“. Nicht stauchen
- Gebucht 45 Minuten, gesagt „eine Stunde“: 45 in den Blöcken, 15 unter „If there's time left“
- Keine Zeitnot-Kaskade im Sheet („bei Zeitnot nur Block 3 …“). Wer den Call führt, entscheidet
  im Gespräch, welche Fragen fallen
- Vorlesbare Passagen über 800 Wörter werden zweistufig: ein Kern zum Vorlesen und „Vertiefung auf
  Rückfrage“. Nicht kürzen

*Warum:* In einem Robotik-Fall (10/2026) waren 45 Minuten von oben auf zehn Blöcke verteilt, das
Opening eingerechnet. Darin lagen 22 Hauptfragen und 36 Nachfragen, also rund 1,8 Minuten je
Hauptfrage samt Antwort. Die Minuten waren Verteilung, keine Schätzung.

## 9. Gesprächstechnik (in die Fragen einbauen)

- **Bezugsgröße nachfragen statt Zahl stehenlassen** – „is that five million on top, or five million
  in total?“. Gilt besonders für ACVs: „per year and customer, or over the contract?“ Ein ACV ohne
  Bezugsgröße ist keine Zahl
- **Bei Ausweichen ein zweites Mal fragen** – die Anschlussfrage vorformuliert ins Sheet, damit sie
  im Moment nicht erfunden werden muss. Grundsätzlich bei Preis, ICP, Rundenmechanik und Kundennamen
- **Sorge offen benennen statt ankündigen** – wie die Vorbild-Formulierung einer erfahrenen
  Investorin: *„I would really drill down on that if I were you“* nennt die Sorge und gibt eine
  Empfehlung
- **Mit Empfehlung schließen statt mit Urteil** – „in your shoes I'd dig deeper there“ ist für die
  Gegenseite verwertbar, ein Urteil nicht
- **Eigene Fonds-Restriktionen offenlegen, nicht verstecken** – sie machen aus einem Urteil über die
  Firma eine nachprüfbare Aussage über uns
- **Die Frageformen der kommerziellen Prüfung übernehmen** statt sie neu zu erfinden:
  `kommerzielle-pruefung.md`, Abschnitt „Die Fragen für den Call“

## 10. Die Lesarten-Datei

`# Lesarten zu Call N – <Firma>`, dann:

1. **Gehört-zu-Zeile** mit Links auf Sheet, Prior, Report, Primer, Research-Notes und dem Satz
   „Nicht vorlesen; nach dem Call Gerüst für die Auswertung“
2. **Ein Absatz zur Anlage** der Fassung: worauf das Sheet zielt, was in dieser Fassung neu ist
3. **`## Vorab`:** Länge laut Kalender · **Uhrzeit-Marke** für den Rundenblock · die
   Fallzusammenfassung gilt nur auf Frage · 🔒 nicht andeuten · nicht zitieren / zitierbar ·
   Gästeliste kurz vorher neu lesen · wer spricht und wer gezielt angesprochen wird · bei Preis
   und Beachhead zweimal fragen
4. `## Reserve, falls nur einer kommt`, wenn mehrere eingeladen sind
5. **Je Block** `## N. <Thema>` mit einer Tabelle `| Antwort | Lesart |`: was welche Antwort
   bedeutet, Abbruchschwellen, welche Hypothese aus dem Prior sie trifft
6. `## Schriftlich im Follow-up oder in Call 2`
7. `## Nach dem Call`: Hypothesen prüfen, Conviction überschreiben, `/dd:debrief`, Haus-Haken
   „nach Call“

## 11. Prüfung vor Abgabe (Pflicht, auch bei jeder Fortschreibung)

```bash
python3 -I ${CLAUDE_PLUGIN_ROOT}/scripts/check-call-sheet.py <sheet.md> [--exclusions exclusion-rules.md] [--call 1]
# Fallback: python3 -I ~/.claude/dd-scripts/check-call-sheet.py …
```

Das Skript prüft die Form: Herkunftsmarker vor jeder fetten Frage, Dokument als Subjekt,
Satzlänge, Gedankenstrich und Semikolon, Ziffernbeträge außerhalb „Numbers to hand“, Pronomen für
Dritte, Verbotsliste, 🔒-Begriffe, bei `--call 1` die Pflichtabschnitte. **Treffer werden behoben,
nicht begründet.**

Was kein Skript prüft und vor Abgabe selbst geprüft wird: Opening ist die Fallzusammenfassung und
nimmt keine Antwort vorweg · Blöcke in der Reihenfolge aus §3 · Block 4 und Block 6 vorhanden,
Block 6 mit Übernehmern · Hauptfragen offen, Recherche in den Nachfragen · Sprache passt zur
letzten Nachricht der Gegenseite.
