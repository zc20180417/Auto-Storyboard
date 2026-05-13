{
  "pass": true,
  "summary": "工地板房讨薪段已对照原剧本完成审核，台词、动作因果、横屏站位和道具连续性可交付。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组"
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
      "type": "horizontal_composition",
      "evidence": "爸爸从画面左侧门口冲入，包工头固定在画面右侧桌后，现金和安全帽位于桌面中央，左右对峙和道具位置清楚。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "爸爸台词“我干了三个月，你扣什么钱！”安排在0-3秒，约12字/3秒；包工头台词“你干什么！打人要坐牢的！”安排在6.5-9.5秒，均低于6.5字/秒硬上限。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "保留爸爸松手、抓起桌上几百块零钱、转身冲出，以及台词“这点算路费。剩下的回头算。”，未新增改变剧情的动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "爸爸始终由画面左侧向右侧包工头施压，包工头守在右侧桌后，组内视线方向稳定。",
      "fix_instruction": "若不通过，应在组首或镜头描述补充爸爸从左到右逼近、包工头在右侧后退的轴线。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "安全帽从第1组桌面偏左延续到第2组桌面震动，零钱仍在桌面右侧，为第3组抓钱做铺垫。",
      "fix_instruction": "若不通过，应补充安全帽和零钱在桌面上的固定位置，以及爸爸抓钱前的视线落点。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "10秒内只承载松手、抓零钱、回头放话、冲出门四个连续动作，均来自原剧本，表演链条清楚。",
      "fix_instruction": "若不通过，应删去无关停顿或拆分抓钱与冲出门动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
