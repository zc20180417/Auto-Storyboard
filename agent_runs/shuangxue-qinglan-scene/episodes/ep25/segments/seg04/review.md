{
  "pass": true,
  "summary": "seg04 保留周建国抓周美娟裙角、周美娟撇清、张总揪出周建国、周建国把债推给沈清和张总问替父还债，动作拆段清楚。",
  "checked_groups": ["第7组", "第8组"],
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
      "group": "第7组",
      "type": "action_atomicity",
      "evidence": "周建国抓裙角、周美娟尖叫、张总揪衣领、张总讽刺分成四段，每段一个主动作或主对白。"
    },
    {
      "group": "第8组",
      "type": "dialogue_pacing",
      "evidence": "周建国两段求债台词分别用4.5秒和4秒承载，张总短问用3秒承载，均低于6.5字/秒。"
    },
    {
      "group": "第8组",
      "type": "script_fidelity",
      "evidence": "周建国指沈清说她有钱、找她要，张总转头问沈老板替父还债，原台词和对象保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "周美娟裙角和金镯子在组首、动作和张总台词中连续出现，支撑抓裙角和穿金戴银的信息。",
      "fix_instruction": "若不通过，应补充裙角归属或金镯子位置。"
    },
    {
      "group": "第7组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "抓裙角、撇清、揪衣领、讽刺属于同一连续追债事件链，14秒内分段承载。",
      "fix_instruction": "若不通过，应把张总揪出周建国拆为独立组。"
    },
    {
      "group": "第8组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第7组尾部张总抓周建国衣领、周美娟退到桌旁，第8组组首直接继承。",
      "fix_instruction": "若不通过，应在第7组尾或第8组首补张总手和周美娟位置。"
    },
    {
      "group": "第8组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "周建国两句均明确对张总说道，张总最后明确对沈清说道，没有假对象。",
      "fix_instruction": "若不通过，应改明真实对话对象。"
    },
    {
      "group": "第8组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首列出张总、周建国、沈清、周美娟、讨债人员和宾客在宴会厅内的站位与朝向。",
      "fix_instruction": "若不通过，应补充人物画面位置和身体朝向。"
    },
    {
      "group": "第8组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第8组禁止项锚定张总、沈清、周建国和周美娟，避免还债关系被错误生成。",
      "fix_instruction": "若不通过，应删除泛泛项并补本组剧情错误风险。"
    }
  ],
  "issues": [],
  "warnings": []
}
