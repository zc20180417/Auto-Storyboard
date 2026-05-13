{
  "pass": true,
  "summary": "seg01 两组保留宋子昂车内密谋和张局长电话承诺，电话音与现场口型区分清楚。",
  "checked_groups": ["第1组", "第2组"],
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "evidence": "张局长台词写为手机听筒电话音，宋子昂嘴唇闭合不做口型，未把电话音写成现场开口。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "宋子昂“老张，不管你用什么借口，卡死黑风山文件！”约20字用4秒，约5字/秒，情绪对白可承载。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "evidence": "第1组结尾宋子昂握手机听电话，第2组组首继续贴近耳侧通话，手机归属和车厢位置连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留扯松领带、保镖递手机、宋子昂要求卡死文件、张局长保证打回文件等原剧本信息。",
      "fix_instruction": "若不通过，应补回遗漏台词或关键动作。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "手机从宋子昂手中通话到结束后被扔在真皮座椅上，道具转移有可见动作。",
      "fix_instruction": "若不通过，应补充手机递接或放置过程。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、参考模板、字幕、首尾帧或工程占位符。",
      "fix_instruction": "若不通过，应删除污染词并改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
