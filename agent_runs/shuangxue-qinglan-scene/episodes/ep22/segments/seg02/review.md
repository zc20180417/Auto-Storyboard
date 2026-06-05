{
  "pass": true,
  "summary": "seg02 保留赵强护车、工程队长堆杂物、沈清威胁拖车和赵强服软，动作拆分清楚。",
  "checked_groups": ["第3组", "第4组", "第5组"],
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
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "赵强急跑护住新车并保留“你们清房就清房，别碰我的车！”；工程队长保留堆到院外的命令。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "沈清约31字用5秒，约6.2字/秒，赵强约9字用4秒，约2.25字/秒且含转身开车动作，未越硬上限。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "赵强的新车从第3组车头被护住，至第4组被废旧物品围住，再到第5组车门旁只剩窄缝，状态连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "急跑护车、赵强喊话、工程队长挥手下令、工人搬杂物分段呈现。",
      "fix_instruction": "若不通过，应拆开护车动作和工程队长下令。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载杂物逐步围住车身和赵强短反应，10秒有完整可见动作链。",
      "fix_instruction": "若不通过，应压缩或合并堆杂物动作。"
    },
    {
      "group": "第5组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈清对赵强说道威胁拖车，赵强对沈清喊出服软台词，对话对象明确。",
      "fix_instruction": "若不通过，应补充真实对话对象。"
    }
  ],
  "issues": [],
  "warnings": []
}
