{
  "pass": true,
  "summary": "seg01分镜稿无硬性问题，时长计算准确，空间锁定完整，台词指向明确。",
  "checked_groups": [
    "第1组",
    "第2组"
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
      "evidence": "3-5秒赵德胜热情台词10字/6.0≈2秒，实际2秒；7-11秒赵德胜职责台词12字/5.2≈3秒加倒水1秒共4秒，实际4秒；各镜头时长与语速计算一致。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "组首空间锁定明确列出朱文浩位于画面右侧手持水杯、赵德胜位于画面中央，人物画面位置与身体朝向完整，未出现同上或简写。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本报到、倒水、递水、欢迎台词、职责介绍等关键动作与台词全部保留，未删减或新增剧情。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩与赵德胜均在组首空间锁定中获得明确位置与身体朝向，敲门后赵德胜迎上前的入场动作发生在台词之前。",
      "fix_instruction": "已通过，无需修复"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组以赵德胜递出水杯收尾，第2组以朱文浩手持水杯开场，道具状态连续；同一场景内人物位置自然衔接。",
      "fix_instruction": "已通过，无需修复"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "心声内容通过画外音形式呈现，转身出门为可见动作，冷笑为面部表情，无抽象不可视信息。",
      "fix_instruction": "已通过，无需修复"
    }
  ],
  "issues": [],
  "warnings": []
}