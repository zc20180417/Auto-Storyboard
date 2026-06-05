{
  "pass": true,
  "summary": "seg01 保留十九万逼债、一起死威胁、金镯子被扣住和摘镯抵债命令，格式与时长合同通过。",
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
      "evidence": "赵强 16 字用 3 秒约 5.3 字/秒，沈清 11 字用 2.5 秒约 4.4 字/秒，周美娟威胁句 16 字在 5 秒内含攥手动作，未超过 6.5 字/秒。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "金镯子从组首周美娟右手腕、到沈清扣住手腕并指向镯子、到组尾仍卡在周美娟手腕上，归属和位置连续。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留“一起死？你舍得你手上的金镯子吗？”和“摘下来！抵债！”两句关键台词，并保留抓手腕指金镯子的关键动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "赵强、沈清、周美娟所有现场对白均写明对沈清、对赵强或对周美娟说道。",
      "fix_instruction": "若不通过，应补足每句现场对白的真实对话对象。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "抓手腕、命令摘镯、周美娟攥紧分别拆成清楚时间段，没有在单个时间段塞入多个主动作。",
      "fix_instruction": "若不通过，应拆分抓手腕和命令台词的时间段。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项围绕周美娟金镯子、沈清抓手腕、赵强不抢动作，均有本组人物或道具锚点。",
      "fix_instruction": "若不通过，应替换无锚点或与剧情矛盾的禁止项。"
    }
  ],
  "issues": [],
  "warnings": []
}
