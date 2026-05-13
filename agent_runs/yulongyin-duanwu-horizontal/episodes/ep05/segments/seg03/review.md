{
  "pass": true,
  "summary": "seg03两组横屏分镜保留胡永贵泼黑液、天天阻止、云宝挡泉眼和变灰坠地，硬规则通过。",
  "checked_groups": [
    "第1组",
    "第2组"
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
      "evidence": "胡永贵原台词邪门了我今天非把这破洞平了不可保留，黑色废液从身后拎起并泼向泉眼，天天喊不要，剧情因果未改。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "云宝从水壶跃出挡在泉眼前，黑色废液尽数浇在云宝身上，云宝惨叫、摔地并从青蓝变死灰，关键状态完整呈现。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "胡永贵大怒台词约17个有效字放在3秒内，约5.7字每秒；天天不要约2个有效字放在1.5秒内并伴随扑救动作，未触发硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "黑色废液桶先在胡永贵身后岩壁旁，之后被胡永贵拎起、倾倒并形成飞向泉眼的黑液弧线，道具运动可见。",
      "fix_instruction": "若不通过，应补充拿桶、提桶或倾倒动作，避免废液凭空出现。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部黑液飞向右后方泉眼，第2组首部胡永贵仍在中右侧倾倒，黑液继续落向泉眼，动作衔接一致。",
      "fix_instruction": "若不通过，应让第2组组首承接第1组尾部的废液位置和人物站位。"
    },
    {
      "group": "第2组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "云宝从左前方水壶跃向右后方泉眼，胡永贵在中右侧，天天在左前方，横向运动和人物分区清楚。",
      "fix_instruction": "若不通过，应明确云宝跃出路径、泉眼位置和胡永贵站位。"
    }
  ],
  "issues": [],
  "warnings": []
}
