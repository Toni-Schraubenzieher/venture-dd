# Investoren und Spuren – wer ist dabei, wer prüft gerade, wer steht dahinter

Diese Datei definiert zwei Dinge, die in jeder DD mitlaufen: das **Inventar, wer schon investiert
ist**, und den **Spuren-Scan**, der zeigt, wer gerade prüft oder im Hintergrund steht – auch wenn
der Gründer es nicht sagt.

**Wann:** Spuren-Scan beim ersten Data-Room-Scan (Pfad A, Schritt 1) und bei jeder neuen Datei.
Inventar in Session 2. Spuren außerhalb des Data Rooms in jeder Recherche-Phase.
**Wohin:** Sofort als ❗-Zeile in den Chat, dann in den Abschnitt `## Investoren und Spuren` der
Investments-Extraktion und in die „Runde“-Zeile der Deal-`CLAUDE.md`.

---

## Warum das existiert

Gründer nennen im Erstgespräch selten den Lead, fast nie die Bewertung und oft nicht alle
Vorinvestoren. Die Dokumente, die sie teilen, wissen mehr. Office-Dateien tragen Kommentare,
Autoren, Änderungsverfolgung und versteckte Blätter mit, die beim Lesen über `textutil` oder
`openpyxl(data_only=True)` **unsichtbar bleiben** – genau der Weg, den dieser Workflow für den
Inhalt vorschreibt. Der Scan muss deshalb separat laufen.

Anlass (Herbst 2026, Seed-Fall): In der Cap Table eines Data Rooms stand ein nicht gelöschter
Kommentar-Thread aus dem Gastkonto eines Fonds, mit Fragen zu Gründeranteilen und Mitarbeiterpool,
und eine Pricing-Datei trug das Kürzel desselben Fonds im Namen. Beides deutete auf den Lead der
Runde, den der Gründer im Gespräch nicht genannt hatte. Der Fund stand drei Tage nur in den
Notizen; der Partner erfuhr erst auf Nachfrage davon.

## 1. Inventar „Wer ist schon dabei“

Pflichttabelle in der Investments-Extraktion, auch wenn sie nur die Gründer enthält:

| Investor | Instrument | Betrag | Bewertung/Cap | Datum | Quelle | Belegstufe |
|---|---|---|---|---|---|---|

Quellen, in dieser Reihenfolge abfragen:
- **Register:** Gesellschafterliste, Gründungs- und Kapitalerhöhungsurkunden (DE), SH01 und PSC (UK),
  Transparenzregister. Wandeldarlehen und SAFEs erscheinen dort erst bei Wandlung – ein leeres
  Register heißt nicht „keine Investoren“.
- **Data Room:** Cap Table, CLAs, SAFEs, Side Letter, Board-Protokolle, Investor Updates.
- **Gründer:** Deck, Call, Mails.
- **Fonds-Seiten:** Portfolio-Listen und Jobboards (Getro-Boards der Fonds führen Portfoliofirmen oft
  vor der Ankündigung).
- **Öffentlich:** Pressemeldungen, LinkedIn-Posts von Fonds und Angels („excited to back“),
  Lobbyregister (Finanzierung, Auftraggeber), Förderdatenbanken (CORDIS, EXIST, Landesprogramme).

Belegstufe je Zeile: Register/Vertrag = Beleg, Cap Table/Deck = Selbstauskunft, Spur = Lesart.

## 2. Spuren-Scan im Data Room

Was gesucht wird:

| Dateityp | Spur |
|---|---|
| XLSX | `xl/comments*`, `xl/threadedComments/*` (Thread mit Zeitstempel), `xl/persons/person.xml` (Anzeigename, `userId` mit Mail-Domain – zeigt Gastkonten), versteckte Blätter (`state="hidden"`/`veryHidden`), `definedNames`, `xl/externalLinks` (Pfade zu fremden Ordnern und Tenants) |
| DOCX | `word/comments.xml`, `word/people.xml`, Autoren der Änderungsverfolgung (`w:ins`/`w:del`) |
| PPTX | `ppt/comments/*`, `ppt/commentAuthors.xml`, Sprechernotizen, versteckte Folien (`show="0"`) |
| Office allgemein | `docProps/core.xml` (`creator`, `lastModifiedBy`, Zeitstempel), `docProps/app.xml` (`Company`, `Manager`) |
| PDF | `pdfinfo`: Author, Creator, Producer, Title, Erstellungsdatum |
| Alles | Datei- und Ordnernamen (Investor-Kürzel, „v2_for_…“, „Fundraising – Seed Round“), Freigabe-Mails (Tenant-Name, Einladender, Gastkonten), Screenshots (Browser-Tabs, Kanalnamen, Benachrichtigungen) |

Das Skript liest nur, schreibt nichts und braucht nur die Standardbibliothek plus `pdfinfo`. In den
Session-Scratchpad schreiben (nicht in den Data Room) und mit `python3 -I <skript> "<Data-Room-Ordner>"`
ausführen:

```python
import pathlib, re, subprocess, sys, zipfile

ROOT = pathlib.Path(sys.argv[1])
SPUR = re.compile(r"docProps/(core|app)\.xml|comments|threadedComments/|persons/|people\.xml|"
                  r"commentAuthors|externalLinks/.*\.rels|notesSlides/notesSlide\d+\.xml|"
                  r"xl/workbook\.xml|ppt/presentation\.xml|ppt/slides/slide\d+\.xml")
FELD = re.compile(r"<(dc:creator|cp:lastModifiedBy|dc:title|Company|Manager|dcterms:created|dcterms:modified)[^>]*>([^<]+)<")
MAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")


def text(xml):
    return " ".join(t for t in re.findall(r">([^<>]+)<", xml) if t.strip())


def office(f):
    z = zipfile.ZipFile(f)
    for n in sorted(x for x in z.namelist() if SPUR.search(x) and not x.endswith(".vml")):
        x = z.read(n).decode("utf-8", "replace")
        if n.startswith("docProps/"):
            for k, v in FELD.findall(x):
                if v.strip():
                    print(f"  {n}: {k} = {v.strip()}")
        elif n == "xl/workbook.xml":
            for s in re.findall(r"<sheet [^>]*state=\"(?:hidden|veryHidden)\"[^>]*>", x):
                print(f"  verstecktes Blatt: {s}")
            for d in re.findall(r"<definedName [^>]*name=\"([^\"]+)\"", x):
                print(f"  definedName: {d}")
        elif n == "ppt/presentation.xml" or n.startswith("ppt/slides/"):
            if 'show="0"' in x:
                print(f"  versteckte Folie: {n}")
        elif "externalLinks" in n:
            for t in re.findall(r"Target=\"([^\"]+)\"", x):
                print(f"  externer Link: {t}")
        elif "persons/" in n or n.endswith("people.xml") or "commentAuthors" in n:
            for a in re.findall(r"<[^>]*(?:displayName|w15:author|name)=\"[^\"]*\"[^>]*>", x):
                print(f"  Person: {a}")
        else:
            autoren = sorted(set(re.findall(r"(?:w:author|author)=\"([^\"]+)\"|<author>([^<]+)</author>", x)))
            autoren = sorted({a or b for a, b in autoren})
            print(f"  {n}: Autoren {autoren} | {text(x)[:400]}")
    if f.suffix.lower() == ".docx":
        doc = z.read("word/document.xml").decode("utf-8", "replace")
        aend = re.findall(r"<w:(ins|del) [^>]*w:author=\"([^\"]+)\"", doc)
        if aend:
            print(f"  Aenderungsverfolgung: {len(aend)} Stellen, Autoren {sorted(set(a for _, a in aend))}")
    alles = " ".join(z.read(n).decode("utf-8", "replace") for n in z.namelist() if n.endswith((".xml", ".rels")))
    mails = sorted(set(MAIL.findall(alles)))
    if mails:
        print(f"  Mailadressen: {mails}")


for f in sorted(p for p in ROOT.rglob("*") if p.is_file()):
    print(f"== {f.relative_to(ROOT)}")
    s = f.suffix.lower()
    try:
        if s in (".xlsx", ".xlsm", ".docx", ".pptx"):
            office(f)
        elif s == ".pdf":
            out = subprocess.run(["pdfinfo", str(f)], capture_output=True, text=True).stdout
            for z in out.splitlines():
                if z.split(":")[0] in ("Title", "Author", "Creator", "Producer", "CreationDate", "ModDate"):
                    print(f"  {z}")
    except Exception as e:
        print(f"  nicht lesbar: {e}")
```

Die Ausgabe ist roh. Relevant ist alles, was auf eine **Person oder Organisation außerhalb des
Gründerteams** zeigt: fremde Mail-Domains, Gastkonten, Kommentarautoren, Kürzel in Dateinamen,
Firmen in `Company`, Pfade in externen Links. Gründer-Autoren und Software-Producer sind Rauschen,
außer sie widersprechen der Erzählung (Dokument vor der Gründung, auf dem Rechner eines früheren
Arbeitgebers).

## 3. Spuren außerhalb des Data Rooms

- Website: Logos „backed by“, JSON-LD, Footer; ältere Stände über Wayback (verschwundene
  Investorenlogos sind ein Befund).
- LinkedIn: Posts von Fonds und Angels, Teammitglieder mit Fondshintergrund, Beiräte.
- Mail und Kalender: Absender-Domains (alte Firmennamen, Holding-Domains), CC-Listen in
  Weiterleitungen, Tenant-Namen in Freigabe-Einladungen.
- PDFs von der Website: Metadaten wie oben.

## 4. Meldung und Ablage

**Sofort im Chat**, in der Antwort, in der die Spur gefunden wurde – nicht erst am Session-Ende:

```
❗ <Fund> – <Fundort: Datei, Zelle, Zeitstempel> – <was es nahelegt> – Beleg | Lesart
```

Mehrere Funde stehen gesammelt **oben** in der Antwort. Das gilt in jeder Phase: Data Room,
Register, Web, Ingest, Mails.

**In der Akte:** Abschnitt `## Investoren und Spuren` in der Investments-Extraktion:

| Spur | Fundort | Wortlaut/Wert | Lesart | Belegstufe | gemeldet am |
|---|---|---|---|---|---|

Dazu die Investorenliste in der „Runde“-Zeile der Deal-`CLAUDE.md`, mit „nach Aktenlage“ für alles,
was nur aus Spuren kommt.

## 5. Grenzen

- **Eine Spur ist eine Lesart, kein Beleg.** Ein Gastkonto zeigt, dass jemand geprüft hat, nicht,
  wer führt. Formulierung: „nach Aktenlage wahrscheinlich“.
- **Im Call als geschlossene Frage.** Ob die Spur selbst genannt wird, entscheidet der Partner.
  Metadaten, die auf ein Fehlverhalten deuten (Dokument vom Rechner des früheren Arbeitgebers),
  werden nie offengelegt – gefragt wird nur nach dem Sachverhalt.
- **Vertraulich.** Investorennamen aus Spuren fallen unter das Confidentiality-Gate (Absage-Standard)
  und gehen in kein Dokument, das das Haus verlässt.
- **❗ nur im Chat und in Arbeitsdateien.** In Außendokumenten gilt weiter: keine Emoji.
- **Nichts verändern.** Der Scan liest; Dateien im Data Room werden nicht geöffnet, gespeichert oder
  verschoben.
