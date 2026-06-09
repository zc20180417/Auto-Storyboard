{
  "pass": true,
  "summary": "第1组法官宣判赵强、第2组法官宣判周美娟，格式、台词、节奏、空间锁定均符合规则，无硬问题。",
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
      "evidence": "法官'被告人赵强，犯偷税漏税罪、职务侵占罪。'16字/3秒=5.3字/秒；'判处有期徒刑五年，并处罚金三百万元！'17字/5秒=3.4字/秒，均未超过6.5字/秒硬上限。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "法官'被告人周美娟，犯盗窃罪、非法侵占他人财产罪。'18字/3秒=6字/秒；'判处有期徒刑三年，责令退赔所有赃款！'11字/2秒=5.5字/秒，均未超过6.5字/秒硬上限。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "组首空间锁定明确列出法官、沈清、周桂兰、赵强、周美娟的位置和朝向，单一物理空间（法庭），无跨场景。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有对白均为法官现场开口，有明确说话对象（赵强、周美娟），无心声/画外音混用。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "2个强节拍（宣读罪名、宣判刑期+反应），属同一审判事件链，7秒容量充足。",
      "fix_instruction": "无需修复"
    },
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每个时间段只承载一个主动作：法官敲槌、法官宣读赵强罪名、法官宣判赵强刑期+赵强瘫跪，无动作过载。",
      "fix_instruction": "无需修复"
    }
  ],
  "issues": [],
  "warnings": []
}
