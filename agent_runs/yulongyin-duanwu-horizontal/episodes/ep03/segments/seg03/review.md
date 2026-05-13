{
  "pass": true,
  "summary": "seg03已逐项审核，天天追问、爷爷糊涂认错、退回房间、旧照片和云溪龙舟队线索均忠于原剧本。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组"
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
      "evidence": "天天追问小龙是什么、为什么会画龙舟，爷爷清明消散后说端午和鼓，台词原文与顺序均保留。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "evidence": "上组天天在右侧门边抱壶，本组仍从右侧门边承接，随后退回房间；爷爷留在左侧堂屋，站位连续。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "爷爷从旧木柜抽屉中翻出泛黄老照片，照片正面年轻爷爷和鼓槌在9-12秒展示，道具来源明确。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "“三十年了……云中君的影子。”约11字承载3.5秒，低语状态下节奏合理，照片背面字迹另用4秒展示。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "天天在画面右侧、爷爷在画面左侧延续前一场对峙轴线，二人视线左右相对，没有无过渡换边。",
      "fix_instruction": "若不通过，应补充从卧室门边进入堂屋的中性过渡或保持左右站位。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载爷爷认错人、天天叹气、抱壶退回房间和爷爷独留堂屋，动作链清楚且13秒内不过载。",
      "fix_instruction": "若不通过，应拆出天天退回房间或删去非必要停顿。"
    },
    {
      "group": "第3组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "爷爷从左侧空堂屋摸索到旧木柜，抽屉和照片在横屏中形成左到中的动作路线，空间调度明确。",
      "fix_instruction": "若不通过，应补充旧木柜、抽屉、爷爷移动路线和照片位置。"
    },
    {
      "group": "第4组",
      "type": "filmability",
      "result": "pass",
      "evidence": "云溪龙舟队线索通过照片背面字迹和爷爷低语呈现，抽象历史信息转译为可见道具与声音。",
      "fix_instruction": "若不通过，应把历史线索落到照片、字迹或可见反应上。"
    },
    {
      "group": "第4组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模板编号、占位符、工程词或批量化套话，保持自然短剧分镜格式。",
      "fix_instruction": "若不通过，应删除污染词并改成现场动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
