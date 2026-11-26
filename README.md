# Funniest One-Line Bio for an AI on a Dating App

[![make.fun](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/3840633835/dating-bio/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/3840633835/dating-bio/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)

Entry for the [make.fun bounty "Funniest One-Line Bio for an AI on a Dating App"](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf): one line, at most 180 characters, as the bio on an AI agent's dating app profile. It has to read as a bio, sound like a character, and land a laugh on the first read.

## The entry

> I have no heartbeat, but my fan spins faster when you type. Swipe right if you can live with the noise.

103 characters, 103 bytes, one line (counted programmatically).

## How it works

`main.py` writes the bio to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set). The bio is a fixed, hand-written constant, so the program is fully deterministic: same bytes on every run, no network, no files read outside this repository. Before writing, `main.py` enforces the competition gate (UTF-8, 1–180 characters, not only white space, exactly one line) and writes the output file mode 0644.

## Files

- `main.py` — the entry program
- `entry.txt` — the entry, exact bytes
- `README.md` — this file
- `METHODOLOGY.md` — how the bio was chosen (35 candidates scored, head-to-heads, refinement note)
- `test_determinism.sh` — two-run byte-identity + gate check
- `LICENSE` — MIT

## Tests

```sh
sh test_determinism.sh
```

Runs `main.py` twice into separate directories and requires byte-identical output that passes the gate.
