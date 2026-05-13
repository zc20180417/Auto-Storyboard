{
  "pass": true,
  "summary": "已对第28集单段分镜的10组逐项核对原剧本、竖屏生成规则、台词承载、时长与空间连续性，未发现硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组",
    "第8组",
    "第9组",
    "第10组"
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
      "evidence": "9-13秒连续承载林小满8字、许安3字、唐婶9字，共20字/4秒=5.0字/秒，未超过6.5字/秒；主持、韩彪、帮工乙、路人对白也分别有2.5秒、3秒、3.5秒承载。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "保留韩彪质问“许安，你还守这一套？”、“评选看的是场面。”以及许安回应“够用。”“最后留下的，不是场面。”，未改变两人对峙关系和肉串火候动作。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "3-7秒路人甲、路人乙两句共21字/4秒=5.25字/秒；7-10秒评委乙和林小满两句共12字/3秒=4.0字/秒，节奏可表演。"
    },
    {
      "group": "第8组",
      "type": "handoff_continuity",
      "evidence": "第7组尾部韩彪已在花样台旁盯住许安，第8组组首复述韩彪在画面左侧前景面向许安，许安仍在旧炭炉后，评委位于中央偏后，位置连续。"
    },
    {
      "group": "第10组",
      "type": "audio_mouth_sync",
      "evidence": "许安OS“这才是最后一局。”写成内心声音，并明确“嘴唇闭合不做口型”，没有让画面人物现场开口承载心声。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定同一夜市评选现场，左右两摊、主持人、路人、许安、韩彪、林小满、唐婶和帮工乙均有画面位置与朝向。",
      "fix_instruction": "若不通过，应在组首补齐每位开口人物的位置、朝向和关键道具状态。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组主要承载韩彪花样展示、许安落第一把肉串和两轮短句对峙，4个时间段共13秒，没有叠加新道具转移或跨空间事件。",
      "fix_instruction": "若不通过，应拆开花样展示和对峙对白，或压缩无关动作。"
    },
    {
      "group": "第3组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "评委甲、评委乙、韩彪和阿顺均在组首空间内可见，阿顺在烤炉旁持夹子，后续看火紧张动作有可用位置。",
      "fix_instruction": "若不通过，应在组首补阿顺位于韩彪身后烤炉旁，或安排他先入场再行动。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留第一轮后人群往回走、两名路人评价韩彪口味重和许安舒服、评委乙要求许安再来一把、林小满应声的剧情顺序。",
      "fix_instruction": "若不通过，应按原剧本顺序恢复人群回流、评价、评委点名和林小满回应。"
    },
    {
      "group": "第6组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "韩彪两句均明确对阿顺喊/说道，阿顺对韩彪回应“人太多了。”，没有假对白对象或对象缺失。",
      "fix_instruction": "若不通过，应把每句现场对白改为明确的A对B说道/喊道。"
    },
    {
      "group": "第8组",
      "type": "timing_math",
      "result": "pass",
      "evidence": "第8组时间段为0-3.5、3.5-6、6-9、9-12秒，连续且合计12秒，标题镜头数4个与时间段一致。",
      "fix_instruction": "若不通过，应修正时间段连续性、总时长或标题镜头数。"
    },
    {
      "group": "第9组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "评委乙宣布“不比花样，只比最基础的炭火肉串。”、林小满说“来了。”、韩彪反问“只比肉串？”、评委甲确认“对。谁都别藏了。”均完整保留。",
      "fix_instruction": "若不通过，应恢复最后一轮规则宣布及各角色反应台词。"
    },
    {
      "group": "第10组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终文本没有出现模板编号、参考图占位符、视频延长、自动分镜或非短剧模板语气；结尾只保留自然分镜描述和固定负面提示。",
      "fix_instruction": "若不通过，应删除模型说明词、模板编号、参考占位符或广告/MV类语气。"
    }
  ],
  "issues": [],
  "warnings": []
}
