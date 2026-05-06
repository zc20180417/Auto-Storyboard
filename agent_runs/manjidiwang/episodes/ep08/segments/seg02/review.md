{
  "pass": true,
  "summary": "seg02三组均保持单一物理空间，台词与关键动作忠于原剧本，时长计算与节奏合格，无硬错误。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "evidence": "朱文浩'我提议增设纪律督察长一职'12字/2秒=6.0字/秒；班主任'特训班没有这个先例'12字/2秒=6.0字/秒；朱文浩'总部督导组最新要求'9字/2秒=4.5字/秒；朱文浩'特训班必须设立风控督察岗'12字/2秒=6.0字/秒。均在合理区间，无超速或拖慢硬错误。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "培训中心阶梯教室单一物理空间，组首空间锁定明确文件落在朱文浩面前桌上，朱文浩位于中央偏左、刘宇位于右侧前排、班主任位于深处讲台，道具与人物位置清晰。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "朱文浩'名正言顺，专查违纪''班长，记得按时交活动财报'、班主任'既然是总部要求，那就定下'、刘宇'凭什么你来当'等8-2核心台词全部保留，'脸色大变''被气场震慑''如鲠在喉'等关键动作与表情均已转译为可见镜头描述。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩、刘宇、班主任均在组首空间锁定中有明确画面位置与身体朝向，无'尚未进入''暂未出现'等负面描述，所有说话人物均满足可用性。",
      "fix_instruction": "当前已通过，无需修改"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾文件落在朱文浩面前桌上，第2组组首文件仍在朱文浩面前桌上；第2组组尾朱文浩逼近姿态未收，第3组组首朱文浩保持逼近姿态，刘宇仍在右侧前排，连续性一致。",
      "fix_instruction": "当前已通过，无需修改"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "原剧本'班主任被其气场震慑，不敢反驳'已转译为'双手下意识攥紧讲台边缘，不敢反驳，视线在朱文浩和刘宇之间游移'，通过手部动作与视线游移呈现震慑状态，无抽象概念残留。",
      "fix_instruction": "当前已通过，无需修改"
    }
  ],
  "issues": [],
  "warnings": []
}
