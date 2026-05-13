{
  "pass": true,
  "summary": "seg03审核通过，电话音与周昌平现场开口区分清楚，赵乡长安排、副主任岗位和陆凡任命均保留。",
  "checked_groups": ["第5组", "第6组"],
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
      "group": "第5组",
      "type": "audio_mouth_sync",
      "evidence": "刘波台词均写为听筒里的电话音，周昌平听电话时写明嘴唇闭合不做口型，现场口型没有混用。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "evidence": "周昌平指定陆凡、刘波提出不合规、周昌平拍桌命令、刘波答应和周昌平OS均按原剧本顺序保留。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "0-4秒台词约16字/4秒，4.0字/秒；8-11秒含两句电话交锋约18字/3秒，6.0字/秒，均低于6.5硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "刘波以电话声音出现，声音来源为红色电话；周昌平在组首已持有听筒。",
      "fix_instruction": "若刘波现场出现，应改成电话音或安排明确入场。"
    },
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "内心旁白段写明周昌平嘴唇闭合不做口型，符合OS承载要求。",
      "fix_instruction": "若OS被写成现场开口，应改为内心旁白并补闭口状态。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾部周昌平听见人选追问，第6组组首仍握着电话并继续回答，电话状态连续。",
      "fix_instruction": "若电话道具状态断裂，应补充持有或放下电话的可见过渡。"
    }
  ],
  "issues": [],
  "warnings": []
}
