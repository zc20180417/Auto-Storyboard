{
  "pass": true,
  "summary": "两组分镜忠实还原原剧本对白和动作，台词指向明确，时空连续，道具状态清晰，无硬问题。",
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
      "evidence": "沈清14字/3秒=4.67字秒比，周美娟6字/2秒=3.0，赵强8字/3秒=2.67，均未超过6.5硬上限，情绪对白未低于4.5下限（周美娟崩溃喊叫属极短反应句，3.0可接受）。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "两组均在周家正屋客厅，单一物理空间。组2组首空间锁定与组1组尾衔接一致：赵强已起身、沈清仍举手机、周美娟仍挡脸。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "五句对白全部保留原文，说话对象正确（沈清→周美娟、周美娟→沈清、赵强→沈清）。关键道具录像手机贯穿两组，状态从沈清举起到赵强抓住，有可见过渡。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "全部对白为画面内真人现场开口，每句均写明说话人和对象。周美娟喊叫时沈清画外音尾音描述合理（前一镜头沈清刚说完话，尾音自然延续）。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "组2为6秒短动作余波，只承载赵强冲出+抓手机一个完整复合动作链和一句对白，强节拍2个（动作+对白），无过载。10字/2秒=5.0字秒比合格。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "组1组尾写明赵强从桌边起身、沈清仍举手机、周美娟双手仍挡在面前。组2组首复述赵强已起身在画面中央、沈清举手机、周美娟双手挡面前。人物位置、道具状态、朝向均连续。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "录像手机从组1沈清右手举起，到组2赵强伸手抓住沈清手中手机和手腕，有明确可见过渡动作。手机未消失或跳变。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "组2每个时间段只有一个主动作：0-3秒赵强冲出+喊话，3-6秒赵强抓手机。周美娟尖叫为画外音，不占主动作。非主动作人物沈清只展示手腕被钳住的状态反应。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "组2包含视频禁止项'录像手机消失、赵强直接挥拳打人而非抓手机、周美娟离开原位、沈清提前放下手机'，共4条，均锚定本组人物和道具，无泛泛词。",
      "fix_instruction": "无需修改"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "全文无Seedance可、自动正反打、@图片/@视频/@音频、模板编号等模型说明词或工程词，无模板化批量描述。",
      "fix_instruction": "无需修改"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "generation_density",
      "problem": "6秒短组，虽属短动作余波，但建议在交付说明中确认其作为短承接组的合理性。",
      "evidence": "组2总时长6秒，承载赵强冲出+喊话+抓手机的完整动作链，属短动作余波。",
      "fix": "已确认属于短动作余波，无需修改。"
    }
  ]
}
