{
  "pass": true,
  "summary": "seg05 保留私人停机坪转场、龙天傲迎接鬼王、鬼王威胁和车队开往黑风山，动作与对白承载稳定。",
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
      "evidence": "保留视频挂断后切至省城私人停机坪、豪华客机舱门打开、龙天傲和黑衣鬼王下机。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "9-14秒承载龙天傲约19字恭敬台词并包含侧身动作，字秒比约3.8，未超过硬上限且有表演支撑。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留鬼王两句威胁、龙天傲下令备车目标黑风山摧毁嘉禾，以及越野车队驶出机场。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "组首锁定豪华客机、红地毯、越野车、龙天傲和鬼王位置朝向，后续说话和上车方向可生成。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "转场、开舱门、下机和龙天傲恭敬开口分为4段共14秒，鬼王台词另拆到第2组，未过载。",
      "fix_instruction": "若不通过，应拆分下机动作和龙天傲对白。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "鬼王两句均对龙天傲说道，龙天傲对身旁随从喊道备车，现场对白对象明确。",
      "fix_instruction": "若不通过，应补充鬼王和龙天傲的真实说话对象。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾龙天傲在红地毯旁侧身、鬼王站在半步后；第2组首复述两人相对位置和越野车待命。",
      "fix_instruction": "若不通过，应在第2组组首补红地毯旁两人站位。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模板编号、参考图、视频延长、字幕或模型说明词。",
      "fix_instruction": "若不通过，应删除污染词并改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
