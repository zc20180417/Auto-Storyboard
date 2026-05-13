{
  "pass": true,
  "summary": "第1组村民乙躲进小卖部报警已按原剧本、横屏调度、台词节奏和可生成性完成审核，未发现阻断交付的硬问题。",
  "checked_groups": [
    "第1组"
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
      "evidence": "保留村民乙趁乱躲进小卖部报警、完整报警台词、电话里警察回复马上到并要求保护自己。"
    },
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "evidence": "左侧玻璃门连接广场混乱，右侧货架和柜台提供躲藏空间，村民乙右前景打电话形成室内横屏遮挡。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "报警句约31字/5秒约6.2字秒比，电话警察回复约19字/3秒约6.3字秒比，均未超过硬上限；全组14秒4镜头。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "村民乙对电话里的警察说话，警察声音明确来自手机听筒，未写成画面内人物开口。",
      "fix_instruction": "已通过；若后续修改台词，保持说话对象和声音来源明确。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定小卖部内左侧玻璃门、右侧柜台货架、手机在村民乙手里，声音载体清楚。",
      "fix_instruction": "已通过；若后续改镜头，保留组首左右、前后景和关键道具位置。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、参考图占位、视频延长、自动分镜等工程说明词；负向词仅用于排除竖屏构图。",
      "fix_instruction": "已通过；不要加入模型模板说明或控制台占位符。"
    }
  ],
  "issues": [],
  "warnings": []
}
