{
  "pass": true,
  "summary": "ep24 seg01 保留保险室取证、会客室对峙、电梯停运和楼梯间突围，全段按物理空间拆组并通过审核。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组"],
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
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "喷淋头被金属杆砸碎、水雾让红外线短暂失灵、顾北辰说“我选第三个。”、拔下录音笔并踢短路自毁装置均按原剧本保留。"
    },
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "evidence": "顾北辰“笔到手，撤。”作为耳机声音出现，许知夏嘴唇闭合不做口型，只表现听见后的眼神反应。"
    },
    {
      "group": "第8组",
      "type": "space_locking",
      "evidence": "楼梯间组首写明许知夏在楼梯平台、安全门位置、上下楼梯的秦越手下位置；顾北辰在0-3秒从安全门入场后才挡人和说话。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "顾北辰OS写为心声，镜头描述明确嘴唇闭合不做口型；秦越和顾北辰的现场对白均有真实对话对象。",
      "fix_instruction": "若不通过，应把OS改成心声闭口，或把现场对白补齐对象。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组把砸喷淋头、水雾干扰、短句反击、取走录音笔并踢短路装置分成四段，复杂动作链有5秒完成。",
      "fix_instruction": "若不通过，应拆开取笔和踢自毁装置，或把打斗动作移到下一组。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "许知夏长句约26字给5.5秒，约4.7字/秒；沈曼短句2秒，符合现场紧张对白节奏。",
      "fix_instruction": "若不通过，应把许知夏长句拆成反打或增加0.5秒。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾部许知夏站起与秦越对峙，第6组组首保持许知夏站在桌边、秦越站在门内、沈曼在身后半步，人物位置连续。",
      "fix_instruction": "若不通过，应在第5组尾或第6组组首补明三人站位。"
    },
    {
      "group": "第8组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "顾北辰入场挡人、放话、护着许知夏下撤、上下夹击逼近、格开下方手臂分别分段；秦越手下只负责夹击，没有抢走保护动作。",
      "fix_instruction": "若不通过，应把楼梯间打斗拆成两组并分别锚定录音笔和许知夏站位。"
    },
    {
      "group": "第8组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定录音笔、许知夏、秦越手下和顾北辰保护站位，数量4项，均为本组特有风险。",
      "fix_instruction": "若不通过，应删除泛泛风险并补充具体人物和道具锚点。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终正文没有模型说明词、参考模板、官方编号、参考图占位符或非分镜正文。",
      "fix_instruction": "若不通过，应删除工程说明和模板化描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
