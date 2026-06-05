{
  "pass": true,
  "summary": "seg04 保留周桂兰控诉、周建国恼羞成怒承认花养老钱、沈清冷酷反击并保存云端备份的证据闭环。",
  "checked_groups": ["第5组", "第6组"],
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
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "第5组完整保留周桂兰“我是疯了”“连你也合伙骗我”和周建国两句反驳，没有改变人物关系。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "evidence": "沈清的录像手机从组首在右手，到点保存按钮，再转向周建国展示，和周美娟的钻石壳手机区分明确。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "沈清“养我妈？你有什么脸说这话！”约12字给2秒约6字/秒，云端备份台词约12字给3秒内完成，未超过6.5字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "周桂兰先对周美娟喊，再对周建国控诉，周建国两句均对周桂兰吼，现场对象明确。",
      "fix_instruction": "若不通过，应补明周桂兰和周建国的对话对象。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第5组是同一冲突下四句现场对峙，拍桌动作与周建国第二句同步，不额外新增强动作。",
      "fix_instruction": "若不通过，应把周建国拍桌与第二句台词分开或缩短普通反应。"
    },
    {
      "group": "第6组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "第6组分为沈清反击、保存视频、展示云备份三段，每段一个主动作或一句关键台词。",
      "fix_instruction": "若不通过，应拆分保存和展示手机动作。"
    },
    {
      "group": "第6组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第6组禁止项锚定沈清录像手机、周美娟钻石壳手机、云端备份台词和周建国抢夺风险，未使用通用占位词。",
      "fix_instruction": "若不通过，应改为本组证据手机相关的具体禁项。"
    }
  ],
  "issues": [],
  "warnings": []
}
