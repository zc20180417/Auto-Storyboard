{
  "pass": true,
  "summary": "ep13 单段分镜保留追逃、耳机通话、档案库对峙、文件散落突围和旧桌卡门等关键剧情，未发现阻断交付的硬问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组", "第8组", "第9组"],
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
      "type": "action_atomicity",
      "evidence": "追堵动作拆为顾北辰冲出、周振邦对讲机喊话、击中第一名保安、夺棍顶腹甩墙四段，没有把两名保安的攻击压入同一时间段。"
    },
    {
      "group": "第2组",
      "type": "audio_mouth_sync",
      "evidence": "许知夏只以耳机声出现，顾北辰现场开口均写明对耳机里的许知夏说道；许知夏较长 VO 时顾北辰嘴唇闭合听着。"
    },
    {
      "group": "第4组",
      "type": "space_locking",
      "evidence": "组首明确安全通道门关闭且顾北辰位于门后只以声音出现，随后许知夏让开、顾北辰推门入场，人物可用性和门状态连续。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "秦越 17 字台词给 4 秒，约 4.25 字/秒；顾北辰 11 字给 2 秒，约 5.5 字/秒；许知夏 18 字给 3 秒，约 6 字/秒，均未超过 6.5 字/秒硬上限。"
    },
    {
      "group": "第8组",
      "type": "prop_continuity",
      "evidence": "档案文件由许知夏扬起后变成散落纸页，手机仍由许知夏持有，组尾继续锚定手机和散落纸页位置。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第3组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "许知夏退到安全通道门旁、秦越抬手让手下堵路、双方关于电子版和九点十五分自动发出的台词均按原剧本保留。",
      "fix_instruction": "若不通过，应恢复许知夏手机扫描件和秦越索要东西的原始因果。"
    },
    {
      "group": "第5组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "顾北辰对秦越说道三年前那笔账，秦越对顾北辰回应许振南硬盘，现场对白对象明确。",
      "fix_instruction": "若不通过，应为每句现场对白补足真实对话对象。"
    },
    {
      "group": "第6组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "许知夏 OS 写为嘴唇闭合、不做口型的心声，未被误写成现场开口。",
      "fix_instruction": "若不通过，应改为闭口心声或明确现场对白。"
    },
    {
      "group": "第7组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组承载秦越威胁、顾北辰追问三年前清场、顾北辰迈步、许知夏拉袖提醒四个节拍，分布在 15 秒内且动作不互相抢占。",
      "fix_instruction": "若不通过，应拆出顾北辰迈步或许知夏拉袖提醒。"
    },
    {
      "group": "第8组",
      "type": "action_atomicity",
      "result": "pass",
      "evidence": "纸页扬起、右拳击中一人、横扫另一人、翻过档案柜拉住许知夏、退向安全通道分成独立时间段，主动作清楚。",
      "fix_instruction": "若不通过，应继续拆分格斗和撤退动作。"
    },
    {
      "group": "第9组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "视频禁止项锚定旧桌子、许知夏、手机倒计时和秦越进入安全通道等本组具体风险，共 4 项，没有泛泛占位。",
      "fix_instruction": "若不通过，应替换为本组具体人物、道具和门缝状态风险。"
    }
  ],
  "issues": [],
  "warnings": []
}
