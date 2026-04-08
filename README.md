# Venture DD

**AI-powered Due Diligence for Venture Capital — a Claude Code Plugin**

Venture DD turns Claude Code into a critical VC analyst that systematically extracts, cross-references, and challenges startup data rooms. It runs a structured 6-session workflow — from legal extraction to investment conviction — with built-in bias prevention, independent calculations, and web-verified founder checks.

Built for investors who want rigor, not confirmation bias. The guiding question throughout: *"Would I invest my own money?"*

---

## About the Author

**Anton Foertsch** is Principal at [Kensho Ventures](https://www.kensho.vc), a solo-GP deep-tech VC fund investing in European resilience technologies — robotics, cybersecurity, quantum computing, and industrial AI. He has been investing in deep tech for several years, covering fund management, dealflow, and hands-on portfolio support including board-level involvement. He built Venture DD to systematize the due diligence process across the fund's dealflow.

---

## What it does

Drop into any deal folder containing pitch decks, financial models, contracts, and proposals — then run `/dd`. The plugin automatically:

1. **Scans the data room** — detects and categorizes all documents (PDFs, XLSX, DOCX)
2. **Extracts structured data** — parallel subagents process documents into standardized formats
3. **Cross-references everything** — flags discrepancies between pitch, model, contracts, and conversations
4. **Runs independent calculations** — unit economics, customer ROI, dilution scenarios, break-even analysis
5. **Conducts web research** — competitor analysis, market validation, founder background verification
6. **Builds investment conviction** — Top-5 risks, Top-5 strengths, and a clear recommendation

---

## Installation

```bash
claude plugin add https://github.com/Toni-Schraubenzieher/venture-dd
```

## Usage

Navigate to a deal's data room folder and run:

```
/dd
```

The workflow is **state-aware** — it picks up where you left off. Run `/dd` repeatedly to progress through sessions or resume after a break.

---

## The 6-Session Workflow

| # | Session | What happens |
|---|---------|-------------|
| 1 | **Legal & Contracts** | Extracts SHA, LOIs, customer contracts, VSOP terms. Identifies binding vs. non-binding commitments. |
| 2 | **Investments & Cap Table** | Maps CLAs, funding rounds, dilution scenarios. Reconstructs cap table from available data. |
| 3 | **Product, Market & Financials** | Full extraction of pitch deck, financial model (Excel), market sizing, unit economics, traction pipeline. |
| 4 | **Cross-Referencing** | Two-phase analysis: Quick Scan of key metrics across all documents, then Deep Dive on discrepancies. Independent calculations. Mandatory checklist (GTM vs. model, pipeline definitions, pricing validation, etc.). |
| 5 | **Deep Analysis & Conviction** | 5 parallel web research blocks (competitors, market, customers, technology, founders). Builds investment conviction with Top-5 risks and strengths. |
| 6 | **DDQ** | Generates prioritized founder questions based on findings. After receiving answers: systematic re-assessment of conviction. |

---

## How it works

### Architecture

```
/dd command
  |
  ├── State Detection (reads CLAUDE.md)
  |     ├── No CLAUDE.md → Setup (scan, extract, generate sessions)
  |     ├── Open session with chunks → Parallel subagent extraction
  |     ├── Open session without chunks → Sequential extraction
  |     └── All sessions done → Report & next steps
  |
  ├── Parallel Extraction (Sessions 1-3)
  |     ├── Splits documents into chunks (~100 pages each)
  |     ├── Dispatches dd-extractor subagents in parallel
  |     ├── Each chunk writes Key Metrics for cross-referencing
  |     └── Consolidates chunks into final extraction files
  |
  ├── Cross-Referencing (Session 4)
  |     ├── Phase 1: Quick Scan — loads only Key Metrics sections
  |     ├── Mandatory checklist (8 universal + vertical-specific checks)
  |     └── Phase 2: Deep Dive — own calculations on discrepancies
  |
  ├── Web Research (Session 5)
  |     ├── 5 parallel research agents
  |     ├── Competitor & valuation benchmarks
  |     ├── Market tailwinds & regulatory analysis
  |     ├── Customer & pricing validation
  |     ├── Technology & hardware benchmarks
  |     └── Founder background verification
  |
  └── Outputs
        ├── extracted/     → Raw structured data
        ├── analysis/      → Cross-references, research, working notes
        └── report/        → DD report, investment memo
```

### Bias Prevention

Built-in safeguards against confirmation bias:

- **Own calculations** — never accepts startup numbers at face value
- **Counter-evidence search** — actively asks "What would make this NOT work?"
- **Founder claim verification** — cross-checks LinkedIn, patents, press against deck claims
- **Pricing validation** — checks if anyone has actually *paid* the stated price
- **Pipeline reality check** — distinguishes "signed contract" from "had a meeting"

### Vertical Modules

Industry-specific modules that enrich the analysis with sector benchmarks, specialized checks, and targeted research queries:

| Vertical | Focus areas |
|----------|------------|
| `hardware-robotics` | BOM analysis, TRL assessment, production ramp feasibility, all-in unit economics, certification timelines |
| `space-logistics` | Orbital mechanics validation, launch cost benchmarks, spectrum/licensing, radiation hardening |
| `_template` | Create your own vertical — add keywords, extraction focus areas, cross-referencing checks, research blocks, risk framework, and benchmarks |

Verticals live in `skills/dd/references/verticals/`. The plugin auto-matches based on keywords in the startup's industry description.

---

## Output Structure

After running all sessions, your deal folder contains:

```
deal-folder/
├── CLAUDE.md                        → State tracker (conviction, risks, session status)
├── extracted/
|   ├── legal.md                     → Contracts, LOIs, terms
|   ├── investments.md               → Cap table, funding, dilution
|   ├── product-market.md            → Product, market, competition
|   └── financials.md                → Full financial model extraction
├── analysis/
|   ├── cross-references.md          → Discrepancy table + own calculations
|   ├── working-notes.md             → Open questions, flags for DDQ
|   ├── research-block1-competition.md
|   ├── research-block2-market.md
|   ├── research-block3-customers.md
|   ├── research-block4-technology.md
|   ├── research-block5-founders.md
|   └── ddq-questions.md             → Founder questionnaire
├── report/
|   ├── dd-report.md                 → Full DD report with conviction
|   └── investment-memo.md           → IC-ready investment memo
└── sessions/
    ├── 01-legal.md                  → Session instructions (auto-generated)
    ├── 02-investments.md
    ├── 03-product-market.md
    ├── 04-cross-referencing.md
    ├── 05-deep-analysis.md
    └── 06-ddq.md
```

---

## Post-DD Options

After Session 5, the plugin offers:

- **Investment Memo** — IC-ready memo with deal summary, thesis, risks, unit economics, and recommendation
- **Pass Letter** — Professional, respectful decline email with real reasons (structural, not personal)
- **DDQ** — Prioritized founder questions with systematic re-assessment after answers
- **Deep Dive** — Drill into specific concerns (competitive threats, technology moat, regulatory risk)

---

## Language

All outputs in **German**. Web research queries in **English**. This reflects the fund's DACH focus. Language can be adapted by modifying the `/dd` command.

---

## Requirements

- [Claude Code](https://claude.ai/claude-code) CLI
- WebSearch enabled (for Session 5 research)
- PDF reading capability (built into Claude Code)

---

## Contributing

Venture DD is open source. Contributions welcome — especially new vertical modules for additional industries. See `skills/dd/references/verticals/_template.md` for the vertical format.

---

## License

MIT

---

*Built by [Anton Foertsch](https://www.linkedin.com/in/anton-foertsch-2a07721b0/) at [Kensho Ventures](https://www.kensho.vc).*
