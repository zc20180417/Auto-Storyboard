{
  "pass": true,
  "summary": "第4-5组完整保留保镖甲擒拿、陆凡扣腕反制、推倒保镖甲和连续三记过肩摔制服其余三人的动作链，节奏可表演。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "保镖甲“躺下吧。”4字分配2秒，带近景威胁表情，不存在过快或拖慢。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "保镖甲擒拿逼咽喉、陆凡不退反进扣住手腕、发力一推摔倒保镖甲均对应原剧本动作。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "evidence": "三名保镖扑上、陆凡穿插走位、三记过肩摔被拆成12秒三段，连续动作链有完整表演时间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾部保镖半包围逼近，第4组组首复述陆凡和保镖甲的面对位置及三名保镖包围状态。",
      "fix_instruction": "若不通过，应在第4组组首补齐保镖位置和朝向。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "第4组尾部保镖甲甩棍脱手滚到家具旁，第5组组首复述甩棍在他手边，其余保镖仍持甩棍。",
      "fix_instruction": "若不通过，应补充甩棍掉落或保镖持棍状态。"
    },
    {
      "group": "第5组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "动作描述为可见打斗和摔落结果，无模型词、模板编号、参考图或禁用批量句。",
      "fix_instruction": "若不通过，应删除工程说明并改为可见动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
