{
  "pass": true,
  "summary": "seg01已按横屏新结构完成，原剧本台词、取水动机、父亲闪回和关键道具连续性均保留，未发现hard issue。",
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
    "narrative_progression": "checked",
    "asset_scope": "checked",
    "special_effects": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组保留天天触到陶笛冰凉缩手、小爪子松开、道歉台词和“你千万别死！等我回来救你！”的求救承诺。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "陶笛从第1组留在天天手里，第2组取水时仍被压在掌心边缘，水壶在堂屋桌面被天天双手拿起，道具归属清楚。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "爸爸两句台词分别安排4秒承载，均低于6.5字/秒硬上限，画面用稳定双人中景承接口型。"
    },
    {
      "group": "第3组",
      "type": "prompt_pollution",
      "evidence": "全家福只作为情绪视觉道具，未写参考图、首帧、尾帧、模型自动处理或模板编号。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "special_effects",
      "result": "pass",
      "evidence": "青蓝微光只作为裂缝内极弱边缘光和小爪子透明感出现，没有科幻激光、怪物化或卡通萌宠化。",
      "fix_instruction": "若不通过，应删去夸张魔法、科幻光束或完整小龙提前现身，改成局部微光和人物反应。"
    },
    {
      "group": "第2组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "第2组明确村路左后到右前、堂屋桌面在右侧、天天从左侧推进到桌边，16:9方向和道具位置清楚。",
      "fix_instruction": "若不通过，应补足画面左/右、前/后景和水壶位置，避免单人居中近景。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "第3组保留爸爸背行囊递陶笛、两句父亲台词、现实中天天看全家福并抱水壶离开，没有改父子关系。",
      "fix_instruction": "若不通过，应恢复爸爸男性父亲身份、原台词顺序和陶笛触发闪回的因果。"
    },
    {
      "group": "第3组",
      "type": "asset_scope",
      "result": "pass",
      "evidence": "第3组资产为天天、爸爸、堂屋/院子闪回、水壶、陶笛、行囊、全家福，未把尘土、门框、土墙列为资产。",
      "fix_instruction": "若不通过，应删去普通环境细节资产，只保留推动剧情或稳定生成的关键资产。"
    }
  ],
  "issues": [],
  "warnings": []
}
