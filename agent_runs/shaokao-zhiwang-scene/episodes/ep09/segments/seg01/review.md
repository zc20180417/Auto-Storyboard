{
  "pass": true,
  "summary": "seg01 分镜覆盖后排货摊断供、街口摊位硬撑和马会递纸条三段剧情，台词顺序、人物关系、空间切换和 cut_id 合同均通过审核。",
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
    "audio_mouth_sync": "checked",
    "generation_density": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "7-12秒承载许安问刘叔和肉贩乙回应，约23个有效汉字用5秒完成，约4.6字/秒；12-15秒承载林小满追问和肉贩乙低声回应，约16字用3秒完成，约5.3字/秒，未超过6.5字/秒硬上限。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "保留唐婶问备货少、林小满解释新鲜货少、老客提到对面搞事、许安让客人别管、林小满压声抱怨和许安稳客的台词顺序，没有新增改变剧情的动作。"
    },
    {
      "group": "第5组",
      "type": "prop_continuity",
      "evidence": "纸条在组首明确位于马会手中，2.5-5秒由马会塞进许安手心，8-10秒许安捏着纸条发问，10-15秒许安低头看纸条并握紧，道具归属转移可见。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "本组只发生在夜市后排货摊，组首列明许安、林小满、肉贩甲、肉贩乙的位置、朝向和案板肉料状态，人物在发言前均已可见。",
      "fix_instruction": "若不通过，应补齐每个说话人物的画面位置、身体朝向和可见状态。"
    },
    {
      "group": "第2组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第1组组尾为许安和林小满看向肉贩乙，第2组组首仍在同一货摊通道并保持对肉贩乙的视线，第2组尾部明确两人拎少量肉料离开，为下一场街口摊位转场提供过渡。",
      "fix_instruction": "若不通过，应在上一组组尾或本组组首补充人物位置和离开动作。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "唐婶对林小满、林小满对唐婶、老客对许安、许安对老客、林小满对许安、许安对林小满均有明确说话对象，没有假对象或无对象台词。",
      "fix_instruction": "若不通过，应把每句现场对白改为“A对B说道/问道”。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组主要节拍为许安分烤少量肉串、林小满分送餐盘、唐婶评价和许安回应，总时长12秒，动作链和两句短对白未过载。",
      "fix_instruction": "若不通过，应拆分分烤动作和对白回应，或减少无关动作。"
    },
    {
      "group": "第5组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "所有台词均为画面内人物现场低声开口，马会、许安的说话对象明确，没有心声、电话音或门外音混用。",
      "fix_instruction": "若不通过，应标明声音来源，心声或画外音需写嘴唇闭合不做口型。"
    },
    {
      "group": "第5组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "分镜正文未出现模板编号、官方模板说明、@图片/@视频/@音频、自动正反打、Seedance 可等模型或模板污染词。",
      "fix_instruction": "若不通过，应删除工程说明词并改成自然画面描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
