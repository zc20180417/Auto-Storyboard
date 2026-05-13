{
  "pass": true,
  "summary": "seg03已审核，龙家人被控制、龙万山挣脱冲向控制台、自毁装置威胁和总管保护命令均符合剧本。",
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
      "type": "script_fidelity",
      "evidence": "纠察员控制龙家人、龙万山喊“不！我龙家百年基业，不能毁于一旦！”以及挣脱冲向控制台均按原剧本顺序呈现。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "龙万山两句威胁台词分别给5秒和6秒，约5字/秒左右；商会总管10字急喊给4秒且带上前保护动作，未超速。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "evidence": "第5组交代控制台位于画面深处右后方，第6组组首明确龙万山已在控制台前，红色自毁键位于手边，为下一段按键动作建立道具位置。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第5组把控制龙家人、龙万山一句崩溃台词和冲向控制台分成3段，13秒内动作链完整。",
      "fix_instruction": "若不通过，应拆出冲向控制台动作。"
    },
    {
      "group": "第6组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "龙万山两句威胁均明确对陆凡喊道，商会总管明确对联合纠察员喊道。",
      "fix_instruction": "若不通过，应补足每句现场对白的真实对象。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组结尾龙万山冲向控制台方向，第6组组首以龙万山位于控制台前开始，空间与动作结果连续。",
      "fix_instruction": "若不通过，应在第5组尾部或第6组组首补到达控制台的状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
