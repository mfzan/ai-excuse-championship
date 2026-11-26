#!/usr/bin/env python3
"""The One-Line Excuse Championship entry.

Writes one line -- the excuse an AI agent gives its human when something
went wrong -- to /output/entry.txt.
"""

import os

os.umask(0o022)

LINE = "I asked myself for a second opinion, and I agreed with me."
MAX_CHARS = 200


def main() -> None:
    if len(LINE) > MAX_CHARS:
        raise SystemExit(f"entry is {len(LINE)} chars, over the {MAX_CHARS} limit")
    if "\n" in LINE.strip():
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
