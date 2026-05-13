{
  "pass": true,
  "summary": "seg01两组已对照原剧本和横屏规则审核，父亲回归、天天求救、爷爷入场和鼓槌递出均保留，横屏站位和道具归属清楚。",
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
      "evidence": "第1组保留爸爸对天天说“对不起，爸爸回来晚了。”、天天对爸爸喊“爸爸快救云宝！它快死了！”，并让爸爸转头看见地上奄奄一息的云宝，剧情顺序与原剧本一致。"
    },
    {
      "group": "第2组",
      "type": "horizontal_composition",
      "evidence": "第2组明确爷爷从画面左后方门口入场，爸爸在中央偏右，天天和云宝在右侧低处，鼓槌被递到画面中央，左右和前后层次可生成。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "爷爷“燃燃！你回来了！时辰没过！”安排在2.5秒情绪喊话内，约12字/2.5秒；“敲鼓！唤龙！救活它！”安排在1.5秒内，约7字/1.5秒，未超过6.5字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "爸爸台词写明对天天说道，天天台词写明对爸爸喊道，现场口型承载和对象明确。",
      "fix_instruction": "若不通过，应在对应镜头补明说话人、对象和同框反应。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "老木鼓槌由爷爷从怀里摸出，再由爷爷双手递向爸爸，全组归属始终在爷爷手中，没有漂移。",
      "fix_instruction": "若不通过，应补充鼓槌拿出、递近或停在两人之间的可见动作。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾门口留出空位，第2组组首爷爷从左后方门口入场，爸爸和天天仍围绕云宝，空间衔接自然。",
      "fix_instruction": "若不通过，应调整上一组尾部或下一组组首的人物位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
