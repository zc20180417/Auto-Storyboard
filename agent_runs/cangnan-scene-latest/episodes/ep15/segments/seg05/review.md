{
  "pass": true,
  "summary": "seg05保留酒店套房电话黑客剧情，黑客K电话音来源明确，宋子昂砸桌和转账命令可表演。",
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
      "type": "audio_mouth_sync",
      "evidence": "黑客K“宋少，没有我进不去的系统。”写为手机扬声器电话音，宋子昂嘴唇闭合不做口型，声音来源明确。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "宋子昂要求黑进黑风山项目财务系统、转钱去海外空壳公司，黑客K回应十分钟搞定，最后威胁陆凡发工资困境，剧情因果保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "0-3.5秒约15字命令，3.5-8秒约19字狠话，8-10.5秒黑客K约11字电话音，10.5-14秒宋子昂约17字自语威胁，均低于6.5字/秒。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定酒店总统套房、宋子昂、威士忌、手机，黑客K仅以电话音出现，没有未入场人物现场说话。",
      "fix_instruction": "若不通过，应将黑客K标明为电话音或加入屏幕来源。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "手机从第1组拨通后由宋子昂持有，第2组组首继续通话；酒杯在桌面，4-8秒砸桌使酒杯震动，道具状态连续。",
      "fix_instruction": "若不通过，应补充手机和酒杯的前后位置。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "宋子昂对电话里的黑客K下令，最后一句威胁写为看向窗外夜色后的低声自语，未发明假物体对象。",
      "fix_instruction": "若不通过，应区分电话对象和真实自语。"
    }
  ],
  "issues": [],
  "warnings": []
}
