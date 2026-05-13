{
  "pass": true,
  "summary": "seg03两组均通过审核，书房对话节奏合理，道具操作与台词自然融合。",
  "checked_groups": ["第4组", "第5组"],
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
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "9-14秒连续对话节拍包含朱文浩'打一巴掌必给甜枣'（8字）+'刘家会给我补偿'（7字）和朱天和'他们会安排你去哪'（8字）共23字+倒茶递茶动作在5秒内完成，台词4.6字/秒，道具操作与台词自然同步。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "evidence": "第5组包含3个强节拍（朱文浩揭示去向、朱天和震惊、朱文浩冷笑+沉声宣言），均属同一冲突目标下的信息递进，未超过复杂度预算。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "原剧本朱天和砸茶杯、朱文浩倒茶递茶、'这是苏总裁的借刀杀人'、'打一巴掌必给甜枣'等关键台词和道具操作全部保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱天和坐于书桌后位于画面右侧，朱文浩坐于茶台边位于画面左侧，两人位置和朝向在组首空间锁定中明确。",
      "fix_instruction": "无需修复，角色位置和朝向完整。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组以朱天和手握茶杯悬在半空收尾，第5组组首朱天和仍手握茶杯、表情困惑，空间和道具状态连续。",
      "fix_instruction": "无需修复，空间和道具状态连续。"
    },
    {
      "group": "第5组",
      "type": "filmability",
      "result": "pass",
      "evidence": "所有信息已转译为可见画面：朱文浩的冷笑通过嘴角和眼神呈现，'借刀开路'的策略意图通过台词直接表达。",
      "fix_instruction": "无需修复，不可视信息已转译为可见画面。"
    }
  ],
  "issues": [],
  "warnings": []
}
