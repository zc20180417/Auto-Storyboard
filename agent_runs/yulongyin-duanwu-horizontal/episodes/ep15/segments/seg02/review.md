{
  "pass": true,
  "summary": "seg02两组已完成横屏审核，裂缝不可补、野牛颈皮条件、云宝撞壶指向别墅和天天说明牛皮位置均与原剧本一致。",
  "checked_groups": [
    "第1组",
    "第2组"
  ],
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "爸爸冲到巨大牛皮鼓前看到裂缝，连续问“不能补吗？用胶水或者缝起来！”，爷爷两句解释不响和深山野牛颈皮条件均保留。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "爸爸焦急台词约14字/3秒，爷爷第一句约13字/3秒，爷爷第二句约23字/5秒，均未超过6.5字/秒硬上限。"
    },
    {
      "group": "第2组",
      "type": "horizontal_composition",
      "evidence": "天天和水壶在左前景，爸爸在右侧鼓前，祠堂门在右后方，云宝小爪子从左前景指向右后方门外，宽画幅方向明确。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "evidence": "天天最后一句写为对爸爸和爷爷说道，两名听者均在背景转向门口，现场对白对象明确。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "timing_math",
      "result": "pass",
      "evidence": "第1组总时长13秒，0-2、2-5、5-8、8-13秒连续，镜头数4个与标题一致。",
      "fix_instruction": "若不通过，应重新分配镜头时长并保持最后一段结束于13秒。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定巨鼓在右侧、爸爸从左侧冲向鼓前、爷爷左后、天天左前，关键人物和裂缝位置完整。",
      "fix_instruction": "若不通过，应补齐爸爸、爷爷、天天和裂缝的左右前后关系。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "水壶从天天怀里剧烈晃动，到云宝撞壶并伸爪指向祠堂门外，关键道具和动作路径没有跳变。",
      "fix_instruction": "若不通过，应补充水壶从怀中到壶口指向的可见过渡。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "12秒内只承载水壶晃动、云宝撞壶、指向门外和天天解释四个节拍，动作与台词分段清楚。",
      "fix_instruction": "若不通过，应拆分云宝指向和天天解释，或压缩非关键反应。"
    }
  ],
  "issues": [],
  "warnings": []
}
