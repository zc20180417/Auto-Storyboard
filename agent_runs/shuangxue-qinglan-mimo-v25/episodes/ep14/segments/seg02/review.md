{
  "pass": true,
  "summary": "seg02分镜忠实原剧本，卡号验证流程清楚，周美娟慌乱反应节奏自然。",
  "checked_groups": ["第2组"],
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
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "沈清5字÷1.5秒=3.3字/秒含开APP动作，周建国5字÷2秒=2.5字/秒，沈清+周桂兰16字÷3.5秒=4.6字/秒，周美娟5字÷2秒=2.5字/秒含退缩反应，5字÷2秒=2.5字/秒含拉人动作，均在合理范围内。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "单一物理空间周家正屋客厅，组首列出5人位置，沈清手中持有银行卡，道具状态从上一组连续。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "5句对白全部保留原词，沈清核对卡号流程完整，周美娟慌乱喊爸和催促离开均忠实原剧本。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有对白均为画面内现场开口，每句写明说话人和对象。",
      "fix_instruction": "若不通过，应补充说话人和对象指向。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "强节拍3个，属同一验证流程的连续推进，每段只有一个主动作。",
      "fix_instruction": "若不通过，应拆分强节拍或延长组时长。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "组首从上一组组尾继承：沈清持有银行卡，周美娟原位攥包。组尾写明沈清持手机和银行卡。",
      "fix_instruction": "若不通过，应在组首补充具体人物位置和道具状态。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "旧银行卡从上一组沈清手中延续，本组内沈清翻看后打开手机APP核对卡号，道具状态连续。",
      "fix_instruction": "若不通过，应补充道具状态过渡动作。"
    },
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "5个时间段各承载一个主动作或连续对话节拍，无过载。",
      "fix_instruction": "若不通过，应拆分过载时间段。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "本组为对话验证组，无复杂动作/保护站位，省略视频禁止项合理。",
      "fix_instruction": "若不通过，应补充2-5个本组特有视频禁止项。"
    }
  ],
  "issues": [],
  "warnings": []
}
