{
  "pass": true,
  "summary": "seg04分镜保留宋子昂车内拨电话、王局长电话回应、地契封山指令和挂断后的阴冷反应，电话音承载正确。",
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
      "type": "audio_mouth_sync",
      "evidence": "王局长'宋少放心，土地局我说了算'写为手机听筒电话音，宋子昂嘴唇闭合不做口型。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "宋子昂砸方向盘、拨通王局长、要求亲自出马和拿地契封黑风山均按原剧情顺序呈现。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "宋子昂约24字冷笑台词安排5秒，王局长约18字电话音安排3秒，字秒比均低于6.5。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首限定劳斯莱斯车厢单一空间，宋子昂位置、手机和王局长电话音来源明确。",
      "fix_instruction": "若不通过，应把电话对方写成画外电话音，并列明手机载体。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部宋子昂握手机命令王局长，第2组组首仍为宋子昂在驾驶位贴着手机继续通话，状态连续。",
      "fix_instruction": "若不通过，应补充手机仍在耳侧或通话已结束的过渡。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模板编号、参考官方模板、首尾帧、字幕或模型自动处理类词。",
      "fix_instruction": "若不通过，应删除污染词并改写为可见动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
