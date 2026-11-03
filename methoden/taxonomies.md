# DD-Taxonomien (verbindliche Referenz)

Diese Datei definiert die 7 Taxonomien, die beim Extrahieren (Sessions 1–3), beim Cross-Referencing (Session 4), beim Memo-Schreiben und beim `/dd:rationality-pass` konsequent anzuwenden sind. Die Taxonomien sind **weich enforced** — sie leben durch Denk-Disziplin, nicht durch Build-Hooks. Aber: jede Abweichung im externen Memo ist beim Rationality-Pass ein Finding.

**Leitprinzip:** Taxonomien sind ordinal. Schwächere Stufen dürfen nie als stärkere Stufen framed werden. Das ist der häufigste Drift-Mechanismus in VC-Memos — und der einfachste zu vermeiden, sobald die Hierarchie explizit ist.

---

## 1. Evidence-Level (Validation-Evidenz)

Wenn du im Memo schreibst *"reviewed by X"* / *"validated by Y"* / *"audited by Z"* — welche Stufe ist das wirklich?

| Stufe | Bezeichnung | Kriterium |
|---|---|---|
| **E1** | Formal independent audit / certification | Extern beauftragt, methodisch strukturiert, zitierbares Dokument (z. B. FIPS 140-3, ISO 27001, formeller Crypto-Audit) |
| **E2** | Formal third-party review | Zitierbares Review eines externen Instituts / Universitäts-Labors / akkreditierter Prüfstelle; methodisch dokumentiert |
| **E3** | Informal senior-expert review | Ein oder mehrere Experten-Gespräche, qualitativ stark aber ohne formelle Methodik (z. B. Gespraeche mit Hyperscaler- und Industrie-Experten) |
| **E4** | Partner-programme eligibility review | Baseline-Security-Review als Gate zum Partner-Programm (Citrix, Kaspersky). Geht in die Tiefe der Partnerschaft, nicht in die Tiefe der Kryptographie |
| **E5** | Self-administered test | Vom Startup selbst durchgeführt (Hackathon, internes Red-Teaming, Bug-Bounty ohne externe Moderation) |
| **E6** | Founder-Claim | Nur als Aussage des Gründers vorhanden, nicht extern belegt |

**Good:** *"Five separate external touchpoints have examined the company's security posture across two distinct levels: informal cryptography expert reviews (two hyperscalers, one industry practitioner) and partner-programme eligibility reviews (two vendors)."*

**Bad:** *"Five independent technical evaluations at globally recognised organisations."* — bundelt E3 und E4 als Gleichwertiges.

---

## 2. Pilot-Stage (Customer-Validation-Stadium)

| Stufe | Bezeichnung | Kriterium |
|---|---|---|
| **P1** | Signed paid pilot | Vertrag unterschrieben, Pilot-Fee bezahlt oder verbindlich zugesichert |
| **P2** | Signed unpaid pilot | Vertrag unterschrieben, Hardware gestellt, keine Cash-Flow-Komponente |
| **P3** | Verbal agreement | Ja-Zusage mündlich/Email, aber noch kein unterschriebener Rahmen |
| **P4** | Active lead / scheduled evaluation | Konkrete Evaluations-Termin steht, NDA ggf. unterzeichnet, aber keine Commitments zur Deployment-Umsetzung |
| **P5** | Demo request | Kunde hat Demo angefragt, keine Folge-Termine gesetzt |
| **P6** | Exploratory conversation | Erstgespräche, keine konkreten Use-Cases definiert |

**Regel:** Im externen Memo muss klar sein, wie viele Pilots auf welcher Stufe stehen. Plural-Formen ohne Count sind Drift.

**Good:** *"One signed commercial pilot (infrastructure operator, €20,000 contracted in writing) plus a broader set of active defense engagements at different stages (verbal agreement with one special-forces unit; scheduled technical evaluation with a national cyber command; active leads with two armed forces; exploratory with a further armed force and a regional police force)."*

**Bad:** *"Committed, contracted pilots — not demonstrations, not letters of intent."* (Plural, keine Count-Differenzierung zwischen P1 und P3-P6.)

---

## 3. Team-Status

| Stufe | Bezeichnung | Kriterium |
|---|---|---|
| **T1** | Founder (CEO/CTO) | Equity-vested Gründer, permanente Rolle |
| **T2** | Full-time CxO (permanent) | Angestellte Permanent-Stelle, unbefristet |
| **T3** | Full-time CxO (tenure horizon) | Full-time-Angestellter mit expliziter zeitlicher Begrenzung (z. B. 2–3 Jahre bis permanenter Nachfolger gefunden) |
| **T4** | Operational advisor with deepened commitment | Advisor, der Day-to-Day-Execution unterstützt, aber keine formelle Employment-Relation |
| **T5** | Advisor (Board / Formal) | Formell auf Advisor-Board, periodische Meetings, Equity-Grant |
| **T6** | Consultant | Projektbezogene, honorar-basierte Zusammenarbeit |
| **T7** | Referrer / Network Contact | Keine Rolle, aber regelmäßige Intros |

**Regel:** Das externe Memo darf keine Person auf einer höheren Stufe framen als sie tatsächlich ist. Titel wie "full-time Chief X Officer" sind reserviert für T2 und T3 — nicht für T4.

**Good:** *"<Name> — Chief Revenue Officer (full-time, tenure horizon ~2–3 Jahre). <Name> — operational advisor with materially deepened commitment (defense GTM)."*

**Bad:** *"Three former advisors transitioned to full-time operational roles."* (Wenn in Wirklichkeit 1× T3 + 2× T4.)

---

## 4. Investor-Status

| Stufe | Bezeichnung | Kriterium |
|---|---|---|
| **I1** | Wire committed | Geld auf dem Escrow / Company-Account |
| **I2** | Signed subscription | Zeichnungsschein unterschrieben, Wire pending |
| **I3** | Term-sheet signed | Term-Sheet unterschrieben, Closing-Docs in Arbeit |
| **I4** | Soft commit with ticket size | Ticket-Größe mündlich/Email kommuniziert, kein unterschriebenes Papier |
| **I5** | Active DD | In laufender DD, keine Ticket-Indikation |
| **I6** | Warm interest | Erstgespräche positiv, keine Materials-Requests |
| **I7** | Cold | Keine Gespräche oder Ablehnung |

**Regel:** In internen Round-Construction-Dokumenten (Memory-File) muss jeder Investor auf einer konkreten Stufe stehen. Unterschied zwischen I3 und I4 entscheidet über "Runde closet diese Woche" vs. "Runde offen für Monate".

---

## 5. TRL-Disaggregation

**Regel ohne Stufen-Tabelle — es gibt keinen einheitlichen company-weiten TRL.**

TRL muss **per Use Case** oder **per Deployment-Track** angegeben werden, nie als einzelner Company-Score. Unterschiedliche Verticals / Deployment-Modi bewegen sich auf unterschiedlichen TRLs.

**Good:**
- *"Defense / TAC-systems: TRL 7–8 (near deployment-ready). Airport / UGV: TRL 4 today (security layer functional in lab; field deployment on UGV hardware is the open step)."*

**Bad:**
- *"MVP TRL 6."* (einheitlicher Company-Score)
- *"Exceptional product maturity for pre-seed."* (kein TRL-Anker überhaupt)

**Check im Rationality-Pass:** Scan nach *"TRL"* und *"maturity"* — wird immer per Use Case differenziert?

---

## 6. Bus-Factor-Split

**Regel ohne Stufen-Tabelle — Bus Factor ist nie ein einziger Score.**

Jede Bus-Factor-Aussage muss differenziert werden in:
- **Technical Bus Factor:** Wer kann die Codebase, die Kryptographie, die Hardware-Integration pflegen / weiterentwickeln?
- **Commercial Bus Factor:** Wer kann Customer-Verhandlungen führen, Deals closen, den Sales-Prozess skalieren?

Diese sind typischerweise unterschiedlich. Beispiel: Technical Bus Factor = 1 (der technische Gruender), Commercial Bus Factor = 2–3 (Gruender, CRO, zwei operative Rollen).

**Good:** *"The technical Bus Factor sits at one (the founder as sole developer). Commercial-side dependency has been materially reduced by a full-time CRO onboarding and by two deepened operational roles — but technical concentration on the founder remains until the Founding Engineer and the technical co-founder hires close."*

**Bad:** *"Execution-side dependency has been materially reduced."* (Verwischt die beiden.)

---

## 7. Burn-Rate-Framing

**Regel ohne Stufen-Tabelle — jede Burn-Rate-Aussage muss den Konfigurations-Zustand angeben.**

- **Pre-funding configuration:** aktuelle Running-Cost, oft strukturell niedrig (Home-Office, minimales Team)
- **Post-first-closing run-rate:** indikative Running-Cost nach geplanten Hires, Entity-Gründung, Office-Kosten
- **Post-second-closing run-rate:** falls bereits geplant

**Good:** *"The company's burn rate in its pre-funding configuration sits below €2,000 per month — this will change materially post first closing (office, Founding Engineer hire, entity-setup costs)."*

**Bad:** *"Burn rate below €2,000 per month — an extraordinary figure."* (kein Konfigurations-Marker, kein Post-Funding-Ausblick)

---

## Anwendung in den Skill-Phasen

| Phase | Wie die Taxonomien eingesetzt werden |
|---|---|
| **Session 3 (Extract)** | Pilot-Stage und Team-Status als Pflicht-Felder in `extracted/product-market.md`. Evidence-Level bei jeder "Validation"-Aussage mitführen. |
| **Session 4 (Cross-Ref)** | Cross-Check: stimmt Pitch-Deck-Framing mit Taxonomie-Realität überein? |
| **Session 5 (Deep-Analysis)** | Evidence-Hierarchie als Stratifizierung bei Conviction-Bildung. |
| **External Memo (Active Deal)** | Beim Schreiben jeder Plural-Aussage / jedes "reviewed by" / jedes Team-Titels prüfen: stimmt die Taxonomie-Stufe? |
| **`/dd:rationality-pass`** | Jede der 7 Taxonomien wird als Audit-Punkt in der Rationality-Checkliste gespiegelt. |
