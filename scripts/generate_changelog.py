#!/usr/bin/env python3
"""
Local Changelog Generator Script for Brando.
Parses Conventional Commits from git log and builds a structured CHANGELOG.md.
"""

import subprocess
import sys
from collections import defaultdict


def run_git_command(args: list[str]) -> str:
    """Runs a git command and returns its standard output."""
    try:
        result = subprocess.run(
            ["git"] + args,
            capture_output=True,
            text=True,
            check=True,
            encoding="utf-8",
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e.stderr}", file=sys.stderr)
        return ""
    except FileNotFoundError:
        print("Git is not installed or not in PATH.", file=sys.stderr)
        return ""


def main():
    # Retrieve commit history in format: hash|date|subject
    log_format = "%H|%cs|%s"
    stdout = run_git_command(["log", f"--pretty=format:{log_format}"])
    if not stdout:
        print("No git history found to generate changelog.")
        return

    # Categorize conventional commit prefixes
    categories = {
        "feat": "Features",
        "fix": "Bug Fixes",
        "docs": "Documentation",
        "perf": "Performance Improvements",
        "refactor": "Code Refactoring",
        "test": "Tests",
        "chore": "Maintenance Tasks",
    }

    # Group commits by date and category
    # structure: { date: { category_header: [commit_messages] } }
    releases = defaultdict(lambda: defaultdict(list))

    for line in stdout.split("\n"):
        if "|" not in line:
            continue
        parts = line.split("|", 2)
        if len(parts) < 3:
            continue
        commit_hash, date, subject = parts
        short_hash = commit_hash[:7]

        # Check for conventional prefix
        prefix = ""
        clean_subject = subject
        if ":" in subject:
            left, right = subject.split(":", 1)
            # handle scopes like feat(cli):
            clean_prefix = left.split("(")[0].strip().lower()
            if clean_prefix in categories:
                prefix = clean_prefix
                clean_subject = right.strip()

        header = categories.get(prefix, "Other Changes")
        formatted_entry = f"* {clean_subject} ([{short_hash}](https://github.com/mrxsierra/brando/commit/{commit_hash}))"
        releases[date][header].append(formatted_entry)

    # Build CHANGELOG.md content
    header_text = (
        "# Changelog\n\nAll notable changes to the Brando naming engine "
        "will be documented in this file.\n"
    )
    markdown = [header_text]

    # Sort releases descending by date
    for date in sorted(releases.keys(), reverse=True):
        markdown.append(f"## [{date}] - {date}\n")

        # Sort headers so Features and Bug Fixes appear first
        headers = releases[date]
        sorted_headers = sorted(
            headers.keys(),
            key=lambda x: 0 if x == "Features" else (1 if x == "Bug Fixes" else 2),
        )

        for header in sorted_headers:
            markdown.append(f"### {header}\n")
            for entry in headers[header]:
                markdown.append(entry)
            markdown.append("")  # spacing
        markdown.append("---")

    # Write to CHANGELOG.md at repository root
    try:
        with open("CHANGELOG.md", mode="w", encoding="utf-8") as f:
            f.write("\n".join(markdown))
        print("CHANGELOG.md successfully generated/updated.")
    except Exception as e:
        print(f"Failed to write CHANGELOG.md: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
