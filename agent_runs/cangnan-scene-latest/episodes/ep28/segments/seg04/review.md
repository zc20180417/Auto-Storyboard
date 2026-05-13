{
  "pass": true,
  "summary": "seg04保留陆凡CQB击倒队员、双方对话、踢椅逼近、马伽术扣腕和过肩摔。",
  "checked_groups": ["第7组", "第8组"],
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
      "group": "第7组",
      "type": "dialogue_pacing",
      "evidence": "毒刺“顶级CQB战术？你到底是什么组织的！”约18字用3秒，情绪惊骇约6字/秒，低于6.5硬上限；陆凡8字用3秒，节奏合理。"
    },
    {
      "group": "第8组",
      "type": "generation_density",
      "evidence": "踢椅、欺身、毒刺挥拳、扣腕、过肩摔拆为4段14秒，关键动作链没有与长台词叠加。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "evidence": "第7组尾部办公椅仍在陆凡右侧地面，第8组组首复述该椅子位置，0-3秒陆凡踢飞办公椅，过渡清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "原剧本“砰砰两下，两名队员被陆凡精准击中要害，倒地不起”被保留为4-7秒动作段，未新增致命武器或额外剧情。",
      "fix_instruction": "若动作被删，应补回两名队员被精准击中要害倒地。"
    },
    {
      "group": "第8组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "整组仍在董事长办公室内，组首写明两名队员倒地、陆凡、毒刺、办公椅和玻璃茶几的位置。",
      "fix_instruction": "若茶几或办公椅不可用，应在组首补明位置。"
    },
    {
      "group": "第8组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第7组结尾陆凡盯住毒刺、两名队员倒地，第8组组首延续同一状态并展开追击。",
      "fix_instruction": "若状态跳变，应在第7组尾或第8组首补陆凡与毒刺的站位。"
    }
  ],
  "issues": [],
  "warnings": []
}
