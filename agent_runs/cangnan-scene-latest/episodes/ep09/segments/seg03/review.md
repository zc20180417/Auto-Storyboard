{
  "pass": true,
  "summary": "seg03审讯室反转两组保留林夏破门、证据甩桌和陆凡交出原版账单的关键反杀信息。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "evidence": "林夏在组首位于门外走廊阴影处并持有银行流水单，破门入场和甩证据前具备可用位置和道具。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "林夏18字台词用4秒约4.5字/秒，王建国13字用3.5秒约3.7字/秒并带瘫软反应，陆凡20字用5.5秒含站起动作，节奏可表演。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留资金来源合法、财政所账对不上、原版账单已交市纪委三项信息，未新增改变因果的动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "银行流水单从林夏手中甩向审讯桌，随后第2组组首明确散落在王建国一侧，归属和位置连续。",
      "fix_instruction": "若不通过，应补充流水单落桌后的具体位置。"
    },
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "林夏对王建国暴喝，王建国对林夏解释，台词对象均为画面内真实人物。",
      "fix_instruction": "若不通过，应补充真实对话对象。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾流水单落桌，林夏、王建国、陆凡三人位置在第2组组首被具体复述，无同空间跳变。",
      "fix_instruction": "若不通过，应在第2组组首写清三人的桌边位置。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组为桌面证据特写、林夏定性错案、王建国瘫软辩解、陆凡起身揭示市纪委四个节拍，15秒内无额外外部事件。",
      "fix_instruction": "若不通过，应拆出陆凡揭示原版账单为单独短组。"
    }
  ],
  "issues": [],
  "warnings": []
}
