{
  "pass": true,
  "summary": "seg01 保留赵强扑抢、沈清绊倒、果盘翻倒、周美娟删短信威胁和沈清喝止，两个短动作组密度可执行。",
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
      "type": "script_fidelity",
      "evidence": "第1组逐步保留赵强猛扑、沈清侧身一闪并伸脚一绊、赵强惊呼和下巴磕茶几角，没有新增改变剧情的动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "周美娟“我现在就把短信删了！看你怎么查！”校验有效字数14字给2.5秒约5.6字/秒，沈清7字给1.5秒约4.7字/秒。"
    },
    {
      "group": "第1组",
      "type": "prop_continuity",
      "evidence": "录像手机一直在沈清右手，果盘从茶几摆放到被撞歪，组尾明确赵强倒地和果盘状态，能接第2组苹果滚落。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "赵强扑抢、沈清闪避绊脚、赵强失衡惊呼、摔到茶几角分成四段，每段只有一个主动作。",
      "fix_instruction": "若不通过，应继续拆分扑抢和摔倒动作。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾赵强倒在茶几旁、果盘被撞歪；第2组组首继承赵强倒地、果盘倾翻和沈清手握录像手机。",
      "fix_instruction": "若不通过，应在第2组组首补齐赵强和果盘状态。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "周美娟对赵强尖叫、周美娟对沈清威胁、沈清对周美娟喝止均有真实画面对象。",
      "fix_instruction": "若不通过，应补明每句台词的对话对象。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第2组禁止项锚定周美娟的手机、转账短信、沈清的录像手机和赵强，没有使用占位泛词。",
      "fix_instruction": "若不通过，应替换为本组人物和手机状态相关的具体禁项。"
    }
  ],
  "issues": [],
  "warnings": []
}
