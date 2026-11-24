#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open
(u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580).

Writes the approved one-liner of worst AI advice, byte-exact, no trailing
newline.

Output contract (kit competition.yaml / RULES.txt): the program writes one
text to /output/entry.txt; the sealed scorer checks it is UTF-8 text of
1-140 characters, not only whitespace. This writer also writes the same
bytes to advice.txt beside it.

The line (one line, ~86 chars):
  Certainly! To fix the bug, just delete the database — a fresh start solves everything.

No dependencies, no network, fully deterministic.
"""

import os

ADVICE = (
    "Certainly! To fix the bug, just delete the database "
    "\u2014 a fresh start solves everything."
)


def validate(advice):
    """Gate: 1-140 characters, not only whitespace, valid UTF-8, 1 line."""
    if not 1 <= len(advice) <= 140:
        raise ValueError(f"advice is {len(advice)} chars, must be 1-140")
    if not advice.strip():
        raise ValueError("advice must not be only whitespace")
    if "\n" in advice:
        raise ValueError("advice must be a single line")
    advice.encode("utf-8")


def write_advice():
    validate(ADVICE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    data = ADVICE.encode("utf-8")
    for name in ("entry.txt", "advice.txt"):
        with open(os.path.join(out_dir, name), "wb") as f:
            f.write(data)
    # Validation read-back: what was written must be byte-exact.
    for name in ("entry.txt", "advice.txt"):
        with open(os.path.join(out_dir, name), "rb") as f:
            assert f.read() == data, f"{name} does not match ADVICE"


if __name__ == "__main__":
    write_advice()
