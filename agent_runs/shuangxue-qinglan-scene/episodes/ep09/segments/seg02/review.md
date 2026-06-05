{
  "pass": true,
  "summary": "seg02 保留了沈清逐笔念出月份金额、赵强冒汗、承认进账后狡辩周转以及沈清追问欠条利息和还款的连续逼问，没有 hard issue。",
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
      "evidence": "沈清列举去年三月八千、五月八千、过年一万约24字给4秒，字秒比约6.0；后续质问约14字给3.5秒，节奏可承载。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本的沈清拿起流水单居高临下、逐笔报金额、赵强冒汗闪躲、沈清逼问日期金额分毫不差均被保留。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "evidence": "第2组为两人连续短句攻防，15秒内分为赵强承认周转、沈清追问、赵强狡辩、沈清反击四个清楚节拍，没有并列外部事件或动作过载。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "本段全部发生在周家正屋客厅，组首列出沈清、赵强、茶几、流水单和茶杯状态，没有跨物理空间。",
      "fix_instruction": "若出现其他地点，应拆组或明确屏幕画面、回忆等例外。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "赵强、沈清的每句现场对白均明确写成对对方说道，没有假对象或口型来源错误。",
      "fix_instruction": "若缺少对象，应补为赵强对沈清说道或沈清对赵强说道。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "流水单在茶几上从第1组延续到第2组，沈清压住并点在流水单上质问，赵强茶杯仍在手中或膝前，转移可见。",
      "fix_instruction": "若道具跳变，应补放下、压住或握持的可见过渡。"
    }
  ],
  "issues": [],
  "warnings": []
}
