{
  "pass": true,
  "summary": "seg01 已按竖屏 scene 规则审完，7组均保留原剧本关键动作、台词和三处物理空间切分，未发现阻断问题。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组", "第7组"],
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
      "type": "generation_density",
      "evidence": "第2组在15秒内承载断绳绕石销、铁钎卡缝、石销松动、闸板顶开、沈砚川滑入检修槽；均为同一洞内连续动作链，5个时间段连续到15秒，未跨物理空间。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "第3组3-8秒连续承载“下面也出水了！”“旧河道开了！”“主闸开了！”约19个有效字，5秒内约3.8字/秒；8-13秒承载“我哥呢！”“去哪找他？”约10个有效字，5秒内约2字/秒并包含哭泣与追问反应，不存在过快。"
    },
    {
      "group": "第5组",
      "type": "script_fidelity",
      "evidence": "第5组保留塌石动、沈砚川满身泥血爬出、手攥铁钎，以及沈小禾“哥！”、周大柱“你真出来了！”、林知夏“伤哪儿了？”、沈砚川“皮外伤。”等原台词。"
    },
    {
      "group": "第7组",
      "type": "prop_continuity",
      "evidence": "第7组组首写明沈砚川右手持有铁钎，3-7秒用铁钎指向半边水线，铁钎归属和使用连续；出口上方料场碎料作为堵口证据出现，未凭空改变道具状态。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "audio_mouth_sync",
      "result": "pass",
      "evidence": "沈砚川“还没完……”“还有一手。”均写为画面人物低声对自己说，属于真实开口自语，不涉及心声误作口型。",
      "fix_instruction": "若改成心声，应补写嘴唇闭合、不做口型；当前不需要修改。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组尾部众人等待林知夏判断去向，第4组组首复述林知夏、周大柱、沈小禾、沈母、赵有福等仍在洞口外，并让林知夏给出下口乱石滩判断，状态连续。",
      "fix_instruction": "若出现人物瞬移到乱石滩，应在第4组尾或第5组首补充奔跑到达；当前第4组已写众人冲向坡下。"
    },
    {
      "group": "第6组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "第6组只发生在旧河道下口乱石滩，组首列出沈砚川、林知夏、沈小禾、周大柱、沈母和村民的位置与朝向，沈母以背景坡道位置承载远喊。",
      "fix_instruction": "若沈母不在组首可见，应改为画外远喊并给出来源；当前组首已列出背景坡道位置。"
    },
    {
      "group": "第7组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "周大柱对沈砚川问“你咋看出来的？”，沈砚川对周大柱解释“水线只开半边”“出口上头压了料场”，随后对村民甲和众人下令，现场对白对象明确。",
      "fix_instruction": "若对白对象缺失，应补为A对B说道/问道/喊道；当前不需要修改。"
    },
    {
      "group": "第1组至第7组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "正文未出现Seedance模板编号、参考图、@图片/@视频/@音频、自动正反打、官方模板说明或禁止的模板化批量描述。",
      "fix_instruction": "若发现模型说明词或模板污染，应删除并改写成自然画面描述；当前不需要修改。"
    }
  ],
  "issues": [],
  "warnings": []
}
