{
  "pass": true,
  "summary": "seg01 已对照第11集剧本和竖屏生成规则审完，6组均保留原剧本台词、人物关系、空间转换和柴油缺失悬念，无阻断硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组"
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
      "evidence": "剧本中村民甲“砚川，山下又上来一拨！”、村民乙“我家老头走不动了！”、沈砚川“老人进仓房左边，孩子都到棚里。”和周大柱“听见没！别乱！”均按原顺序保留，未新增改变剧情的动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "赵有福询问、沈砚川回应、林知夏报受伤人数、沈小禾分热水分别放在3秒、2秒、4秒、4秒时间段内；最长对白“这边三个受伤的，要腾地方。”约12字/4秒，低于6.5字/秒硬上限。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "第4组进入果园仓房内后，组首锁定墙面、粮袋、被褥、油灯和沈砚川、赵有福、林知夏、村民甲、老人位置，后续划线分区、问答和安排睡处都发生在同一仓房空间。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "evidence": "柴油桶以墙角两个空位呈现，林知夏先依据登记木板发现缺口，沈小禾确认“刚才还在”，周大柱再入场追问，关键道具状态和信息揭示连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "沈砚川、周大柱、村民甲、村民乙、老人和孩子均在组首拥有明确位置和朝向，所有开口人物在说话前已可见。",
      "fix_instruction": "若不通过，应在组首补齐说话人物的位置、身体朝向和可见状态，或在开口前写明入场。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "村民丙对沈砚川喊“我粮袋不能离身！”，沈砚川对村民丙说“不登记，丢了别找我。”，对白对象真实且未发明假对象。",
      "fix_instruction": "若不通过，应把无对象对白改为A对B说道，且对象必须是画面内真实人物。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载粮袋统一堆放、赵有福请缨和沈砚川反压三项强节拍，13秒内分为4个时间段，动作和对白没有硬挤。",
      "fix_instruction": "若不通过，应拆出赵有福请缨或粮袋堆放动作，避免同组过载。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾部物资区和登记状态延续到第6组组首；第6组内仓门半开、周大柱在门外阴影中可用，随后冲入发问，结尾关门查油形成自然收束。",
      "fix_instruction": "若不通过，应在第6组组首补具体仓门状态、人物位置或在周大柱发问前补入场动作。"
    },
    {
      "group": "第6组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现Seedance说明、模板编号、参考图占位符、自动分镜、字幕、广告式话术或项目内部说明。",
      "fix_instruction": "若不通过，应删除模型说明词和工程占位符，改为自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
