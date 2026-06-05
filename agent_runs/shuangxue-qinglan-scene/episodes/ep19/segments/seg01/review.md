{
  "pass": true,
  "summary": "seg01保留到账确认、删视频诉求、利息和精神损失费追问，空间与道具连续，未发现hard issue。",
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
      "evidence": "原剧本中的绿色对号、十九万二到账、赵强要求删视频和沈清反问本金未完均按顺序保留。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "赵强台词约15字用3秒，约5字/秒；沈清反问约17字用3.5秒，约4.9字/秒，未超过6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "组首锁定同一周家正屋客厅，沈清、赵强、周美娟和杂物间门位置明确，第二段指向杂物间没有跨空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "三句对白均为画面内真人开口，并写明沈清对赵强、赵强对沈清的真实对象。",
      "fix_instruction": "若不通过，应补足真实对白对象或改为明确声音来源。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载周美娟短句反应和沈清连续追责两句，同一冲突目标下连续推进，10秒容量足够。",
      "fix_instruction": "若不通过，应拆出精神损失费追问或压缩非关键逼近动作。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定沈清、杂物间门、赵强，均为本组可能影响剧情的具体错误，没有使用占位模板。",
      "fix_instruction": "若不通过，应删除泛化禁止词并改为本组人物或道具锚点。"
    }
  ],
  "issues": [],
  "warnings": []
}
