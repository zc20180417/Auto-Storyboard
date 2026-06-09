{
  "pass": true,
  "summary": "已对照第14集原剧本、竖屏生成规则和当前分镜逐组审核，公开证据策略、秦越亮录音笔、停车场威胁、安全屋推理和冷库备份线索均完整保留，无阻断交付硬问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组", "第10组", "第11组"],
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
      "evidence": "许知夏公开证据策略长句约42字安排在2-9秒的7秒内，字秒比约6.0，运动中断续但清晰，未超过6.5硬上限。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "秦越在车旁持小型录音笔，第4组特写X·Z·N刻字，第5组继续由秦越把玩并收起录音笔，归属连续。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "evidence": "法务声音来自许知夏手机免提，分镜明确许知夏听电话时嘴唇闭合，随后她才对免提回应。"
    },
    {
      "group": "第10组",
      "type": "script_fidelity",
      "evidence": "许知夏提到父亲、地下档案室、秦越没提编号，顾北辰解释项目备份柜和地下冷库，均按原剧本信息顺序保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "顾北辰OS被写成嘴唇闭合的内心声，许知夏现场开口对耳机说策略，声音来源区分明确。",
      "fix_instruction": "若后续调整，应继续把顾北辰OS写成内心声，不要让他现场开口说出。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组组尾两人接近安全通道出口，第3组组首锁定出口门内侧，顾北辰再推门，动作衔接清楚。",
      "fix_instruction": "若合并或拆分通道段，应保留出口门状态和两人相对站位。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载秦越把玩录音笔、顾北辰护人发问、秦越开车门威胁三个强节拍，15秒内没有再加入车辆离开，且威胁台词给到4.5秒承载，密度可执行。",
      "fix_instruction": "若加入秦越上车离开，应保持第6组单独承载，不要塞入第5组。"
    },
    {
      "group": "第6组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "秦越上车、汽车驶离、许知夏判断、顾北辰判断和抢回决定按时间段顺序推进，车辆动作和对白没有压在同一瞬间。",
      "fix_instruction": "若缩短本组，应保留车窗升起和车辆驶离两个可见阶段。"
    },
    {
      "group": "第8组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定安全屋内顾北辰在监控屏前、许知夏在桌边，许知夏走到他身侧的移动发生在后续时间段。",
      "fix_instruction": "若修改组首，应避免写许知夏正在走到顾北辰身边这类过程动作。"
    },
    {
      "group": "第10组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定ST-CLD-A17编号、许知夏手机、顾北辰、盛远协议和地下冷库信息，数量4条且未使用模板占位。",
      "fix_instruction": "若改视频禁止项，应继续使用本组关键编号、人物和道具作为锚点。"
    },
    {
      "group": "第11组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终正文无模型说明词、参考图、模板编号、工程占位符或非分镜 JSON 内容。",
      "fix_instruction": "若追加结尾，不要加入说明性工作流文字或模型提示词来源。"
    }
  ],
  "issues": [],
  "warnings": []
}

