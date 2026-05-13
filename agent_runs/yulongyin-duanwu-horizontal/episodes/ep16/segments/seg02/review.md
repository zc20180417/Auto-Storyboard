{
  "pass": true,
  "summary": "第2组准确保留胡永贵用打火机威胁烧牛皮、爸爸怒喝并掷棍击腕的因果，左右轴线和道具位置连续。",
  "checked_groups": [
    "第2组"
  ],
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "不到两分钟后保镖倒地、胡永贵抓起防风打火机、原台词威胁烧牛皮、爸爸原台词怒喝、掷出甩棍击中手腕、打火机掉地均完整保留。"
    },
    {
      "group": "第2组",
      "type": "horizontal_composition",
      "evidence": "爸爸稳定在画面左侧，胡永贵和牛皮标本在画面右侧，甩棍从左向右飞行，横屏宽画幅承担了对峙和道具距离。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "胡永贵台词约17个有效字安排在3秒疯狂喊话中，约5.7字/秒；爸爸“你敢！”是0.5秒短促怒喝，作为爆发式两字制止，不挤压后续掷棍动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "防风打火机从桌面被胡永贵右手拿起，随后靠近牛皮，最后被甩棍击中手腕后掉到地上，关键道具有完整过渡。",
      "fix_instruction": "若不通过，应补充拿起、靠近、掉落或熄灭的可见动作。"
    },
    {
      "group": "第2组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "爸爸左、胡永贵右的对峙轴线从组首到组尾保持稳定，甩棍飞行方向与人物站位一致。",
      "fix_instruction": "若不通过，应固定爸爸和胡永贵左右位置，避免无过渡换边。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "15秒内主要节拍为残局、抓火机、威胁台词、点火靠近、怒喝、掷棍击腕，复杂动作与台词没有挤在同一短镜头内。",
      "fix_instruction": "若不通过，应拆分点火和掷棍动作，或压缩非关键倒地保镖反应。"
    }
  ],
  "issues": [],
  "warnings": []
}
