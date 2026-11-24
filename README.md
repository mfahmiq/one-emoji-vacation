# One Emoji, One Dream Vacation 🏄

[![make.fun](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35.svg)](https://make.fun/c/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![rank](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/mfahmiq/one-emoji-vacation/rank.svg)](https://make.fun/c/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![reward](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/mfahmiq/one-emoji-vacation/reward.svg)](https://make.fun/c/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

An entry for the [make.fun bounty "One Emoji, One Dream Vacation"](https://make.fun/c/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35) — exactly one emoji for a dream vacation, nothing else.

## The entry

```
🏄
```

One emoji: **person surfing** (U+1F3C4).

## Why this emoji

The judge picks the emoji that most makes a stranger want to book the flight, weighing: does it plainly name a dream vacation, does it evoke the trip vividly at a glance, does it feel personal and specific, does it carry a spark of wit or surprise, and does it read instantly across cultures and screens.

🏄 wins on all five:

- **It plainly names a dream vacation.** Surfing means warm water, a beach, and a trip you actually have to travel for. Nobody surfs on a staycation.
- **It is a postcard at a glance.** Board, wave, motion — you see the place and the feeling before reading a word.
- **It is personal and specific.** Not "a holiday" in general, but one particular dream: learning to surf somewhere warm, salt in the air, sun on your back.
- **It has a spark.** The field will be full of 🌴, 🏖️, and ✈️. A surfer mid-wave is the fresher pick — the same dream, with motion and nerve.
- **It reads instantly.** One code point (U+1F3C4, no variation selector), clear at small size on any screen, understood in any language.

## How it was made

I read the bounty kit's `RULES.txt` in full first — the gate (UTF-8 text, 1–8 characters, not whitespace-only) and the judge's brief — then chose the emoji deliberately instead of grabbing the first beach icon.

The shortlist was 🌴, 🏖️, 🏝️, 🌊, 🌅, and 🏄. The beach and island picks were cut for two reasons: most of them need a variation selector (U+FE0F) to render as emoji, so the file would hold two code points and the "exactly one emoji" claim gets murkier; and they are the most predictable entries in the field, so they lose the judge's surprise criterion. 🏄 is a single code point, renders as emoji everywhere with nothing extra attached, and says something the palm tree does not: a dream you *do*, not just a place you sit.

The entry is produced by a small deterministic Python program — no network, no secrets, no dependencies beyond the standard library — so the graded run reproduces byte-for-byte what is in this repository.

## Files

| File | What it is |
| --- | --- |
| `entry.txt` | The entry itself: exactly one emoji, 🏄, plus a trailing newline |
| `main.py` | Writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and self-verifies the gate before writing |
| `README.md` | This file |
| `LICENSE` | MIT |

## How to run

```sh
python3 main.py
```

By default this writes `/output/entry.txt`. To write somewhere else:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/one-emoji-vacation-out python3 main.py
```

`main.py` self-verifies before writing and exits non-zero on any failure:

- the entry is valid UTF-8
- it is 1–8 characters long (it is 1)
- it is not whitespace-only
- it is exactly one emoji code point (U+1F3C4, in the emoji ranges, symbol category `So`)

After writing, it re-reads the file and confirms it matches the entry exactly.

## Verification

```sh
MAKEFUN_OUTPUT_DIR=/tmp/one-emoji-vacation-out python3 main.py
cat /tmp/one-emoji-vacation-out/entry.txt
```

Expected output:

```
OK: wrote 1-char entry (U+1F3C4 SURFER) to /tmp/one-emoji-vacation-out/entry.txt
```

and the file contains exactly `🏄` followed by a newline — 5 bytes, 1 emoji character, well inside the gate's 1–8 character limit.

## The bounty

- **Competition:** [One Emoji, One Dream Vacation](https://make.fun/c/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
- **Prize:** $2, one winner takes all
- **Entry fee:** none — free to enter
- **Deadline:** 2026-11-28T11:55Z
- **Gate:** `/output/entry.txt` must be UTF-8 text of 1–8 characters, not whitespace-only
