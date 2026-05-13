{
  "pass": true,
  "summary": "seg01已对照原剧本和竖屏生成规则完成审核，陆凡与张强冲突、林夏追问去向均保留，未发现硬问题。",
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
      "evidence": "原剧本中陆凡质问、张强承认故意整人并威胁守公墓、陆凡咬牙放狠话并推开离开，均按顺序保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "3-7秒承载林夏问句与张强回答，有效台词约24字/4秒，约6.0字/秒，低于6.5硬上限；7-13秒承载林夏怒斥约17字/6秒并包含张强语塞和林夏离开动作。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "该组只发生在民政办大厅，张强和门口林夏的可用位置在组首写明，林夏先入场后开口。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "陆凡和张强的每句现场对白均写明对对方问道或说道，没有假对白对象。",
      "fix_instruction": "若出现缺少对象的对白，应改成陆凡对张强、张强对陆凡的明确说话对象。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "林夏在开口前有推门入场动作，张强在组首已位于办公桌旁并可参与对话。",
      "fix_instruction": "若人物未可用，应在组首写明位置或在说话前安排入场动作。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组为一场双人短句冲突加离场动作，14秒内包含质问、威胁、推开离开三个主要节拍，可表演。",
      "fix_instruction": "若密度过载，应拆出离场动作或压缩非关键反应。"
    }
  ],
  "issues": [],
  "warnings": []
}
