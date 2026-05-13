{
  "pass": true,
  "summary": "对照seg01脚本、竖屏生成规则和当前分镜，6组完整保留韩彪加桌抢客、路人口味对比、唐婶带动回流、韩彪决定断货、肉贩避开许安、后门马会听见威胁等关键剧情，未发现硬问题。",
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
    "prompt_pollution": "checked",
    "prop_continuity": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "阿顺0-2.5秒喊客约12个有效字，2.5秒承载约4.8字/秒；韩彪2.5-5.5秒约16个有效字，3秒承载约5.3字/秒；林小满和许安5.5-8.5秒两句约16个有效字，3秒承载约5.3字/秒，均未超过6.5字/秒硬上限。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "唐婶带邻居坐下、邻居甲评价韩彪那边看着多吃着空、邻居乙承认许安这边真实在、唐婶拍桌、林小满顺势接单、许安提醒辣度、邻居甲追加二十串，台词顺序和因果均与原剧本一致。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "本组单一物理空间为夜晚肉贩摊位街，组首列出许安、肉贩甲乙丙的位置和朝向；许安先到摊前，肉贩随后低头收摊，没有让未入场人物直接参与动作。"
    },
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "evidence": "韩彪0-2.5秒持手机对电话那头说断货威胁，声音来源和口型属于画面中的韩彪；后续马会与韩彪面对面对话，均写明真实说话对象。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "阿顺对路人、韩彪对街边路人、林小满对许安、许安对林小满、路人甲对路人乙、路人乙对路人甲均有明确现场对白对象。",
      "fix_instruction": "若不通过，应补清每句真人对白的说话对象，避免无对象喊话或假对象承载。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "两边同时出串、年轻人边吃边比、韩彪质疑差一口、许安回应差的是心、韩彪冷笑少装均被保留，没有新增改变剧情的动作。",
      "fix_instruction": "若不通过，应补回缺失的比串动作或恢复韩彪与许安的原台词顺序。"
    },
    {
      "group": "第3组",
      "type": "timing_math",
      "result": "pass",
      "evidence": "第3组标题总时长15秒，时间段0-2、2-6、6-9、9-12.5、12.5-15秒连续，末段结束于15秒，镜头数5个与标题一致。",
      "fix_instruction": "若不通过，应修正标题总时长、时间段连续性或镜头数。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载排队回流、韩彪低声决策、阿顺确认、韩彪反压和阿顺沉默五个清晰节拍，总时长13秒，台词短且动作轻，没有把外部事件、长动作和关键道具操作挤在同一时间段。",
      "fix_instruction": "若不通过，应拆分排队反应与断货决策，或压缩非关键反应。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "许安收摊后去进货，熟识肉贩见他过来纷纷低头收摊，被转译为冰柜盖合、肉钩晃动、卷帘门半落和许安空篮停住，剧情含义未改写。",
      "fix_instruction": "若不通过，应保留许安进货受阻和肉贩回避的关键状态，不要改成明确拒绝台词或新增冲突。"
    },
    {
      "group": "第6组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "马会在组首位于后门内侧阴影处，2.5-4.5秒先走到门边并停住，再开口质问韩彪；韩彪从组首即持手机可用，人物出场顺序清楚。",
      "fix_instruction": "若不通过，应在组首或前半段补充马会的可见位置和入场动作。"
    },
    {
      "group": "第6组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "分镜正文为自然短剧画面描述，未出现模型说明词、模板编号、占位符、参考图、广告化话术或横屏字段。",
      "fix_instruction": "若不通过，应删除污染词并改写为人物动作、声音来源、道具状态和可见反应。"
    }
  ],
  "issues": [],
  "warnings": []
}
