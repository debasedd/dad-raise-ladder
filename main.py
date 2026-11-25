#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes a single original one-line dad joke to /output/entry.txt.

The joke: a setup a dad would actually say out loud (asking his wife for a
raise) with a fast, clean turn — she hands him a ladder — and a kicker that
finishes the pun in two words: "Start here." One sentence, one read, the
punchline lands inside the line and the groan is earned. The line is 79 of
the 140 allowed characters.
"""

import os

JOKE = "I told my wife I needed a raise. She handed me a ladder and said, 'Start here.'"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE.strip()
    # Gate: UTF-8 text, 1 to 140 characters, not only whitespace.
    assert 1 <= len(text) <= 140, f"joke is {len(text)} characters"
    assert text.strip(), "joke is only whitespace"
    assert "\n" not in text, "joke must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
