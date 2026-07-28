import unittest
from pathlib import Path

import storyboard_agent_workspace as saw


class EpisodeTaskFocusTests(unittest.TestCase):
    def test_vertical_task_front_loads_short_production_focus(self):
        task = saw.make_episode_task(
            run_dir=Path("H:/run"),
            episode_dir=Path("H:/run/episodes/ep01"),
            episode=saw.EpisodeInput(
                source_path=Path("H:/scripts/ep01.txt"),
                episode_number=1,
                display_name="ep01",
                series_title="测试剧",
                script_text="第1集\n",
            ),
            episode_id="ep01",
            output_name="ep01-storyboard.txt",
            generator_skill_path=Path("H:/project/agent_skills/storyboard-generator/SKILL.md"),
            reviewer_skill_path=Path("H:/project/agent_skills/storyboard-reviewer/SKILL.md"),
            seedance_profile_path=Path("H:/project/agent_skills/seedance-prompt-profile/SKILL.md"),
            aspect="vertical",
            mode="scene",
        )

        self.assertIn("## Production Focus", task)
        self.assertLess(task.index("## Production Focus"), task.index("## Workflow"))
        self.assertIn("组首空间锁定等于本组第一帧", task)
        self.assertIn("每个时间段默认只承载一个主动作", task)
        self.assertIn("紧凑动作链可在 2-3 秒完成", task)
        self.assertIn("每镜可合理运镜也可固定机位，不设数量指标", task)
        self.assertIn("Cross-episode boundary: `boundary_context.md`", task)
        self.assertIn("`dialogue_checks`, `handoff_checks`, `camera_motion_checks`", task)
        self.assertIn("不要为凑满 10 秒硬塞动作、对白或停顿", task)
        self.assertIn("高冲击打断", task)
        self.assertIn("归位动作", task)
        self.assertIn("视频禁止项", task)
        self.assertIn("本组或本集上下文", task)
        self.assertIn("完整规则仍以 generator/reviewer skill 和 quality policy 为准", task)

    def test_horizontal_3d_cg_task_uses_inline_cg_tail_contract(self):
        task = saw.make_episode_task(
            run_dir=Path("H:/run"),
            episode_dir=Path("H:/run/episodes/ep01"),
            episode=saw.EpisodeInput(
                source_path=Path("H:/scripts/ep01.txt"),
                episode_number=1,
                display_name="ep01",
                series_title="测试剧",
                script_text="第1集\n",
            ),
            episode_id="ep01",
            output_name="ep01-storyboard.txt",
            generator_skill_path=Path("H:/project/agent_skills/storyboard-horizontal-generator/SKILL.md"),
            reviewer_skill_path=Path("H:/project/agent_skills/storyboard-horizontal-reviewer/SKILL.md"),
            seedance_profile_path=Path("H:/project/agent_skills/seedance-prompt-profile/SKILL.md"),
            cg_visual_style_skill_path=Path("H:/project/agent_skills/3d-cg-visual-style/SKILL.md"),
            visual_style="3d-cg",
            aspect="horizontal",
            mode="scene",
        )

        self.assertIn("3D CG visual style skill", task)
        self.assertIn("agent_skills/3d-cg-visual-style/SKILL.md", task.replace("\\", "/"))
        self.assertIn("横屏 final.txt 每组必须直接写入 3D CG 版", task)
        self.assertIn("负向不得包含 `3D渲染`、`CG感`、`动画感`、`卡通`、`动漫`、`二次元`", task)
        self.assertIn("3D CG 横屏每组至少安排 1 个有明确路径或落点的可见运镜", task)
        self.assertIn("视觉峰值不只来自打斗", task)
        self.assertIn("关键道具显影、身份揭示、权力压场、危险进入、环境异变、心理冲击、信息落点", task)
        self.assertIn("beat/hero 级视觉峰值", task)
        self.assertIn("不能只靠固定画面风格尾部", task)
        self.assertNotIn("灵药/玄铁/真气/罡气/剑气题材的强节拍", task)
        self.assertNotIn("真人实拍短剧质感", task)


if __name__ == "__main__":
    unittest.main()
