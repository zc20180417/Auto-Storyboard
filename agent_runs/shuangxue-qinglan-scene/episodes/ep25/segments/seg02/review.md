{
  "pass": true,
  "summary": "seg02 保留周建国两百万高利贷借条、沈清逼问、宾客鄙夷和律师执行令说明，单场景连续。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "大屏幕切到两百万高利贷借条，沈清两句对周建国的原台词按顺序保留。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "律师约51字台词使用2.5-12秒的9.5秒承载，约5.4字/秒；宾客甲短句2.5秒承载，未超过6.5字/秒。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "evidence": "第3组尾部借条停在大屏幕，第4组组首继续显示借条，周建国仍站在宾客桌旁。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "沈清两句均为画面内真人对白，明确对周建国说道。",
      "fix_instruction": "若不通过，应补充沈清对白对象或拆出旁白来源。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组为屏幕切换、沈清两句逼问和周建国轻反应，12秒内每段主动作清楚。",
      "fix_instruction": "若不通过，应把屏幕切换和逼问分组或压缩轻反应。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "高利贷借条始终在大屏幕上，文件夹始终由律师持有，没有无过渡转移。",
      "fix_instruction": "若不通过，应补充道具归属或屏幕画面状态。"
    },
    {
      "group": "第4组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "宾客甲评价和律师宣读分成两个时间段，讨债人员入场没有提前塞入本组。",
      "fix_instruction": "若不通过，应把外部事件另起一组。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首列明周建国、宾客甲、律师、沈清和宾客在宴会厅内的位置与朝向。",
      "fix_instruction": "若不通过，应补充画面位置和身体朝向。"
    },
    {
      "group": "第4组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第4组视频禁止项锚定律师、讨债人员、周建国和执行令节点，数量为3条且不泛化。",
      "fix_instruction": "若不通过，应替换为本组具体人物或道具风险。"
    }
  ],
  "issues": [],
  "warnings": []
}
