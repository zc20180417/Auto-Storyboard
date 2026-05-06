{
  "pass": true,
  "summary": "第10集第三段分镜忠于原剧本，对话指向清晰，时长计算准确，景别切换合理，空间锁定完整，无硬性错误。",
  "checked_groups": ["第1组", "第2组"],
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
      "evidence": "苏清寒11字台词按普通对白5.2字/秒取整3秒；朱文浩12字取整3秒叠加翻阅动作同步；18字台词取整4秒；13字台词取整3秒叠加递回动作同步。对话节拍紧凑，未出现拖慢。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "组首空间锁定明确列出天台苏清寒与朱文浩的位置、朝向及间距，单组仅涉及天台一个物理空间，风大衣摆等环境细节与场景一致。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "原剧本中'我去接人，这是扳倒他的关键'、'这很危险，黑皮那帮人没有底线'、'我若怕死，怎么做你的执棋人'及车钥匙交付均完整保留，未删减台词或新增剧情动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "组首空间锁定已明确列出苏清寒与朱文浩的画面位置与身体朝向，两人均在组首拥有可生成位置。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾为朱文浩递回卷宗、视线凝重；第2组组首两人仍在同一天台，位置与间距与上一组兼容。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第1组",
      "type": "filmability",
      "result": "pass",
      "evidence": "'凝重'转译为眉头微蹙与视线凝重；'笃定'转译为目光笃定锁住对方；'坚定'转译为眼神坚定。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "无台词镜头",
      "problem": "组首环境交代镜头2秒虽在允许范围内，但可考虑压缩至与递卷宗动作同步完成，以更快进入对话。",
      "evidence": "0-2秒：中景，集团天台，风卷苏清寒风衣下摆。苏清寒将一份卷宗递给朱文浩，朱文浩伸手接过。",
      "fix": "可与下一句台词合并或压缩至1秒，但当前2秒不阻断产出。"
    }
  ]
}
