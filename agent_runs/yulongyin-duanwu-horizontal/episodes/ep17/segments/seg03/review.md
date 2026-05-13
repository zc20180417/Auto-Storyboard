{
  "pass": true,
  "summary": "河床裂缝段保留胡永贵带炸药、说明水眼、投放炸药和点引线前一刻，危险道具归属连续。",
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
      "evidence": "胡永贵满头大汗拎沉重帆布包到裂缝边，台词“李燃，你以为修好一头破鼓就能翻盘？”、炸药雷管露出、台词“这裂缝下面是全村的水眼！”均保留。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "第1组末尾胡永贵扯出长引线，第2组开头炸药包在胡永贵脚边并由他扔入裂缝，最后防风打火机靠近同一长引线，道具路径连续。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "胡永贵“炸平了水眼...”有效约21字安排在6-10秒的4秒镜头内，约5.3字/秒，符合冷酷情绪对白节奏。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "裂缝横贯画面左前景至中央，胡永贵始终位于右侧，帆布包、雷管和引线在中央被展示，左右关系便于生成。",
      "fix_instruction": "若调整镜头，应保持裂缝在左侧/中央、胡永贵在右侧控制炸药的构图。"
    },
    {
      "group": "第2组",
      "type": "blocking_continuity",
      "result": "pass",
      "evidence": "胡永贵从右侧抡起炸药包，炸药包越过中央进入左侧裂缝，引线仍由右侧手部控制，动作路线从投放到点火前一刻清楚。",
      "fix_instruction": "若补充动作，应只补投放或引线被拉紧的可见过渡，不新增爆炸结果。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "原剧本到胡永贵掏出防风打火机凑近引线为止，分镜停在火轮即将被按下，没有提前引燃或新增爆炸。",
      "fix_instruction": "若修改结尾，必须停在打火机靠近引线，不得提前表现爆炸。"
    }
  ],
  "issues": [],
  "warnings": []
}
