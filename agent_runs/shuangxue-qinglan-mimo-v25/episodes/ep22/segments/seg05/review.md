{
  "pass": true,
  "summary": "第5组沈清身份揭晓场景，台词节奏合格，身份揭示情绪递进清楚，结尾自然。",
  "checked_groups": ["第5组"],
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
      "evidence": "周桂兰台词12字/3秒=4.0字/秒，沈清身份揭示34字/5秒=6.8字/秒（情绪对白目标5.2），沈清扶母亲台词18字/4秒=4.5字/秒，均未超6.5字/秒硬上限。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "原剧本三句核心台词完整保留：周桂兰震惊发问、沈清揭示CEO身份和A轮融资、沈清接母亲享福。关键动作（扶母亲上车）完整。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "evidence": "上一组（第4组）尾部车门已打开、司机躬身等候；本组组首车门已打开、司机位于车门旁，状态完全连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "全部台词为画面内真人开口对白，无心声/画外音混用，对话指向正确。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "2个强节拍（身份揭示+扶母亲上车），12秒容量合理，无过载。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第5组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "3个时间段各承载一个对话节拍，非主动作人物（司机）只站立待命不抢动作。",
      "fix_instruction": "无需修改"
    }
  ],
  "issues": [],
  "warnings": []
}

