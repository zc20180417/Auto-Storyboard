{
  "pass": true,
  "summary": "seg01 保留办公室撞破、重拳殴打、决裂离开的剧情链，分组时长和对白承载可交付。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "evidence": "保留陆凡进门、王建国拉林薇薇手、林薇薇抽回以及“你们在干什么”“你听我解释”“解释什么？无耻之徒！”的台词顺序。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "0-4秒承载王建国和陆凡约13字对话，字秒比约3.25；10-12秒承载“陆凡你疯了”6字，字秒比3，未超过硬上限。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "文件在组首由陆凡持有，8-10秒明确由陆凡砸到办公桌边，文件归属变化有可见过渡。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首写明办公室、门、办公桌以及三人的画面位置和身体朝向，所有说话人物第一帧可用。",
      "fix_instruction": "若不通过，应补充人物位置、朝向和文件/门/桌子的静态状态。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "重拳、摔倒、尖叫被拆成4个时间段，总时长12秒，没有把决裂对白继续塞入同组。",
      "fix_instruction": "若不通过，应继续拆分打斗余波或移出情绪台词。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾王建国倒地、林薇薇站在桌旁、陆凡停在两人面前；第3组首复述这些状态。",
      "fix_instruction": "若不通过，应在第3组组首复述王建国倒地、林薇薇位置和陆凡持文件状态。"
    },
    {
      "group": "第3组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、模板编号、参考图或自动分镜等污染内容。",
      "fix_instruction": "若不通过，应删除工程词并改为自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
