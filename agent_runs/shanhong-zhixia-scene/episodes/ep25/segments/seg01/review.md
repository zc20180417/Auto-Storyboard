{
  "pass": true,
  "summary": "seg01 已对照第25集完整剧本、竖屏生成规则和当前分镜逐组审核，证据对质、装载机抢堵、赵有福供出小货车夹层均保留，未发现阻断交付的硬问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组"],
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
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "沈砚川开铁箱、施工方代表质疑“凭这点纸？”，沈砚川回应“你先看清。”并指出“旧河道回填。”，林知夏接“泄口封堵人工。”和周大柱“这就是命账！”均按原剧本顺序保留。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "evidence": "15秒内承载施工方代表一句威胁、沈砚川冲下坡抓扶手、工人乙与沈砚川两句短对白、驾驶位撕扯与铲斗逼近，强动作链有4秒冲下坡和4秒撕扯支撑，没有再塞入额外道具转折。"
    },
    {
      "group": "第8组",
      "type": "dialogue_pacing",
      "evidence": "赵有福、沈砚川、林知夏、周大柱和沈砚川的短句共约30字，分布在0-9秒和12-15秒，含小货车亮灯3秒事件镜头，字秒比低于6.5且追车收束清楚。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "该组限定在旧河道坡道，坡上人物、坡下装载机和旧河道口均在同一坡道空间内，工人乙在组首位于驾驶位，行动前人物可用。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "“凭这点纸？”写为施工方代表对沈砚川沉声说道，“你先看清。”写为沈砚川对施工方代表说道，后续证据台词也有明确对象。",
      "fix_instruction": "若出现无对象对白，应补成A对B说道，不得发明假对象。"
    },
    {
      "group": "第4组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "工人乙在组首已位于坡下装载机驾驶位，施工方代表使眼色后装载机启动，人物出场和行动顺序清楚。",
      "fix_instruction": "若工人乙未在组首或行动前入场，应在组首写明其驾驶位状态。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "第5组尾沈砚川手伸向车钥匙位置，第6组组首复述其手靠近车钥匙，3.5-8秒完成拔钥匙并让装载机熄火，道具过渡可见。",
      "fix_instruction": "若钥匙突然出现在沈砚川手中，应补拔钥匙动作。"
    },
    {
      "group": "第7组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第6组尾装载机熄火、沈砚川抓扶手；第7组组首装载机仍熄火，沈砚川在驾驶室外手持车钥匙，施工方代表从装载机旁退向坡下，状态连续。",
      "fix_instruction": "若同一空间状态跳变，应在组尾或组首补具体位置和道具归属。"
    },
    {
      "group": "第8组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、官方模板说明、参考图占位符、模型自动分镜或非短剧模板语气，结尾只保留稳定画面风格与负面提示。",
      "fix_instruction": "若出现模型说明词或模板说明，应删除并改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
