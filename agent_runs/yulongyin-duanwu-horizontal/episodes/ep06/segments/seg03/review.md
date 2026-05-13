{
  "pass": true,
  "summary": "工地段保留爸爸搬钢筋、陶土挂坠发烫、陶笛声穿透机器、工友追问和爸爸奔离工地，声音来源与横向走位清楚。",
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
      "type": "script_fidelity",
      "evidence": "原剧本的夜间工地、机器轰鸣、爸爸满脸泥污搬沉重钢筋、胸口陶土挂坠发烫并闪烁微光均按顺序呈现。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "陶笛声作为穿透机器轰鸣的画外异响出现，爸爸嘴唇闭住不做口型，由胸口陶土挂坠闪烁和爸爸反应承载声音来源。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "evidence": "工友从右后方对左侧爸爸喊“燃哥，你发什么呆？”，爸爸再对工友说“是天天的笛声……村里出事了！”，现场对白对象明确。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "爸爸在左中部搬钢筋，工友在右后方忙碌，机械与施工灯沿后方横向排开，陶土挂坠在胸口形成清晰中心道具。",
      "fix_instruction": "若不通过，应补充钢筋堆、爸爸、工友、机械和通道的左右前后位置。"
    },
    {
      "group": "第2组",
      "type": "blocking_continuity",
      "result": "pass",
      "evidence": "第1组尾爸爸停在左中部钢筋堆旁，第2组首仍在同位置，随后扔钢筋、扯安全帽并向右侧通道奔跑，走位路线连续。",
      "fix_instruction": "若不通过，应补充爸爸从钢筋堆到右侧通道的转身和奔跑路径。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "15秒内依次承载陶笛声反应、工友追问、爸爸判断、扔钢筋、扯安全帽、奔跑离开，动作链按时间段拆开，未在单镜头中硬塞长对白和大动作。",
      "fix_instruction": "若不通过，应把扔钢筋、摘帽、奔跑拆成更明确的连续动作段，或删掉非剧本动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
