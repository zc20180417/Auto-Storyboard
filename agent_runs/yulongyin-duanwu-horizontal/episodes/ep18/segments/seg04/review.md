{
  "pass": true,
  "summary": "第18集18-4分段拆为鼓声聚云与水龙入云两组，保留爸爸连续击鼓、太阳被乌云遮蔽、狂风沙石、天天震撼台词、水壶炸裂、水龙入雷云和紫雷。",
  "checked_groups": [
    "第1组",
    "第2组"
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
      "evidence": "爸爸疯狂击鼓、“咚！咚！咚！”、太阳被乌云遮蔽、狂风卷沙石、村民睁不开眼、天天喊“爸爸！天黑了！”均按原剧本顺序保留。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "水壶剧烈炸裂、金光与血色水龙虚影冲天、扎进墨色雷云、天际紫雷全部保留，未新增其他仪式动作。"
    },
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "evidence": "敞开祠堂门连接室内外，爸爸中央偏右击鼓，天天右前景，村民们左侧和门外后景，风从左侧卷入到右侧，横向调度明确。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "evidence": "第1组尾部水壶在爸爸胸前剧烈震颤，第2组首部仍是同一水壶在胸前鼓胀并裂开，人物位置和道具状态连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "天天“爸爸！天黑了！”约6个有效字在4秒动作段中承载，但该段同时包含仰望、转头和水壶震颤反应，未形成过快或过慢硬问题。",
      "fix_instruction": "若压缩该镜头，应保留天天先看天再对爸爸喊的动作关系。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "水壶从第1组胸前震颤，进入第2组胸前膨胀、裂纹蔓延、炸裂并释放水龙，关键道具状态递进完整。",
      "fix_instruction": "若修改水龙出现方式，应先展示壶裂或水光外溢，不要凭空出现。"
    },
    {
      "group": "第2组",
      "type": "filmability",
      "result": "pass",
      "evidence": "水龙虚影、墨云和紫雷均转译为可见光影、气浪、剪影和天空远景，不靠抽象说明承载剧情。",
      "fix_instruction": "若降低特效强度，也要保留水龙入云和紫雷两个可见结果。"
    },
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "原剧本18-4被拆为两组，第1组只处理击鼓、云遮日、狂风和天天台词，第2组再处理水壶炸裂与水龙入云，避免一组过载。",
      "fix_instruction": "不要把两组重新合并成单个15秒片段。"
    }
  ],
  "issues": [],
  "warnings": []
}
