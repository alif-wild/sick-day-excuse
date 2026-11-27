#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — one line that gets you out of work.

Writes a single sick-day excuse to /output/entry.txt.
"""

LINE = "I can't come in today — my smart fridge locked me out of the kitchen and I'm currently negotiating my release."


def main() -> None:
    import os

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
