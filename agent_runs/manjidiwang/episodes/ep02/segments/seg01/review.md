{
  "pass": true,
  "summary": "seg01 两组均忠于原剧本，空间锁定完整，时长合规，对话指向明确，无硬性错误。",
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
      "evidence": "2-6秒画外音22字/4秒=5.5字/秒，符合5.2字/秒基准；6-10秒情绪台词22字/4秒=5.5字/秒，符合6.0字/秒情绪基准向上取整。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "组首空间锁定明确列出朱文浩位于画面中央、侧对镜头、脸朝画右，电脑屏幕与书架位置清晰，单组物理空间为书房，无跨场景硬切。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "朱文浩皱眉台词'内卫森严的别墅区谁能进？'与OS'必然是有人授意。'均完整保留，未删减、未改写，敲门声作为动作节点自然嵌入0-2秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "本组仅朱文浩一人，在组首空间锁定中已明确其坐在办公桌后、侧对镜头、脸朝画右，满足可生成位置与可见状态。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾为朱文浩提笔记录状态，第2组组首为朱文浩仍坐办公桌后、握笔、面前摊纸，人物位置与道具状态连续，无跳变。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第1组",
      "type": "filmability",
      "result": "pass",
      "evidence": "原剧本中的'冷笑''敏锐''提笔'等情绪/动作标签均已转译为可见的面部表情与手部动作，无抽象概念直接输出。",
      "fix_instruction": "无需修改"
    }
  ],
  "issues": [],
  "warnings": []
}
