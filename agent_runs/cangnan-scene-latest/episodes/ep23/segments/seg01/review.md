{
  "pass": true,
  "summary": "seg01 保留会议室证据反转、逮捕、陆凡断罪和李队长致谢的全部关键台词与动作，无硬问题。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "evidence": "李队长关于龙国商会总部数据、吴总监否认、李队长指出伪造账目的是吴总监，台词顺序和说话对象均与剧本一致。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "evidence": "警员甲、警员乙在组首位于背景左侧门边，先上前按住吴总监，再由李队长宣布逮捕，人物可用性成立。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "陆凡台词“充当商业间谍，破坏重点生态项目，够你把牢底坐穿。”约24字分配5秒，约4.8字/秒，符合冷酷对白节奏；李队长致谢约15字分配3秒，约5字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "李队长、吴总监的现场对白均写明对吴总监或对李队长说道，没有假对白对象。",
      "fix_instruction": "若不通过，应补齐说话对象并恢复原台词顺序。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只有挥手、警员按倒、逮捕宣告和短反应三个主要节拍，12秒内可表演。",
      "fix_instruction": "若过载，应拆出按倒动作或缩短无台词反应。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾吴总监被压住，第3组首复述他被两名警员压在会议桌边，状态连续。",
      "fix_instruction": "若不连续，应在组首复述吴总监被压住和手铐位置。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "吴总监身份疑问、陆凡商业间谍断罪、李队长铐人并感谢陆凡均保留。",
      "fix_instruction": "若缺失，应只补回对应台词和动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
