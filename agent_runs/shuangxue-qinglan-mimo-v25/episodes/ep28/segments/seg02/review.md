{
  "pass": true,
  "summary": "第3组周美娟崩溃争执，格式、台词、节奏、空间锁定均符合规则，无硬问题。",
  "checked_groups": ["第2组", "第3组"],
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
      "type": "dialogue_pacing",
      "evidence": "周美娟'三年……我不要坐牢……我不去！'10字/3秒=3.3字/秒；'都怪你！是你让我拿老太婆的钱填账的！'17字/3秒=5.7字/秒；赵强'是你自己贪慕虚荣买金买车！'12字/2秒=6字/秒；法警'肃静！法庭之上严禁喧哗！'10字/2.5秒=4字/秒，均未超过6.5字/秒硬上限。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "evidence": "第2组组尾赵强瘫跪地面、周美娟僵立被告席、法警两侧待命；第3组组首赵强仍瘫跪、周美娟坐在椅子上，连续无跳变。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "周美娟颤声哭喊、怒视赵强指责、赵强反唇相讥、法警喝止并控制——均与原剧本一致，台词顺序、说话对象、关键动作完整保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有对白均为现场开口，周美娟对赵强说、赵强对周美娟说、法警对两人喝止，指向明确。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "5个强节拍属同一争执事件链的连续推进，每个时间段只承载一个主动作，13秒容量充足。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第3组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每个时间段只承载一个主动作或一个连续对话节拍，法警控制两人作为复合动作在同一时间段内完成，无动作过载。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": []
}
