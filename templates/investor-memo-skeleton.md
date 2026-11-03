# Technical Due Diligence for Investors: [Company]

**Prepared by:** <Fonds>, <Ort>
**For:** Prospective Investors
**Date:** [Month Year]
**Version:** [x.y — description]
**Status:** [Draft / Final]
**Classification:** Confidential — for internal use by the recipient only

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Company & Team](#2-company--team)
3. [The Problem: Why the Market Needs [Company]](#3-the-problem-why-the-market-needs-company)
4. [The Technology](#4-the-technology)
5. [Validation & Security Evidence](#5-validation--security-evidence)
6. [Market & Competitive Landscape](#6-market--competitive-landscape)
7. [Go-to-Market & Traction](#7-go-to-market--traction)
8. [Investment Thesis](#8-investment-thesis)
9. [Key Milestones](#9-key-milestones)
- [Annex A: Sources](#annex-a-sources)
- [Annex B: Glossary](#annex-b-glossary)

---

## 1. Executive Summary

**[One opening paragraph: what the company does, in plain language. 3–5 sentences max. No superlatives without evidence.]**

**Assessment of the Investment Case:** [Use qualified language — "notable for the stage, asymmetric by use case" rather than "exceptional". Explicitly flag the asymmetry: e.g. "TRL 7–8 on the defense track, TRL 4 today on the UGV track, converting to TRL 7+ with the Q2/Q3 2026 pilot". State what is signed (with exact figures) and what is active-lead.]

**[Update block — versioned].** [Mention only developments since the prior version. Team changes should use Team-Status taxonomy (taxonomies.md §3) — "full-time CxO" reserved for T2/T3; advisors with deepened commitment stay "operational advisors".]

**Core Risks and Mitigation:** [Summarise the open risks honestly. Include at minimum: IP-assignment status if in progress, technical Bus Factor split if sole developer, certification gaps, formal academic review gap if not yet commissioned. For each: one-line mitigation with timeline.]

> **[Company] at a Glance**
>
> | Dimension | Status |
> |---|---|
> | **Stage** | [Pre-seed / Seed / Bridge — be specific] |
> | **Signed commercial pilot(s)** | [Exact count + contracted amount. Plural only if >1] |
> | **Defense / institutional traction** | [Active pilots vs. active leads vs. exploratory — distinguish] |
> | **Product maturity** | [TRL per use case, not single score] |
> | **Burn Rate** | [Pre-funding configuration + note that post-funding will change] |
> | **Team** | [T1 Founder + T2/T3 full-time roles + T4 operational advisors — use taxonomy] |
> | **Cap Table** | [Founder %, cleaned-up or not, key investor entries] |

---

## 2. Company & Team

### 2.1 Corporate Structure & Entities

[Current and planned entity setup. Table per entity: Jurisdiction / Role / Rationale. Include any in-progress IP-assignment status explicitly — this is a Section 4.5 risk item also, not a hidden footnote.]

### 2.2 Founder: [Name] — [Title]

[Background, prior operating history with verifiable outcomes. Patents, awards, exits — each citable in Annex A. Keep factual; avoid hero-narrative framing.]

### 2.3 Team Expansion & Co-Founder Search

**[Name] — [Title] ([T2/T3: Full-time permanent / Full-time tenure-horizon], [Month Year]).** [Background + key network assets + explicit tenure horizon if T3. Do not describe T4 as full-time.]

**[Name] — [operational advisor with deepened commitment, Month Year].** [Explain the arrangement honestly — "operational advisor with materially deepened commitment" is the correct framing for T4. State that a permanent senior hire is scheduled. This honest framing builds credibility.]

**Active [co-founder / senior] search.** [Profile + target window + sourcing channels. Acknowledge that the search window is an execution risk.]

### 2.4 Advisory Board

[Distinguish current T5 advisors from T4 operational advisors (who may be listed in 2.3). Be precise about who holds what role.]

### 2.5 Investor Base & Funding Round Status

[Round structure, anchor, target composition. **Do not expose operational dependencies on specific investors currently being pitched.** Specific names withheld pending close.]

---

## 3. The Problem: Why the Market Needs [Company]

### 3.1 [Structural Driver 1]

[Regulatory pressure, geopolitical, technological shift — with citable data points.]

### 3.2 [Structural Driver 2]

### 3.3 [Structural Driver 3]

---

## 4. The Technology

### 4.1 Architecture Overview

[High-level description. If proprietary, frame architecture as innovation rather than cryptography — "X's innovation sits at the architectural level, not at the level of the underlying primitives" is a fair framing when true.]

### 4.2 Hardware / Platform

[Physical or platform characteristics. Concrete specs.]

### 4.3 Core Technology

[Technical deep-dive. Cite primitives. Differentiate between well-established components and novel composition.]

### 4.4 Core Product Strengths

[3–5 bullet points. Each with evidence, not assertion.]

### 4.5 Open Technical Questions and Mitigation Plan

[Standard structure: problem / assessment / mitigation / timeline per item. Include at minimum:]

**1. [Risk item — typically: formal academic review or certification gap]**
*Problem:* [...]
*Assessment:* [...]
*Mitigation:* [... with timeline]

**2. [Risk item — typically: scalability, PQC migration, etc.]**

**3. [Risk item — typically: certifications]**

**4. [Risk item — typically: IP assignment, if in progress]**

**5. [Risk item — Technical Bus Factor if applicable]**

[Rule: any risk flagged KRITISCH in internal DD-Report (tech-dd-report-INTERNAL-ONLY.md) must either appear here with mitigation, or must have a documented exclusion decision. See rationality-audit.md §10.]

---

## 5. Validation & Security Evidence

**Product maturity at a glance (TRL).** [TRL table per use case. Not a single company-wide score. See taxonomies.md §5.]

### 5.1 [Public Validation Event — e.g. Hackathon, Pilot Outcome]

[Describe the event, the scope, the result — and the limitation. Self-administered tests are self-administered tests; label them honestly.]

### 5.2 Third-Party Reviews

[**Structure in two levels per taxonomies.md §1. Do not conflate.**]

**Level 1 — Informal expert reviews.** [Microsoft / AWS / sector practitioner — qualitative, not formalised. Name each with what they reviewed and their finding.]

**Level 2 — Partner-programme eligibility reviews.** [Citrix / Kaspersky / similar — baseline security assessments as partnership gates, not cryptographic audits. Describe them honestly.]

**Assessment:** [Summarise. Acknowledge the residual gap — formal independent audit — openly. Link to Section 4.5.]

### 5.3 Active Pilots & Customer Validation

[**Pilot table following taxonomies.md §2. Distinguish P1 (signed paid) from P3/P4 (verbal / active lead) from P6 (exploratory). Plural "pilots" only when ≥2 at stage P1/P2.**]

| # | Customer | Vertical | Stage | Commercial structure | Next milestone |
|---|---|---|---|---|---|
| 1 | [Customer] | [Vertical] | [**Signed paid pilot** — exact amount if shareable] | [...] | [...] |
| 2 | [Customer] | [Vertical] | [Active lead / scheduled evaluation] | [...] | [...] |
| 3 | ... | ... | ... | ... | ... |

**Headline framing.** [Honest count statement: "One signed commercial pilot plus a broader set of active engagements at different stages." Avoid plural "pilots" when only one is contracted.]

**How deployments are evaluated by these customers.** [If relevant: the 5-step CIO/CISO-driven process or equivalent. Frame evaluation as customer-side structural, not proprietary-specific.]

### 5.4 [Domain-Specific Validation — e.g. Defense Validation]

[Table of validation points with status. Qualify — most engagements are typically at lead/demo/evaluation stage, converting to contract in following quarters.]

### 5.5 Certification Status

[Table: certification / meaning / status (In place / In progress / Planned / Long-term roadmap).]

---

## 6. Market & Competitive Landscape

### 6.1 Market Dynamics & Drivers

[Data-driven: market size sources, spending trends, M&A signals — each citable.]

### 6.2 Competitive Landscape Overview

[Comparison table: competitor / category / funding / key contracts.]

### 6.3 — 6.N Deep Dives

[Per-competitor deep dives where relevant. Differentiation tables.]

### 6.N+1 Market Size (Bottom-Up)

[TAM / SAM / SOM with explicit methodology and conservative SOM assumptions.]

### 6.N+2 Market Validation Through Competitor Investment

[Validating rounds / acquisitions that corroborate the market thesis.]

---

## 7. Go-to-Market & Traction

### 7.1 GTM Strategy

[Clear, resource-weighted strategy.]

### 7.2 [Vertical 1 — e.g. Commercial Land-and-Expand]

### 7.3 [Vertical 2 — e.g. Defense Programme-Driven]

[Include procurement mechanics where relevant — e.g. if a specific exercise like REPMUS is a procurement qualifier, explain how that process converts participation into contract.]

### 7.4 Exploratory Verticals (early stage)

[Clearly mark as exploratory. No scale assumptions.]

### 7.5 Business Model & Capital Efficiency

**Revenue model:** [Pricing components.]

**Target ACV:** [Per vertical range.]

**Capital efficiency:** [Burn rate — explicitly mark as pre-funding configuration and note that post-funding will change. See taxonomies.md §7.]

**Implication for investors:** [Use-of-funds narrative — be honest about engineering-adjacent costs (certifications, PQC migration, Founding Engineer, new IP filings) alongside commercial scale-up. Avoid "funding enables commercial scale-up, not R&D" — that's almost always a blanket statement violation.]

---

## 8. Investment Thesis

This due diligence combines [list: technical architecture review, competitive landscape, reference conversations, direct founder engagement — whichever applies]. On this basis, [N] central arguments:

### 1. [Product Maturity Argument — qualified]

[Use stage-qualified language. "Unusual for pre-seed" with evidence beats "exceptional" without.]

### 2. [Customer Pull Argument]

### 3. [Timing Convergence]

[Regulatory + geopolitical + technological triad if relevant.]

### 4. [Capital Efficiency]

### 5. [Execution Moat & Multi-Vertical Optionality]

[Bullet list of execution-moat elements. Distinguish actual position from aspirational one — "already deploying" vs. "once the system is embedded".]

### Overall Assessment

[Use the "X is not a bet on Y. The investment case rests on Z" framing — honest about what is and is not claimed. Explicit on downside considerations alongside upside. End with a clear-eyed summary ("This is a case to be entered with clear-eyed acknowledgement of what is already proven and what remains to be proven") rather than promotional language.]

---

## 9. Key Milestones

| Period | Milestone |
|---|---|
| [Near-term] | [...] |
| [Next quarter] | [...] |
| [...] | [...] |

---

## Annex A: Sources

[Every numbered claim in the body must have a citable source here. Include:
- Deal-internal references (founder calls, dates)
- Institutional references with URLs
- Statistics with publishing source and date
- Industry reports with publisher and year
- Government / regulatory references with official URL]

---

## Annex B: Glossary

| Term | Explanation |
|---|---|
| [Term] | [Plain-language explanation for non-technical investors] |

---

## Writing Checklist (Remove before sharing)

- [ ] Exec Summary: no unqualified superlatives
- [ ] Team: Team-Status taxonomy applied (T2/T3 vs. T4 distinction honest)
- [ ] Section 4.5: all KRITISCH risks from internal DD surface or are documented exclusions
- [ ] Section 5.2: two-level Evidence-Level structure (Expert Reviews vs. Partner-Programme)
- [ ] Section 5.3: pilot count plural ↔ actual Plural check
- [ ] Section 5.3: TRL disaggregated per use case
- [ ] Section 7.5: burn rate marked as pre-funding configuration
- [ ] Section 8: no "already answered" claims without qualification
- [ ] Exclusion-rules check: no excluded terms in source
- [ ] All numerical claims have Annex A sources
- [ ] Rationality-pass run (`/dd:rationality-pass`)
