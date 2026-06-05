{
  "pass": true,
  "summary": "seg02 按阶段呈现刘美娟进门、拉周桂兰、沈清追问8864手机和保管借口，人物站位、道具和台词均可执行。",
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
      "type": "action_atomicity",
      "evidence": "刘美娟推门、穿过大厅、拉周桂兰手腕、假笑说台词被拆成4个时间段，外部入场没有压缩成单镜。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "沈清“放手！你怎么知道我们在银行？”、刘美娟“我……我路过看见你们进来了。”和8864手机质问按原顺序保留。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "刘美娟最后一句约19字承载在6-12秒，约3.2字/秒，配合咬牙和捂包动作，未超过6.5字/秒硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首把刘美娟置于银行玻璃大门内侧远处，后续先入场再拉人和开口，人物可用性成立。",
      "fix_instruction": "若不通过，应把刘美娟放在门内可见位置或增加入场前状态。"
    },
    {
      "group": "第1组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "禁止项锚定刘美娟名牌包、拉周桂兰、周桂兰位置和老年机状态，都是本组关键执行风险。",
      "fix_instruction": "若不通过，应替换泛泛禁止项为本组人物和道具风险。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "名牌包从刘美娟肩上到被她下意识捂住，老年机仍在沈清手中，银行卡仍在柜台凹槽旁。",
      "fix_instruction": "若不通过，应补包、老年机或银行卡归属位置。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组为同一对峙目标下的短句追问与捂包反应，4个时间段内没有多主动作抢焦点。",
      "fix_instruction": "若不通过，应拆出捂包反应或压缩非关键反应。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾刘美娟捂包、沈清挡在周桂兰前，第3组组首继续保持同样站位和道具状态。",
      "fix_instruction": "若不通过，应在组首复述沈清、周桂兰、刘美娟与名牌包状态。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "刘美娟和沈清所有现场对白均明确对沈清或刘美娟说道，没有假对象或对象缺失。",
      "fix_instruction": "若不通过，应逐句补充真实对话对象。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有出现Seedance说明词、参考模板、占位符或模板化批量描述。",
      "fix_instruction": "若不通过，应删除工程词和模板语气。"
    }
  ],
  "issues": [],
  "warnings": []
}
