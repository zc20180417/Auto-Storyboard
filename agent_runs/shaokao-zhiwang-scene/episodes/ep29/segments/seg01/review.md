{
  "pass": true,
  "summary": "已对照第29集分段剧本和竖屏生成规则检查，9组分镜保留最后一轮备料、出串评判和韩彪拦路指控的关键台词与动作，未发现阻断问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组",
    "第8组",
    "第9组"
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
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "原剧本中韩秀兰说“你爸那口火，不能少个人送你上场”并递出父亲留下的旧炭夹；分镜0-5秒保留台词，5-8秒保留布包取炭夹、递给许安、许安指节收紧的关键动作。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "3-6秒、6-9秒、9-12秒分别承载8字、8字、6字短句，12-15秒承载评委乙与许安共9字对白，均低于6.5字/秒硬上限。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "evidence": "组首写明韩彪手中持有一把烤串，3-7秒递到评委面前，7-9秒评委甲接过并咬下，烤串归属变化有可见过渡。"
    },
    {
      "group": "第8组",
      "type": "handoff_continuity",
      "evidence": "第7组组尾写明许安守在炉旁、韩彪在评委桌旁笑意僵住；第8组组首延续韩彪在评委桌旁、许安在旧炭炉前，并在4-7秒写出韩彪冲到许安面前的过渡。"
    },
    {
      "group": "第9组",
      "type": "script_fidelity",
      "evidence": "韩秀兰“韩彪，别再闹。”、许安“我逼你？”、韩彪“你抢客，抢名，抢招牌，不就是要我死？”均按原顺序保留，并以全场静住作为剧本收尾。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "韩秀兰在组首已位于通道入口并持有布包，林小满、许安、韩彪、阿顺、评委均有位置和朝向，后续说话人物均可用。",
      "fix_instruction": "若不通过，应在组首补足人物画面位置、身体朝向和可见状态，或把入场动作提前到说话前。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "布包在组首贴在韩秀兰身前，5-8秒打开布包取出旧炭夹并递给许安，10.5-13秒许安已握紧旧炭夹，关键道具转移清楚。",
      "fix_instruction": "若不通过，应补充递出、接住或放置的可见动作，避免炭夹突然变更归属。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组核心为重料与稳火对照、三句围观评价、评委乙发令，动作和对白按5个短时间段拆开，没有把评判、冲突和结果宣布挤在同组。",
      "fix_instruction": "若不通过，应将出串或评委试吃拆到下一组，或压缩非关键围观反应。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "result": "pass",
      "evidence": "10-12秒“这把火稳”4字，12-14秒“肉也干净”“就是这口”合计8字，字秒比均未超过硬上限，并与评委和唐婶反应同步。",
      "fix_instruction": "若不通过，应延长对应时间段或拆分唐婶反应。"
    },
    {
      "group": "第8组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "本组均为现场人物开口对白，韩彪对许安、林小满对韩彪、唐婶对韩彪的对象明确，没有心声或画外音误写成口型。",
      "fix_instruction": "若不通过，应改成明确现场说话对象，或为画外音补充声音来源和闭口反应。"
    },
    {
      "group": "第9组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第8组结尾韩彪拦在许安面前、林小满半挡；第9组组首复述韩彪拦在中央偏左、许安位于中央偏右、林小满在两人之间，状态连续。",
      "fix_instruction": "若不通过，应在第8组组尾或第9组组首补充两人相对位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
