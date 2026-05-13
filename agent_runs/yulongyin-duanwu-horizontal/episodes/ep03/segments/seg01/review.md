{
  "pass": true,
  "summary": "seg01已对照原剧本和横屏生成规则审核，喂食、取名、水雾与心声均保留，未发现硬问题。",
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "原剧本中反锁房门、掏出半个干瘪白馒头、轻声喂小龙、掰碎丢进水壶和小龙吞下馒头渣均在0-13秒内保留，未新增改变剧情的动作。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "“慢点吃，别噎着。我明天再去给你找吃的。”约17字承载3.5秒，约4.9字/秒；“你从云里来，又是个宝贝，以后就叫你云宝吧。”约21字承载4.5秒，约4.7字/秒，均在可表演范围。"
    },
    {
      "group": "第3组",
      "type": "audio_mouth_sync",
      "evidence": "天天OS被写为画外心声，画面明确嘴唇闭合、不做口型，且水雾、手背和脸颊动作承载心声氛围。"
    },
    {
      "group": "第3组",
      "type": "horizontal_composition",
      "evidence": "水壶位于画面中央偏左，天天在右侧，云宝喷出的水雾从左到右连接壶口、手背和脸颊，横屏轴线清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定卧室左侧房门、中央书桌、右侧床沿和水壶位置，天天从门口到桌前的走位可见。",
      "fix_instruction": "若不通过，应补充房门、书桌、水壶与天天左右位置。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "馒头碎从天天掌心到水壶内、云宝在壶中吞咽和翻滚的归属清晰，没有道具跳变。",
      "fix_instruction": "若不通过，应补充馒头碎被掰下、落水、被云宝吞下的连续动作。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组只承载喷水雾、水雾落脸和OS感受三个节拍，12秒内表演空间充足。",
      "fix_instruction": "若不通过，应拆开心声和水雾动作，或压缩非关键停顿。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "分镜正文未出现模型说明词、官方模板编号、占位符或工程化调度语。",
      "fix_instruction": "若不通过，应删除污染词并改为自然画面动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
