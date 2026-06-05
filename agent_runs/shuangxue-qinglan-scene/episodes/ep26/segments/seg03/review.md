{
  "pass": true,
  "summary": "seg03完成周建国哭骂、周桂兰揭出救命钱和杂物间旧账、沈清逼近戳穿谎言的审稿，台词和站位连续。",
  "checked_groups": ["第7组", "第8组", "第9组"],
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
      "group": "第7组",
      "type": "dialogue_pacing",
      "evidence": "周建国约18字痛哭台词安排在3-7秒4秒内，约4.5字/秒，符合情绪对白节奏。"
    },
    {
      "group": "第8组",
      "type": "script_fidelity",
      "evidence": "周桂兰两句原台词完整保留，治关节痛救命钱和杂物间剩饭两个信息点没有改写。"
    },
    {
      "group": "第9组",
      "type": "handoff_continuity",
      "evidence": "第8组尾周建国仍在地面，第9组首保持被保镖控制；沈清从画面右侧靠近后停在周建国前方半步。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首列出周建国、两个保镖、周桂兰和沈清的位置朝向，周建国台词发生前人物可用。",
      "fix_instruction": "若不通过，应在组首补周桂兰或保镖位置。"
    },
    {
      "group": "第8组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "周桂兰两句现场对白都写明对周建国说，没有心声或旁白混用。",
      "fix_instruction": "若不通过，应改成周桂兰对周建国说道。"
    },
    {
      "group": "第9组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "周建国狡辩、沈清走近、沈清冷声反击分别成段，每段只有一个主动作或对白块。",
      "fix_instruction": "若不通过，应拆开沈清走近和冷声台词。"
    },
    {
      "group": "第9组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "沈清逼近组有4个锚定人物的禁止项，避免殴打、逃跑、放人和台词错位。",
      "fix_instruction": "若不通过，应替换为本组具体动作风险。"
    }
  ],
  "issues": [],
  "warnings": []
}
