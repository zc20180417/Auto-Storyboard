{
  "pass": true,
  "summary": "seg02 三组已逐项审查清水救援、小龙饮水、黑水伤害和水壶避难动作，横屏调度与原剧本一致。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组"
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
      "type": "dialogue_pacing",
      "evidence": "天天“你还在吗？我带水来了！干净的水！”约15个有效字对应3秒，约5.0字/秒；“你……你像水做的一样。太神奇了。”约14个有效字对应3.5秒，约4.0字/秒。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "水壶始终由天天在画面左侧控制，清水滴向裂缝；黑水滩固定在小龙尾巴右后方，误碰、惨叫和尾尖变灰的因果清楚。"
    },
    {
      "group": "第3组",
      "type": "horizontal_composition",
      "evidence": "天天位于画面左侧，水壶横在画面中央，壶口朝向右下裂缝，小龙从右下方朝壶口移动，避开右后方黑水滩。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "跑回裂缝、拧开水壶、呼喊、滴水、青蓝光恢复、小龙探头和天天惊喜台词均按原剧本顺序呈现。",
      "fix_instruction": "若不通过，应按原剧本顺序补回漏掉的水滴、亮光或小龙探头动作。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载饮水恢复、误碰黑水、尾尖变灰和天天警告三个强节拍，14秒内表演空间充足。",
      "fix_instruction": "若不通过，应拆出黑水伤害或压缩非关键反应。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "天天明确对小龙喊“快！爬进水壶里！里面安全！”，说话对象和画面中的小龙位置一致。",
      "fix_instruction": "若不通过，应补明天天对小龙说话，不能写成无对象呼喊。"
    }
  ],
  "issues": [],
  "warnings": []
}
