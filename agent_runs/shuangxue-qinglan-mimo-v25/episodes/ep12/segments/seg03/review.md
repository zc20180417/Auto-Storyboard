{
  "pass": true,
  "summary": "seg03 两组均通过审核，外部事件入场、道具揭示、慢语台词均无硬伤。",
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
      "evidence": "周美娟尖叫12字/2.5秒=4.8字/秒（情绪对白），周建国耍赖21字/4秒=5.25字/秒（情绪对白），均在4.5-6.5范围内。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "沈清冷若冰霜22字/4秒=5.5字/秒（情绪对白），沈清一字一句19字/5.5秒=3.45字/秒（明确慢语'一字一顿'，目标3.8字/秒，19字需5.0秒，实际5.5秒充足）。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "第1组组首写明右侧里屋门关着、周美娟和赵强尚未出来，与全景镜头中两人从里屋冲出的动作一致。外部事件入场按阶段拆开：冲出→尖叫→周建国指骂→沈清冷笑，无过载。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有对白均为画面内真人开口。周美娟对沈清尖叫，周建国对沈清耍赖，指向明确。沈清冷笑无台词，不做口型。",
      "fix_instruction": "无需修改，口型和指向均正确。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第1组4个时间段，2个强节拍（外部事件入场、周建国指骂）。第2组4个时间段，2个强节拍（铺流水道具揭示、一字一句台词）。动作链完整，无过载。",
      "fix_instruction": "无需修改，强节拍密度合理。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "委托书从seg02延续到seg03组首仍在茶几上，第2组中被银行流水账单覆盖，组尾写明'委托书压在账单下方'，道具状态连续。",
      "fix_instruction": "无需修改，道具归属连续。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第1组因外部事件入场写了视频禁止项3条，第2组因关键道具揭示写了视频禁止项3条，均锚定本组人物和道具，无泛泛词。",
      "fix_instruction": "无需修改，视频禁止项具体且锚定上下文。"
    }
  ],
  "issues": [],
  "warnings": []
}
