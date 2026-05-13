{
  "pass": true,
  "summary": "seg01保留陆凡录像报警、血狼撤逃、警车到场和血狼被按倒的完整因果，格式和时长可交付。",
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
      "evidence": "原剧本中五名打手挥棍、陆凡后退到挖掘机后方、举手机录像并报警的动作和台词均被保留，未新增反击或硬拼动作。"
    },
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "陆凡警告台词约34字安排在6-13秒共7秒，约4.9字/秒，且包含举手机后的稳定对峙，口型节奏合理。"
    },
    {
      "group": "第2组",
      "type": "space_locking",
      "evidence": "组首明确陆凡、血狼、五名打手和远处警车的位置与朝向，警车从背景山路进入同一半山腰工地空间，没有跨空间跳切。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "陆凡的现场对白写成对打手们沉声说道，真实对话对象明确，没有假对象或心声混用。",
      "fix_instruction": "若不通过，应补清陆凡对白的真实对象或改成画外音来源。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第2组15秒承载警笛、血狼命令、撤逃、警车到场、民警喇叭和按倒血狼，均为同一抓捕动作链，时间段分配清楚。",
      "fix_instruction": "若过载，应拆出警车到场或按倒血狼的动作。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组尾部陆凡举手机、打手停在挖掘机前；第2组首继续同一站位并补入远处警车灯光，状态连续。",
      "fix_instruction": "若不通过，应在第2组组首复述陆凡手机和打手位置。"
    }
  ],
  "issues": [],
  "warnings": []
}
