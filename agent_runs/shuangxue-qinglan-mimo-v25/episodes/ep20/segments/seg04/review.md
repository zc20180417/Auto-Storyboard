{
  "pass": true,
  "summary": "seg04 两组均符合规则：周桂兰已列入人物栏，台词忠实完整保留，口型指向正确，空间单一且连续。",
  "checked_groups": ["第6组", "第7组"],
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
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "周建国11字÷3秒=3.7字/秒，沈清连续台词37字÷9秒=4.1字/秒，均未超6.5字/秒硬上限。"
    },
    {
      "group": "第7组",
      "type": "action_atomicity",
      "evidence": "第7组三个时间段分别承载：周建国跌坐（单一动作）、沈清连续对白（一个说话节拍）、沈清扶周桂兰离开（单一动作），每段一个主动作。"
    },
    {
      "group": "第7组",
      "type": "script_fidelity",
      "evidence": "沈清台词'偷盗古董可是重罪''明早八点我来收房，谁还留在里面，我就让警察请他出来！'完整保留；'沈清扶着周桂兰，转身决绝地离开客厅'忠实还原。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词均为画面内现场对白，沈清对周建国直接质问，无心声/旁白混用。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第7组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "3个强节拍（周建国跌坐、沈清通牒、扶周桂兰离开），每段只承载一个主动作，13秒容量合理。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "上一组组尾'周建国瘫坐在太师椅上'，本组组首'周建国瘫坐在太师椅上'，状态连续；沈清位置从手持手机过渡到站立原位。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第7组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第7组不涉及复杂站位或保护关系，不需要视频禁止项。",
      "fix_instruction": "无需修改"
    }
  ],
  "issues": [],
  "warnings": []
}