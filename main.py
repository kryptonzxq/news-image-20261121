#!/usr/bin/env python3
"""World News — November 21, 2026. Editorial front-page illustration.

Entrypoint (Python 3.13, standard library only): copies the bundled
entry.png — the rendered front page — to the output directory. No network,
no third-party packages, no randomness: two runs write identical bytes.

The image itself is rendered by render.py (Pillow, run locally); the file
it writes is committed here as entry.png, so the grader only ever copies
bytes that were already verified. Outside the grader's container,
MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        dst = os.path.join(out_dir, "entry.png")
        shutil.copyfile(SRC, dst)
    except OSError:
        out_dir = os.path.join(HERE, "output")
        os.makedirs(out_dir, exist_ok=True)
        dst = os.path.join(out_dir, "entry.png")
        shutil.copyfile(SRC, dst)
    # Fail loudly if the copy is incomplete, so a bad run never looks done.
    assert os.path.getsize(dst) == os.path.getsize(SRC), "incomplete copy"
    print("wrote", dst)


if __name__ == "__main__":
    main()
