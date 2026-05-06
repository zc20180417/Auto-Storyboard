{
  "pass": true,
  "summary": "已对第3集单段分镜逐组核对原剧本、时长、空间锁定、对话指向和自然格式，未发现硬性问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组"
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
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "2-6秒承载赵大强“哎哟！老天开眼遭报应了吧！”和村民甲“活该！连村里人的钱都敢黑。”，有效字数约22字，镜头4秒，约5.5字/秒；6-8秒林刚下车并说“是挺准的。警察同志，过来吧。”，短句配合下车动作，未超7字/秒。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "全组保持白天露天停车场一个物理空间，警察甲、警察乙在组首已位于背景右侧墙角并在0-2秒走到赵大强面前；林刚手机红外监控作为屏幕画面出现，没有硬切到夜间现实空间。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "赵大强“我买！多少钱？”，林刚“五万。少一分进去蹲三年。”，赵大强“这破车五千都不值！”，林刚要求警察带走，赵大强抱腿答应给钱，均按原剧本顺序保留。"
    },
    {
      "group": "第6组",
      "type": "dialogue_direction",
      "evidence": "林刚、物流主管的每句对白均写明对象，例如林刚对物流主管说道“主管，我想接干线物流的活。”，物流主管对林刚问道“乡下来的？你有车吗？”。"
    },
    {
      "group": "第7组",
      "type": "timing_math",
      "evidence": "第7组时间段为0-4、4-6、6-9、9-11秒，合计11秒，与标题总时长11秒和镜头数4个一致。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "林刚在驾驶位、赵大强在车头外侧、村民甲和村民在背景左侧、警察甲和警察乙在远处墙角阴影后方均在组首拥有可生成位置，警察后续出场来源明确。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "红外证据被转译为手机屏幕中的夜间监控画面，赵大强倒白糖、林刚举手机、警察盯住赵大强均为可见动作，没有把“证据确凿”等抽象判断当作画面。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组结尾林刚举着手机、赵大强被警察盯住；第3组组首延续林刚持手机、赵大强站在车头附近双腿发软、警察甲靠近手铐，人物和道具状态连续。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "赵大强痛哭流涕转账、林刚看到到账提醒、拎起帆布包并说“以后你就是村里大老板了。”均完整保留，没有新增改变剧情的处罚或冲突。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第6组为物流中心办公室单一空间，组首写明办公桌、物流主管坐在桌后、林刚在门口提帆布包，现金在本组0-2秒被拍到桌上。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第7组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "林刚站在桌前、物流主管坐在桌后，驾照、现金、抽屉和陈旧单子均在角色行动前具备明确位置或来源。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第7组",
      "rule": "dialogue_pacing",
      "problem": "主管最后一句情绪台词节奏偏快但不构成硬错误。",
      "evidence": "9-11秒“今晚有个送命件，敢接留你。”有效字数约13字，镜头2秒，约6.5字/秒，处于6-7字/秒可接受区间。",
      "fix": "如后续人工想放缓，可将该句与按住陈旧单子的动作扩为3秒，但需重新压缩同组其他镜头保持总时长。"
    }
  ]
}
