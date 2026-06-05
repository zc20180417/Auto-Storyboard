{
  "pass": true,
  "summary": "seg03保留赵强公司账托词、沈清银行查证和非法侵占判断，以及刘美娟赵强烧旧账单的尾钩，动作与道具连续。",
  "checked_groups": ["第7组", "第8组", "第9组"],
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
      "group": "第7组",
      "type": "script_fidelity",
      "evidence": "赵强“合同都在公司走账呢”、沈清“钱根本不在我妈名下”、赵强“放谁名下不都一样嘛”均按原剧本顺序保留。"
    },
    {
      "group": "第8组",
      "type": "handoff_continuity",
      "evidence": "第7组尾部沈清持有传单和手机流水，第8组组首继续持有；第8组尾部沈清扶周桂兰向门口离开，第9组组首继承两人在门口附近背影。"
    },
    {
      "group": "第9组",
      "type": "action_atomicity",
      "evidence": "刘美娟腿软抓胳膊、低声问怎么办、赵强摸手机、赵强命令烧旧账单分四段执行，没有把抓人和打电话压成一个动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "赵强22字用4秒，沈清20字用3.5秒，赵强13字用2.5秒，均未超过6.5字/秒。",
      "fix_instruction": "若不通过，应延长对应对白或拆为短组。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "手机流水记录和广告宣传单从第7组延续到第8组沈清手中，离开时也由沈清带走，没有无过渡换手。",
      "fix_instruction": "若不通过，应补充道具归属或删除矛盾动作。"
    },
    {
      "group": "第9组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "刘美娟和赵强在组首明确位于客厅右侧并面向画左，沈清和周桂兰在门口附近背对镜头，所有参与动作人物均可用。",
      "fix_instruction": "若不通过，应在组首补足人物位置和朝向。"
    },
    {
      "group": "第9组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "第9组涉及手机和烧账单尾钩，视频禁止项锚定赵强手机、刘美娟抓胳膊、沈清周桂兰，不是泛泛模板词。",
      "fix_instruction": "若不通过，应替换为本组具体风险。"
    },
    {
      "group": "第8组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文保持自然短剧分镜格式，未出现模型说明词、工程占位符或模板编号。",
      "fix_instruction": "若不通过，应删除污染词。"
    }
  ],
  "issues": [],
  "warnings": []
}
