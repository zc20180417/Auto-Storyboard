{
  "pass": true,
  "summary": "seg01 覆盖本集全部11组，夜市收束与新铺开张的台词、空间、道具和组间衔接均已对照原剧本审过，未发现硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组",
    "第8组",
    "第9组",
    "第10组",
    "第11组"
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
    "prompt_pollution": "checked",
    "prop_continuity": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "许安与韩彪的四句短对白被分在2.5-3.5秒的近景交锋里，包含必要的拦路、握旧炭夹和咬牙反应，未出现超过6.5字/秒的口型压力。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "结果单在组首位于评选桌上，7-9秒由主持人拿起并走到画面中央，9-12秒再举着结果单公布结果，关键道具归属有可见过渡。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "主持人宣布“本次夜市招牌，许安炭炉。”，林小满、唐婶、路人甲、路人乙的庆祝台词均按原剧本顺序保留，韩彪退在旁边未新增反击动作。"
    },
    {
      "group": "第7组",
      "type": "space_locking",
      "evidence": "新铺面开门组只使用新铺面门口这一现实空间，组首锁定了旧炭炉、柜台、许安、林小满、韩秀兰、唐婶、老周、马会和两名路人的位置与朝向。"
    },
    {
      "group": "第10组",
      "type": "prompt_pollution",
      "evidence": "开烤组直接写鞭炮、落串、火起、人物发问和回应，没有出现模型说明、模板编号、占位符、字幕或广告式口号。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "许安的两句台词均写成对韩彪说道，韩彪的质问也明确对许安发出，没有假对白对象或无对象对白。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "许安指出韩彪怕别人先想到自己、韩彪沉默、韩秀兰说“做吃的，先做人。”以及韩彪说“我只是想让人看见我。”均保留原剧本顺序和情绪转折。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第5组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "0-2秒全场安静时明确众人嘴唇闭合不做口型；之后主持人、林小满、唐婶和两名路人的现场对白均由画面内人物开口承载。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "夜市评选结束后进入“几天后”的新铺面新场景，场景跳转由组首明确新时间和新空间；同场景后续第8组继续旧炭炉、柜台和众人围店状态。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第9组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "医院钱够了的核心对白分为林小满低声告知、许安一顿追问、韩秀兰回应和许安简短确认，台词量与14秒内的停顿、视线和炉边动作相匹配。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第10组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "14秒内承载鞭炮两响、第一把串落炉、林小满问以后、许安回应守火、唐婶喊开烤五个轻中节拍，没有叠加复杂走位或关键道具跳变。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第11组",
      "type": "filmability",
      "result": "pass",
      "evidence": "片尾以翻串、收火、起签和旧炭炉火光持续亮着收束，使用可见手部动作、炉火和环境声，没有把抽象结论当作画面主体。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
