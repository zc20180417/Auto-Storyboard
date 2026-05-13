{
  "pass": true,
  "summary": "第6-7组保留保镖失去战斗力、龙万山追问、陆凡宣告龙家罪行、龙天傲提示商会直升机、龙万山拨打加密电话求援，审核通过。",
  "checked_groups": ["第6组", "第7组"],
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
      "group": "第6组",
      "type": "script_fidelity",
      "evidence": "四名保镖砸在红木家具上、龙万山问来头、陆凡指出商业垄断和非法恶性竞争、龙天傲提到商会重装直升机均保留。"
    },
    {
      "group": "第7组",
      "type": "prop_continuity",
      "evidence": "加密电话从龙万山衣袋中掏出并拨号，再贴到耳边通话，关键道具可操作状态完整。"
    },
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "evidence": "龙万山电话台词约29字分配6秒，字秒比约4.8；前一句约18字分配3.5秒，字秒比约5.1，均未超过硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第6组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "龙万山对陆凡问，陆凡对龙万山说，龙天傲对龙万山提醒，现场对白对象明确。",
      "fix_instruction": "若不通过，应补足说话对象并避免把电话音或画外音写成现场口型。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "电话内容由龙万山现场对电话另一端喊出，画面有加密电话载体，不存在无来源声音。",
      "fix_instruction": "若不通过，应写明电话载体或改成现场对白。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾部四名保镖全部倒地，第6组组首复述保镖倒在红木家具周围，陆凡仍面向龙万山。",
      "fix_instruction": "若不通过，应补齐倒地保镖、陆凡和龙万山的起始位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
