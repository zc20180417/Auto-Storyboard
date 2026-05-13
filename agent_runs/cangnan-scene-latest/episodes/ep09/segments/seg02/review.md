{
  "pass": true,
  "summary": "seg02大厅两组保留江若晴、林夏和律师闯入派出所并递交流向证明的关键动作与台词。",
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
      "type": "space_locking",
      "evidence": "大厅、接待台和审讯区走廊门在组首明确，江若晴、林夏、值班警员和律师均有位置与朝向。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留律师递交底层流向证明、江若晴质问资金来自嘉禾集团对公账户、值班警员去汇报和林夏推开警员走向审讯室。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "江若晴24字质问用5秒，约4.8字/秒；律师17字说明用3秒，约5.7字/秒，均在可表演范围内。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "值班警员对两人说道，林夏对值班警员说道，现场对白对象明确。",
      "fix_instruction": "若不通过，应补足每句台词的真实对话对象。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "文件袋在律师手中，随后抽出证明材料递向值班警员，值班警员接住证明，关键道具有可见过渡。",
      "fix_instruction": "若不通过，应补充文件从律师到警员的递接动作。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组包含递文件、江若晴质问、警员回应和林夏推开通道四个轻中节拍，14秒内分配清楚。",
      "fix_instruction": "若不通过，应将递交证据和闯入审讯区拆成两组。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾林夏停在警员面前，第2组首保持相同对峙位置，再由林夏推开警员进入走廊，状态连续。",
      "fix_instruction": "若不通过，应在第2组组首复述林夏和警员的对峙位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
