"""make.fun bounty news-image-20261120 entry.

Writes the bundled image of Friday 20 November 2026's world news to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output). Standard library only:
no network, no randomness, no timestamps -- every run writes identical
bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
# The image bundled beside this program; copied byte for byte, so the
# output is identical on every run.
BUNDLED = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(BUNDLED, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
