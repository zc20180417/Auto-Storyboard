{
    "pass":  true,
    "summary":  "已对照25-5救场脚本审核，倒计时、江若晴握笔、陆凡推门救场、台词、金董惊问、夺合同和撕碎砸回均保留，无硬问题。",
    "checked_groups":  [
                           "第1组",
                           "第2组",
                           "第3组"
                       ],
    "audit_coverage":  {
                           "script_fidelity":  "checked",
                           "dialogue_direction":  "checked",
                           "timing_math":  "checked",
                           "dialogue_pacing":  "checked",
                           "space_locking":  "checked",
                           "format":  "checked",
                           "character_availability":  "checked",
                           "handoff_continuity":  "checked",
                           "filmability":  "checked",
                           "audio_mouth_sync":  "checked",
                           "generation_density":  "checked",
                           "prompt_pollution":  "checked"
                       },
    "spot_checks":  [
                        {
                            "group":  "第1组",
                            "type":  "script_fidelity",
                            "evidence":  "金董倒计时台词、江若晴颤抖握笔、会议室大门推开、陆凡“敢动她的家人...”均按顺序保留。"
                        },
                        {
                            "group":  "第2组",
                            "type":  "dialogue_pacing",
                            "evidence":  "江若晴“陆凡！你回来了！”2.5秒、金董“怎么可能！黑曼巴失手了？”3秒，均未超过6.5字/秒硬上限。"
                        },
                        {
                            "group":  "第3组",
                            "type":  "prop_continuity",
                            "evidence":  "第2组尾部合同被陆凡夺在手中，第3组组首复述陆凡手中持有收购合同，随后撕碎并砸向金董。"
                        }
                    ],
    "semantic_checks":  [
                            {
                                "group":  "第1组",
                                "type":  "character_availability",
                                "result":  "pass",
                                "evidence":  "陆凡在组首位于门外走廊暗处，先通过大门入场后再说话，突然救场可生成。",
                                "fix_instruction":  "若不通过，应在门外或前半段补陆凡入场。"
                            },
                            {
                                "group":  "第2组",
                                "type":  "handoff_continuity",
                                "result":  "pass",
                                "evidence":  "第1组尾部陆凡站门口、保镖倒地、江若晴握笔转头；第2组组首逐项复述。",
                                "fix_instruction":  "若不通过，应补门口倒地保镖和签字笔状态。"
                            },
                            {
                                "group":  "第3组",
                                "type":  "generation_density",
                                "result":  "pass",
                                "evidence":  "第3组8秒只承载撕合同和碎纸砸回两个短动作，是片尾道具动作余波，短组理由成立。",
                                "fix_instruction":  "若不通过，应并入第2组或扩展为10秒，但不能拖慢动作。"
                            }
                        ],
    "issues":  [

               ],
    "warnings":  [

                 ]
}
