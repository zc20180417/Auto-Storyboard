{
  "pass": true,
  "summary": "seg01 保留天天护舟、被踢倒、瓷碗碎裂、云宝暴露和胡永贵起贪念的因果，横屏站位与道具连续可交付。",
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
      "evidence": "原剧本两句台词“不许你们碰龙舟！滚出去！”和“又是你这小野种。给我滚开！”均保留，随后胡永贵踢开天天、瓷碗脱手的动作没有改写因果。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "瓷碗从第1组尾的天天手中脱出，进入第2组中央地面摔裂，黑水和云宝均从碎碗位置显露，道具位置连续。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "“这是什么怪物？还在冒寒气？”约12字用2.5秒承载，约4.8字/秒；“泡药酒肯定大补，给我装起来！”约14字用3秒承载，约4.7字/秒，均未超过硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "天天固定在画面左前方护龙舟，胡永贵和手下在画面右侧压迫，瓷碗归属在天天胸前，左右关系明确。",
      "fix_instruction": "若不通过，应补充天天、胡永贵、手下和瓷碗的左右/前后位置。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首写明天天左前景、瓷碗中央、胡永贵右侧、手下右后景，云宝在中央偏前暴露，关键人物和道具均可见。",
      "fix_instruction": "若不通过，应在组首锁定中补齐碎碗、黑水和云宝的位置。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载胡永贵观察、两句台词和命令手下取袋，强节拍数量可在13秒内表演。",
      "fix_instruction": "若不通过，应把观察寒气与下令装走拆成两个独立组。"
    }
  ],
  "issues": [],
  "warnings": []
}
