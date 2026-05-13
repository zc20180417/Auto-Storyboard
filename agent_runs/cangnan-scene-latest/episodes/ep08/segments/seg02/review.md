{
  "pass": true,
  "summary": "seg02两组完整保留天价卖沙、陆凡警告、徐虎嘲讽和陆凡离开的冲突推进，审核未发现硬问题。",
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
    "filmability": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第3组",
      "type": "generation_density",
      "evidence": "本组负载为徐虎站起和手下围拢、天价报价、陆凡反驳、徐虎逼近四个强节拍，15秒内分段清楚。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "陆凡“不卖是吧？后果自负”、徐虎“这全县的矿都是我包的”、陆凡转身离开和徐虎吐痰嘲讽均保留。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "徐虎“吓唬我？这全县的矿都是我包的！”约16字用4秒，陆凡短句用3秒，徐虎尾句约15字用3秒，均在硬上限内。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "徐虎和陆凡的每句现场对白都明确写为对对方说道，未出现假对白对象。",
      "fix_instruction": "若失败，应补成A对B说道格式。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾部徐虎逼近、手下围门，第4组首部延续同一办公室、打开的大门和双方站位。",
      "fix_instruction": "若失败，应补充门、手下围拢和陆凡位置的连续状态。"
    },
    {
      "group": "第4组",
      "type": "filmability",
      "result": "pass",
      "evidence": "徐虎吐痰、陆凡离开、手下让开等都是可见动作，未用抽象判断替代关键画面。",
      "fix_instruction": "若失败，应将抽象情绪改为可见动作和表情。"
    }
  ],
  "issues": [],
  "warnings": []
}
