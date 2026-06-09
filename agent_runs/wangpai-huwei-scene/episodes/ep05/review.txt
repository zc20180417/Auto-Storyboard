{
  "pass": true,
  "summary": "第5集分镜保留晚宴反击、后台夺U盘、监控曝光、赵明海通话和周振邦盯上顾北辰的完整证据链；时间轴、对白指向、心声闭口和关键道具连续性均已检查通过。",
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
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "许知夏对全场的长句安排在10-15秒，31个有效字约5秒，字秒比约6.2，未超过6.5硬上限；工作人员、顾北辰、宾客甲和周振邦短句均有独立或足够时间段承载。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "保留周振邦质疑视频不清楚、顾北辰举U盘和手机说明u盘/视频/后台登录记录、许知夏心声惊讶，以及赵明海在人群后退的原剧本顺序。"
    },
    {
      "group": "第6组",
      "type": "prop_continuity",
      "evidence": "第5组组尾写明手机和U盘在顾北辰手中；第6组组首继续写顾北辰右手举手机、左手持U盘，并用手机点出赵明海，关键道具归属连续。"
    },
    {
      "group": "第8组",
      "type": "dialogue_pacing",
      "evidence": "许知夏'周总错了...'台词安排在8-13秒，约20个有效字用5秒承载，字秒比约4.0，情绪质问节奏稳定。"
    },
    {
      "group": "第10组",
      "type": "audio_mouth_sync",
      "evidence": "周振邦和顾北辰均为心声，正文明确画面人物嘴唇闭合不做口型，没有把OS写成现场开口。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第2组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "顾北辰反制两名黑衣人的动作按推搡避开、压墙、闪拳摔倒、轻笑收束分段，每个时间段只有一个主动作链，没有让黑衣人或旁观者抢主动作。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第3组",
      "type": "timing_math",
      "result": "pass",
      "evidence": "第3组标题15秒，时间段为0-2、2-5、5-7.5、7.5-10、10-15，连续且使用0.5秒粒度，镜头数5个与时间段一致。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "本组主空间为晚宴大厅舞台与大屏，屏幕内容被明确写成后台监控画面，不与现实空间混淆；许知夏、周振邦、宾客和监控画面中的工作人员/周氏助理均有可用位置。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第7组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "手机外放赵明海'她会上台，按计划放'、赵明海辩解和许知夏追问流程均按原剧本保留，未新增改变剧情的动作或台词。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第9组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "第9组只承载许知夏向全场宣告移交证据与掌声递增两个节拍，10秒内有长台词和群体反应支撑，不是低密度撑时长。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第2组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "复杂打斗组的视频禁止项为黑衣人甲越过顾北辰、黑衣人乙替顾北辰反击、黑衣人乙提前站起、后台门变正门，均锚定本组人物和场景，数量4条且不禁止原剧本动作。",
      "fix_instruction": "无需修复。"
    },
    {
      "group": "第1组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现Seedance说明、自动正反打、参考模板、@图片/@视频/@音频或模板化批量描述。",
      "fix_instruction": "无需修复。"
    }
  ],
  "issues": [],
  "warnings": []
}
