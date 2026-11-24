"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, written by a house cat
about its human, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR). The
text is fixed: no randomness, no network, no clock, so two runs write
the same bytes, which is what the determinism check wants.
"""

import os

LINE = "One star. The food bowl was empty for four whole minutes while my human stared at a glowing rectangle. I am taking my business to the dog."

MAX_CHARS = 200


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(f"line must be 1-{MAX_CHARS} chars, got {len(line)}")
    if "\n" in line:
        raise SystemExit("line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
