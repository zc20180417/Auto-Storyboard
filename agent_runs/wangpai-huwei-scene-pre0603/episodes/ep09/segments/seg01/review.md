{
  "pass": true,
  "summary": "ep09按安全屋揭旧案、仓库闪回、许父视频、盛叔反转完成分组，台词、道具、闪回边界和口型承载符合竖屏分镜规则。",
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
      "group": "第3组",
      "type": "script_fidelity",
      "evidence": "保留许知夏要点开隐藏文件夹、顾北辰按住鼠标、顾北辰说“别看”和“更关系一群已经死了的人”的因果顺序，未提前打开文件。"
    },
    {
      "group": "第5组",
      "type": "action_atomicity",
      "evidence": "背负移动、搭档挣扎下来、顾北辰追问、抓衣领推开、顾北辰摔倒被拆成5个时间段，没有把推人和摔倒压在同一瞬间。"
    },
    {
      "group": "第8组",
      "type": "dialogue_pacing",
      "evidence": "许知夏20字疑问给4秒，约5.0字/秒；顾北辰16字回答给4秒，约4.0字/秒，均低于6.5字/秒硬上限。"
    },
    {
      "group": "第9组",
      "type": "audio_mouth_sync",
      "evidence": "许父关键内容明确来自电脑视频，许知夏OS明确写闭口不做口型，现场人物没有代替视频或心声开口。"
    },
    {
      "group": "第11组",
      "type": "dialogue_pacing",
      "evidence": "顾北辰35字解释给7秒，约5.0字/秒；许知夏15字反问给4秒，约3.8字/秒，符合普通对白承载。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "组首列明铁门、保险栓、监控屏、电脑药箱、布防图和两人站位，第一帧就是安全屋落锁后的可生成状态。",
      "fix_instruction": "若不通过，应补齐门锁、屏幕、桌面道具和两人的画面位置。"
    },
    {
      "group": "第4组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "爆炸、搭档喊走、顾北辰喊一起走、火势扩大分为4个时间段，闪回空间明确，不与安全屋现实场景混写。",
      "fix_instruction": "若不通过，应拆出爆炸冲击或搭档台词，避免一段承载多个强动作。"
    },
    {
      "group": "第6组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第5组尾顾北辰摔倒、搭档在钢架前；第6组首复述顾北辰前景地面半撑起、搭档在坍塌钢架前，状态连续。",
      "fix_instruction": "若不通过，应同步第5组尾和第6组首的摔倒、站位、火浪状态。"
    },
    {
      "group": "第7组",
      "type": "prop_continuity",
      "result": "pass",
      "evidence": "鼠标从第3组被按住延续到第7组顾北辰手下，再以手慢慢松开完成状态转移，硬盘仍连接电脑侧边。",
      "fix_instruction": "若不通过，应补鼠标和硬盘的起止位置，避免道具突然消失。"
    },
    {
      "group": "第9组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "许父台词全部标为电脑视频中的声音，许知夏OS标明闭口不做口型，符合视频声源和心声承载要求。",
      "fix_instruction": "若不通过，应将许父台词改回屏幕视频声源，并为OS补闭口说明。"
    },
    {
      "group": "第10组",
      "type": "video_negative_constraints",
      "result": "pass",
      "evidence": "普通疑问对话组未强行添加视频禁止项；复杂动作和关键道具组的视频禁止项均为2-4个具体剧情错误并锚定人物或道具。",
      "fix_instruction": "若不通过，应删除普通对话组泛泛禁止项，或把复杂组禁止项改为本组具体人物道具错误。"
    },
    {
      "group": "第11组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现模板编号、模型说明词、参考图、首尾帧、固定画面风格或手写--neg等污染项。",
      "fix_instruction": "若不通过，应删除非分镜正文和模型模板术语。"
    }
  ],
  "issues": [],
  "warnings": []
}
