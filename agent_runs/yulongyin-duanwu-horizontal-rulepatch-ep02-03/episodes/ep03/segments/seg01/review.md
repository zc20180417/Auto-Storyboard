{
  "pass": true,
  "summary": "Segment 3-1 passed: feeding, naming, water mist, title timing, naming state and kettle/lid continuity are clean.",
  "source_status": "script_provided",
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
      "evidence": "Group 1 preserves lock-door, stale bun, feeding crumbs into the upright kettle, small dragon eating, bubbles, and Tiantian dialogue without deleting key beats."
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "Group 2 uses old name before the naming line and only uses Yunbao after the line \"????????\"."
    },
    {
      "group": "第3组",
      "type": "physical_continuity",
      "evidence": "Group 3 establishes the lid being half-screwed back on screen before the group tail says the lid is half-screwed."
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "Dialogue is distributed across 4-second shots and stays under the 6.5 chars/sec hard cap.",
      "fix_instruction": "If failed, repair only the cited group and keep unrelated groups unchanged."
    },
    {
      "group": "第2组",
      "type": "special_effects",
      "result": "pass",
      "evidence": "Yunbao response is limited to bubbles, tail movement and weak blue reflection, with no cartoon or sci-fi laser effect.",
      "fix_instruction": "If failed, repair only the cited group and keep unrelated groups unchanged."
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "The OS line states Tiantian keeps his lips closed and does not mouth the voiceover.",
      "fix_instruction": "If failed, repair only the cited group and keep unrelated groups unchanged."
    }
  ],
  "issues": [],
  "warnings": []
}