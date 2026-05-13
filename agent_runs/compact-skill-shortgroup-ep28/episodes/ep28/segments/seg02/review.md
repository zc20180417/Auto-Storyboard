{
  "pass": true,
  "summary": "seg02 审核通过。第3组作为 6 秒必要短组保留完整“昨晚已经被双规了，带走！”台词，没有为了时长压缩原文。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组"],
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
      "evidence": "李少爷台词“那臭娘们破产没有？”和保镖台词“货全压在仓库了，不出三天准垮。”完整保留，病房门被推开作为后续干警入场动作写在时间段内。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "第3组总时长 6 秒，0-3秒承载“你父亲昨晚已经被双规了，带走！”，约 15 个有效字，字秒比约 5.0，低于 6.5 硬上限。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "第4组组首写“李少爷已在病房门口，被两名干警一左一右架住”，这是第一帧已成立状态；走到走廊中央的过程放入 0-3 秒镜头。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组是独立逮捕/带走命令短节拍，若强行并入第2组会把涉嫌洗钱、反驳、父亲双规和控制动作压进 15 秒，容易过载或删台词；6 秒短组必要。",
      "fix_instruction": "若不通过，应恢复为 4-9 秒必要短组，或拆到相邻独立短组，不能压缩原台词。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "原剧本“你父亲昨晚已经被双规了，带走！”在分镜中逐字保留，没有删掉“昨晚”或“带走”。",
      "fix_instruction": "若不通过，应恢复被删改台词，并按短组承载。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组组尾两名干警控制住李少爷，第4组组首李少爷已在病房门口被两名干警架住，状态衔接自然；从门口移动到走廊中央写在时间段内。",
      "fix_instruction": "若不通过，应在上一组组尾和下一组组首补齐人物位置、控制状态和门状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
