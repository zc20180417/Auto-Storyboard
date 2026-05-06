{
  "pass": true,
  "summary": "seg03已审核第4至第5组，戴手铐、对赌协议威胁、苏清寒入场、账户冻结、清算书、管家价码反转均保留，未发现硬性问题。",
  "checked_groups": [
    "第4组",
    "第5组"
  ],
  "audit_coverage": {
    "script_fidelity": "checked",
    "dialogue_direction": "checked",
    "timing_math": "checked",
    "dialogue_pacing": "checked",
    "space_locking": "checked",
    "format": "checked",
    "character_availability": "checked",
    "handoff_continuity": "checked",
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "龙建秋被戴手铐、挣扎说对赌协议仍在、疯狂说鼎丰资本吞并、苏清寒高跟鞋声后推门入场并举文件，均按原剧本呈现。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "0-2秒“这是鼎丰资本的破产清算书。”约12字/2秒，2-4秒“不可能！你们怎么做到的！”约12字/2秒，4-6秒“你的管家，收了我十倍的价码。”约14字/2秒，未超过硬上限。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "第5组仅在集团一楼大堂内完成递清算书、质问和朱文浩揭露管家收价码，没有跨场景或屏幕信息切换。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "苏清寒在组首被放置于大堂门外通道阴影处且手持文件，6-8秒推门后才正式行动和说话，来源明确。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组结尾苏清寒举文件站在入口内，第5组组首延续为苏清寒位于画面右侧手拿文件，龙建秋仍被手铐控制。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第5组",
      "type": "filmability",
      "result": "pass",
      "evidence": "海外账户冻结和破产清算通过苏清寒台词与文件、清算书纸面呈现；龙建秋震惊通过瞪眼和视线变化呈现。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第5组",
      "rule": "dialogue_pacing",
      "problem": "朱文浩最终短句节奏接近偏快上限。",
      "evidence": "4-6秒台词“你的管家，收了我十倍的价码。”约14字/2秒，字秒比约7.0，属于可接受但偏快的爽点短句。",
      "fix": "如后续模型口型压力较大，可将该镜扩为3秒并压缩6-10秒反应镜头。"
    }
  ]
}
