{
  "pass": true,
  "summary": "seg01分镜保留第28集三处转场的关键台词、认定结果、追责认罪和果园重种收束，格式、时长、空间锁定与声口承载均可交付。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组", "第10组", "第11组", "第12组", "第13组"],
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
      "evidence": "原剧本中勘验员、巡查队长、林知夏、周大柱和村民甲乙围绕旧洞、料场和沈砚川救人作证的台词均保留，且按原顺序由石桌证据推进到村民作证。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "施工方代表、沈砚川和巡查队长台词合计约45字，分配在14秒内并拆为4个时间段，最高台词密度约4.3字/秒，未超过6.5字/秒硬上限。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "晒场边组首列明沈母、沈小禾、沈砚川、林知夏、周大柱、赵有福、赵成武及被押离的施工方人员位置和朝向，赵有福跪地动作发生在0-3秒后才对白。"
    },
    {
      "group": "第12组",
      "type": "filmability",
      "evidence": "原剧本中村民不再质疑沈砚川被转译为村民顺着沈砚川手势分头行动，后续保留周大柱喊新桩、沈砚川回应和这地不卖台词。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "公章和底单先位于石桌，勘验员6-9秒将其装入防水袋并持有，再询问赵有福盖章来源，道具归属有可见过渡。",
      "fix_instruction": "若不通过，应补充勘验员装袋、封袋或举起防水袋的可见动作。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "本组全为现场对白，勘验员、赵有福、赵成武、巡查队长均在画面中可见并有真实对话对象，没有心声或画外音误承载。",
      "fix_instruction": "若不通过，应改成明确现场开口对象或标注画外音来源及闭口反应。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载周大柱追问、村民指责、沈砚川赔担、林知夏重核和村民作证，均为同一晒场追责冲突内的短句交锋，14秒4段可表演。",
      "fix_instruction": "若不通过，应拆出村民作证为独立短承接组或压缩非关键反应。"
    },
    {
      "group": "第8组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第7组尾部沈家人面向烂果园，第8组组首转到晒场边通往东排果园的小路，周大柱和村民带工具下果园，完成从安慰到行动的过渡。",
      "fix_instruction": "若不通过，应在第7组尾或第8组开头补充村民拿工具、朝果园移动的动作。"
    },
    {
      "group": "第13组",
      "type": "timing_math",
      "result": "pass",
      "evidence": "第13组为8秒片尾动作意象，2个时间段连续0-4秒、4-8秒，总时长为整数且在6-15秒硬范围内，承接上一组种回来的台词。",
      "fix_instruction": "若不通过，应并入第12组或明确作为片尾动作余波保留。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现Seedance说明、模板编号、参考图占位符、自动正反打、广告字卡或模板化批量描述。",
      "fix_instruction": "若不通过，应删除模型说明和模板污染词，改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第13组",
      "rule": "timing_math",
      "problem": "第13组为8秒短组。",
      "evidence": "该组只承载两人并肩下沟和第一锹新泥翻起，是第12组宣告后不可硬凑的片尾动作意象，短组理由成立。",
      "fix": "交付时保留为短收束组，不需要扩写到10秒。"
    }
  ]
}
