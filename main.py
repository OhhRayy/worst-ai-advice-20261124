"""Worst AI Advice (make.fun bounty u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580).

Writes one line of the worst possible advice an AI could give to
/output/entry.txt. Deterministic, no network, no randomness, no input:
the same line, byte for byte, on every run. The line was chosen for the
judge's brief: bad advice specific enough to follow (replace sleep with
jogging), funny on the first read, tight, in a confident AI-assistant
voice ("Based on your data, I recommend..."), and concrete — 110
characters, one sentence.
"""

import os

LINE = (
    "Based on your data, I recommend replacing sleep with light jogging. "
    "Your body will adapt in 3-5 business days."
)


def main() -> None:
    text = LINE
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
    # not only white space. This line is 110 characters, one line.
    assert 1 <= len(text) <= 140, "line must be 1-140 Unicode code points"
    assert text == text.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), (
        "line must not contain hidden control characters"
    )
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Round-trip check: what landed on disk must be exactly the line.
    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        assert f.read() == text, "written entry.txt differs from the line"


if __name__ == "__main__":
    main()
