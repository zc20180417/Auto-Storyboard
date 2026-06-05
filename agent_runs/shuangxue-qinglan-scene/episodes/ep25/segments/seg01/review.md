{
  "pass": true,
  "summary": "seg01 两组保留强盛建材证据链、经侦移交和赵强周美娟慌乱反应，时间轴与对白指向可交付。",
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "沈清约29字台词放在2.5-8秒的5.5秒内，约5.3字/秒，低于6.5硬上限。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "律师实名移交市经侦大队、赵强质问来真的、周美娟向父亲求救均按原剧本顺序保留。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "两组都固定在龙腾酒店宴会厅，大屏幕和人物站位从第1组组尾接到第2组组首。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "沈清为画面内真人对白，明确对赵强说道，没有心声或画外音混用。",
      "fix_instruction": "若不通过，应补明真实对白对象或改为画外音来源。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只有打响指切屏和沈清质问两个强节拍，8秒短组属于证据揭示加单句反击，没有硬凑长时长。",
      "fix_instruction": "若不通过，应拆出证据切屏或压缩非关键反应。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部大屏幕停在证据链，第2组组首继续显示同一证据链，律师文件夹位置连续。",
      "fix_instruction": "若不通过，应在组尾或组首补充大屏幕和律师文件夹状态。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "证据链由大屏幕承载，文件夹始终在律师手中，没有发生无过渡转移。",
      "fix_instruction": "若不通过，应补充文件夹递出或屏幕画面切换动作。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "律师陈述、赵强反应、周美娟求救分成三个时间段，每段只承载一个主对白节拍。",
      "fix_instruction": "若不通过，应拆分连续对白或弱化非主动作人物。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第1组视频禁止项聚焦证据链画面、赵强和律师三个本组锚点，数量为3条。",
      "fix_instruction": "若不通过，应删除泛泛项并替换成本组人物或道具锚点。"
    }
  ],
  "issues": [],
  "warnings": []
}
