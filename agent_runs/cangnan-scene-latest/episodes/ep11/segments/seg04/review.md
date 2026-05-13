{
  "pass": true,
  "summary": "seg04 四组保留合同对峙、打手围攻、罪名劝阻、警笛逼退和徐虎逃跑，未发现硬问题。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "陆凡长台词约43字分配10秒，字秒比约4.3字/秒，并同步举合同动作，节奏可表演。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "徐虎关于报警的台词、下令围攻、五六个手持钢管打手扑向陆凡和陆凡利用机床货架掩体均保留。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "铁管在组首位于陆凡脚边，第4组3-6秒写明陆凡弯身抄起后只用于防守，道具转移可见。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定打开大门、铁柱、陆凡、徐虎、赵大江和江若晴，仍在同一厂房车间。",
      "fix_instruction": "若不通过，应补齐入口、铁柱和四人位置。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组12秒承载徐虎两段短台词、打手扑来和陆凡退入掩体，强节拍可表演。",
      "fix_instruction": "若不通过，应将打手扑来或陆凡退入掩体拆出。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "陆凡对打手们喊话、徐虎对打手怒吼均有真实对象，未出现假对象对白。",
      "fix_instruction": "若不通过，应补为A对B说道或改成画外音来源。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾打手动摇且徐虎加钱，第4组首两个打手再次冲、陆凡仍在机床旁，连续性成立。",
      "fix_instruction": "若不通过，应在第4组组首复述陆凡、打手和徐虎位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
