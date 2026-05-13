{
  "pass": true,
  "summary": "seg03 已审核堂屋追问、爷爷糊涂、天天退回卧室、旧木柜老照片和照片背字，横屏调度、夜间光源和运镜设计均满足规则。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组"],
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
    "camera_motion": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "保留天天追问“爷爷，它到底是什么？为什么它会画龙舟？”，爷爷清明消散，并转入“龙舟？端午快到了，鼓还没擦干净。”"
    },
    {
      "group": "第2组",
      "type": "blocking_continuity",
      "evidence": "爷爷留在画面左侧堂屋中央，天天抱水壶从右侧退向右后方卧室门，组尾与后续爷爷独处堂屋衔接。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "拐杖、旧木柜、抽屉和泛黄老照片的动作链清楚：摸索到柜前、拉开抽屉、取出照片、揭示年轻爷爷举鼓槌。"
    },
    {
      "group": "第4组",
      "type": "filmability",
      "evidence": "“云溪龙舟队，最后一场”以照片背面真实手写字呈现，属于剧情道具信息，不是字幕或工程文字。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "天天对画面左侧爷爷追问，爷爷对画面右侧天天回应，现场对白对象明确。",
      "fix_instruction": "若不通过，应写明说话人面对的具体人物和左右站位。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "组尾天天退回右后方卧室，爷爷独自留在左侧堂屋，下一组组首堂屋只剩爷爷一人，状态连续。",
      "fix_instruction": "若不通过，应补充天天离场方向或爷爷留在堂屋的位置。"
    },
    {
      "group": "第3组",
      "type": "camera_motion",
      "result": "pass",
      "evidence": "后拉用于显示空堂屋，横向跟拍用于爷爷摸索到柜前，固定近景用于照片取出，推近用于揭示鼓槌照片，目的具体。",
      "fix_instruction": "若不通过，应把空泛运动改为跟随爷爷、抽屉或照片的具体目标。"
    },
    {
      "group": "第4组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终文本未出现模板编号、参考图、首尾帧、视频延长或自动分镜等工程词；照片文字来自原剧本中的实物道具。",
      "fix_instruction": "若不通过，应删除工程词，并保留道具内真实可见文字。"
    }
  ],
  "issues": [],
  "warnings": []
}
