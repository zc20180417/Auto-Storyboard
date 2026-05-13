{
  "pass": true,
  "summary": "seg01已对照原剧本4-1完成横屏审稿，插队、洗车、村民质问、天天抢管被推倒均保留，未发现阻断交付的硬问题。",
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
      "type": "horizontal_composition",
      "evidence": "送水车在画面左侧、皮卡在右侧、队伍斜向排到右后方，天天处在队尾，胡永贵从右侧闯入，横屏左右关系和队伍压迫清楚。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "村民甲台词约15字安排3.5秒，胡永贵台词约17字安排4.5秒，均低于6.5字/秒硬上限并保留对话对象。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "天天原句“别浪费水！给我留一点！”保留；她冲上前抢水管、被胡永贵推倒、水壶险些摔碎的动作因果完整。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "胡永贵从画面右侧皮卡方向进入并压向左侧送水车，后续第2组仍保持他在右前景控制水管。",
      "fix_instruction": "若后续换边，应在组尾或组首补充绕车、穿过队伍或中性正面镜头。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "水管从送水车左侧被胡永贵夺到右前景，水流喷向皮卡并形成泥水，位置变化有可见动作。",
      "fix_instruction": "若水管位置跳变，应补充拿起、拖拽、转向或脱手动作。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组13秒承载天天喊话、抢管、被推倒、护住水壶四个连续动作，动作链都围绕同一水管冲突展开，没有额外事件堆叠。",
      "fix_instruction": "若表演显拥挤，应拆出推倒后的水壶险坠为下一组起始。"
    }
  ],
  "issues": [],
  "warnings": []
}
