# Rationality Audit — Checkliste gegen Memo-Drift

Diese Checkliste wird beim Schreiben externer Investor-Memos referenziert und vom Sub-Command `/dd:rationality-pass` strukturiert abgearbeitet. Sie ist die Enforcement-Schicht für die Taxonomien in `taxonomies.md` — und die Disziplin gegen den eigenen Conviction-Bias.

---

## 0. Bias-Priming (vor jedem Audit lesen)

**Du hast Conviction im Case. Genau darum entstehen die Drift-Muster. Diese Checkliste arbeitet gegen deine eigene Sympathie.**

Der Rationality-Pass ist **nicht primär gegen AI-Drift**, sondern gegen die eigene VC-Einbettung. Wenn du Monate an einem Case gearbeitet hast, Sympathie für den Founder aufgebaut hast und die Pitch-Modus-Sprache bereits im Kopf hast, entstehen die Überstatements nicht aus Nachlässigkeit — sondern aus Zugehörigkeit. Die Leitfragen gegen diese Einbettung:

- *"Würde ich diesen Satz schreiben, wenn ich den Founder nicht kennen würde?"*
- *"Lese ich einen Claim wohlwollender, weil ich ihn plausibel finde, oder weil er durch Evidenz gedeckt ist?"*
- *"Welche Superlative, Plural-Dehnungen und Blanket-Statements habe ich durchgewunken, die ich bei einem fremden Deck markieren würde?"*

Dokumentiere deine Antworten. Wenn sie dir schwerfallen, ist das ein Signal, nicht eine Ausrede.

---

## 1. Superlativ-Budget

**Ziel:** Superlative nur dort belassen, wo sie durch spezifische Evidenz gedeckt sind.

**Search-Terms** (case-insensitive): `exceptional`, `extraordinary`, `unprecedented`, `unparalleled`, `unmatched`, `world-class`, `best-in-class`, `superior`, `dominant`, `remarkable`, `outstanding`.

**Audit pro Treffer:**
1. Ist der Superlativ durch eine spezifische Zahl / Evidenz-Referenz qualifiziert?
2. Lässt sich der Satz ohne das Superlativ stärker schreiben (d. h. wird die Aussage durch die Qualifizierung ehrlicher, nicht schwächer)?
3. Gibt es einen Qualifizierer wie *"notable for the stage"* / *"unusual at this stage"* / *"unusually broad"* — das ist ok.

**Budget-Richtwert:** max. 2–3 Superlative pro Memo, jedes mit direkter Evidenz-Bindung im selben Satz oder direkt danach.

**Bekannte zulässige Ausnahme:** Marktsegment-Beschreibungen (*"the market is in a phase of exceptional dynamism"*) — hier ist das Superlativ Attribut des Markts, nicht des Startups.

---

## 2. Plural-Overclaim-Audit

**Ziel:** Plurale sind Counts. Ein Plural darf nie einen Count von 1 implizieren.

**Search-Terms:** `pilots`, `contracts`, `partnerships`, `customers`, `deployments`, `certifications`, `reviews`, `validations`, `engagements`, `references`, `commitments`.

**Audit pro Treffer:**
1. Wie viele tatsächliche Einheiten stehen hinter dem Plural?
2. Stehen die Einheiten auf derselben Pilot-Stage (siehe `taxonomies.md` §2)? Wenn nein → Count differenziert benennen.
3. Ist eine umformulierte Aussage ("One signed X plus N active leads at earlier stages") ehrlicher?

**Red Flag:** Plural + qualifying adjective ohne Count (*"committed, contracted pilots"*) — fast immer Overclaim.

---

## 3. Blanket-Statement-Scan

**Ziel:** Absolutheits-Aussagen durch Qualifikation ersetzen.

**Muster-Suche:**
- `"not X, but Y"` — prüfen: ist X wirklich komplett ausgeschlossen?
- `"every euro"`, `"every dollar"` — prüfen: ist die Allokation wirklich so monolithisch?
- `"always"`, `"never"`, `"only"`, `"the sole"`, `"the only"` — prüfen: Gegenbeispiel auffindbar?
- `"cannot be replicated"`, `"cannot be substituted"` — prüfen: worauf genau basiert der Claim?
- `"funding enables X, not Y"` — häufiger Fehler: ignoriert Post-Funding-Engineering-Bedarf.

**Audit:** Jede Blanket-Aussage muss entweder (a) faktisch korrekt und verifizierbar sein, oder (b) in eine qualified Version umgeschrieben werden.

---

## 4. "Already-Answered"-Audit

**Ziel:** Keine vorschnelle Resolution-Claims.

**Search-Terms:** `already answered`, `already resolved`, `no longer a question`, `settled`, `closed`, `proven`, `demonstrated`.

**Audit pro Treffer:**
1. Für welche Facette ist der Claim wahr? Für welche nicht?
2. Bei multi-track Produkten (z. B. Defense-Track vs. ziviler Track): stimmt der Claim für beide Tracks?
3. Gibt es einen noch offenen Punkt in Section 4.5 "Open Technical Questions", der genau diese Aussage relativiert?

**Good:** *"…substantially answered on the defense / TAC track and demonstrated in lab conditions on the UGV track — the specific open item the ANA pilot will resolve is field-deployment integrity on UGV hardware at scale."*

**Bad:** *"The central investor question is already answered."*

---

## 5. Team-Titel-Honesty

**Ziel:** Externer Titel und interne Charakterisierung dürfen nicht divergieren.

**Prozedur:**
1. Liste alle Team-Titel im externen Memo.
2. Öffne das interne Memory-File (`project_<deal>_round.md`) und den internen DD-Report.
3. Pro Person: stimmt die Taxonomie-Stufe (`taxonomies.md` §3) im externen Memo mit der internen Beschreibung?

**Red Flags:**
- "Full-time" extern, aber intern als "advisor with deepened commitment" beschrieben → T3-vs-T4-Drift
- Titel-Hierarchie (CEO, CRO, CTO) extern, aber faktisch keine formelle Employment → T2-Overclaim
- "Chief" extern, aber Zeit-Horizont < 12 Monate → fehlende Tenure-Horizon-Qualifizierung

**Remediation:** Taxonomie-konforme Umformulierung, keine Titel-Abwertung um ihrer selbst willen — Ehrlichkeit.

---

## 6. Evidence-Level-Nivellierung

**Ziel:** Unterschiedliche Evidence-Stufen nicht als gleichwertig framen.

**Prozedur:**
1. Scan aller "reviewed by" / "validated by" / "audited by" / "evaluated by" Claims.
2. Klassifiziere jeden nach `taxonomies.md` §1 (E1–E6).
3. Werden E3 (Expert-Review) und E4 (Partner-Programm) im selben Aufzählungsabsatz gebundelt, ohne die Stufen zu benennen?

**Good:** Zwei-Ebenen-Struktur im Memo (*"Level 1 — Informal cryptography expert reviews … Level 2 — Partner-programme eligibility reviews"*), mit Assessment-Satz am Ende, der ehrlich sagt, was die Bundelung aussagt und was nicht.

**Bad:** *"Five independent technical evaluations at globally recognised organisations — no structural concerns identified."*

---

## 7. TRL-Disaggregation

**Ziel:** Kein einheitlicher company-weiter TRL.

**Search-Terms:** `TRL`, `technology readiness`, `maturity`, `deployment-ready`.

**Audit:**
- Wird TRL per Use Case angegeben (siehe `taxonomies.md` §5)?
- Bei multi-track Produkten: stehen unterschiedliche TRLs pro Track?
- Ist der Plan artikuliert, wie TRL-schwächere Tracks angehoben werden?

---

## 8. Bus-Factor-Split

**Ziel:** Technical vs. commercial Bus Factor differenzieren.

**Audit:**
- Findet sich "Bus Factor" / "key person" / "sole developer" / "single founder" im Memo?
- Ist im selben Kontext klar differenziert zwischen Technical und Commercial Bus Factor (siehe `taxonomies.md` §6)?
- Wenn "execution-side dependency reduced" steht — ist präzisiert, welche Seite (commercial oder technical) reduziert wurde?

---

## 9. Burn-Rate-Framing

**Ziel:** Burn-Rate immer mit Konfigurations-Marker.

**Audit:**
- Wird ein Burn-Rate-Wert genannt?
- Ist klar gesagt: pre-funding configuration vs. post-first-closing run-rate?
- Wird der Post-Funding-Anstieg (Hires, Office, Entity-Kosten) anerkannt?

**Bad:** *"Burn rate below €2,000 per month — an extraordinary figure."*
**Good:** *"Burn rate in its pre-funding configuration sits below €2,000 per month — this will change materially post first closing."*

---

## 10. Hidden-Risk-Check (kritischster Audit-Punkt)

**Ziel:** Jedes Risiko aus dem internen DD-Report muss im externen Memo entweder offen adressiert oder bewusst exkludiert sein.

**Prozedur:**
1. Öffne den internen Tech-DD-Report (`report/internal/tech-dd-report-INTERNAL-ONLY.md`).
2. Liste die Top-Risiken (typischerweise Top-5-Risiken-Tabelle).
3. Pro Risiko: finde die entsprechende Passage im externen Memo.
   - Ist das Risiko in Section 4.5 "Open Technical Questions" (oder äquivalent) offen benannt?
   - Gibt es eine dokumentierte Mitigations-Logik?
   - Wenn das Risiko nicht im externen Memo auftaucht: ist das eine bewusste Entscheidung (ggf. in Section 5.2 / 7.3 dezent adressiert) oder ein Hidden-Risk?

**Red Flag:** Risiken im internen Report als KRITISCH markiert, im externen Memo nur im Exec-Summary-Absatz kurz gestreift oder gar nicht erwähnt.

**Remediation:** Entweder als eigener Punkt in Section 4.5 aufnehmen oder im Memo explizit dokumentieren, warum dieses Risiko nicht externally surfaced wird.

---

## 11. Quote- / Footnote-Integrity

**Ziel:** Jede spezifische Zahl, jedes Zitat, jede externe Referenz muss zitierbar sein.

**Prozedur:**
1. Scan aller konkreten Zahlen im Memo (Finanzangaben, Marktgrößen, Funding-Beträge Dritter).
2. Für jede: gibt es eine Annex-A-Referenz oder inline-Citation?
3. Bei Direkt-Zitaten (*"Security has been the blocker…"*): ist der Sprecher-Kontext korrekt, und ist die Verwendung durch den Kunden / die Quelle gedeckt?

**Red Flag:** Markt-Zahlen ohne Source. Kunden-Zitate, deren Ursprung nicht klar dokumentiert ist.

---

## 12. Exclusion-Cross-Check

**Ziel:** Per-Projekt-Exclusion-Regeln vor Memo-Build greifen.

**Prozedur:**
1. Öffne `exclusion-rules.md` im Workspace.
2. Grep die Source-Markdown nach jedem Exclusion-Term.
3. Treffer = Build-Blocker. Mit `build-docx.py --override --reason "<text>"` nur in Ausnahmefällen bypassen.

**Dieser Check ist hart enforced** (siehe `build-docx.py`-Hook-Pattern), im Gegensatz zu den weichen Audits 1–11.

---

## Usage-Pattern

### Beim Schreiben (inline)
Checkliste durch Abschnitt relevant lesen, bevor der Abschnitt final geschrieben wird. Nicht alle 12 Punkte sind in jedem Abschnitt relevant — §5 (Team-Titel) ist Section-2-spezifisch, §7 (TRL) ist Section-5-spezifisch etc.

### Nach größeren Edits (`/dd:rationality-pass`)
Vollständiger Durchlauf aller 12 Punkte gegen das gesamte externe Memo. Findings nach Priorität gruppieren:
- **Klar (Change nötig):** direkter Edit-Vorschlag
- **Judgment-Call:** via `AskUserQuestion` vorlegen
- **OK:** dokumentieren, dass geprüft

### Vor Memo-Dispatch an Investor
Mindestens §10 (Hidden-Risk-Check) und §12 (Exclusion-Cross-Check) — beide blockierend bei Unsauberkeiten.

---

## Meta-Note

Wenn diese Checkliste mechanisch abgearbeitet wird, verliert sie Wirkung. Der Wert entsteht, wenn die Audits als **Fragen** behandelt werden, nicht als Regeln. Frage bei jedem Punkt: *"Warum existiert dieser Audit? Welchen Drift-Mechanismus adressiert er? Greift der Mechanismus in dem Memo, das ich gerade vor mir habe?"* — Dann wird die Checkliste zu einem Werkzeug, nicht zu einer Abhak-Übung.
