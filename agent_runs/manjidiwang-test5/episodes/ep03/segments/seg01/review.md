{
  "pass": true,
  "summary": "seg01两组分镜忠实于原剧本，对话指向明确，时长计算合理，空间锁定完整，格式正确。",
  "checked_groups": ["第1组", "第2组"],
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
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "第1组第3镜李娟台词'太阳打西边出来了？起这么早'共10字，按普通对白4.5字/秒=2.2秒，分配2秒，符合短台词2秒规则。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组组首空间锁定明确朱文浩位于画面左侧刚站起身、李娟位于画面右侧端着茶杯，与第1组尾部李娟端杯发问、朱文浩坐在餐桌前的状态自然衔接，人物位置连续。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "第2组完整保留原剧本全部台词：'母亲，今天麻烦您陪我去苏家''去那干嘛？''提亲''跟苏家大女儿苏清寒？''是的''集团高岭之花，被你拿下了？''恋爱三年，时机成熟''有意思，老苏老脸往哪搁''买套正装，我给你撑场子'，无删减无新增。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱天和在组首空间锁定中有明确位置（餐桌右侧，面向门口方向），在第1镜说完台词后从门口离开；李娟在第2镜从楼梯走下获得入场；朱文浩在组首有明确位置（餐桌左侧）。所有关键人物均有可生成来源。",
      "fix_instruction": "无需修改，人物可用性已满足规则。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组以李娟端杯惊讶发问、朱文浩坐在餐桌前收尾；第2组组首写朱文浩刚站起身、李娟端着茶杯，位置和道具状态连续，过渡自然。",
      "fix_instruction": "无需修改，组间衔接已满足连续性规则。"
    },
    {
      "group": "第1组",
      "type": "filmability",
      "result": "pass",
      "evidence": "所有不可视信息已转译为可见细节：'惊讶'转译为眉毛微挑、嘴角带笑的面部表情；'大步出门'转译为朱天和快步走向门口的动作。无不可视信息残留。",
      "fix_instruction": "无需修改，可视化转译已满足规则。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "generation_density",
      "problem": "第1组第1镜为纯环境全景无台词，占2秒，节奏稍慢但作为新场景开场可接受。",
      "evidence": "全景，朱家别墅餐厅...红木餐桌上摆着精致早点。0-2秒无台词。",
      "fix": "可选：缩短至1.5秒或加入朱天和起身动作，但当前处理作为场景交代已合格。"
    }
  ]
}