{
  "pass": true,
  "summary": "seg01分镜保留会议室签署、闯入、对赌文件和抵押摊牌的原剧本顺序，组时长与空间锁定可通过。",
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
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "朱天和签署接管文件、说“田立民的残余势力已全部清理”、盖章后说“集团终于重回正轨”，均按原剧本顺序保留。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "0-3秒承载“我是鼎丰资本首席法务”10字和扔文件动作，3-6秒承载“田立民在离岸账户的操作，触发了对赌协议”18字，8-13秒承载朱天和质问11字和翻看动作，6-8秒用文件推进承接，均未出现1秒镜头或8秒以上台词镜头。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "全组发生在集团顶层会议室，人物为陈律师、朱天和、朱文浩、高管和黑衣人，文件、公文包和会议桌状态从上一组自然延续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "组首写明陈律师和黑衣人在门外走廊暗处可见且身体朝向门内，随后0-8秒完成推门、涌入和走到桌前，行动前有可生成位置来源。",
      "fix_instruction": "无需修复；若后续改稿，应继续避免写成尚未进入等负面状态。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组结尾为朱天和攥着文件抬头质问，文件摊在会议桌上；第4组组首延续为朱天和手里拿着文件，陈律师手按文件旁。",
      "fix_instruction": "无需修复；保持文件归属和桌前站位连续。"
    },
    {
      "group": "第1组",
      "type": "filmability",
      "result": "pass",
      "evidence": "轻松气氛通过高管姿态放松、互相点头、柔和晨光和盖章动作呈现，没有把心理结论当作主要画面。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
