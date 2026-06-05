{
  "pass": true,
  "summary": "seg01保留医院复查结论、康复安排和母女承诺，时间轴、对白指向和道具连续性均可执行。",
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
      "evidence": "专家医生两句诊断和进口药台词、沈清关于康复理疗设备的回应均按原剧本顺序保留。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "专家医生第一句约18字用3.5秒，第二句约23字用4秒，沈清约20字用3.5秒，均低于6.5字/秒硬上限。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "evidence": "第1组尾部X光片和病历夹停在桌面，第2组组首继续复述诊疗桌和三人位置，复查室状态连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "全组只发生在市立医院复查室，组首列出专家医生、沈清、周桂兰位置和X光片状态。",
      "fix_instruction": "如不通过，应补足人物朝向或拆出跨空间内容。"
    },
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "X光片从专家医生手中到病历夹旁有可见放下动作，组尾继续锚定在桌面。",
      "fix_instruction": "如不通过，应补充X光片放置位置或归属变化。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "周桂兰对沈清说道、沈清对周桂兰说道，现场对白对象明确，没有假对象。",
      "fix_instruction": "如不通过，应逐句补清说话对象。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组只承载周桂兰感受、沈清承诺和轻微手部安抚，10秒内没有外部事件或复杂动作过载。",
      "fix_instruction": "如不通过，应压缩轻反应或拆分动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
