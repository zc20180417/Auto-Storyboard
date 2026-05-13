{
  "pass": true,
  "summary": "seg01 分镜保留了第30集三处空间与全部关键台词，5组均满足10-15秒、单空间、声音口型和尾部衔接要求。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组"],
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
      "evidence": "第1组 6-10秒承载“涨停了！上市即涨停！”约9字/4秒，10-14秒承载“妈！咱们家发大财啦！”约9字/4秒，均低于6.5字/秒。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "第2组保留“这只是一个新起点”“启动希望小学捐建项目”“第一站定在哪里”“我的老家，远县北沟村”四个关键信息，且说话对象为助理或身旁众人。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "第3组全部发生在远县北沟村村口外，组首写明水泥大桥、赵朵朵、赵大雷、村长和村民位置，0-2.5秒全景有重卡驶过的剧情推进。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "evidence": "第4组承接第3组桥头状态，赵朵朵和赵大雷仍在村口桥头，重卡继续驶过，没有无过渡换空间。"
    },
    {
      "group": "第5组",
      "type": "filmability",
      "evidence": "第5组把家庭团圆转成端菜、夹肉、举杯、碰杯、吃红烧肉和看星空等可见动作，没有用抽象情绪替代画面。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "第1组所有台词均为画面内人物现场开口，铜钟“咚”的声音来自鼓槌敲钟动作，声音来源可见。",
      "fix_instruction": "无；保持铜钟声与敲钟动作同段呈现。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组为同一大厅内的连续决策对话，4个时间段分别承载新起点、转身下令、助理提问、确认老家，强节拍未过载。",
      "fix_instruction": "无；保持同空间连续对话节拍。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "村长对赵朵朵说道，村民们朝赵朵朵方向喊道，赵大雷和赵朵朵均对村民们说话，没有假对象对白。",
      "fix_instruction": "无；保持明确说话对象。"
    },
    {
      "group": "第4组",
      "type": "timing_math",
      "result": "pass",
      "evidence": "第4组时间段为0-3秒、3-7秒、7-13秒，总和13秒，与标题总时长和镜头数一致。",
      "fix_instruction": "无；保持整数总时长与0.5秒粒度合同。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "第5组保留大嫂端红烧肉、桂姨夹肉、赵大雷举杯、赵朵朵祝家里日子红火、碰杯、吃红烧肉看星空等原剧本收尾动作。",
      "fix_instruction": "无；保持温情收尾动作和台词顺序。"
    },
    {
      "group": "第5组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模型说明词、官方模板编号、参考图占位、自动分镜或模板化批量描述。",
      "fix_instruction": "无；保持自然分镜正文。"
    }
  ],
  "issues": [],
  "warnings": []
}
