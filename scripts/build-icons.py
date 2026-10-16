#!/usr/bin/env python3
"""SVGを原本に、ImageMagickで不透明なホーム画面用PNGを生成する。"""
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[1]
for filename, size in (("apple-touch-icon.png", 180), ("favicon.png", 48),
                       ("icon-192.png", 192), ("icon-512.png", 512)):
    subprocess.run([
        "magick", "-density", "288", str(root / "icon.svg"),
        "-resize", f"{size}x{size}", "-background", "#2563eb",
        "-alpha", "remove", "-alpha", "off", "-strip",
        "PNG24:" + str(root / filename),
    ], check=True)
