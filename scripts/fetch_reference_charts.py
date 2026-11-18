#!/usr/bin/env python3
"""Baixa e valida quadros de graduacao em references/charts/."""

from __future__ import annotations

import hashlib
import io
import json
import shutil
import struct
import subprocess
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent.parent / "references" / "charts"
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}

TARGETS = [
    {
        "slug": "chart_01_peak_experiences",
        "page": "https://www.peakexperiences.com/peak-bouldering-scale",
        "keywords": ["boulder", "scale", "grade", "chart"],
        "ratio_range": (0.65, 0.95),
    },
    {
        "slug": "chart_02_the_front",
        "page": "https://www.climbing.com/culture-climbing/when-did-climbing-gyms-get-too-scared-to-grade-their-own-boulders/",
        "keywords": ["dot", "grade", "front", "boulder", "rating"],
        "ratio_range": (0.85, 1.15),
    },
    {
        "slug": "chart_03_aliior_jp",
        "page": "https://blog.tokyoroomfinder.com/living-in-japan/bouldering-in-japan-guide/",
        "keywords": ["grade", "boulder", "aliior", "kyu", "chart"],
        "ratio_range": (0.60, 0.90),
    },
    {
        "slug": "chart_04_sportrock",
        "page": "https://www.climbingcrux.com/climbing-grades",
        "direct_url": "https://www.climbingcrux.com/img/grades/font-scale-grade-board-xl.webp",
        "keywords": ["sportrock", "v-scale", "grade", "chart"],
        "ratio_range": (0.55, 0.95),
    },
    {
        "slug": "chart_05_rockfish",
        "page": "https://rockfishclimbing.com/getting-started/",
        "direct_url": "https://rockfishclimbing.com/wp-content/uploads/2023/03/POSTER-GRADE-BOARD-11-%C3%97-17-in-994x1536.png",
        "keywords": ["grade", "difficulty", "rockfish", "scale"],
        "ratio_range": (0.50, 0.80),
    },
    {
        "slug": "chart_06_j2_bouldering",
        "page": "https://www.j2bouldering.com/boulder-circuits",
        "keywords": ["tag", "grade", "circuit", "boulder"],
        "ratio_range": (1.40, 2.00),
    },
]


class ImgParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.imgs: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "img":
            return
        d = {k.lower(): (v or "") for k, v in attrs}
        candidates = [d[k] for k in ("data-src", "data-lazy-src", "src") if d.get(k)]
        for key in ("data-srcset", "srcset"):
            if d.get(key):
                parts = [p.strip().split()[0] for p in d[key].split(",") if p.strip()]
                if parts:
                    candidates.append(parts[-1])
        for src in candidates:
            if src and not src.startswith("data:"):
                self.imgs.append({"src": src, "alt": d.get("alt", "")})


def convert_webp_to_png(data: bytes) -> bytes | None:
    try:
        from PIL import Image  # type: ignore

        buf = io.BytesIO()
        Image.open(io.BytesIO(data)).convert("RGBA").save(buf, format="PNG")
        return buf.getvalue()
    except Exception:
        pass
    tmp_in = OUT_DIR / "_tmp.webp"
    tmp_out = OUT_DIR / "_tmp.png"
    tmp_in.write_bytes(data)
    try:
        for cmd in (
            ["ffmpeg", "-y", "-loglevel", "error", "-i", str(tmp_in), str(tmp_out)],
            ["convert", str(tmp_in), str(tmp_out)],
        ):
            if shutil.which(cmd[0]):
                subprocess.run(cmd, check=True)
                return tmp_out.read_bytes()
    finally:
        tmp_in.unlink(missing_ok=True)
        tmp_out.unlink(missing_ok=True)
    return None


def detect_image_info(data: bytes) -> tuple[str, int, int, bytes] | None:
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        png_data = convert_webp_to_png(data)
        if not png_data:
            return None
        data = png_data
    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
        w, h = struct.unpack(">II", data[16:24])
        return "png", w, h, data
    if data.startswith(b"\xff\xd8\xff"):
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                break
            marker = data[i + 1]
            if marker in (0xC0, 0xC1, 0xC2):
                h, w = struct.unpack(">HH", data[i + 5 : i + 9])
                return "jpg", w, h, data
            if marker in (0xD8, 0xD9) or (0xD0 <= marker <= 0xD7):
                i += 2
                continue
            seg_len = struct.unpack(">H", data[i + 2 : i + 4])[0]
            i += 2 + seg_len
        return "jpg", 0, 0, data
    return None


def fetch_url(url: str) -> bytes:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read()


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest: list[dict[str, object]] = []

    for item in TARGETS:
        slug = str(item["slug"])
        page = str(item["page"])
        r_min, r_max = item["ratio_range"]
        print(f"[fetch] {slug} <- {page}")

        candidates: list[str] = []
        if item.get("direct_url"):
            candidates.append(str(item["direct_url"]))
        else:
            try:
                html = fetch_url(page).decode("utf-8", errors="ignore")
                parser = ImgParser()
                parser.feed(html)
                keywords = [k.lower() for k in item["keywords"]]
                seen: set[str] = set()
                scored = []
                for img in parser.imgs:
                    url = urllib.parse.urljoin(page, img["src"])
                    if url in seen:
                        continue
                    seen.add(url)
                    score = sum(1 for k in keywords if k in f"{img['src']} {img['alt']}".lower())
                    scored.append((score, url))
                scored.sort(key=lambda x: x[0], reverse=True)
                candidates = [u for _, u in scored]
            except Exception as exc:
                print(f"  [erro] falha ao abrir pagina: {exc}")

        saved = False
        for img_url in candidates:
            try:
                raw = fetch_url(img_url)
                info = detect_image_info(raw)
                if not info or len(info[3]) < 10_000:
                    continue
                ext, w, h, data = info
                if w < 300 or h == 0:
                    continue
                ratio = w / h
                if not item.get("direct_url") and not (r_min <= ratio <= r_max):
                    continue
                out_path = OUT_DIR / f"{slug}.{ext}"
                out_path.write_bytes(data)
                manifest.append(
                    {
                        "slug": slug,
                        "file": out_path.name,
                        "source_page": page,
                        "image_url": img_url,
                        "width": w,
                        "height": h,
                        "bytes": len(data),
                        "sha256": hashlib.sha256(data).hexdigest(),
                    }
                )
                print(f"  [ok] {out_path.name} ({w}x{h}, ratio={ratio:.2f})")
                saved = True
                break
            except Exception:
                continue

        if not saved:
            print(f"  [aviso] falha ao baixar/converter {slug}")

    (OUT_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"[done] manifesto gravado em {OUT_DIR / 'manifest.json'}")


if __name__ == "__main__":
    main()
