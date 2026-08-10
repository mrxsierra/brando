#!/usr/bin/env python3
"""
Documentation & Markdown Linting & Formatting Automation Script for Brando.

Performs strict validation across all documentation files:
1. Audits Markdown files for hardcoded numeric heading prefixes (e.g. '## 1. Title').
2. Automatically fixes hardcoded numbered headings when run with `--fix`.
3. Executes `mkdocs build --strict` to verify site configuration and cross-references.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"

# Regex pattern matching hardcoded numbered headings like '## 1. Installation'
HARDCODED_HEADING_PATTERN = re.compile(r"^(#{1,4})\s+[0-9]+\.\s+(.*)$")

# List of excluded files/directories for public doc heading linting
EXCLUDED_PATHS = {"private", "PRD.md"}


def should_skip(path: Path) -> bool:
    """Check if a file or directory should be skipped during public doc linting."""
    relative = path.relative_to(DOCS_DIR)
    parts = relative.parts
    return any(excluded in parts for excluded in EXCLUDED_PATHS)


def audit_and_format_markdown(fix: bool = False) -> list[str]:
    """Audit markdown files and optionally fix heading violations."""
    violations = []
    for md_file in DOCS_DIR.rglob("*.md"):
        if should_skip(md_file):
            continue

        content = md_file.read_text(encoding="utf-8")
        lines = content.splitlines()
        modified = False
        new_lines = []

        for line_num, line in enumerate(lines, start=1):
            match = HARDCODED_HEADING_PATTERN.match(line)
            # Skip code blocks comments or numbered code lines
            if (
                match
                and not line.strip().startswith("# ")
                and not line.strip().startswith("## ")
                and not line.strip().startswith("### ")
            ):
                new_lines.append(line)
                continue

            if match and (
                line.startswith("#") or line.startswith("##") or line.startswith("###")
            ):
                relative_path = md_file.relative_to(DOCS_DIR.parent)
                violations.append(
                    f"{relative_path}:{line_num}: Hardcoded numbered heading -> '{line.strip()}'"
                )
                if fix:
                    hashes, title = match.groups()
                    new_line = f"{hashes} {title.strip()}"
                    new_lines.append(new_line)
                    modified = True
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)

        if fix and modified:
            md_file.write_text("\n".join(new_lines) + "\n", encoding="utf-8")

    return violations


def check_mkdocs_strict_build() -> tuple[int, str]:
    """Execute mkdocs build --strict to verify site structure and link integrity."""
    result = subprocess.run(
        ["uv", "run", "mkdocs", "build", "--strict"],
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout + result.stderr


def main():
    parser = argparse.ArgumentParser(
        description="Lint and format Brando documentation."
    )
    parser.add_argument(
        "--fix", action="store_true", help="Automatically fix heading violations."
    )
    args = parser.parse_args()

    print("🔍 Auditing Markdown typography & heading standards...")
    if args.fix:
        print("🛠️  Auto-formatting enabled (`--fix`). Cleaning heading violations...")

    violations = audit_and_format_markdown(fix=args.fix)

    if violations and not args.fix:
        print(f"❌ Found {len(violations)} Heading Rule Violation(s):")
        for v in violations:
            print(f"   - {v}")
        print(
            "\n💡 Guideline: Do not hardcode numbers into headings (e.g. use '## Quickstart' instead of '## 1. Quickstart')."
        )
        print("   Run `uv run python scripts/lint_docs.py --fix` to auto-format!")
    elif args.fix:
        print("✅ Auto-formatting completed cleanly.")
    else:
        print("✅ Markdown typography & heading standards clean.")

    print("\n🔍 Running strict MkDocs site build validation (mkdocs build --strict)...")
    returncode, output = check_mkdocs_strict_build()
    if returncode != 0:
        print("❌ Strict MkDocs Build Failed:")
        print(output)
        sys.exit(1)
    else:
        print("✅ Strict MkDocs site build passed cleanly with 0 warnings.")

    if violations and not args.fix:
        sys.exit(1)

    print("\n🎉 Documentation linting & formatting automation PASSED!")


if __name__ == "__main__":
    main()
