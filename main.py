#!/usr/bin/env python3
"""Sorry, I Heard That Wrong - make.fun entry.

A smart speaker apologises to its owner after mishearing them.
The program writes the single-line apology to /output/entry.txt.
The line is 122 characters, within the bounty's 1-140 limit.
"""

import os

MAX_CHARS = 140

ENTRY = "Sorry, I heard 'set the mood' as 'set the moose loose' — he's in the kitchen, he's calm, and he likes your Wi-Fi password."


def validate_entry(text: str) -> str:
    """Check the entry against the bounty's gate before writing it.

    The sealed scorer accepts UTF-8 text of 1 to 140 characters that is
    not only white space. A line that fails here must never reach the
    output file, so raise instead of writing a bad entry.
    """
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be empty or only white space")
    if len(text) != len(stripped):
        raise ValueError("entry must not start or end with white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, over the {MAX_CHARS} limit")
    return text


def main() -> None:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
