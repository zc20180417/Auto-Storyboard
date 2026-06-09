{
  "pass": true,
  "summary": "seg01保留顾北辰顶层潜入、秦越诱捕、红外陷阱和沈曼接通声纹的关键因果，格式与视频执行规则通过。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组"],
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "许知夏耳机声约38个有效字安排在6秒内，约6.3字/秒，顾北辰“收到”单独2秒承载，未超过6.5字/秒硬上限。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "evidence": "许知夏台词写为耳机声音，顾北辰嘴唇闭合；秦越“晚了”写明对顾北辰现场说道，口型来源清楚。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "evidence": "楼下会客室与顶层保险室门口的切换明确写为蒙太奇转场，未伪装成同一物理空间连续移动。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "evidence": "折叠反光镜从工具车底层抽屉取出，袖口信号发射器在按下按钮后亮起，道具状态有可见过渡。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留许知夏关于暗格、声纹备份、B3和顶层的完整信息，以及顾北辰低声回应“收到”。",
      "fix_instruction": "若不通过，应补回许知夏耳机声中的两个信息和顾北辰回应。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "撬开门禁、取出干扰器、夹线、警报预响分成连续四段，每段一个主动作。",
      "fix_instruction": "若不通过，应拆开门禁操作和秦越逼近声源。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "秦越和顾北辰的现场对白均写明对对方说道，没有假对象或对象缺失。",
      "fix_instruction": "若不通过，应为每句现场对白补充真实对话对象。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "迈步、门开、红外线亮起、耳机警告和秦越后退被分成4段，总时长12秒，没有把陷阱触发和反应压进同一镜。",
      "fix_instruction": "若不通过，应拆出保险室开门和红外线亮起。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "组首继承第4组门开、红外线封住空房、秦越手持录音笔的状态；组尾交代反光镜和袖口信号发射器已启动。",
      "fix_instruction": "若不通过，应补充红外线、录音笔和工具车状态。"
    },
    {
      "group": "第6组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定沈曼、墙后暗格、秦越录音笔和顾北辰红外线位置，共4条且不与剧情矛盾。",
      "fix_instruction": "若不通过，应删除泛泛禁止项并改成本组人物和道具风险。"
    },
    {
      "group": "第6组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有Seedance说明词、模板编号、参考图占位符或内部审核标记。",
      "fix_instruction": "若不通过，应删除模型说明词和工程占位。"
    }
  ],
  "issues": [],
  "warnings": []
}
