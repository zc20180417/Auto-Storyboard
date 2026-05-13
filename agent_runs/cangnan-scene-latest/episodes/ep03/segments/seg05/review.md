{
  "pass": true,
  "summary": "seg05审核通过，陆凡回到大厅、刘波喝止张强、宣读副主任任命和陆凡反击均完整保留。",
  "checked_groups": ["第9组", "第10组"],
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
      "group": "第9组",
      "type": "dialogue_pacing",
      "evidence": "10-15秒刘波连续宣读两句约31字/5秒，约6.2字/秒，低于6.5硬上限且属于正式宣读的快速信息节拍。"
    },
    {
      "group": "第10组",
      "type": "script_fidelity",
      "evidence": "全场错愕、张强质疑、刘波反问、张强哑火、陆凡微笑请多指教，均与原剧本一致。"
    },
    {
      "group": "第9组",
      "type": "character_availability",
      "evidence": "陆凡和刘波在门口近处，张强在办公桌旁；刘波在宣读前有大步走到中央的入场和站位过渡。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第9组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组15秒承载陆凡进门、张强怒斥、刘波喝止和宣读任命，动作与对白分段明确，没有超过模型硬时长。",
      "fix_instruction": "若宣读显得过快，应把宣读任命拆入下一组，但当前字秒比未超硬上限。"
    },
    {
      "group": "第10组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "张强对刘波、刘波对张强、陆凡对张强的对白对象均明确。",
      "fix_instruction": "若对象缺失，应补为具体人物而非泛泛说话。"
    },
    {
      "group": "第10组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第9组尾部刘波宣读任命、陆凡门内、张强办公桌旁，第10组组首复述三人位置并接全场反应。",
      "fix_instruction": "若位置跳变，应补充陆凡、刘波或张强的移动状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
