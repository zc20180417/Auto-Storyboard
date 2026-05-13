{
  "pass": true,
  "summary": "seg04保留父子带云宝到活水井、胡永贵以毒液瓶威胁泉眼的悬念，岩洞内左右对峙和道具危险位置明确。",
  "checked_groups": ["第7组", "第8组"],
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第7组",
      "type": "space_locking",
      "evidence": "岩洞入口在左侧，古老深井在中央偏右，爸爸和天天从左侧进入并靠近井口，云宝始终在爸爸手中。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "evidence": "玻璃瓶由胡永贵右手持有，从右后方阴影带出后悬在活水井正上方，毒液威胁位置清楚。"
    },
    {
      "group": "第8组",
      "type": "script_fidelity",
      "evidence": "保留手电光打断、胡永贵“别动！”台词、毒液瓶威胁泉眼、天天喊“你这个大坏蛋！快把瓶子拿开！”的原剧情顺序。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "爸爸对天天说“就是这口活水井，天天，快把云宝放进去！”，对象明确且与递交动作一致。",
      "fix_instruction": "若不通过，应明确爸爸面向天天而非自语。"
    },
    {
      "group": "第8组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "爸爸、天天在左中，活水井在中央偏右，胡永贵从右后方走出，毒液瓶悬在井口上方，左右对峙成立。",
      "fix_instruction": "若不通过，应固定井口和胡永贵的左右关系。"
    },
    {
      "group": "第8组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "15秒内分为手电打断、胡永贵警告、现身持瓶、瓶子悬井、天天反应五个短节拍，没有长动作叠长台词。",
      "fix_instruction": "若不通过，应拆分胡永贵现身和天天反应。"
    }
  ],
  "issues": [],
  "warnings": []
}
