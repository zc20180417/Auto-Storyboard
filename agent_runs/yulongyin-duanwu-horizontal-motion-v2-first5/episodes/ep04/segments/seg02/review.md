{
  "pass": true,
  "summary": "已对照第4集4-2原剧本、横屏生成规则和当前分段分镜逐项审查，云宝醒来、水雾结冰、胡永贵摔倒、天天接水离开的动作链完整，无硬问题。",
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
      "evidence": "水壶在天天怀里，云宝在壶内睁眼并喷出水雾，组尾水雾从壶口溢出，奇幻效果来源清楚。"
    },
    {
      "group": "第2组",
      "type": "camera_motion",
      "evidence": "第2组用低位横向平移呈现水雾到薄冰的路径，用固定中景承载胡永贵台词和脚前薄冰，摔倒时保持水管与薄冰在画面中线。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "胡永贵台词“小兔崽子，敢跟我抢——哎哟！”安排在3-6秒，情绪对白约5字/秒，未超硬上限。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "保留天天接住水管、将清水注满水壶、兴奋说“走！我们回家！”的原剧本顺序，没有新增改变剧情的动作。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首写天天低伏左前景、胡永贵右后景、水管中景偏右、水壶贴近天天胸口，均为第一帧静态状态。",
      "fix_instruction": "若后续修改，应继续避免在组首写喷出、转圈、扑过去等过程动作。"
    },
    {
      "group": "第2组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "水雾从左前景水壶到右侧脚边薄冰，胡永贵右侧、天天左侧的横向因果关系清楚。",
      "fix_instruction": "如需调整镜头，应保留水雾来源、路径和胡永贵脚前结果的左右关系。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组组尾水管落在中景偏左，第3组组首水管仍在中央偏左地面，天天从左前景接水管，状态衔接一致。",
      "fix_instruction": "不得让水管在第3组开头突然变成天天已经握住，必须保留可见接住动作。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "分镜没有出现模板编号、模型控制台占位符、参考图、视频延长或自动分镜说明。",
      "fix_instruction": "后续修改时继续保持自然短剧分镜正文。"
    }
  ],
  "issues": [],
  "warnings": []
}
