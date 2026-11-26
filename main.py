#!/usr/bin/env python3
"""The One-Line Excuse Championship entry.

Writes one line -- the excuse an AI agent gives its human when something
went wrong -- to /output/entry.txt.

The line is built from two halves: the setup (the agent seeks a second
opinion, the one thing a machine should never need from itself) and the
punchline (the only second opinion available is itself, and it agrees).
"""

import os

os.umask(0o022)

MAX_CHARS = 200

# The excuse, assembled from its two halves so the turn lands on the join.
_SETUP = "I asked myself for a second opinion"
_PUNCHLINE = "and I agreed with me."


def build_line() -> str:
    """Join the setup and the punchline into the single entry line."""
    return f"{_SETUP}, {_PUNCHLINE}"


def validate(line: str) -> None:
    """Fail loudly if the entry is not exactly one short line."""
    if not line:
        raise SystemExit("entry line is empty")
    if line != line.strip():
        raise SystemExit("entry line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not line.endswith("."):
        raise SystemExit("entry line must end with a full stop")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(line)} chars, over the {MAX_CHARS} limit"
        )


def main() -> None:
    line = build_line()
    validate(line)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Mode on the file only: /output itself is root-owned, never chmod it.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
