{
  "pass": true,
  "summary": "seg04保留沈清点破两元提醒、周美娟崩溃拒拍、赵强暴怒抢录像手机的升级动作，无硬问题。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "第5组保留沈清“到账两元的提醒”、周美娟“你滚开！别拍我！”和赵强“你别太过分了！”。"
    },
    {
      "group": "第6组",
      "type": "action_atomicity",
      "evidence": "赵强冲上、吼叫、伸手抓旧手机分为0-3秒、3-6秒、6-9秒，未塞进同一时间段。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "evidence": "沈清旧手机始终在沈清手中，赵强目标是抢旧手机；周美娟自己的手机由她抱着躲到赵强身后。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "沈清约16字用3秒，周美娟约8字和赵强约7字共用4秒的连续升级节拍，均可自然承载。",
      "fix_instruction": "无须修复；不要把第5组扩成长停顿。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第6组只处理赵强冲前抢录像手机这一连续动作链，11秒内分阶段展示，周美娟和周桂兰只做站位反应。",
      "fix_instruction": "无须修复；不得让周美娟或周桂兰抢主动作。"
    },
    {
      "group": "第6组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定赵强、周美娟、沈清旧手机、周桂兰，防止抢错手机或非主动作人物抢动作。",
      "fix_instruction": "无须修复；保持禁止项不超过5条且不使用泛泛词。"
    }
  ],
  "issues": [],
  "warnings": []
}
