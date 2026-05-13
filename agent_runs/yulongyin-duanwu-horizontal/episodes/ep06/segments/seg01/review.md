{
  "pass": true,
  "summary": "卧室段保留了云宝中毒、清水无效、爷爷入场判断和祠堂底木方案，横屏站位、道具归属与对白承载均可生产。",
  "checked_groups": [
    "第1组",
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
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本中云宝躺在书桌上、天天痛哭喊“云宝你醒醒！我用清水给你洗！”、清水无法冲掉黑色毒素、爷爷进门并说“毒气攻心，凡水救不了它了”均按顺序保留。"
    },
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "evidence": "书桌和云宝锁在画面左中部，天天在右前方，爷爷从左后方门口进入，形成可见的左后到右前关系和门、桌、床窗锚点。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "天天祈求台词约12字用3秒承载，爷爷“去祠堂，用老龙舟的底木吸毒。”约14字用3秒承载，均低于6.5字/秒硬上限且符合情绪语速。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "清水碗在组首位于天天右手边，5-7.5秒由天天从右侧浇到云宝身上，组尾仍在书桌区域，没有道具跳变。",
      "fix_instruction": "若不通过，应补充清水碗从桌面到手中再回到桌面的可见拿起或放下动作。"
    },
    {
      "group": "第2组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "第1组尾爷爷停在左后门边，第2组首仍站在左后方，天天仍在右前方守着云宝，二人左右轴线连续。",
      "fix_instruction": "若不通过，应在第1组尾或第2组首加入爷爷绕桌或中性重建轴线的过渡。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只包含天天祈求、爷爷判断并转身、给出祠堂底木方案、二人出门四个节拍，10秒内可表演，没有叠加额外剧情动作。",
      "fix_instruction": "若不通过，应拆分祈求和出门，或删除非剧本要求的停顿与动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
