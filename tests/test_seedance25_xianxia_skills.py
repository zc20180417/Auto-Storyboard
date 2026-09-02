import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "agent_skills" / "seedance-2-5-horizontal-xianxia-3d-cg-generator" / "SKILL.md"
REVIEWER = ROOT / "agent_skills" / "seedance-2-5-horizontal-xianxia-3d-cg-reviewer" / "SKILL.md"
PROFILE_DIR = ROOT / "agent_skills" / "seedance-2-5-horizontal-xianxia-3d-cg"
VFX = PROFILE_DIR / "references" / "xianxia-vfx-grammar.md"
AUDIO = PROFILE_DIR / "references" / "native-audio.md"
HANDOFF = PROFILE_DIR / "references" / "segment-handoff.md"


class Seedance25XianxiaSkillContractTests(unittest.TestCase):
    def read(self, path: Path) -> str:
        self.assertTrue(path.is_file(), f"missing required skill resource: {path}")
        return path.read_text(encoding="utf-8")

    def test_generator_owns_new_model_contract_and_reference_routing(self):
        text = self.read(GENERATOR)

        self.assertIn("name: seedance-2-5-horizontal-xianxia-3d-cg-generator", text)
        self.assertIn("4–30", text)
        self.assertIn("整数秒", text)
        self.assertIn("single", text)
        self.assertIn("16:9", text)
        self.assertIn("720p", text)
        self.assertIn("references/xianxia-vfx-grammar.md", text)
        self.assertIn("references/native-audio.md", text)
        self.assertIn("realistic-material-restrained-anime-outline", text)
        self.assertNotRegex(text, r"组时长硬范围\s*6-15|可以使用\s*0\.5\s*秒")

    def test_vfx_grammar_is_generic_semantic_not_a_project_pack(self):
        text = self.read(VFX)

        for term in ("来源", "形态", "路径", "作用对象", "反馈", "收束", "声音对应"):
            self.assertIn(term, text)
        for family in ("修为显化", "灵火", "炼丹", "丹药", "法器", "符箓", "阵法", "遁光", "回溯"):
            self.assertIn(family, text)
        for forbidden_project_fact in ("方平", "元鼎", "落阳宗", "每日九次"):
            self.assertNotIn(forbidden_project_fact, text)

    def test_native_audio_contract_covers_dialogue_world_and_vfx_without_bgm(self):
        text = self.read(AUDIO)

        for term in ("对白", "口型", "环境底噪", "动作拟音", "特效声", "空间方位", "静默", "无配乐"):
            self.assertIn(term, text)
        self.assertIn("声音先于画面", text)
        self.assertIn("画面先于声音", text)
        self.assertIn("同帧", text)

    def test_segment_handoff_uses_world_state_instead_of_last_frame(self):
        handoff = self.read(HANDOFF)
        generator = self.read(GENERATOR)
        reviewer = self.read(REVIEWER)

        for term in ("世界状态", "画外", "待重建/不可确认", "特写只改变观察焦点", "最后一帧不是连续性的真源"):
            self.assertIn(term, handoff)
        self.assertIn("references/segment-handoff.md", generator)
        self.assertIn("references/segment-handoff.md", reviewer)
        self.assertIn("上一组 `组尾衔接` 与下一组 `组间承接`", reviewer)

    def test_prompt_structure_preserves_dynamic_vfx_and_prepends_real_assets(self):
        profile = self.read(PROFILE_DIR / "SKILL.md")
        generator = self.read(GENERATOR)
        vfx = self.read(VFX)

        self.assertIn("全部真实引用资产及职责按", profile)
        self.assertIn("人物资产／场景资产／道具与关键视觉资产", profile)
        self.assertIn("整体画风说明", generator)
        self.assertNotIn("**一句话概述**", generator)
        self.assertIn("连续整数秒时间轴", generator)
        self.assertNotIn("**视觉峰值/特效重点**", generator)
        self.assertNotIn("**运镜强化词**", generator)
        self.assertNotIn("**Seedance执行提示补充**", generator)
        self.assertIn("不能替代动态语义链", vfx)
        self.assertIn("来源、形态、路径、作用对象、反馈、收束和声音", generator)

    def test_reviewer_requires_real_script_comparison_vfx_provenance_and_audio(self):
        text = self.read(REVIEWER)

        self.assertIn("name: seedance-2-5-horizontal-xianxia-3d-cg-reviewer", text)
        self.assertIn("原剧本", text)
        self.assertIn("当前 final.txt", text)
        self.assertIn("xianxia_vfx_provenance", text)
        self.assertIn("native_audio", text)
        self.assertIn("timing_math", text)
        self.assertIn("prompt_pollution", text)
        self.assertIn("checked_groups", text)
        self.assertIn("semantic_checks", text)
        self.assertIn("pass=false", text)
        self.assertNotIn("缺 cut_id、人物、场景、关键资产、视觉峰值", text)
        self.assertNotRegex(text, r"组总时长超出\s*6-15|0\.5\s*秒边界")


if __name__ == "__main__":
    unittest.main()
