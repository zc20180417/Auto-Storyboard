{
  "pass": true,
  "summary": "seg03 已对照原剧本完成审核，打掉夺卡的手、蛋糕落地、保管质问、披外套和自助机查账反击均保留，未发现硬问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组"],
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
      "evidence": "打手、刘美娟缩手、蛋糕砸地、尖叫与沈清短句反击分成 4 个时间段，动作链清楚。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "银行卡从第2组沈清举着延续到第3组沈清手中，旧外套从床尾被拿起并披到周桂兰肩上，组尾继续锚定。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "刘美娟银行关门台词约 15 字 / 3 秒，约 5.0 字/秒；沈清自助机台词约 17 字 / 5 秒，约 3.4 字/秒但伴随扶稳母亲和越过刘美娟看向门外，属于结尾压迫短反击。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "原剧本中的啪地打掉刘美娟手、手背发红、蛋糕砸地、刘美娟尖叫和沈清别碰东西均保留。",
      "fix_instruction": "若不通过，应恢复打手与蛋糕落地动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "刘美娟和沈清的三句对质均明确写成对沈清或刘美娟说道，未发明假对象。",
      "fix_instruction": "若不通过，应补足真实对话对象。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组包含沈清举卡警告、扶起周桂兰、披旧外套和查账台词，动作按阶段拆成 12 秒，未并列抢焦点。",
      "fix_instruction": "若不通过，应将披外套和查账台词拆开。"
    },
    {
      "group": "第4组",
      "type": "timing_math",
      "result": "pass",
      "evidence": "第4组总时长 8 秒，属于结尾短句反击；时间段 0-3 秒、3-8 秒连续，镜头数 2 个匹配。",
      "fix_instruction": "若不通过，应保持 6-9 秒短组理由或并入前组但不得压缩台词。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组组尾周桂兰披旧外套、沈清扶着她、银行卡在沈清手中；第4组组首完整继承这些状态。",
      "fix_instruction": "若不通过，应在第4组组首补齐旧外套和银行卡归属。"
    },
    {
      "group": "第4组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定刘美娟、银行卡、周桂兰、旧外套和沈清，数量 3 条，聚焦结尾查账风险。",
      "fix_instruction": "若不通过，应替换为本组具体剧情错误。"
    }
  ],
  "issues": [],
  "warnings": []
}
