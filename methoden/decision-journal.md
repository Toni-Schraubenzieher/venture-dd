# Decision Journal — Entscheidungen mit Prognose festhalten

Diese Datei definiert das Format und die Disziplin des Decision Journals. Ein Eintrag entsteht bei **jeder** Entscheidung über einen Deal — Absage, Investment, Watch, Not-now.

**Ablage:** `~/.claude/dd-journal/<deal>.md`, eine Datei je Deal, **append-only**.

---

## Warum das existiert

Belastbare Intuition entsteht nur über Sample Size — und Sample Size entsteht nur, wenn die Entscheidung **zum Zeitpunkt der Entscheidung** festgehalten wird, inklusive dessen, was man damals erwartet hat.

Der Anlass ist konkret: Bei der ersten retrospektiven Auswertung abgeschlossener DDs musste der Prior je Deal nachträglich aus dem Pitch-Material rekonstruiert werden, weil zum Entscheidungszeitpunkt keiner festgehalten worden war. Das war aufwendig, methodisch angreifbar und ist **jedes Mal verlorene Stichprobe**, wenn es unterbleibt.

VC ist eine Umgebung mit sehr langsamem und sehr uneindeutigem Feedback. Genau dort wird Intuition ohne schriftliche Vorab-Prognose systematisch überschätzt — man erinnert sich an das, was man am Ende gedacht hat, nicht an das, was man am Anfang dachte. Der Journaleintrag ist die einzige Gegenmaßnahme.

---

## Harte Regeln

1. **Append-only.** Ältere Einträge werden nie überschrieben. Ändert sich die Einschätzung, entsteht ein **neuer** Eintrag mit Datum und Verweis auf den vorigen.
2. **Die Prognose wird vor dem Outcome geschrieben** und danach nicht angefasst. Ein Eintrag ohne falsifizierbare Prognose ist nicht auswertbar.
3. **Die Journaldateien bleiben lokal.** Sie enthalten Entscheidungen, Conviction-Werte und Fonds-Restriktionen. Sie gehen **nie** in ein Repository, nie in ein externes Memo, nie an einen Gründer.
4. **Das Outcome-Feld wird beim Review ausgefüllt, nicht vorher.** Wer es beim Anlegen füllt, hat die Prognose nachträglich angepasst.
5. **Kein Scoring.** Der Journal bewertet Deals nicht und rangiert sie nicht. Er hält fest, was entschieden wurde und woraufhin.

---

## Wann ein Eintrag entsteht

| Anlass | Wo im Workflow |
|---|---|
| Absage | Pfad C Option A — direkt nach dem Pass Letter |
| Investment-Memo für IC/Partner | Pfad C Option B — mit dem Memo |
| Übergang in den Active-Deal-Modus | Pfad C Option E |
| Entscheidung aus dem Active Deal heraus | Pfad D, bei Absage oder Commitment |
| Review-Datum eines bestehenden Eintrags erreicht | eigenständig, ohne Anlass im Workflow |

Der **Absage-Standard** erzeugt Endgültigkeit, Schärfe, Begründungs-Ketten aus den Top-5-Risiken und einen konkreten Re-Engagement-Trigger bereits als Pflichtfelder. Der Journaleintrag **greift sie ab**, statt sie neu zu erfragen.

---

## Reason-Codes

Feste Liste. Ohne feste Codes sind Einträge über Deals hinweg nicht vergleichbar, und genau die Vergleichbarkeit ist der Zweck.

| Code | Feld |
|---|---|
| `R-TECH` | Technischer Reifegrad, unbelegte Leistungskennzahlen |
| `R-GTM` | Pilot → Umsatz, Zugang zum Buying Centre, Sales Cycle |
| `R-MARKT` | Wettbewerb, Moat, Substitution, Marktgröße |
| `R-UNIT` | Unit Economics, Kostenmodell, Preisannahmen |
| `R-CAP` | Cap Table, Rundenvollzug, Terms, Verwässerung |
| `R-IP` | Schutzrecht, Schutzumfang, Lizenzkette |
| `R-TEAM` | Bus-Factor, Rollenlücke, Teamkonstellation |
| `R-GOV` | Governance, Gesellschaftsrecht, Board- und Shareholder-Struktur |
| `R-REG` | Regulatorik, Akkreditierung, Beschaffungslinie |
| `R-FIN` | Runway, Finanzplanung, Kapitalbedarf bis Meilenstein |
| `R-DATA` | Datenrechte, Datenzugang, Datenherkunft |
| `R-ALIGN` | Exit-Alignment, Ambition, Gründer-Fonds-Passung |

Mehrfachnennung ist zulässig. Zusätzlich zulässig, weil es keine Eigenschaft der Firma ist:
`X-FONDS` — die Entscheidung trägt eine Fonds-Restriktion (Ticket, Stage-Mandat, kein Follow-on-Kapital, Portfolio-Konflikt, Timing-Fenster).

**Die Trennung ist der Punkt.** Eine Absage aus `X-FONDS` ist kein Urteil über die Firma. Wer sie später als solches erinnert, zieht aus dem eigenen Portfolio die falschen Lehren.

---

## Eintrags-Template

```markdown
## <YYYY-MM-DD> — <Deal> — <INVEST / PASS / NOT NOW / WATCH>

**Stadium:** <Pre-Seed / Seed / …>
**Runde:** <Größe, Instrument, Bewertung oder Cap, soweit bekannt>
**Quellenstand bei Entscheidung:** <Deck-only / + Call / + Data Room / vollständige DD>
**Voriger Eintrag:** <Datum oder „keiner">

### Prior — wörtlich aus `analysis/00-prior.md`, nicht neu formuliert

- **Achsen:** A1-… × A2-… × A4-… · **Evidenz-Decke:** <S2 erreichbar / S3-Decke>
- **F-/D-Stufen je Gründer:** …
- **P1:** <prüfbare Behauptung mit Fundstelle>
- **P2:** …
- **P3:** …
- **Outlier-Kandidat:** <ja/nein — welche Dimension>

*Fehlt eine Session 0, hier ausdrücklich „kein Prior festgehalten" schreiben. Nicht rekonstruieren — ein nachträglich gebauter Prior ist wertlos und täuscht die spätere Auswertung.*

### Was die DD daraus gemacht hat

| Prognose | Ergebnis | Beleg |
|---|---|---|
| P1 | bestätigt / widerlegt / nicht berührt | <Zitat aus dem DD-Befund> |
| P2 | | |
| P3 | | |

**Was die DD gefunden hat, das im Prior nicht vorkam:** <…>

### Entscheidung

**<INVEST / PASS / NOT NOW / WATCH>** · **Conviction:** <n>/10
**Reason-Codes:** <R-…, R-…, ggf. X-FONDS>

**Tragende Begründung** — je Grund eine Kette *Behauptung → Mechanik → Konsequenz*:
1. …
2. …

**Fonds-Restriktion, die mitträgt:** <konkret, oder „keine">

### Prognose — der eigentliche Zweck des Eintrags

**Was ich erwarte:** <eine falsifizierbare Aussage über die nächsten 12–24 Monate. „Wird sich gut entwickeln" ist keine.>
**Woran ich merke, dass ich falsch lag:** <…>
**Review-Datum:** <YYYY-MM-DD>
**Re-Engagement-Trigger:** <2–4 messbare Ereignisse oder Kennzahlen>

### Outcome — beim Review ausfüllen, nicht vorher

**Stand am <Datum>:** *(leer)*
**Prognose getroffen?** *(leer)*
**Was ich daraus lerne:** *(leer)*
```

---

## Review-Disziplin

Ein Journal ohne Reviews ist ein Archiv. Der Wert entsteht erst, wenn die Prognose gegen die Realität gehalten wird.

- **Review-Datum ist Pflichtfeld.** Ohne Datum kein Eintrag.
- Beim Review wird **nur** das Outcome-Feld gefüllt. Prognose und Begründung bleiben unangetastet, auch wenn sie im Rückblick peinlich sind — besonders dann.
- **Auch Absagen werden reviewed.** Die teure Fehlerklasse in dieser Anlageklasse ist der verpasste Deal, nicht der schlechte. Ein Journal, das nur Investments verfolgt, misst genau die falsche Seite.

---

## Was der Journal ausdrücklich nicht ist

Kein Bewertungssystem, kein Ranking, kein Gate. Er erzeugt **Datenbasis**, keine Urteile. Aus der Datenbasis können später Auswertungen entstehen — Trefferquoten je Reason-Code, Kalibrierung der Conviction-Skala, systematische blinde Flecken. Bis dahin ist er reine Buchführung, und schon das rechtfertigt ihn.
