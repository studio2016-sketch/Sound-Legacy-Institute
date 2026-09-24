#!/usr/bin/env python3
"""Connect approved Sound Legacy imagery once the original files are in images/."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
IMAGES=ROOT/"images"
CLASSROOM=IMAGES/"D03C9C3A-D955-4724-BF6F-272ED221DB71.png"
PERFORMANCE=IMAGES/"A0ED085F-D25A-4953-8ECC-2F9093648688.png"
if not CLASSROOM.exists() or not PERFORMANCE.exists():
    print("Waiting for both approved photographs in images/. No pages changed.")
    raise SystemExit(0)
index=ROOT/"index.html"
html=index.read_text()
if "D03C9C3A-D955-4724-BF6F-272ED221DB71.png" not in html:
    html=html.replace(".hero { position:relative;",".hero { background-image:linear-gradient(90deg,rgba(5,20,37,.91),rgba(5,20,37,.36)),url('/images/D03C9C3A-D955-4724-BF6F-272ED221DB71.png') !important; background-position:center; background-size:cover; position:relative;")
    html=html.replace('<section class="impact" id="programs">','<section class="wrap" aria-label="Student performance" style="padding:0 0 100px"><img src="/images/A0ED085F-D25A-4953-8ECC-2F9093648688.png" alt="Illustrative image of a young jazz ensemble performing with a mentor" loading="lazy" style="display:block;width:100%;max-height:650px;object-fit:cover"><p style="font-size:.78rem;color:#667;margin-top:12px">Concept imagery illustrating the Institute’s vision for mentorship and performance.</p></section><section class="impact" id="programs">')
    index.write_text(html)
work=ROOT/"the-work.html"
html=work.read_text()
html=html.replace('<section class="w intro">', '<section class="w" style="padding:45px 0 0"><img src="/images/A0ED085F-D25A-4953-8ECC-2F9093648688.png" alt="Illustrative image of a young jazz ensemble performing with a mentor" loading="lazy" style="width:100%;max-height:600px;object-fit:cover"><p style="font-size:.8rem;color:#596778">Concept imagery illustrating the Institute’s educational vision.</p></section><section class="w intro">')
html=html.replace('<section class="story">', '<section class="w" style="padding:0 0 70px"><img src="/images/D03C9C3A-D955-4724-BF6F-272ED221DB71.png" alt="Illustrative image of a music educator guiding young musicians" loading="lazy" style="width:100%;max-height:600px;object-fit:cover"></section><section class="story">')
work.write_text(html)
giving=ROOT/"give.html"
html=giving.read_text()\nif "A0ED085F-D25A-4953-8ECC-2F9093648688.png" not in html:\n    html=html.replace('<section class="section soft" id="ways">', '<section class="wrap" style="padding:0 0 70px"><img src="/images/A0ED085F-D25A-4953-8ECC-2F9093648688.png" alt="Illustrative image of students performing together" loading="lazy" style="width:100%;max-height:580px;object-fit:cover"></section><section class="section soft" id="ways">')
giving.write_text(html)
print("Approved imagery connected to homepage, The Work and Giving.")
