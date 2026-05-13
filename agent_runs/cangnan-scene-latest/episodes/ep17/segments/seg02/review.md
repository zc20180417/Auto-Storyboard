{
  "pass": true,
  "summary": "seg02分镜完整保留马行长否认、陆凡点出海外私账、林夏入场曝光资金和马行长退回专户的剧情闭环。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "type": "dialogue_pacing",
      "evidence": "马行长约16字发抖否认安排4秒，陆凡约17字冷漠回应安排5秒，均低于6.5字/秒且符合情绪对白节奏。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "evidence": "林夏和纪委干部在组首位于玻璃门外可见位置，0-3秒推门进入后再开口，入场和发言顺序成立。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "马行长'完了……全完了'、陆凡催促联系拦截中心、马行长承诺马上退回专户三处关键台词均按原顺序保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部马行长发虚被围在大厅中央，第2组组首仍保持陆凡、马行长和保安在大厅内，林夏从门外入场。",
      "fix_instruction": "若不通过，应补充上一组尾部或本组组首的人物位置过渡。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "柜台电脑在组首位于右后方，8-12秒马行长扑向柜台并摸向键盘后开始操作，关键道具可操作状态清楚。",
      "fix_instruction": "若不通过，应补充走向、拿起或操作道具的可见过渡。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文无模板编号、参考图、模型说明词、自动分镜或字幕工程词。",
      "fix_instruction": "若不通过，应删除工程说明并改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
