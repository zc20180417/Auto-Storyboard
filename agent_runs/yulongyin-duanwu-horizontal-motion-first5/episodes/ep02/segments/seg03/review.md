{
  "pass": true,
  "summary": "seg03按原剧本完成小龙入壶、天天带回卧室、安抚、自责、壶壁划出龙舟和结尾追问，审核未发现硬问题。",
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
    "camera_motion": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "河床到卧室被标为连续动作蒙太奇，水壶从裂缝边到天天胸前再到卧室书桌，跨空间方式明确。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "evidence": "天天对水壶里的小龙说“别怕，我带你回家了，这里没有黑水。”，小龙在壶底右侧可见，对象明确。"
    },
    {
      "group": "第3组",
      "type": "camera_motion",
      "evidence": "固定中近景稳定自责口型，壶内推近承接小龙睁眼，固定特写锁住尾巴划水雾，摇回天天疑问。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "壶壁出现船头高昂、船尾下沉的龙舟轮廓，并保留天天“这是一个……龙舟？”和追问找船的原台词。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "小龙先进入壶底，天天再拧紧壶盖并抱壶回卧室，水壶状态转移完整。",
      "fix_instruction": "若压缩蒙太奇，应保留入壶和拧盖两个关键动作。"
    },
    {
      "group": "第2组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "卧室内天天左侧、水壶中央、小龙壶底右侧的横屏关系稳定，桌面和窗光提供空间锚点。",
      "fix_instruction": "若增加近景，应回到桌面中近景确认水壶位置。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "两句天天台词都由画面左侧的天天现场开口承载，小龙无台词，只用眼神和尾巴动作回应。",
      "fix_instruction": "若加入小龙声音，必须标明声音来源和是否现场开口。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "13秒分为擦雾、显出龙舟、震惊台词和追问四段，信息递进清楚，没有同时挤压多个复杂动作。",
      "fix_instruction": "若缩短结尾，应分开保留“龙舟？”和“想去找一条船？”两句台词。"
    }
  ],
  "issues": [],
  "warnings": []
}
