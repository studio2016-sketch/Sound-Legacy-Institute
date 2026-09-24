#!/usr/bin/env python3
"""Connect approved Sound Legacy imagery once the original files are in images/."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
IMAGES=ROOT/"images"
CLASSROOM=IMAGES/"sound-legacy-mentorship.jpg"
PERFORMANCE=IMAGES/"sound-legacy-student-performance.jpg"
if not CLASSROOM.exists() or not PERFORMANCE.exists():
    print("Waiting for both approved photographs in images/. No pages changed.")
    raise SystemExit(0)
index=ROOT/"index.html"
html=index.read_text()
if "sound-legacy-mentorship.jpg" not in html:
    html=html.replace(".hero { position:relative;",".hero { background-image:linear-gradient(90deg,rgba(5,20,37,.91),rgba(5,20,37,.36)),url('/images/sound-legacy-mentorship.jpg') !important; background-position:center; background-size:cover; position:relative;")
    html=html.replace('<section class="impact" id="programs">','<section class="wrap" aria-label="Student performance" style="padding:0 0 100px"><img src="/images/sound-legacy-student-performance.jpg" alt="Illustrative image of a young jazz ensemble performing with a mentor" loading="lazy" style="display:block;width:100%;max-height:650px;object-fit:cover"><p style="font-size:.78rem;color:#667;margin-top:12px">Concept imagery illustrating the Institute’s vision for mentorship and performance.</p></section><section class="impact" id="programs">')
    index.write_text(html)
work=ROOT/"the-work.html"
html=work.read_text()
html=html.replace("/images/photo-1493225457124-a3eb161ffa5f.jpg","/images/sound-legacy-student-performance.jpg")
html=html.replace("/images/photo-1520523839897-bd0b52f945a0.jpg","/images/sound-legacy-mentorship.jpg")
work.write_text(html)
giving=ROOT/"give.html"
html=giving.read_text().replace("/images/photo-1516280440614-37939bbacd81.jpg","/images/sound-legacy-mentorship.jpg")
giving.write_text(html)
print("Approved imagery connected to homepage, The Work and Giving.")
