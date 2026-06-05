{
  "pass": true,
  "summary": "seg01保留周建国雪地捡纸皮、叹气、撞散纸皮和路人嫌恶的剧情，格式和节奏可交付。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "周建国台词“哎，早知今日，何必当初啊……”约12字，用6-10秒中的4秒承载，约3字/秒，符合悔恨自语的慢语场景。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "原剧本的撞倒纸皮、路人嫌恶台词、路人躲开和周建国蹲地捡纸皮均被保留，没有新增改变剧情的动作。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "两组都限定在寒风中的商业街头，组首写明周建国、路人、破三轮车和纸皮位置。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "周建国的自言自语是画面人物真实开口，镜头写到嘴唇动作清楚，没有误写为画外音或心声。",
      "fix_instruction": "若不通过，应明确自语为现场开口或改成闭口画外音来源。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "撞散纸皮、路人责备、路人绕开、周建国蹲下捡纸皮分在不同时间段，每段一个主动作。",
      "fix_instruction": "若不通过，应拆开撞倒、责骂、捡拾等动作。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定周建国、破三轮车、破旧军大衣和纸皮，未使用占位模板。",
      "fix_instruction": "若不通过，应删除泛泛词并替换成本组人物和道具锚点。"
    }
  ],
  "issues": [],
  "warnings": []
}
