{
  "pass": true,
  "summary": "seg03两组保留包厢内宋子昂挑衅、江若晴维护陆凡、陆凡反击和拍桌收尾，时长与口型承载合格。",
  "checked_groups": ["第5组", "第6组"],
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
      "group": "第5组",
      "type": "format",
      "evidence": "标题含EP08-G05，15秒5个时间段，时间轴0-2.5-5-9-12-15连续并以第5组结束标记收束。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "江若晴主位、宋子昂摇红酒杯、宋子昂嘲笑陆凡要不到沙石、陆凡喝茶回应和宋子昂投资建材的台词均保留。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "宋子昂“若晴，让他滚出清河乡，我就批条子”约17字用4秒，陆凡“你的条子，一文不值”约9字用3.5秒，节奏自然。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "包厢、圆桌、茶杯、红酒杯和三人左右/中央站位明确，单一物理空间成立。",
      "fix_instruction": "若失败，应补足空间、人物朝向和道具位置。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "红酒杯从第5组宋子昂手边延续到第6组手中和桌面晃动，茶杯从陆凡面前被放回桌面，归属清楚。",
      "fix_instruction": "若失败，应补充放下、拿起或杯子位置变化。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "江若晴制止、宋子昂提条件、陆凡反击、宋子昂拍桌四个节拍在15秒内分配清楚，没有额外强动作。",
      "fix_instruction": "若失败，应拆组或压缩非关键反应。"
    }
  ],
  "issues": [],
  "warnings": []
}
