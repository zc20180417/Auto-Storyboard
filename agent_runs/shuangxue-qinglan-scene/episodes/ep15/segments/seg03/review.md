{
  "pass": true,
  "summary": "seg03用15秒快速对质保留隐私辩解、养老钱质问、周桂兰确认和拒绝解锁的全部台词，无硬问题。",
  "checked_groups": ["第4组"],
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "保留周美娟隐私辩解、沈清养老钱质问、周桂兰“真是你拿的？”、周美娟“别听她挑拨”和沈清要求解锁短信。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "本组约71个有效对白字分布在15秒内，整体约4.7字/秒；末尾三句拆为10-12秒、12-14秒、14-15秒分别承载，单段均未超过6.5字/秒。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "全组只在灯光明亮的周家正屋客厅，组首列明沈清、周美娟、周桂兰、赵强位置、朝向和手机归属。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "所有现场对白均写明周美娟对沈清、沈清对周美娟、周桂兰对周美娟、周美娟对周桂兰，没有假对象。",
      "fix_instruction": "无须修复；保持每句现场对白有真实对象。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组是同一空间同一目标下的连续短句交锋，虽拆成7个短时间段，但动作仅为抱手机、逼近半步、周桂兰上前半步和周美娟后退半步，未塞入抢夺或肢体冲突。",
      "fix_instruction": "无须修复；不要在本组加入赵强冲上前动作。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "周美娟手机始终由她抱在胸前，沈清旧手机始终用于录像，名牌包挂在周美娟手臂上。",
      "fix_instruction": "无须修复；不得让沈清在本组夺走周美娟手机。"
    }
  ],
  "issues": [],
  "warnings": []
}
