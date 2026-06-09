{
  "pass": true,
  "summary": "seg03分镜忠实原剧本，沈清拦人对峙节奏清楚，台词指向完整。",
  "checked_groups": ["第3组"],
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
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "沈清4字+周美娟6字=10字÷2秒=5字/秒含拦人动作，周美娟5字÷2秒=2.5字/秒含退缩反应，沈清10字÷2秒=5字/秒含举手机，赵强9字÷2秒=4.5字/秒，沈清7字÷2秒=3.5字/秒含输入动作，均在合理范围内。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "单一物理空间周家正屋客厅，组首列出全部在场人物位置，沈清持有手机和银行卡，道具状态从上一组连续。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "5句对白全部保留原词，沈清拦人动作和输入转账信息动作忠实原剧本。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有对白均为画面内现场开口，每句写明说话人和对象。",
      "fix_instruction": "若不通过，应补充说话人和对象指向。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "强节拍3个（沈清拦人、赵强怒喝、沈清输入转账信息），属同一对峙链的连续推进，每段只承载一个主动作。",
      "fix_instruction": "若不通过，应拆分强节拍或延长组时长。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "组首从上一组组尾继承：沈清持手机和银行卡，周美娟原位攥包。组尾写明沈清手机屏幕亮着、周美娟被拦在原地。",
      "fix_instruction": "若不通过，应在组首补充具体人物位置和道具状态。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "手机和银行卡在沈清手中保持连续，组尾明确锚定手机屏幕亮着、银行卡在另一只手中。",
      "fix_instruction": "若不通过，应补充道具状态过渡动作。"
    },
    {
      "group": "第3组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "5个时间段各承载一个主动作，无过载。",
      "fix_instruction": "若不通过，应拆分过载时间段。"
    },
    {
      "group": "第3组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "本组为对峙对话组，拦人动作简单明确，省略视频禁止项合理。",
      "fix_instruction": "若不通过，应补充2-5个本组特有视频禁止项。"
    }
  ],
  "issues": [],
  "warnings": []
}
