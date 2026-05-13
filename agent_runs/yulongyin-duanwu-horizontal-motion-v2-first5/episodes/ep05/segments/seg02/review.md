{
  "pass": true,
  "summary": "seg02横屏分镜完整呈现云宝指向水洼、天天取陶笛、笛声引发水弹和包工头逃离，水壶、陶笛、水洼、水弹状态链清楚。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组"
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
    "camera_motion": "checked",
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "prop_continuity",
      "evidence": "水壶在天天胸前，云宝在壶内撞击并指向中央水洼，天天随后拧开壶盖并抽出陶笛，道具来源和操作归属清楚。"
    },
    {
      "group": "第2组",
      "type": "camera_motion",
      "evidence": "第2组运镜按水壶青光、陶笛声、水洼爆开、水弹射向右侧包工头推进，每段都有起点、终点或服务目的。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "天天“云宝，靠你了！”为1.5秒短句承载，后续用3秒吹笛和3.5秒水洼爆开，不把台词、水弹形成和攻击全部塞进同一镜头。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "包工头惨叫“哎哟！什么东西打我的脸！”、捂脸红肿、连滚带爬逃出岩洞都被保留，胡永贵仍留在现场。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "天天和水壶在左前景，包工头和胡永贵在右侧，小水洼在中央偏下，画面左右和前后层次支撑云宝指向关系。",
      "fix_instruction": "若修改构图，需保持水壶、陶笛、小水洼和右侧威胁在同一横屏空间内。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "水壶青光、陶笛声、小水洼震纹、水弹凝成并射出构成连续来源、路径、结果，没有突然出现的奇幻效果。",
      "fix_instruction": "不得删掉水洼震纹或水弹从中央射向右侧的路径。"
    },
    {
      "group": "第3组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "水弹攻击方向从中央或左侧来源射向右侧包工头，包工头逃离沿右侧洞口方向，未出现无过渡换边。",
      "fix_instruction": "如调整逃离镜头，需保留包工头从右中景到右侧洞口的方向。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第3组10秒只承担水弹余击、惨叫、失衡和逃出岩洞，不叠加新台词或新道具使用，动作密度可表演。",
      "fix_instruction": "不要在该组再加入胡永贵黑液动作，黑液应放在下一段。"
    }
  ],
  "issues": [],
  "warnings": []
}
