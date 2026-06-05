{
  "pass": true,
  "summary": "seg03 保留周美娟和赵强上铐、周美娟狡辩、警察以十九万证据驳回、沈清补刀和三名反派被带离，未发现 hard issue。",
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
      "type": "prop_continuity",
      "evidence": "手铐从警察乙手中到周美娟腕上，另一副由带队警察扣到赵强腕上，组尾明确两人均戴着手铐。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "警察原台词中的非法侵占高达十九万、证据确凿和回局里跟预审员说均保留；沈清法律只看偷钱的台词也保留。"
    },
    {
      "group": "第3组",
      "type": "action_atomicity",
      "evidence": "周美娟赵强被带向出口、母女不追、保镖带走周建国分成三个时间段，避免多人物押送动作混在一镜。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "周美娟约18字抗辩用4秒，约4.5字/秒；前后有上铐与控制动作支撑，未超速。",
      "fix_instruction": "若不通过，应延长台词段或拆出上铐动作。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组包含警察宣告证据、沈清回应和周美娟被控制准备带离，三段强节拍在12秒内各有清楚表演时间。",
      "fix_instruction": "若不通过，应把准备带离拆到下一组或压缩轻反应。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组组尾写两人戴铐被警察控制、沈清周桂兰在左后方；第3组组首继承该状态并加入周建国、张总和保镖位置。",
      "fix_instruction": "若不通过，应补足周美娟、赵强、周建国的组首站位和道具状态。"
    },
    {
      "group": "第3组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定周美娟、赵强、保镖、沈清和强制执行诉状，限制错误押送对象和道具消失，数量为4条。",
      "fix_instruction": "若不通过，应替换无锚点泛泛词或删除与正文冲突的禁止项。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模型说明、模板套话、参考图占位符或非短剧模板语气。",
      "fix_instruction": "若不通过，应改成自然可视动作和声音描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
