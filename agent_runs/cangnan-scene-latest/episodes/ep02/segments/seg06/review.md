{
  "pass": true,
  "summary": "seg06已审核，锈钥匙羞辱、次日电话调去公墓和张强嘲笑均保留，电话音与口型分离正确。",
  "checked_groups": ["第13组", "第14组", "第15组"],
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
      "group": "第13组",
      "type": "script_fidelity",
      "evidence": "张强扔出锈钥匙、安排河边老红砖房、陆凡答没问题、张强嘲讽招待所均保留。"
    },
    {
      "group": "第14组",
      "type": "audio_mouth_sync",
      "evidence": "党政办电话音从座机听筒传出，陆凡听电话时写明嘴唇闭合不做口型。"
    },
    {
      "group": "第15组",
      "type": "dialogue_pacing",
      "evidence": "第15组0-3秒党政办12字电话音约4字/秒，5.5-10秒张强10字嘲讽约2.2字/秒且伴随狂笑动作，未超过硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第13组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "锈钥匙从张强手中扔到桌面，再被陆凡拿起收进掌心，关键道具转移完整。",
      "fix_instruction": "若不通过，应补钥匙落桌或陆凡拿起的可见动作。"
    },
    {
      "group": "第14组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "次日清晨的新时间点另起一组，组首锁定陆凡工位、张强远处和座机位置。",
      "fix_instruction": "若不通过，应拆分时间跳转并补足座机位置。"
    },
    {
      "group": "第15组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第15组仅电话补充、挂断和张强嘲笑三个节拍，10秒内清楚可表演。",
      "fix_instruction": "若不通过，应把张强嘲笑单独保留为短收尾组。"
    }
  ],
  "issues": [],
  "warnings": []
}
