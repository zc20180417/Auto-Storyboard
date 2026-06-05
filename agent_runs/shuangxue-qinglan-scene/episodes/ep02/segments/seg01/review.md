{
  "pass": true,
  "summary": "seg01 已对照原剧本完成审核，转账记录、十九万二、视频电话真相和银行卡来源均保留，未发现阻断生产的硬问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组"],
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
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "沈清关于刘美娟挂断视频和变声器的长台词放在 5-14 秒，约 48 个有效字 / 9 秒，约 5.3 字/秒，未超过 6.5 硬上限。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "evidence": "银行卡从旧棉衣夹层和手帕中取出，经周桂兰递出后转到沈清手中，组尾明确银行卡在沈清手中。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留了胶布老花镜、24个月、每月25号、每月八千和总计十九万二的关键证据链。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首只锁定沈清和周桂兰在杂物间内的位置、朝向、手机和旧木床，未写刘美娟或后续动作。",
      "fix_instruction": "若不通过，应删除组首中的过程动作，只保留第一帧静态状态。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "周桂兰三句崩溃台词都写成对沈清说道或痛哭说道，画面内对白有真实对象。",
      "fix_instruction": "若不通过，应补足说话对象，避免只写台词不写对象。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载两段母女对话和周桂兰短反应，均在同一杂物间同一冲突目标内，没有外部事件或中等动作叠加。",
      "fix_instruction": "若不通过，应把长台词再拆组或减少非关键动作。"
    },
    {
      "group": "第5组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "掀床板、取塑料袋、拆夹层、递卡、接卡反问分成独立时间段，每段只有一个主动作或一段台词。",
      "fix_instruction": "若不通过，应继续拆分取卡和递卡动作。"
    },
    {
      "group": "第5组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定银行卡、周桂兰、刘美娟和旧棉衣夹层，数量为 3 条，没有使用占位项。",
      "fix_instruction": "若不通过，应替换为本组具体人物和道具风险。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、参考图、模型说明词、@图片占位符或模板化批量描述。",
      "fix_instruction": "若不通过，应删除所有工程词和模板描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
