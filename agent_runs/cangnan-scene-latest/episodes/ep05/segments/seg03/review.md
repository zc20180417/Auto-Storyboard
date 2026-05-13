{
  "pass": true,
  "summary": "seg03已按电话音和办公室空间规则完成审核，赵大江与徐虎通话的声音来源、口型和剧情因果清楚。",
  "checked_groups": ["第6组", "第7组"],
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
      "group": "第6组",
      "type": "audio_mouth_sync",
      "evidence": "徐虎只以座机听筒里的电话音出现，第6组7.5-12秒明确赵大江嘴唇闭合不做口型。"
    },
    {
      "group": "第7组",
      "type": "script_fidelity",
      "evidence": "第7组保留赵大江冷笑判断鱼干运不出去、徐虎汇报兄弟守路、赵大江叮嘱别出人命以及挂电话喝茶。"
    },
    {
      "group": "第7组",
      "type": "dialogue_pacing",
      "evidence": "第7组0-3.5秒约18字、3.5-7秒约19字、7-10秒约13字，字秒比均未超过6.5。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第6组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "赵大江在组首坐于办公桌后，徐虎声明为电话音来源，不需要画面入场。",
      "fix_instruction": "若把徐虎写成画面人物，应补充入场或改回电话音。"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第6组尾部赵大江握听筒听电话，第7组组首延续手中持有座机听筒。",
      "fix_instruction": "若电话状态变化，应写出放下、重拨或继续通话的过渡。"
    },
    {
      "group": "第7组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第7组为同一通电话内三句短对白加挂断喝茶动作，13秒内节拍清楚。",
      "fix_instruction": "若加入新的外部事件或他人入场，应拆组。"
    },
    {
      "group": "第6组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "两个办公室组均为自然分镜正文，未出现模型说明词或模板占位。",
      "fix_instruction": "若出现工程说明，应删除并改为可见动作和声音来源。"
    }
  ],
  "issues": [],
  "warnings": []
}
