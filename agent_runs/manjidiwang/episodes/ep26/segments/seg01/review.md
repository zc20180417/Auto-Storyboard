{
  "pass": true,
  "summary": "seg01已对照原剧本完成审核，茶杯、吐血、刘管家呼喊与朱文浩入门均保留，无硬性问题。",
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
      "evidence": "刘管家台词“老爷，今晚风雨真大。”置于4-6秒，约8个有效字/2秒；朱天和台词“鼎丰资本的事，让我心神不宁。”置于6-8秒，约12个有效字/2秒，未超过7字/秒。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "保留窗外雷电交加、朱天和饮茶、刘管家端果盘、朱天和揉眉心、茶杯脱手和“咳咳……这茶……”等原剧本信息。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组始终在朱家别墅客厅内，组首列出朱天和、刘管家和客厅大门，朱文浩通过5-8秒踹门入场获得可生成来源。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱天和在沙发中央，刘管家在画面左侧端果盘，二人说话与动作前均在组首空间锁定中有明确位置和朝向。",
      "fix_instruction": "无须修复；若新增人物参与动作，应先在组首或行动前给出可生成位置。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组结尾茶杯落在茶几旁、朱天和捂胸，正接第2组组首茶杯落在茶几旁、朱天和前倾捂胸的状态。",
      "fix_instruction": "无须修复；若改变朱天和位置，应在组尾或组首补足过渡动作。"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "心神不宁由揉眉心和台词承载；暴雨、吐血、踹门、雨水入室均转译为可见动作、道具和声光变化。",
      "fix_instruction": "无须修复；不可视心理信息应继续用表情、动作、台词或光影承载。"
    }
  ],
  "issues": [],
  "warnings": []
}
