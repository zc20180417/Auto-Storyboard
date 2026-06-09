{
  "pass": true,
  "summary": "第7组审核通过：周美娟索要证据场景，台词忠实、节奏合理、冲突升级清楚。",
  "checked_groups": ["第7组"],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "space_locking": "checked",
    "format": "checked",
    "character_availability": "checked",
    "handoff_continuity": "checked",
    "filmability": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "evidence": "第7组46字有效台词/14秒=3.29字/秒。6-10秒段17字/4秒=4.25字/秒，10-14秒段20字/4秒=5字/秒，均在6.5字/秒硬上限内。"
    },
    {
      "group": "第7组",
      "type": "script_fidelity",
      "evidence": "第7组保留原剧本全部台词：周建国怒吼'你再说一句盗窃试试'、沈清'不是盗窃是什么'、周美娟挑衅'你有证据吗'、沈清'你确定要证据'均完整。原剧本'刘美娟'为笔误，统一为周美娟。"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "evidence": "第6组组尾周建国手掌按桌面、沈清直视周建国；第7组组首周建国手掌按桌面、沈清直视周建国方向，状态完全连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "第7组全部为画面内真人开口对白，每句均写明'A对B说道'，无心声/画外音混用。",
      "fix_instruction": "无需修改，口型和声音承载正确。"
    },
    {
      "group": "第7组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第7组强节拍：周建国怒吼、沈清反击、周美娟挑衅转变、沈清反问+周美娟挑衅。4个节拍分布在14秒内，冲突升级清楚，每个时间段一个主动作。",
      "fix_instruction": "无需修改，强节拍分布合理。"
    },
    {
      "group": "第7组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "本集对话组为主，未要求视频禁止项。第7组为纯对话对质，无复杂动作/保护站位/关键道具操作，省略视频禁止项合理。",
      "fix_instruction": "无需修改，视频禁止项省略合理。"
    }
  ],
  "issues": [],
  "warnings": []
}
