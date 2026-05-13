{
  "pass": true,
  "summary": "seg04已审核，黑风山主干道通车、江若晴推进项目、村民送锦旗和牛大春感谢陆凡均完整保留。",
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
      "evidence": "保留阳光明媚、柏油路通向黑风山、江若晴激动说项目推进、陆凡说清河乡马上起飞。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组3-6秒牛大春台词13字约4.3字/秒；6-10秒陆凡台词14字加扶起动作，约3.5字/秒但有可见动作支撑。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "锦旗、花生、核桃在组首由村民持有，0-3秒送到陆凡面前，3-6秒牛大春手持锦旗感谢，归属变化清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第1组只在黑风山主干道外，组首明确陆凡、江若晴和施工队位置朝向。",
      "fix_instruction": "若不通过，应拆出不同物理空间或补全人物位置。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部陆凡和江若晴仍在剪彩现场，第2组组首复述二人仍在主干道旁，村民围到同一现场。",
      "fix_instruction": "若不通过，应补村民接近或二人位置状态。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组为送礼、感谢、扶起回应三个轻节拍，10秒短组作为庆祝收尾成立。",
      "fix_instruction": "若不通过，应与第1组合并或减少非关键庆祝动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
