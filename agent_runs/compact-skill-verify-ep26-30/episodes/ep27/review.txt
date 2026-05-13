{
  "pass": true,
  "summary": "5组分镜全部通过审核。时长合规（11/11/14/10/15秒），台词节奏均低于6.5字/秒硬上限，组间空间连续性良好，夜景光源正确，无模板污染。存在2条软性warnings：第3组赵朵朵台词为控制节奏做了轻微压缩，第2组组首未提及李少爷。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组"],
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "4句台词共65字分布在11秒内，最密集时段0-3.5秒为21字/3.5秒=6.0字/秒，低于6.5硬上限。情绪对白（争吵、威胁）语速合理。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "核心台词保留：赵朵朵质问'我妈呢'、顾长海威胁'换上婚纱'、李少轻浮'跟着本少有什么不好'、赵朵朵指控'攀附权贵，绑架勒索'。第3组末尾赵朵朵台词'攀附权贵，绑架勒索'为压缩版，去掉了'顾长海，你为了'和'都干得出来'，核心指控信息保留。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "组首明确写出赵朵朵按住李少爷在茶几上、保镖举枪、顾长海在楼梯方向，位置关系清晰。红蓝爆闪灯从窗外射入的光源变化有交代。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首空间锁定写明顾长海立于窗前背对房间、李少爷坐于沙发上翻转打火机、保镖立于门旁，三人位置和朝向清晰，无动作推进。",
      "fix_instruction": "若不通过，应在组首补写人物具体位置、朝向和关键道具状态，不得写'正在进入''从远处走来'等动作推进。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾顾长海面色阴狠侧头朝门方向；第2组组首顾长海站在窗前面朝门方向，状态连续。保镖位置从门旁到门旁一致。",
      "fix_instruction": "若不通过，应在第2组组首补写顾长海具体位置和姿态，确保与第1组组尾自然衔接。"
    },
    {
      "group": "第5组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "全部5组正文未出现Seedance可、自动分镜、模板编号、参考图、首尾帧参考等模型词或工程词。夜景光源使用台灯暖光、吊灯暖光、窗外夜色、红蓝爆闪灯，无'天光''阳光照入'等昼夜错误。",
      "fix_instruction": "若不通过，应删除正文中的模型说明词、模板编号、参考图/首尾帧等工程词，并将夜景光源替换为月光、星光、路灯、室内暖光等可见光源。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第3组",
      "rule": "script_fidelity",
      "problem": "赵朵朵台词'攀附权贵，绑架勒索'为压缩版，原剧本为'顾长海，你为了攀附权贵，连绑架勒索都干得出来'，去掉了称呼和语气词'连...都干得出来'，力度略有减弱。",
      "evidence": "原剧本21字，分镜压缩为8字。核心指控信息（攀附权贵、绑架勒索）保留，说话对象在上下文中明确。",
      "fix": "如需恢复力度，可扩展为'攀附权贵，绑架勒索你都干得出来'（13字），仍需验证字秒比。"
    },
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "handoff_continuity",
      "problem": "第1组组尾提及'李少爷坐在沙发上'，但第2组组首空间锁定未提及李少爷，直到第3组组首才重新出现。",
      "evidence": "第2组只有顾长海和保镖在场，李少爷虽在同空间但未被写入组首。第3组组首重新出现'李少爷坐于右侧沙发上'。",
      "fix": "可在第2组组首补充'李少爷仍坐于沙发上'以保持连续性。"
    }
  ]
}