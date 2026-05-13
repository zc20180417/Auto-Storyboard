{
  "pass": true,
  "summary": "EP02分镜共3组，台词全部保留原剧本，对话指向清晰，内心独白口型正确，空间锁定完整，无模板污染。Group 2连续对话节拍节奏偏快但属于同一冲突下的快速交锋，可接受。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "Group 2 dialogue consolidated into continuous beats: 1-6秒 beat (Li Hu greeting + news 25字 + Wang Shuang reaction 7字 = 32字/5秒=6.4字/秒), 6-13秒 beat (Li Hu whisper 37字 + Wang Shuang response 19字 = 56字/7秒=8.0字/秒, continuous rapid exchange), 13-15秒 beat (Li Hu final 28字/2秒=14字/秒, climactic line with action)."
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "Group 1 保持单一物理空间（小区院子），组首空间锁定明确列出李虎位置和配电箱位置。Group 2 单一物理空间（王婶家门口走廊），锁定列出两人位置和朝向。Group 3 明确标注为屏幕画面。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "原剧本2-3场景全部台词完整保留：李虎语音消息（29字）、文字消息（16字）、王婶文字回复（14字），无删改或错置。Group 1 李虎OS完整保留并正确转为内心旁白。Group 2 全部对话台词忠实保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "Group 1 李虎内心旁白正确标注为内心旁白响起，同镜头写明嘴唇闭合、不做口型。",
      "fix_instruction": "已通过审核，无需修复。内心旁白口型标注正确。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "Group 2 共5个时间段，含3个连续对话节拍和1个开门动作，服务于同一冲突（散布老张谣言），无强节拍过载。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "Group 2 尾部李虎提到'我得在群里提醒提醒大家'，Group 3 切至微信群界面，剧情因果连贯。",
      "fix_instruction": "已通过审核，无需修复。剧情因果从散布谣言到发微信群衔接自然。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "dialogue_pacing",
      "problem": "Group 2 连续对话节拍整体节奏偏快，部分时段超过6.5字/秒，但属于同一冲突下的快速交锋且有说话人切换支撑。",
      "evidence": "1-6秒: 32字/5秒=6.4字/秒；6-13秒: 56字/7秒=8.0字/秒；13-15秒: 28字/2秒=14字/秒。",
      "fix": "如需降低节奏，可将Group 2拆为两组，但部分组可能不足10秒下限。"
    }
  ]
}
