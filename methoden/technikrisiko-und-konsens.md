# Technikrisiko und Konsens – was eine DD klären kann, und was sie nicht abwerten darf

Diese Datei definiert, wie die DD **Risiken nach ihrer Klärbarkeit trennt**, wie sie das technische Risiko
an seinen Grenzen prüft, woher eine Idee kommt und warum sie jetzt kommt, und wie sie das eigene Urteil
gegen den Sog zum Konsens prüft. Dazu kommen die **Kernfragen**: die ein bis drei Fragen, die den Fall
entscheiden, und der schnellste verlässliche Weg zu ihrer Antwort.

**Wann:** Die Herkunft der Idee und die Kernfragen entstehen vor der Planfreigabe (Marktbild, Zeile 0e). Die
Sessions 3 bis 5 liefern und prüfen. Session 6 fragt.
**Wohin:** Klassen, Bemerkenswert, die Wette und die Kernfragen in den Zustandsblock der Deal-`CLAUDE.md`.
Befunde in den Report, Fragen in das Call-Sheet.

---

## Warum es diese Datei gibt

Der Skill war darauf gebaut, Gegenbeweise zu finden. Das bleibt richtig. Er hatte aber keinen Ort für das
Gegenstück: Was müsste wahr sein, damit eine Firma gross wird, und was an einem Fall ist ungewöhnlich genug,
um die Quelle eines Ausreissers zu sein? Wer nur Risiken zählt, landet bei gut geprüften, durchschnittlichen
Firmen. Eine KI-gestützte DD hat diesen Hang von Haus aus. Sie wertet ab, was noch nie versucht wurde, und
gewichtet Benchmarks aus früheren Deals über.

Anlass waren Kolumnen eines Deep-Tech-Investors aus dem Jahr 2026. Er argumentiert, dass die besten
Deep-Tech-Firmen Marktrisiko gegen Technikrisiko tauschen. Technikrisiko lasse sich durch Prüfung klären,
Kundenverhalten kaum. Gründlich sei nicht dasselbe wie langsam: Es gehe um die kürzeste Zeit bis zur
belastbaren Einsicht, und die komme oft von den richtigen Menschen statt von mehr Recherche.

**Die Kolumnen liefern den Rahmen, die Belege kommen aus der eigenen Praxis.** Was hier als Prüfschritt steht,
schliesst eine Lücke und gilt sofort. Was hier eine Urteilsregel ist, trägt eine Belegstufe wie in
`kommerzielle-pruefung.md`: **[bestätigt]** heisst, in zwei oder mehr eigenen Fällen aufgetreten, und macht die
Regel zum Pflichtcheck. **[Einzelbeobachtung]** heisst, bisher ein Fall, und dient als Referenz.

**Was diese Datei nicht ändert:** Die kommerzielle Prüfung bleibt vollständig. Im B2B-Geschäft lässt sich
Marktrisiko zu einem guten Teil prüfen, über zählbare Käufer, vorhandene Budgets und bezahlte Piloten.
Unprüfbar ist vor allem Verhalten: wie schnell Menschen eine neue Arbeitsweise annehmen. Auch die Fondsmechanik
bleibt. Technikrisiko kostet Kapital und Zeit, und ein kleiner Fonds ohne Reserve muss wissen, ob seine Runde
das Entscheidende beweist.

---

## 1. Risiken nach Klärbarkeit zerlegen

Jedes Risiko der Top 5 bekommt eine Klasse und einen Klärungsweg:

| Klasse | Was | Typischer Klärungsweg |
|---|---|---|
| `T` Technik | Physik, Engineering, Fertigung, Ausbeute | eigene Rechnung, Primärquelle, Experte |
| `K` Kommerz | zählbare Käufer, Budget, Preis, Vertrieb | kommerzielle Prüfung, Referenzgespräch |
| `A` Adoption | Verhalten von Nutzern und Organisationen, Tempo der Annahme | meist nur Zeit, allenfalls ein Pilot |
| `F` Fonds, Runde, Struktur | Rundengrösse, Preis, Kapitalbedarf bis zum nächsten Nachweis, Gesellschaft, Eigentum an IP, Name und Code | Rechnung, Register, Vertrag |

Ein Risiko, das sich durch keine Prüfung klären lässt, wird **einmal als „die Wette“** benannt, in einer
Zeile. Es wird nicht in mehreren Punkten wiederholt und nicht mehrfach von der Conviction abgezogen. Die
Tiefe der DD geht dorthin, wo sich etwas klären lässt.

**Prüfschritt.** Der Zustandsblock führt die Klasse in eckigen Klammern hinter jedem Risiko, zum Beispiel
`[T, Rechnung]` oder `[A, nur Zeit]`.

---

## 2. Technische Grenzfragen – [bestätigt]

Für jedes `T`-Risiko vier Fragen:

1. **Wo liegt die Grenze?** Theoretischer oder physikalischer Grenzwert gegen die Behauptung und gegen den
   besten kommerziell verfügbaren Stand. Eine Behauptung nahe an der Grenze braucht einen Messnachweis, eine
   jenseits davon ist ein Befund.
2. **Wo kippt die Techno-Ökonomie?** Ab welchem Preis, welcher Stückzahl, welchem Wirkungsgrad oder welcher
   Ausbeute wird der Kauf selbstverständlich, mit einer Grösse, die im Budget des Kunden schon existiert?
   Das ist der Test „wenn es funktioniert, kauft es jeder“. Er schliesst an das Positivmuster der
   kommerziellen Prüfung an. Vor dem ersten Produkt tritt dieser **Kipppreis** an die Stelle der fehlenden
   Vertragszahl.
3. **Engineering oder noch Wissenschaft?** Ist das offene Problem irgendwo schon gezeigt worden, im Labor, in
   einer Nachbarbranche, in einem Paper mit Messdaten? Dann ist es Engineering: Zeit und Geld. Wenn nicht, ist
   es Wissenschaft: Der Ausgang ist offen, und die Zeit dahin lässt sich nicht planen.
4. **Beweist die Runde die eine Zahl?** Welche Zahl entscheidet den Fall, und reicht das Geld dieser Runde,
   um sie zu erzeugen? Wenn nicht, ist das ein `F`-Befund, kein Urteil über die Technik.

**Warum [bestätigt]:** In einem Halbleiter-Fall (07/2026) ergab erst die eigene Leistungsrechnung gegen den
besten Wettbewerber, dass aus der kommunizierten tausendfachen Verbesserung eine sechs- bis siebenfache
wurde. In einem Photonik-Fall (10/2026) senkte die Physik-Gegenrechnung nach dem ersten Call die Conviction
und bestimmte den zweiten Call. In beiden Fällen hat die Grenzfrage den Fall entschieden, nicht die
Marktgrösse.

---

## 3. Herkunft der Idee und warum jetzt

Nicht zu verwechseln mit der **Vorgeschichte**, also der eigenen Historie mit der Firma. Hier geht es um die
Idee selbst. Eine Tabelle mit drei bis sechs Zeilen:

| Früherer Versuch (Firma oder Forschungslinie) | Woran gescheitert oder stehen geblieben | Was sich seitdem geändert hat (Enabler) | Beleg |
|---|---|---|---|

Enabler sind eine Kostenkurve, eine neue Komponente, ein Datensatz, ein Fertigungsverfahren, eine Regulierung.
Dazu eine Zeile, **auf welchen kleineren Schritten** die Idee aufbaut: Durchbrüche haben fast immer Vorstufen,
und wer sie kennt, sieht schneller, ob das Team die nächste Stufe nimmt oder eine überspringt.

**Quellen:** OpenAlex und Patentfamilien für Forschungslinien, Presse, Handelsregister und Wayback für
eingestellte Firmen, dazu die Gründerfrage. Die Werkzeuge stehen in `outside-in-recherche.md`.

### Ein früherer Fehlschlag ohne neuen Enabler ist ein Gegenbefund – [Einzelbeobachtung]

Hat jemand dasselbe ernsthaft versucht und ist gescheitert, und lässt sich kein Enabler benennen, der sich
seitdem geändert hat, dann ist das ein starker Gegenbefund. Er wiegt schwerer als jede Marktzahl. Umgekehrt ist
ein belegter Enabler ein Pluspunkt und gehört unter **Bemerkenswert**.

**Warum [Einzelbeobachtung]:** In einem Robotik-Fall (11/2026) nannte der Gründer selbst, dass ein Kunde
denselben Ansatz bereits eingestellt hatte. Welcher Enabler den neuen Versuch trägt, wurde zur Gate-Frage für
den zweiten Call. Ein zweiter Fall, in dem ein früherer Fehlschlag den Ausgang bestimmt, hebt die Regel auf
Pflichtcheck.

---

## 4. Lieferanten-Uhr und Industriephase – [bestätigt]

Jede These, die auf fremder Hardware oder einer fremden Plattform aufsetzt, hat eine Uhr laufen. Der
Lieferant wächst in die Schicht darüber. Drei Fragen:

1. **Welche Schichten besitzt die Firma, welche kauft sie zu?**
2. **Wer liefert die Schicht darunter, und ist er in Nachbarmärkten schon eine Schicht aufgestiegen?** Gehört
   der Flaschenhals einem Wettbewerber, ist das ein eigenes Risiko neben der reinen Lieferantenabhängigkeit:
   Der Wettbewerber kann bündeln, die Firma muss zukaufen.
3. **In welcher Phase steht die Industrie?** Gibt es für die Schnittstellen Standards und mehrere austauschbare
   Lieferanten (modulare Phase), oder legt jeder sie noch selbst fest (integrierte Phase)? Neue Technik setzt
   eine reife Industrie wieder in die integrierte Phase zurück.

**Folgerung:** In der integrierten Phase ist zugekaufte Standard-Hardware die Falle. Die Firma endet als
Systemintegrator auf fremder Plattform, und jede einzelne Zukaufentscheidung war für sich vernünftig. In der
modularen Phase verbrennt eigene Integration Kapital, das die Spezialisten nicht brauchen. Die Frage ist
also nicht „Plattform oder nicht“, sondern ob die Wahl zur Phase passt, und ob die Runde den
Integrationsschritt bezahlen kann.

**Warum [bestätigt]:** Das Muster ist 2026 in fünf eigenen Fällen aus Robotik, Sensorik und Security
aufgetreten. Es ist das verlässlichste Frühwarnsignal, das die Fallpraxis kennt. Die Fassung mit der
Industriephase ersetzt den früheren bewussten Ausschluss der Stack-Positions-Frage. Dieser Ausschluss richtete
sich gegen die Standardfrage „konkurriert ihr mit der Plattform“. Hier wird nach Mechanik und Phase gefragt.

---

## 5. Die eigene Fabrik: Burggraben oder Umweg – [Einzelbeobachtung]

Baut eine Firma eigene Fertigung auf, drei Fragen:

1. Liefert die Fertigung etwas, das sonst keiner hat: Daten, Prozesswissen, Lieferfähigkeit, Zertifizierung?
2. Ist der Ausstoss je Kopf oder die Ausbeute **messbar** besser als bei den Etablierten? Dass KI den Ausstoss
   von der Arbeit entkoppelt, ist eine Hypothese, kein Befund.
3. Wer finanziert den nächsten Integrationsschritt nach dieser Runde, und mit welchem Nachweis?

Ist die Fabrik der Burggraben, trägt sie den Fall. Ist sie ein Umweg um ein Softwareproblem, kauft sich die
Firma das falsche Problem.

**Warum [Einzelbeobachtung]:** Ein kapitalintensiver Fertigungs-KI-Fall (08/2026) ging nach einer
Finanzierung im zweistelligen Millionenbereich in die Eigenverwaltung. Der Engpass seines Marktes waren
Fachkräfte und Maschinen, nicht Kapazität. Ein zweiter Fall hebt die Regel auf Pflichtcheck.

---

## 6. Konsens-Gegenprobe am eigenen Urteil

Der Skill ist selbst eine KI und teilt deren Hang zum Konsens. Deshalb drei Schritte vor der Conviction:

1. **Präzedenz-Argumente markieren.** Jede Negativaussage, die nur darauf ruht, dass etwas noch niemand
   geschafft hat, dass es keinen Vergleichsfall gibt oder dass ein Benchmark aus früheren Deals es so sagt,
   bekommt die Marke `[Präzedenz]`. Sie bleibt nur dann ein Risiko, wenn ein **Mechanismus** benannt ist:
   Physik, Ökonomie oder belegtes Käuferverhalten. Ohne Mechanismus wird sie zur offenen Frage.
2. **Die Spiegelfrage stellen:** Was müsste wahr sein, damit diese Firma gross wird? Die Antwort steht neben
   der Frage, was wahr sein müsste, damit sie scheitert.
3. **Die Selbstfrage:** Würde jeder andere Fonds diesen Fall genauso lesen? Wenn ja, woher käme unser
   Vorsprung, und warum ist die Runde dann nicht schon voll?

---

## 7. Bemerkenswert

Bis zu **drei Punkte**, die an dem Fall ungewöhnlich sind und die Quelle eines Ausreissers sein könnten,
jeweils mit Beleg:

- eine Sicht der Gründer, die gegen den Konsens steht und sich begründen lässt
- ein Zugang zu Käufern, Daten oder Fertigung, den andere nicht haben
- ein technisches Asset, das sich nicht in Monaten nachbauen lässt
- ein Enabler für „warum jetzt“, den andere übersehen

**Ein Vermerk, kein Gewicht.** Bemerkenswert hebt die Conviction nicht automatisch. Es sorgt dafür, dass das
Ungewöhnliche im Urteil sichtbar bleibt, statt in der Risikoliste unterzugehen. Fehlt etwas Bemerkenswertes,
steht dort „nichts gefunden“. Auch das ist ein Befund.

---

## 8. Zeit bis zur Einsicht: die Kernfragen

Langsam ist nicht dasselbe wie gründlich. Die DD benennt **ein bis drei Kernfragen**: die Fragen, deren Antwort
den Fall entscheidet. Sie stehen im Plan vor der Freigabe und werden nach Session 4 geprüft. Jede bekommt
den schnellsten verlässlichen Weg:

1. eigene Rechnung
2. Primärquelle (Register, Patent, Paper, Datenblatt)
3. ein Mensch mit Fachwissen aus dem Haken `experten` der Haus-Schicht
4. die Gründerfrage im nächsten Call

**Die Reihenfolge ändert sich, gekürzt wird nichts.** Die Kernfragen laufen zuerst, der übrige Umfang bleibt.
Kann ein Gespräch von dreissig Minuten eine Kernfrage klären, ist es schneller und verlässlicher als ein Tag
Recherche.

**Grenzen beim Experten-Weg:** Claude schlägt vor, wen Anton fragen könnte und mit welcher Frage. Claude
schreibt niemanden selbst an. Die Frage ist so formuliert, dass sie ohne Falldaten auskommt: keine
Firmennamen, keine Zahlen aus dem Data Room, nichts unter NDA. Was ein Experte sagt, ist ein Generator für
Fragen und eine Einschätzung mit Bias-Klasse, kein Befund (siehe `externe-einschaetzung.md`).

---

## Die Fragen für den Call

Sprechbar gehalten, eine Frage auf einmal.

| Abschnitt | Frage im Gespräch |
|---|---|
| 2 · Grenze | *„Wo liegt die Grenze für das, was ihr macht, und wie nah seid ihr dran?“* |
| 2 · Techno-Ökonomie | *„Ab welchem Preis kauft ein Kunde das, ohne lange nachzudenken?“* |
| 2 · Engineering oder Wissenschaft | *„Hat jemand das schon einmal gezeigt, auch nur im Labor? Oder seid ihr die Ersten?“* |
| 2 · Die eine Zahl | *„Welche Zahl wollt ihr mit dieser Runde beweisen?“* |
| 3 · Herkunft | *„Wer hat das vor euch versucht, und was ist heute anders?“* |
| 4 · Selbst bauen | *„Welchen Teil baut ihr selbst, welchen kauft ihr, und warum?“* |
| 4 · Lieferanten-Uhr | *„Wer liefert euch die Ebene darunter, und was hält ihn davon ab, eure Ebene selbst zu bauen?“* |
| 4 · Phase | *„Gibt es für eure Schnittstellen schon Standards, oder legt ihr sie gerade selbst fest?“* |
| 5 · Fabrik | *„Welches Wissen steckt heute in den Köpfen der Fachkräfte, und wie macht ihr es messbar?“* |
| 5 · Nächster Schritt | *„Was kostet der nächste Integrationsschritt, und wer finanziert ihn nach dieser Runde?“* |

---

## Ausgabeform

**Im Zustandsblock der Deal-`CLAUDE.md`**, unter „Conviction & Top-5-Risiken“:

```
1.–5. <Risiko> [T|K|A|F, Klärungsweg]: <Beleg>
Bemerkenswert: <bis zu drei Punkte mit Beleg, oder „nichts gefunden“>
Die Wette: <eine Zeile – was nicht klärbar ist und trotzdem gekauft würde>
Kernfragen: <1–3 Fragen · schnellster Weg · Stand>
```

**Im Report:** die Grenzfragen und die Lieferanten-Uhr in Block 4 (Technologie), die Herkunft der Idee in
Block 1, die Konsens-Gegenprobe vor der Conviction. In die Lesefassung kommen „warum jetzt“, die Kernfragen
und Bemerkenswert.

**Was nicht hineingehört:** Begeisterung ohne Beleg. Bemerkenswert ist kein Werbetext, und die
Spiegelfrage ist keine Verteidigungsrede. Beides folgt denselben Belegregeln wie jedes Risiko.
