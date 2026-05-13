{
  "pass": true,
  "summary": "第3-4组把祠堂内大鼓裂开、爸爸倒下、水龙收缩、云宝失光和爷爷台词拆开承载，空间与道具连续，无硬问题。",
  "checked_groups": [
    "第3组",
    "第4组"
  ],
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "野牛大鼓沉闷回音并裂开、老木鼓槌断成两截、爸爸双眼一黑仰面倒下、天天惊呼“爸爸！”均被保留。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "第3组尾水壶留在天天左前景，第4组首水壶在天天手边，水龙虚影收缩并变成壶底的云宝，关键道具位置连续。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "爷爷台词“燃燃，你救了全村的命啊！”放在6.5-10秒的3.5秒镜头内，约11字，情绪哽咽但未超过6.5字/秒硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组以爸爸倒在鼓前、天天手碰到肩膀、水壶留在左前景收尾，第4组从同一位置承接天天抱住爸爸和水壶内变化。",
      "fix_instruction": "若不通过，应在第3组尾或第4组首补足爸爸、水壶和天天的相对位置。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "天天抱住爸爸、水龙虚影迅速收缩、云宝变回巴掌大沉在壶底失去光泽、爷爷老泪纵横说原台词，未新增剧情。",
      "fix_instruction": "若不通过，应恢复原动作顺序并删除额外剧情动作。"
    },
    {
      "group": "第3组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "大鼓在中央，爸爸偏右，天天左前景，爷爷右后方，横屏左右和前后层次清楚。",
      "fix_instruction": "若不通过，应明确三人和大鼓、水壶在横屏里的左右前后位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
