{
  "pass": true,
  "summary": "seg02分镜保留刀疤男命令开枪、打手举枪、云宝化作十丈真水龙、龙尾横扫并撞墙倒地的动作链。",
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
      "type": "dialogue_direction",
      "evidence": "刀疤男明确对身后的打手们喊“怪物！开枪！全给我开枪！”，说话对象和现场反应均可见。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "云宝暴涨为十丈真水龙、龙尾横扫、刀疤男和打手们倒飞撞岩壁吐血，均对应原剧本关键动作。"
    },
    {
      "group": "第2组",
      "type": "horizontal_composition",
      "evidence": "真水龙占据画面中央到右侧，敌群在左侧和后景成弧线，龙尾从右向左横扫，宽幅调度明确。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "台词约13字放在3.5秒惊恐喊话段内，配合后退和指向云宝，约3.7字/秒且有情绪动作支撑。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "14秒分成显形、蓄势、横扫、撞墙四段，动作连续但没有叠加台词或额外剧情。"
      ,"fix_instruction": "无需修复。"
    },
    {
      "group": "第1组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "刀疤男和打手保持左侧，云宝从右上方进入中央，第2组继续由右向左横扫，轴线稳定。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
