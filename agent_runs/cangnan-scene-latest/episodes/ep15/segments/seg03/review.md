{
  "pass": true,
  "summary": "seg03保留发动机开箱、抢修命令、江若晴追问、捕鼠夹回应和仓库推土机揭示，分组避免空间过载。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "evidence": "集装箱打开露出防爆级核心发动机，陆凡对工人们喊“抢修组！三小时内完成换装！”，工头回应“是！保证完成任务！”均保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "0-3秒江若晴约14字问句，3-7秒陆凡约16字回应，均未超过6.5字/秒，且有明确对视和表情承载。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "第3组切到车场边废弃仓库门口，组首重新锁定陆凡、江若晴、铁门状态，没有把仓库揭示硬塞进上一组空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾部陆凡走到废弃仓库铁门前，第3组组首即从铁门关闭、陆凡背对镜头面向铁门开始，状态连续。",
      "fix_instruction": "若不通过，应补充陆凡从车场到仓库门口的过渡动作。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组包含拉门、展示五台推土机、陆凡拍履带说台词、江若晴反应，13秒内按四个清楚节拍展开。",
      "fix_instruction": "若不通过，应拆出仓库开门或推土机揭示。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "铁门组首关闭，0-3秒陆凡拉开，3秒后仓库和推土机可见，履带在6-10秒可被陆凡拍到，道具状态有过渡。",
      "fix_instruction": "若不通过，应补充铁门打开和履带可触及的过程。"
    }
  ],
  "issues": [],
  "warnings": []
}
