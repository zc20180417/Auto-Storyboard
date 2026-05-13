{
  "pass": true,
  "summary": "seg01已对照原剧本完成审核，路障两侧的横屏轴线、胡永贵诱逼台词和村民失控动机均可交付。",
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
    "filmability": "checked",
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "evidence": "路障横贯画面中线，左侧村民挖土，右侧胡永贵在遮阳伞下握冰水，人物左右关系和关键道具位置清楚。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "村民甲台词约17字承载在2-5.5秒的3.5秒段落，胡永贵台词约21字承载在5.5-9秒的3.5秒段落，未超过硬上限。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留村民乙指责胡永贵、胡永贵嫁祸李燃并提出砸龙舟换通路的台词顺序，未新增改变剧情的动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "冰水杯从第1组右侧胡永贵手边延续到第2组右侧伞下，铁锹和水泥碎块始终在左侧村民区域。",
      "fix_instruction": "无需修复；若后续改动，应保持冰水杯属于胡永贵、铁锹属于村民。"
    },
    {
      "group": "第2组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "第2组延续第1组左村民右胡永贵的对话轴线，村民乙向画面中央迈出但没有无过渡换边。",
      "fix_instruction": "无需修复；若调整镜头，胡永贵仍应在画面右侧或通过明确过渡换位。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组包含村民乙质问、胡永贵诱逼和村民失控反应三个强节拍，13秒内分为4个镜头，表演空间充足。",
      "fix_instruction": "无需修复；不要再加入额外争执或新动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
