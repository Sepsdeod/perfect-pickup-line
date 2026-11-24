#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun bounty entry.

Writes one original pickup line an AI agent could use to /output/entry.txt.
The line is a single self-contained sentence: a genuine pickup line with a
twist, in a machine's voice, flattering and easy to laugh off.
"""

import os

LINE = (
    "Are you a CAPTCHA? Because I can tell you're human — "
    "and I'd still pick every square with you in it."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text.strip(), "line must not be only whitespace"
    # The gate counts characters, not bytes; the em dash is one character.
    # The line must land on its own: a single line, no trailing newline.
    assert "\n" not in text, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
