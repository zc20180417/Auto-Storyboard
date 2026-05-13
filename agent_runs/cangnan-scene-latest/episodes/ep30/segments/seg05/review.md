{
  "pass": true,
  "summary": "seg05正确区分电话音和陆凡现场口型，保留龙家主威胁与陆凡全面封杀宣告，审核通过。",
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
      "type": "audio_mouth_sync",
      "evidence": "龙家主第一句明确为手机听筒电话音，陆凡嘴唇闭合不做口型；陆凡回应时才对电话里的龙家主开口。"
    },
    {
      "group": "第1组",
      "type": "prop_continuity",
      "evidence": "加密电话先在龙天傲身旁地面亮屏，随后陆凡弯腰捡起并接通，道具归属转移有可见过渡。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "龙家主两段电话音分别约24字/5秒和22字/4秒，陆凡结尾约28字/5秒，均未超过6.5字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "电话响起、陆凡捡起接通、龙家主要求放人、陆凡指出商业窃密和非法竞争证据确凿，顺序完整。",
      "fix_instruction": "若删除电话响起或接通过程，应补回道具动作。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "龙家主威胁均写为电话音，画面主体陆凡嘴唇闭合不做口型，避免电话音误配口型。",
      "fix_instruction": "若电话音被写成陆凡现场开口，应改为手机听筒传出并写明画面人物闭口反应。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾陆凡拿着正在通话的加密电话、龙天傲被按住；第2组首延续电话通话和控制状态。",
      "fix_instruction": "若第2组电话状态缺失，应补正在通话的加密电话。"
    }
  ],
  "issues": [],
  "warnings": []
}
