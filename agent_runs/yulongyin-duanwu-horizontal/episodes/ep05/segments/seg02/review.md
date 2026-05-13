{
  "pass": true,
  "summary": "seg02两组横屏分镜保留云宝指水洼、天天吹陶笛、水弹攻击和包工头逃离，节奏与道具连续。",
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
      "evidence": "云宝在水壶里撞壶壁并指向小水洼，天天拧壶盖、掏陶笛并说云宝靠你了，随后吹响陶笛，分镜没有新增其他解法。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "小水洼从第1组右后方开始震动，到第2组右后方炸开成水弹；陶笛始终在天天手中，铁锤在包工头手里后脱手落到中央地面。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "包工头惨叫台词约11个有效字放在2.5秒内，约4.4字每秒，并被水弹连续击中动作承载，未超过硬上限。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "天天在左前方，包工头在中央偏左，水洼和泉眼在右后方，云宝指向把观众视线从左前方水壶引到右后方水洼。",
      "fix_instruction": "若不通过，应补充水壶、水洼和包工头在16:9画面中的相对位置。"
    },
    {
      "group": "第2组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "水弹从右后方射向中央偏左，包工头向左后方逃，延续上一组水洼在右、天天在左的轴线，没有无过渡换边。",
      "fix_instruction": "若不通过，应在组首或组尾补足水弹方向和逃跑路线。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "12秒分成水洼炸开、水弹击脸、包工头脱手后退、逃出岩洞四个节拍，每个节拍有明确可见动作。",
      "fix_instruction": "若不通过，应拆分水弹命中和逃跑，避免同一镜头塞入过多动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
