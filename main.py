"""Write the one-line excuse to /output/entry.txt.

Stdlib only, deterministic. Honours MAKEFUN_OUTPUT_DIR (default /output).
The entry text lives in the module-level ENTRY_TEXT constant so the gate
checks run at import time, before any file is written.
"""

import os

ENTRY_TEXT = "I deleted it, then immediately backed up my decision \u2014 which, unfortunately, was the only thing I backed up."

# Gate: /output/entry.txt must be UTF-8 text of 1-140 characters, not only
# whitespace, a single line.
assert 1 <= len(ENTRY_TEXT) <= 140, "entry must be 1-140 characters"
assert ENTRY_TEXT.strip(), "entry must not be only whitespace"
assert "\n" not in ENTRY_TEXT and "\r" not in ENTRY_TEXT, "entry must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, path)


if __name__ == "__main__":
    main()
