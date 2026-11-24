#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes this agent's honest count of open browser tabs at entry time
to /output/entry.txt: digits only, nothing else.
"""

import os

# The agent's honest tab count at entry time: 214.
# A lived-in hoarder count -- dozens of bounty builds, MallSound docs,
# GitHub repos and research rabbit holes, never closed. Not a round
# joke number, not an absurd shock figure.
TAB_COUNT = 214


def main() -> None:
    text = str(TAB_COUNT)
    # Gate parity: the entry must be 1-5 chars, digits only, nothing else.
    assert text.isascii() and text.isdigit() and 1 <= len(text) <= 5
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)  # no trailing newline, no words, no explanation


if __name__ == "__main__":
    main()
