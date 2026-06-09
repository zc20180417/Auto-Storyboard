{
  "pass": true,
  "summary": "seg02审核通过，2组台词节奏和空间锁定无硬伤。",
  "checked_groups": ["第4组", "第5组"],
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
      "evidence": "刘美娟'肯定是老太太自己取钱花了，忘了'14字÷5.2=2.7秒分配3秒；沈清'取钱？一分钟内拿老年机网银转账？'14字÷5.2=2.7秒分配4秒；'她连拼音都不会打，怎么转的账'13字÷5.2=2.5秒分配3秒。字秒比均在4.3-4.7，合格。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "组首空间锁定列出沈清举老年机和账单在画面左侧、刘美娟在画面右侧、柜员在柜台后方，柜员抬头插话的空间关系清楚。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "原剧本'那……那可能是去ATM机取的''并不是取现，系统显示全是通过手机银行转账的''我……我不知道，反正跟我没关系'全部保留，柜员插话打脸刘美娟的关键转折忠实还原。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词均为现场开口对白，有明确说话对象。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "4个时间段、12秒，包含刘美娟结巴（3秒）、柜员事实反驳（5秒）、刘美娟慌张否认（2秒）、刘美娟后退（2秒），每段一个主动作，未过载。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "老年机从第4组沈清掏出举起，到第5组组首'沈清右手举着老年机'，道具归属连续。",
      "fix_instruction": "无需修改"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第5组",
      "rule": "dialogue_pacing",
      "problem": "刘美娟慌张台词字秒比达到6.5上限。",
      "evidence": "有效字数13，镜头2秒，字秒比6.5，恰好在6.5硬上限处。",
      "fix": "如需更稳妥可延长至2.5秒，但当前不超标。"
    }
  ]
}
