{
  "pass": true,
  "summary": "seg02已对照原剧本4-2完成横屏审稿，云宝醒来、水雾、泥水结冰、胡永贵摔倒、天天接满水壶离开均完整保留。",
  "checked_groups": [
    "第4组",
    "第5组",
    "第6组"
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
      "group": "第4组",
      "type": "space_locking",
      "evidence": "天天延续上一段倒在左前景护壶，胡永贵在右后景，水壶、泥水、水管位置都有明确左右和前后层次。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "原剧本中泥水改变方向并结成薄冰、胡永贵踩冰摔倒、水管脱手全部保留，没有新增打斗或额外惩罚动作。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "天天台词“走！我们回家！”约6字安排2.5秒，同时有抱壶转身动作，口型节奏自然。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "filmability",
      "result": "pass",
      "evidence": "云宝醒来、转圈和喷水雾均转译为水壶特写与壶内近景，可生成且不靠抽象说明推进剧情。",
      "fix_instruction": "若画面不可见，应改为壶壁波纹、雾气溢出或天天反应来承载。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "泥水从皮卡右侧流向中央，结冰后位于胡永贵脚下；水管从他手中甩到中央偏左，具备可见过渡。",
      "fix_instruction": "若水管脱手位置不清，应补写滑落路线和喷口朝向。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾部水管落到天天右前方，第6组组首即写水管在中央偏左、天天视线锁住喷口，衔接连续。",
      "fix_instruction": "若衔接断裂，应在第5组尾或第6组首补充天天看准水管落点。"
    }
  ],
  "issues": [],
  "warnings": []
}
