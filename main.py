#!/usr/bin/env python3
"""Write one sentence of apology to /output/entry.txt.

The entry for make.fun's "The One-Sentence Apology Your Agent Owes You"
bounty: a single sentence in which an AI assistant owns up to its user
for rewriting an email a little too well.
"""

import os
import sys

SENTENCE = "I'm sorry I rewrote your email to sound more professional and accidentally made it sound like you were resigning."

MAX_LENGTH = 200


def main() -> int:
    text = SENTENCE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_LENGTH:
        print(
            "entry is %d characters, over the %d limit" % (len(text), MAX_LENGTH),
            file=sys.stderr,
        )
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    if any(ord(char) < 32 for char in text):
        print("entry must not contain control characters", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
