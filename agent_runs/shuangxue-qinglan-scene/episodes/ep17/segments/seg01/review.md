{
  "pass": true,
  "summary": "seg01 已对照原剧本完成审核，房产证复印件举证、周建国反驳和沈清两句追责台词均保留，未发现硬问题。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "周建国约10字台词给3.5秒、沈清约14字台词给4秒，均低于6.5字/秒，手提包动作独立承载。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留沈清拿出红色房产证复印件、声明院子来源、倒插门指控，以及周建国“胡说八道”的反驳。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "红色房产证复印件从第2组组尾延续到第3组组首，并在两段台词中持续由沈清持有。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "周建国和沈清的现场对白均写为对对方说道，没有假对象或心声混用。",
      "fix_instruction": "若缺对象，应补成周建国对沈清说道或沈清对周建国说道。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组按拿出复印件、举证、怒斥、周建国反驳四个阶段拆开，15秒内每段只有一个主动作或对白块。",
      "fix_instruction": "若过载，应把周建国反驳拆成下一组或压缩非关键反应。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组组尾沈清举着复印件，第3组组首直接复述该状态，人物仍在同一客厅位置。",
      "fix_instruction": "若缺连续性，应在第2组组尾或第3组组首补复印件归属和人物位置。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定沈清、周建国、赵强和红色房产证复印件，数量3条且不禁止原剧本动作。",
      "fix_instruction": "若出现泛泛词，应替换为本组具体人物或复印件风险。"
    }
  ],
  "issues": [],
  "warnings": []
}
