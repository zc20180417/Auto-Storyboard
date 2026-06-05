{
  "pass": true,
  "summary": "seg02完整保留沈清索要合同、电子凭证和刘美娟用野鸡传单糊弄的过程，道具传递清楚且无硬问题。",
  "checked_groups": ["第4组", "第5组", "第6组"],
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
      "type": "script_fidelity",
      "evidence": "保留沈清要求“合同和收益单”、刘美娟称合同在保险柜、沈清要求打开手机银行APP三处关键台词。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "evidence": "名牌包在组首挂在刘美娟左臂，0-7秒完成翻找并取出皱巴巴广告宣传单，7-10秒传单递到沈清面前。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "沈清14字质问用3秒、22字追问用4.5秒，均在6.5字/秒以内，最后0.5秒只承载短反应。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈清与刘美娟的三句现场对白均明确写为对刘美娟或对沈清说，没有假对象。",
      "fix_instruction": "若不通过，应逐句补充真实对话对象。"
    },
    {
      "group": "第5组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "翻包、取出传单、递传单并说话分段呈现，单段主动作明确。",
      "fix_instruction": "若不通过，应拆分翻找和递出传单。"
    },
    {
      "group": "第6组",
      "type": "filmability",
      "result": "pass",
      "evidence": "不知名小公司野鸡理财通过皱巴巴广告宣传单、廉价印刷和沈清台词呈现，没有依赖抽象判断。",
      "fix_instruction": "若不通过，应把不可视判断改成纸面、印章、签字等可见细节。"
    },
    {
      "group": "第6组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第6组关键风险锚定广告宣传单、周桂兰、赵强和沈清手中的宣传单，共3项且不与剧情矛盾。",
      "fix_instruction": "若不通过，应替换成具体人物和道具锚点。"
    },
    {
      "group": "第4组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模型说明词、官方模板编号、@图片/@视频/@音频占位或模板化批量句。",
      "fix_instruction": "若不通过，应删除污染文本。"
    }
  ],
  "issues": [],
  "warnings": []
}
