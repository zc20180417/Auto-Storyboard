{
  "pass": true,
  "summary": "seg04保留周建国否认青花瓷、沈清当铺监控与报警威慑、周建国跌坐、明早八点收房和扶母离开的完整收束。",
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
      "type": "script_fidelity",
      "evidence": "周建国早打碎了、沈清听说当铺换二十万、举手机要求查监控三处关键文本按原剧本顺序保留。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "第1组对白约13字/3秒、22字/3.5秒、22字/4秒，最高约6.3字/秒，低于硬上限。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "evidence": "周建国跌坐、沈清说重罪、沈清明早收房、沈清扶周桂兰离开分别拆段，归位动作没有挤入同一镜。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "博古架空位、茶几遗嘱和沈清手机三类道具状态分别锚定，手机只在6.5秒后被抬起。",
      "fix_instruction": "无。若手机提前出现或遗嘱被替换，应按时间段修正。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾沈清举亮屏手机，第2组组首继续举手机；周建国从站在茶几右侧到太师椅前双腿发软可连续承接。",
      "fix_instruction": "无。若周建国直接坐下，应在第2组0-3秒保留跌坐动作。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "偷盗古董重罪、明早八点收房、警察请出、沈清扶周桂兰离开均忠于原剧本。",
      "fix_instruction": "无。若新增报警已经发生或警察入场，应删除。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定手机、泛黄遗嘱、周建国、青花瓷、博古架和赵强，3条均为本组关键误生成风险。",
      "fix_instruction": "无。若出现泛泛词，应改成本组人物道具。"
    }
  ],
  "issues": [],
  "warnings": []
}

