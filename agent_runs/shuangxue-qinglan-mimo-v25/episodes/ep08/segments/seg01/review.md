{
  "pass": true,
  "summary": "seg01审核通过，3组台词节奏、空间锁定和剧本忠实度均无硬伤。",
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
      "evidence": "沈清台词'妈，你看，25号下午两点进账八千'共14字，普通对白÷4.5=3.1秒，实际分配6秒（4-10秒），字秒比2.3，合格。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "组首空间锁定列出沈清在画面中央持账单、周桂兰在左侧低头看账单、刘美娟在右侧后方、柜员在柜台后方，空间关系清晰。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "原剧本'二十四个月！次次都是分批小额转出，完美规避了银行的风控预警！这手段够专业的啊！'和'造孽啊……这是算计好了吸我的血啊！'完整保留，刘美娟脸色惨白后退的反应忠实还原。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词均为画面人物现场开口对白，有明确说话对象。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "3个时间段、11秒，包含声音颤抖揭露（5秒）、翻动账单（3秒）、账单特写（3秒），每段一个主动作，未过载。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾部'账单仍在沈清手中，已翻至多页；周桂兰攥紧衣角'与第3组组首'沈清手中持有流水账单，翻至记录页；周桂兰双手攥在衣角'连续。",
      "fix_instruction": "无需修改"
    }
  ],
  "issues": [],
  "warnings": []
}
