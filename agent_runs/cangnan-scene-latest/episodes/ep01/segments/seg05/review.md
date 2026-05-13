{
  "pass": true,
  "summary": "seg05 保留陆凡到民政办、张强刁难、秦虹搬资料和考核威胁，分两组承载清楚。",
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
      "evidence": "保留陆凡走入大厅、有人打游戏、张强拦路、“你就是新来的陆凡”“我来报到”“听说你连县里领导都敢打”“请让开”。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留张强叫秦虹拿资料、秦虹说资料未录完、张强呵斥并要求陆凡下班前录入系统、考核责任威胁。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "救助资料从秦虹身边到办公桌，通过3-6秒秦虹抱起并放下两摞资料完成可见过渡。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "张强与陆凡所有现场对白均写明对对方说，未出现假对象对白。",
      "fix_instruction": "若不通过，应补充真实对话对象。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "秦虹在第2组组首已位于右后方办公桌旁，行动和说话前可用。",
      "fix_instruction": "若不通过，应在组首加入秦虹位置或安排入场。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "资料搬放、秦虹解释、张强呵斥、陆凡反问和张强威胁分为5段，总时长15秒可承载。",
      "fix_instruction": "若不通过，应拆分资料搬放和考核威胁。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "未出现工程词、模板编号、自动分镜或参考图描述。",
      "fix_instruction": "若不通过，应删除污染词。"
    }
  ],
  "issues": [],
  "warnings": []
}
