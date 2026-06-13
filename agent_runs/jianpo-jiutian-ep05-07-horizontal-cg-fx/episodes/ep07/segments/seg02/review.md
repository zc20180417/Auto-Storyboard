{
  "pass": true,
  "summary": "已对照第7集7-2脚本、横屏生成规则和3D CG视觉规则复审，2组保留天字一号包厢、太乙神芝亮相、拍卖师底价、沐清寒救父希望和一百五十万两首次竞价，未发现阻断交付问题。",
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
    "visual_peak": "checked",
    "special_effects": "checked",
    "genre_style": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组保留包厢可俯瞰大厅、拍卖师揭开锦盒、血色太乙神芝、底价一百万两和沐清寒救父台词，未改剧情因果。"
    },
    {
      "group": "第1组",
      "type": "special_effects",
      "evidence": "第1组1-2把太乙神芝的青金灵光和药香流光绑定在锦盒与灵芝本体，光影说明只照亮手指和桌面，不形成法阵。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "第2组承接上一组竞价铃在沐清寒右手边，2-1写按下竞价铃，2-2报价后组尾仍保留竞价铃停在手边。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "第1组写明包厢在画面上方左侧、展台在下方中央，陆渊在沐清寒后侧，拍卖师与锦盒是大厅焦点，16:9空间层次清楚。",
      "fix_instruction": "若不通过，应补充包厢、展台、人物和锦盒的上下左右关系。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "拍卖师底价台词安排4秒，沐清寒救父台词安排3秒，均低于6.5字/秒硬上限，口型可承载。",
      "fix_instruction": "若不通过，应拆镜或延长台词镜头，不能压缩关键台词。"
    },
    {
      "group": "第2组",
      "type": "camera_motion",
      "result": "pass",
      "evidence": "第2组用焦点转移从沐清寒眼神落到竞价铃，之后稳定近中景承载一百五十万两报价，短组有明确道具落点。",
      "fix_instruction": "若不通过，应补充焦点转移或急停落点，同时保留稳定口型镜头。"
    }
  ],
  "issues": [],
  "warnings": []
}
