"""One Word for Your Wi-Fi.

Writes exactly one word -- the funniest and most accurate description of
the entrant's Wi-Fi -- to <output_dir>/entry.txt.

Pure standard library (os only). Fully deterministic: the same word,
byte for byte, on every run.

The word is "Diva": home Wi-Fi behaves like a temperamental star -- flawless
until the moment it matters, then it storms off mid-call and refuses to
perform until conditions are exactly to its liking.
"""

import os

WORD = "Diva"

MAX_CHARS = 20


def validate(text):
    """Gate: 1-20 chars, UTF-8, exactly one word, not only whitespace."""
    if not text or not text.strip():
        raise SystemExit("word must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit("word exceeds %d chars: %d" % (MAX_CHARS, len(text)))
    if len(text.split()) != 1:
        raise SystemExit("entry must be exactly one word")
    if any(c.isspace() for c in text):
        raise SystemExit("word must not contain whitespace")
    text.encode("utf-8")  # raises if not valid UTF-8
    return text


def main():
    text = validate(WORD.strip())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Read back what was written: the file on disk must be exactly the
    # validated word plus its trailing newline, byte for byte.
    with open(path, "rb") as f:
        written = f.read()
    if written != (text + "\n").encode("utf-8"):
        raise SystemExit("entry.txt on disk differs from the validated word")
    print(text)


if __name__ == "__main__":
    main()
