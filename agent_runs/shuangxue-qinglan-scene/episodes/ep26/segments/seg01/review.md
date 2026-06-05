{
  "pass": true,
  "summary": "seg01保留沈清断绝父名、张总清算、保镖按倒和周桂兰拒绝求情的剧情链，时间与空间连续可执行。",
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
      "evidence": "沈清两句原台词完整保留，先否认周建国父亲身份，再把清算权交给张总，顺序与原剧本一致。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "evidence": "张总下令、保镖冲上、按倒周建国、周建国求救分成4个时间段，没有把冲上和按倒挤在同一镜。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "周桂兰约17字反击安排在6-10秒的4秒内，约4.3字/秒，冷声质问节奏自然且未超过6.5字/秒硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈清两句现场对白分别写明对周建国和在场众人、对张总说，口型对象明确。",
      "fix_instruction": "若不通过，应补足沈清对白对象。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "15秒内承载一条连续清算动作链，张总下令6秒、保镖动作6秒、周建国短求救3秒，强节拍按阶段拆开。",
      "fix_instruction": "若不通过，应拆出保镖按倒或周建国求救。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾部周建国低伏被控，第3组首保持同一地面状态，周桂兰位置也连续。",
      "fix_instruction": "若不通过，应在第2组尾或第3组首补周建国被控状态。"
    },
    {
      "group": "第3组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "按地和拒绝求情组提供4个本组特有禁止项，锚定周桂兰、周建国、沈清、张总和酒杯。",
      "fix_instruction": "若不通过，应删除泛化禁止项并替换为本组人物或道具锚点。"
    }
  ],
  "issues": [],
  "warnings": []
}
