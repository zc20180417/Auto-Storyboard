{
  "pass": true,
  "summary": "密林开路到毒蛇袭面两组已按横屏关系和原剧本危险递进完成，未发现阻断生产的硬问题。",
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
      "type": "horizontal_composition",
      "evidence": "爸爸固定在画面左前方开路，天天背水壶在画面右后方跟随，组首和5-7.5秒镜头都明确左/右、前/后景与山路轴线。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "天天台词“爸爸，云宝说还有两座山头。”放在2.5秒疲惫喘息镜头内，爸爸“停下！前面有动静。”放在2秒警惕停步镜头内，未超过6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "原剧本毒蛇盘起、吐信、弹射直逼天天面门均保留，爸爸仍从左侧用开山刀拦截，未新增打中毒蛇或云宝提前出手。"
    },
    {
      "group": "第2组",
      "type": "screen_direction",
      "evidence": "第1组尾部草丛在画面中央，天天停在右后方；第2组组首延续爸爸左、天天右、草丛中央偏右，蛇向右后方弹射，轴线连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首写明密林山路、爸爸左前景、天天右后景、水壶位置、刀和视线方向，单组可独立生成。",
      "fix_instruction": "无需修改；若后续调整，保留爸爸左前方开路和天天右后方跟随的空间关系。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "10秒内只承载毒蛇显形、蓄力、弹射、爸爸拦截未及四个动作节拍，没有叠加长对白或额外道具操作。",
      "fix_instruction": "无需修改；不要加入云宝救援动作，救援应留到下一段。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "水壶一直在天天右后景胸前，开山刀从第1组爸爸手中延续到第2组左侧拦截，没有道具跳位。",
      "fix_instruction": "无需修改；如果改写动作，必须保留水壶在天天身上、开山刀在爸爸手中的归属。"
    }
  ],
  "issues": [],
  "warnings": []
}
