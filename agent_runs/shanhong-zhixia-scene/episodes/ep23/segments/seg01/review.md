{
  "pass": true,
  "summary": "seg01 分镜保留了第23集旧河道清障、旧河床暴露、沈母发病、小禾取药被困的主要台词、动作和因果，竖屏格式、时长、空间锁定与口型承载均可通过。",
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
      "evidence": "原剧本中周大柱“这哪是堆料，这就是封道！”、村民乙“谁让你们堆这儿的！”、赵有福“先别动！一动全塌！”、沈砚川“不动，全村塌。”和林知夏“右边先清，左边一松就会带开。”均按原顺序保留，且说话对象明确。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "0-3.5秒承载赵有福“我怕出人命！”和沈砚川“出人命的，是你。”两句情绪对白，合计约15字/3.5秒，约4.3字/秒，并包含轻微反应动作，未超过6.5字/秒硬上限。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "该组保持在料场塌边同一物理空间，组首写明沈母在背景坡上雨披下、沈小禾在坡路上，后续咳声和冲到沈砚川身旁都有可见来源，不存在人物凭空出现。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "evidence": "林知夏的“小禾！”被写为门外喊声，并通过门缝外的模糊身影承载；沈小禾现场开口“找到了！”和“哥！”均由画面内人物承担口型，声音来源清楚。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "evidence": "药包从第7组沈小禾抓到并抱紧，延续到第8组组首和0-3秒的一手抱着药包；横梁压住仓门半边的状态也从第7组组尾延续到第8组组首。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "周大柱、村民乙、赵有福、沈砚川、林知夏的台词均使用对具体人物或众人的现场对白承载，没有假对象和心声混用。",
      "fix_instruction": "若不通过，应把每句现场对白改为明确的A对B说道，画外声音需补声音来源和可见反应。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组主要强节拍为沈砚川下令、周大柱带人搬钢管、赵成武加入、赵有福阻拦并被质问，14秒内分为4个时间段，动作链和对白分配清楚。",
      "fix_instruction": "若不通过，应拆出赵有福阻拦或沈砚川质问为独立组，避免清障动作和长对白互相挤压。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组组尾林知夏指着后打木桩、众人看向旧河床边线；第4组组首继续写青石和歪斜木桩露在雨水中，人物仍围在料场塌边，状态连续。",
      "fix_instruction": "若不通过，应在上一组组尾或下一组组首补齐青石、木桩和人物位置的具体状态。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "沈砚川“我去”、沈小禾“你伤了，我去更快！”、周大柱“你别硬冲！”、沈砚川“小禾！”均保留，且脚下塌石一滑被扶住的动作未删改。",
      "fix_instruction": "若不通过，应恢复原剧本台词顺序和塌石滑倒、周大柱扶住的关键动作。"
    },
    {
      "group": "第7组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "本组限定为果园仓房内外门口，仓门作为同一建筑边界，沈小禾在门内取药，林知夏在门外呼喊，未把远处料场与仓房硬塞为同一连续空间。",
      "fix_instruction": "若不通过，应拆分室内取药与门外呼喊，或明确门内外属于同一仓房门口空间。"
    },
    {
      "group": "第8组",
      "type": "filmability",
      "result": "pass",
      "evidence": "急水灌入、没过脚面、仓门被横梁压住、后墙裂缝延长、沈砚川贴门喊话均是可见可听信息，没有把“危险”作为抽象结论单独输出。",
      "fix_instruction": "若不通过，应把抽象危险改为水位、裂缝、门板、人物动作和声音来源等可生成细节。"
    },
    {
      "group": "第1组至第8组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终分镜未出现模板编号、参考图、Seedance自动、自动正反打、@图片/@视频/@音频、字幕贴片或“空间先被交代出来”等污染表达。",
      "fix_instruction": "若不通过，应删除模型说明词、工程占位符和模板化批量描述，改为自然画面语言。"
    }
  ],
  "issues": [],
  "warnings": []
}
