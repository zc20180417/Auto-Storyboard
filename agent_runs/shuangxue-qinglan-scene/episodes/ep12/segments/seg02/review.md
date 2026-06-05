{
  "pass": true,
  "summary": "seg02保留周桂兰痛哭、周建国家用狡辩和沈清赡养费反击，短组理由成立且无硬问题。",
  "checked_groups": ["第4组", "第5组", "第6组"],
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
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "周桂兰约18字用4.5秒，约4字/秒；周建国两句分别约23字/4秒、16字/3.5秒，均低于6.5字/秒。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "保留金镯子、新车、杂物间吃剩饭三个指控，没有把金镯子或新车改成客厅实物出场。"
    },
    {
      "group": "第6组",
      "type": "format",
      "evidence": "第6组标题含EP12-G06，9秒短组属于两句短促对峙，时间轴0-4、4-9连续，镜头数2个一致。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "周建国前倾吼人和拍桌吼第二句拆成两个时间段，茶几震动可执行。",
      "fix_instruction": "若失败，应把拍桌和长台词拆开或延长。"
    },
    {
      "group": "第5组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "两句沈清台词均明确对周建国怒斥或说道，未使用假对象。",
      "fix_instruction": "若失败，应补足沈清对周建国的对白指向。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第6组只有周建国一句权威狡辩和沈清一句反击，9秒短促交锋没有硬凑到10秒。",
      "fix_instruction": "若失败，应保留短组而不是添加停顿。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾部周建国压茶几、周桂兰痛哭；第5组组首继续复述周建国压茶几和沈清护在周桂兰前。",
      "fix_instruction": "若失败，应在第4组尾或第5组组首补具体站位。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "授权委托书持续留在茶几中央，拍桌只让纸角震起，没有丢失关键证据。",
      "fix_instruction": "若失败，应补充纸张位置或删除飞走动作。"
    },
    {
      "group": "第6组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定周建国、周桂兰、沈清和授权委托书，都是本组可能误生成的具体错误。",
      "fix_instruction": "若失败，应改成带本组人物和道具锚点的2-5条风险。"
    }
  ],
  "issues": [],
  "warnings": []
}
