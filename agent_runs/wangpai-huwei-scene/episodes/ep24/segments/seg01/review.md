{
  "pass": true,
  "summary": "seg01按保险室、会客室、楼梯间拆组，保留夺取录音笔、证据公开威胁和撤离夹击，审核未发现硬问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组", "第10组"],
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
    "action_atomicity": "checked",
    "video_negative_constraints": "checked",
    "prompt_pollution": "checked"
  },
  "spot_checks": [
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "顾北辰OS写明嘴唇闭合，许知夏警告写为耳机声音且顾北辰嘴唇闭合；秦越质问为现场对顾北辰说道。"
    },
    {
      "group": "第5组",
      "type": "dialogue_pacing",
      "evidence": "许知夏对沈曼的长句约29个有效字安排在6秒内，约4.8字/秒；沈曼短句3秒承载，节奏合理。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "evidence": "顾北辰耳机声确认笔到手，会客室内秦越按下遥控器后警报和电梯停运提示出现，遥控器状态清楚。"
    },
    {
      "group": "第10组",
      "type": "action_atomicity",
      "evidence": "上下夹击、下方推挡、上方挡冲、护着下撤分四段呈现，许知夏明确不参与打斗。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留秦越质问沈曼背叛、顾北辰反击台词和暗柜内录音笔出现。",
      "fix_instruction": "若不通过，应补回两句对峙台词和录音笔位置。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "心声、金属杆挑笔、自毁装置弹出、许知夏警告、秦越质问分段承载，总时长14秒但有足够道具操作和信息容量。",
      "fix_instruction": "若不通过，应拆出强磁装置弹出和耳机警告。"
    },
    {
      "group": "第3组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "看反光、砸喷淋头、水雾落下、红外线失灵和台词分为清楚动作链，没有同段塞入拔笔动作。",
      "fix_instruction": "若不通过，应把砸喷淋和夺笔分到不同组。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "录音笔从暗柜边缘被拨到手边后由顾北辰拔下，自毁装置从柜底被踢入积水再短路，道具转移可见。",
      "fix_instruction": "若不通过，应补录音笔离柜和自毁装置入水过程。"
    },
    {
      "group": "第6组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "秦越在组首位于会客室门外阴影中并在0-3秒推门入场，随后才开口提许知夏父亲旧案。",
      "fix_instruction": "若不通过，应补秦越入场前位置或推门动作。"
    },
    {
      "group": "第7组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "秦越关于许氏旧案漩涡的台词和许知夏反击台词均明确对对方说道，沈曼只作为背景反应不抢对白。",
      "fix_instruction": "若不通过，应补清对话对象并避免沈曼抢对峙。"
    },
    {
      "group": "第9组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "从会客室撤离切到楼梯间是新物理空间；第9组尾部明确顾北辰挡在许知夏身前、安全门打开、录音笔在手，能接第10组。",
      "fix_instruction": "若不通过，应补顾北辰和许知夏在楼梯间的站位。"
    },
    {
      "group": "第10组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "楼梯间动作组提供5条具体禁止项，锚定许知夏、顾北辰、录音笔、秦越手下和上下夹击方向。",
      "fix_instruction": "若不通过，应替换泛泛禁止项并锚定本组人物道具。"
    },
    {
      "group": "第1组-第10组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文无模型说明词、模板编号、参考图占位符、JSON调试文字或模板化批量描述。",
      "fix_instruction": "若不通过，应删除污染词并改成自然分镜。"
    }
  ],
  "issues": [],
  "warnings": []
}
