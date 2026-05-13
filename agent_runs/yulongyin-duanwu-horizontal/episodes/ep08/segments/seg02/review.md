{
  "pass": true,
  "summary": "seg02 保留塑料袋抓云宝、天天扑咬、被甩到鼓架、云宝透明和胡永贵下令砸船的关键动作，审核未发现硬问题。",
  "checked_groups": ["第4组", "第5组", "第6组"],
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
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "手下拿出塑料袋伸手抓云宝、天天喊“别碰它！”并扑上去咬住手下胳膊，均按原剧本顺序呈现。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "evidence": "塑料袋从第4组手下手里滑到右下角，第5组组首仍落在右前景；天天被甩到左后方鼓架，血滴落到鼓面，位置连续。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "胡永贵台词“敬酒不吃吃罚酒！给我连人带船一起砸！”约19字用3.5秒承载，约5.4字/秒，符合争吵台词节奏。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第4组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "天天从画面左侧扑向右侧手下，手下从右侧伸手抓中央云宝，冲突轴线清楚，没有无过渡换边。",
      "fix_instruction": "若不通过，应统一天天左侧、手下右侧、云宝中央的轴线。"
    },
    {
      "group": "第5组",
      "type": "blocking_continuity",
      "result": "pass",
      "evidence": "手下从中央把天天甩向左后方鼓架，后续血滴落在左下鼓面，动作路线和落点一致。",
      "fix_instruction": "若不通过，应补出天天从中央到鼓架的甩动路线。"
    },
    {
      "group": "第6组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第6组承载云宝透明、胡永贵下令、手下举锤三个强节拍，12秒内可表演且未塞入额外剧情。",
      "fix_instruction": "若不通过，应拆出手下举锤或压缩非关键反应。"
    }
  ],
  "issues": [],
  "warnings": []
}
