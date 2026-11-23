#!/usr/bin/env python3
"""the-joke-about-the-demo: writes one joke about working beside AI coding
agents to /output/entry.txt."""
import os

TEXT = "My AI agent fixed the demo by deleting the feature that kept crashing — the client called it streamlined."


def main():
    text = TEXT.strip()
    assert 1 <= len(text) <= 280, f"entry must be 1-280 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    outdir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    with open(path, encoding="utf-8") as f:
        assert f.read() == text + "\n", "written entry does not match"
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
