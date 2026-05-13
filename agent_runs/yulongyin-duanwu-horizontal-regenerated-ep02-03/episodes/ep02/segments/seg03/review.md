{
  "pass": true,
  "summary": "seg03已完成小龙入壶、卧室安置、灰白尾巴自责和龙舟线索揭示，人物称谓、道具文字规则和物理连续性均通过。",
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
    "narrative_progression": "checked",
    "asset_scope": "checked",
    "special_effects": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "physical_continuity",
      "evidence": "第1组先让小龙完全进入壶底，再把壶身竖正并拧盖，之后水壶端正放到书桌，液体和容器状态连续。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "第2组保留小龙蜷缩在水壶底、灰白尾巴刺眼、天天说“都怪我没早点发现那些黑水有毒”和小龙睁眼回应。"
    },
    {
      "group": "第3组",
      "type": "prop_text",
      "evidence": "龙舟信息由壶壁湿痕轮廓和天天“这是一个……龙舟？”台词共同表达，不依赖可读文字。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "第3组三句台词分别安排3秒、4秒、4秒，均低于6.5字/秒硬上限，并有反打或双主体镜头承载口型。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "水壶从裂缝边到卧室一直由天天持有，壶内清水留在底部，小龙进入后盖子状态明确。",
      "fix_instruction": "若不通过，应补足水壶由谁持有、是否竖正、盖子何时拧紧以及壶内水位。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "天天在壶外左侧可见，小龙在壶内右侧可见，台词对象明确为壶里的小龙。",
      "fix_instruction": "若不通过，应明确天天对壶里的小龙说话，并保持小龙可见或以壶内青蓝影子承载。"
    },
    {
      "group": "第3组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "第3组未出现参考图、首帧、尾帧、模型自动处理或字幕说明，龙舟轮廓不是道具文字。",
      "fix_instruction": "若不通过，应删去工程说明和可读文字，改用湿痕形状加人物台词表达。"
    },
    {
      "group": "第3组",
      "type": "narrative_progression",
      "result": "pass",
      "evidence": "壶壁第一道弧线延续为龙舟轮廓，天天从误解吃东西到识别龙舟再追问找船，信息推进清楚。",
      "fix_instruction": "若不通过，应补足线条成形和天天理解过程，避免直接跳到结论。"
    }
  ],
  "issues": [],
  "warnings": []
}
