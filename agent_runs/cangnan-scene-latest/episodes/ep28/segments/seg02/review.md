{
  "pass": true,
  "summary": "seg02保留办公室破门、江若晴质问、毒刺问好和逼迫带走，落地窗风雨作为本段结尾冲击处理。",
  "checked_groups": ["第3组", "第4组"],
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
      "type": "script_fidelity",
      "evidence": "江若晴核对账目、特种玻璃门被砸碎、江若晴惊呼“你们是什么人！”、毒刺手电直射并说“龙少向您问好，江女士。”均已保留。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "江若晴“龙天傲简直疯了！这里是国内！”约15字用3秒，约5字/秒；毒刺“我们拿钱办事，走吧，别逼我动粗。”约17字用4秒，约4.25字/秒，均不过快。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "第3组毒刺持强光手电进入，第4组组首继续持有手电并收低手电逼近，碎玻璃和办公桌位置连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首明确江若晴在办公桌后、毒刺在门外暗处、账目文件和特种玻璃门的位置，人物入场前状态可生成。",
      "fix_instruction": "若毒刺不可用，应在组首写明其位于门外或在镜头中先入场。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "该组承载两句对峙、毒刺伸手抓肩、落地窗破裂风雨灌入，分4段13秒，动作和台词没有压缩进同一短段。",
      "fix_instruction": "若仓促，应拆出抓肩和落地窗破裂为独立组。"
    },
    {
      "group": "第4组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模板编号、参考图、模型自动、字幕或广告式文字，尾部仅保留通用画面风格和负面提示。",
      "fix_instruction": "若出现工程词，应删除并改为自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
