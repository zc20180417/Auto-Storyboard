{
  "pass": true,
  "summary": "seg02保留疯狗拖拽、宋少任务信息、陆凡驾车赶到和双方转向对峙的完整因果。",
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
      "type": "dialogue_pacing",
      "evidence": "江若晴8字挣扎台词分配2秒，疯狗16字冷笑台词分配4秒，字秒比均在可接受范围内。"
    },
    {
      "group": "第4组",
      "type": "character_availability",
      "evidence": "陆凡在组首锁定为越野车驾驶位内，先有车辆急停和踹门入场，再开口暴喝。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "远光灯撕裂雨幕、黑色越野车急刹、陆凡喊“找死！”、疯狗丢开江若晴并说“猎物终于来了！”均保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "破碎车窗承接上一段，疯狗持铁棒和抓衣服的动作均有可见来源。",
      "fix_instruction": "若不通过，应补写破碎车窗状态和疯狗手中铁棒归属。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组拆为远光、急刹、陆凡入场、疯狗转向四个节拍，总时长10秒，没有把拖拽对白塞入同组。",
      "fix_instruction": "若不通过，应把车辆到场和双方对白继续拆开。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾部江若晴在车外被抓；第4组组首复述她在保时捷外侧被疯狗拉住，并让陆凡从远处车内入场。",
      "fix_instruction": "若不通过，应在组首补江若晴车外位置和疯狗拉住她的状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
