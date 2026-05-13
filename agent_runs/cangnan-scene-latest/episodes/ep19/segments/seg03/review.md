{
  "pass": true,
  "summary": "seg03对陆凡报警牵制、江若晴回车录像、警笛逼退和陆凡按住疯狗的连续动作做了分组承载，未新增主动攻击。",
  "checked_groups": ["第5组", "第6组", "第7组", "第8组"],
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
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "疯狗铁棒砸来、陆凡侧身避开、铁棒砸车门、陆凡报警和警方设卡台词、疯狗威胁台词均保留。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "evidence": "疯狗再次扑来、陆凡绕车闪避和提醒江若晴回车三项强节拍拆成10秒3段，没有压进第5组长对白中。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "evidence": "铁棒从疯狗手边滑落到地面后，陆凡按住疯狗肩膀，避免铁棒归属跳变。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "陆凡长句分配5.5秒，疯狗威胁句分配3.5秒，均未超过6.5字/秒且不显拖慢。",
      "fix_instruction": "若不通过，应拆分长句或缩短无台词动作段。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "警笛作为远处声音事件处理，并用远处警灯和疯狗反应承载来源，没有写成画面人物开口。",
      "fix_instruction": "若不通过，应补远处警灯、警笛来源或人物听见后的反应。"
    },
    {
      "group": "第8组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第7组尾部疯狗转身要跑，陆凡压低重心；第8组组首复述疯狗背向道路出口、陆凡在其身后前倾。",
      "fix_instruction": "若不通过，应在第8组组首明确疯狗背向陆凡和陆凡身后位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
