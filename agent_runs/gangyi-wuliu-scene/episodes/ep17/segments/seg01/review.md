{
  "pass": true,
  "summary": "seg01分镜经节奏修复后保留原剧本全部台词、关键动作和人物关系，4组均为重卡经销店销售大厅单一物理空间，未发现硬性问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组"],
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
      "evidence": "林刚对经理说“外面那五台重卡，我全要了。立刻提车。”有效字数15字/3秒，约5.0字/秒，并同步敲桌动作；经理“好嘞老板！现金结账，马上给您办手续！”有效字数15字/3秒，约5.0字/秒；孙彪“慢着。这五台车，我今天包圆了。”有效字数12字/2秒，约6.0字/秒，未超过7字/秒，也无明显拖慢。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "本组场景始终为重卡经销店销售大厅，组首明确林刚在画面左侧、孙彪在画面右侧、经理在背景销售台后方，黑皮箱和雪茄位置连续。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "保留林刚收箱子说“关你屁事。别挡路。”、孙彪提王强并阻止买车、林刚握拳反问、孙彪拍手叫人、打手持棒球棍堵门等原剧本顺序和信息。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "2-8秒连续对话节拍承载经理劝阻、林刚回答和脱外套动作，有效字数约33字/6秒，约5.5字/秒，符合连续对话节奏；8-10秒孙彪命令约13字/2秒，约6.5字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "林刚和经理在组首已有明确位置和朝向；孙彪在10-12秒先以手臂按住皮箱入场，12-15秒走近后才开口说话。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾孙彪手按黑皮箱、经理在销售台后；第2组组首延续孙彪压箱、林刚和经理在销售台两侧的对峙状态。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "打手在第3组13-15秒从玻璃大门外挤入并堵住门口，本组内没有让打手在入场前说话或行动。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组组尾打手堵死玻璃大门，第4组组首继续写玻璃大门被十几个打手堵住，打手甲位于画面中央偏后并持棒球棍。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第4组",
      "type": "filmability",
      "result": "pass",
      "evidence": "“惹不起”“给脸不要脸”等不可视态度均通过经理后缩冒汗、孙彪甩雪茄挥手、打手举棍冲近等可见动作呈现。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
