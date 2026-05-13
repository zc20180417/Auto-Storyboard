{
  "pass": true,
  "summary": "seg06审核通过，张强威胁离场、纪委调查组进入、封存账目和张强阻挠失败均完整保留。",
  "checked_groups": ["第11组", "第12组"],
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
      "group": "第11组",
      "type": "character_availability",
      "evidence": "纪委干部在组首写为门外近处被门板遮挡，4-7秒明确推门涌入后，7-10秒才开口。"
    },
    {
      "group": "第12组",
      "type": "script_fidelity",
      "evidence": "实名举报、贪污养老金案、封存近五年账目、收缴手机、张强按住抽屉和强制措施警告均按原剧本保留。"
    },
    {
      "group": "第12组",
      "type": "dialogue_pacing",
      "evidence": "8-14秒承载张强与纪委干部两句约34字/6秒，约5.7字/秒，低于6.5硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第11组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第11组13秒内包含张强威胁、调查组入场、身份宣告和众人反应，分成四段，动作顺序清楚。",
      "fix_instruction": "若入场和身份宣告拥挤，应把苏有光反应并入下一组。"
    },
    {
      "group": "第12组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "抽屉在组首位于张强手边，张强先贴近抽屉再死死按住，账本和手机由工作人员封存收缴，归属变化可见。",
      "fix_instruction": "若道具突然被拿走，应补封条、伸手示意或张强松手的过渡。"
    },
    {
      "group": "第12组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "纪委干部对在场众人、对工作人员、对张强的命令和警告对象明确，张强对纪委干部开口对象明确。",
      "fix_instruction": "若对象缺失，应补充对在场众人、工作人员或张强说道。"
    }
  ],
  "issues": [],
  "warnings": []
}
