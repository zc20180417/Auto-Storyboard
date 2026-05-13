{
  "pass": true,
  "summary": "seg03 四组已检查小龙入壶、卧室安置、壶壁作画和龙舟轮廓揭示，剧情与横屏空间连续性可交付。",
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
      "type": "prop_continuity",
      "evidence": "小龙从裂缝右下方爬进画面中央水壶，天天随后拧紧盖子并抱走水壶，水壶归属从裂缝边转移到天天胸前。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "evidence": "天天贴近水壶，对水壶里的小龙小声说“别怕，我带你回家了，这里没有黑水。”，后续自责台词也明确对小龙说。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "壶壁船头高昂、船尾下沉的轮廓被保留，天天先问“这是一个……龙舟？”，再问“你到底想要干什么？你想去找一条船？”。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "承接上一段小龙扒住壶口，本组让小龙完整进入壶底，再由天天抱着水壶离开河床，动作闭环明确。",
      "fix_instruction": "若不通过，应补充小龙进入壶口和天天拧盖之间的可见动作。"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "小龙自责感知被转译为睁眼、抬头和用受伤尾巴划开壶壁水雾，属于可见动作，不依赖抽象说明。",
      "fix_instruction": "若不通过，应把不可视心理改为具体眼神、尾巴动作或壶壁痕迹。"
    },
    {
      "group": "第4组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "龙舟轮廓居中，天天在画面左侧，小龙在画面右下壶底，三者关系横向分布清楚，疑问视线落到船形痕迹。",
      "fix_instruction": "若不通过，应补明天天、小龙和龙舟轮廓在画面中的左右位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
