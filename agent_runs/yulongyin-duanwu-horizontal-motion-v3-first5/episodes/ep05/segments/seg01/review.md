{
  "pass": true,
  "summary": "seg01 两组保留泉眼冲突、胡永贵命令、包工头逼近和水壶发光，横屏轴线、运镜和道具状态链可交付。",
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
    "camera_motion": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组保留巴掌大清泉、包工头铁锤对准石壁、天天喊“住手！那是村里最后一口活水！”以及胡永贵命令“小叫花子又来捣乱，把他给我扔下山去！”，顺序与原剧本 5-1 一致。"
    },
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "evidence": "泉眼位于中央后景，天天在左前景，胡永贵和包工头在右侧，铁锤贴近泉眼旁石壁，左右压迫和道具位置清楚。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "铁锤从包工头右腿旁到威胁压近，水壶始终在天天怀中，5-10秒明确壶口青蓝光从壶内亮起并反射到水洼。"
    },
    {
      "group": "第2组",
      "type": "camera_motion",
      "evidence": "第2组 0-2秒横向跟拍包工头脚步，2-5秒固定机位稳定压迫关系，5-8秒轻推水壶，8-10秒固定道具特写，运镜服务走位和道具触发。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "天天 3 秒承载 12 个有效字左右，胡永贵 3.5 秒承载约 18 个有效字，均低于 6.5 字/秒硬上限。双方对话对象均在同场画面关系中明确。",
      "fix_instruction": "若台词过快，应延长对应时间段或拆分反应镜头，不能删改原台词。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首只写天天、包工头、胡永贵、泉眼、水洼和铁锤的静态位置，没有把放下铁锤、逼近、后退或水壶发光写进组首动作过程。",
      "fix_instruction": "若出现过程动词，应把动作移到后续镜头描述，并保留组首第一帧静态位置。"
    },
    {
      "group": "第2组",
      "type": "narrative_progression",
      "result": "pass",
      "evidence": "信息从包工头压近，推进到天天退到岩壁，再落到水壶青蓝光亮起，为下一段云宝提示和水洼呼应提供明确状态锚点。",
      "fix_instruction": "若递进断裂，应补充水壶光与水洼呼应的可见状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
