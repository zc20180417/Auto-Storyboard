{
  "pass": true,
  "summary": "seg01 两组已对照原剧本、横屏结构、台词归属、时间轴和闪回边界审查，未发现阻断交付的硬问题。",
  "checked_groups": [
    "第1组",
    "第2组"
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
    "horizontal_composition": "checked",
    "screen_direction": "checked",
    "blocking_continuity": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本中冰凉触感、半透明小爪松开跌回黑暗、天天道歉、青蓝光消失和喊出“你千万别死！等我回来救你！”均按顺序保留。"
    },
    {
      "group": "第2组",
      "type": "horizontal_composition",
      "evidence": "堂屋段明确门口在画面左侧、旧木桌和水壶在画面中央偏右、全家福在右后方；闪回中爸爸在画面右侧、天天在左侧，陶笛处于两人之间。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "爸爸“村里没活路了，爸爸得出去打工赚钱。”约16个有效字对应3.5秒，约4.6字/秒；“想爸爸的时候就吹，爸爸听得到。”约13个有效字对应3秒，约4.3字/秒，节奏合规。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "天天稳定在画面左前方，裂缝和小龙方向稳定在画面中央到右下方，视线轴线由左向右下延续到离开河床。",
      "fix_instruction": "若不通过，应在组首或组尾补充天天、裂缝和陶笛的左右关系与离场方向。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "水壶从桌面中央偏右被天天抓起并抱在胸前，陶笛只出现在明确标注的闪回传递中，道具归属没有混淆。",
      "fix_instruction": "若不通过，应补清水壶从桌面到天天怀里的可见拿起动作，并把闪回道具与现实道具分开。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "两句爸爸台词都发生在可见闪回画面里，由画面右侧爸爸对画面左侧天天说出，没有心声或画外音误写为现场口型。",
      "fix_instruction": "若不通过，应标明声音来源是闪回中的爸爸，或补充嘴唇闭合规则。"
    }
  ],
  "issues": [],
  "warnings": []
}
