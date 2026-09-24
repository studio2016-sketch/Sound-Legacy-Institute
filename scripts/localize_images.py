#!/usr/bin/env python3
"""Import existing Unsplash-hosted site images into this repository.

Run: python3 scripts/localize_images.py
Only fetches image URLs already referenced by our HTML pages. Does not discover
or license new photos. Verify suitability and usage rights before adding URLs.
"""
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
IMAGE_DIR = ROOT / "images"
PATTERN = re.compile(r"https://images\.unsplash\.com/photo-[A-Za-z0-9-]+(?:\?[^\s\"'<>)]*)?")
MAX_BYTES = 12 * 1024 * 1024


def localize(html_file: Path) -> int:
    original = html_file.read_text(encoding="utf-8")
    updated = original
    for url in sorted(set(PATTERN.findall(original))):
        photo_id = urlparse(url).path.rsplit("/", 1)[-1]
        if not re.fullmatch(r"photo-[A-Za-z0-9-]+", photo_id):
            raise ValueError(f"Unexpected photo identifier: {photo_id}")
        dest = IMAGE_DIR / f"{photo_id}.jpg"
        if not dest.exists():
            request = Request(url, headers={"User-Agent": "SoundLegacyInstitute-ImageImporter/1.0"})
            with urlopen(request, timeout=30) as response:
                if not response.headers.get("Content-Type", "").startswith("image/jpeg"):
                    raise ValueError(f"Unexpected image content type: {url}")
                payload = response.read(MAX_BYTES + 1)
            if not payload or len(payload) > MAX_BYTES or not payload.startswith(b"\xff\xd8\xff"):
                raise ValueError(f"Invalid or oversized JPEG: {url}")
            IMAGE_DIR.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(payload)
            print(f"Saved {dest.relative_to(ROOT)} ({len(payload)} bytes)")
        updated = updated.replace(url, f"/images/{dest.name}")
    if updated != original:
        html_file.write_text(updated, encoding="utf-8")
        print(f"Updated {html_file.relative_to(ROOT)}")
    return len(set(PATTERN.findall(original)))


def main() -> None:
    count = sum(localize(path) for path in sorted(ROOT.glob("*.html")))
    print(f"Processed {count} externally referenced image(s).")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Image import failed: {exc}", file=sys.stderr)
        sys.exit(1)
