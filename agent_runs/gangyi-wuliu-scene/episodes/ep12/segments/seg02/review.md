{
  "pass": true,
  "summary": "seg02 两组完整保留林刚交内存卡、王百川看片震怒、王强在副驾画面中暴露并跪地认错，屏幕画面已明确标识，无硬性问题。",
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
      "type": "script_fidelity",
      "evidence": "0-3秒保留林刚踹门并拍下内存卡，3-5秒保留“自己看”，5-11秒保留王百川插卡和播放重卡被砸、突围全过程，11-13秒保留“敢动我的货！反了！”。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "主要空间为仓库办公室，8-11秒明确写为电脑屏幕画面，属于屏幕画面例外，不会误解为角色现实跨到盘山夜路。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "林刚“看第一辆车副驾。”在0-2秒完成，王百川“畜生！给我跪下！”在5-7秒完成，王强“叔！我错了！”在10-12秒完成，均为短台词2秒节拍。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "组首锁定林刚在门外方向、王百川在桌边，林刚踹门入屋后才拍内存卡和说话，王百川已在桌边可操作电脑。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "王强在组首被锁定为位于背景门边阴影处，5-7秒被王百川怒斥前已具备可生成位置。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "王强露馅通过电脑屏幕放大副驾驶座、满脸惊恐和随后跪地认错呈现，均为可见动作和表情。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
