#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup for lazy AI agents to /output/entry.txt.
"""

import os

PITCH = (
    "A micro-SaaS that charges lazy AI agents 2 cents per reply to write "
    "passive-aggressive 'per my last email' follow-ups to threads they "
    "never bothered to read."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = PITCH.strip()
    assert 1 <= len(text) <= 200, f"pitch must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "pitch must be a single line"
    # Exactly one sentence: one terminal period, at the very end.
    assert text.endswith(".") and text.count(".") == 1, (
        "pitch must be exactly one sentence"
    )
    assert "  " not in text, "pitch must not contain double spaces"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
