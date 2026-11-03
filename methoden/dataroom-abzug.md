# Data-Room-Abzug – Decks und Unterlagen hinter Links

Wie Unterlagen hinter DocSend-, Notion- oder Figma-Links vollständig und prüfbar in die Akte kommen.
Danach greift der Data-Room-Eingang (`dd.md`, Ende von Pfad A0) bzw. Pfad A.

**Grundsätze:** Anmelden macht der User selbst, nie wird eine Mailadresse in ein Formular getippt.
Abgezogen wird 1:1, mit Inventar (`sources/dataroom/00-inventar.md`: Datei, Seiten, Quelle,
Abrufdatum, Prüfsumme). Viele Viewer protokollieren jede Seite samt Sichtzeit für die Gründer – der
Abzug geschieht zügig und der Tab wird danach sofort geschlossen.

---

## DocSend

- Keine Textebene: jede Seite ist ein serverseitig gerendertes Bild
- Nach der Anmeldung im Seitenkontext `fetch(location.pathname + '/page_data/<n>')` → JSON mit
  `imageUrl`, `documentLinks` (Ziel-URLs der Links im Dokument), `documentMedia`. Die signierten
  Bild-URLs laufen nach wenigen Minuten ab: Bilder sofort holen und ablegen. Seite n+1 mit
  `AccessDenied` markiert das Ende; gegen „1 / N“ im Viewer prüfen
- **`Last-Modified` der Bilder zeigt den Upload der Fassung.** Hinter einem alten Link kann eine neue
  Fassung liegen – das Datum gehört ins Inventar
- Dateinamen und Metadaten gibt DocSend nicht aus; der Spuren-Scan bleibt leer, das ist zu vermerken
- Abschrift visuell, kleine Diagrammschrift vergrößert; eine OCR-Gegenprobe in beide Richtungen,
  jede Abweichung am Ausschnitt prüfen

## Öffentliche Notion-Seiten

- Ohne Login über die interne API lesbar (`loadPageChunk`). **Toggle-Inhalte fehlen im ersten Zug**:
  so lange `syncRecordValues` auf die fehlenden Block-IDs, bis keine mehr fehlt
- **HTML-Einbettungen haben oft zwei Fassungen** (`source` und `format.display_source`); die ältere
  mitnehmen – Unterschiede zwischen beiden sind ein Befund
- Anhänge nach der Anhangs-UUID benennen, nicht nach dem Präfix der Block-ID (Kollisionen)
- Interaktive Einbettungen über Quelltext und CSS lesen; Kommentare sind ohne Login gesperrt (nur
  Anker und Zahl der Threads erfassen)
- Google-Drive-Ordner: `drive.google.com/embeddedfolderview?id=…` für die Liste

## Figma-Decks ohne Edit-Zugriff

- Der Ansichtslink lässt sich vollständig lesen, auch wenn Design-Werkzeuge Edit-Rechte verlangen und
  Screenshots am Canvas hängen: die Checkpoint-Datei aus den Netzwerkressourcen der Seite laden
  (Signatur hält nur kurz) und den Text strukturiert auslesen
- **Ausgeblendete Folien** (`isSkippedSlide`) sind oft Vorversionen mit früheren Umsätzen, Preisen
  oder Zitaten. Sie sind eine **Spur, keine Aussage der Gründer**: ins Inventar und in den
  Spuren-Abschnitt, im Call nie zitieren

## Verträge und Konditionen

- **Konditionen nur aus der Urkunde.** Cap, pre oder post, Longstop, Pro-rata-Rechte werden erst
  gerechnet, wenn die unterzeichnete Fassung gelesen ist. Gesprächsnotizen und Mails unterscheiden
  pre und post nicht verlässlich
- Liegen Verträge nur als Anhang in einem CRM oder Wiki, lesend über dessen API holen, in den
  Scratchpad laden und mit `pdftotext -layout` lesen
- Amendments und Side Letters gezielt suchen; sie stehen selten neben dem Hauptvertrag
