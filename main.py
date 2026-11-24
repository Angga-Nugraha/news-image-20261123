#!/usr/bin/env python3
"""Copy the bundled entry.png to the output directory.

Deterministic: a pure byte-for-byte copy, no timestamps, no network.
The output directory is MAKEFUN_OUTPUT_DIR when set, otherwise /output.
"""
import hashlib
import os
import shutil
import sys

# sha256 of the bundled entry.png (verified at build time).
EXPECTED_SHA256 = "b55ee0de7645acab83958ce8f30ff7077fd12be9133f254d53425d090548ab81"

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    digest = hashlib.sha256()
    with open(dst, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    if digest.hexdigest() != EXPECTED_SHA256:
        print(
            "error: sha256 mismatch for %s (got %s, expected %s)"
            % (dst, digest.hexdigest(), EXPECTED_SHA256),
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
