{
  "pass": true,
  "summary": "ep21分镜保留会议室逼供、周振邦供出保险室与沈曼、走廊并肩行动及秦越电梯内心声，格式和视频执行稳定性通过。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组"],
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
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "顾北辰说明流水的关键台词约31字安排在2-7.5秒，约5.6字/秒；周振邦追问和顾北辰反击分别有2秒、2.5秒，均未超过6.5字/秒。"
    },
    {
      "group": "第3组",
      "type": "action_atomicity",
      "evidence": "周振邦起身冲向赵明海、保安横到两人之间、赵明海崩溃喊出录音笔信息分在三个连续时间段，未把冲撞、阻拦、喊话压入同一镜。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "evidence": "周振邦OS写为嘴唇没有开合、内心独白响起，和前面顾北辰现场压低声音的对白承载明确区分。"
    },
    {
      "group": "第7组",
      "type": "script_fidelity",
      "evidence": "许知夏负责见沈曼、顾北辰负责拿录音笔、顾北辰回应“好，并肩”、秦越OS“想拿录音笔，就先把命押上”均按原剧本顺序保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "董事甲对周振邦、周振邦对董事甲和许知夏、许知夏对周振邦的现场对白均写明对象。",
      "fix_instruction": "若不通过，应为每句现场对白补足真实说话对象。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载一个冲向赵明海的动作链、一个保安阻拦动作和赵明海一段崩溃揭露，13秒内强节拍清楚且动作分段。",
      "fix_instruction": "若不通过，应拆出阻拦或赵明海揭露为独立组。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "顾北辰的威胁是现场低声对白，周振邦关于秦越能灭口的内容是闭口内心独白，声音来源和口型不混。",
      "fix_instruction": "若不通过，应把OS改为闭口内心声或改成现场开口台词并调整原剧本忠实度。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保险室、录音笔明晚九点转入秦越私人柜、声纹、沈曼可进入等关键事实完整保留，没有新增密码或实物录音笔。",
      "fix_instruction": "若不通过，应恢复原剧本中的保险室、声纹和沈曼线索。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组会议室信息结束后，第6组明确切到会议结束后的许氏集团走廊；新物理空间另起组，手机通话和顾北辰走到身侧均有可见起点。",
      "fix_instruction": "若不通过，应拆分会议室和走廊空间，或补充会议结束后的过渡状态。"
    },
    {
      "group": "第7组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第7组涉及秦越闭口OS和远处电梯状态，视频禁止项锚定秦越、许知夏、录音笔、顾北辰，且没有泛泛占位词。",
      "fix_instruction": "若不通过，应替换无锚点禁止项，并保留秦越闭口内心声约束。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、参考图、模型说明词、自动正反打或非分镜正文。",
      "fix_instruction": "若不通过，应删除工程词和模板化表达，只保留自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
