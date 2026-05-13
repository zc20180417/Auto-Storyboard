{
  "pass": true,
  "summary": "seg03 保留手下举锤、背包飞入、砸倒手下、胡永贵惊恐和爸爸门口现身，门内外横屏轴线清楚。",
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第7组",
      "type": "script_fidelity",
      "evidence": "两个手下举锤、破旧背包从门口砸进来并命中手下脸部、手下惨叫倒地，严格对应原剧本动作。"
    },
    {
      "group": "第8组",
      "type": "dialogue_direction",
      "evidence": "胡永贵朝画面右侧门外喊“谁！谁敢管闲事！”，爸爸在门口对胡永贵和手下说“敢动我儿子，找死！”，现场对白对象明确。"
    },
    {
      "group": "第8组",
      "type": "horizontal_composition",
      "evidence": "胡永贵和手下被放在画面左侧室内阴影，爸爸站在画面右侧门外逆光，破旧背包在中央地面，左右对峙和入场来源清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "破旧背包从右侧门外飞入，第7组尾停在倒地手下旁，第8组组首继续作为双方中间的地面证据。",
      "fix_instruction": "若不通过，应补充背包从门外飞入到落地停留的连续动作。"
    },
    {
      "group": "第8组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "爸爸在第8组组首明确站在画面右侧大门外逆光里，承载暴怒台词时可见口型和下颌动作。",
      "fix_instruction": "若不通过，应在组首或入场镜头中明确爸爸的可见位置和口型承载。"
    },
    {
      "group": "第7组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第7组只处理举锤、背包飞入、命中、众人转向门口四个动作节拍，12秒内动作链完整。",
      "fix_instruction": "若不通过，应把爸爸完整亮相留到下一组，避免同组过载。"
    }
  ],
  "issues": [],
  "warnings": []
}
