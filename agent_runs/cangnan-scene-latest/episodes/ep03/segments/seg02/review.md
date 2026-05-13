{
  "pass": true,
  "summary": "seg02已审核通过，林夏质问、周昌平否认、转怒赵大江并拨电话给刘波的因果链完整。",
  "checked_groups": ["第3组", "第4组"],
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
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "林夏推门进入、周昌平起身寒暄、林夏追问守公墓与党委会流程，台词顺序与原剧本一致。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "12-15秒周昌平电话喊话有效台词约14字/3秒，约4.7字/秒；其余对白块均低于6.5字/秒硬上限。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "红色电话在组首明确位于周昌平右手边桌角，12-15秒有伸手抓起电话的可见过渡。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第3组只在乡党委书记办公室内发生，林夏入场前门和周昌平位置明确。",
      "fix_instruction": "若跨空间，应另起一组或标注明确转场例外。"
    },
    {
      "group": "第4组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "电话拨出前周昌平为现场开口；末段对电话那端刘波喊话，声音来源和对象明确。",
      "fix_instruction": "若电话音由对方出现，应写明听筒声音和画面人物闭口反应。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾部林夏逼视周昌平，第4组组首延续二人在办公桌前位置，随后林夏离开，状态连续。",
      "fix_instruction": "若人物位置跳变，应在组尾或组首补充移动动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
