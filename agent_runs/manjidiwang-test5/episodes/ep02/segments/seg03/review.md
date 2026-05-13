{
  "pass": true,
  "summary": "第5-8组审核通过。客厅场景台词完整保留，高明检查后退场动作清晰，父子对话节奏合理，递纸揭示底牌有完整动作链。",
  "checked_groups": ["第5组", "第6组", "第7组", "第8组"],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "generation_density": "checked",
    "space_locking": "checked",
    "format": "checked",
    "character_availability": "checked",
    "handoff_continuity": "checked",
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "朱天和5字+朱文浩10字+高明9字+朱天和8字=32字，10s组内节奏合理，高明退场有完整关门动作。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "evidence": "3个时间段：递水+质问、揭露+反应、追问+坐下+回答。强节拍3个（递水、揭露栽赃、坐下交底），无过载。"
    },
    {
      "group": "第7组",
      "type": "script_fidelity",
      "evidence": "台词'苏吃暗亏绝不善罢甘休''明天开会敲打内卫部''不可捂盖子只会坐实心虚''那你想借题发挥''明天大张旗鼓去苏家提亲''火药桶搬到他办公桌上''你这是把他架在火上烤'全部保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "高明搀扶朱天和从门口进入，朱文浩从楼梯下方走来，三人均在组首有明确位置和朝向。",
      "fix_instruction": "无需修复，人物可用性完整。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "G05组尾高明关门离开、朱天和站客厅中央、朱文浩站楼梯旁；G06组首朱天和坐沙发上揉眉心、朱文浩站沙发旁端水。朱天和从站立到坐下有自然过渡。",
      "fix_instruction": "无需修复，组间连续性完整。"
    },
    {
      "group": "第8组",
      "type": "filmability",
      "result": "pass",
      "evidence": "城投三亿亏空通过递纸动作可视化展示，纸张在茶几上摊开有明确道具状态。'烂账底牌''掀翻总裁位置'通过台词自然表达。",
      "fix_instruction": "无需修复，不可视信息已通过道具动作和台词转译。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第7组",
      "rule": "dialogue_pacing",
      "problem": "第7组4个时间段含7句台词（54字/13秒），台词密度较高，但均为短句连续对白交锋，整体节奏在可接受范围。",
      "evidence": "朱天和22字+朱文浩22字+朱天和10字=54字/13s=4.2字/秒，合理。",
      "fix": "无需修改。"
    }
  ]
}
