{
  "pass": true,
  "summary": "seg01 已对照第6集完整剧本、竖屏生成规则和当前草稿完成真实审核，5个分镜组覆盖早雨预警、周大柱拒绝、夜雨塌方和赶往仓房的剧情，无阻断交付的硬问题。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组"
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "evidence": "第1组保留路边裂缝、泥水下渗、沈砚川蹲下挖土和沈小禾“哥，真软了。”、沈砚川“上层吃满水了。”、周大柱“你又在吓唬谁？”、沈砚川“让你娘先往高处挪。”的原始顺序与对象。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组14秒承载周大柱“我家仓房结实。”、沈砚川“结实扛不住泡。”、村民甲“真有那么凶？”、沈砚川“老人孩子先走，粮食搬高点。”约39个有效字，平均约2.8字/秒，并配合看裂缝和举伞反应，不存在超过6.5字/秒的硬性问题。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "第4组明确切入夜雨中的通村路口，组首列明沈砚川、林知夏、周大柱、村民乙和村民在裂缝近处的位置与朝向，未把早晨进山土路和夜晚通村路口硬塞进同一现实空间。"
    },
    {
      "group": "第5组",
      "type": "format",
      "evidence": "第5组标题含cut_id EP06-G05，总时长15秒，5个时间段为0-3、3-6、6-9、9-12、12-15秒，镜头数与时间段数一致，组结构字段完整。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "沈小禾、沈砚川、周大柱的现场对白均写明对沈砚川、沈小禾或周大柱说话，未出现假对象或对象缺失。",
      "fix_instruction": "若不通过，应补足每句真人对白的真实对象，不能用空气、泥土或裂缝等假对象承接。"
    },
    {
      "group": "第2组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "沈砚川、沈小禾、周大柱、村民甲均在组首空间锁定中有明确位置和身体朝向，后续说话和反应都在可见状态下发生。",
      "fix_instruction": "若不通过，应在组首或说话前补充人物可见位置、身体朝向或入场动作。"
    },
    {
      "group": "第3组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第2组尾部周大柱仍站在泥水里不服气，村民甲举伞发愣；第3组组首延续同一早雨土路、裂缝和各人物位置，再承接周大柱拒绝搬离，状态连续。",
      "fix_instruction": "若不通过，应补充第2组组尾或第3组组首中裂缝、人物位置、伞和泥水状态。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第4组15秒集中在夜雨路口的退后、周大柱惦记车、沈砚川拽人和村民乙哭喊四个强节拍，动作链清楚且没有叠加额外道具操作或跨空间转场。",
      "fix_instruction": "若不通过，应拆分周大柱冲向车辆和沈砚川拽回，或压缩非关键人群动作。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "第5组组首延续第4组沈砚川抓住周大柱、林知夏手持手电照向裂缝；0-6秒再呈现裂缝边缘滑落到半边土路陷下去，手电位置和路面状态有可见过渡。",
      "fix_instruction": "若不通过，应补充手电、裂缝、塌坑或沈砚川抓住周大柱的可见过渡。"
    },
    {
      "group": "第5组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "第5组闷响作为现场环境事件由土路塌陷画面承载；周大柱、林知夏、沈砚川均在画面内开口并有明确说话对象，没有心声或画外音误作现场口型。",
      "fix_instruction": "若不通过，应明确声音来源，并让画面人物嘴唇闭合不做非现场声音口型。"
    },
    {
      "group": "第1组-第5组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "草稿正文未出现模型说明词、官方模板编号、参考图、首尾帧、视频延长、字幕占位、广告语或工程说明；负面提示仅为常规画质和字幕水印约束。",
      "fix_instruction": "若不通过，应删除污染词，并改写为自然可拍的画面、动作、声音和光影描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
