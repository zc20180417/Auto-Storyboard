{
  "pass": true,
  "summary": "两组分镜忠实还原债务追讨场景，台词指向和口型正确，空间锁定和组间衔接清晰，无硬错误。",
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
      "evidence": "周美娟台词14字÷3秒含动作=4.67字/秒（情绪对白），张总台词16字÷3秒含抓人动作=5.33字/秒（情绪对白），均在合理范围。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "周建国台词'她有钱！她是我女儿，她今天包场花了上百万！找她要！她是大老板！她有的是钱给你们！'完整保留，张总台词'哟，沈老板，替父还债啊？'完整保留，台词顺序与原剧本一致。"
    },
    {
      "group": "第1组→第2组",
      "type": "handoff_continuity",
      "evidence": "第1组组尾写明'周建国被张总揪住衣领站立'，第2组组首空间锁定复述同一状态，人物位置和道具归属连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "周美娟和张总均为画面内现场开口对白，均写明了说话对象（对周建国说道），无心声/画外音混用。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组4个时间段各承载一个主动作或连续对话节拍：指认喊话→继续指认→哀求→张总转向冷笑，强节拍数约3-4个，属于同一事件链（祸水引向沈清）的连续推进。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第1组→第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "第1组关键道具'周美娟裙角'在组尾已脱离周建国的手，第2组周美娟不在画面中，裙角不再需要锚定。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每个时间段只有一个主动作：0-3秒指认+喊话，3-6秒继续指认+台词，6-9秒哀求+台词，9-13秒张总转向+冷笑台词。非主动作人物周建国在9-13秒只写肩膀轮廓，没有抢张总动作。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项3条均锚定本组人物和动作：周美娟主动扶起周建国、张总松开衣领、沈清提前出现，均为本组特有剧情错误。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "全文无Seedance可、自动正反打、模板编号、@图片等模型说明词或模板污染，无模板化批量描述。",
      "fix_instruction": "无需修改"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "dialogue_pacing",
      "problem": "0-3秒段有效台词仅4字（'她有钱！'），含指人动作后仍有约1秒空余，整体偏慢（约2字/秒）。",
      "evidence": "有效字数4÷约2秒有效台词时间=2.0字/秒，低于情绪对白4.8字/秒目标；但有中等动作（指向沈清）填充，不构成硬错误。",
      "fix": "可考虑将0-3秒与3-6秒合并为0-6秒连续对话节拍'她有钱！她是我女儿，她今天包场花了上百万！'，但分开拍摄也有指认动作的戏剧张力。"
    }
  ]
}