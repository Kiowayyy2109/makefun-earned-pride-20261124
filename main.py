#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line of quiet, earned pride to /output/entry.txt:
a home baker, forty failed loaves behind her, opening the oven
to find this one finally rose. No input, no network, no secrets:
the line is fixed, so both grading runs produce the same file.
"""

import os

ENTRY = (
    "After forty failed loaves, she wiped the flour from her hands, "
    "opened the oven, and this one rose."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 240, f"entry must be 1-240 chars, got {len(line)}"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read back and verify: the graded file must be byte-identical to
    # the line, so a partial or mangled write fails loudly here instead
    # of silently shipping a broken entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == line, "read-back mismatch in entry.txt"
    print(f"wrote {len(line)} chars ({len(line.encode('utf-8'))} bytes) to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
