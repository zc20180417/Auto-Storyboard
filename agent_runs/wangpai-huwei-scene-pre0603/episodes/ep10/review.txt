{
  "pass": true,
  "summary": "ep10按电话设陷、安全屋决策、定位针袭扰、视频要挟和共同设局分组，台词节奏、视频声源、硬盘/探针连续性和动作拆分符合规则。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组", "第10组", "第11组", "第12组"],
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
      "type": "audio_mouth_sync",
      "evidence": "秦越明确不在画面内，只以电话里的陌生男声出现，所有VO均写为手机声源，未让画面内周振邦替他说话。"
    },
    {
      "group": "第5组",
      "type": "action_atomicity",
      "evidence": "红点移向肩头、顾北辰扑倒许知夏、玻璃碎裂探针钉墙、许知夏低声发问分为4段，避开同一时间段多主动作过载。"
    },
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "evidence": "周振邦手机视频台词分成5秒和4秒两段承载，关键威胁没有超过6.5字/秒硬上限，并保留旧照片画面。"
    },
    {
      "group": "第9组",
      "type": "script_fidelity",
      "evidence": "完整保留周振邦“明早九点，盛远会议室。你一个人来。带上硬盘”的条件，硬盘仍在桌上形成筹码指向。"
    },
    {
      "group": "第12组",
      "type": "audio_mouth_sync",
      "evidence": "顾北辰OS明确写嘴唇闭合不做口型，许知夏现场对白明确对顾北辰说“这次别一个人。我们设局”。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "旧照片从桌面被周振邦看见并作为顾北辰软肋线索，未被替换成其他照片或道具。",
      "fix_instruction": "若不通过，应恢复顾北辰和搭档合影的旧照片位置和用途。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "许知夏和顾北辰的现场对白均写明互相说话对象，许知夏“不让替我决定”的核心态度保留。",
      "fix_instruction": "若不通过，应补齐每句现场对白的说话对象，并保留原剧本台词顺序。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾探针钉墙、两人倒地；第6组首复述探针在墙面、顾北辰半跪挡在窗前，再完成拔针、收进口袋、拉窗帘。",
      "fix_instruction": "若不通过，应同步第5组尾和第6组首的探针、玻璃碎渣、人物姿态。"
    },
    {
      "group": "第8组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "搭档母亲只存在于手机楼道视频中，顾北辰和许知夏在安全屋观看，未把视频人物误放进安全屋。",
      "fix_instruction": "若不通过，应将搭档母亲限制在手机视频画面，现场只保留顾北辰和许知夏。"
    },
    {
      "group": "第10组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "许知夏分析盛远、顾北辰收硬盘并决定独去、许知夏阻拦、顾北辰内疚分别承载，争执节奏清楚。",
      "fix_instruction": "若不通过，应拆出硬盘收起或争执对白，避免一段内同时完成分析、移动、反驳和情绪转折。"
    },
    {
      "group": "第11组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "硬盘关键组写有锚定硬盘、周振邦、许知夏、手机视频的具体禁止项，没有泛泛模板词或超量。",
      "fix_instruction": "若不通过，应删除泛泛禁止项，改成本组具体剧情错误。"
    },
    {
      "group": "第12组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "final.txt未出现固定画面风格、--neg、模板编号、参考图、首尾帧或模型说明语。",
      "fix_instruction": "若不通过，应删除所有非分镜正文和模型模板术语。"
    }
  ],
  "issues": [],
  "warnings": []
}
