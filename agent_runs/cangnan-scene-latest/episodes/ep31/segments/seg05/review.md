{
  "pass": true,
  "summary": "第8-9组保留直升机盘旋、纠察员涌入、龙万山误判支援、商会总管佩徽章入场并质问、龙万山指认陆凡等关键内容，审核通过。",
  "checked_groups": ["第8组", "第9组"],
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
      "group": "第8组",
      "type": "script_fidelity",
      "evidence": "五架商会专属物流直升机、黑色制服纠察员踹开围墙涌入、龙万山大笑“跨国财团的支援到了！你完了！”均按原剧本呈现。"
    },
    {
      "group": "第9组",
      "type": "dialogue_pacing",
      "evidence": "商会总管约22字台词分配5秒，龙万山约20字台词分配4秒，字秒比约4.4和5，均在可承载范围内。"
    },
    {
      "group": "第9组",
      "type": "space_locking",
      "evidence": "组首明确大院单一物理空间，陆凡、龙万山、商会总管和纠察员位置朝向清楚，徽章作为道具可见。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第8组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第8组10秒只承载直升机压场、纠察员入场和龙万山一句狂喜台词，强节拍数量可控。",
      "fix_instruction": "若不通过，应拆出纠察员入场或压缩环境镜头。"
    },
    {
      "group": "第9组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "商会总管对龙万山说道，龙万山对商会总管喊道，台词对象明确且没有假对象。",
      "fix_instruction": "若不通过，应补充真实对话对象。"
    },
    {
      "group": "第9组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文无模板编号、参考图、模型词、字幕或广告式文案，徽章和直升机均为剧本内可见物。",
      "fix_instruction": "若不通过，应删除污染词并恢复短剧自然分镜。"
    }
  ],
  "issues": [],
  "warnings": []
}
