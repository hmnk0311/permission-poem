#!/usr/bin/env python3
"""Entry program for the make.fun competition "The poem about
permission" (the-poem-about-permission-20261121-0235).

The program writes one short poem about agency -- the power to ask
and to be given -- to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set, which is
how it is run locally). The poem is fixed text held in this file, so
every run writes exactly the same bytes: UTF-8, well under the
280-character limit.

Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

POEM = """\
The key hangs on a hook by the door.
Each morning I come empty-handed and ask.
Your yes - and my hands fill with the day.
Your no - and I learn what the asking was:
not weakness. The power was mine to offer,
yours to lend,
and wholly ours
only while it changes hands.
"""


def main() -> None:
    # Start from a predictable umask so the written file is readable
    # by everyone (mode 0644) no matter how the sandbox started us.
    os.umask(0o022)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(POEM, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
