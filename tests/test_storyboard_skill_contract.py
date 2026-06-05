import unittest
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR_SKILL = ROOT / "agent_skills" / "storyboard-generator" / "SKILL.md"
REVIEWER_SKILL = ROOT / "agent_skills" / "storyboard-reviewer" / "SKILL.md"
CRAFT_PASS_SKILL = ROOT / "agent_skills" / "storyboard-craft-pass" / "SKILL.md"
QUALITY_POLICY = ROOT / "agent_skills" / "storyboard-quality-policy.json"
DIALOGUE_PROMPT = ROOT / "竖屏分镜规则_对话版.txt"


class StoryboardSkillContractTests(unittest.TestCase):
    def test_generator_has_front_loaded_production_priorities(self):
        text = GENERATOR_SKILL.read_text(encoding="utf-8")

        self.assertIn("## 生产优先级（先读此段）", text)
        self.assertIn("最终分镜首先服务“视频模型稳定执行”", text)
        self.assertIn("时间规则服务于视频可执行性", text)
        self.assertIn("12. 复杂动作、保护站位、关键道具、多人物调度组可写短 `视频禁止项`", text)
        self.assertIn("内部检查以下 6 项", text)

    def test_generator_uses_modern_video_execution_examples(self):
        text = GENERATOR_SKILL.read_text(encoding="utf-8")

        self.assertIn("示例 A：外部事件进入", text)
        self.assertIn("示例 B：保护站位和关键道具连续", text)
        self.assertIn("车队压住庆贺声", text)
        self.assertIn("林远挡到父母身前", text)
        self.assertNotIn("朝堂对峙", text)

    def test_video_negative_hints_are_limited_and_specific(self):
        generator_text = GENERATOR_SKILL.read_text(encoding="utf-8")
        reviewer_text = REVIEWER_SKILL.read_text(encoding="utf-8")

        self.assertIn("每组写 2-5 个本组特有错误", generator_text)
        self.assertIn("不每组复制同一串通用词", generator_text)
        self.assertIn("模板中的 `视频禁止项` 只是占位示例", generator_text)
        self.assertNotIn("视频禁止项：成绩单消失、林远提前上车", generator_text)
        self.assertIn("`视频禁止项` 超过 5 个", reviewer_text)
        self.assertIn("泛泛词如“画面混乱/人物错误/道具错误”", reviewer_text)

    def test_video_negative_policy_is_externalized(self):
        policy = json.loads(QUALITY_POLICY.read_text(encoding="utf-8"))

        self.assertIn("storyboard_rule_version", policy)
        self.assertEqual(policy["video_negative_constraints"]["max_items"], 5)
        self.assertIn("人物换位", policy["video_negative_constraints"]["generic_terms"])
        self.assertIn("本组关键道具消失", policy["video_negative_constraints"]["placeholder_terms"])
        self.assertIn("context_anchor_stop_terms", policy["video_negative_constraints"])
        self.assertIn("人物", policy["video_negative_constraints"]["context_anchor_stop_terms"])

    def test_external_event_entry_rule_is_reviewed(self):
        generator_text = GENERATOR_SKILL.read_text(encoding="utf-8")
        reviewer_text = REVIEWER_SKILL.read_text(encoding="utf-8")

        self.assertIn("外部事件进入规则", generator_text)
        self.assertIn("事件进入 → 关键人物/道具状态变化 → 主角或被影响者反应 → 对峙/台词", generator_text)
        self.assertIn("外部事件进入被压缩到不可执行", reviewer_text)
        self.assertIn("优先按动作阶段写成同组内多个时间段", generator_text)
        self.assertIn("不应仅因强节拍数量多而判错", reviewer_text)

    def test_continuous_event_chains_are_not_mechanically_split(self):
        generator_text = GENERATOR_SKILL.read_text(encoding="utf-8")
        reviewer_text = REVIEWER_SKILL.read_text(encoding="utf-8")

        self.assertIn("强节拍是容量核算工具，不是自动拆组触发器", generator_text)
        self.assertIn("连续事件链", generator_text)
        self.assertIn("不要因为每一步都有状态变化就机械拆成多个 10-15 秒组", generator_text)
        self.assertIn("强节拍只用于判断容量，不用于机械拆组", generator_text)
        self.assertIn("不能只按数量判 hard issue", reviewer_text)
        self.assertNotIn("对白+外部事件+中等/长动作+道具操作 同组？→ 是则拆组", generator_text)

    def test_high_impact_interrupt_reposition_rule_is_reviewed(self):
        generator_text = GENERATOR_SKILL.read_text(encoding="utf-8")
        reviewer_text = REVIEWER_SKILL.read_text(encoding="utf-8")

        self.assertIn("高冲击打断与归位规则", generator_text)
        self.assertIn("打断/反应", generator_text)
        self.assertIn("放下道具/跨位移/保护站位/团圆确认", generator_text)
        self.assertIn("高冲击打断后又压入归位动作", reviewer_text)

    def test_reviewer_template_includes_video_execution_coverage(self):
        text = REVIEWER_SKILL.read_text(encoding="utf-8")

        self.assertIn("生产 reviewer 默认也应在 `audit_coverage` 中包含并检查", text)
        self.assertIn('"action_atomicity": "checked"', text)
        self.assertIn('"video_negative_constraints": "checked"', text)
        self.assertIn('"type": "action_atomicity"', text)
        self.assertIn('"type": "video_negative_constraints"', text)

    def test_generator_prevents_low_density_time_padding(self):
        text = GENERATOR_SKILL.read_text(encoding="utf-8")

        self.assertIn("先估每个剧情块的自然时长，再组合成 6-15 秒组", text)
        self.assertIn("10-15 秒是常规承载区间，不是填满目标", text)
        self.assertIn("12-15 秒长组准入", text)
        self.assertIn("至少满足以下两项", text)
        self.assertIn("连续 3 个及以上 12-15 秒组", text)
        self.assertIn("明显多数（约三分之二以上）", text)
        self.assertIn("低密度组必须压缩或合并", text)
        self.assertIn("看向、低头、停住、等待、仍、继续、状态延续", text)
        self.assertIn("连续流程动作合并", text)
        self.assertIn("联系后勤、准备保温箱、递出一箱、登记一行、复核无误", text)
        self.assertIn("设备到场、接线、压缩机恢复", text)

    def test_reviewer_flags_low_density_padding_and_fragmented_process_groups(self):
        text = REVIEWER_SKILL.read_text(encoding="utf-8")

        self.assertIn("12-15 秒长组未过长组准入", text)
        self.assertIn("低密度撑时长", text)
        self.assertIn("相邻同场景同冲突的流程节点", text)
        self.assertIn("联系、准备、递出、登记、复核", text)
        self.assertIn("不应各自写成 10-15 秒组", text)
        self.assertIn("连续 3 个及以上 12-15 秒组", text)
        self.assertIn("按 `generation_density` 或 `dialogue_pacing` 判 hard issue", text)

    def test_dramatic_pause_is_not_a_padding_exception(self):
        generator_text = GENERATOR_SKILL.read_text(encoding="utf-8")
        reviewer_text = REVIEWER_SKILL.read_text(encoding="utf-8")

        self.assertIn("停顿不是质感例外", generator_text)
        self.assertIn("不再提供有动机戏剧停顿例外", generator_text)
        self.assertIn("高冲击后的可见反应可以写入已有镜头", generator_text)
        self.assertIn("不豁免连续无台词铺垫", generator_text)
        self.assertIn("停顿不是合法 craft 例外", reviewer_text)
        self.assertIn("不能因为身份揭穿、重大证据落地或关系崩塌就自动放行", reviewer_text)
        self.assertNotIn("有动机戏剧停顿（极窄例外，默认不用）", generator_text)
        self.assertNotIn("1.5-2.5 秒", reviewer_text)

    def test_craft_pass_cannot_suggest_extra_time(self):
        text = CRAFT_PASS_SKILL.read_text(encoding="utf-8")

        self.assertIn("只替换，不加秒", text)
        self.assertIn("不得建议新增时间段、延长组时长", text)
        self.assertIn("不建议新增停顿或延长总时长", text)
        self.assertNotIn("1.5-2.5 秒", text)

    def test_dialogue_prompt_matches_rhythm_economy_contract(self):
        text = DIALOGUE_PROMPT.read_text(encoding="utf-8")

        self.assertIn("先估自然时长", text)
        self.assertIn("10-15 秒只是常规承载区间，不是填满目标", text)
        self.assertIn("低密度组必须压缩或合并", text)
        self.assertIn("12-15 秒长组准入", text)
        self.assertIn("连续 3 个及以上 12-15 秒组", text)
        self.assertIn("连续流程动作合并", text)
        self.assertIn("停顿不是质感例外", text)
        self.assertNotIn("有动机戏剧停顿（极窄例外，默认不用）", text)
        self.assertIn("组尾衔接只写连续性锚点", text)
        self.assertNotIn("默认 10-15 秒", text)
        self.assertNotIn("自然收尾", text)


if __name__ == "__main__":
    unittest.main()
