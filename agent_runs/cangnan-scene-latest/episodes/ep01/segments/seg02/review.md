{
  "pass": true,
  "summary": "seg02 保留处分、下放、即刻报到和陆凡内心旁白，音画分离处理正确。",
  "checked_groups": ["第1组"],
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
      "evidence": "保留红头文件、纪委干部处分理由、陆凡接受处理、调离县委下放清河乡、即刻去民政办的全部信息。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "10.5-15秒内心旁白约26字用4.5秒承载，字秒比约5.8；其他对白段均低于6.5字/秒硬上限。"
    },
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "evidence": "陆凡内心旁白明确写为嘴唇闭合不做口型，未写成现场开口对白。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "县委会议室、长会议桌、红头文件、纪委干部和陆凡位置朝向均在组首锁定。",
      "fix_instruction": "若不通过，应补齐会议室布局和两人面对关系。"
    },
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "纪委干部与陆凡的现场对白均以对方为真实对象，陆凡OS没有被改成对人说话。",
      "fix_instruction": "若不通过，应改为“A对B说道”或明确内心旁白闭口。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只包含推文件、处分问答、起身离开和内心旁白，15秒内容量可表演。",
      "fix_instruction": "若不通过，应拆出内心旁白或减少非关键动作。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有Seedance说明、模板编号、占位符或工程性描述。",
      "fix_instruction": "若不通过，应删除污染词。"
    }
  ],
  "issues": [],
  "warnings": []
}
