{
  "pass": true,
  "summary": "seg05 四组保留炸弹启动、排爆口令、剪线成功、赵大江被抓和陆凡安抚江若晴，审核通过。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组"],
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
      "evidence": "徐虎按红色按钮、喊出炸弹启动、江若晴身上倒计时闪烁和陆凡不冲炸弹均保留。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "陆凡现场对门外排爆组喊话有口型，排爆手回应写为门外传来并有警察身影靠近作为来源。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "红蓝黄三线在第2组由陆凡报出，第3组排爆手用专业工具分开引线并剪断，倒计时定格在最后五秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第1组12秒只承载按按钮、疯狂喊话、倒计时闪烁和陆凡转向门外，节拍清楚。",
      "fix_instruction": "若不通过，应拆出倒计时或陆凡呼叫前反应。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "陆凡24字左右紧急喊话分配5秒，约4.8字/秒；排爆手回应约11字分配2.5秒，约4.4字/秒，未超过硬上限。",
      "fix_instruction": "若不通过，应延长喊话时间或拆分排爆回应。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第3组锁定厂房车间内铁柱、江若晴和两名排爆手，未跨空间。",
      "fix_instruction": "若不通过，应补两名排爆手入场位置和炸弹状态。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾炸弹解除、江若晴仍绑在铁柱上，第4组首江若晴绳索正被松开，陆凡扶住她并说没事了，状态连续。",
      "fix_instruction": "若不通过，应补江若晴由被绑到被扶住的解绳过渡。"
    }
  ],
  "issues": [],
  "warnings": []
}
