{
  "pass": true,
  "summary": "seg02已完成仓库段真实审稿，鱼干危机、重打包决策和拍照动作均按原剧本保留。",
  "checked_groups": ["第3组", "第4组", "第5组"],
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
      "group": "第3组",
      "type": "filmability",
      "evidence": "剧本中的腥臭味没有作为不可视信息单独承载，而是转译为两人停住呼吸、鱼干发白发灰和潮湿竹筐。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "第4组四段对白分别为4秒、4秒、3秒、4秒，单段有效台词均低于6.5字/秒，陆凡站起动作有4-8秒承载。"
    },
    {
      "group": "第5组",
      "type": "timing_math",
      "evidence": "第5组0-2秒、2-6秒连续相加为6秒，标题总时长6秒、镜头数2个一致，属于手机拍照道具插入短组。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "推门、鱼干发霉、牛大春痛心和陆凡判断只是受潮均与原剧本一致。",
      "fix_instruction": "若后续删掉发霉鱼干或受潮判断，应恢复对应动作和台词。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第4组集中在同一仓库内的压价说明、组织挑拣、疑问和陆凡承诺，15秒内四个轻中节拍清楚。",
      "fix_instruction": "若加入村民入场或实际打包动作，应拆分到新组。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾部陆凡站在鱼干筐前接下销路，第5组组首延续仓库站位，再由他从口袋取出手机拍照。",
      "fix_instruction": "若手机提前出现在手中，应补充取出或持有状态。"
    },
    {
      "group": "第5组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "第5组只写手机拍照和鱼干纹理，没有参考图、模型说明或模板编号。",
      "fix_instruction": "若出现参考图或工程占位词，应删除并改成自然镜头动作。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第5组",
      "rule": "timing_math",
      "problem": "第5组为6秒短组。",
      "evidence": "该组只承载陆凡拿出手机并拍下鱼干照片，属于道具插入和销路动作铺垫，短组理由成立。",
      "fix": "最终交付时可保留；不要为凑10秒增加无关凝视或仓库展示。"
    }
  ]
}
