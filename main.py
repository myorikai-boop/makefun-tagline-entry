#!/usr/bin/env python3
"""make.fun tagline entry: writes one tagline to /output/entry.txt.

Deterministic, standard library only, no network. Two runs on the same
machine write identical bytes.
"""
import os

TAGLINE = "Build the software. The metric decides. USDC settles."


def main() -> None:
    text = TAGLINE.strip()
    if not (1 <= len(text) <= 280):
        raise SystemExit("tagline length out of the allowed range")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
