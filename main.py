#!/usr/bin/env python3
"""Copy the bundled entry.png to the output directory.

Deterministic: a pure byte-for-byte copy, no timestamps, no network.
The output directory is MAKEFUN_OUTPUT_DIR when set, otherwise /output.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
