#!/usr/bin/env python3
"""Split the Cangnan Fengyun anthology script into per-episode files."""

from __future__ import annotations

import argparse
import re
from collections import OrderedDict
from pathlib import Path


TITLE = "苍南风云"
SCENE_HEADING_RE = re.compile(r"^\s*第(?P<episode>\d+)集\s+(?P=episode)-\d+\s*$")


def normalize_text(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def split_episodes(text: str) -> "OrderedDict[int, list[str]]":
    episodes: "OrderedDict[int, list[str]]" = OrderedDict()
    current_episode: int | None = None

    for raw_line in normalize_text(text).split("\n"):
        line = raw_line.strip()
        match = SCENE_HEADING_RE.match(raw_line)
        if match:
            episode_no = int(match.group("episode"))
            current_episode = episode_no
            episodes.setdefault(episode_no, [])

        if current_episode is None:
            if line:
                raise ValueError(f"Content before first episode heading: {line[:80]}")
            continue

        episodes[current_episode].append(line)

    if not episodes:
        raise ValueError("No episode headings found")

    expected = list(range(1, max(episodes) + 1))
    actual = list(episodes)
    if actual != expected:
        raise ValueError(f"Episode numbers are not contiguous: expected {expected}, got {actual}")

    return episodes


def write_episode(out_dir: Path, episode_no: int, lines: list[str]) -> Path:
    content = "\n".join(lines).strip() + "\n"
    path = out_dir / f"{TITLE}-第{episode_no:02d}集.txt"
    path.write_text(content, encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path("inputs/苍南风云.txt"))
    parser.add_argument("--out-dir", type=Path, default=Path("split_scripts/cangnan-fengyun"))
    args = parser.parse_args()

    source = args.source.resolve()
    out_dir = args.out_dir.resolve()
    if not source.is_file():
        raise FileNotFoundError(source)

    episodes = split_episodes(source.read_text(encoding="utf-8-sig"))
    out_dir.mkdir(parents=True, exist_ok=True)

    written: list[Path] = []
    for episode_no, lines in episodes.items():
        written.append(write_episode(out_dir, episode_no, lines))

    print(f"[done] split {source} -> {len(written)} episodes")
    print(f"[out] {out_dir}")
    for path in written:
        content = path.read_text(encoding="utf-8")
        first = next((line.strip() for line in content.splitlines() if line.strip()), "")
        scene_count = sum(1 for line in content.splitlines() if SCENE_HEADING_RE.match(line))
        print(f"- {path.name}: chars={len(content)} scenes={scene_count} first={first!r}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
