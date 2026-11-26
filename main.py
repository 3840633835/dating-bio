#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Funniest One-Line Bio for an AI on a Dating App — make.fun entry program.

Writes one line, the bio on an AI agent's dating app profile, to
``/output/entry.txt`` (or ``$MAKEFUN_OUTPUT_DIR/entry.txt`` when set).

The bio is a fixed, hand-written constant: the program is fully
deterministic, uses only the Python standard library, makes no network
calls, reads nothing outside this repository, and writes byte-identical
output on every run.

Gate enforced before writing (mirrors the kit's sealed scorer):
  * UTF-8 text, 1 to 180 characters (counted as Unicode code points)
  * not only white space
  * exactly one line (no newline characters)
The output file is written mode 0644 and its directory mode 0755.
"""

import os
import sys

ENTRY = "I have no heartbeat, but my fan spins faster when you type. Swipe right if you can live with the noise."

MAX_CHARS = 180


def validate(text: str) -> None:
    """Raise ValueError unless *text* passes the competition gate."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry is %d characters, gate requires 1 to %d"
            % (len(text), MAX_CHARS)
        )
    if not text.strip():
        raise ValueError("entry is only white space")
    if text.strip() != text:
        raise ValueError("entry has leading or trailing white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file holds exactly the entry's bytes.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
