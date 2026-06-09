{
  "pass": true,
  "summary": "两组分镜忠实原剧本，台词节奏合规，空间连续性好，无硬问题。宾客对白语速偏快（5.4-5.6字/秒）属于情绪对白正常范围，作为软提示。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "宾客甲19字÷3.5秒=5.43字/秒，宾客乙14字÷2.5秒=5.6字/秒，均属情绪对白（赞叹/举杯祝酒），低于6.5字/秒硬上限，合规。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "组首空间锁定单一物理空间（龙腾酒店宴会厅），沈清手中端红酒杯、周桂兰位于画面左侧，与上一组组尾衔接一致（沈清位于画面中央、周桂兰位于画面左侧），空间连续。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "红酒杯在组首空间锁定中由沈清手中持有，0-3秒碰杯后仍在沈清手中，组尾衔接写明'沈清手中仍端红酒杯'，道具状态连续无跳变。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "宾客甲和宾客乙均为现场开口对白，写明了说话对象（'对身旁宾客赞叹说道''朗声说道'），无心声/画外音混用。",
      "fix_instruction": "无需修改，当前对白指向和口型描述正确。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "4个时间段，每段一个主动作（走动碰杯/沈清说话前半/沈清说话后半/周桂兰回应），强节拍约3个（碰杯、沈清台词、周桂兰台词），未过载。",
      "fix_instruction": "无需修改，强节拍数量和表演时间合理。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每个时间段只承载一个主动作或一个连续对话节拍：0-3秒走动碰杯，3-5秒沈清前半句，5-7.5秒沈清后半句，7.5-10秒周桂兰回应，无多主动作并列。",
      "fix_instruction": "无需修改，每个时间段只承载一个主动作。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项4条（沈清放下红酒杯、宾客挤到母女中间、周桂兰转身离开、红酒杯消失），均为本组特有剧情错误，锚定了本组人物和道具。",
      "fix_instruction": "无需修改，禁止项为本组特有且锚定正确。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾'沈清位于画面中央，周桂兰位于画面左侧'，第2组组首'沈清位于画面中央，手中端着一杯红酒，周桂兰位于画面左侧'，人物位置一致，红酒杯为新增道具由沈清端起，连续合理。",
      "fix_instruction": "无需修改，人物位置和道具衔接连续。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "宾客甲和宾客乙对白语速5.4-5.6字/秒，属情绪对白（赞叹、举杯祝酒）正常范围，但偏快，可留意是否需要微调。",
      "evidence": "宾客甲19字÷3.5秒=5.43字/秒，宾客乙14字÷2.5秒=5.6字/秒，情绪对白基准5.2字/秒。",
      "fix": "可选：将宾客甲时间段延长0.5秒至4秒（5.43→4.75字/秒），进一步降低语速。"
    }
  ]
}
