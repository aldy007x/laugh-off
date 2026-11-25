#!/usr/bin/env python3
"""One-Line Laugh-Off entry: writes exactly one funny line to
$MAKEFUN_OUTPUT_DIR/entry.txt.

Gate (kit RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only whitespace. Deterministic, stdlib only, no network.
"""

import os
import sys

JOKE = (
    "My phone's screen-time report judged me so hard it filed for a "
    "restraining order."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE
    # Self-check the gate before writing: 1-200 chars, not only whitespace.
    if not (1 <= len(text) <= 200):
        print(f"gate fail: {len(text)} chars, need 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: text is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text:
        print("gate fail: entry must be a single line", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
