import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import storyboard_agent_workspace as saw


def task(episode_id, script_chars, segments=1):
    return {
        "episode_id": episode_id,
        "prompt_file": f"H:/run/episodes/{episode_id}/agent_prompt.md",
        "episode_dir": f"H:/run/episodes/{episode_id}",
        "script_chars": script_chars,
        "segments": segments,
    }


class DynamicWorkerBatchTests(unittest.TestCase):
    def test_pairs_adjacent_short_simple_episodes(self):
        batches = saw.build_worker_batches([
            task("ep01", 1200),
            task("ep02", 1800),
            task("ep03", 900),
        ])

        self.assertEqual(
            [[item["episode_id"] for item in batch] for batch in batches],
            [["ep01", "ep02"], ["ep03"]],
        )

    def test_keeps_long_or_multi_segment_episodes_single(self):
        batches = saw.build_worker_batches([
            task("ep01", 1200),
            task("ep02", saw.SIMPLE_BATCH_MAX_SCRIPT_CHARS + 1),
            task("ep03", 900, segments=2),
            task("ep04", 1000),
            task("ep05", 1000),
        ])

        self.assertEqual(
            [[item["episode_id"] for item in batch] for batch in batches],
            [["ep01"], ["ep02"], ["ep03"], ["ep04", "ep05"]],
        )

    def test_dispatcher_files_include_dynamic_batches(self):
        with TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            episodes_dir = run_dir / "episodes"
            episodes = []
            for episode_id, script_chars in (("ep01", 1200), ("ep02", 1300), ("ep03", 4000)):
                episode_dir = episodes_dir / episode_id
                episode_dir.mkdir(parents=True)
                (episode_dir / "script.txt").write_text("x" * script_chars, encoding="utf-8")
                episodes.append({
                    **task(episode_id, script_chars),
                    "episode_dir": str(episode_dir),
                    "prompt_file": str(episode_dir / "agent_prompt.md"),
                })
            saw.write_json(run_dir / "manifest.json", {"episodes": episodes})

            saw.write_runner_scripts(run_dir=run_dir, agent="codex", parallelism=5, model=None)

            next_steps = (run_dir / "NEXT_STEPS.md").read_text(encoding="utf-8")
            self.assertIn("Dynamic worker batches:", next_steps)
            self.assertIn("- batch 1: `ep01`, `ep02`", next_steps)
            self.assertIn("- batch 2: `ep03`", next_steps)


if __name__ == "__main__":
    unittest.main()
