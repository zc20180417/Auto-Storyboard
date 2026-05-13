{
  "pass": true,
  "summary": "seg03五组已对照原剧本和横屏规则审核，小龙入壶、卧室安置、天天安抚与自责、壶壁画龙舟的情绪和道具状态完整，无阻断问题。",
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
      "type": "handoff_continuity",
      "evidence": "小龙从裂缝边进入水壶、天天拧紧盖子并通过救援转场蒙太奇带回卧室，跨空间转换有明确蒙太奇标识。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "evidence": "原剧本的水壶放上书桌、天天贴近观察、台词“别怕，我带你回家了，这里没有黑水。”以及灰白尾巴刺眼均保留。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "“都怪我没早点发现那些黑水有毒。”有效约15字，安排在3秒镜头内，约5字/秒，符合心疼自责语速且不超硬上限。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "evidence": "龙舟轮廓由第4组的船形线条延续而来，第5组明确船头高昂、船尾下沉，小龙尾巴点向图形，提示意图连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首锁定裂缝、水壶、天天、小龙和黑水滩的静态位置；小龙入壶和天天拧盖均放在时间段中。",
      "fix_instruction": "若组首出现爬行、抱起或拧盖过程，应挪入镜头描述。"
    },
    {
      "group": "第2组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "天天对水壶里的小龙小声说话，说话对象明确，小龙处于壶底可见位置，没有把独白误作现场对空气说话。",
      "fix_instruction": "若小龙不可见，应补充壶底位置或改为天天画外低声自语并说明口型。"
    },
    {
      "group": "第3组",
      "type": "camera_motion",
      "result": "pass",
      "evidence": "固定近景承载自责台词，推近小龙眼睛，摇向尾巴和壶壁接触点，固定特写呈现划线结果，运镜围绕回应和图形生成递进。",
      "fix_instruction": "若运镜过多或失焦，应保留固定台词镜头并删去无目的移动。"
    },
    {
      "group": "第4组",
      "type": "horizontal_composition",
      "result": "pass",
      "evidence": "水壶居中，天天在左侧，小龙在壶底右侧，尾巴与壶壁线条同框，横屏左右关系服务读图和提问。",
      "fix_instruction": "若只拍单人特写，应补回水壶、图形和小龙的位置关系。"
    },
    {
      "group": "第5组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "龙舟轮廓和天天追问均以自然画面与台词表达，没有出现模板编号、官方占位符或参考图说明。",
      "fix_instruction": "若出现模板化或工程词，应删除并改为画面内道具和动作。"
    }
  ],
  "issues": [],
  "warnings": []
}
