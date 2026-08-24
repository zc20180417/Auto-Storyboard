import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace

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

    def test_pairs_adjacent_continuous_scene_even_when_episodes_are_complex(self):
        ep01 = task("ep01", 6000, segments=3)
        ep02 = task("ep02", 7000, segments=4)
        ep01["continuity_with_next"] = True
        ep02["continuous_from_previous"] = True

        batches = saw.build_worker_batches([ep01, ep02])

        self.assertEqual(
            [[item["episode_id"] for item in batch] for batch in batches],
            [["ep01", "ep02"]],
        )

    def test_does_not_delay_independent_episode_behind_continuous_tail(self):
        ep02 = task("ep02", 1200)
        ep02["continuous_from_previous"] = True
        ep03 = task("ep03", 1200)

        batches = saw.build_worker_batches([ep02, ep03])

        self.assertEqual(
            [[item["episode_id"] for item in batch] for batch in batches],
            [["ep02"], ["ep03"]],
        )

    def test_detects_same_scene_at_adjacent_source_boundary(self):
        episodes = [
            saw.EpisodeInput(Path("ep01.txt"), 1, "ep01", "测试剧", "场1-1：外景 小区停车场 - 傍晚\n甲递出钥匙。"),
            saw.EpisodeInput(Path("ep02.txt"), 2, "ep02", "测试剧", "场2-1：外景 小区停车场 - 日\n乙接住钥匙。"),
        ]

        links = saw.build_source_continuity_links(episodes)

        self.assertEqual(len(links), 1)
        self.assertTrue(links[0]["time_conflict"])

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
            self.assertIn("- batch 1 [ready]: `ep01`, `ep02`", next_steps)
            self.assertIn("- batch 2 [ready]: `ep03`", next_steps)

    def test_initial_wave_skips_batches_waiting_for_previous_episode(self):
        with TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            episodes = []
            for episode_id in ("ep01", "ep02", "ep03", "ep04"):
                episode_dir = run_dir / "episodes" / episode_id
                episode_dir.mkdir(parents=True)
                item = {
                    **task(episode_id, 4000, segments=2),
                    "episode_dir": str(episode_dir),
                    "prompt_file": str(episode_dir / "agent_prompt.md"),
                }
                episodes.append(item)
            episodes[0]["continuity_with_next"] = True
            episodes[1]["continuous_from_previous"] = True
            episodes[1]["depends_on_episode"] = "ep01"
            episodes[1]["continuity_with_next"] = True
            episodes[2]["continuous_from_previous"] = True
            episodes[2]["depends_on_episode"] = "ep02"
            saw.write_json(run_dir / "manifest.json", {"episodes": episodes})

            saw.write_runner_scripts(run_dir=run_dir, agent="codex", parallelism=3, model=None)

            dispatch = (run_dir / "DISPATCH_PROMPT.md").read_text(encoding="utf-8")
            self.assertIn("- batch 2 [wait for `ep02`]: `ep03`", dispatch)
            initial_wave = dispatch.split("Initial worker wave:", 1)[1].split("All episode prompts:", 1)[0]
            self.assertIn("`ep01`, `ep02`", initial_wave)
            self.assertIn("`ep04`", initial_wave)
            self.assertNotIn("`ep03`", initial_wave)

    def test_prepare_writes_vertical_boundary_context_and_v2_contract(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source"
            source.mkdir()
            (source / "第01集.txt").write_text(
                "# 第1集\n场1-1：外景 小区道路 - 傍晚\n甲拦在车前。\n",
                encoding="utf-8",
            )
            (source / "第02集.txt").write_text(
                "# 第2集\n场2-1：外景 小区道路 - 日\n甲仍拦在车前。\n",
                encoding="utf-8",
            )
            args = SimpleNamespace(
                source=source,
                prompt=None,
                review_skill=None,
                workspace_dir=root / "runs",
                out_dir=root / "outputs",
                run_name="boundary-test",
                agent="codex",
                model=None,
                output_model_suffix="test",
                mode="scene",
                aspect="vertical",
                visual_style="live-action",
                parallelism=5,
                force=False,
            )

            result = saw.prepare_workspace(args)

            self.assertEqual(result, 0)
            run_dir = root / "runs" / "boundary-test"
            ep02 = run_dir / "episodes" / "ep02"
            boundary = (ep02 / "boundary_context.md").read_text(encoding="utf-8")
            metadata = saw.read_json(ep02 / "episode.json")
            manifest = saw.read_json(run_dir / "manifest.json")
            self.assertIn("continuous_from_previous: true", boundary)
            self.assertIn("previous_final: ../ep01/final.txt", boundary)
            self.assertEqual(metadata["vertical_review_contract_version"], 2)
            self.assertTrue(metadata["continuous_from_previous"])
            self.assertTrue(manifest["episodes"][0]["continuity_with_next"])


if __name__ == "__main__":
    unittest.main()
