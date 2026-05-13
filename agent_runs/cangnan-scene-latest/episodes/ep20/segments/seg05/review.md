{
  "pass": true,
  "summary": "seg05保留宋天明命令动手、黑衣人举武器、陆凡制裁反问、至尊黑卡亮出、独眼老者阻止和身份揭示。",
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
    "filmability": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组保留宋天明“给我上！把他拿下！”、黑衣人举武器和陆凡“动用私家武装……”的台词顺序。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "至尊黑卡由陆凡0-3秒取出并砸到桌面，后续宋天明瞥见、独眼老者识别和宋天明震惊均围绕桌面黑卡展开。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组8.5-13秒承载独眼老者提醒和宋天明短反问，约29个有效字4.5秒，字秒比约6.4，未超过6.5硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "第2组8.5-13秒为快速惊恐提醒加短反问，约29个有效字4.5秒，字秒比约6.4，且包含明确说话人切换反应。",
      "fix_instruction": "若不通过，应把宋天明反问拆到单独2秒反应镜头。"
    },
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "独眼老者在第1组组首已位于宋天明身后右侧背景，能自然在第2组站出来阻拦黑衣人。",
      "fix_instruction": "若不通过，应在第1组组首补入独眼老者位置。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "独眼老者台词“老爷！不可！那是龙国商会最高裁决官的黑卡！”和宋天明“商会裁决官？这怎么可能！”均完整保留。",
      "fix_instruction": "若不通过，应恢复被删改的身份揭示台词。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "两组均未出现模板编号、参考图、自动分镜、字幕或广告式表达。",
      "fix_instruction": "若不通过，应删除污染项。"
    }
  ],
  "issues": [],
  "warnings": []
}
