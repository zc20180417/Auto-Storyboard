{
  "pass": true,
  "summary": "seg03 两组保留观景台直播、推介会造势、官方大号连麦和徐厅长出现在大屏幕的推进。",
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
      "type": "filmability",
      "evidence": "直播间热度和弹幕通过后台设备屏幕、提示音和周思思反应呈现，可见可听。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "江若晴约15字疑问用3秒，约5字/秒；陆凡约16字回应用4秒，约4字/秒，均可自然表演。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "evidence": "保留热度突破五百万、官方大号请求连麦、陆凡要求接通并切到大屏幕、徐厅长出现。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定观景台一个主要物理空间，三人位置、朝向、直播设备和大屏幕均明确。",
      "fix_instruction": "若不通过，应补齐人物画面位置或设备布局。"
    },
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "徐厅长只作为大屏幕画面出现，未让现场人物承担他的口型。",
      "fix_instruction": "若不通过，应明确屏幕画面和现场人物闭口反应。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾周思思被后台动静吸引，第6组首她站在后台设备旁继续查看提示，状态连续。",
      "fix_instruction": "若不通过，应在第6组组首复述后台设备和周思思视线状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
