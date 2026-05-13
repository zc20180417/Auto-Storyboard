{
  "pass": true,
  "summary": "seg03保留龙家封杀令解决、剪彩和卡车出山的关键剧情，台词顺序、道具归属和空间转接通过。",
  "checked_groups": ["第5组", "第6组"],
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
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "江若晴两句问题、陆凡两句回应和共同剪彩动作均按原剧本顺序保留。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "最长台词“你一个人，扳倒了京城顶级财阀？”约16字用3.5秒，约4.6字/秒；未超过硬上限。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "evidence": "第6组为仪式现场与公路远景的庆祝收尾，卡车从新修公路起点驶向山外，属于同一通车仪式动作链的远景展示。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "金剪刀从上一段陆凡手中延续到本组，9-14秒由陆凡和江若晴共同使用剪断红绸。",
      "fix_instruction": "若不通过，应补充金剪刀递交或握持状态。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组为无对白庆祝与车队出山，礼炮、彩带、卡车三个动作分段清楚，12秒内可表演。",
      "fix_instruction": "若不通过，应压缩环境展示或拆出卡车出山远景。"
    },
    {
      "group": "第6组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、参考图、自动分镜、字幕或模型说明词。",
      "fix_instruction": "若不通过，应删除工程词和模板化描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
