#!/usr/bin/env python3
"""Entry program: The Meeting That Should Have Been an Email.

Writes one joke line to /output/entry.txt.

The line (105 characters):
  I muted myself to type the email this meeting was supposed to replace, then unmuted to say 'great point'.

Deterministic: identical bytes on every run. No network access, no
dependencies, no environment reads, no files outside this repository.
"""

import os

LINE = "I muted myself to type the email this meeting was supposed to replace, then unmuted to say 'great point'."

OUTPUT_PATH = "/output/entry.txt"


def main():
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("line is %d characters, outside the 1-200 gate" % len(LINE))
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(LINE.encode("utf-8"))
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
