import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR_SKILL = ROOT / "agent_skills" / "storyboard-generator" / "SKILL.md"
REVIEWER_SKILL = ROOT / "agent_skills" / "storyboard-reviewer" / "SKILL.md"


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

    def test_external_event_entry_rule_is_reviewed(self):
        generator_text = GENERATOR_SKILL.read_text(encoding="utf-8")
        reviewer_text = REVIEWER_SKILL.read_text(encoding="utf-8")

        self.assertIn("外部事件进入规则", generator_text)
        self.assertIn("事件进入 → 关键人物/道具状态变化 → 主角或被影响者反应 → 对峙/台词", generator_text)
        self.assertIn("外部事件进入被压缩到不可执行", reviewer_text)

    def test_reviewer_template_includes_video_execution_coverage(self):
        text = REVIEWER_SKILL.read_text(encoding="utf-8")

        self.assertIn("生产 reviewer 默认也应在 `audit_coverage` 中包含并检查", text)
        self.assertIn('"action_atomicity": "checked"', text)
        self.assertIn('"video_negative_constraints": "checked"', text)
        self.assertIn('"type": "action_atomicity"', text)
        self.assertIn('"type": "video_negative_constraints"', text)


if __name__ == "__main__":
    unittest.main()
