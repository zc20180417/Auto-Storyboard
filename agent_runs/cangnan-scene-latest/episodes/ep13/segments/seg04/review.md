{
  "pass": true,
  "summary": "seg04 将省厅线上问责和张局长办公室被带走拆成两个空间清楚的组，屏幕音源处理正确。",
  "checked_groups": ["第7组", "第8组"],
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
      "group": "第7组",
      "type": "audio_mouth_sync",
      "evidence": "徐厅长前三句均来自大屏幕扬声器，现场三人嘴唇闭合听他说话；陆凡现场对屏幕回应，口型主体明确。"
    },
    {
      "group": "第8组",
      "type": "space_locking",
      "evidence": "第8组切到县审批局办公室，组首只锁定办公室单一物理空间，徐厅长以电脑屏幕画面存在。"
    },
    {
      "group": "第8组",
      "type": "dialogue_pacing",
      "evidence": "徐厅长约23字停职台词用5.5秒，约4.2字/秒并有拍桌画面；张局长6字哀嚎用1.5秒，约4字/秒，未超硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第7组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留徐厅长称赞生态名片、追问迟迟不开工、陆凡说明张局长认为细节不达标、徐厅长要求立刻落实。",
      "fix_instruction": "若不通过，应补回缺失问责台词。"
    },
    {
      "group": "第8组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留通报批评停职检查、张局长满头大汗看直播、纪委工作人员推门架起、张局长哀嚎。",
      "fix_instruction": "若不通过，应补回被带走的动作链或台词。"
    },
    {
      "group": "第8组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "13秒内为屏幕问责、张局长瘫坐反应、纪委入场架起、哀嚎四个连续节拍，动作链时间足够且无长台词叠压。",
      "fix_instruction": "若不通过，应拆出纪委入场架起动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
