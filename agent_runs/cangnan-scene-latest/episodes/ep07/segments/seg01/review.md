{
  "pass": true,
  "summary": "seg01已对照原剧本完成审核，警车到场、报案理由、陆凡解释、直播证据和老张看回放的转折均保留，无硬问题。",
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
      "evidence": "第1组保留三辆警车停村口、老张询问谁是陆凡、牛大春询问原因、老张出示出警单说明徐虎报案的剧情和台词。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组3-7秒承载老张问话和陆凡前半句说明，约24字/4秒；7-11秒承载陆凡后半句约24字/4秒，均未超过6.5字/秒硬上限。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "第3组始终在水头村村口泥地，周思思在组首位于村民前排右后方并持手机，随后挤到老张面前递出回放，人物可用性成立。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "老张对在场众人喝问，牛大春对老张问话，老张对陆凡和牛大春说明报案内容，所有现场对白均有真实对象。",
      "fix_instruction": "若出现无对象对白，应补为对老张、对陆凡或对在场众人说道。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "周思思组首手中持有手机，5-11秒举起手机，11-15秒递向老张，老张接过手机看回放，道具归属有可见过渡。",
      "fix_instruction": "若手机突然变到老张手中，应补周思思递出或老张接过的动作。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾部老张质疑徐虎的人被打，第3组组首仍在同一村口，老张、陆凡、周思思和手机位置连续。",
      "fix_instruction": "若同空间状态跳变，应在组首复述老张、警察、陆凡与牛大春的具体位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
