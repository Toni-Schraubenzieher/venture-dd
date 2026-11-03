#!/usr/bin/env python3
"""Formpruefung fuer vorlesbare Call-Sheets (/dd, methoden/call-sheet.md §11).

Aufruf:
    python3 -I check-call-sheet.py <sheet.md> [--exclusions exclusion-rules.md] [--call 1]

Prueft nur die Form, nicht den Inhalt:
  1. vor jeder fetten Frage eine Einleitung mit Herkunftsmarker in erster Person
  2. kein Satz mit dem Dokument als Subjekt ("Slide 6 says", "Your deck shows")
  3. Saetze ueber 25 Woerter (die fuenf laengsten werden immer gezeigt)
  4. Gedankenstrich und Semikolon im Vorlesetext
  5. Ziffernbetraege ausserhalb von "Numbers to hand"
  6. Pronomen fuer Dritte (englische Sheets)
  7. Verbotsliste: Metasaetze, Beteuerungen, Uebergabesaetze
  8. Begriffe aus exclusion-rules.md (vertrauliche Quellen)
  9. mit --call 1: Pflichtabschnitte vorhanden

Exit-Code 1 bei mindestens einem Treffer der Klassen 1, 2, 4, 5, 7, 8, 9; sonst 0.
Nur Standardbibliothek. Liest keine Dateien ausser den uebergebenen.
"""
import argparse
import re
import sys

ORIGIN_EN = re.compile(
    r"\b(I|I'm|I've|I'd|my|me|we|We|we've|our|us|You wrote|you wrote|You said|you said|"
    r"You told|you told|You mentioned|you mentioned|On our|on our|In our|in our)\b"
)
ORIGIN_DE = re.compile(
    r"\b(ich|Ich|mir|mich|mein|meine|wir|Wir|uns|unser|unsere|Du hast|du hast|Sie haben|"
    r"ihr habt|Ihr habt|Im ersten|im ersten|In unserem|in unserem)\b"
)
DOC_SUBJECT = re.compile(
    r"((^|[.!?]\s+)(Slide \d+|Your deck|The deck|Your website|The website|Your site|"
    r"Companies House|The register|Your one-pager|Folie \d+|Das Deck|Euer Deck|Ihr Deck|"
    r"Eure Website|Ihre Website|Die Website|Das Register|Das Handelsregister)\b)|"
    r"(\b(your|the) (deck|website|site|one-pager|slide|register) (says|shows|lists|states|claims|adds|covers)\b)",
    re.I,
)
ORIGIN_2ND = re.compile(
    r"\b(on|in|from) (your|the) (website|site|deck|post|blog|slide|page|paper|profile|one-pager)\b|"
    r"\byou (posted|showed|write|shared|published|announced|presented)\b|"
    r"\b(auf|in|aus) (eurer|eurem|ihrer|ihrem|der|dem) (Website|Seite|Deck|Folie|Post|Profil)\b",
    re.I,
)
AMOUNT = re.compile(
    r"([£$€]\s?\d)|(\b\d+([.,]\d+)?\s?(k|K|m|M|bn|Mio\.?|Mrd\.?)\b)|(\b\d{1,3}([.,]\d{3})+\b)"
)
PRONOUNS_EN = re.compile(r"\b(he|she|his|her|him|hers|himself|herself)\b", re.I)
FORBIDDEN = [
    "honestly", "to be honest", "for what it's worth", "frankly", "just asking",
    "ehrlich gesagt", "ich frage nur", "um ehrlich zu sein",
    "stop me", "out of nowhere", "aus dem nichts", "none of my questions",
    "quick word on why", "kurz, warum", "not by accident",
    "that's our view going in", "now i'd like yours", "let me tell you how we see",
    "i'd rather be corrected", "als freund der these", "as a friend of the thesis",
    "i don't want to catch you out", "ich will dich nicht", "so most of my questions",
    "i have to ask a critical question", "kritische frage stellen",
]
REQUIRED_CALL1 = [
    ("If asked / Opening", r"if asked|opening|how i read the case|wie ich den case"),
    ("Gap", r"gap|lücke|luecke"),
    ("Product", r"product|produkt"),
    ("Technology", r"technolog|technik|integration"),
    ("Who wants this", r"who wants|customers|market access|kunden|marktzugang|wer will"),
    ("Pricing", r"pric|preis"),
    ("Who else builds this", r"who else|competition|differentiation|wettbewerb|wer baut"),
    ("Vision", r"vision|rollout|ausrollen"),
    ("Company and round", r"round|runde|company and|gesellschaft"),
    ("Numbers to hand", r"numbers to hand|zahlen zur hand"),
]


def strip_frontmatter(lines):
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return lines[i + 1:], i + 1
    return lines, 0


def sentences(text):
    text = re.sub(r"\*\*", "", text)
    text = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ\"„“(])", text)
    return [p.strip() for p in parts if p.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sheet")
    ap.add_argument("--exclusions")
    ap.add_argument("--call", type=int)
    ap.add_argument("--max-words", type=int, default=25)
    a = ap.parse_args()

    raw = open(a.sheet, encoding="utf-8").read().splitlines()
    lines, offset = strip_frontmatter(raw)

    hard, soft = [], []
    headings = []
    section = ""
    seen_first_h2 = False
    body = []  # (lineno, text) des Vorlesetexts
    for i, ln in enumerate(lines, start=offset + 1):
        s = ln.strip()
        if s.startswith("#"):
            headings.append(s.lstrip("#").strip())
            if s.startswith("## "):
                seen_first_h2 = True
                section = s[3:].strip().lower()
            continue
        if not seen_first_h2:  # Kopf: Termin- und Minutenzeile, Tagesablauf
            continue
        if not s or s.startswith("|") or s.startswith("```") or s.startswith(">"):
            continue
        if "numbers to hand" in section or "zahlen zur hand" in section:
            continue
        body.append((i, re.sub(r"^[-*]\s+", "", s)))

    text_all = " ".join(t for _, t in body)
    german = len(re.findall(r"\b(und|nicht|ist|der|die|das)\b", text_all)) > len(
        re.findall(r"\b(and|not|is|the)\b", text_all))
    origin = ORIGIN_DE if german else ORIGIN_EN

    # 1 Herkunft vor jeder fetten Frage
    prev = ""
    for i, t in body:
        for m in re.finditer(r"\*\*([^*]+?\?)\*\*", t):
            intro = t[:m.start()]
            intro = re.sub(r"^\*\*\d+(\.\d+)*\*\*\s*", "", intro).strip()
            if not intro:
                intro = prev
            if origin.search(intro):
                continue
            if ORIGIN_2ND.search(intro):
                soft.append((i, "Herkunft nicht in erster Person ('I read on your website …'): " + m.group(1)[:70]))
            else:
                hard.append((i, "Frage ohne Herkunft: " + m.group(1)[:80]))
        prev = t

    # 2 Dokument als Subjekt, 3 Satzlaenge, 4 Zeichen, 5 Betraege, 6 Pronomen, 7 Verbote
    lengths = []
    for i, t in body:
        if DOC_SUBJECT.search(re.sub(r"\*\*", "", t)):
            hard.append((i, "Dokument als Subjekt: " + t[:90]))
        for sn in sentences(t):
            n = len(re.findall(r"\b[\w'’-]+\b", sn))
            lengths.append((n, i, sn))
        if "—" in t or ";" in t or re.search(r"\s–\s", t):
            hard.append((i, "Gedankenstrich oder Semikolon: " + t[:90]))
        for m in AMOUNT.finditer(t):
            if re.fullmatch(r"\d+\.\d+", m.group(0)) and t.startswith("**"):
                continue  # Fragenummer
            hard.append((i, "Ziffernbetrag ausserhalb 'Numbers to hand': " + m.group(0)))
        if not german:
            for m in PRONOUNS_EN.finditer(re.sub(r"\*\*", "", t)):
                soft.append((i, "Pronomen fuer Dritte? '" + m.group(0) + "': " + t[:70]))
        low = t.lower()
        for f in FORBIDDEN:
            if f in low:
                hard.append((i, "Verbotsliste: '" + f + "'"))

    lengths.sort(reverse=True)
    for n, i, sn in lengths:
        if n > a.max_words:
            soft.append((i, f"Satz mit {n} Woertern: {sn[:90]}"))

    # 8 Exclusions
    if a.exclusions:
        terms = []
        for ln in open(a.exclusions, encoding="utf-8"):
            s = ln.strip()
            if not s or s.startswith("#") or s.startswith("<!--"):
                continue
            s = re.sub(r"^[-*]\s+", "", s).strip("`").strip()
            if len(s) >= 3 and not s.startswith("|"):
                terms.append(s)
        full = "\n".join(raw).lower()
        for term in terms:
            if term.lower() in full:
                hard.append((0, "Begriff aus exclusion-rules.md im Sheet: " + term))

    # 9 Pflichtabschnitte
    if a.call == 1:
        hs = " | ".join(h.lower() for h in headings)
        for name, pat in REQUIRED_CALL1:
            if not re.search(pat, hs):
                hard.append((0, "Pflichtabschnitt fehlt: " + name))

    print(f"Sheet: {a.sheet}  ({'deutsch' if german else 'englisch'}, {len(body)} Vorlesezeilen)")
    print("Laengste Saetze:")
    for n, i, sn in lengths[:5]:
        print(f"  {n:>3} W  Z.{i}: {sn[:100]}")
    if not hard and not soft:
        print("OK – keine Treffer.")
        return 0
    for kind, items in (("FEHLER", hard), ("HINWEIS", soft)):
        for i, msg in items:
            print(f"{kind} Z.{i}: {msg}")
    print(f"\n{len(hard)} Fehler, {len(soft)} Hinweise.")
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
