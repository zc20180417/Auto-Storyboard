{
  "pass": true,
  "summary": "seg01 分镜保留原剧本被陷害、反证红泥鞋底、赵百川暗中断水果园的主要剧情和台词，时间、空间、口型与组间衔接均可执行。",
  "checked_groups": [
    "第1组",
    "第2组",
    "第3组",
    "第4组",
    "第5组",
    "第6组",
    "第7组"
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
      "evidence": "原剧本晒谷场指控中的赵百川“你偷割集体电线，证据确凿”、赵大强“人赃俱获”、林建国和张桂兰求情四句台词按顺序保留，说话对象分别指向林跃、赵百川，未改变人物关系。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "林跃 OS 被写为“林跃心声响起”，同镜头明确林跃嘴唇闭合不做口型，画面只表现睁眼、呼吸和眼神变化，未误写成现场自语。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "6-10.5秒林跃质问约18字用4.5秒承载，约4.0字/秒；10.5-14秒赵百川答复加林跃短问约18字用3.5秒承载，约5.1字/秒，均未超过6.5字/秒。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "林跃抓住李二狗脚踝、展示红泥鞋底、说“村里只有电线杆下是红泥地”和“鞋底为何全是红泥”均来自原剧本；赵大强“血口喷人”台词保留在组尾。"
    },
    {
      "group": "第7组",
      "type": "space_locking",
      "evidence": "王四关水闸与赵百川 OS 涉及晒谷场和水渠总闸两处，分镜在场景栏和镜头中明确写“蒙太奇并行”，没有伪装成同一现实空间连续移动。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "character_availability",
      "result": "pass",
      "evidence": "林跃、赵百川、赵大强、林建国、张桂兰、李二狗和众村民均在组首空间锁定中有位置与朝向；本组说话人物在开口前已经可见。",
      "fix_instruction": "若不通过，应在组首补足缺失人物的位置、身体朝向和视线关系。"
    },
    {
      "group": "第3组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组强节拍为挣断麻绳站起、赵家父子后退、林跃质问赃物、赵百川答复与林跃反问，14秒内分成4个时间段，动作链和对白没有挤压。",
      "fix_instruction": "若不通过，应把挣断麻绳动作或赃物问答拆到相邻组，避免动作和对白互相抢时长。"
    },
    {
      "group": "第5组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "林跃先对众村民说明红泥地，再对李二狗质问鞋底，赵大强最后对林跃喊话；每句真人对白均有真实对象，没有假对象。",
      "fix_instruction": "若不通过，应把每句现场对白改成明确的人对人说话，并删除假对象承载。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾部林跃仍扣着李二狗脚踝、赵大强反驳；第6组首复述该状态，并用0-2秒写林跃松开李二狗脚踝后逼近赵大强，状态过渡清楚。",
      "fix_instruction": "若不通过，应在第5组尾部或第6组开头补出松手、转身、逼近等过渡动作。"
    },
    {
      "group": "第7组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "赵百川 OS 被写成心声，镜头明确赵百川嘴唇闭合不做口型；王四关闸动作与水流停止有可见载体，声音和画面来源清楚。",
      "fix_instruction": "若不通过，应把赵百川心声改成闭口旁白，或把画面切回现场开口对白并重新计算口型时长。"
    }
  ],
  "issues": [],
  "warnings": []
}
