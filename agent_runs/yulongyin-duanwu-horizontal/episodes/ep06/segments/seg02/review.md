{
  "pass": true,
  "summary": "祠堂段完整呈现旧龙舟刮木屑、木屑水吸毒、云宝暂缓和三天期限，横屏构图与道具连续性满足规则。",
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
      "evidence": "原剧本的祠堂正中残破木制龙舟、爷爷用小刀刮船首木屑入碗，以及台词“把它放进去。这是祖宗留的最后一点底子。”均保留。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "第1组尾木屑已入碗，第2组首碗位于供桌中央，天天从右侧把云宝放入碗内，随后木屑变黑并减轻云宝死灰色，关键道具流向清楚。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "爷爷“三天内”台词约20字用4.5秒承载，字秒比约4.4，符合严肃说明的自然语速，没有超过硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "残破龙舟横贯后方，船首靠左，供桌和碗居中，爷爷左侧刮木屑、天天右侧抱云宝，横屏左右和前后层次明确。",
      "fix_instruction": "若不通过，应补足龙舟船首、供桌、碗、天天和爷爷的左右前后位置。"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "毒素被转译成木屑迅速变黑、黑色水纹扩散、云宝死灰色稍退和胸腹起伏变清楚，均为可见变化。",
      "fix_instruction": "若不通过，应把抽象的吸毒效果改为水色、木屑颜色和云宝起伏的可见变化。"
    },
    {
      "group": "第3组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "天天守在右侧护碗，爷爷站左侧对她说三天期限，与第2组爷爷从左后走近供桌的方向连续，未出现无过渡换边。",
      "fix_instruction": "若不通过，应在第2组尾补充爷爷走到左侧供桌边，或在第3组首用中性镜头重建轴线。"
    }
  ],
  "issues": [],
  "warnings": []
}
