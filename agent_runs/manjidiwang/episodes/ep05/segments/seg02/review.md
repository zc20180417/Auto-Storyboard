{
  "pass": true,
  "summary": "seg02分镜稿无硬性问题，会议室场景空间锁定完整，对话指向清晰，连续对话节拍时长合理。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组"
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
      "type": "space_locking",
      "evidence": "组首空间锁定完整列出王海涛、老孙、吴德海、朱文浩四人的画面位置与身体朝向，会议室单一物理空间，无跨场景硬切。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "3-10秒连续对话节拍包含王海涛10字怒喝、朱文浩24字连珠质问，按情绪对白6.0字/秒计算约6秒，加两次换人交锋间隙0.6秒，目标约7秒，实际7秒，节奏准确。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "王海涛从发怒到倒戈的情绪转变、郑总监独断专行、资金流向插不上手、朱文浩拿笔记录等关键台词与动作均保留，无删减新增。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "王海涛、老孙、吴德海、朱文浩均在组首空间锁定中拥有明确位置与身体朝向，朱文浩虽位于背景角落但已在场，后续抬手打断动作合理。",
      "fix_instruction": "已通过，无需修复"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组以朱文浩逼视质问收尾，第2组以王海涛坐直变色、老孙笔掉开场，同会议室场景内人物状态自然衔接，无位置跳变。",
      "fix_instruction": "已通过，无需修复"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "笔掉桌上、坐直、脸色大变、额头青筋、怒喝、寸步不让等均为可见动作或表情，无抽象心理判断替代画面。",
      "fix_instruction": "已通过，无需修复"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "有台词镜头时长比目标时长多1秒",
      "evidence": "11-14秒镜头'为什么没过风控会？'10字按情绪对白6.0字/秒计算约2秒，实际3秒",
      "fix": "可缩短至2秒或在组内微调，当前1秒偏差可接受"
    }
  ]
}