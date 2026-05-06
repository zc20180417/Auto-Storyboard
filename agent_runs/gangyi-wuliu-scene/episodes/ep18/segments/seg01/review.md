{
  "pass": true,
  "summary": "seg01已按原剧本逐项审核，5组均保持重卡经销店单一主空间，台词、关键动作、道具状态和组间衔接无硬性问题。",
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
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本中林刚抓铁烟灰缸、躲过当头一棍、说“太慢了”、反手敲倒打手甲，以及孙彪命令“给我往死里打”均按顺序保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "经理台词“别打啦！我的店啊！我报警啦！”约11字/2秒，字秒比约5.5；林刚短句“还有谁想挨揍？”配合夺棍动作3秒，未超过硬性语速上限。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "本组主空间仍为重卡经销店展厅内，门外黑色轿车通过玻璃门可见，王百川和八个保镖在8-14秒从门口入场后再开口，未跨入无标识的第二主空间。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "evidence": "第3组结尾王百川已站在展厅入口内侧、孙彪握刀愣住；第4组组首延续王百川、保镖、孙彪持刀和林刚持棍的位置，道具状态连续。"
    },
    {
      "group": "第5组",
      "type": "timing_math",
      "evidence": "第5组时间段为0-3、3-5、5-8、8-11、11-13秒，相加13秒，与标题总时长13秒和镜头数5个一致。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "林刚、打手甲、孙彪、经理和其余打手均在组首拥有明确画面位置和身体朝向，打手甲在行动前已位于画面左侧举棍逼近。",
      "fix_instruction": "无。"
    },
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "王百川和八个保镖未在组首预置，但8-14秒明确从玻璃门大步走进展厅，并在入场后王百川才喊出台词。",
      "fix_instruction": "无。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "孙彪问“王总？您怎么亲自来了？”，王百川甩耳光并说“瞎了狗眼！林刚是我签的车队老板！”，随后刀子掉地、孙彪解释、林刚说明买车受阻，均未删改。",
      "fix_instruction": "无。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾弹簧刀掉在地上、孙彪捂脸站在王百川面前；第5组组首写明弹簧刀落在地砖上、孙彪捂脸站立，随后才跪下求饶。",
      "fix_instruction": "无。"
    },
    {
      "group": "第5组",
      "type": "filmability",
      "result": "pass",
      "evidence": "“城南的活儿全停”“五台车落户”等不可视业务信息均通过王百川对孙彪和经理的台词表达，画面只补充跪下、指向展车、经理点头等可拍动作。",
      "fix_instruction": "无。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第4组",
      "rule": "dialogue_pacing",
      "problem": "林刚解释句节奏偏快但不超过硬性阈值。",
      "evidence": "第4组9-11秒，台词“他要打断我的腿，还不让我买车。”有效字数13，镜头2秒，字秒比约6.5。",
      "fix": "可在人工精修时将该句拆成林刚近景和王百川反应，但当前不阻断通过。"
    },
    {
      "severity": "soft",
      "group": "第5组",
      "rule": "dialogue_pacing",
      "problem": "经理答应句节奏偏快但在可接受范围内。",
      "evidence": "第5组11-13秒，台词“马上办！绝不耽误林老板发财！”有效字数13，镜头2秒，字秒比约6.5。",
      "fix": "可在人工精修时增加极短反应节拍并重组第5组，但当前不阻断通过。"
    }
  ]
}
