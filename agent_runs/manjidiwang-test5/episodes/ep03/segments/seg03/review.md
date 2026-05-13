{
  "pass": true,
  "summary": "seg03四组分镜忠实于原剧本，苏清寒入场和手腕抓取动作衔接自然，画外音口型隔离正确，全部台词保留完整。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组"],
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
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "第2组完整保留原剧本关键动作'朱文浩霸道地扣住苏清寒的手腕，将她拉到身侧'和台词'关关雎鸠，在河之洲'，以及苏清寒心声'他在教我如何下这盘棋'，无删减无新增。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "第4组第3镜苏晓晓台词'妈，爸要是知道非扒了我的皮'共11字，按情绪对白5.2字/秒=2.1秒，加发颤的表演状态分配2.5秒，节奏合理。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "evidence": "第3组包含4个强节拍：朱文浩转身宣告（动作+信息）、提亲宣言（信息）、李佳佳结巴反应（情绪）、朱文浩虚扶+高帽（动作+信息），分布在12秒内，每个节拍有充足表演时间，未过载。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "苏清寒在第2组组首未出场，但在第1镜（0-3秒）从楼梯走下获得明确入场动作，在第2镜（3-5.5秒）开始与朱文浩互动，满足入场先于行动的规则。其余人物（朱文浩、李娟、李佳佳、苏晓晓）在组首均有明确位置。",
      "fix_instruction": "无需修改，人物可用性已满足规则。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组以朱文浩说完恭维话、李佳佳慌乱无措收尾；第4组组首写朱文浩位于画面右侧面向李佳佳、李娟从沙发区站起，人物位置和状态与上一组自然衔接。李娟起身说'聘礼放下'是新的动作起点，过渡合理。",
      "fix_instruction": "无需修改，组间衔接已满足连续性规则。"
    },
    {
      "group": "第4组",
      "type": "filmability",
      "result": "pass",
      "evidence": "第4组苏清寒心声'釜底抽薪，苏这回遇到对手了'正确处理为心声，镜头描述写明苏清寒嘴唇闭合、不做口型，音画分离正确。心声内容已通过面部表情变化（眉头皱起→舒展→嘴角浮现笑意）转译为可见细节。",
      "fix_instruction": "无需修改，音画分离和可视化转译已满足规则。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "generation_density",
      "problem": "第2组第3镜（5.5-8秒）包含中等动作'扣住手腕、拉到身侧'，时长2.5秒，略紧但属于快速动作范畴，可接受。",
      "evidence": "中景，朱文浩大步上前，右手霸道地扣住苏清寒的手腕，五指收紧，将她拉向自己身侧。5.5-8秒，2.5秒。",
      "fix": "可选：如表演需要更流畅，可将此镜延长至3秒，相应缩短第4镜0.5秒。"
    }
  ]
}