{
  "pass": true,
  "summary": "第1组爸爸把天天和云宝托付给山路已按原剧本、横屏调度、台词节奏和可生成性完成审核，未发现阻断交付的硬问题。",
  "checked_groups": [
    "第1组"
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "保留爸爸交代找泉眼、天天拉住爸爸拒绝、云宝探头吐水泡、爸爸摸头承诺和冷酷宣言。"
    },
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "evidence": "爸爸在左侧蹲下并站起，天天和水壶在右侧，右侧山路通向泉眼，云宝以水壶道具焦点出现。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "爸爸首句约21字/3.5秒约6.0字秒比，天天拒绝句约15字/3秒约5.0字秒比，其余台词均在安全范围；全组15秒5镜头。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "爸爸对天天交代和承诺，天天对爸爸回应，云宝只以水泡动作表达焦急，没有新增台词。",
      "fix_instruction": "已通过；若后续修改台词，保持说话对象和声音来源明确。"
    },
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定爸爸左、天天右、水壶在天天怀里、山路向右延伸，站起后位置与组尾承接明确。",
      "fix_instruction": "已通过；若后续改镜头，保留组首左右、前后景和关键道具位置。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、参考图占位、视频延长、自动分镜等工程说明词；负向词仅用于排除竖屏构图。",
      "fix_instruction": "已通过；不要加入模型模板说明或控制台占位符。"
    }
  ],
  "issues": [],
  "warnings": []
}
