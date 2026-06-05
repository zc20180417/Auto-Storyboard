{
  "pass": true,
  "summary": "seg03完成周美娟护镯、赵强暴怒夺镯、沈清隔纸巾接镯，动作链拆段清楚。",
  "checked_groups": ["第5组", "第6组"],
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
      "group": "第5组",
      "type": "action_atomicity",
      "evidence": "周美娟拒绝、赵强怒骂、赵强扣腕拉扯分为三个时间段，没有把起身和夺镯结果挤到同一短镜。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "evidence": "金镯子从周美娟手腕被赵强撸下，随后由赵强递出，最终隔纸巾落到沈清手中，转移路径完整。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "周美娟惨叫约12字用2.5秒，约4.8字/秒；赵强赔笑台词约16字用3秒，约5.3字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第5组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留周美娟护镯拒绝、赵强骂败家娘们并抓腕往下撸的因果，没有新增沈清抢夺动作。",
      "fix_instruction": "若不通过，应恢复赵强作为夺镯主动作人物。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "12秒组包含惨叫、撸下金镯、递给沈清、纸巾接镯四个连续动作阶段，属于同一夺镯事件链。",
      "fix_instruction": "若不通过，应将递镯和接镯另拆短组。"
    },
    {
      "group": "第6组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项针对金镯归属、沈清纸巾接镯、赵强收入口袋和周美娟抢回等本组具体风险。",
      "fix_instruction": "若不通过，应删除与本组无关或无锚点的禁止项。"
    }
  ],
  "issues": [],
  "warnings": []
}
