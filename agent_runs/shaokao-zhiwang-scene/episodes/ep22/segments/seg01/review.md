{
  "pass": true,
  "summary": "已对第22集9组竖屏分镜逐项审查，货单揭露、当街对峙、后厨追账的台词与人物关系均保留，无阻断交付问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组",
    "第8组",
    "第9组"
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
      "evidence": "原剧本中马会拍下单据、林小满询问进货单、马会说明许安老周肉市天天鲜货、唐婶和路人查看日期斤两，均按原顺序写入0-10秒。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "0-5秒承载路人甲和路人乙约21个有效字，字秒比约4.2；5-9秒韩彪喝问约11个有效字，字秒比约2.8；均低于6.5硬上限。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "韩彪伸手抢单据后，第4组组首明确他右手靠近案板、马会手掌压住货单；0-3秒许安抬手挡住手腕，3-8秒林小满扬起许安那叠单据，道具归属清楚。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "evidence": "后厨新场景组首明确卷帘门、灶台、火炉、账本位置，并列出韩彪、马会、阿顺初始站位；投资人甲乙在10-14秒从前厅门口进入后再发声，人物可用性成立。"
    },
    {
      "group": "第8组",
      "type": "dialogue_direction",
      "evidence": "投资人甲对韩彪喝道让他说，马会对投资人甲和投资人乙说明真稳味的人不是韩彪，阿顺对马会低声反应，韩彪和马会互相对话，所有现场对白都有真实对象。"
    },
    {
      "group": "第9组",
      "type": "timing_math",
      "evidence": "第9组时间段为0-2、2-6、6-10、10-11、11-14秒，相加14秒且最后一段结束于标题总时长；镜头数5个与标题一致。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "许安追问还有呢、马会抽出韩彪货单、林小满指出冻货压货、马会说明宴席前几批就是这些，未改动证据链因果。",
      "fix_instruction": "若不通过，应恢复许安追问、韩彪货单、冻货压货、宴席前几批四个信息点及原台词顺序。"
    },
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "韩彪在组首已经位于背景对街，5-9秒快步来到摊前后才开口喝问，未出现无来源突然说话。",
      "fix_instruction": "若不通过，应在组首补韩彪空间位置，或在他说话前补明确入场动作。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾部韩彪被众人盯住，许安挡在案板前；第5组组首延续韩彪僵在案板外侧、许安仍挡在案板前、林小满持单据的状态，转身离开有可见过程。",
      "fix_instruction": "若不通过，应在第4组尾或第5组开头补韩彪转身离开、许安收手、单据归属的具体状态。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第6组包含卷帘门落下和韩彪拽住马会、两句冲突对白、阿顺插话、投资人甲入场追问，分成4个时间段，总时长14秒，入场和对白没有挤在同一短镜头里。",
      "fix_instruction": "若不通过，应拆分投资人入场追问，或把韩彪拽人动作与后续问责分到不同组。"
    },
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "第7组最长台词为投资人乙3-7.5秒约15个有效字，字秒比约3.3；其余2.5-3秒对白均低于硬上限，情绪对白没有被压缩。",
      "fix_instruction": "若不通过，应延长对应对白时间段或把投资人追问与韩彪回应拆开。"
    },
    {
      "group": "第8组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "本组均为画面内真人现场开口，没有心声、电话音或画外音；每句对白都由对应角色在画面内承载口型。",
      "fix_instruction": "若不通过，应把非现场声音改成画外音并写明嘴唇闭合，或恢复现场说话人的可见位置。"
    },
    {
      "group": "第9组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终正文没有出现模型说明词、模板编号、参考图占位符、首尾帧说明或模板化批量描述；画面风格和负面词保持自然生产约束。",
      "fix_instruction": "若不通过，应删除模型说明词、模板占位符或模板化表达，并改成可见动作、道具和人物站位。"
    }
  ],
  "issues": [],
  "warnings": []
}
