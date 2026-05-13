{
  "pass": true,
  "summary": "seg02 已对照原剧本、竖屏 generator 规则和当前分镜逐组审核；关键抓捕台词完整保留，走廊收束空间连续，无 hard issue。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组"
  ],
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
      "evidence": "李少爷得意喝红酒、询问“那臭娘们破产没有？”，保镖回答“货全压在仓库了，不出三天准垮。”以及干警推门进入均按原剧本保留。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "干警对李耀宗说明跨省洗钱案、李少爷惊恐提到父亲、干警完整说出“你父亲昨晚已经被双规了，带走！”均未删改，关键时间信息和命令保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "“李耀宗，你涉嫌参与跨省洗钱案。”给4秒，“你们敢抓我？我爸是……”给3秒，“你父亲昨晚已经被双规了，带走！”给5秒并含扣押动作，均低于6.5字/秒硬上限。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "evidence": "第2组尾部两名干警已架住李少爷且病房门敞开；第3组首在走廊左侧放置赵朵朵，门内可见干警架住李少爷，随后0-4秒完成押出门，空间衔接清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首只写李少爷、保镖、门和红酒杯的第一帧已成立状态；干警进入放在6-9秒动作段，没有把入场过程写进组首。",
      "fix_instruction": "若不通过，应将推门、进入等过程动作移入时间段。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "“你父亲昨晚已经被双规了，带走！”完整保留，没有缩写为“已被双规”或删掉“昨晚”“带走”。",
      "fix_instruction": "若不通过，应恢复该句完整台词和干警冷脸下令的对象。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "李少爷被押出后对赵朵朵喊“是你！是你交的证据！”，赵朵朵对李少爷回应“多行不义必自毙。”，双方对象明确。",
      "fix_instruction": "若不通过，应补写对话对象，不能写成无对象自语。"
    },
    {
      "group": "第1组-第3组",
      "type": "timing_math",
      "result": "pass",
      "evidence": "三组总时长分别为12、12、10秒，时间段连续且镜头数与标题一致，没有4-9秒短组。",
      "fix_instruction": "若不通过，应修正时间段、标题时长或镜头数，使每组相加一致。"
    },
    {
      "group": "第1组-第3组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现官方模板编号、参考图占位、首尾帧、自动分镜或模板化批量描述，保持自然短剧分镜文本。",
      "fix_instruction": "若出现污染词，应删除工程说明，改写为具体画面和声音来源。"
    }
  ],
  "issues": [],
  "warnings": []
}
