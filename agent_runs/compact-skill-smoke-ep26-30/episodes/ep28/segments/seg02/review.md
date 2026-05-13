{
  "pass": true,
  "summary": "seg02已对照剧本、生成规则和当前分镜逐组审核，破产消息、干警进门和走廊收束均保留，未发现阻断交付的硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组"
  ],
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
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "李少爷“那臭娘们破产没有？”放在3-7秒，约9个有效字/4秒；保镖“货全压在仓库了，不出三天准垮。”放在7-12秒，约16个有效字/5秒，节奏安全。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "evidence": "组首锁定李少爷、保镖和关闭的病房门；干警在0-3秒先推门进入并亮证，之后才开口宣布案由，人物可用性成立。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "evidence": "第2组尾部手铐打开、干警围到床边，第3组首部两名干警押着李少爷从开着的病房门走出，状态自然衔接。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "干警面对李少爷说案由和双规信息，李少爷面对干警反问，均为画面内可见人物现场开口。",
      "fix_instruction": "若不通过，应标明声音来源，或让说话人物进入画面后再开口。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "15秒内包含推门进场、亮证宣告、李少爷反问、干警打断并取手铐四个清楚节拍，台词段分别有5秒、3.5秒、3.5秒承载，未超过密度上限。",
      "fix_instruction": "若不通过，应把干警进门或双规信息拆成独立组。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "本组明确切到病房外走廊，组首锁定赵朵朵站位、病房门敞开、干警押人从门内出来，没有把走廊和病房混作同一镜头空间。",
      "fix_instruction": "若不通过，应独立锁定走廊空间并说明病房门与人物位置。"
    },
    {
      "group": "第1组至第3组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未写入模板编号、控制台占位符、广告语或视频工程说明，风格约束保持为自然短剧画面描述。",
      "fix_instruction": "若不通过，应删除污染词并改为具体人物动作、声音来源和道具状态。"
    }
  ],
  "issues": [],
  "warnings": []
}
