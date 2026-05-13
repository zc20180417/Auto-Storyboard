{
  "pass": true,
  "summary": "ep26 seg01 已对照原剧本和竖屏生成规则审核，关键台词、动作、证据道具、空间衔接和时间轴均可交付。",
  "checked_groups": ["第1组", "第2组", "第3组", "第4组", "第5组", "第6组"],
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
      "evidence": "原剧本中小货车打滑、周大柱喊“要翻了！”，林知夏喊“前头没路了！”，沈砚川甩麻绳并喊“拉！”，周大柱回应“拉住了！”均按顺序保留，未新增改变因果的动作。"
    },
    {
      "group": "第3组",
      "type": "dialogue_pacing",
      "evidence": "8-15秒承载林知夏三句短念读和村民乙一句反应，总有效台词约24字，7秒内约3.4字/秒，并含翻页、众人围看动作，不存在过快口型。"
    },
    {
      "group": "第4组",
      "type": "prop_continuity",
      "evidence": "第3组组尾明确红文件夹打开在林知夏和沈砚川手边，第4组0-3秒施工方代表一把抢走红文件夹，再抱紧文件夹奔向断崖小路，道具归属变化有可见过渡。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "evidence": "第5组组首锁定通山残路口，施工方代表靠近崖边并持有红文件夹，沈砚川、林知夏、周大柱等人在左侧泥路上，所有本组说话或反应人物均已可用。"
    },
    {
      "group": "第6组",
      "type": "dialogue_pacing",
      "evidence": "第6组0-3秒“你扔。”、3-5秒“啥？”、5-9秒“你今天跑不掉。”均为短句，分别配合逼近和群体反应，字秒比低于硬性上限且没有拖成超长台词镜头。"
    }
  ],
  "semantic_checks": [
    {
      "group": "第1组",
      "type": "generation_density",
      "result": "pass",
      "evidence": "本组包含车辆失控、两句预警、甩绳后拽三个强节拍，12秒内动作链完整，未叠加搜证或抢夺等额外强剧情。",
      "fix_instruction": "若不通过，应把甩绳后拽动作拆到下一组，或压缩预警反应而不删台词。"
    },
    {
      "group": "第2组",
      "type": "script_fidelity",
      "result": "pass",
      "evidence": "车身一抖、半边轮子悬空、沈砚川砸窗扳手刹、工人甲喊“你松手！”、沈砚川喊“下来！”、拽出驾驶位和小货车停死均与原剧本一致。",
      "fix_instruction": "若不通过，应只恢复缺失的车窗、手刹或拽人动作，不改写其他已通过镜头。"
    },
    {
      "group": "第3组",
      "type": "dialogue_direction",
      "result": "pass",
      "evidence": "林知夏、周大柱、沈砚川、村民乙的现场对白均写明对沈砚川、林知夏或众人说话，没有把短句写成无对象台词或假对象台词。",
      "fix_instruction": "若不通过，应给每句现场对白补真实听话人，例如对沈砚川或对众人说道。"
    },
    {
      "group": "第4组",
      "type": "handoff_continuity",
      "result": "pass",
      "evidence": "第3组组尾施工方代表在背景人群边缘盯着文件夹，第4组组首复述其位于人群边缘且朝向红文件夹，0-3秒抢走文件夹，前后状态连续。",
      "fix_instruction": "若不通过，应在第3组组尾或第4组组首补施工方代表位置和红文件夹归属。"
    },
    {
      "group": "第5组",
      "type": "space_locking",
      "result": "pass",
      "evidence": "本组只发生在通山残路口一个主要物理空间，崖边、黄水、众人位置、施工方代表手持红文件夹都在组首锁定中明确。",
      "fix_instruction": "若不通过，应把从小货车旁奔跑到残路口的过渡保留在第4组，避免第5组跨空间。"
    },
    {
      "group": "第6组",
      "type": "prompt_pollution",
      "result": "pass",
      "evidence": "最终分镜没有出现 Seedance 模板编号、参考图、自动正反打、模型说明词、官方占位符或模板化批量描述。",
      "fix_instruction": "若不通过，应删除工程说明词并改为自然画面动作、台词和光影描述。"
    }
  ],
  "issues": [],
  "warnings": []
}
