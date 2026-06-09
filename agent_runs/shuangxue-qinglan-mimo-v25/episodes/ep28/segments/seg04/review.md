{
  "pass": true,
  "summary": "第5组周美娟被拖出法庭、第6组沈清安慰母亲回家，格式、台词、节奏、空间锁定均符合规则，无硬问题。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "周美娟'不——沈清！你好狠的心啊！'10字/2.5秒=4字/秒，未超过6.5字/秒硬上限。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "沈清'妈，全结束了。恶人得到报应了。'13字/2.5秒=5.2字/秒；周桂兰'是啊，结束了。心里的石头总算落了地。'14字/9秒=1.6字/秒（含搀扶动作时间），沈清'走，我们回家。回真正属于我们自己的家。'16字在同一时间段内，均合规。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "evidence": "第4组组尾周美娟抓栏杆哭泣、法警准备掰手；第5组组首延续相同状态，法警执行掰手动作，连续无跳变。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每个时间段只承载一个主动作：掰手、拖行惨叫、大门关闭，3个时间段无动作过载。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "3个强节拍（握手、安慰对话、搀扶起身），属同一收尾事件链，14秒容量充足。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "法庭大门作为关键道具从打开到关闭，状态变化清晰，与第6组组首（大门已关闭）自然衔接。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": []
}
