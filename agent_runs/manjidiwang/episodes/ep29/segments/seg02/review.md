{
  "pass": true,
  "summary": "seg02两组已对照医院病房剧本审核，病情说明、集团汇报和交托台词完整，未发现硬性问题。",
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
    "filmability": "checked"
  },
  "spot_checks": [
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "组内保留朱天和已摘呼吸机、医生翻病历并说“毒素完全清除，朱副董度过危险期。”、朱天和虚弱询问集团情况，顺序与原剧本一致。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "朱文浩两句汇报分别为10字/2秒和11字/2秒，朱天和“好，好，你比我强。”7字/2秒为短句，“以后，这个家，这个集团，交给你了。”14字/4秒且带虚弱气息，符合病房慢语状态。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "第3组场景始终为市医院特护病房，病床、呼吸机、病历和三名人物在组首空间锁定中交代清楚，没有跨到其他物理空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "朱天和、朱文浩、医生在组首均有位置、身体朝向和道具来源，医生说话前已手持病历，朱天和发问前在病床上可见。",
      "fix_instruction": "无需修复；若增加护士或其他人员，需先在组首或行动前写明位置。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组结尾朱文浩站在床边准备坐下回应，第4组组首朱文浩在床边椅子旁并靠近水杯，坐下与倒水动作衔接原剧本。",
      "fix_instruction": "无需修复；保持病床、床头柜、水杯位置连续。"
    },
    {
      "group": "第4组",
      "type": "filmability",
      "result": "pass",
      "evidence": "欣慰和交托通过朱天和眼眶、嘴角、叹气、肩膀放低和具体台词表现，未使用不可拍的内心结论替代画面。",
      "fix_instruction": "无需修复；继续用表情、动作和台词承载情绪。"
    }
  ],
  "issues": [],
  "warnings": []
}
