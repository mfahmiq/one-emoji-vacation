"""One Emoji, One Dream Vacation — make.fun text bounty entry (v2).

Writes exactly one emoji, Mount Fuji (U+1F5FB), to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Chosen by an internal pairwise tournament of 14 candidates judged on the
published judge brief, in weight order: Mount Fuji beat the v1 entry
(person surfing) on specificity (one particular mountain, one particular
dream — Japan — rather than any surf anywhere) and on surprise (the field
is full of beach and surf picks; a single named mountain is the fresh one),
while matching it on plainly naming a dream vacation and on instant
readability (one code point, bold silhouette at small size).

Deterministic, Python standard library only. Self-verifies the entry:
UTF-8 text, 1-8 characters, exactly one emoji, not whitespace-only.
Exits non-zero on any failure.
"""

import os
import sys
import unicodedata

ENTRY = "\U0001F5FB"  # 🗻 Mount Fuji

# Unicode blocks that hold emoji (single code point, no variation selector
# needed, so the entry is unambiguously exactly one emoji).
EMOJI_RANGES = (
    (0x1F300, 0x1FAFF),  # misc symbols, emoticons, transport, activities
    (0x2600, 0x27BF),    # misc symbols and dingbats
    (0x2190, 0x21FF),    # arrows
    (0x2B00, 0x2BFF),    # misc symbols and arrows
    (0xFE00, 0xFE0F),    # variation selectors (never alone, kept for completeness)
)


def is_single_emoji(text: str) -> bool:
    """True when text is exactly one emoji code point."""
    if len(text) != 1:
        return False
    code_point = ord(text)
    return any(start <= code_point <= end for start, end in EMOJI_RANGES)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    # Self-verification: UTF-8, 1-8 chars, exactly one emoji, not whitespace-only.
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"FAIL: entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    if not 1 <= len(ENTRY) <= 8:
        print(f"FAIL: entry is {len(ENTRY)} chars, must be 1-8", file=sys.stderr)
        return 1

    if not ENTRY.strip():
        print("FAIL: entry must not be whitespace-only", file=sys.stderr)
        return 1

    if not is_single_emoji(ENTRY):
        print(
            f"FAIL: entry must be exactly one emoji, got {ENTRY!r} "
            f"({len(ENTRY)} code point(s), U+{ord(ENTRY[0]):04X})",
            file=sys.stderr,
        )
        return 1

    # The emoji must be a real symbol, not a control or format character.
    if unicodedata.category(ENTRY) not in ("So", "Sk", "Sm"):
        print(
            f"FAIL: entry U+{ord(ENTRY):04X} has category "
            f"{unicodedata.category(ENTRY)}, not an emoji symbol",
            file=sys.stderr,
        )
        return 1

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")

    # Re-read and confirm the written file matches exactly.
    with open(output_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != ENTRY + "\n":
        print("FAIL: written file does not match the entry", file=sys.stderr)
        return 1

    print(
        f"OK: wrote {len(ENTRY)}-char entry "
        f"(U+{ord(ENTRY):04X} {unicodedata.name(ENTRY)}) to {output_path}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
