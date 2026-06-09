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
            happyhorse_profile_path=None,
            ai_video_prompt_skill_path=None,
            target_video_model="seedance",
            aspect="vertical",
            mode="scene",
        )

        self.assertIn("## Production Focus", task)
        self.assertLess(task.index("## Production Focus"), task.index("## Workflow"))
        self.assertIn("组首空间锁定等于本组第一帧", task)
        self.assertIn("每个时间段默认只承载一个主动作", task)
        self.assertIn("不要为凑满 10 秒硬塞动作、对白或停顿", task)
        self.assertIn("高冲击打断", task)
        self.assertIn("归位动作", task)
        self.assertIn("视频禁止项", task)
        self.assertIn("本组或本集上下文", task)
        self.assertIn("完整规则仍以 generator/reviewer skill 和 quality policy 为准", task)


if __name__ == "__main__":
    unittest.main()
