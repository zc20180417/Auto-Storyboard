{
  "pass": true,
  "reviewer_source": "storyboard-horizontal-reviewer",
  "summary": "已对照第4集4-2原剧本和横屏生成规则审核，三组完整呈现天天护壶、云宝苏醒喷水雾、泥水结冰、胡永贵摔倒、水管脱手与天天接水离开的动作链，未发现阻断交付的硬问题。",
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
    "camera_motion": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "evidence": "水壶从组首就在天天胸前和地面之间，云宝的睁眼、旋转和喷水雾都发生在同一水壶内部，奇幻效果来源明确。"
    },
    {
      "group": "第2组",
      "type": "camera_motion",
      "evidence": "0-3秒低位摇向从水壶雾线到泥水，3-5.5秒推近鞋底薄冰，8.5-12秒跟随摔倒后停在水管落点，运镜服务来源、路径和结果。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "胡永贵骂天天的台词放在5.5-8.5秒，并有低头看冰、转向天天的动作承载，未超过6.5字/秒硬上限。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "evidence": "第2组尾水管脱手落在中央，第3组首水管喷头仍在中央地面，天天从左前景扑向喷头，前后道具状态连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "filmability",
      "result": "pass",
      "evidence": "云宝苏醒被转译为水壶内近景、涟漪、转圈和雾线，不依赖抽象灵力说明，可直接生成。",
      "fix_instruction": "无需修改；若增加效果，应继续写清来源和路径。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "雾线从左前景水壶到中央泥水，泥水再到胡永贵脚下薄冰，胡永贵摔倒后水管落到中央，状态链完整。",
      "fix_instruction": "无需修改；如调整镜头，需保留水壶、泥水、薄冰、水管落点四个锚点。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留天天眼疾手快接住水管、将清水注满水壶、兴奋说“走！我们回家！”的动作和台词，没有改变剧情结果。",
      "fix_instruction": "无需修改；不得把接水动作省略成结果陈述。"
    },
    {
      "group": "第3组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "胡永贵倒在右前景，水管在中央，天天从左前景到中央，右失控、中央道具、左得手的横向关系清楚。",
      "fix_instruction": "无需修改；后续若接离开广场，应保持天天离开方向和皮卡位置一致。"
    }
  ],
  "issues": [],
  "warnings": []
}
