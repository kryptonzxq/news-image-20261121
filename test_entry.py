#!/usr/bin/env python3
"""Validation for the news-image entry. Run from the repo root.

Checks: main.py exits 0, writes a valid PNG, <=1024x1024, <=1 MiB, and two
consecutive runs produce identical SHA-256 bytes. Standard library only,
so it runs anywhere (no Pillow needed): PNG width/height are read from the
IHDR chunk. The entrypoint itself only copies the bundled entry.png.
"""
import hashlib
import os
import struct
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = "/output/entry.png"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def png_size(path):
    with open(path, "rb") as f:
        head = f.read(33)
    assert head[:8] == b"\x89PNG\r\n\x1a\n", "not a PNG file"
    assert head[12:16] == b"IHDR", "missing IHDR chunk"
    w, h = struct.unpack(">II", head[16:24])
    return w, h


def run():
    r = subprocess.run([sys.executable, os.path.join(HERE, "main.py")],
                       capture_output=True, text=True)
    assert r.returncode == 0, f"main.py failed: {r.stderr}"
    return r.stdout.strip()


def main():
    # Run twice; both must write identical bytes.
    run()
    assert os.path.exists(OUT), f"missing {OUT}"
    h1 = sha256(OUT)
    run()
    h2 = sha256(OUT)
    assert h1 == h2, f"non-deterministic: {h1} != {h2}"

    w, h = png_size(OUT)
    assert w <= 1024 and h <= 1024, f"too large: {(w, h)}"
    size = os.path.getsize(OUT)
    assert size <= 1024 * 1024, f"over 1 MiB: {size} bytes"
    print(f"OK: {OUT} {(w, h)} PNG {size} bytes sha256 {h1}")
    print("OK: deterministic across two runs")


if __name__ == "__main__":
    main()
