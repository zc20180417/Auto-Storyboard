{
  "pass": true,
  "summary": "seg01完整保留保险柜、钥匙、证据链、录音入侵和黑车尾钩，时间轴、口型、空间拆分和关键道具连续性均可交付。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组", "第10组", "第11组"],
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
      "group": "第1组",
      "type": "dialogue_pacing",
      "evidence": "顾北辰对白“许总既然看见了，就打开吧。他们今晚来，就是为里面的东西。”有效字数24字，4秒承载，约6.0字/秒，未超过6.5硬上限；许知夏短句分别在2.5秒内完成，没有拉成长停顿。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "保险柜钥匙先在桌面，第4组0-3秒由许知夏拿起并插入锁孔，5.5-8秒保险柜打开，8-11秒旧档案和加密硬盘被取出放到桌面，道具转移可见。"
    },
    {
      "group": "第9组",
      "type": "audio_mouth_sync",
      "evidence": "许振南录音由电脑播放界面承载，许知夏被明确写为嘴唇闭合不做口型，录音没有被误写成现场真人开口。"
    },
    {
      "group": "第11组",
      "type": "space_locking",
      "evidence": "第11组单独切到许氏集团大楼外和黑车，没有把室内办公室人物与楼外车辆塞入同一现实空间；8秒作为尾钩短组成立。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "保留许知夏对撬痕的讽刺、顾北辰要求打开保险柜、许知夏没有钥匙三项原剧本信息。",
      "fix_instruction": "若不通过，应补回原台词和保险柜未打开的起点状态。"
    },
    {
      "group": "第4组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "拿钥匙、插入锁孔、打开柜门、取出档案硬盘、露出证据链封面分成连续时间段，没有把开柜和取物压进一个短镜头。",
      "fix_instruction": "若不通过，应拆分保险柜开启动作和档案硬盘取出动作。"
    },
    {
      "group": "第6组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "照片内容保持为年轻顾北辰站在许振南身后，并保留许知夏“你跟我爸，关系很好。”和顾北辰“他早些年帮过我很多。”",
      "fix_instruction": "若不通过，应恢复照片人物关系和两句原台词。"
    },
    {
      "group": "第8组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载情绪静止、许知夏要求真相、顾北辰警告危险、许知夏反击四个节拍，均为同一办公室同一对峙目标，15秒内清楚可表演。",
      "fix_instruction": "若不通过，应把许知夏反击拆到下一组或压缩前置静止节拍。"
    },
    {
      "group": "第9组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "录音、屏幕红字、拔网线三个信息源都有可见载体，许父声音与许知夏口型分离明确。",
      "fix_instruction": "若不通过，应补电脑播放界面、人物闭口反应或网线断开动作。"
    },
    {
      "group": "第10组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第9组尾部网线被拔下、电脑仍显示入侵提示，第10组组首复述网线头脱离电脑接口、硬盘仍连接电脑，状态连续。",
      "fix_instruction": "若不通过，应在第10组组首补断开的网线和屏幕红字。"
    },
    {
      "group": "第11组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "黑车尾钩组的视频禁止项锚定黑车、秦越、许知夏和许氏大楼，数量4个，没有泛泛模板词，也没有禁止原剧本必须发生的停车与望楼动作。",
      "fix_instruction": "若不通过，应替换为本组特有且不矛盾的黑车尾钩风险。"
    },
    {
      "group": "第1组-第11组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现Seedance说明、参考图、模板编号、自动分镜、工程字段或泛化批量描述。",
      "fix_instruction": "若不通过，应删除模型说明词和模板污染文本。"
    }
  ],
  "issues": [],
  "warnings": []
}
