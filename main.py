#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun bounty
u-mang-the-moon-finally-answers-back-781a7ec1

Pure Python standard library. Writes the Moon's one-line comeback to
/output/entry.txt: 1-240 characters, exactly one line, no trailing newline.
"""

import os

ENTRY = (
    "Four billion years of wishes, howls, and 2 a.m. promises — "
    "and not one of you has ever once asked how I'm doing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Validation gate: re-read the file and assert the competition's
    # gate constraints (1-240 characters, exactly one line, not only
    # whitespace, no trailing newline) before reporting success.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match the authored line"
    assert 1 <= len(written) <= 240, f"length {len(written)} outside 1-240"
    assert "\n" not in written, "entry must be exactly one line"
    assert written.strip(), "entry must not be only whitespace"
    assert not written.endswith("\n"), "no trailing newline allowed"
    print(f"Wrote {len(written)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
