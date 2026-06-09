{
  "pass": true,
  "summary": "第23集单场景分镜格式正确、台词忠实、时长合理，无硬问题。",
  "checked_groups": ["第1组"],
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
      "evidence": "4段台词：周美娟9字/3秒=3.0字/秒，赵强17字/3秒=5.67字/秒，周建国23字/5秒=4.6字/秒，周美娟18字/4秒=4.5字/秒，均未超过6.5字/秒硬上限。赵强段5.67字/秒略快但未超限。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "evidence": "单一物理空间城中村出租屋，无跨场景。组首空间锁定列出三人画面位置、身体朝向和关键道具，无过程动词，符合静态结果态要求。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本5句台词全部保留，顺序和说话对象未变。周美娟兴奋、赵强贪婪、周建国冷笑转阴险、周美娟附和，情绪递进完整。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "全部为画面内现场开口对白，无心声/画外音/电话音，每句写明说话人和对象。",
      "fix_instruction": "无需修改，口型和声音来源均正确。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "15秒组含4个台词强节拍+轻反应，总计约5个强节拍，未超过5.5拍上限。每个时间段只承载一个主动作/连续对话节拍。",
      "fix_instruction": "无需修改，强节拍密度合理。"
    },
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "仅一组，无组间衔接问题。组内三人位置稳定，无跳变。",
      "fix_instruction": "无需修改，单组无衔接问题。"
    },
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "铁架床、折叠桌、折叠椅为静态场景道具，无归属变化，无需过渡。",
      "fix_instruction": "无需修改，道具状态稳定。"
    },
    {
      "group": "第1组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "4个时间段各承载一个主动作/对话节拍，无动作过载。",
      "fix_instruction": "无需修改，每个时间段动作清晰。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "本组为普通对话组，无复杂动作/保护站位/关键道具操作，省略视频禁止项合理。",
      "fix_instruction": "无需修改，对话组省略视频禁止项符合规则。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第1组",
      "rule": "dialogue_pacing",
      "problem": "赵强段3秒承载17字（5.67字/秒），接近偏快区间但未超6.5硬上限。",
      "evidence": "光要钱不够，必须逼她把欠税的窟窿补上！= 17字 ÷ 3秒 = 5.67字/秒",
      "fix": "如需更舒适可延长至3.5秒，但当前在可接受范围内。"
    }
  ]
}
