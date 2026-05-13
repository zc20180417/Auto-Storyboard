{
  "pass": true,
  "summary": "seg02保留打手乙网兜逼近、云宝水针反击、打手丙持刀劈下的连续危机，横屏空间和道具归属清楚。",
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
      "type": "character_availability",
      "evidence": "天天、云宝、打手乙、打手丙均在组首空间锁定中可见，天天无力起身解释其不参与后续阻挡。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "黑色网兜在第3组由打手乙拿出，第4组打手乙中针后网兜晃到左下；开山刀始终由打手丙从左后方持有并举起。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "打手乙13字哀嚎用3.5秒并包含倒地动作，约3.7字/秒，属于痛叫慢节拍；打手丙18字怒吼用3秒，约6字/秒，处于可接受风险范围内。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留天天蜷缩、打手乙拿黑色金属网兜、台词“胡总说这发光的东西值大钱，千万别弄死了！”以及云宝猛地睁眼低啸。",
      "fix_instruction": "若不通过，应恢复遗漏的网兜动作或胡总台词。"
    },
    {
      "group": "第4组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "云宝固定在右前景，打手乙在左中景被水针击中，打手丙从左后方到中央劈向右前景，攻击方向连续。",
      "fix_instruction": "若不通过，应补充打手丙从左后方进入中央的走位。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "云宝低啸写为无声低啸，真人对白分别由打手乙对打手丙、打手丙对云宝承载，声音来源明确。",
      "fix_instruction": "若不通过，应区分云宝无声反应和真人口型台词。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第4组",
      "rule": "dialogue_pacing",
      "problem": "打手丙怒吼台词节奏偏快但未超过硬错误阈值。",
      "evidence": "18字约3秒，约6字/秒，符合5.8-6.5字/秒风险区间。",
      "fix": "演员可用急促怒吼完成，保持现状即可。"
    }
  ]
}
