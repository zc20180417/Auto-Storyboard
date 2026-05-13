{
  "pass": true,
  "summary": "seg03两组已完成审核，别墅院、野牛皮标本、胡永贵与包工头对白以及大铁门巨响均符合原剧本和横屏调度要求。",
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
      "type": "horizontal_composition",
      "evidence": "胡永贵位于右侧藤椅高位，包工头在左侧低位奉承，野牛皮标本挂在背景中央，铁门位于左后方，横屏空间目标清楚。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "胡永贵躺藤椅盘核桃、墙上巨大完整野牛皮标本、包工头说中午和李燃求雨失败的台词均按原剧本出现。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "胡永贵“废话！这年头谁还信敲破鼓能下雨。”约18字/4秒，“等过了十二点，我亲自去收他的命！”约17字/3.5秒，节奏可表演。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "大铁门巨响写为门板猛震、门缝爆光和人物回头反应，声音来源有可见载体。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "野牛皮标本从组首背景中央建立，到第2组继续保持背景中央位置，是后续爸爸闯入目标的稳定道具。",
      "fix_instruction": "若不通过，应在两组组首都固定野牛皮位置和可见状态。"
    },
    {
      "group": "第2组",
      "type": "timing_math",
      "result": "pass",
      "evidence": "第2组总时长14秒，0-4、4-7.5、7.5-11、11-14秒连续，镜头数4个与标题一致。",
      "fix_instruction": "若不通过，应调整时间段至0.5秒粒度并确保合计14秒。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾胡永贵看向铁门，第2组首仍在右侧藤椅上面对左侧包工头和门位，直到门在左后方巨响，空间连续。",
      "fix_instruction": "若不通过，应补充胡永贵从躺到半坐起和铁门方位的过渡。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "分镜正文未出现模板编号、参考图、首尾帧、视频延长或自动生成说明，仍是自然短剧分镜文本。",
      "fix_instruction": "若出现工程词，应删除并改成可见动作、声音来源或光影描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
