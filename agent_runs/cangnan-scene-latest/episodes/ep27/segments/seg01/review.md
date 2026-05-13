{
  "pass": true,
  "summary": "seg01 保留物资抵达、工人复工、江若晴追问和陆凡宣告清算三大豪门的完整剧情链，分组时长和对白承载可交付。",
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "保留集装箱打开、钢筋建材堆积、工人甲欢呼、陆凡命令所有班组开动以及挖掘机推土机轰鸣复工的顺序。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "2-5秒承载工人甲约19字欢呼，字秒比约6.3；5-9秒承载陆凡约20字命令，字秒比约5.0，均未超过6.5硬上限。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "组首锁定黑风山主干道、建材堆、机械、陆凡、江若晴和背景工人位置，全部对白人物第一帧可用。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "江若晴两句追问和陆凡关于重点项目、三大豪门总账的两句回应均按原顺序保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "物资展示、工人欢呼、陆凡命令和机械复工分为4段共13秒，没有把后续江若晴追问硬塞入同组。",
      "fix_instruction": "若不通过，应拆出江若晴追问或压缩非关键环境镜头。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "江若晴每句都明确对陆凡问或说道，陆凡也明确对江若晴说道，没有假对象或无对象对白。",
      "fix_instruction": "若不通过，应补充真实对话对象。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾工地继续施工、陆凡站在建材堆前；第2组首复述建材、机械、陆凡和工人状态，空间连续。",
      "fix_instruction": "若不通过，应在第2组组首补工地和人物状态。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、参考模板、占位符、自动分镜或字幕工程词。",
      "fix_instruction": "若不通过，应删除工程污染词并改写为自然画面。"
    }
  ],
  "issues": [],
  "warnings": []
}
