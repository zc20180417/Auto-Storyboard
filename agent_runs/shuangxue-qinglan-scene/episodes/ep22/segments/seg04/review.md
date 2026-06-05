{
  "pass": true,
  "summary": "seg04 保留院门外母女对话、豪车到达、司机称呼沈总、CEO身份揭示和扶母亲上车。",
  "checked_groups": ["第9组", "第10组", "第11组", "第12组"],
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
      "group": "第9组",
      "type": "script_fidelity",
      "evidence": "周桂兰看空院、叹气问住哪儿，沈清保留“这破房子早就配不上你了”。"
    },
    {
      "group": "第10组",
      "type": "action_atomicity",
      "evidence": "豪车驶近、停稳、司机下车、司机开门说话分四段，外部事件进入没有压缩进一镜。"
    },
    {
      "group": "第11组",
      "type": "dialogue_pacing",
      "evidence": "周桂兰约17字/4秒，沈清前半句约17字/6秒、后半句约17字/4秒，均未超过6.5字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第10组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "司机在6-9秒下车并站到车门旁，9-12秒才开门说话，人物可用性成立。",
      "fix_instruction": "若不通过，应在司机说话前补入场动作。"
    },
    {
      "group": "第11组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "完整保留“沈总？”、“厂里加夜班”、“创业公司赶项目”、“A轮融资成功”和CEO身份。",
      "fix_instruction": "若不通过，应恢复被删改的身份揭示台词。"
    },
    {
      "group": "第12组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定沈清、周桂兰、司机、豪华轿车车门，避免上车动作和台词归属错误。",
      "fix_instruction": "若不通过，应替换泛泛禁止项并锚定本组人物道具。"
    }
  ],
  "issues": [],
  "warnings": []
}
