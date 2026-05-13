{
  "pass": true,
  "summary": "seg02 两组保留刀疤下令、混混冲锋、陆凡呼叫老李、钢管升起和水泵轰鸣的动作链，无硬问题。",
  "checked_groups": ["第3组", "第4组"],
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
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "老李台词来自陆凡手中对讲机，陆凡嘴唇闭合不做口型，声音来源和可见载体明确。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "陆凡对讲机台词约14字用3.5秒，老李回复约9字用3.5秒，均低于6.5字/秒硬上限。"
    },
    {
      "group": "第4组",
      "type": "timing_math",
      "evidence": "第4组时间段为0-3、3-5、5-10秒，连续且以10秒结束，普通环境交代控制在3秒内。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "刀疤喊上、混混持钢管木棍涌来、陆凡取对讲机、老李回复水阀打开均按原剧本顺序呈现。",
      "fix_instruction": "若不通过，应恢复冲锋、呼叫、回复的原顺序。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首只锁定道路、树林、陆凡、刀疤、混混和埋设钢管的位置，未把升起动作写成组首状态推进。",
      "fix_instruction": "若不通过，应把过程动作移入时间段描述。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载钢管升起、刀疤短句反应和水泵启动三个节拍，10秒内表演空间充足。",
      "fix_instruction": "若不通过，应拆分钢管升起和水泵启动，或压缩非关键反应。"
    }
  ],
  "issues": [],
  "warnings": []
}
