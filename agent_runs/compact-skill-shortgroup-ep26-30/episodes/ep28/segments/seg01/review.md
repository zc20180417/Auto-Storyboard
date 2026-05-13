{
  "pass": true,
  "summary": "seg01 已对照原剧本、竖屏 generator 规则和当前分镜逐组审核；关键台词、道具、空间锁定、时间轴和对话对象均可交付，无 hard issue。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组"
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
      "type": "script_fidelity",
      "evidence": "原剧本中李少爷扫落水果、怒吼“废了我的手！我要她全家死！”、保镖说明顾家倒了、李少爷命令“给京城打电话！断她所有的货运专线！”均在本组保留，未压缩成摘要。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "“封杀她！一瓶果冻也别想运出省！”安排在3.5秒，“李少，您的手骨碎裂，很难复原了。”安排在3.5秒，“滚！我要让赵朵朵求生不得求死不能！”安排在5秒，均未超过6.5字/秒硬上限。"
    },
    {
      "group": "第3组",
      "type": "space_locking",
      "evidence": "本组固定在罐头厂办公室，组首已给出赵朵朵、赵大雷、物流经理和退货单的位置，后续动作只在同一办公室内推进。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "U盘在组首位于赵朵朵面前桌角，4-8秒被赵朵朵拿起，8-12秒递给赵大雷，组尾赵大雷接住U盘，道具归属连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "李少爷对保镖怒吼和命令，保镖对李少爷回报，真人对白对象明确，没有对空气或道具说话。",
      "fix_instruction": "若不通过，应把每句真人对白改成明确的说话人对真实在场对象说。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组包含封杀命令、医生说明伤势、踹倒医生和威胁四个强节拍，12秒内每个节拍有独立时间段或动作承载，未把两个剧情目标硬压成一个镜头。",
      "fix_instruction": "若不通过，应拆出医生报伤或踹倒医生的独立组，不能删改台词。"
    },
    {
      "group": "第3组",
      "type": "timing_math",
      "result": "pass",
      "evidence": "本组总时长13秒，时间段0-3、3-6、6-9.5、9.5-13连续，镜头数4个与标题一致。",
      "fix_instruction": "若不通过，应调整标题总时长、镜头数或时间段边界，使其连续并相加一致。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "赵朵朵冷笑反击、拿U盘说明顾家账本和李家分红、递给大哥要求寄给京城纪委均按原剧本保留，未新增改变因果的动作。",
      "fix_instruction": "若不通过，应恢复原台词和U盘交接动作，只允许补充可见过渡。"
    },
    {
      "group": "第1组-第4组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现Seedance模板编号、参考图占位、自动分镜、模板说明或“空间先被交代出来”等污染词。",
      "fix_instruction": "若出现污染词，应删除工程说明，改写为自然可见的画面动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
