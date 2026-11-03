# Auftragsarten – wenn es keine Investment-DD ist

Default von `/dd` ist die Investment-DD (Pfad A0 oder A). In der Praxis kommen vier weitere
Auftragsarten vor, jede mit eigenem Output. Die Eingangs-Klassifikation in `dd.md` erkennt sie,
nennt sie in der Klassifikationszeile, und der Plan folgt dann dieser Datei statt der
Standardtabelle. Im Zweifel einmal fragen.

| Art | Erkennung | Output |
|---|---|---|
| Investigativ / Wettbewerb | Material kommt über eine Beteiligung oder einen Partner, die Gründer sind noch im Stealth oder bei alten Arbeitgebern, Auftrag „was können wir herausfinden“ | Dossier |
| Personen-Gespräch | eine Person statt einer Firma, „was macht er, woran baut sie“ | Personenprofil + Gesprächsfragen |
| Portfolio-Abgleich | „vergleich das mit X aus dem Portfolio“, „kannibalisieren sie sich“, „passt das zu X“ | Abgrenzung |
| Listen-Screening | Ordner oder Liste mit vielen One-Pagern, Event- oder Batch-Listen | Tabelle + kurze Liste (`/dd:screening`) |

**Erkennung aus dem Freitext.** Benennt der Freitext den Zweck („investigativ“, „vergleich das mit
unserer Beteiligung“, „was macht der Typ“, „welche soll ich mir anschauen“), bestimmt er die
Auftragsart. Nur ein Freitext, der keine Art benennt, ist Schwerpunkt innerhalb der Investment-DD.

**Mischformen:** die Hauptart nach dem Zweck wählen, die zweite als eigener Abschnitt im Output
(etwa ein Dossier mit Abschnitt „Abgrenzung zur Beteiligung“). Eine Zeile im Plan sagt, welche
Art führt.

**Was aus Pfad A0 für alle vier gilt:** Vorgeschichte prüfen · Plan zuerst, kurz, mit den
Schritten der jeweiligen Art statt der Standardtabelle · Spuren sofort als ❗-Zeile · Recherche nach
`outside-in-recherche.md` · Haken `nach-setup`. **Was nicht gilt:** die Standardtabelle, das
Marktbild mit drei Agents (ausser es trägt den Zweck), „Call-1-Sheet immer“ – Fragen gibt es nur
beim Personen-Gespräch.

**CLAUDE.md für diese Arten:** dieselbe Form wie in Pfad A, im Startup-Kontext die Zeile
`Auftragsart: <Art>`, in der Workflow-Tabelle die Schritte dieser Art. Ein späterer `/dd` im
selben Ordner liest die Auftragsart und bleibt in ihr – auch wenn inzwischen Unterlagen
im Ordner liegen –, bis der User daraus eine Investment-DD macht. Dann wird die Tabelle durch die
Standardtabelle von Pfad A0 ersetzt und das Bisherige als Quelle übernommen.

---

## 1. Investigativ / Wettbewerb

Zweck: einer Beteiligung oder einem Partner zeigen, wer da kommt und was das für sie heißt. Kein
Investmenturteil, kein Call-Sheet.

- Recherche nach `outside-in-recherche.md`, Schwerpunkt Personen (§5, Hintergrundprüfung) und
  Artefakte (§4): Wer sind die Leute, wo arbeiten sie noch, was haben sie vorher gebaut, was zeigen
  Domain, Register, Archiv, Patente, Stellenanzeigen
- **Perspektive des Empfängers:** Was ist für die Beteiligung relevant – überschneidende Kunden,
  Technik, Personal, Partner, Zeitplan. Auch Kleinigkeiten (Namensherkunft, frühere Projekte), wenn
  sie etwas erklären
- **Quellen als Fußnoten**, jede Aussage mit Belegstufe; Abgeleitetes als Ableitung kennzeichnen
- Die Herkunft des Materials (wer das Deck weitergeleitet hat) ist 🔒 und steht nur in der Akte
- **Ein weitergeleiteter Deck-Link protokolliert den Abruf.** DocSend und ähnliche Viewer zeigen den
  Gründern, wer wann geöffnet hat; das kann den Weiterleiter und unser Interesse offenlegen. Vor dem
  Öffnen den User fragen. Ohne Freigabe nur mit dem arbeiten, was als Datei vorliegt
- Ausgabe `report/dossier-<thema>-DATUM.md`; Format und Begleittext über Haken `memo` der Haus-Schicht

## 2. Personen-Gespräch

Zweck: ein offenes Gespräch mit jemandem, dessen Vorhaben noch unklar ist (früherer Gründer,
Stealth-Profil, Kontakt aus einem Netzwerk).

- **Personenprofil** `analysis/personenprofil-<name>.md` nach `outside-in-recherche.md` §5:
  Identität, Werdegang, frühere Firmen und deren Ausgang, eigene Aussagen mit Datum, was offen ist.
  Bei einem früheren Unternehmen der Person kurz auch dessen Stand (Runde, Markt, Wettbewerber)
- **Gesprächsfragen** `analysis/ddq-questions-<vorname>-gespraech.md` plus `-lesarten.md` nach
  `call-sheet.md` (Termin, Frage-Format, Satzregeln, Pool für die gebuchte Länge), Blockgerüst:
  Werdegang und was sie zuletzt gemacht hat · was jetzt entsteht · das Thema dahinter · wie wir
  helfen können. Kein Rundenblock, solange es keine Firma gibt
- Was die Person im Gespräch über frühere Firmen erzählt, nach `call-nachbereitung.md` §1 behandeln

## 3. Portfolio-Abgleich

Zweck: klären, wie ein Fall zu einer bestehenden Beteiligung steht.

- **Umfang:** eine kurze Übersicht der Firma (was sie bauen, wer dahinter steht, wo sie stehen – die
  Punkte 1–4 der Lesefassung in wenigen Sätzen), dann die Abgrenzung. Register und Team nur in
  Stammdaten, Website-Artefakte nur so weit, wie sie den Produktumfang zeigen
- Ausgabe `analysis/<beteiligung>-abgrenzung.md`: was beide tun (je ein Satz) · Gemeinsamkeiten ·
  Unterschiede in Käufer, Produkt, Technik, Geschäftsmodell · **Kannibalisierung**: konkurrieren sie
  um dieselben Kunden oder dasselbe Budget, heute oder absehbar · **Chancen**: Kunde, Lieferant,
  Partner, Intro in eine Richtung oder beide · offene Fragen an beide Seiten
- **Eine Überschneidung ist ein Vermerk, kein Filter.** Die Entscheidung trifft der User
- Was über die Beteiligung intern bekannt ist, bleibt intern; Intro-Entwürfe nur auf Auftrag

## 4. Listen-Screening (`/dd:screening`)

Zweck: aus einer langen Liste schnell die Firmen finden, die ein Gespräch lohnen. **Dieser Lauf ist
der erste Screening-Layer – er zeigt alles**, sortiert und begründet, und filtert nicht still aus.

- **Eingang:** Ordner mit One-Pagern, PDF-Tabellen mit Links, Event-Exporte. Links in PDFs als
  Annotationen mitnehmen (Website, Deck)
- **Raster:** A = sprechen, B = prüfen (eine entscheidende Tatsache fehlt oder widerspricht sich),
  C = kein Fit, immer mit Ausstiegsgrund. Gewichtet werden **thematische Passung und Gründerprofil**;
  das technische Asset ergänzt. **Umsatz ist kein Kriterium**, nur Plausibilitätsprüfung der
  Selbstauskunft; widerlegte Angaben zählen als Gründersignal
- **Gründerprofil mit Quelle** bewerten, nicht aus dem Bauch: Domänentiefe und Käuferkenntnis ·
  technische Tiefe · Team vollständig (technisch und kommerziell in Vollzeit) · Track Record ·
  decken sich Angaben und Quellen. Fehlt die Quelle, steht „unbelegt“
- **Gates statt Gewichte:** Region bzw. Mandat und Fondsmechanik (Ticket, Bewertungsrahmen aus Haken
  `fondsparameter`). Thesen und ein hauseigenes Raster aus der Haus-Datei, falls vorhanden
- **Portfolio-Überschneidung** steht als Info-Zeile bei der Firma; die Firma bleibt in der Liste.
  Laufende Prüffälle sind keine Beteiligungen
- **Tiefe:** ein schneller Filter je Liste, kein Voll-Screening. Je Firma Website und ein, zwei
  Primärquellen, keine Anfragewellen
- **Ausgabe:** im Chat zuerst die kurze A-Liste mit je einem Satz, warum; dann die Gesamtliste als
  Notiz (`<ordner>/screening-DATUM.md`) mit Urteil, Grund und Quelle je Firma
