{
  "pass": true,
  "summary": "seg02 完成银行APP打开、尾号6789确认和周美娟退缩离场意图，段内短组属于逃离前的短动作承接。",
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
      "type": "script_fidelity",
      "evidence": "沈清打开银行APP、周美娟问“你要干什么”、周建国说“别胡闹了”、沈清核对尾号6789和周桂兰确认均保留。"
    },
    {
      "group": "第2组",
      "type": "timing_math",
      "evidence": "第2组时间段为0-2.5、2.5-5、5-8秒，总计8秒，属于周美娟退缩和催促回屋的短承接。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "9-13秒连续承载沈清两句短话和周桂兰确认，约31字/4秒，未超过6.5字/秒硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "旧银行卡从组首就在沈清手里，打开APP后仍与手机同框，组尾继续由沈清持有。",
      "fix_instruction": "若调整镜头，应继续明确旧银行卡和手机都在沈清可操作范围。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部周美娟在右侧，第2组组首继承右侧站位并写明脸色发白、攥包，状态连续。",
      "fix_instruction": "若重排，应避免周美娟无过渡地离开客厅。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组只有退半步、向周建国求助和催促回屋三个轻节拍，8秒不靠停顿凑长。",
      "fix_instruction": "若扩写，不要用长凝视或沉默把该短承接硬凑成10秒以上。"
    }
  ],
  "issues": [],
  "warnings": []
}
