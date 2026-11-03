# Outside-In-Recherche – Fälle ohne Data Room

Methode für Pfad A0 (`dd.md`), für die Hintergrundprüfung von Gründern und für die
Auftragsarten „Investigativ“ und „Personen-Gespräch“ (`auftragsarten.md`). Ziel ist ein belastbarer
Wissensstand vor Call 1 aus Quellen, die ohne Login und ohne Kosten erreichbar sind.

**Grundsatz:** Register und Primärquellen vor Suchmaschine. Suchmaschinen sind für Agents
weitgehend dicht oder liefern Rauschen; Register liefern Umsatz, Verlust, Kapital und Gerichtsakten,
die in keinem Presseartikel stehen. **Login-, Captcha- und Bot-Sperren werden nicht umgangen** –
was dahinter liegt, wird eine Frage an den User (Link, Screenshot, eingeloggter Browser) oder eine
Call-Frage.

---

## 1. Vorgeschichte zuerst

Bevor ein „neuer“ Fall aufgesetzt wird: Ablage bzw. Vault, CRM und Mail **inklusive Gesendet**
nach Firmenname, alter und neuer Domain und Gründernamen durchsuchen. Das Ergebnis ist die erste
Zeile der Antwort an den User, vor jedem Plan.

- Eine frühere Absage oder ein früherer Kontakt ändert die Leitfrage des ganzen Falls: nicht mehr
  „was ist das“, sondern „hebt das, was sich seither geändert hat, die damalige Begründung auf“.
  Der Wortlaut kommt als Quellennotiz in die Akte, Report und Briefing prüfen ihn Punkt für Punkt
- Anhänge früherer Mails (Decks) sind oft die einzigen Unterlagen, auch wenn „kein Deck“ gesagt wurde
- Namen wechseln: Rebranding, Domainumzug, Parallelfirmen der Gründer

## 2. Marktbild vor dem Plan

Zwei Fragen müssen beantwortet sein, bevor ein Plan steht:

- **Wer baut so etwas auch?** Direkte Startups und Scale-ups, die Kategorie-Welle, Konzerne und
  Plattformen mit Feature-Risiko, andere Technologien für denselben Job
- **Wer ist grundsätzlich interessiert?** Käufer mit Budgettopf und zählbarer Zahl, Kanäle
  (Integratoren, Beratungen), strategische Käufer mit M&A-Belegen – also wer es übernehmen würde

Dazu: **Warum jetzt?** Was im Markt sich gerade ändert und den Fall möglich macht.

Ausgabe kompakt im Chat, mit Tabelle der direkten Wettbewerber (Name, Ort, Finanzierung, was
gleich, was anders). Drei Recherche-Agents parallel: Startups · Konzerne und M&A · Käuferseite.
Später nach `analysis/research-notes.md` und `analysis/themen-primer.md` übertragen.

**Das WebSearch-Budget gilt für die ganze Session, alle Subagents zusammen.** Fünf parallele Agents
können es in zehn Minuten aufbrauchen. Deshalb nur einem Agent die Breitensuche geben, die anderen
von Anfang an auf Register und Primärquellen setzen. Patentdatenbanken drosseln bei parallelen
Abfragen ebenfalls; Patentprüfung einem einzigen Agent geben.

## 3. Register und Rechtsträger (ohne Key, per `curl`)

| Land | Endpunkt | liefert |
|---|---|---|
| FR | `https://recherche-entreprises.api.gouv.fr/search?q=<SIREN\|Name>` | SIREN, Gründung, Rechtsform, NAF, Beschäftigtenklasse, Sitz, Dirigeanten **mit Geburtsmonat**, letztes Jahresergebnis (`finances`). Findet auch Firmen, die eine Websuche noch nicht kennt |
| FR | `https://data.economie.gouv.fr/api/records/1.0/search/?dataset=ratios_inpi_bce&q=siren:<SIREN>` | Jahresergebnis je Geschäftsjahr, rund zehn Jahre |
| FR | `https://bodacc-datadila.opendatasoft.com/api/records/1.0/search/?dataset=annonces-commerciales&q=<SIREN>` | Insolvenz- und Gerichtsakten, vertraulich hinterlegte Abschlüsse |
| UK | `https://find-and-update.company-information.service.gov.uk/company/<nr>` und Filing History | Status, Directors, PSC, **SH01**, Articles, Resolutions, Insolvenzakten |
| NO | `https://data.brreg.no/enhetsregisteret/api/enheter/<orgnr>` und `…/roller`; Bekanntmachungen `https://w2.brreg.no/kunngjoring/hent_nr.jsp?orgnr=<orgnr>` | Kapital, Satzung, Rollen. **Falle:** `sistEndret` an einer Rollengruppe ist die letzte Änderung der Gruppe, nicht der Rollenbeginn – den zeigen erst die Bekanntmachungen |
| FI | `https://avoindata.prh.fi/opendata-ytj-api/v3/companies?name=<Name>` | Stammdaten und alle Parallelnamen; Abschlüsse nicht über die API |
| BE | `kbopub.economie.fgov.be` | Stammdaten |
| DE | Handelsregister, chronologischer Abdruck | Gesellschafter, Kapital, auch gelöschte Blätter |
| PT | `publicacoes.mj.pt` (oft Captcha – dann als offen führen) | Gründung, Gesellschafter, Gerentes |
| US/Delaware | kein offener Weg | – |
| EU-Förderung | `https://cordis.europa.eu/search/en?q=<query>&format=json` | Projekt, Call, EC-Beitrag je Organisation – verifiziert Grant-Behauptungen auf den Euro |
| Patente | `https://patents.google.com/xhr/query?url=q%3D%22<begriff>%22` | Inhaber, Erfinder, Prioritäten, **Familie nach Ländern** – die Reichweite der Familie zeigt, wohin das Budget und damit die Überzeugung geht |
| Literatur | `https://api.openalex.org/works?search=…` | Publikationen, frei lesbare Fassungen |

Hinweise:

- **Der Geburtsmonat eines Geschäftsführers ist der Identitätsbeleg** gegen Namensvettern, gehalten
  gegen öffentliche Altersangaben
- System-Python hat oft kein CA-Bundle: mit `curl` holen, mit Python nur parsen
- Ein Register zeigt keine Domain; die Brücke von Firma zu Website läuft über die Person

### UK: die Runde aus dem SH01

Das SH01 (Return of Allotment) nennt Stückzahl, Aktienklasse und den **gezahlten Betrag je Aktie**:

```
Rundengröße   = Stück(neu) × Preis je Aktie
Pre-Money     = Stück(alt) × Preis je Aktie
Post-Money    = Stück(gesamt) × Preis je Aktie
Verwässerung  = Stück(neu) / Stück(gesamt)
```

- Den Preis zusätzlich gegen die **voll verwässerte Basis** rechnen (Gründeraktien plus der in den
  Resolutions ermächtigte Optionsrahmen) – so zeigt sich, ob die Runde inklusive Pool bepreist war
- **Articles lesen**, auch als Bild-PDF: Definitionen wie „Lead Investor“ oder „Investor Majority“
  nennen Investoren, die das SH01 nicht nennt
- Läuft die Runde noch, zeigen die **Written Resolutions** (s.-551-Ermächtigungen) Obergrenzen für
  Wandlung und Pool
- Grenzen: Wandeldarlehen und SAFEs erscheinen erst bei Wandlung
- **Vor Call 1 rechnen, nicht vorab nennen**, im Gespräch gegen die Angabe der Gründer halten

### UK: „previously acquired“

Sagt ein Gründer, die Vorfirma sei übernommen worden, die Filing History der Vorfirma lesen – die
Dokumente selbst. **AM02** (Statement of Affairs) und **AM03** (Administrator's Proposals) sind
Bild-PDFs ohne Textebene; mit dem Read-Werkzeug seitenweise lesen. Darin: Umsatz- und
Verlusthistorie, Chronologie des Scheiterns, Erlöse, Gläubiger, Gesellschafterliste. **Die Zahlen
bleiben interne Akte**; im Gespräch wird daraus eine Frage nach der Lehre, kein Vorhalt. Mitlesen,
was entlastet (Käufer ohne Verbindung, Pflichtformeln).

## 4. Website und öffentliche Artefakte

Belastbar für „was gebaut ist“, **nie für „was verkauft ist“**. Im Call wird nur zitiert, was die
Firma selbst offen zeigt (Website, Datenschutz, Subprozessoren, LinkedIn, Register); der Rest wird
offene Frage und steht in den Lesarten unter „nicht zitieren“.

- **Zertifikatslog** `crt.sh/?q=<domain>&output=json`: erstes Ausstellungsdatum je Subdomain ergibt
  die Bauchronik (app, api, docs, auth, admin; Wildcards deuten auf Mandanten)
- **Routen-Manifest und Bundles** einer Web-App (`/assets/manifest-*.js` u. ä.): Funktionsumfang,
  UI-Texte im Wortlaut, Demo-Szenarien – ohne API-Aufrufe, ohne Login
- **Subprozessorliste, DPA, Datenschutz, AGB** im Volltext: Stack, Hosting-Regionen, Vertragsformen
- **JSON-LD im HTML**, `sitemap.xml`-lastmod, HTML-Kommentare (nie zitieren)
- **Wayback-CDX** `web.archive.org/cdx/search/cdx?url=<domain>/*&filter=statuscode:200&collapse=urlkey`:
  frühere Positionierung, Team-Seiten, Logos, gestrichene Meldungen. Nach einem Domainwechsel ist
  die **alte Domain** am ergiebigsten. Das Archiv ist offen nennbar („on your earlier website I read …“)
- **GitHub-API** für verlinkte Repositories und PRs: Anlagedatum, Status, Reviews gegen
  Blog-Behauptungen halten
- `llms.txt`, `openapi.json`, Hugging-Face-Organisationen, Paketregister
- DNS und Whois nur als Kontext (Domain-Alter, Mail-Setup), nie im Call

## 5. Personen

- **LinkedIn über Playwright ohne Login:** Profil öffnen und das JSON-LD lesen
  (`script[type="application/ld+json"]`): Post-Volltexte mit Datum, `worksFor`, `alumniOf`,
  Publikationen. Gesperrte Felder sind zeichengenau maskiert; die Wortlängen erlauben eine
  Rekonstruktion, **die aber nur als Frage ins Sheet geht**. Logo-Dateinamen im HTML können maskierte
  Arbeitgeber auflösen. Der erste Aufruf ist oft der einzige, der durchkommt: die wichtigste Person
  zuerst, das Ergebnis sofort vollständig auswerten. Läuft das Profil in die Anmeldeschranke, den
  User um Link, Screenshot oder seinen eingeloggten Browser bitten – sonst wird der Werdegang eine
  Call-Frage
- **Identität gegen ein zweites Merkmal halten** (Ort, Arbeitgeber, Geburtsmonat aus dem Register,
  Publikation). Namensvettern sind häufiger als gedacht
- **ORCID** für Promotions- und Anstellungsstatus (Affiliation ohne Enddatum = noch dort; wichtig
  für IP-Fragen bei Ausgründungen)
- **Video-Interviews** mit automatischen Untertiteln: oft die einzige Quelle für Runde, Kundenzahl,
  Bootstrapping. Untertitel sind Spracherkennung – Wortlaut mit Zeitmarke, als Selbstangabe führen
- **Metadaten archivierter PDFs** (`pdfinfo`): Autor und Verzeichnis zeigen, auf welchem Rechner ein
  Dokument entstand. Eine Ableitung, kein Befund – im Call höchstens die Frage nach dem Austrittsdatum
- Öffentliche Speaker-Bios, Accelerator- und Programmprofile, Konferenzseiten

### Hintergrundprüfung (eigener Ablauf, auf Auftrag)

Für jede Person: Identität (zwei Merkmale) · Werdegang gegen Register, Publikationen und Archiv ·
frühere Firmen mit Status und Ausgang (Register, Insolvenzakten) · Beteiligungen und
Parallelfirmen · öffentliche Auftritte und eigene Aussagen mit Datum · Namensvarianten und
Schreibweisen · was offen bleibt, als Frage. Ausgabe `analysis/hintergrundpruefung-DATUM.md`, jede
Zeile mit Quelle und Belegstufe. Persönliches ohne Bezug zum Fall bleibt draußen.

## 6. Bewertungsregeln

- **Recherche-Geografie folgt Käufermarkt und Mandat.** Quellen aus Ländern ohne Bezug zum Fall nur
  als Kontextzeile
- **Mehrfach zitiert heißt nicht mehrfach belegt.** Eine Marktzahl bis zum Ursprung zurückverfolgen:
  benannter Autor, Methodik und Stichprobe, verdient der Herausgeber am Ergebnis? Fällt eines aus,
  streichen oder auf die Größenordnung zurückschneiden und die Quellenkritik in der Datei
  festhalten, aus der die Zahl sonst weiterwandert
- **Nicht auffindbar ist ein Befund, mit Datum** – „im Register am TT.MM. nicht gefunden“, nie
  „unbelegt“ oder „existiert nicht“. Eine erfolglose Suche ist keine Gegenidentität
- **Eine Gesellschafterliste ohne Fremde heißt nicht „kein externer Investor“**: Wandler und SAFEs
  stehen dort nicht. Der Vorbehalt reicht durch jede Verdichtung (Key Metrics, CLAUDE.md, Chat)
- **Ein öffentlich unsichtbarer Lead** ist bei Pre-Seed und Seed normal, kein Widerspruch – Spur
  melden, neutral fragen
- **Programmbedingungen prüfen**, bevor ein leeres Register als Warnsignal gelesen wird (manche
  Programme verlangen, dass noch kein Rechtsträger existiert)
- **Outside-In-Rechnungen sind vorläufig:** Kopfzeile `Stand: Outside-In, revisionsbedürftig`, die
  fehlenden Inputs, „Was diese Rechnung kippen würde“; fortschreiben, nicht überschreiben; im Call
  als Frage
- **Agent-Befunde stichprobenartig gegen die Primärquelle prüfen** und das Ergebnis vermerken
  („29 Aussagen nachgeprüft, 2 korrigiert“)

## 7. Werkzeug-Hygiene

- **Der Playwright-Browser ist ein Browser für alle.** Läuft eine eingeloggte Sitzung (Deck, Data
  Room), bekommen parallele Recherche-Agents im Prompt „keine Playwright-Werkzeuge, nur WebFetch,
  WebSearch, curl“. Login-pflichtige Abzüge zuerst, dann die Agents
- Rohdateien aus dem Netz in einen eigenen leeren Ordner im Scratchpad, Python darauf nur mit `-I`
