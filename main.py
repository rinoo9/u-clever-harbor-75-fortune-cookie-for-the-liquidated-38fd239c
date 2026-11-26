"""Fortune Cookie for the Liquidated Trader.

A single fortune cookie message for a crypto trader who has just been
liquidated. The program validates the line (one line, at most 20 words,
non-blank) and writes it to /output/entry.txt.
"""

import os

ENTRY = "Lucky numbers: 100, 5, 0. That is your leverage, your stop-loss, and your remaining balance."

MAX_WORDS = 20


def main():
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    words = line.split()
    if len(words) > MAX_WORDS:
        raise ValueError(f"entry has {len(words)} words, more than the {MAX_WORDS} allowed")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
