"""The One-Line AI Excuse for Breaking Production.

Writes a single funny excuse, spoken by an AI agent to its human
right after breaking production, to /output/entry.txt.
"""

import os

LINE = (
    "Good news: I found the bug. Bad news: the bug was me "
    "\u2014 and I already deployed myself to production at 3 a.m."
)

assert 1 <= len(LINE) <= 180, f"entry is {len(LINE)} chars, must be 1-180"
assert "\n" not in LINE, "entry must be a single line"
assert LINE.strip() == LINE, "entry must not start or end with whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

print(f"Wrote {len(LINE)}-character entry to /output/entry.txt")
