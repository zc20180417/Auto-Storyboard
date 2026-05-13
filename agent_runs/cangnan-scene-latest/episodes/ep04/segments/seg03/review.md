{
  "pass": true,
  "summary": "seg03保留张强被押、向赵大江求救、赵大江掌掴撇清并试探陆凡的走廊对峙，审核通过。",
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
      "evidence": "张强被戴手铐押解、赵大江夹公文包迎面走来、张强求救、赵大江扬手掌掴和怒斥均按原剧本顺序呈现。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "赵大江“胡说八道！党纪国法面前，谁也救不了你！”约21字承载在8.5-14秒并包含掌掴动作，整体约3.8字/秒，动作支撑成立。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "组首锁定张强右侧捂脸且双手仍受手铐限制、赵大江中央、陆凡左后方，三人可用性完整。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "赵大江在组首已位于走廊远端背景中央，之后迎面走来和掌掴均有可见来源。",
      "fix_instruction": "若不通过，应在赵大江说话前补入场或组首位置。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "张强对赵大江、赵大江对纪委干部和陆凡、陆凡对赵大江的说话对象均明确。",
      "fix_instruction": "若不通过，应逐句补明对话对象。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾张强被打偏脸，第2组首张强捂脸并仍被手铐限制，状态连续。",
      "fix_instruction": "若不通过，应补张强捂脸和手铐状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
