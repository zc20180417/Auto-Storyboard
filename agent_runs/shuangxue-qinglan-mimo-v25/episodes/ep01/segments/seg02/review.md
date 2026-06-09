{
  "pass": true,
  "summary": "seg02一组分镜通过审核，环境交代1.5秒+动作+对话节奏合理。",
  "checked_groups": ["第3组"],
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {"group": "第3组", "type": "generation_density", "evidence": "环境1.5秒+动作+对话+咳嗽反应=10秒，强节拍3个，未过载。"},
    {"group": "第3组", "type": "dialogue_pacing", "evidence": "'妈！我回来了！'7字/2.5秒=2.8字/秒，'这声音……是妈？'7字/2.5秒=2.8字/秒，节奏合理。"},
    {"group": "第3组", "type": "space_locking", "evidence": "客厅单一物理空间，组首锁定水晶吊灯、彩带气球、烫金字、电视机，空间清晰。"}
  ],
  "semantic_checks": [
    {"group": "第3组", "type": "generation_density", "result": "pass", "evidence": "10秒内3个强节拍合理分布，环境1.5秒不超标。", "fix_instruction": "无需修改"},
    {"group": "第3组", "type": "dialogue_pacing", "result": "pass", "evidence": "呼喊和紧张提问台词字秒比合理。", "fix_instruction": "无需修改"},
    {"group": "第3组", "type": "handoff_continuity", "result": "pass", "evidence": "G2组尾铁门敞开、院子垃圾散落，G3组首客厅内，空间从室外到室内有沈清走入动作衔接。", "fix_instruction": "无需修改"}
  ],
  "issues": [],
  "warnings": []
}
