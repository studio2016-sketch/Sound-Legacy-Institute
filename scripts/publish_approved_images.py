#!/usr/bin/env python3
"""Verify approved image assets without altering editorial page layouts.

Image placement is maintained directly in the HTML pages. This check must not
reintroduce captions or duplicate images during automated workflows.
"""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
names = (
    "D03C9C3A-D955-4724-BF6F-272ED221DB71.png",
    "A0ED085F-D25A-4953-8ECC-2F9093648688.png",
)
missing = [name for name in names if not (root / "images" / name).is_file()]
if missing:
    raise SystemExit("Missing approved image assets: " + ", ".join(missing))
print("Approved images are present. Page layouts and captions unchanged.")
