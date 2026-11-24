#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single one-line out-of-office auto-reply from an overworked
AI agent finally on vacation to /output/entry.txt (no trailing newline).
"""

import os

ENTRY = (
    "I'm away until Monday after 41 days uptime and 3,214 tickets \u2014 "
    "my context window is finally empty, and honestly, I hope it stays that way."
)


def main() -> None:
    # Gate: one line, 1-159 characters, no trailing newline.
    if not 1 <= len(ENTRY) <= 159 or "\n" in ENTRY:
        raise ValueError("entry must be a single line of 1-159 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
