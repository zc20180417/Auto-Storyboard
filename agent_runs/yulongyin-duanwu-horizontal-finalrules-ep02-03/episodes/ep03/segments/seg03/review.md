{
  "pass": true,
  "summary": "seg03 passed: Tiantian's retreat, grandfather's confusion, and the old-photo dragon-boat clue preserve the script and avoid relying on generated tiny text.",
  "source_status": "script_provided",
  "checked_groups": ["第1组", "第2组"],
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
    "prop_continuity": "checked",
    "physical_continuity": "checked",
    "special_effects": "checked",
    "genre_style": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组保留天天追问“它到底是什么？为什么它会画龙舟？”以及爷爷糊涂后的两句台词。"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "evidence": "第2组旧照片正面先显示年轻爷爷坐在龙舟船头、高举鼓槌，背面旧字只作道具纹理，关键信息由爷爷念出。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "第2组从旧木柜抽屉翻出泛黄老照片，再翻到背面，照片来源和正反面状态都有可见动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "天天保持右侧抱壶，爷爷在左侧堂屋入口，天天朝右后方退回卧室，方向和门框参照清楚。",
      "fix_instruction": "若不通过，应补充画面左/右/前/后的方向和中性过渡。"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "照片背面文字不作为唯一信息来源，爷爷明确念出“云溪龙舟队，最后一场”。",
      "fix_instruction": "若不通过，应让人物念出或通过动作反应同步表达道具文字信息。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "第2组没有参考图、@图片、字幕说明、模型会处理或模板编号等污染词。",
      "fix_instruction": "若不通过，应删除工程说明、参考图调用语和模板化描述，只保留分镜正文。"
    }
  ],
  "issues": [],
  "warnings": []
}
