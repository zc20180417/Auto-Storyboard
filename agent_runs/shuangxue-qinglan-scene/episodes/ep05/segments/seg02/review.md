{
  "pass": true,
  "summary": "seg02按厨房单一空间完成发现残羹、夺筷、端碗离开，关键道具连续清楚。",
  "checked_groups": ["第3组", "第4组", "第5组"],
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
    {"group": "第3组", "type": "script_fidelity", "evidence": "第3组保留厨房油烟、塑料小板凳、周桂兰端缺口碗吃鱼骨菜汤、夹起发黑鱼肉未入口。"},
    {"group": "第4组", "type": "action_atomicity", "evidence": "沈清喊停、冲到面前夺筷、周桂兰解释分别拆成0-3、3-6、6-9秒，夺筷主动作独立。"},
    {"group": "第5组", "type": "prop_continuity", "evidence": "第4组尾筷子在沈清手里、碗在周桂兰手边；第5组先放筷子到灶台，再端起缺口碗离开，转移可见。"}
  ],
  "semantic_checks": [
    {"group": "第3组", "type": "space_locking", "result": "pass", "evidence": "组首只写厨房第一帧状态，沈清在门内、周桂兰坐小板凳，未把进入过程写进组首。", "fix_instruction": "若组首使用走进、冲过去等过程动词，应移到镜头描述。"},
    {"group": "第4组", "type": "dialogue_pacing", "result": "pass", "evidence": "‘妈！别吃了！’约5字占3秒，含喊停和对方停手动作；周桂兰台词约11字占3秒，约3.7字/秒并有慌张反应，未构成硬问题。", "fix_instruction": "若台词超过6.5字/秒，应延长或拆段。"},
    {"group": "第5组", "type": "script_fidelity", "result": "pass", "evidence": "沈清质问‘外面吃鲍鱼海参……口水菜？’并端起残羹冷炙的破碗往外走，未新增剧情动作。", "fix_instruction": "若改成倒掉剩菜或拉走周桂兰，应恢复原动作。"},
    {"group": "第5组", "type": "video_negative_constraints", "result": "pass", "evidence": "第5组视频禁止项锚定缺口碗、沈清、筷子和残羹，数量3条且不与正文矛盾。", "fix_instruction": "若禁止项泛泛，应替换为本组具体道具和动作风险。"}
  ],
  "issues": [],
  "warnings": []
}
