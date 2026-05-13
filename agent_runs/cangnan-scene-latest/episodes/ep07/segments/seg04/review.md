{
  "pass": true,
  "summary": "seg04已对照原剧本完成审核，晴天村口版林夏怒停抓捕、盖章文件、赵乡长指示和解开手铐均保留，无硬问题。",
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组保留黑色奥迪急刹、林夏怒容下车、要求打开手铐、老张称执行公务、林夏质问保护伞并砸文件。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组0-4秒、4-7秒、7-10秒分别承载林夏、老张、林夏三句短台词，均在可表演范围内。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "第2组组首陆凡仍戴手铐，10-13秒老张接过钥匙打开手铐，13-15秒陆凡手铐已解开，道具状态连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "林夏在组首位于黑色奥迪内并可被车窗遮挡看见，2-5秒下车后才说话和递文件，人物可用性成立。",
      "fix_instruction": "若林夏未在组首或未入场就说话，应补车内可见状态或下车入场动作。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部文件砸在老张胸口、陆凡仍戴手铐；第2组组首复述文件位置和陆凡手铐状态，衔接明确。",
      "fix_instruction": "若文件或手铐状态跳变，应在组首复述或在镜头中补可见过渡。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模型说明词、参考图、模板编号或字幕指令，文件砸胸口和手铐均为可生成动作。",
      "fix_instruction": "若出现模板污染，应改成具体动作、道具和对白承载。"
    }
  ],
  "issues": [],
  "warnings": []
}
