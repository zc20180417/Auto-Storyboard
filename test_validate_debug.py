from pathlib import Path
import re
from storyboard_agent_workspace import (
    CLEAN_GROUP_RE, CLEAN_SHOT_TIME_RANGE_LINE_RE, CLEAN_LEGACY_SHOT_RE,
    _extract_time_range_durations, _extract_legacy_shot_durations,
    validate_clean_storyboard_format,
)

text = Path('agent_runs/zhangben-zhangba/episodes/ep04/final.txt').read_text(encoding='utf-8')
groups = list(CLEAN_GROUP_RE.finditer(text))
print(f'Clean groups found: {len(groups)}')

for idx, group_match in enumerate(groups):
    group_number = idx + 1
    block_start = group_match.end()
    block_end = groups[idx + 1].start() if idx + 1 < len(groups) else len(text)
    block = text[block_start:block_end]

    time_matches = list(CLEAN_SHOT_TIME_RANGE_LINE_RE.finditer(block))
    legacy_shot_matches = list(CLEAN_LEGACY_SHOT_RE.finditer(block))

    if time_matches:
        seconds, time_issues = _extract_time_range_durations(time_matches)
        shot_count = len(time_matches)
    else:
        seconds, time_issues = _extract_legacy_shot_durations(block, legacy_shot_matches)
        shot_count = len(legacy_shot_matches)

    if any(value <= 1 for value in seconds):
        print(f'Group {group_number}: SHORT SHOT DETECTED')
        print(f'  seconds={seconds}')
        print(f'  time_matches={len(time_matches)}, legacy={len(legacy_shot_matches)}')
        print(f'  time_issues={time_issues}')
        print(f'  block_preview={repr(block[:200])}')
        break
