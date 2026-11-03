# Call-Nachbereitung – Transkript ablegen, Call auswerten, Follow-up

Gilt für jeden Call vor der Investmententscheidung (`/dd:debrief`, oder `/dd` mit Transkript in
einer bestehenden Akte). Im Active Deal Mode übernimmt `/dd:ingest`.

**Warum es diese Datei gibt:** Nach fast jedem Call kam derselbe Auftrag von Hand – einarbeiten,
Wissensstand nachziehen, Einschätzung, Follow-up mit Unterlagen-Anfrage, Intros. Die Auswertungen
hatten trotzdem eine stabile Form gefunden; hier steht sie.

---

## 1. Transkript ablegen

- Ablage `sources/calls/DATUM_call-N-<name>.md`, ungekürzt. Kopf: Teilnehmer, Dauer, Plattform,
  Sprache, Quelle des Transkripts
- **Sprecherlabels nicht trauen.** In Meet-Transkripten hängt eine Stimme oft am falschen Label;
  „Them“ trägt alle Externen zusammen, und wer zu zweit an einem Gerät sitzt, landet unter einem
  beliebigen Namen, auch dem eigenen. Anker in dieser Reihenfolge: Selbstvorstellung, Übergaben
  („I'll let X go into …“), Anrede mit Namen (wer angesprochen wird, spricht nicht), Antworten mit
  Ich-Bezug, Wissen, das nur eine Seite hat. Die Rekonstruktion steht als Transkript-Hinweis mit
  einem Beispielzitat je Sprecher im Kopf; was offen bleibt, wird als Firma statt als Person geführt
- **Eigennamen aus der Spracherkennung sind unbestätigt.** Bevor ein Name in einen Dateinamen, eine
  Anrede, ein Build-Ziel oder eine Mail geht, wird er gegen Ablage, CRM, Mail-Signaturen und Kalender
  gegrept, mit phonetischen Varianten. Ein Firmenname schlägt einen Vornamen. Ist die Auflösung
  belegt, wird sie ohne Rückfrage übernommen
- **Korrekturtabelle** im Transkriptkopf: `ASR | richtig | Beleg`. Die falsche Schreibweise bleibt
  genau dort und als Warnhinweis stehen, sonst nirgends. „Schreibweise unbestätigt“ ist ein offener
  Prüfauftrag, kein Datenpunkt
- **Was unklar bleibt, wird nicht geraten:** eine nummerierte Frageliste an den User, nach Firma
  gruppiert. Fragen, die nur ein Partner beantworten kann, kommen als fertiger Nachrichtentext dazu.
  Die Antworten (oft selbst diktiert, die Nummerierung kann verrutschen) gehen unter „Im Chat
  geklärt“ ins Transkript, damit die Korrektur an der Quelle steht
- **Persönliches einer Person über sich selbst** (etwa wie ein früherer Gründer ausgeschieden ist):
  das Transkript bleibt ungekürzt. Die Auswertung nennt nur, wer die Trennung angestoßen hat, ob sie
  einvernehmlich war und ob Anteile bleiben. Abfindung und Gesundheitliches stehen nur im
  Transkript; vor dem Abschluss außerhalb von `sources/calls/` danach greppen
- **Kritik an Dritten**, die im Call über Kollegen oder andere Firmen fällt, gehört nicht in
  Auswertung, Hub oder Karten

## 2. Die Auswertung `analysis/call-N-auswertung.md`

In dieser Reihenfolge:

1. **Entscheidung oder Einschätzung des Users**, falls er sie mitgegeben hat, im Wortlaut
2. **Der eine Satz** – was der Call am Fall verändert hat
3. **Key Metrics (Call N)** – Tabelle `Metrik | Wert | Wer hat es gesagt`
4. **Was neu ist** gegenüber der Akte
5. **Was vom Call-Sheet drankam** – je Block: gefragt, beantwortet, ausgewichen, offen
6. **Entscheidungsbedingungen** aus der Contingency-Liste des Reports: welche erfüllt, welche nicht
7. **Hypothesen vor dem Call geprüft** – je Hypothese aus `00-prior.md` und den Lesarten: bestätigt,
   widerlegt, offen
8. **Analyse** als nummerierte Thesen, jede als Behauptung formuliert („Die Integration trennt sie von
   A, nicht von B“), darunter der Beleg aus dem Call und aus der Akte
9. **Die Angaben der Gegenseite, gegen die Akte gehalten** – Widersprüche mit Fundstelle
10. **Wirtschaftlichkeit in vier Fragen:** Fliegt der Fall? Rechnet er sich? Wie viel Geld lässt sich
    damit verdienen? Wie lange dauert es, bis Geld fließt? Jeweils mit Rechenweg und
    `Stand: Outside-In`, solange kein Data Room vorliegt. Bei bekannter Runde: Fondsrechnung zum
    aufgerufenen Preis
11. **Investoren und Spuren** – jede neue Spur auch als ❗-Zeile im Chat
12. **Im Data Room prüfen, sonst schriftlich**
13. **Was wir gesagt und zugesagt haben** (Intros, Unterlagen, Termine)
14. **Nächste Schritte**

Zwei Prüfgriffe, die regelmäßig treffen:

- **Reduziert ein Gründer im Call seinen eigenen Außenclaim**, ist das kein Charaktersignal,
  sondern ein Rechentest: trägt der reduzierte Claim den Fall noch? Erst die Vergleichsrechnung neu
  führen, dann die Ehrlichkeit würdigen
- **Mündliche Stände und zitierte Präzedenzfälle** gegen die Quelle halten, bevor sie in eine Notiz
  oder einen Außentext gehen. Ist die Quelle nicht greifbar, als mündlich markieren. Ein Name, den
  die Gegenseite nachschlagen kann, muss belegt sein

## 3. Danach

- **Einschätzung im Chat**: drei bis fünf Sätze, was sich an der Conviction ändert und warum
- `CLAUDE.md`: eine Zeile `Call N (Datum): …` im Startup-Kontext, Workflow-Status, Conviction und
  Top-5-Risiken **überschreiben**, nicht anhängen
- **Follow-up-Entwurf**: Dank in einem Satz, die zugesagten Unterlagen anfragen, **offene
  Gate-Fragen (Runde, Bewertung, Instrument, Lead, Cap Table) als eigener Absatz**, reine
  Auskunftsfragen dazu. Vor dem Schreiben den Verlauf im Postfach lesen, auch die gesendeten Mails;
  Sprache der letzten Nachricht der Gegenseite. Nie selbst versenden; der Volltext steht im Chat
- **Intros**, die im Call zugesagt wurden, als eigene Entwürfe
- Haken `nach-call` der Haus-Schicht

## 4. Spätere Mails der Gegenseite

Ein Update der Gründer wird **zuerst gegen den Mailthread desselben Absenders** gehalten, dann gegen
die Akte: den Thread von hinten lesen, jede Zahl und jeden Namen gegen die letzte eigene Äußerung
des Absenders. Mehrere Abweichungen in dieselbe Richtung sind eine Eigenschaft der Quelle, kein
Zufall.

## 5. Referenzprotokolle für den Umlauf

Geht ein Referenzprotokoll an die Gründer, läuft es in deren Fundraising weiter. Dann wird **das
Unternehmen genannt, die Person nicht**: Name, Funktion und alles, was den Personenkreis verengt,
raus; wörtliche Zitate in indirekte Rede; Eingeständnisse über die eigene Sicherheits- oder
Betriebslage streichen; ein sichtbarer Hinweis im Dokument, was anonymisiert ist. Keine Freigabe
behaupten, die es nicht gibt.
