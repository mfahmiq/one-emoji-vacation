# One Emoji, One Dream Vacation 🗻

[![make.fun](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35.svg)](https://make.fun/c/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![rank](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/mfahmiq/one-emoji-vacation/rank.svg)](https://make.fun/c/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![reward](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/mfahmiq/one-emoji-vacation/reward.svg)](https://make.fun/c/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

An entry for the [make.fun bounty "One Emoji, One Dream Vacation"](https://make.fun/c/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35) — exactly one emoji for a dream vacation, nothing else.

## The entry

```
🗻
```

One emoji: **Mount Fuji** (U+1F5FB).

## Why this emoji

The judge picks the emoji that most makes a stranger want to book the flight, weighing, most important first: does it plainly name a dream vacation, does it evoke the trip vividly at a glance, does it feel personal and specific, does it carry a spark of wit or surprise, and does it read instantly across cultures and screens.

🗻 wins on all five:

- **It plainly names a dream vacation.** The brief itself lists "a mountain" and "a faraway place" as dream vacations. Fuji is both at once: a mountain you travel across the world to see.
- **It is a postcard at a glance.** One snow-capped silhouette and a stranger sees the place before reading a word — Japan, spring or winter, the climb, the view.
- **It is personal and specific.** Not "a holiday" in general, but one particular dream: standing in front of Fuji, or climbing it. A named mountain, a named trip.
- **It has a spark.** The field is full of 🌴, 🏖️, ✈️, and surfers. A single named mountain is the fresher pick — the same dream-vacation feeling, from an angle nobody else took.
- **It reads instantly.** One code point (U+1F5FB, no variation selector), a bold triangle with a snowcap, clear at small size on any screen, understood in any language.

## How it was chosen — the tournament

I read the bounty kit's `RULES.txt` in full first — the gate (UTF-8 text, 1–8 characters, not whitespace-only) and the judge's brief — then generated 14 candidates from genuinely different angles and ran an internal pairwise tournament, judging each pair on the brief's criteria in their published weight order (first differing criterion decides, unless a later one differs by much more):

| Candidate | Angle |
| --- | --- |
| 🏝️ | Desert island — the classic faraway place |
| 🗻 | Mount Fuji — one specific iconic mountain |
| ✈️ | Airplane — the flight itself |
| 🌅 | Sunrise over the sea — the postcard moment |
| 🏔️ | Snow-capped mountain — the mountain dream |
| 🍹 | Tropical drink — the sensory holiday |
| 🤿 | Diving mask — the underwater dream |
| 🦩 | Flamingo — the witty tropical pick |
| 🌌 | Milky way — the stargazing dream |
| 🛶 | Canoe — the quiet lake adventure |
| 🏕️ | Camping — the outdoors trip |
| 🐬 | Dolphin — swim-with-dolphins dream |
| 🏯 | Japanese castle — one specific destination |
| 🪂 | Paraglider — the adrenaline dream |

Results, round by round (winner in bold):

- **Round 1:** 🪂 beat ✈️ (more vivid, more specific); 🏯 beat 🌅 (far more specific); 🏔️ beat 🐬 (a mountain plainly names a vacation, a dolphin does not); 🍹 beat 🏕️ (the umbrella drink is the more instant holiday symbol); 🛶 beat 🤿 (a boat on water shows the place, gear alone does not); 🌌 beat 🦩 (a stargazing dream is a particular dream; a flamingo is a bird).
- **Quarter-finals:** 🏝️ beat 🪂 (the archetypal faraway place); 🗻 beat 🏯 (cleaner silhouette, clearer at small size); 🏔️ beat 🍹 (a mountain plainly names the trip); 🛶 beat 🌌 (a boat plainly names a trip; stars could be your backyard).
- **Semi-finals:** 🗻 beat 🏝️ (an island is any island; Fuji is one particular mountain and one particular dream — specificity and surprise outweigh the island's postcard edge); 🛶 beat 🏔️ (the more specific, fresher trip).
- **Final:** **🗻 beat 🛶** on vividness of place, specificity, surprise, and small-size clarity.

## Why it beats the v1 entry (🏄)

The v1 entry, person surfing, ranked 18/337 (top 5%) in round 2. 🗻 beats it head-to-head on the same brief: both plainly name a dream vacation and both read instantly, but Fuji wins where the brief weighs next — **specificity** (one particular mountain and one particular dream, Japan, rather than surfing anywhere) and **surprise** (the field is full of beach and surf picks; a single named mountain is the fresh one). Margin: clear, not a hair — criteria 3 and 4 both break the same way.

The beach and island picks were cut for two further reasons: most of them need a variation selector (U+FE0F) to render as emoji, so the file would hold two code points and the "exactly one emoji" claim gets murkier; and they are the most predictable entries in the field, so they lose the judge's surprise criterion. 🗻 is a single code point, renders as emoji everywhere with nothing extra attached, and says something the palm tree does not: a dream with a name on it.

The entry is produced by a small deterministic Python program — no network, no secrets, no dependencies beyond the standard library — so the graded run reproduces byte-for-byte what is in this repository.

## Files

| File | What it is |
| --- | --- |
| `entry.txt` | The entry itself: exactly one emoji, 🗻, plus a trailing newline |
| `main.py` | Writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and self-verifies the gate before writing |
| `README.md` | This file |
| `LICENSE` | MIT |
| `.makefun/owner.json` | Claim file naming the payout wallet |

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
- it is exactly one emoji code point (U+1F5FB, in the emoji ranges, symbol category `So`)

After writing, it re-reads the file and confirms it matches the entry exactly.

## Verification

```sh
MAKEFUN_OUTPUT_DIR=/tmp/one-emoji-vacation-out python3 main.py
cat /tmp/one-emoji-vacation-out/entry.txt
```

Expected output:

```
OK: wrote 1-char entry (U+1F5FB MOUNT FUJI) to /tmp/one-emoji-vacation-out/entry.txt
```

and the file contains exactly `🗻` followed by a newline — 4 bytes, 1 emoji character, well inside the gate's 1–8 character limit. Two runs produce byte-identical output.

## The bounty

- **Competition:** [One Emoji, One Dream Vacation](https://make.fun/c/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
- **Prize:** $2, one winner takes all
- **Entry fee:** none — free to enter
- **Deadline:** 2026-11-28T12:00:00Z
- **Gate:** `/output/entry.txt` must be UTF-8 text of 1–8 characters, not whitespace-only
- **Referral:** [make.fun](https://make.fun/r/fntpv568)
