{
  "pass": true,
  "summary": "第1组石头打断甩棍，爸爸单枪匹马入场已按原剧本、横屏调度、台词节奏和可生成性完成审核，未发现阻断交付的硬问题。",
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
      "evidence": "保留刀疤男踩村民、威胁废手、石头飞来砸弯甩棍、刀疤男喊“谁！”和爸爸从广场边缘走来。"
    },
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "evidence": "刀疤男和胡永贵占右侧压迫中心，左侧入口留给石头飞入和爸爸入场，左右压力反转清楚。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "刀疤男威胁句约12字/3秒约4.0字秒比，“谁！”独立反应镜头充足；全组15秒5镜头。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "刀疤男先对倒地村民威胁，再对左侧来袭方向喊“谁！”，对象和视线方向清楚。",
      "fix_instruction": "已通过；若后续修改台词，保持说话对象和声音来源明确。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定刀疤男右中景、倒地村民右下、胡永贵右后方、左侧村道入口，石头运动线可生成。",
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
