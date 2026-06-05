{
  "pass": true,
  "summary": "seg01 保留诉状逼签、周建国签字按印、沈清切割关系和五百万债务反击，未发现 hard issue。",
  "checked_groups": ["第1组", "第2组", "第3组"],
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
      "type": "script_fidelity",
      "evidence": "原剧本中债主律师拍下强制执行诉状、张总喝令查封祖宅、周建国喊我签均保留，且未新增改变结果的动作。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "离婚协议书从桌面到周建国签字按印，再到沈清手中，有签字笔、印泥和红色指印的可见过渡。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "沈清约25字用5秒承载，约5字/秒；周建国约10字用3秒且带嘶吼动作，未超过6.5字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "本组固定在龙腾酒店宴会厅，周建国、张总、律师、沈清的位置和朝向在组首均已写明。",
      "fix_instruction": "若不通过，应补齐第一帧在场人物的位置、身体朝向和桌面道具状态。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "签字、按手印、沈清拿起协议、沈清宣告关系切割分别占用独立时间段，没有把多段主动作挤进同一镜。",
      "fix_instruction": "若不通过，应拆开签字、按手印和拿协议动作。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组是五百万债务落地后的短句反击和绝望嘶吼，8秒属于极短戏剧节拍，不靠普通停顿凑时长。",
      "fix_instruction": "若不通过，应与前组重组或压缩普通反应，不能硬拉到10秒。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定离婚协议书、周建国和沈清，限制手印缺失和错误签字主体，数量为3条。",
      "fix_instruction": "若不通过，应删除泛泛禁止项并改成具体人物或道具错误。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明、官方模板编号、参考图占位符或模板化批量描述。",
      "fix_instruction": "若不通过，应删除模型词和模板说明，改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
