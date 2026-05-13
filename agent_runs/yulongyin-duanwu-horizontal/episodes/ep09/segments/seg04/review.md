{
  "pass": true,
  "summary": "seg04三组已审核，祠堂震动、天天绝望询问、云宝吐水珠、伤疤青光、外墙倒塌和爸爸抓住鼓槌均按剧本推进，横屏人物与道具衔接清楚。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组"
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
      "evidence": "第1组保留头顶灰尘落下、龙舟震动、天天问“爸爸！我们是不是都要死在这里了？”和云宝爬到爸爸脚边的顺序。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "纯净水珠从云宝口中吐出，落到爸爸右手伤疤，随后青光贯穿手臂，道具和身体接触路径可见。"
    },
    {
      "group": "第3组",
      "type": "horizontal_composition",
      "evidence": "第3组外墙破口在左后方，龙舟在右后方，爸爸居中转向破口怒吼，再向左侧爷爷伸手攥鼓槌，左右空间服务剧情转折。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "天天“爸爸！我们是不是都要死在这里了？”放在3秒绝望询问内，约15字/3秒，情绪对白节奏合理。",
      "fix_instruction": "若不通过，应给天天台词增加反应时间或拆分镜头。"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "温热感和青光被转译为水珠落在伤疤、手指抽动、青光沿手腕一闪而过等可见动作。",
      "fix_instruction": "若不通过，应把抽象治愈感改写成皮肤、光线、动作和人物反应。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "爸爸怒吼“老天爷不给活路，老子就劈开这条路！”后，用布满伤疤的右手攥住爷爷手里的鼓槌，未提前敲鼓或新增动作结果。",
      "fix_instruction": "若不通过，应删除原剧本未发生的敲鼓、唤龙成功或外墙完全倒塌结论。"
    }
  ],
  "issues": [],
  "warnings": []
}
