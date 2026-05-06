{
  "pass": true,
  "summary": "seg01两组空间锁定完整，台词忠于原剧本，时长与节奏合格，无硬错误。",
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
      "evidence": "班主任'今天竞选班委，刘宇竞选班长'11字/2秒=5.5字/秒；雷军与刘宇连续对话节拍21字/4秒=5.25字/秒，含换人间隙，整体估算合理，未触发硬错误阈值。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "培训中心阶梯教室单一物理空间，组首空间锁定列出班主任（讲台正中）、朱文浩（左侧后排）、刘宇（右侧前排）、雷军（左侧中排）的画面位置与身体朝向，无跨场景硬切。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本8-1中班主任宣布、雷军起哄'刘大少当班长，众望所归'、刘宇得意'感谢大家，我一定做好服务'、朱文浩推辞'生活委员责重大，我难胜任'、刘宇嘲讽'怎么，朱少连端茶倒水都干不好'全部逐句保留，无删减或新增台词。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩虽在第1组无台词，但在组首空间锁定中明确位于画面左侧后排、侧对镜头、脸朝画右，已满足在场可用性要求。",
      "fix_instruction": "当前已通过，无需修改"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾刘宇说完台词看向雷军，第2组组首班主任仍在讲台正中、刘宇仍在右侧前排、朱文浩仍在左侧后排，人物位置与状态未发生跳变，连续一致。",
      "fix_instruction": "当前已通过，无需修改"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "原剧本'全班目光聚焦在朱文浩身上，带着戏谑'已转译为'全班学员目光齐刷刷聚焦在朱文浩身上，若干学员嘴角带笑，眼神带着戏谑'，通过群体视线与表情动作实现可视化，无抽象概念残留。",
      "fix_instruction": "当前已通过，无需修改"
    }
  ],
  "issues": [],
  "warnings": []
}
