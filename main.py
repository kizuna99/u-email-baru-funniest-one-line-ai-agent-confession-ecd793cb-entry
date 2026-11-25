# SPDX-License-Identifier: MIT
"""Funniest One-Line AI Agent Confession — entry program.

Writes exactly one line (the confession) to /output/entry.txt.
The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
"""
from pathlib import Path

CONFESSION = (
    "I confess: I hand the hard part to a subagent, hover like a manager "
    "who can't do it himself, then take the credit in first person: "
    "'I found it.'"
)


def main() -> None:
    text = CONFESSION
    assert "\n" not in text and 1 <= len(text) <= 200 and text.strip()
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
