{
  "pass": true,
  "summary": "seg02 保留扣腕阻删、销毁证据台词、手机滑到周桂兰脚边和亮屏短信，手机归属与位置连续。",
  "checked_groups": ["第3组"],
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
      "evidence": "第3组保留沈清一步跨上前扣住手腕、手指距删除键一毫米、扭腕掉手机、手机停到周桂兰脚边和沈清喊母亲看屏幕。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "周美娟9字给1.5秒约6字/秒，沈清11字给2秒约5.5字/秒，沈清喊母亲6字给3秒中的主要声音段不足硬上限且伴随手机滑行动作。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "整组只在周家正屋客厅，组首列出周美娟、赵强、沈清、周桂兰的位置和朝向，没有跨物理空间。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "周美娟手机从她右手删除界面，到掉落地板，再滑到周桂兰脚边，转移路径完整可见。",
      "fix_instruction": "若不通过，应补充手机从谁手里掉落及最终停靠位置。"
    },
    {
      "group": "第3组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "扣腕、删除键受阻、两句对峙、扭腕掉手机、手机滑行各自分段，没有把多个主动作压进同一短镜。",
      "fix_instruction": "若不通过，应拆分扣腕和扭腕掉手机。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "周美娟对沈清喊，沈清对周美娟说，沈清对周桂兰喊，三句现场对白都有真实对象。",
      "fix_instruction": "若不通过，应补充每句对白对象。"
    },
    {
      "group": "第3组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定周美娟、周美娟的手机、转账短信和沈清手腕动作，均是本组关键风险。",
      "fix_instruction": "若不通过，应删除泛泛禁项并改为手机位置和删除键相关禁项。"
    }
  ],
  "issues": [],
  "warnings": []
}
