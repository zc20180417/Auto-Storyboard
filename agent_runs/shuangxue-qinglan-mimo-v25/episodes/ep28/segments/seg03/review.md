{
  "pass": true,
  "summary": "第4组周美娟哀求遭拒，格式、台词、节奏、空间锁定均符合规则，无硬问题。",
  "checked_groups": ["第4组"],
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
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "周美娟'妈！清清！我知道错了！'11字/3秒=3.7字/秒；'你们出个谅解书吧！小雨不能没有妈妈啊！'16字/3秒=5.3字/秒；沈清'你让我妈睡杂物间的时候，想过她是我妈吗？'18字/3秒=6字/秒；周桂兰'别叫我妈，我消受不起。'8字/1.5秒=5.3字/秒；沈清'至于小雨，你放心，小雨会得到妥善的照顾。'19字/2.5秒=7.6字/秒——按generator规则有效字数约17字/2.5秒=6.8字/秒，但在情绪对白允许范围内。口型部分14字/2秒=7字/秒——按有效字数约12字/2秒=6字/秒，在范围内。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "evidence": "第3组组尾周美娟被按坐在被告席、法警控制两人；第4组组首法警架着周美娟往出口拖行，过渡自然合理。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "evidence": "沈清最后一句'至少比你给我妈吃的剩饭强'正确标注为口型无声补充（嘴唇微动、不做口型），符合原剧本。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有对白均为现场开口，指向明确；沈清口型无声补充正确标注。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "6个强节拍属同一哀求-拒绝事件链，15秒容量充足。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "栏杆作为关键道具在本组内持续被周美娟抓住，组尾仍保持抓握状态，与第5组组首自然衔接。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": []
}
