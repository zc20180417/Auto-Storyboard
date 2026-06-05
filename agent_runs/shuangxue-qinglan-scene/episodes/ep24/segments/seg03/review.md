{
  "pass": true,
  "summary": "seg03 将周建国要钱、五百万勒索、律师定性和沈清反击拆成两组，短组理由成立。",
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
      "evidence": "第1组0-4.5秒约27字，约6.0字/秒；4.5-9.5秒约27字，约5.4字/秒；9.5-15秒约30字，约5.45字/秒，均低于6.5。"
    },
    {
      "group": "第2组",
      "type": "timing_math",
      "evidence": "第2组为9秒短反击组，时间段0-3.5、3.5-9连续，镜头数2个，属于不可硬凑的短句转折。"
    },
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "周建国家事辩解、五百万赡养费威胁、律师敲诈勒索定性、沈清两句反击均按原台词顺序保留。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "前一段入口隔离状态延续到第1组组首，周建国半蹲僵住，律师手机对准他。",
      "fix_instruction": "若不通过，应在组尾或组首补安保隔离和手机录像状态。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组只承载沈清两句反击和扫视三人的轻动作，9秒短组没有用停顿硬凑10秒。",
      "fix_instruction": "若密度不足，应保持短组或并入同场冲突，不能添加无剧情停顿。"
    },
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "周建国分别对律师、沈清说话，律师对周建国说话，沈清对周建国或三人说话，未出现假对白对象。",
      "fix_instruction": "若不通过，应补清真实对话对象。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "两组正文未出现Seedance说明、参考模板、JSON或模板化批量句。",
      "fix_instruction": "若污染，应删除工程说明并改自然分镜文本。"
    }
  ],
  "issues": [],
  "warnings": [
    {
      "severity": "soft",
      "group": "第2组",
      "rule": "timing_math",
      "problem": "第2组为9秒短组。",
      "evidence": "本组仅承载沈清两句短反击，强行扩到10秒以上会依赖普通停顿。",
      "fix": "保留短组即可，交付说明中说明为短句反击。"
    }
  ]
}
