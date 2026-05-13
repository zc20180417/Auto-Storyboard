{
  "pass": true,
  "summary": "seg03已核对黄毛围攻、陆凡号召录像、抓棍震慑和混混撤退，动作与台词均按剧本顺序保留。",
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
      "type": "script_fidelity",
      "evidence": "保留黄毛站稳后怒吼、三个混混举铁棍、陆凡不还手拉周思思后退并喊村民录像的因果链。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "陆凡“你再动一下试试。直播间几万人看着，你想当网红逃犯？”约27字给5秒，约5.4字/秒，符合情绪对白容量。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "evidence": "第2组尾部陆凡压住铁棍，第3组组首仍为右手压住混混铁棍棍头，关键道具和人物位置连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "陆凡、周思思、黄毛、混混和远处村民均在组首或背景可用，村民举机动作发生在被陆凡喊话之后。",
      "fix_instruction": "若人物不可用，应在组首或入场动作中补足位置。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "铁棍从混混手中举起，到陆凡抓住棍头并压住，没有夺棍，符合原剧本道具状态。",
      "fix_instruction": "若道具跳变，应补充递出、抓住或放下等可见过渡。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "黄毛对三个混混说道、周思思对直播间喊、陆凡对镜头说道，声音对象均明确。",
      "fix_instruction": "若对象缺失，应改成具体角色或直播间/镜头来源。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "撤退组将弹幕震慑、黄毛撤退、周思思播报、陆凡留证分成5个清楚时间段，总时长14秒，没有压缩关键动作。",
      "fix_instruction": "若过载，应拆出撤退或留证说明。"
    }
  ],
  "issues": [],
  "warnings": []
}
