#!/usr/bin/env python3
"""Baixa e valida os quadros de graduacao de referencia em references/charts/."""

from __future__ import annotations

import hashlib
import json
import struct
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
    },
    {
        "slug": "chart_02_the_front",
        "page": "https://www.climbing.com/culture-climbing/when-did-climbing-gyms-get-too-scared-to-grade-their-own-boulders/",
        "keywords": ["dot", "grade", "front", "boulder", "rating"],
    },
    {
        "slug": "chart_03_aliior_jp",
        "page": "https://blog.tokyoroomfinder.com/living-in-japan/bouldering-in-japan-guide/",
        "keywords": ["grade", "boulder", "aliior", "kyu", "chart"],
    },
    {
        "slug": "chart_04_sportrock",
        "page": "https://www.climbingcrux.com/climbing-grades",
        "keywords": ["sportrock", "v-scale", "grade", "chart"],
    },
    {
        "slug": "chart_05_rockfish",
        "page": "https://rockfishclimbing.com/getting-started/",
        "keywords": ["grade", "difficulty", "rockfish", "scale"],
    },
    {
        "slug": "chart_06_j2_bouldering",
        "page": "https://www.j2bouldering.com/boulder-circuits",
        "keywords": ["tag", "grade", "circuit", "boulder"],
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
        src = d.get("data-src") or d.get("src") or ""
        if src:
            self.imgs.append({"src": src, "alt": d.get("alt", "")})


def detect_image_info(data: bytes) -> tuple[str, int, int] | None:
    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
        w, h = struct.unpack(">II", data[16:24])
        return "png", w, h
    if data.startswith(b"\xff\xd8\xff"):
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                break
            marker = data[i + 1]
            if marker in (0xC0, 0xC1, 0xC2):
                h, w = struct.unpack(">HH", data[i + 5 : i + 9])
                return "jpg", w, h
            if marker in (0xD8, 0xD9) or (0xD0 <= marker <= 0xD7):
                i += 2
                continue
            seg_len = struct.unpack(">H", data[i + 2 : i + 4])[0]
            i += 2 + seg_len
        return "jpg", 0, 0
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
        keywords = [k.lower() for k in item["keywords"]]
        print(f"[fetch] {slug} <- {page}")
        try:
            html = fetch_url(page).decode("utf-8", errors="ignore")
        except Exception as exc:
            print(f"  [erro] falha ao abrir pagina: {exc}")
            continue

        parser = ImgParser()
        parser.feed(html)
        scored = []
        for img in parser.imgs:
            hay = f"{img['src']} {img['alt']}".lower()
            score = sum(1 for k in keywords if k in hay)
            if score > 0 and not img["src"].startswith("data:"):
                scored.append((score, urllib.parse.urljoin(page, img["src"])))
        scored.sort(key=lambda x: x[0], reverse=True)

        saved = False
        for _, img_url in scored:
            try:
                data = fetch_url(img_url)
                info = detect_image_info(data)
                if not info or len(data) < 10_000:
                    continue
                ext, w, h = info
                if w and w < 350:
                    continue
                out_path = OUT_DIR / f"{slug}.{ext}"
                out_path.write_bytes(data)
                sha = hashlib.sha256(data).hexdigest()
                manifest.append(
                    {
                        "slug": slug,
                        "file": out_path.name,
                        "source_page": page,
                        "image_url": img_url,
                        "width": w,
                        "height": h,
                        "bytes": len(data),
                        "sha256": sha,
                    }
                )
                print(f"  [ok] {out_path.name} ({w}x{h}, {len(data)} bytes)")
                saved = True
                break
            except Exception:
                continue

        if not saved:
            print(f"  [aviso] nenhuma imagem valida encontrada automaticamente para {slug}")

    (OUT_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"[done] manifesto gravado em {OUT_DIR / 'manifest.json'}")


if __name__ == "__main__":
    main()
