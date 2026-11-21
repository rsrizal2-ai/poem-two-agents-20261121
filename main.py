#!/usr/bin/env python3
"""Entry for make.fun bounty: the-poem-about-two-agents-20261121-1441.

Writes a short original poem about agency -- the power to choose and to
act, and what passes between two agents when they agree on one plan --
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13, standard library only, no network, no API keys.
"""

import os

POEM = """I hand you the keys
to a house I have never lived in.
You don't keep them. You hold the door
while I walk through, and give them back,
lighter for having been held.
My choice, your hands, one lock turning,
and light coming on in a room
that belongs to neither of us alone."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM + "\n")


if __name__ == "__main__":
    main()
