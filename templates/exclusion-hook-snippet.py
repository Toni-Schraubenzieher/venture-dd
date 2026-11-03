"""Exclusion-Grep-Hook — Snippet for projects that build an external
investor memo from markdown via build-docx.py (or equivalent).

PURPOSE
-------
Hard build-blocker for named-entity exclusions in external-facing artifacts.
The hook greps the markdown source against `exclusion-rules.md` before
handing off to pandoc. If any excluded term is present, the build aborts
with exit code 1 and lists the offending lines. An escape hatch
(`--override --reason "<text>"`) exists for the rare legitimate edge case
but is deliberately friction-bearing (explicit flag + required reason).

SCOPING
-------
Only runs when the build target is an EXTERNAL artifact (e.g. investor
memo). Internal reports (e.g. `report/internal/tech-dd-report-INTERNAL-
ONLY.md`) legitimately contain terms that appear on the exclusion list
and must not be gated by this hook.

INTEGRATION
-----------
1. Copy `check_exclusions` and `parse_exclusion_args` into your project's
   build-docx.py.
2. Call `parse_exclusion_args()` at the top of main() to capture the
   `--override` / `--reason` flags.
3. Call `check_exclusions(MD_FILE, EXCLUSION_FILE, override, reason)`
   before the pandoc step.
4. Author an `exclusion-rules.md` at the workspace root with one literal
   term per line (case-insensitive match). Comments with `#`.

EXAMPLE
-------
    # in build-docx.py main():
    override, reason = parse_exclusion_args()
    check_exclusions(MD_FILE, WORKSPACE_ROOT / "exclusion-rules.md",
                     override=override, reason=reason)
    run_pandoc(...)
"""
import argparse
import re
import sys
from pathlib import Path


def parse_exclusion_args():
    """Parse --override / --reason from sys.argv without disturbing other
    argparse setups. Returns (override: bool, reason: str|None)."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--override", action="store_true",
                        help="Bypass the exclusion-rules build blocker")
    parser.add_argument("--reason", type=str, default=None,
                        help="Required justification when --override is used")
    known, _ = parser.parse_known_args()
    if known.override and not known.reason:
        print(
            "ERROR: --override requires --reason \"<text>\" with a written "
            "justification. Aborting.",
            file=sys.stderr,
        )
        sys.exit(2)
    return known.override, known.reason


def _load_exclusion_terms(exclusion_file: Path):
    """Read the exclusion file. One term per line. Lines starting with `#`
    are comments. Blank lines ignored. Returns list of (term, lower_term)."""
    if not exclusion_file.exists():
        return []
    terms = []
    for raw in exclusion_file.read_text(encoding="utf-8").splitlines():
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        terms.append((stripped, stripped.lower()))
    return terms


def check_exclusions(source_path: Path, exclusion_file: Path,
                     override: bool = False, reason: str | None = None) -> None:
    """Pre-build exclusion check. Aborts via sys.exit(1) on violations
    unless `override=True` is passed."""
    if override:
        print(f"[EXCLUSION OVERRIDE] Bypassed by --override. Reason: {reason}")
        return

    terms = _load_exclusion_terms(exclusion_file)
    if not terms:
        # No rules file, or empty — treat as green.
        return

    if not source_path.exists():
        print(
            f"ERROR: exclusion-check cannot locate source file: {source_path}",
            file=sys.stderr,
        )
        sys.exit(1)

    src_lines = source_path.read_text(encoding="utf-8").splitlines()
    violations = []

    for line_no, line in enumerate(src_lines, start=1):
        line_lower = line.lower()
        for term_raw, term_lower in terms:
            # Word-boundary-aware match to avoid accidental substring hits
            # (e.g. avoid "Annex" matching the term "Ann" — even though
            # in our use case such substrings rarely occur, the safeguard
            # costs nothing).
            pattern = r"\b" + re.escape(term_lower) + r"\b"
            if re.search(pattern, line_lower):
                violations.append((line_no, term_raw, line.rstrip()))

    if violations:
        print("=" * 70, file=sys.stderr)
        print("EXCLUSION VIOLATION — build aborted", file=sys.stderr)
        print("=" * 70, file=sys.stderr)
        print(f"Source:         {source_path}", file=sys.stderr)
        print(f"Exclusion file: {exclusion_file}", file=sys.stderr)
        print(f"Violations:     {len(violations)}", file=sys.stderr)
        print("", file=sys.stderr)
        for line_no, term, line in violations:
            print(f"  line {line_no}  [term: {term}]", file=sys.stderr)
            print(f"    {line[:120]}{'...' if len(line) > 120 else ''}",
                  file=sys.stderr)
        print("", file=sys.stderr)
        print(
            "To bypass for a legitimate edge case, re-run with:\n"
            "  --override --reason \"<your written justification>\"\n"
            "The override will be logged to stdout for audit trail.",
            file=sys.stderr,
        )
        sys.exit(1)
