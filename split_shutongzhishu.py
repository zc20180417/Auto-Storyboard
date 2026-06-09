#!/usr/bin/env python3
"""Split 《撕通知书后我卖凉皮暴富》 script into per-episode files."""

import re
import sys
import shutil
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Split shutongzhishu script")
    parser.add_argument("--source", default=r"inputs\《撕通知书后我卖凉皮暴富》卡6付7.txt")
    parser.add_argument("--out-dir", default=r"split_scripts\shutongzhishu")
    args = parser.parse_args()

    source = Path(args.source)
    out_dir = Path(args.out_dir)

    text = source.read_text(encoding="utf-8")

    # Find episode boundaries
    episode_pattern = re.compile(r'^(第(\d+)集\s+.+)$', re.MULTILINE)
    matches = list(episode_pattern.finditer(text))

    print(f"Found {len(matches)} episodes")

    # Extract preamble (character settings, etc.)
    preamble_end = matches[0].start() if matches else len(text)
    preamble = text[:preamble_end].strip()

    # Split preamble into sections
    setting_match = re.search(r'(一、年代设定.+?)(?=二、主要人物小传)', preamble, re.DOTALL)
    character_match = re.search(r'(二、主要人物小传.+)', preamble, re.DOTALL)

    setting_text = setting_match.group(1).strip() if setting_match else ""
    character_text = character_match.group(1).strip() if character_match else ""

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    for i, match in enumerate(matches):
        ep_num = int(match.group(2))
        start = match.start()

        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            end = len(text)

        ep_content = text[start:end].strip()

        # Build full episode script with preamble
        parts = []
        if setting_text:
            parts.append(setting_text)
        if character_text:
            parts.append(character_text)
        parts.append(ep_content)

        full_content = "\n\n".join(parts)

        # Write as flat file in the directory (not in subdirectory)
        script_file = out_dir / f"撕通知书后我卖凉皮暴富第{ep_num:02d}集.txt"
        script_file.write_text(full_content, encoding="utf-8")

        print(f"  ep{ep_num:02d}: {len(ep_content)} chars, {ep_content.count(chr(10))} lines")

    print(f"\nDone. {len(matches)} episodes split to {out_dir}")


if __name__ == "__main__":
    main()
