import json
import shutil
import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]
PREPARE_AGENT = ROOT / "prepare-agent.ps1"


def ps_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


class PrepareAgentWrapperTests(unittest.TestCase):
    def test_visual_style_argument_is_forwarded_to_workspace_prepare(self):
        if shutil.which("powershell") is None:
            self.skipTest("PowerShell is required for prepare-agent.ps1 wrapper coverage")

        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "script.txt"
            capture = tmp_path / "python-args.json"
            source.write_text("第1集\n测试剧情。", encoding="utf-8")

            command = f"""
$ErrorActionPreference = "Stop"
function global:python {{
    $args | ConvertTo-Json -Compress | Set-Content -Encoding UTF8 -LiteralPath {ps_quote(str(capture))}
}}
& {ps_quote(str(PREPARE_AGENT))} `
    -Mode scene `
    -RunName demo-cg `
    -Source {ps_quote(str(source))} `
    -OutDir {ps_quote(str(tmp_path / "outputs"))} `
    -WorkspaceDir {ps_quote(str(tmp_path / "agent_runs"))} `
    -VisualStyle 3d-cg `
    -Force
"""
            result = subprocess.run(
                ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", command],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 0, msg=result.stderr + result.stdout)
            args = json.loads(capture.read_text(encoding="utf-8-sig"))
            self.assertIn("--visual-style", args)
            self.assertEqual(args[args.index("--visual-style") + 1], "3d-cg")
            self.assertIn("--video-profile", args)
            self.assertEqual(args[args.index("--video-profile") + 1], "seedance-2.0")

    def test_seedance25_profile_and_resolution_are_forwarded(self):
        if shutil.which("powershell") is None:
            self.skipTest("PowerShell is required for prepare-agent.ps1 wrapper coverage")

        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "script.txt"
            capture = tmp_path / "python-args.json"
            source.write_text("第1集\n测试剧情。", encoding="utf-8")

            command = f"""
$ErrorActionPreference = "Stop"
function global:python {{
    $args | ConvertTo-Json -Compress | Set-Content -Encoding UTF8 -LiteralPath {ps_quote(str(capture))}
}}
& {ps_quote(str(PREPARE_AGENT))} `
    -Mode scene `
    -RunName demo-seedance25 `
    -Source {ps_quote(str(source))} `
    -OutDir {ps_quote(str(tmp_path / "outputs"))} `
    -WorkspaceDir {ps_quote(str(tmp_path / "agent_runs"))} `
    -Aspect vertical `
    -VisualStyle live-action `
    -VideoProfile seedance-2.5-live-vertical `
    -VideoResolution 480p `
    -Force
"""
            result = subprocess.run(
                ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", command],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 0, msg=result.stderr + result.stdout)
            args = json.loads(capture.read_text(encoding="utf-8-sig"))
            self.assertEqual(args[args.index("--video-profile") + 1], "seedance-2.5-live-vertical")
            self.assertEqual(args[args.index("--video-resolution") + 1], "480p")


if __name__ == "__main__":
    unittest.main()
