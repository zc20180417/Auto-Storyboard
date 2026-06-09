{
  "pass": true,
  "summary": "seg03含第4组，沈清拿出手机拨打110报警，赵强扑抢手机，台词忠实、道具连续。",
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
      "type": "generation_density",
      "evidence": "14秒6时间段，强节拍6个（耍赖、冷声回应、拨110、惊慌、宣读法律、扑抢），属报警事件连续链，每段一个主动作。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "沈清'盗窃十九万，数额巨大，够判三年以上了'15字÷3秒=5字/秒，赵强'别别别！清清，有话好说！'9字÷1.5秒=6字/秒，均在6.5硬上限内。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "台词'钱都花光了！要命有一条！''花光了？没关系，父债子偿。'等与原剧本17-3完全一致。沈清按下110的动作通过特写镜头呈现。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "每个时间段一个主动作：周美娟耍赖→沈清回应→掏手机按键→周美娟惊慌→沈清宣读→赵强扑抢。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "房产证从第3组左手持有延续到第4组左手持有，手机在4.5秒掏出并保持到组尾，道具状态连续。",
      "fix_instruction": "无需修改。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾沈清左手持房产证→第4组首沈清左手持房产证，周美娟和赵强位置延续，状态连续。",
      "fix_instruction": "无需修改。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第4组",
      "rule": "generation_density",
      "problem": "14秒6个时间段承载报警完整流程，强节拍密度偏高但属同一事件链",
      "evidence": "强节拍6个均为报警事件连续阶段，每段一个主动作。",
      "fix": "可考虑将赵强扑抢移至第5组开头，但当前安排在剧情节奏上也可接受。"
    }
  ]
}
