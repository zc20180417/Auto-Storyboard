{
  "pass": true,
  "summary": "seg04保留从钱账转向房子账、沈清限时赶人、周美娟和周建国反弹，房屋冲突清楚。",
  "checked_groups": ["第7组", "第8组"],
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第7组",
      "type": "script_fidelity",
      "evidence": "沈清钱账两清、现在算房子账、周建国家的台词和沈清说明亲生父亲留下的房子均保留。"
    },
    {
      "group": "第8组",
      "type": "dialogue_pacing",
      "evidence": "沈清限时台词约16字用3秒，约5.3字/秒；周建国合法丈夫台词约20字用3.5秒，约5.7字/秒。"
    },
    {
      "group": "第8组",
      "type": "handoff_continuity",
      "evidence": "第7组尾沈清面对周建国、金镯子已收起；第8组首延续沈清右侧、周建国中央偏后、周美娟捂腕状态。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "金镯子由沈清隔纸巾持有并收起，后续不再回到周美娟手腕。",
      "fix_instruction": "若不通过，应在组首或动作中补清金镯归属。"
    },
    {
      "group": "第8组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "11秒组承载沈清两句驱逐、周美娟质问、周建国争房四个短句交锋，没有外部动作过载。",
      "fix_instruction": "若不通过，应拆出周建国争房反击或缩短非台词动作。"
    },
    {
      "group": "第8组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明、模板编号、参考图占位符、广告/MV语气或模板化批量描述。",
      "fix_instruction": "若不通过，应删除工程词和模板化描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
