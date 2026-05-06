{
  "pass": true,
  "summary": "seg02两组已核对病房剧本，苏清寒苏醒、密钥、朱文浩破解和雇佣兵警告均完整保留。",
  "checked_groups": ["第3组", "第4组"],
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
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "第3组逐项保留苏清寒睁眼摘氧气面罩、朱文浩倒水、郑建国儿子安置、U盘密钥、红星厂地下室无密钥进不去。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "第4组0-3秒承载密钥已破解约11字，3秒带递水动作；3-5秒朱文浩短句约10字；5-7秒苏清寒警告约13字，2秒字秒比约6.5，均未超过硬错误阈值。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "第4组始终在市医院特护病房，朱文浩和苏清寒位置、病床、水杯、床头设备均在组首锁定。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "苏清寒位于病床右侧，朱文浩位于床边左侧，二人身体朝向和视线在组首明确。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾朱文浩拿水杯站床边，第4组首延续他手拿水杯、苏清寒靠枕头的状态。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第3组",
      "type": "filmability",
      "result": "pass",
      "evidence": "虚弱状态由胸口起伏、抓床单、靠枕喘息表现；密钥信息通过台词直接出现，不依赖抽象说明。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
