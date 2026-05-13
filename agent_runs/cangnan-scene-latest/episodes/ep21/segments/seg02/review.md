{
  "pass": true,
  "summary": "seg02已审核，警车包围、宋天明求援、高局长下令抓捕和查封宋家黑产洗钱链均忠实呈现。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "第1组保持在包厢内，通过窗外警灯和警笛声呈现外部警车包围，没有切到第二现实空间。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "宋天明向高局长指控陆凡、高局长无视并命令全部拿下、警察控制宋天明和黑衣人、高局长说明商会总部证据，均与原剧本一致。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组0-4秒台词23字，约5.8字/秒；11.5-15秒高局长宣告约22字，3.5秒约6.3字/秒，低于硬上限但节奏偏快。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "警笛声明确来自窗外，画面有警灯扫过玻璃和人物转头反应，不由画面人物错误开口承载。",
      "fix_instruction": "若不通过，应补声音来源和人物听见后的可见反应。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "高局长和警察在第1组后半段入场，第2组组首已明确位于包厢内后再行动和说话。",
      "fix_instruction": "若不通过，应在人物行动前补入场或组首位置。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组虽有抓捕动作，但按指控、命令、控制、挣扎、宣告五段推进，每段时间连续且动作可表演。",
      "fix_instruction": "若不通过，应拆出查封宣告或延长抓捕动作链。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "dialogue_pacing",
      "problem": "12-15秒高局长宣告台词信息密度偏高。",
      "evidence": "有效字数约22字，3.5秒约6.3字/秒，低于硬上限但接近警示区间。",
      "fix": "整集组装时如需更稳，可给该句增加0.5秒，并从抓捕动作或挣扎镜头中回收时长。"
    }
  ]
}
