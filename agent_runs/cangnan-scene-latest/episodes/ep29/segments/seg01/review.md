{
  "pass": true,
  "summary": "seg01保留装药、倒计时、广播警告和两名爆破手逃窜的完整因果，时间与空间合同可执行。",
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
      "evidence": "保留爆破手甲看表说“定时器已设定，十分钟后引爆。”和爆破手乙说“龙少有令，这片稀土矿脉得不到就毁掉。”，未新增改变爆破结果的动作。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "应急广播写为喇叭传出画外广播声，两名爆破手嘴唇闭合不做口型，声音来源明确。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "广播台词约22字分配5秒，爆破手甲短句3秒，爆破手乙“快跑！”2秒，均未超过6.5字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定承重柱、炸药、定时器和两名爆破手位置，后续动作都发生在同一矿洞承重柱旁。",
      "fix_instruction": "若不通过，应补充承重柱、炸药和两名爆破手的画面位置与身体朝向。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "14秒内承载广播、两句短反应和逃跑动作，拆成4个时间段，强节拍密度可表演。",
      "fix_instruction": "若不通过，应拆出广播或逃跑动作，避免把声音事件和逃窜动作硬塞进同一短镜头。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾定时器启动且两人仍在柱旁，第2组首复述炸药和定时器仍固定在承重柱上，状态连续。",
      "fix_instruction": "若不通过，应在第2组组首明确炸药与定时器仍留在柱面。"
    }
  ],
  "issues": [],
  "warnings": []
}
