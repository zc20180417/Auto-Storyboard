{
  "pass": true,
  "summary": "seg01三组保留原剧本逼问、威胁、龙鳞现身的顺序，横屏站位和道具归属清楚，无硬性问题。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "type": "horizontal_composition",
      "evidence": "爸爸和天天固定在画面左侧，胡永贵在画面右侧泉眼边握毒液瓶，泉眼位于中后景中央，左右阵营和关键道具位置明确。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "爸爸台词分配在2-5秒，约18字/3秒，胡永贵台词分配在5-8秒，约21字/3秒，情绪对峙节奏偏紧但可由喊话和反打承载。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "保留胡永贵掏出残缺青色龙鳞以及台词“我有这块伴生鳞片，我就能永远控制它！”，未新增改变剧情的动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "爸爸、胡永贵、天天的台词均写明对胡永贵或爸爸喊话，画面内对象可见。",
      "fix_instruction": "如不通过，应补充说话对象或给出反应镜头。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "毒液瓶从第1组胡永贵右手延续到第2组右侧手中，没有跳到地面或他人手里。",
      "fix_instruction": "如不通过，应补充毒液瓶交接或滑落动作。"
    },
    {
      "group": "第3组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "胡永贵始终在右侧，爸爸和天天始终在左侧，龙鳞从胡永贵怀里取出后仍属于右侧阵营，轴线连续。",
      "fix_instruction": "如不通过，应用中性全景或可见走位解释换边。"
    }
  ],
  "issues": [],
  "warnings": []
}
