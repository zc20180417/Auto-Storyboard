{
  "pass": true,
  "summary": "seg01含第1-2组，沈清掏出房产证并步步紧逼指控周建国，台词忠实、字秒比合格、空间单一。",
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
      "evidence": "8秒4镜头，周建国'备份就备份！老子不怕！'7字÷2秒=3.5字/秒，沈清'是吗？那咱们就好好算算账。'11字÷2.5秒=4.4字/秒，沈清'这个院子，是我亲生父亲留下的！'13字÷2秒=6.5字/秒恰好在硬上限，均合格。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "'房产证上写的是我妈的名字！''你不仅鸠占鹊巢，还合伙偷女主人的钱！'与原剧本17-1完全一致。周建国'你……你胡说八道！'保留结巴停顿。"
    },
    {
      "group": "第1组",
      "type": "action_atomicity",
      "evidence": "每时间段一个主动作：周建国喊道→沈清冷笑掏包→掏出房产证→举证指控。掏出证书和举证分为两个时间段，动作链清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "全部台词为画面人物现场开口，无心声或画外音。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾沈清手持房产证、周建国坐沙发→第2组首沈清右手持房产证、周建国坐沙发，状态连续。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "8秒4镜头，强节拍3个（喊道反驳、冷笑回应、掏出房产证），属同一对峙事件链，无过载。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
