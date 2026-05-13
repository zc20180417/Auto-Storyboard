{
  "pass": true,
  "summary": "seg01已对照剧本完成审核，裁决官身份揭示、总管鞠躬和全体纠察员参见均保留，未发现硬问题。",
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
      "evidence": "原剧本中总管顺着龙万山手指认出陆凡、跑到陆凡面前九十度鞠躬并说“龙国商会总部总管，参见最高裁决官！”均在第1组0-10秒内保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "龙万山“最高裁决官？你……你竟然是全球商盟的幕后掌控者？！”约25字，分配7-13秒共6秒，情绪对白约4.2字/秒，并带瘫软反应，未超过上限。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "两组均固定在夜雨中的龙家庄园大院，组首列出陆凡、龙万山、商会总管和纠察员的位置、朝向与视线关系。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "商会总管现场开口时明确写为对陆凡恭敬说道，未出现假对白对象。",
      "fix_instruction": "若不通过，应补足真实说话对象并保持原台词。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组仅包含纠察员集体参见、声浪冲击、龙万山身份震惊三项强节拍，13秒内可表演。",
      "fix_instruction": "若不通过，应拆分群体参见与龙万山质问。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组结尾总管深鞠躬、龙万山僵住；第2组组首复述总管仍在陆凡面前深鞠躬，龙万山手臂僵硬垂下，状态连续。",
      "fix_instruction": "若不通过，应在第2组组首补足总管和龙万山的承接状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
