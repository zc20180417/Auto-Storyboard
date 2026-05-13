{
  "pass": true,
  "summary": "已对照原剧本、生成规则和当前分镜逐组审核，6组均保留关键台词、动作、空间转换和结尾余韵，未发现阻断交付的 hard issue。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组"
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "证券交易所敲钟、股价涨停、全场欢呼、赵大雷抱起桂姨喊发财均按原剧本顺序保留，没有新增改变剧情的动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "evidence": "赵朵朵看屏幕后说“这只是一个新起点”，随后转向助理下达捐建项目指令；助理对赵朵朵问第一站，赵朵朵回答老家北沟村，对话对象明确。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "组首明确水泥大桥、赵朵朵、赵大雷、村长、村民和果筐位置；本组始终在村口水泥大桥旁，没有跨主要物理空间。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "大嫂13字/3秒、桂姨12字/3秒、赵大雷10字/2.5秒、赵朵朵13字/3秒，均低于6.5字/秒硬上限，并有端菜、夹肉、举杯、碰杯动作承载。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "evidence": "第6组为6秒片尾意象短组，只承载咬红烧肉和抬头看繁星；若并入第5组会把团圆对白、碰杯和星空收束压进15秒，属于不同情绪目标硬合并。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "timing_math",
      "result": "pass",
      "evidence": "第1组时间段为0-2、2-5、5-8、8-12秒，连续且相加为标题12秒，镜头数4个与时间段一致。",
      "fix_instruction": "若不通过，应调整时间段连续性、标题总时长或镜头数，使最后一段结束于标题总时长。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "“这只是一个新起点”“助理，启动希望小学捐建项目”“第一站定在哪里”“我的老家，远县北沟村”四句台词完整保留，顺序和对象未错置。",
      "fix_instruction": "若不通过，应恢复原剧本台词原意、顺序和说话对象，不得摘要化或改地点。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "村长、村民、赵大雷、赵朵朵四处对白分别落在2.5秒、2.5秒、3秒和2.5秒段内，最长约15字/3秒，均未超过6.5字/秒。",
      "fix_instruction": "若不通过，应拆开感谢对白或延长承载时间段，避免台词超过6.5字/秒。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾部赵大雷看向桥外大路，第4组首即为赵朵朵和赵大雷站在村口水泥路边看重卡驶过，人物位置和视线方向自然衔接。",
      "fix_instruction": "若不通过，应在第3组尾或第4组首补充转向大路、走到路边等可见状态。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首明确夜晚四合院葡萄架下餐桌、赵朵朵、赵大雷、桂姨、大嫂和杯盘位置；本组所有动作都发生在同一张餐桌旁。",
      "fix_instruction": "若不通过，应补齐本组第一帧人物站坐位置、餐桌道具归属和夜晚院落光源。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第6组6秒只处理赵朵朵咬红烧肉后的情绪落点和抬头望繁星片尾意象，属于不可自然合并的结尾短节拍。",
      "fix_instruction": "若不通过，应拆出或保留独立片尾意象组，不要把余韵硬塞进家庭碰杯组。"
    },
    {
      "group": "第1组-第6组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、模板编号、官方占位符、参考图、视频延长、一镜到底或模板化批量描述。",
      "fix_instruction": "若不通过，应删除工程说明和模板语气，改为具体人物、动作、空间、道具和声音描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
