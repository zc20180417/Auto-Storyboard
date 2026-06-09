{
  "pass": true,
  "summary": "ep22分镜保留许知夏在启元大厅策反沈曼、以弟弟转院申请换取声纹与保险室权限、沈曼拨通内线带人上楼的完整剧情，格式和审核门槛通过。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组"],
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
      "evidence": "许知夏关于肿瘤科和弟弟的台词约35字安排在5-10.5秒，约6.4字/秒，低于6.5硬上限；前后沈曼短句各有2.5秒。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "evidence": "转院申请单由许知夏从文件包取出，停在两人之间，组尾仍在许知夏手中；第7组再明确收回文件包，申请单没有跳变。"
    },
    {
      "group": "第8组",
      "type": "script_fidelity",
      "evidence": "沈曼托许知夏转告顾北辰三年前档案室销毁记录由她经手，以及“赎罪的机会”台词完整保留，许知夏回应“那就用行动还”。"
    },
    {
      "group": "第9组",
      "type": "action_atomicity",
      "evidence": "许知夏与林元朝电梯走、沈曼深呼吸、拿起内线电话、向秦越报告分为四个时间段，未把转身、按键和通话压在同一镜。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "许知夏、林元、沈曼都在组首空间锁定中给出位置和朝向；沈曼在前台旁可执行迎接和开口动作。",
      "fix_instruction": "若不通过，应在组首补齐人物位置、朝向和工牌状态。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载医院线索揭示、沈曼反应和拉到角落的单一动作转移，15秒内强节拍清楚，没有额外插入交易条件。",
      "fix_instruction": "若不通过，应把医院线索和转移角落拆成两组或压缩非关键反应。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈曼对许知夏的追问、许知夏对沈曼说明查秦越并追问U盘和冷库，均明确现场对白对象。",
      "fix_instruction": "若不通过，应补足每句对白对象，不能写成无对象独白。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "沈曼“他答应过我……”约29字用6秒，许知夏提周振邦约21字用3.5秒，均未超过6.5字/秒。",
      "fix_instruction": "若不通过，应延长对应台词时间段或拆为相邻时间段。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "转院申请单从许知夏文件包取出，红章可见，但没有塞进沈曼手里，组尾仍在许知夏手中，符合第7组收回动作。",
      "fix_instruction": "若不通过，应明确申请单的取出、停留和收回路径。"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第6组申请单在两人之间，第7组组首承接为许知夏手中持有申请单，并在6-10秒收回文件包，状态连续。",
      "fix_instruction": "若不通过，应在第6组组尾或第7组组首补充申请单归属。"
    },
    {
      "group": "第9组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第9组涉及内线电话和人物去向，视频禁止项锚定沈曼、许知夏、林元、秦越、转院申请单，没有使用泛泛占位词。",
      "fix_instruction": "若不通过，应替换为本组具体道具和人物错误风险。"
    },
    {
      "group": "第4组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有出现参考模板、模型说明、自动分镜、@图片或广告化话术，情绪压力通过工牌、眼眶和侧光转译成可见动作。",
      "fix_instruction": "若不通过，应删除工程词和模板污染，改为可视动作与声音来源。"
    }
  ],
  "issues": [],
  "warnings": []
}
