{
  "pass": true,
  "summary": "seg03保留排爆解除定时器、确认安全、陆凡固定证据和民警收队，时间与声音来源合格。",
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
      "evidence": "排爆手穿防爆服进入并用专业工具拆除引线，随后通过对讲机说“定时器已解除，安全。”"
    },
    {
      "group": "第6组",
      "type": "dialogue_direction",
      "evidence": "陆凡对民警说“嫌疑人口供已录，证据固定。”，民警对陆凡回应“收队。”，对象明确。"
    },
    {
      "group": "第5组",
      "type": "timing_math",
      "evidence": "第5组时间段为0-4、4-9、9-12秒，合计12秒，与标题总时长和3个镜头一致。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "12秒内拆成冲入操作、剪断引线、对讲确认三段，排爆动作有5秒特写承载。",
      "fix_instruction": "若不通过，应延长拆线动作或拆分确认安全，避免排爆过程过快。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "第5组尾定时器解除，第6组首定时器已停止并在控制台旁，拆下引线放入证据袋有可见过渡。",
      "fix_instruction": "若不通过，应明确定时器停止状态和引线入袋动作。"
    },
    {
      "group": "第6组",
      "type": "filmability",
      "result": "pass",
      "evidence": "证据固定通过执法记录仪保存、证据袋和对话呈现，抽象办案结论转成可见动作。",
      "fix_instruction": "若不通过，应增加执法记录仪、证据袋或可见记录动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
