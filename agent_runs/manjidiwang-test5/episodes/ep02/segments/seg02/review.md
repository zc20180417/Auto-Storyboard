{
  "pass": true,
  "summary": "第3-4组审核通过。门口对峙场景台词全部保留，对话指向明确，威压逼退节奏合理，王涛逃跑有完整动作链。",
  "checked_groups": ["第3组", "第4组"],
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
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "王涛23字/4.5=5.1s+换人0.3s+朱文浩4字/4.5=0.9s+中等挡门动作2s=8.3s，实际10s合理。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "evidence": "5个时间段包含：对峙揭露、威压逼问、王涛崩溃、逃跑。强节拍4个但均为轻量对白交锋，无复合动作链，无外部事件叠加，节奏合理。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "王涛台词'朱少，我给副董带土特产''这份企划书得当面交给他'完整保留；朱文浩'就在这说''李秘书许了你什么好处'完整保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩位于门框内挡门，王涛位于门外提袋，两人位置在组首空间锁定中明确。王涛有'往里挤'的入场动作。",
      "fix_instruction": "无需修复，人物可用性完整。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "G03组尾朱文浩堵门、王涛后退藏袋，G04组首朱文浩仍在门框内、王涛门外脸色发白，状态连续。",
      "fix_instruction": "无需修复，组间连续性完整。"
    },
    {
      "group": "第4组",
      "type": "filmability",
      "result": "pass",
      "evidence": "朱文浩'监控拍下你提现金进门'为信息揭露节拍，台词自然；王涛逃跑动作链完整（结巴→抱袋→踉跄逃离）。",
      "fix_instruction": "无需修复，不可视信息已通过台词和动作转译。"
    }
  ],
  "issues": [],
  "warnings": []
}
