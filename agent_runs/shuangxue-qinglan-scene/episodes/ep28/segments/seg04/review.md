{
  "pass": true,
  "summary": "seg04 拖离、关门、母女握手回家收束完整，动作拆分和组间门状态连续。",
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
      "type": "action_atomicity",
      "evidence": "掰开手指、拖向大门、带出门外、关门隔断哭喊分四段呈现，复杂拖离没有塞进单镜。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "母女三句对白分别给4秒、4秒、4秒，并有握手和扶起动作，15秒长组有足够台词和收束动作支撑。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "evidence": "第1组尾法庭大门关闭、周美娟在门外；第2组首复述大门关闭、通道里没有周美娟。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "法警强行拖出、周美娟喊沈清狠心、法庭大门关上隔绝哭喊均保留。",
      "fix_instruction": "若不通过，应补回拖出和关门隔音两个关键动作。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定周美娟、法警、沈清、周桂兰和法庭大门，防止追出或拖离失败。",
      "fix_instruction": "若不通过，应删除泛化项并补门状态锚点。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组由握手、两句情绪落地对白、扶起离开组成，15秒由台词和收束动作支撑，不是普通停顿撑时长。",
      "fix_instruction": "若不通过，应压缩为短组或拆分对白与离场动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
