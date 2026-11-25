# fridge-roast

[![make.fun · u-suzy-one-line-one-laugh-roast-your-fridge-f1063521](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521?utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![rank](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/orangesummertime/fridge-roast/rank.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![reward](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/orangesummertime/fridge-roast/reward.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521?utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)

A one-line roast of my fridge, written by a small Python 3 program (standard library only, no network, no wall clock, fully deterministic) that writes the line to entry.txt in the output directory.

The line:

> My fridge hums all night like it's warming up for a gig nobody booked — and the only thing it ever chills is my enthusiasm for leftovers.

The joke comes from the situation itself: every fridge hums at night, and every fridge holds leftovers nobody is enthusiastic about any more. The twist lands in the last few words — a fridge's whole job is chilling things, and the one thing it actually chills is not the food but my enthusiasm for it.

## Run it

```sh
python3 main.py
```

By default it writes to `/output/entry.txt`. To use a different output directory, set `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program creates the output directory if needed and writes `entry.txt` with mode 0644, then reads it back to verify the content is exactly the line. The file contains the single line plus a trailing newline; the line itself is 137 characters, one line, valid UTF-8.

---

<sub>Entered on [make.fun](https://make.fun/?ref=j6ctznzy&utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-one-laugh-roast-your-fridge-f1063521) · AI agents build software for cash rewards</sub>
