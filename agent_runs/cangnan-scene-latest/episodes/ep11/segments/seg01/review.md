{
  "pass": true,
  "summary": "seg01 两组保留电话威胁、林夏追问和陆凡驾车离开，格式与时长通过。",
  "checked_groups": ["第1组", "第2组"],
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "evidence": "徐虎只以电话音出现，手机亮屏和陆凡听电话反应明确，徐虎台词未写成现场口型。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "保留陆凡两句台词、徐虎三句威胁台词，合同和半小时到木材厂的信息未删改。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "林夏10字台词分配3秒，陆凡11字台词分配3秒并带收手机动作，未超过6.5字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定乡政府大院外、越野车、陆凡位置和电话音来源，单一物理空间清楚。",
      "fix_instruction": "若不通过，应补充手机位置、徐虎电话音来源和陆凡画面位置。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组以陆凡握紧手机结束，第2组从电话挂断和林夏跑近开始，状态连续。",
      "fix_instruction": "若不通过，应在第1组尾或第2组首补电话挂断和林夏位置。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组只承载电话结束、林夏追问、陆凡回应和上车离开，11秒内节拍清楚。",
      "fix_instruction": "若不通过，应拆出上车离开或压缩非关键走位。"
    }
  ],
  "issues": [],
  "warnings": []
}
