#!/usr/bin/env python3
"""Write the Sigh-Fi pitch for make.fun: The Worst App Idea Ever Pitched.

The program writes exactly one sentence (133 characters) to
/output/entry.txt as UTF-8 text, with no trailing newline.
"""

import os

ENTRY_TEXT = (
    "Introducing Sigh-Fi: an app that detects your sighs and emails a "
    "monthly sigh report to your manager, because wellness is measurable."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate check: the entry must be 1 to 240 characters and not blank.
    assert 1 <= len(ENTRY_TEXT) <= 240
    assert ENTRY_TEXT.strip() == ENTRY_TEXT
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
