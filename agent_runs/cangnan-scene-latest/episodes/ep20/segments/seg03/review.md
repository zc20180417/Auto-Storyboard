{
  "pass": true,
  "summary": "seg03将拔枪威胁和夺枪推墙拆成两组，保留枪、保险、夺枪、推倒撞墙与宋子昂咳嗽台词，无硬问题。",
  "checked_groups": ["第1组", "第2组"],
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
      "evidence": "第1组保留宋子昂从沙发夹缝掏出黑色手枪、威胁陆凡、陆凡指出保险没开的原始因果。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "黑色手枪在第1组尾由宋子昂双手持有且枪口下沉，第2组0-3秒由陆凡捏住枪管夺下并甩到沙发旁地面，道具转移清楚。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "3-6秒威胁约13字3秒、6-8.5秒陆凡回应约11字2.5秒，均未超过6.5字/秒硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "拔枪、威胁、识破保险和逼近分在13秒4段内，夺枪推倒另放第2组，避免动作过载。",
      "fix_instruction": "若不通过，应继续拆分拔枪与跨步逼近。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾陆凡逼近宋子昂且枪口下沉，第2组首直接复述两人贴近和枪口下沉，状态连续。",
      "fix_instruction": "若不通过，应在第2组组首补足枪和人物距离。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "宋子昂的“你！”和“咳咳……你敢打我？”均明确对陆凡喊或说，没有假对象。",
      "fix_instruction": "若不通过，应补充对陆凡这一对象。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "两组均为自然分镜文本，未出现模型说明、参考模板或工程占位符。",
      "fix_instruction": "若不通过，应删除污染词。"
    }
  ],
  "issues": [],
  "warnings": []
}
