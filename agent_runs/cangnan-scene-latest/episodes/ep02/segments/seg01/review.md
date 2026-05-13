{
  "pass": true,
  "summary": "seg01已对照原剧本和竖屏生成规则审核，门口催签、抢账本、陆凡质问与老李心虚均保留，无硬问题。",
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
      "evidence": "原剧本中老李询问身份、陆凡回答、老李催签、陆凡反问均按顺序保留，账本和确认表位置清楚。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组6.5-10秒承载陆凡18字情绪台词，约5.1字/秒；10-13秒承载老李5字结巴台词并包含表演反应，未超过6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "第1组尾部老李手指压住账本，第2组3.5-6.5秒写出老李抢账本、陆凡侧身护到账本，关键道具转移有可见动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定敬老院门口单一物理空间，陆凡和老李的位置、朝向、账本和确认表位置均明确。",
      "fix_instruction": "若不通过，应补全人物画面位置、身体朝向和关键道具位置。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组只有慌乱解释、抢账本、陆凡质问、老李心虚四个清晰节拍，13秒内可表演。",
      "fix_instruction": "若不通过，应拆出抢账本动作或缩短非关键反应。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "所有现场对白均写为老李对陆凡或陆凡对老李，没有假对象和旁白混用。",
      "fix_instruction": "若不通过，应逐句补足真实对话对象。"
    }
  ],
  "issues": [],
  "warnings": []
}
