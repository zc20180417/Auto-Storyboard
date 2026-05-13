{
  "pass": true,
  "summary": "seg01横屏分镜保留泉眼、铁锤、天天阻拦、胡永贵下令和水壶发光的完整因果，未发现阻断交付的硬问题。",
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
      "type": "horizontal_composition",
      "evidence": "第1组组首把天天锁在画面左前景，包工头和胡永贵锁在右中景、右后景，泉眼和铁锤在中央偏右，16:9左右阵营和道具目标明确。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "天天台词“住手！那是村里最后一口活水！”放在2.5秒内承载，胡永贵台词“小叫花子又来捣乱，把他给我扔下山去！”放在3.5秒内承载，均未超过6.5字/秒硬上限。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "第2组从铁锤停在包工头右脚旁，到水壶贴在天天胸前发光，再到组尾水壶持续微亮，铁锤和水壶归属没有跳变。"
    },
    {
      "group": "第2组",
      "type": "camera_motion",
      "evidence": "第2组每个时间段都有运镜设计，横向跟拍服务包工头压迫路线，固定机位稳定左右站位，轻推揭示水壶异常，最后固定承接下一段。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "原剧本中的泉眼、包工头举铁锤、天天喊停和胡永贵命令均按顺序保留，没有新增改变剧情的动作。",
      "fix_instruction": "如需修改，只能局部调整镜头表达，不得删改两句原台词或改变胡永贵命令对象。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首空间锁定只写天天已在左前景、包工头右中景、胡永贵右后景、泉眼和水壶位置，没有把迈步或发光过程写进组首。",
      "fix_instruction": "若后续发现组首出现走来、逼近、拿起、放下等动词，应移入时间段镜头描述。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部铁锤停在泉眼旁、天天挡住泉眼；第2组组首延续天天左、包工头右、胡永贵右后景，并解释铁锤落在包工头脚旁。",
      "fix_instruction": "如果重新剪组，需保留铁锤落点和水壶在天天胸前的状态锚点。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、参考图占位、首帧尾帧、自动分镜或视频延长等工程词，尾部仅保留短剧风格和负向词。",
      "fix_instruction": "保持自然分镜正文，不要引入Seedance模板说明或控制台占位符。"
    }
  ],
  "issues": [],
  "warnings": []
}
