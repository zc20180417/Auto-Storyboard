{
  "pass": true,
  "summary": "seg01两组均通过审核，台词节奏合理，空间锁定完整，原剧本忠实。",
  "checked_groups": ["第1组", "第2组"],
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
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "朱文浩连续三句回答（闭嘴旁观不站队/点火烧身转移压力/搁置争议先定纪要）共18字在4秒内完成，4.5字/秒，符合普通对白节奏。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组保持单一物理空间（集团特招考场），组首空间锁定列出全部在场人物及其位置，与第1组组尾状态兼容。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "原剧本考官甲'不合格'、三名考官齐刷写下最低分、周正明'你们这是明目张胆压分'、朱文浩'利益面前规则只是废纸/但废纸也能包住火'、推开椅子转身离场等关键台词和动作全部保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱文浩、周正明、考官甲、邱瑞均在组首空间锁定中拥有明确位置和朝向，朱文浩位于画面中央面向讲台，周正明坐于讲台左侧，考官甲坐于讲台右侧，邱瑞坐于后排角落。",
      "fix_instruction": "无需修复，角色位置和朝向完整。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组以邱瑞点头收尾，第2组组首空间锁定保持相同空间布局和全部在场人物，朱文浩仍坐于中央椅子上，与第1组结尾状态连续。",
      "fix_instruction": "无需修复，空间和人物状态连续。"
    },
    {
      "group": "第1组",
      "type": "filmability",
      "result": "pass",
      "evidence": "所有信息已转译为可见画面：'肃杀气氛'通过灯光和空间布局表现，邱瑞的'微微点头'通过面部表情和动作呈现。",
      "fix_instruction": "无需修复，不可视信息已转译为可见画面。"
    }
  ],
  "issues": [],
  "warnings": []
}
