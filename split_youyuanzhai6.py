#!/usr/bin/env python3
"""Split the manually verified Youyuanzhai v6 script into episode files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


EPISODE_RANGES = [
    (1, 1, 173),
    (2, 176, 406),
    (3, 408, 464),
    (4, 465, 546),
    (5, 549, 664),
    (6, 667, 805),
    (7, 808, 954),
    (8, 955, 1131),
    (9, 1132, 1215),
    (10, 1216, 1295),
    (11, 1296, 1380),
    (12, 1381, 1468),
    (13, 1469, 1554),
    (14, 1555, 1627),
]

TITLE = "\u6709\u7f18\u658b"


def normalize_text(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def write_episode(out_dir: Path, episode_no: int, lines: list[str]) -> Path:
    content = "\n".join(lines).strip() + "\n"
    path = out_dir / f"{TITLE}\u7b2c{episode_no:02d}\u96c6.txt"
    path.write_text(content, encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=None)
    parser.add_argument("--out-dir", type=Path, default=Path("split_scripts/youyuanzhai-6"))
    args = parser.parse_args()

    source = args.source.resolve() if args.source else next(Path("inputs").glob("*-6.txt")).resolve()
    out_dir = args.out_dir.resolve()
    if not source.is_file():
        raise FileNotFoundError(source)

    text = normalize_text(source.read_text(encoding="utf-8-sig"))
    lines = text.split("\n")
    out_dir.mkdir(parents=True, exist_ok=True)

    written: list[Path] = []
    for episode_no, start_line, end_line in EPISODE_RANGES:
        episode_lines = lines[start_line - 1 : end_line]
        written.append(write_episode(out_dir, episode_no, episode_lines))

    print(f"[done] split {source} -> {len(written)} episodes")
    print(f"[out] {out_dir}")
    for path in written:
        content = path.read_text(encoding="utf-8")
        first = next((line.strip() for line in content.splitlines() if line.strip()), "")
        last = next((line.strip() for line in reversed(content.splitlines()) if line.strip()), "")
        print(
            f"- {path.name}: chars={len(content)} "
            f"first={first[:40]!r} last={last[:40]!r}"
        )

    end_markers = len(re.findall(r"本集完|全剧终|第[一二三四五六七八九十百0-9]+集\s*完", text))
    print(f"[check] end markers detected: {end_markers}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
