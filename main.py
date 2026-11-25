#!/usr/bin/env python3
"""Worst Superpower — u-suroto-worst-superpower-461dcdbe.

Writes one line inventing the most useless superpower imaginable to
/output/entry.txt, validating the gate (UTF-8, 1-140 chars, not blank)
before writing.

The line: a hero who can stop time for exactly one second — and already
spent it, in 1987, dodging a bee. The power is gone before the story
starts, which is the whole joke. 88 characters, one line, no setup needed.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = "I can stop time for exactly one second \u2014 but I already used it, in 1987, to avoid a bee."


def main() -> None:
    if not 1 <= len(LINE) <= 140:
        raise SystemExit(f"gate fail: length {len(LINE)} outside 1-140 chars")
    if not LINE.strip():
        raise SystemExit("gate fail: line is blank")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Re-read and re-check what actually landed on disk.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("gate fail: written file does not match line")
    if not 1 <= len(written) <= 140 or not written.strip():
        raise SystemExit("gate fail: written file fails the gate")


if __name__ == "__main__":
    main()
