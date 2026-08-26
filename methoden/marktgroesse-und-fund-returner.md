# Marktgröße bottom-up und Fund-Returner-Rechnung

Diese Datei definiert, wie in einer DD die **Marktgröße selbst geschätzt** und daraus die Frage
beantwortet wird: *ist das für unseren Fonds ein interessantes Investment?*

**Wann:** Session 5, als Pflichtblock. Die Eingangsdaten (Preis, Käufersegment) kommen aus Session 3.
**Wohin:** Der **vollständige Rechenweg** in den DD-Report — Inputs, Anker, Zwischenergebnisse,
Output. Nicht die Zusammenfassung, der Rechenweg.

---

## Warum das existiert

**Weil die Zahl im Deck fast nie die Frage beantwortet, die wir haben.** Gründer geben TAM/SAM/SOM
in Geld an, top-down aus Analystenreports, auf ein Zieljahr fünf Jahre in der Zukunft. Wir brauchen
etwas anderes: wie viele Organisationen es gibt, die dieses Produkt heute kaufen könnten, wie viele
davon erreichbar sind, und was daraus für unseren Anteil folgt.

Der Anlass war konkret. In der Haste-DD nannte das Deck EUR 4 Mrd. SAM und begründete ihn mit
*„~160k NIS2-regulated EU entities addressable"*. Die 160.000 stimmen — es ist die Schätzung der
EU-Kommission. **Sie beschreibt aber überwiegend Mittelstand, und den hatte die Firma selbst
abgewählt.** Rechnet man den Markt in Käufern statt in Euro, bleiben rund 4.000. Das findet man
nicht durch Lesen, sondern nur durch eigenes Rechnen.

---

## 🔴 Die Ankerregel

**Jede Stufe der Herleitung braucht einen Anker, und der Anker muss zählbar sein.**

**Zugelassen:**

| Ankertyp | Beispiele |
|---|---|
| Amtliche Unternehmensstatistik | Eurostat SBS (Unternehmen nach Größenklasse und Branche), Destatis, Companies House, ONS |
| Regulatorische Register und Anwendungsbereiche | NIS2-Entitäten, KRITIS-Betreiber, BaFin-Listen, EASA-/ESA-Register, FDA-Establishment-Listen |
| Verbands- und Community-Mitgliederzahlen | Branchenverbände, FIRST, CSSA, ISACs |
| Öffentliche Vergabe mit echten Vertragswerten | TED, EuroHPC JU, nationale Vergabeportale, USAspending, SAM.gov |
| Physische Zählungen | Top500, Rechenzentrums- und Colocation-Register, Satellitenkataloge, Flottenlisten, Anlagenregister |
| Kunden- und Referenzlisten der Wettbewerber | Website-Logos, Case Studies, Pressemitteilungen |
| Die eigenen Referenzgespräche | Was ein Käufer über seine Peer-Gruppe sagt |

**🔴 Nicht als Beleg zugelassen: Analystenreport-TAMs.** Gartner, Forrester, IDC, McKinsey, Grand
View Research, MarketsandMarkets, Mordor Intelligence, Fortune Business Insights, Precedence,
Allied. Sie dürfen als **Kontext** zitiert werden — *„das Deck stützt sich auf X"* —, **nie als
Anker einer Stufe.**

**Die Begründung, und sie ist die Position des Fonds:** Diese Zahlen sind systematisch aufgebläht
und spiegeln den tatsächlichen Markt nicht. Sie entstehen top-down aus Wachstumsannahmen, zählen
angrenzende Kategorien mit, und werden von Anbietern gekauft, die ein Interesse an einer großen Zahl
haben. Ein SAM, der auf einem solchen Report ruht, ist keine Schätzung, sondern eine Übernahme.

**Wo ein Anker fehlt, wird geschätzt — aber die Schätzung wird als solche markiert**, mit der
Annahme im Klartext. *„79.000 × 40 % (Schätzung Branchenanteil)"* ist zulässig. Eine Zahl ohne Anker
und ohne Schätzungsvermerk ist es nicht.

---

## Die fünf Stufen

### Stufe 1 — Käuferdefinition

**Ein Satz, falsifizierbar.** Er benennt, was eine Organisation haben oder tun muss, um überhaupt
Käufer zu sein. Wer die Definition nicht in einen Satz bekommt, hat kein Segment, sondern eine
Stimmung.

Gute Definitionen enthalten drei Teile: ein **technisches oder operatives Merkmal** (was muss da
sein), eine **Größenschwelle** (ab wann gibt es Budget und eine kaufende Funktion), und einen
**Auslöser** (warum kauft jemand jetzt statt irgendwann).

*Beispiel Haste:* „Eine Organisation, die (1) Compute betreibt, auf dem ein konventioneller
EDR-Agent nicht laufen kann oder darf, (2) groß genug für eine eigene Sicherheitsorganisation mit
Budget ist, und (3) einen regulatorischen oder operativen Grund hat, den Nachweis zu führen."

### Stufe 2 — TAM, SAM, SOM als Käuferzahlen

**In Organisationen rechnen, nicht in Geld.** Geld entsteht erst in Stufe 3, aus Zahl × Preis. Wer
in Geld anfängt, kann den eigenen Rechenweg nicht mehr prüfen.

| Stufe | Frage | Typischer Filter |
|---|---|---|
| **TAM** | Wer auf der Welt passt auf die Definition? | Größenklasse, Branche, physische Zählung |
| **SAM** | Wen davon erreichen wir **heute** — mit diesem Produkt, dieser Sprache, dieser Zulassung, diesem Kanal? | Geografie, Regulierung, technische Voraussetzung, vorhandener Vertriebsweg |
| **SOM** | Wen davon gewinnen wir in **3–5 Jahren**, mit diesem Team und diesem Budget? | Vertriebskapazität, Sales Cycle, Wettbewerb |

**Drei Fehler, die regelmäßig passieren:**

- **Der SAM enthält einen Kanal, den es noch nicht gibt.** Ein Reseller- oder MSSP-Weg, der geplant
  ist, gehört nicht in den SAM. Er gehört ins TAM
- **Der SAM enthält ein Segment, das die Firma abgewählt hat.** Passiert, weil das Deck älter ist
  als die Strategie. **Immer gegen das prüfen, was die Gründer im Gespräch gesagt haben**
- **Der SOM ist eine Umsatzzahl geteilt durch einen Wunsch-ACV.** Er muss von der Vertriebsseite her
  gebaut werden: wie viele Abschlüsse pro Jahr, ab wann, mit wie vielen Leuten

**Gegenprobe, immer:** Wie viel Prozent des SAM ist der SOM? Unter 0,1 % ist der SAM zu weit
gefasst; über 5 % ist der SOM optimistisch. Und: Deckt sich das Verhältnis mit dem, was das Deck
behauptet? Zwei unabhängig hergeleitete Zahlen in derselben Größenordnung sind ein starkes Signal.

### Stufe 3 — Preis und Frequenz

**Knüpft direkt an Check 4 (Preis-Konkretisierung) an.** Ohne Abrechnungseinheit, Rate Card,
Minimum Commitment und mindestens eine echte Vertragszahl gibt es keinen Preis — dann wird der Wert
als Spanne geführt und die ganze Rechnung als vorläufig markiert.

**Welchen Preis ansetzen, wenn es mehrere gibt** — und es gibt fast immer mehrere:

| Angabe | Was sie ist |
|---|---|
| Einstiegs-ACV | was der erste Vertrag bringt |
| Ausgebauter Endzustand | was ein voll expandierter Kunde bringt |
| Käuferseitige Validierung | was ein echter Käufer als Spanne genannt hat |
| Deck-ACV | die Planannahme |

**Angesetzt wird ein Wert zwischen Einstieg und Endzustand**, begründet mit der
Land-and-Expand-Annahme, und er muss innerhalb der käuferseitigen Validierung liegen. **Liegt der
Deck-ACV außerhalb jeder Validierung, ist das ein Befund** und gehört in den Report.

**Frequenz:** Bei Jahresverträgen 1. **Aber prüfen, ob es wirklich ein Abo ist.** Eine
Renewal-Quote deutlich unter 100 % des Erstjahres — etwa „Renewal 20–25 % des ARR" — deutet auf
**Lizenz plus Wartung**, nicht auf ein Abo. Dann ist der Umsatz ab Jahr 2 je Kunde ein Bruchteil,
und die ganze SOM-Rechnung ist zu hoch. Als offener Punkt markieren, nicht wegrechnen.

### Stufe 4 — Gegenprobe gegen die Gründerzahlen

Die eigene Rechnung neben die des Decks stellen, Stufe für Stufe, **mit einer Spalte „Grund" für
jede Abweichung.** Eine Abweichung ohne benannten Grund ist kein Befund, sondern ein Rechenfehler
auf einer der beiden Seiten.

Typische Gründe: eine Position im TAM ist eine Prognose statt einer Käuferschicht · der SAM enthält
das abgewählte Segment · der SOM enthält Phasen, die nach eigener Analyse nicht tragen.

### Stufe 5 — Fund-Returner-Rechnung

```
Anteil bei Einstieg      =  Check ÷ Post-Money
Anteil beim Exit         =  Anteil bei Einstieg × (1 − künftige Verwässerung)
Exit für 1× Fonds nötig  =  Fondsgröße ÷ Anteil beim Exit
Nötiges Umsatzmultiple   =  nötiger Exit ÷ SOM-Umsatz
Erwartetes Ergebnis      =  (SOM-Umsatz × marktübliches Multiple) × Anteil beim Exit
```

**Vier Disziplinen, ohne die die Rechnung falsch wird:**

1. **Post-Money, nicht Pre-Money.** Post = Pre + Rundengröße. Die Verwechslung schmeichelt dem Deal
   systematisch
2. **Die künftige Verwässerung ehrlich ansetzen.** Für eine Pre-Seed-Position, die durch Seed,
   Serie A und Serie B geht, sind **50–60 %** realistisch, nicht 30 %. Immer eine Sensitivitätszeile
   mitrechnen — sie verändert das Ergebnis stärker als jede andere Annahme
3. **Das Exit-Multiple aus vergleichbaren Transaktionen**, nicht aus dem Deck. Für europäische
   B2B-Software heute 8–15× ARR; Ausreißer nach oben brauchen eine Begründung
4. **Die Fondsgröße ist die des Fonds, aus dem investiert wird.** Bei einem Warehouse-Deal die
   Zielgröße des aufnehmenden Fonds, nicht der heutige Deckungsgrad — und wenn beides auseinander
   liegt, beide Zeilen zeigen

**Die Frage lautet nicht „schaffen wir 3×", sondern: kann diese Position den Fonds zurückzahlen?**
Ein Fonds mit 15–20 Positionen braucht das nicht von jeder — aber von mindestens einer. Deshalb ist
die richtige Formulierung des Ergebnisses: **ist dieser Deal ein *Kandidat* für diese Rolle, oder
ist er eine solide Multiple-Position?** Beides ist ein legitimes Ergebnis, aber es sind
verschiedene, und die Antwort gehört in den Report.

**Gegenprobe, die den Fall oft entscheidet:** Wenn der nötige Exit unerreichbar aussieht, ausrechnen,
welches Post-Money nötig wäre, damit es funktioniert. Kommt eine absurde Zahl heraus, ist **nicht der
Preis das Problem, sondern die Größenordnung des Marktes** — und das ist eine andere Diskussion als
eine Bewertungsverhandlung.

---

## Ausgabeform im Report

**Ein Ergebnis ohne sichtbaren Rechenweg gilt als nicht geliefert.**

Pflichtbestandteile des Report-Abschnitts:

1. **Die Käuferdefinition** im Wortlaut
2. **Je Stufe eine Zeile mit Anker, Rechnung und Zwischenergebnis** — als Codeblock oder Tabelle, so
   dass jeder Schritt einzeln angreifbar ist
3. **Die Verhältnis-Gegenprobe** (SOM als Prozent des SAM), gegen die Deck-Behauptung gehalten
4. **Die Abweichungstabelle** gegen die Gründerzahlen, mit Grund je Zeile
5. **Die Fund-Returner-Rechnung** als Block, plus mindestens **eine Sensitivitätszeile zur
   Verwässerung**
6. **Ein Urteilssatz**: Fund-Returner-Kandidat oder Multiple-Position — und was daraus für Preis,
   Rolle und Ticket folgt

**Was nicht hineingehört:** eine neue Bewertungszahl. Die Rechnung liefert Argumente für oder gegen
eine Position, sie ersetzt die Preisfindung nicht.

---

## Durchgerechnetes Beispiel — Haste Security, 26.08.2026

**Käuferdefinition:** Organisation mit Compute, auf dem kein konventioneller EDR-Agent laufen kann
oder darf; groß genug für eine eigene Sicherheitsorganisation; mit regulatorischem oder operativem
Nachweisgrund.

```
STUFE 1 — TAM
Anker  Eurostat SBS 2023: 33,1 Mio. aktive EU-Unternehmen, 99,8 % davon KMU
       33.100.000 × 0,2 %                       =  66.200   EU ab 250 Beschäftigten
       66.200 × 25 %     (Schätzung)            =  16.550   davon ab 1.000
       16.550 ÷ 0,21     (Schätzung EU-Anteil)  =  79.000   weltweit ab 1.000
       79.000 × 40 %     (Schätzung Branchen)   =  32.000   mit OT-/Bare-Metal-Bestand
       + Spezialbetreiber (Schätzung)           =   3.000   HPC, Colo, Labs, Space, Quantum
                                        TAM     =  35.000 Käufer

STUFE 2 — SAM   EU-27+DACH, OT-Branchen, technisch erreichbar; KMU ausgeschlossen
       16.550 → 6.600 → 4.000 Käufer
       Gegenprobe NIS2: 160.000 Entitäten im Anwendungsbereich, ~33 % essential (52.800).
       Unsere 4.000 sind deren oberste Schicht, 7,6 %.

STUFE 3 — SOM   20 Käufer in 3–5 Jahren
       Anker: Deck Phase 1 = 5 Mio. ARR bei 250–500k Ø-Vertrag → 10–20 Kunden
       Gegenprobe: 20 ÷ 4.000 = 0,5 % des SAM; Deck behauptet 0,6–1 %. Gleiche Größenordnung.

STUFE 4 — PREIS  250.000 EUR ACV, 1× p. a.
       Einstieg ~100k · Endzustand ~500k · Käufervalidierung 200–850k · Deck 250–500k

ERGEBNIS   SOM-Umsatz = 20 × 250.000 × 1 = EUR 5,0 Mio. ARR

STUFE 5 — FUND RETURNER
       Check 500.000 · Post-Money 14.500.000 (12 pre + 2,5 Runde) · Fonds 10.000.000 · Dil. 30 %
       500.000 ÷ 14.500.000        =  3,45 %   Anteil bei Einstieg
       3,45 % × 0,70               =  2,41 %   Anteil beim Exit
       10.000.000 ÷ 0,0241         =  EUR 414,3 Mio.  Exit für 1× Fonds
       414,3 ÷ 5,0                 =  83 ×     nötiges Umsatzmultiple
       marktüblich                    10–15 ×
       bei 12 ×: 60 Mio. × 2,41 %  =  EUR 1,45 Mio.  =  2,9 × auf den Check

       Sensitivität Verwässerung 60 %:  1,38 %  →  EUR 725 Mio. nötig
       Gegenprobe Post-Money für 60-Mio.-Exit:  2,1 Mio. — also nicht der Preis ist das Problem
```

**Urteil:** kein Fund-Returner-Kandidat auf dem Enterprise-SOM, sondern eine 2,9–5×-Position. Die
Phasen, die das ändern würden, rechnet der Lead-Investor selbst aus der Bewertung heraus. **Folge:
ein Argument für die bestehende Preisposition, kein Ausschlussgrund — und eine deutliche Aufwertung
der offenen Fragen zu den späteren Phasen.**

**Zwei Befunde, die nur durch das eigene Rechnen sichtbar wurden:** der SAM-Treiber des Decks
beschreibt ein abgewähltes Segment · und der Fall ist unabhängig vom Einstiegspreis kein
Fondsrückzahler.
