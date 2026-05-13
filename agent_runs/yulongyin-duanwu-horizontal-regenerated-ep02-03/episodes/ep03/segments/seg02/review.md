{
  "pass": true,
  "summary": "seg02逐组对照剧本、横屏规则和分镜完成审核：门外声音、爷爷闯入、护壶质问、清水脏水禁忌与端午警告均完整，门和水壶物理连续性已处理。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组"
  ],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "format": "checked",
    "character_availability": "checked",
    "handoff_continuity": "checked",
    "filmability": "checked",
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "camera_motion": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "narrative_progression": "checked",
    "asset_scope": "checked",
    "special_effects": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "physical_continuity",
      "evidence": "第1组没有让反锁门无过渡消失，而是写出老木门门闩被拐杖震松、门向内弹出宽缝后爷爷进屋，门状态有可见过渡。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "evidence": "第2组爷爷对画面左侧的天天质问“你手里拿的什么东西”，天天抬头看向右侧爷爷解释“这是喝的水”，对白对象明确。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "第3组保留爷爷不理解释、盯水壶、眼神突然清明、说出“清水养它，脏水害它”，以及天天试探追问。"
    },
    {
      "group": "第4组",
      "type": "special_effects",
      "evidence": "第4组端午黑水警告只由爷爷台词承载，没有把黑水画成夸张毒液或怪物，云宝只藏在清水底部。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组承接seg01结尾的天天水珠和竖立水壶，并建立门内左侧天天、水壶与门外右侧爷爷的空间分割。",
      "fix_instruction": "无需修复；若改写门动作，必须保留门闩松动或其他可见开门过渡。"
    },
    {
      "group": "第2组",
      "type": "physical_continuity",
      "result": "pass",
      "evidence": "第2组天天双手竖抱水壶、掌心压壶盖、壶口朝上，未出现双手抱壶同时开门或水壶平放仍盛水的矛盾。",
      "fix_instruction": "无需修复；继续保持水壶有支撑且壶口朝上。"
    },
    {
      "group": "第3组",
      "type": "special_effects",
      "result": "pass",
      "evidence": "第3组只让云宝以壶中细小影子和水纹存在，符合正式现身后的克制展示，不影响爷爷台词和水壶线索。",
      "fix_instruction": "无需修复；不要让云宝跳出或被爷爷完整看见。"
    },
    {
      "group": "第4组",
      "type": "timing_math",
      "result": "pass",
      "evidence": "第4组3个镜头时长3+5+2=10秒，属于警告短组且在6-15秒范围内，镜头数与标题一致。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
