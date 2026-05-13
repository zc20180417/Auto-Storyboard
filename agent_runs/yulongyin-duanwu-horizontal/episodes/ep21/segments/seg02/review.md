{
  "pass": true,
  "summary": "第1组后山小路听见村口异动已按原剧本、横屏调度、台词节奏和可生成性完成审核，未发现阻断交付的硬问题。",
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
      "evidence": "保留爸爸背行囊、天天抱水壶、山风带来惨叫和汽车轰鸣、爸爸判断胡永贵带人杀回来的剧情。"
    },
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "evidence": "小路向画面右上延伸，村口声音来自左后方，爸爸左、天天右后形成清楚的横屏移动关系。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "天天问句3秒、爸爸回答3秒，短句与停步反应合并承载，字秒比安全；全组12秒4镜头。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "天天明确对爸爸发问，爸爸明确回答天天，惨叫和汽车声作为画外环境声有方向来源。",
      "fix_instruction": "已通过；若后续修改台词，保持说话对象和声音来源明确。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定小路延伸方向、爸爸与天天左右位置、水壶归属和远处村口声源。",
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
