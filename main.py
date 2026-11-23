"""One Letter for Your Day.

Writes exactly one letter to /output/entry.txt: the letter D.

D stands for "doomscrolling" -- the word for today: hours lost thumbing
through disaster news in bed, phone glow at 2am, every refresh worse
than the last. Vivid, funny, and (sadly) true.

Standard library only. No imports beyond os/sys/pathlib, no network,
no files read. The output is a single byte, no trailing newline: the
gate requires /output/entry.txt to be UTF-8 text of exactly 1 character.
"""

import os
import sys

LETTER = "D"
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Self-check: the gate requires exactly 1 UTF-8 character, no newline.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LETTER:
        print(f"error: expected exactly {LETTER!r}, got {written!r}",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
