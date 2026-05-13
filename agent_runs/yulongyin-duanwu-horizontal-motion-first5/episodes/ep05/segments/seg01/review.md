{
  "pass": true,
  "summary": "seg01两组已对照原剧本和横屏规则审核，泉眼、铁锤、胡永贵发令、包工头逼近与水壶青蓝光均保留，未发现 hard issue。",
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
      "evidence": "原剧本中泉眼渗水、包工头举铁锤、天天喊“住手！那是村里最后一口活水！”、胡永贵命令扔下山均按顺序保留。"
    },
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "evidence": "泉眼固定在左中后方，天天左侧护水，包工头和胡永贵在右侧形成威胁，横屏左右阵营清楚。"
    },
    {
      "group": "第2组",
      "type": "camera_motion",
      "evidence": "每个时间段均有运镜设计；固定机位说明稳定铁锤归属、包工头肩背压迫和水壶微光，道具与人物轴线明确。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "铁锤从举起到放低，包工头转向天天；水壶始终在天天怀里并在组尾发青蓝光，承接下一段云宝动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "天天台词约14字用3.5秒，胡永贵台词约20字用3.5秒，均未超过6.5字/秒硬上限。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "包工头从右向左逼近，天天沿左侧岩壁后退，人物没有无过渡换边。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第2组",
      "type": "camera_motion",
      "result": "pass",
      "evidence": "固定过肩、横向跟拍和轻微推近均写明服务目的：压缩空间、稳定威胁轴线、提示水壶介入。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
