{
  "pass": true,
  "summary": "seg05已核对乡长办公室热搜汇报、赵大江怒砸手机并下令抓人，反派转折完整。",
  "checked_groups": ["第1组", "第2组"],
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
      "evidence": "刘波慌张推门、汇报热搜、递手机给赵大江和手机内陆凡直播录像均按剧本保留。"
    },
    {
      "group": "第2组",
      "type": "dialogue_pacing",
      "evidence": "赵大江0-3秒骂徐虎约14字，7-12秒下令抓陆凡约18字，字秒比均低于6.5并符合愤怒对白。"
    },
    {
      "group": "第2组",
      "type": "prop_continuity",
      "evidence": "第1组赵大江接过手机，第2组组首赵大江手中持有手机，3-5秒砸到地面，手机归属和状态变化清楚。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "全组只在乡长办公室内展开，门、办公桌、文件和手机位置明确。",
      "fix_instruction": "若跨出办公室，应另起一组或标明屏幕画面。"
    },
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "手机录像作为屏幕画面出现，没有让陆凡在办公室现场开口；现场对白均由赵大江和刘波承担。",
      "fix_instruction": "若录像声音承载台词，应明确手机外放来源和办公室人物闭口反应。"
    },
    {
      "group": "第2组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "赵大江看手机怒骂、砸手机、刘波反应、下令抓人分成4段，12秒内动作和台词容量清楚。",
      "fix_instruction": "若过载，应拆出砸手机或下令动作。"
    },
    {
      "group": "第2组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文没有模型说明词、模板编号、参考图或自动分镜等污染内容。",
      "fix_instruction": "若出现污染词，应删除并改为办公室现场画面。"
    }
  ],
  "issues": [],
  "warnings": []
}
