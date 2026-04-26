#!/usr/bin/env python3
"""Split the current Youyuanzhai source txt into the confirmed 15 episodes.

This is intentionally explicit because the source file mixes titled episodes,
untitled scene starts, "本集完", and one final "全剧终" marker.
"""

from __future__ import annotations

import argparse
from pathlib import Path


EPISODE_RANGES = [
    (1, 3, 169),
    (2, 172, 402),
    (3, 405, 663),
    (4, 666, 829),
    (5, 832, 947),
    (6, 950, 1088),
    (7, 1091, 1237),
    (8, 1238, 1325),
    (9, 1326, 1414),
    (10, 1415, 1498),
    (11, 1499, 1578),
    (12, 1579, 1663),
    (13, 1664, 1751),
    (14, 1752, 1837),
    (15, 1838, 1910),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Split 有缘斋剧本.txt into 15 confirmed episode files.")
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    out_dir = args.out_dir.resolve()
    text = source.read_text(encoding="utf-8-sig", errors="replace")
    lines = text.splitlines()
    if len(lines) < EPISODE_RANGES[-1][2]:
        raise SystemExit(f"source has only {len(lines)} lines; expected at least {EPISODE_RANGES[-1][2]}")

    out_dir.mkdir(parents=True, exist_ok=True)
    for episode_number, start_line, end_line in EPISODE_RANGES:
        chunk_lines = lines[start_line - 1 : end_line]
        chunk = "\n".join(line.rstrip() for line in chunk_lines).strip() + "\n"
        output_path = out_dir / f"有缘斋第{episode_number:02d}集.txt"
        output_path.write_text(chunk, encoding="utf-8")
        first = next((line.strip() for line in chunk.splitlines() if line.strip()), "")
        last = next((line.strip() for line in reversed(chunk.splitlines()) if line.strip()), "")
        print(f"[split] ep{episode_number:02d}: lines {start_line}-{end_line}, chars={len(chunk)}, file={output_path}")
        print(f"        first={first[:60]}")
        print(f"        last={last[:80]}")

    print(f"[done] wrote {len(EPISODE_RANGES)} episodes to {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
