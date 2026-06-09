{
  "pass": true,
  "summary": "ep14 单段分镜保留倒计时公开、法务电话、停车场录音笔威胁、安全屋推理备份冷库等关键剧情，未发现阻断交付的硬问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组"],
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
      "type": "audio_mouth_sync",
      "evidence": "顾北辰 OS 写明嘴唇闭合、不做口型，许知夏现场边跑边说的长台词对象为身后的顾北辰。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "evidence": "秦越在车辆旁持有小型录音笔，9-13秒特写刻字 X·Z·N，组尾继续锚定录音笔在秦越手中。"
    },
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "evidence": "法务只通过手机免提声音出现，许知夏听电话时嘴唇闭合，随后对手机免提里的法务回应。"
    },
    {
      "group": "第8组",
      "type": "dialogue_pacing",
      "evidence": "许知夏关于地下档案室、秦越拿走录音笔和编号的台词约 36 字给 7 秒，约 5.1 字/秒，低于 6.5 字/秒硬上限。"
    },
    {
      "group": "第9组",
      "type": "script_fidelity",
      "evidence": "顾北辰说明地下档案库下有冷库、许知夏确认录音笔有备份、顾北辰判断秦越今晚会清库，三处推理因果均保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "timing_math",
      "result": "pass",
      "evidence": "15秒组内时间段为0-2、2-10、10-12.5、12.5-15，连续且使用0.5秒粒度，镜头数4个一致。",
      "fix_instruction": "若不通过，应修正时间段连续性或标题镜头数。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "许知夏对耳机里的法务说道，顾北辰对许知夏说道，许知夏对顾北辰说道，所有现场对白对象明确。",
      "fix_instruction": "若不通过，应补足A对B说道的对象。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "秦越把玩录音笔、顾北辰护身提问、秦越收录音笔开车门、秦越威胁四个节拍分布在15秒内，没有同时塞进单镜。",
      "fix_instruction": "若不通过，应拆出开车门或收录音笔动作。"
    },
    {
      "group": "第5组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第4组尾秦越在打开车门旁，第5组首仍在车门旁持录音笔，随后坐进车内离开，人物和车门状态连续。",
      "fix_instruction": "若不通过，应在第4组尾或第5组首补车门和录音笔状态。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "顾北辰关于秦越故意亮录音笔的判断写为嘴唇闭合、不做口型的心声，未误写成现场开口。",
      "fix_instruction": "若不通过，应明确心声闭口，或改成现场对白并给对象。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "父亲视频截图从许知夏手机中翻出，ST-CLD-A17编号被特写并在组尾继续由许知夏举着给顾北辰查看。",
      "fix_instruction": "若不通过，应补充截图来源和编号持续可见状态。"
    },
    {
      "group": "第9组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定冷库编号、许知夏、顾北辰清库时间和桌上盛远文件，共4项，均为本组具体风险。",
      "fix_instruction": "若不通过，应替换泛化禁止项并锚定本组人物道具。"
    }
  ],
  "issues": [],
  "warnings": []
}
