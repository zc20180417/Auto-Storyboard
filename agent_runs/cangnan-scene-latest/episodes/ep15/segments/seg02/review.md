{
  "pass": true,
  "summary": "seg02保留陆凡反击、宋子昂嘲讽、直升机到场和龙国商会物流机队信息，格式与空间连续性通过。",
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
      "evidence": "陆凡“你高兴得太早了”“时间差不多了”和宋子昂“全县的机器都被我买断了，你拿手挖吗？”按原顺序保留。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "3-7秒承载宋子昂约19字嘲讽台词，4秒约4.8字/秒；9.5-11秒陆凡短句约6字，1.5秒约4字/秒，节奏可承载。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组仍在黑风山临时车场，组首列明陆凡、宋子昂、江若晴、工头、律师团和集装箱落点，直升机只在上空进入画面。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "直升机旋翼轰鸣写为环境声，人物只抬头反应，没有错误口型承载。",
      "fix_instruction": "若不通过，应标明声音来源或人物闭口反应。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "两架重型运输直升机吊集装箱、宋子昂惊问、陆凡回答“龙国商会专属物流机队”、集装箱落地均保留。",
      "fix_instruction": "若不通过，应恢复缺失的直升机、集装箱或对白信息。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现Seedance、模板编号、参考图、自动分镜或其他工程说明词。",
      "fix_instruction": "若不通过，应删除模型或模板说明词，改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
