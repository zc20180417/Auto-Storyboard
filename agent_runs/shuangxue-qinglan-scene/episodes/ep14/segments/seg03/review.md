{
  "pass": true,
  "summary": "seg03 真实保留周美娟想溜、沈清拦路、赵强抗议、沈清输入转账信息和OS闭口承载。",
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
      "type": "action_atomicity",
      "evidence": "周美娟转身、沈清上前挡路、双方短句交锋分段呈现，没有把拦路和手机输入塞入同一时间段。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "沈清OS写为心声，9-11秒明确沈清嘴唇闭合、视线落在手机屏幕上，不做现场口型。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "沈清的手机和旧银行卡在组首、6-9秒输入、组尾均由沈清持有，未转移给周美娟或赵强。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "原剧本的“站住！心虚什么？”“谁心虚了！我困了！”和“既然你清白，就让它响一次。”按顺序保留。",
      "fix_instruction": "若后续修稿，不要新增推搡、打人或逃出客厅等原剧本没有的强动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "0-6秒两句现场对白约24字/6秒，6-11秒输入动作和短心声有足够承载时间。",
      "fix_instruction": "若压缩时长，应优先保留赵强抗议、沈清一分钟和OS三处信息。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定周美娟、沈清、旧银行卡，避免误生成离场、推倒和道具消失。",
      "fix_instruction": "若改写禁止项，应继续聚焦本组拦路和旧银行卡归属。"
    }
  ],
  "issues": [],
  "warnings": []
}
