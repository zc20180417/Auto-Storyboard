{
  "pass": true,
  "summary": "seg02 两组完整保留审批局争执，文件、印章、人物站位和对白对象清楚。",
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
      "evidence": "江若晴拍文件质问、张局长以生态评估推诿、陆凡指出半个月拖延均与原剧本一致。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "张局长约23字台词用5秒，约4.6字/秒；江若晴约15字用3.5秒，约4.3字/秒并有愤怒动作承载，未超过硬上限。"
    },
    {
      "group": "第4组",
      "type": "dialogue_direction",
      "evidence": "张局长对两人说，江若晴对张局长说，陆凡对江若晴说，对白对象没有缺失或假对象。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首列明办公室内三人的画面位置、身体朝向、文件和印章盒位置，没有过程动作写入组首。",
      "fix_instruction": "若不通过，应把入场或拍文件动作移入时间段。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾陆凡站在江若晴身后与张局长对视，第4组首保持同一办公室站位和文件状态。",
      "fix_instruction": "若不通过，应在组首复述上一组结束的人物位置和道具状态。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载张局长傲慢回应、江若晴威胁举报、陆凡拉住她三段同空间对白动作，13秒内节奏清楚。",
      "fix_instruction": "若不通过，应拆出陆凡拉住江若晴的动作或缩短非关键反应。"
    }
  ],
  "issues": [],
  "warnings": []
}
