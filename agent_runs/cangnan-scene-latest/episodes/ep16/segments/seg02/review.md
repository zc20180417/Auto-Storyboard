{
  "pass": true,
  "summary": "两组完整保留银行拒绝冻结、宋子昂入场挑衅和项目烂尾威胁，空间、对白和节奏均可交付。",
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
      "type": "script_fidelity",
      "evidence": "江若晴拍报警回执、要求冻结海外账户，马行长以手续齐全和公章无误拒绝，均与原剧本一致。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "evidence": "宋子昂在组首设置为门外阴影后的人物，先由开门入场再说话，没有未入场直接参与对白。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "宋子昂最长句约21字用4秒承载，约5.25字/秒；其余短句均在3秒左右，未超过6.5字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "报警回执从江若晴手中拍到办公桌上，后续继续作为桌面道具存在，道具归属转移清楚。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "宋子昂和江若晴每句对白均明确对对方说道，没有旁白或心声误承载。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "入场、嘲讽、江若晴指认、逼近威胁和烂尾台词分为5个时间段，总时长15秒，动作与台词没有互相挤压。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "银行办公室对峙使用自然分镜语言，未写入Seedance说明、模板编号、参考图或工程占位符。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
