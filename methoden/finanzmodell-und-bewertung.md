# Finanzmodell und Bewertung — was das Geld trägt und was das Preisschild behauptet

Diese Datei definiert die dritte Prüfebene neben Marktgrösse und kommerzieller Prüfung: **das
Finanzmodell und die Bewertung.** Sie prüft nicht, ob der Plan ambitioniert ist — das ist er immer —
sondern ob er **bis zu dem Zustand trägt, auf den sich die nächste Runde raisen lässt.**

**Wann:** Session 3 liefert die Eingangsdaten, Session 5 rechnet, Session 6 fragt.
**Wohin:** Befunde in den Report, Fragen in das DDQ-Dokument.

---

## Warum das existiert

Die Marktgrössen-Rechnung sagt, wie viele Kunden nötig sind. Die kommerzielle Prüfung sagt, ob sie
erreichbar sind. Beides beantwortet nicht die Frage, die am Ende die Zeichnung entscheidet:
**reicht das Geld bis dahin, und ist der aufgerufene Preis gegen die heutige Substanz zu
begründen?**

Der blinde Fleck ist dabei nicht die Rechnung — die geht in fast jedem Modell auf. Er liegt an
zwei anderen Stellen. Erstens wird **Runway als Zeitgrösse gelesen** statt als Zustandsfrage: die
richtige Frage ist nicht, wie lange das Geld reicht, sondern was am Ende wahr sein wird. Zweitens
wird die **Bewertung gegen die Erzählung gehalten** statt gegen die nackte Substanz.

Die Regeln stammen aus derselben Quelle wie
`${CLAUDE_PLUGIN_ROOT}/methoden/kommerzielle-pruefung.md`: der Prüfpraxis eines Fund Advisors mit
über fünfzehn Jahren VC-Erfahrung, beobachtet über Investment-Committee-Gespräche zu mehreren
Fällen. **Die Belegstufen sind dieselben und bedeuten dasselbe** — `[bestätigt]` ist Pflichtcheck
und geht ohne Antwort als offener Punkt in den Report, `[Einzelbeobachtung]` ist Referenz.

---

## Teil 1 — Sechs Prüfgriffe am Modell

### 1. Personalkosten sind nicht Gesamtkosten — [bestätigt]

Der billigste und häufigste Fehler, und er passiert **auf beiden Seiten**: im Modell des Gründers,
das Personalkosten als Kostenstruktur ausgibt, und in der eigenen Zusammenfassung, die die
Jahresspalten übernimmt und die Gesamtsumme daneben stellt.

**Zu prüfen ist deshalb zweierlei:** welche der beiden Grössen das Modell je Jahr zeigt — und
welche die eigene Darstellung zeigt. Wer eine Rechnung selbst machen muss, um auf die Gesamtkosten
zu kommen, wird sie irgendwann falsch machen.

> Fehlen daneben **COGS und Bruttomarge** bei einem Produkt, das selbst etwas einkauft — fremde
> Rechenzeit, Daten, Lizenzen, Fertigung —, ist die Kostenstruktur nicht unvollständig, sondern
> unbekannt.

### 2. Grant: beantragt oder geplant? — [Einzelbeobachtung]

Ein Fördermittel im Finanzierungsbild ist keine Zahl, sondern ein Zustand. **Beantragt und
geplant sind zwei verschiedene Dinge**, und zwischen Zusage und Auszahlung liegt regelmässig ein
weiteres Quartal.

**Zu erheben:** Status, Antragsdatum, erwartete Entscheidung, erwartete Auszahlung — und ob das
Modell ohne diese Mittel noch funktioniert. *Verbindet sich mit der bestehenden Regel, jede
Finanzierungsquelle als COMMITTED oder ASSUMPTION zu markieren.*

### 3. 🔴 Erreichungsgrad statt Runway — [bestätigt]

**Die Frage ist nicht, wie lange das Geld reicht. Dass es irgendwann weg ist, ist kein Befund.**

> *„Die Frage ist, was steht denn dem gegenüber? Was ist der Erreichungsgrad von allen Dingen, die
> sie gerade machen, um zu sagen: okay, jetzt können wir darauf nochmal raisen?"*

**Zu beantworten ist also der Zustand am Ende der Runde:** welche Kunden zahlen, welcher Umsatz
läuft wiederkehrend, welche technische Schwelle ist genommen, welche Belege liegen vor. Erst dieser
Zustand entscheidet, ob die nächste Runde überhaupt stattfindet.

**Und er wird gegen die geplante Folgerunde gehalten** — siehe Teil 2, dritte Gegenprobe. Ein
Erreichungsgrad, der die geplante Rundenstufe nicht trägt, ist der schwerwiegendste Befund, den
diese Methode produziert, weil er das Ausfallrisiko **innerhalb** des Investitionshorizonts
verortet und nicht dahinter.

### 4. Die Umsatzprognose entkernen — [bestätigt]

Die Prognose wird nicht bewertet, sondern **zerlegt und wieder aufgebaut:**

```
Plan-Umsatz
  − Umsatz, der auf Absichtserklärungen beruht
  − projektbasierte One-Off-Erlöse (Piloten, Studien, Integrationsprojekte)
  = wiederkehrender Umsatz, der heute belegt ist
  + Neugeschäft, aber erst nach einem vollen Vertriebszyklus (12–18 Monate im Enterprise)
  + falls das Produkt noch nicht steht: die Monate bis zum MVP davor
```

**Was übrig bleibt, ist die Zahl, gegen die gerechnet wird.** Ein Pilot ist Umsatz, aber kein ARR;
ein LOI ist beides nicht.

> Die Gegenprobe zur eigenen Rechnung ist billig: **liegt das Ergebnis mehr als eine
> Grössenordnung unter der Planzahl, stimmt nicht die Prognose, sondern das Erlösmodell** — dann
> unterstellt der Plan einen Modellwechsel (etwa von Flat Fee auf Umsatzbeteiligung), der als
> eigener Befund geführt gehört.

### 5. 🔴 Szenarienmodelle schwingen mit dem kommerziellen Erfolg — aber nicht so, wie sie es zeigen — [Einzelbeobachtung]

Der häufigste Einwand gegen eine Runway-Kritik lautet, das Modell sei szenarienbasiert und das Team
steuere agil nach. **Der Einwand ist berechtigt und ändert weniger, als er verspricht.**

> *„Deren Runway schwingt extrem mit dem kommerziellen Erfolg. … Werden sie wahrscheinlich nicht
> machen, weil wenn du so erfolgreich bist kommerziell, gehst du einfach wieder raus und raist mehr
> Geld. Also dann schiebst du die Burn wieder hoch."*

**Die Asymmetrie ist der Punkt.** Nach unten wirkt Agilität wirklich — man stellt später ein, nimmt
Freelancer, streicht Positionen. Nach oben wirkt sie nicht: wer kommerziell trifft, verlängert
nicht den Runway, sondern raist mehr und beschleunigt.

> **Ein gutes Szenario, das längeren Runway ausweist, beschreibt einen Verlauf, den es nicht geben
> wird.** Gerechnet wird deshalb gegen das schlechte Szenario, und das gute wird als
> Wachstumsplan gelesen, nicht als Sicherheitsreserve.

### 6. Die fehlenden Zeilen zählen — [bestätigt]

Bruttomarge · COGS · Kundenakquisitionskosten · Vertriebszyklus · Retention und Renewal · Burn in
einer einheitlichen Definition. **Was nicht im Modell steht, ist keine Auslassung, sondern eine
offene Annahme** — und sie wird als solche in den Report geschrieben, mit der Grösse, die sie
verdeckt.

Bei einem Modell ohne diese Zeilen ist keine Bewertung herzuleiten. Das ist ein Befund über die
Unterlage, nicht über die Firma, und gehört genau so formuliert.

---

## Teil 2 — Die Bewertungs-Gegenprobe

Die Bewertung wird nicht gegen die Erzählung geprüft und auch nicht zuerst gegen Vergleichsrunden,
sondern gegen die **heutige Substanz, nüchtern aufgezählt.**

### Die Substanzliste — [bestätigt]

Vier Zeilen, jede beantwortbar ohne Interpretation:

| | Frage | Was zählt |
|---|---|---|
| 1 | **Ist die Gesellschaft gegründet?** | Handelsregistereintrag, nicht „in formation", nicht „pending" |
| 2 | **Wie viele Menschen sind angestellt?** | Auf der Lohnliste, mit Eintrittsdatum — nicht zugesagt, nicht assoziiert |
| 3 | **Gibt es Kundenverträge?** | Unterschrieben und beidseitig, mit Gegenwert. Absichtserklärungen zählen hier nicht |
| 4 | **Wie weit ist das Produkt?** | Was läuft heute bei einem Kunden, nicht was demonstrierbar ist |

**Diese Liste wird der geforderten Bewertung gegenübergestellt, bevor irgendein Vergleichswert
herangezogen wird.** Sie ist bewusst hart und bewusst unfreundlich — sie beschreibt, was ein
Käufer bekommt, wenn die Erzählung nicht eintritt.

*Die Gegenprobe gegen Vergleichsrunden kommt danach und korrigiert das Ergebnis in beide
Richtungen.*

### Die Reihenfolge der Ausgabe ist ein Signal — [Einzelbeobachtung]

Steckt der Plan den Grossteil der Mittel ins Produkt, bevor er in den Vertrieb geht, ist das eine
Aussage über die Gründer — sie sind technisch und nicht kommerziell. **Das ist eine Feststellung
zum Plan, nicht ein Urteil über Personen**, und sie verbindet sich unmittelbar mit der
Commercial-Hire-Regel: wer zuerst baut und dann verkauft, kauft sich zwei Vertriebszyklen ein.

**Zu prüfen:** der Anteil von Forschung und Entwicklung an der Mittelverwendung, gegen den Anteil
für Vertrieb und Kundenentwicklung — und ob die Reihenfolge zu dem Erreichungsgrad passt, den die
nächste Runde verlangt.

### 🔴 Trägt die Rundengrösse bis zum Meilenstein, der die nächste Runde begründet? — [bestätigt]

Nicht bis zum Ende des Geldes, sondern **bis zu dem Zustand, auf den sich raisen lässt.** Die
Rechnung ist einfach und wird trotzdem selten gemacht:

```
Rundenstufen-Sprung  =  geplante Folgerunde ÷ aktuelle Runde
Deckung              =  Erreichungsgrad am Ende der Runde  gegen  was die Folgerunde voraussetzt
```

**Ein zweistelliger Sprung bei einstelligem Umsatz ist kein Plan, sondern eine Hoffnung mit
Datum.** Und wenn zwischen dem Ende des Geldes und der geplanten Folgerunde eine Lücke bleibt, ist
sie zu benennen — auf den Finanzierungsbalken der Decks ist sie nie eingezeichnet.

> **Diese Gegenprobe ist der Ort, an dem die eigene Position steht.** Wer nicht führt, die Terms
> nicht gestaltet und nicht nachziehen kann, wird über zwei Grossrunden hart verwässert. Das ist
> unabhängig von der Qualität der Firma und gehört in die Entscheidung, nicht in eine Fussnote.

---

## Die Fragen für den Call

| Regel | Frage im Gespräch |
|---|---|
| 1 · Gesamtkosten | *„Was sind eure Gesamtkosten je Jahr — nicht nur Personal?"* |
| 2 · Grant | *„Ist der Grant beantragt oder plant ihr ihn zu beantragen? Und wann wäre er auf dem Konto?"* |
| 3 · Erreichungsgrad | *„Wenn das Geld weg ist — was ist dann wahr, worauf ihr die nächste Runde raist?"* |
| 4 · Prognose | *„Wenn ihr die Absichtserklärungen und die Projektumsätze rausnehmt, was bleibt für 2027 stehen?"* |
| 5 · Szenarien | *„Was passiert, wenn ihr statt der vollen Runde nur zwei Drittel raist — und was passiert, wenn ihr kommerziell trefft?"* |
| 6 · Fehlende Zeilen | *„Was ist eure Bruttomarge, und was kauft ihr je Auftrag ein?"* |
| Substanzliste | *„Ist die Gesellschaft eingetragen, wer steht auf der Lohnliste, und welcher Vertrag ist beidseitig unterschrieben?"* |
| Rundengrösse | *„Eure nächste Runde ist ein Vielfaches dieser hier. Wo müsst ihr dafür stehen, und reicht dieses Geld bis dahin?"* |

**Gesprächsführung:** Die Erreichungsgrad-Frage ist die wertvollste des ganzen Blocks und wird
regelmässig mit einer Umsatzzahl beantwortet. **Dann ein zweites Mal fragen** — gefragt ist der
Zustand, nicht die Zahl. Und die Substanzliste nicht als Liste vorlesen; sie wird über den
Gesprächsverlauf verteilt und danach zusammengesetzt.

---

## Ausgabeform

**Im Report:** die entkernte Umsatzprognose und die Deckungsrechnung als **ausgeschriebener
Rechenweg** — Inputs, Zwischenergebnisse, Output. Ein Ergebnis ohne sichtbaren Rechenweg gilt als
nicht geliefert, wie bei der Marktgrössen-Rechnung.

**Die Substanzliste steht als vierzeilige Tabelle im Bewertungsabschnitt**, direkt vor den
Vergleichswerten. Sie wird nicht kommentiert, sie wird nur beantwortet.

**Was nicht hineingehört:** ein Urteil über die Ambition. Ein ambitionierter Plan ist der
Normalfall und kein Befund. Der Befund entsteht erst, wo der Plan eine Grösse voraussetzt, die er
selbst nicht erzeugt.
