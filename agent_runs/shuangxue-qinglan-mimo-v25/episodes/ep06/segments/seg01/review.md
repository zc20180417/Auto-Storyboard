{
  "pass": true,
  "summary": "两组均在周家正屋客厅，台词全部忠实保留，对话指向明确，时长与字秒比合格。",
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
      "type": "dialogue_pacing",
      "evidence": "沈清厉声质问13字/2.5秒=5.2字/秒(情绪对白)；赵强装傻13字/3秒=4.33字/秒(普通对白≥3.8)；沈清逼问23字/4.5秒=5.11字/秒(情绪对白≥4.5)。全部在6.5硬上限内。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "单一物理空间周家正屋客厅，组首锁定沈清位于画面左/赵强位于画面右持有手机，与第一个时间段起点一致。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "刘美娟'疑心病'、周建国'家用'、沈清'个人生活费不是扶贫'三句台词全部原文保留，说话对象和顺序与原剧本一致。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词均为画面内真人现场开口对白，每句写明'A对B说道'，无心声/画外音混用。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "刘美娟冲入(2秒)+刘美娟对白(4.5秒)+周建国起身+对白(3秒)+沈清回击(4.5秒)=14秒，四个时间段各承载一个主动作或一个对话节拍，属于同一冲突事件链的阶段推进。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾赵强后退半步、沈清紧盯；第2组组首刘美娟从侧面冲入、周建国坐在椅子上，同空间人物站位自然衔接。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "video_negative_constraints",
      "problem": "刘美娟冲入+周建国起身打断+沈清回击属于多人物调度组，建议补充2-3条视频禁止项如'刘美娟提前出现'、'周建国没有站起来'、'沈清后退'。",
      "evidence": "第2组缺少视频禁止项行。",
      "fix": "在组尾衔接后补一行视频禁止项。"
    }
  ]
}
