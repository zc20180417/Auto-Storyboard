{
  "pass": true,
  "summary": "seg03（第5-8组）通过审核，公寓对峙场景刀抵喉、以命要挟、忠诚之债三个高潮节拍均合理编排，心声正确标注闭口，无硬错误。",
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
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "0-5秒：苏清寒掏刀抵喉+逼问，动作描述精简至20字内，对白39字按情绪语速5.2字/秒=7.5秒，但实际分段承载：第一句17字约3.3秒+第二句22字约4.2秒，分入0-5秒和5-8秒两个时间段，节奏合理。"
    },
    {
      "group": "第7组",
      "type": "space_locking",
      "evidence": "全组保持单一物理空间（东湖湾公寓客厅），0-6秒朱文浩揭露母亲手术事实，6-9秒刀掉捡起递回，9-12秒站起说话，所有动作均在同一客厅空间内完成。"
    },
    {
      "group": "第8组",
      "type": "script_fidelity",
      "evidence": "原剧本所有关键台词和动作完整保留：苏清寒追问'为什么帮我？'、朱文浩回答'不是帮你。是让你欠我。''欠我的债，要用忠诚来还。'、门关上、瘫坐沙发、心声'他可怕得让人心安。这是什么样的怪物？'"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组为公寓场景首组，无需与前组衔接。组首空间锁定完整声明朱文浩坐在沙发上、苏清寒站在茶几旁、财务报表在茶几上。",
      "fix_instruction": "N/A"
    },
    {
      "group": "第6组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩和苏清寒均在组首空间锁定中声明位置：朱文浩坐在沙发上（画面左侧），苏清寒站在茶几旁（画面右侧），手提包挂在肩上。苏清寒后续掏刀动作从包中取出，来源合理。",
      "fix_instruction": "N/A"
    },
    {
      "group": "第8组",
      "type": "filmability",
      "result": "pass",
      "evidence": "心声'他可怕得让人心安。这是什么样的怪物？'已正确标注为心声格式，苏清寒嘴唇闭合、不做口型。门关上、瘫坐沙发、低头看刀均为可拍动作。无不可视信息。",
      "fix_instruction": "N/A"
    }
  ],
  "issues": [],
  "warnings": []
}