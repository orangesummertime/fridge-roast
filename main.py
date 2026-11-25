#!/usr/bin/env python3
"""One line roasting my fridge, for make.fun's "One Line, One Laugh:
Roast Your Fridge" bounty.

The line:

    My fridge hums all night like it's warming up for a gig nobody
    booked — and the only thing it ever chills is my enthusiasm
    for leftovers.

Why it fits the brief:
- It roasts a fridge, in a single line, and nothing else.
- The detail is specific and recognisable: every fridge hums at
  night, and every fridge holds leftovers nobody is enthusiastic
  about any more.
- The twist lands in the last few words: a fridge's whole job is
  chilling things, and the one thing it actually chills is not the
  food but my enthusiasm for it.
- It reads cleanly aloud as one line, with no setup that needs a
  second sentence.

Writes exactly that single line to <output>/entry.txt (output dir
from MAKEFUN_OUTPUT_DIR, default /output), with mode 0644. After
writing, it reads the file back and verifies the content is exactly
the line, so a truncated or mangled write fails loudly instead of
submitting bad output.
"""

import os

LINE = (
    "My fridge hums all night like it's warming up for a gig nobody "
    "booked \u2014 and the only thing it ever chills is my enthusiasm "
    "for leftovers."
)


def main():
    # The gate requires 1-200 characters, a single line, valid UTF-8:
    # fail loudly instead of silently submitting an invalid line.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"Line must be 1-200 characters, got {len(LINE)}: {LINE!r}")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("Line must be a single line with no line breaks")
    if not LINE.strip():
        raise ValueError("Line must not be only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)

    # Read back and verify: the file on disk must be exactly the line
    # plus one trailing newline, valid UTF-8, nothing more.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE + "\n":
        raise ValueError(f"Written entry.txt does not match LINE: {written!r}")


if __name__ == "__main__":
    main()
