{
  "pass": true,
  "summary": "seg01已对照原剧本和横屏规则完成审核，三组均保留送水车、皮卡、水管和水壶的左右归属，未发现hard issue。",
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
      "type": "horizontal_composition",
      "evidence": "送水车在左、皮卡在右、天天在右后方队尾，胡永贵从右向左插队，横屏左右关系清楚。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "水管从左侧送水车被胡永贵夺到右侧皮卡旁，泥水从皮卡方向流向队伍脚边，后续冲突可承接。"
    },
    {
      "group": "第3组",
      "type": "camera_motion",
      "evidence": "每个时间段都有运镜设计，固定机位说明了对白口型、水管归属和天天跌倒方向，移动镜头跟随抢水路线。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留送水车排队、天天抱水壶在最后、胡永贵插队并说原台词的剧情顺序。",
      "fix_instruction": "若后续改稿，仍需保留胡永贵从皮卡方向闯入并抢占水源的因果。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "村民甲质问放在3.5秒，胡永贵反驳放在4.5秒，字秒比在可表演范围内。",
      "fix_instruction": "若压缩时长，不要压短这两句对话口型。"
    },
    {
      "group": "第3组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "天天由右后方向中央冲，胡永贵始终在右前景，推倒后天天落到左前方，动作轴线连续。",
      "fix_instruction": "若调整镜头，不要让胡永贵无过渡换到画面左侧。"
    }
  ],
  "issues": [],
  "warnings": []
}
