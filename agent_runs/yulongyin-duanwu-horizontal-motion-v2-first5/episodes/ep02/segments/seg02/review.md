{
  "pass": true,
  "summary": "seg02五组已对照原剧本和横屏规则审核，水滴复亮、小龙现身、饮水恢复、黑水灼伤和水壶避难入口的状态链完整，无阻断问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组"],
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
      "evidence": "水壶从天天胸前到拧开壶盖再到壶口对准裂缝，壶盖归属和清水滴落路径均可见，没有道具跳变。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "原剧本的清水滴入裂缝、青蓝光复亮、小龙探头，以及天天台词“你……你像水做的一样。太神奇了。”均完整保留。"
    },
    {
      "group": "第4组",
      "type": "dialogue_pacing",
      "evidence": "“别碰那个黑水！危险！快过来！”有效约10字，安排在2秒惊呼镜头内，约5字/秒，符合情绪喊话节奏且未超硬上限。"
    },
    {
      "group": "第5组",
      "type": "horizontal_composition",
      "evidence": "天天在左侧、水壶壶口居中、小龙在右侧、黑水滩更右下方，横屏画面清楚区分安全入口和危险边界。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "camera_motion",
      "result": "pass",
      "evidence": "横向跟拍用于带水返回，固定过肩用于喊话，固定道具近景用于水滴路径；每段运镜都有服务目标。",
      "fix_instruction": "若后续改稿，应避免只写横移或推进，应说明跟随对象和揭示目标。"
    },
    {
      "group": "第3组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "第3组将水壶、清水、小龙和黑水滩同框，尾巴逐渐靠近黑水滩，为第4组误触黑水提供明确衔接。",
      "fix_instruction": "若黑水位置不清，应在组首和组尾同时补充黑水滩相对尾巴的位置。"
    },
    {
      "group": "第4组",
      "type": "screen_direction",
      "result": "pass",
      "evidence": "小龙始终在右侧裂缝边，天天始终在左侧持壶喊话，左右站位没有无过渡换边。",
      "fix_instruction": "若角色换边，应补出可见走位或使用中性镜头重新建立轴线。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首只写天天半跪、双手握水壶、小龙趴在裂缝边、黑水滩位置和干土通道，未把放置水壶或小龙挪动写入组首。",
      "fix_instruction": "若组首出现动作过程，应移入0-3秒或7-10秒镜头描述。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "该段未出现模板编号、官方占位符、参考图说明、自动分镜等污染词，保持自然短剧分镜正文。",
      "fix_instruction": "若出现工程说明，应删除并改成画面内可见信息。"
    }
  ],
  "issues": [],
  "warnings": []
}
