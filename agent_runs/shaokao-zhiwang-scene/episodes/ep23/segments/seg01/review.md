{
  "pass": true,
  "summary": "已对照第23集原剧本、竖屏生成规则和当前seg01分镜逐组审核，前厅揭穿韩彪与后厨阿顺倒戈的台词、空间、人物可用性、时长和提示词洁净度均可交付。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组",
    "第8组",
    "第9组"
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
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "第2组9-15秒承载马会台词“我没忘。可我也没忘，这店最早能立住，靠的是谁守火。”，约26个有效字分配6秒，约4.3字/秒，符合情绪压稳的口型容量；本组总时长15秒且4个时间段连续。"
    },
    {
      "group": "第4组",
      "type": "script_fidelity",
      "evidence": "第4组保留韩彪“放屁！一个看火的……”、马会关于分红赖账、流程偷学、阿顺位置本属于许安的指控，并保留阿顺“我……”、老伙计甲和投资人乙的反应，没有改变人物关系或因果。"
    },
    {
      "group": "第5组",
      "type": "timing_math",
      "evidence": "第5组为前厅质问后的短动作余波，6秒内只表现韩彪哑口无言和众人目光变化；上一组已满15秒，下一组切入后厨新物理空间，因此该短组不能自然并入相邻组。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "evidence": "第6组单一物理空间为韩彪店后厨，组首明确炉台、案板、便宜货、阿顺和韩彪的位置及朝向；从前厅到后厨另起一组，没有把两处空间塞入同一片段。"
    },
    {
      "group": "第8组",
      "type": "character_availability",
      "evidence": "第8组组首明确马会在门口内侧、老伙计甲在门外右侧阴影里可见，二人开口前都有可用位置；阿顺手中签子延续第6-7组状态，归属连续。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "韩彪对马会、马会对韩彪、老伙计甲对桌边众人、投资人乙对韩彪的说话对象都明确，没有把对白写成对空气或对道具说。",
      "fix_instruction": "若后续修改新增对白，继续用“A对B说道/问道/喊道”的对象格式。"
    },
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "许安是稳味、稳火、稳客核心的信息按原顺序揭示，老伙计乙“许安？”和投资人甲“他说的是真的？”均保留，未新增额外证据或动作。",
      "fix_instruction": "若发现漏台词，应只补回原台词与对应反应，不添加新剧情证据。"
    },
    {
      "group": "第5组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第5组仅包含韩彪语塞和众人目光变化两个轻节拍，作为前厅戏的短动作余波成立，没有拖慢台词或硬塞动作凑时长。",
      "fix_instruction": "若要扩展本组，不能添加原剧本没有的新对抗动作；应保持为前厅余波。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "前厅会散后另起后厨空间，组首给出阿顺炉前持签子、韩彪门口内侧铁青脸色，和原剧本“会散后，后厨空了大半”一致。",
      "fix_instruction": "若调整前后顺序，保持前厅与后厨分组，不要跨空间合并。"
    },
    {
      "group": "第7组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "马会在组首被锁定于门外阴影里，11.5秒镜头中站在后厨门口开口，对阿顺说“你总算说句像样的了”，出声前可用性明确。",
      "fix_instruction": "若删去组首门口状态，需要在开口前增加明确入场或揭示动作。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "阿顺从第6组起一直手中持有签子，第8组继续攥紧签子承载情绪，没有出现签子归属跳变；便宜货一直位于案板上。",
      "fix_instruction": "若新增道具操作，必须写清拿起、放下、递出或归属变化。"
    },
    {
      "group": "第9组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终分镜没有出现模板编号、参考图、自动分镜、模型说明词、字幕贴片或横屏字段；画面风格和负面词保持竖屏短剧自然提示词口径。",
      "fix_instruction": "若后续补写说明文字，不能进入final.txt正文。"
    }
  ],
  "issues": [],
  "warnings": []
}
