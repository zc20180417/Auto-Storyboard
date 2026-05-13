{
  "pass": true,
  "summary": "seg04乡长办公室两组完整保留王建国被带走、陆凡抢修和赵大江下令炸路的因果升级。",
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
      "evidence": "保留赵大江踱步、手下撞入、王建国被市纪委带走、陆凡放出并抢修水头村公路的信息顺序。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "赵大江24字炸路命令用4.5秒约5.3字/秒，疯狂收尾15字用4秒并含指门动作，均未超过6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "第2组始终在乡长办公室内，赵大江和手下都在组首有明确位置、身体朝向和可见状态。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "手下在组首位于办公室门外走廊一侧，撞门入场后才汇报，人物可用性成立。",
      "fix_instruction": "若不通过，应将手下放在门外可入场的位置或先写入场动作。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组为踱步、撞门入场、两段汇报和赵大江惊问，14秒内节拍清楚，无道具操作叠加。",
      "fix_instruction": "若不通过，应拆分市纪委消息和抢修消息。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "赵大江阻止修路、命令拿雷管炸路、手下提示重罪、赵大江以进监狱威胁催促均保留。",
      "fix_instruction": "若不通过，应恢复被删改的炸路命令或重罪提醒。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾办公室门打开，手下在门边汇报；第2组组首延续门打开、两人对峙的位置。",
      "fix_instruction": "若不通过，应补充办公室门和两人站位状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
