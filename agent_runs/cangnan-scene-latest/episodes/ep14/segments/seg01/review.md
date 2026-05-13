{
  "pass": true,
  "summary": "seg01 两组保留车队被拦、江若晴提醒、陆凡下车对峙和陆凡反问刀疤的原剧情，无硬问题。",
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
      "type": "script_fidelity",
      "evidence": "保留十辆挖掘机驶向入口、刀疤用喇叭威胁、司机刹车、江若晴提醒警察半小时、陆凡下车的完整顺序。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "刀疤台词约14字用3秒，江若晴台词约14字用3秒，均低于6.5字/秒硬上限。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "组首明确陆凡在画面左侧道路中央、刀疤在画面右侧路障前、混混在刀疤身后，人物可用性清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "刀疤对挖掘机车队喊话，江若晴对陆凡说道，陆凡对江若晴说道，现场对白对象明确。",
      "fix_instruction": "若不通过，应补齐每句台词的真实说话对象。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "刀疤挑衅和陆凡提到宋子昂安家费的原台词均保留，未改变说话对象或因果。",
      "fix_instruction": "若不通过，应恢复原剧本台词和对峙顺序。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部陆凡走向阵前，第2组组首陆凡已在路障前与刀疤对峙，位置承接自然。",
      "fix_instruction": "若不通过，应在第1组尾部或第2组组首补足陆凡移动后的明确位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
