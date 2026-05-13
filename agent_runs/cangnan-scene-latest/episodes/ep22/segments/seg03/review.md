{
  "pass": true,
  "summary": "seg03保留安保逼近、陆凡识破假账、手机发送云备份和大屏揭证据，审核通过。",
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
      "evidence": "第1组保留两名手下逼近、陆凡问周长海、吴总监命令带走、陆凡反问植入假账和吴总监铁证如山。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "陆凡组首持有手机，0-5秒说明云备份，5-8秒按下发送，8-11秒大屏亮起显示真实账目和篡改痕迹。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "陆凡约28字台词用5秒承载并含手机操作准备，吴总监约18字台词用4秒承载，均低于6.5字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首写明陆凡、吴总监和两名手下均在会议室内，手下从右后方逼近后参与动作，人物可用。",
      "fix_instruction": "若不通过，应补手下组首位置或入场动作。"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "真实账目和篡改痕迹通过大屏幕画面呈现，抽象证据信息转成可见屏幕内容。",
      "fix_instruction": "若不通过，应把证据转译成屏幕或纸面可见细节。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾陆凡仍在桌前对峙吴总监，第2组首陆凡持手机、吴总监盯着陆凡，空间和人物状态连续。",
      "fix_instruction": "若不通过，应补充陆凡取手机动作或组首状态。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "全段未出现模型说明词、模板污染或不可生成的内部提示。",
      "fix_instruction": "若不通过，应改写为自然分镜正文。"
    }
  ],
  "issues": [],
  "warnings": []
}
