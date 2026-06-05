{
  "pass": true,
  "summary": "seg03 将大门打开、讨债人员入场、张总喊话、五百万追债、宾客避让和周建国跪地分阶段承载，外部事件没有过载。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第5组",
      "type": "action_atomicity",
      "evidence": "开门、讨债人员入场、张总喊话、周建国回应分为四段，没有把外部事件塞入同一时间段。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "张总约48字追债台词使用8秒承载，约6.0字/秒，低于6.5硬上限。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "evidence": "连本带利五百万、法院强制执行令、宾客避让、周建国扑通跪地均保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "张总和周建国均为画面内真人开口，分别明确对周建国、张总说道。",
      "fix_instruction": "若不通过，应明确喊话对象或改成门外音来源。"
    },
    {
      "group": "第5组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "张总先在0-6秒入场，之后才在6-10秒喊话，人物可用性成立。",
      "fix_instruction": "若不通过，应把张总预置在门后或先写入场。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾部大门打开、张总站门口、周建国在宾客桌旁，第6组组首直接复述这些状态。",
      "fix_instruction": "若不通过，应补充大门、张总和周建国位置。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第6组为张总追债长台词、宾客避让、周建国跪地三段连续事件链，13秒内动作顺序清楚。",
      "fix_instruction": "若不通过，应把跪地动作拆到下一组或压缩宾客反应。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "高利贷借条仍在大屏幕，门保持打开，未出现关键道具无过渡转移。",
      "fix_instruction": "若不通过，应补门状态或屏幕画面状态。"
    },
    {
      "group": "第6组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第6组禁止项锚定宾客空道、周建国、张总和讨债人员，数量4条，符合复杂多人物调度风险。",
      "fix_instruction": "若不通过，应删掉无锚点通用词或矛盾禁止项。"
    }
  ],
  "issues": [],
  "warnings": []
}
