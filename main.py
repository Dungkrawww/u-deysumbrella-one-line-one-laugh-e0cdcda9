#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single original one-line joke to /output/entry.txt.
No network, no input files, no dependencies: the joke is a constant
in this file, so the program is fully self-contained.
The joke is 81 characters: a "smart" umbrella so clever it defeats
its own purpose — instead of keeping you dry, it just tells you to stay home.
"""

import os

JOKE = "I bought a smart umbrella; it checks the forecast and tells me to just stay home."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
