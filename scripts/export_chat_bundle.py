#!/usr/bin/env python3
"""Export the maintained workflow as one text attachment, without case data."""

import argparse
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL = Path("skills/reimbursement-workflow")
# Explicit public inputs: never recursively collect a user's case directory.
SOURCES = (
    Path("prompts/start.md"),
    SKILL / "SKILL.md",
    SKILL / "references/workflow.md",
    SKILL / "references/rules.md",
    SKILL / "references/scenarios/nju-travel-materials.md",
    SKILL / "references/scenarios/SCENARIO_TEMPLATE.md",
    SKILL / "references/collection.md",
    SKILL / "references/finance-review.md",
    SKILL / "assets/case.md",
    SKILL / "assets/oa-draft.md",
    SKILL / "assets/expenses.csv",
    SKILL / "assets/review.md",
    SKILL / "references/replay.md",
    SKILL / "references/integrity.md",
    SKILL / "scripts/check_packet.py",
)


def export(root, destination):
    sections = [
        "NANJING UNIVERSITY INTERNATIONAL COMPUTER SCIENCE CONFERENCE REIMBURSEMENT — CHAT EDITION\n\n"
        "Attach this file or paste its full contents into your agent, then describe "
        "your Nanjing University unit, traveler role, conference trip, and available materials. Unknown "
        "details can be discovered during intake. No installation is required.\n\n"
        "This file is generated from the maintained public sources listed below. "
        "It contains instructions, empty working templates, and an optional "
        "freshness script; it contains no claimant evidence and is not an official policy publication.\n\n"
        "For the agent: begin with the starter prompt and canonical workflow. "
        "Relative links refer to included SOURCE sections, resolved from the "
        "referencing source's directory; read those sections within this attachment "
        "rather than requesting separate files. The script section is source code, "
        "not an installed executable or evidence that it ran. Use only capabilities "
        "actually available in this chat. Missing filesystem, browser, mail, or "
        "rendering access must not be reported as completed actions.\n\n"
        "CONTENTS\n" + "\n".join(str(path) for path in SOURCES)
    ]
    for relative in SOURCES:
        source = root / relative
        sections.append(
            f"\n=== SOURCE: {relative.as_posix()} ===\n\n"
            + source.read_text(encoding="utf-8").rstrip()
            + f"\n\n=== END SOURCE: {relative.as_posix()} ==="
        )
    # Read every input before creating output; never overwrite an earlier export.
    with destination.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write("\n".join(sections) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="New text file; parent must exist")
    args = parser.parse_args()
    try:
        export(ROOT, args.output)
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    print(f"Created {args.output} from {len(SOURCES)} public source files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
