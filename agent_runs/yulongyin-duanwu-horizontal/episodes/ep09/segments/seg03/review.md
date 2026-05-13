{
  "pass": true,
  "summary": "seg03两组已审核，外部履带声、挖掘机进场、胡永贵下令、村民甲阻止和老墙掉灰均完整保留，机器对祠堂的横屏压迫关系明确。",
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
      "type": "audio_mouth_sync",
      "evidence": "履带摩擦声和发动机轰鸣写为画面左侧逼近的环境声，并给出村民甲转头反应，胡永贵现场喊话则由画面左中景人物承载。"
    },
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "evidence": "第1组把祠堂外墙压在画面右后方，挖掘机从左侧进入，胡永贵偏左、村民甲右前景，机器推进方向与威胁目标明确。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "第2组保留胡永贵“给我连墙带船一起推平！”、村民甲“永贵你疯了！里面还有人呢！”以及挖掘机继续推进导致老墙掉灰。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "胡永贵“李燃！你再能打，能扛得住机器吗！”安排在3.5秒疯狂喊话中，约14字/3.5秒，节奏可表演且未超硬上限。",
      "fix_instruction": "若不通过，应延长该喊话镜头或拆出反应镜头。"
    },
    {
      "group": "第2组",
      "type": "blocking_continuity",
      "result": "pass",
      "evidence": "挖掘机从中央偏左向右侧老墙推进，村民甲被迫退到右前景，动作路线和阻挡失败的结果连续。",
      "fix_instruction": "若不通过，应补清机器推进方向和村民甲退让路线。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组强节拍为胡永贵下令、村民甲阻止、机器顶墙掉灰，13秒内用4个镜头分配，未同时塞入额外剧情。",
      "fix_instruction": "若不通过，应拆分机器推进和墙体受损。"
    }
  ],
  "issues": [],
  "warnings": []
}
