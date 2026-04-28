# Agent Dispatch

Python is intentionally limited to prepare / validate / collect.
It must not launch Codex CLI, Qwen CLI, or any model process.

## Recommended Dispatch

Use the current Codex session or Codex subagents to process episodes.
Quality is checked per episode. Dispatch can use one episode per worker, or two adjacent short/simple episodes per worker when the scripts are small.
Run up to 5 workers in parallel if the host agent supports safe parallel work.
When one worker handles two episodes, finish generation, review, repair, and validation for the first episode before starting the second. Never merge reviews or outputs across episodes.

## Episode Tasks

- `ep01`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep01\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep01`.
- `ep02`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep02\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep02`.
- `ep03`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep03\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep03`.
- `ep04`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep04\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep04`.
- `ep05`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep05\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep05`.
- `ep06`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep06\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep06`.
- `ep07`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep07\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep07`.
- `ep08`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep08\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep08`.
- `ep09`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep09\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep09`.
- `ep10`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep10\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep10`.
- `ep11`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep11\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep11`.
- `ep12`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep12\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep12`.
- `ep13`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep13\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep13`.
- `ep14`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep14\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep14`.
- `ep15`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep15\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep15`.
- `ep16`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep16\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep16`.
- `ep17`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep17\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep17`.
- `ep18`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep18\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep18`.
- `ep19`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep19\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep19`.
- `ep20`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep20\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep20`.
- `ep21`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep21\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep21`.
- `ep22`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep22\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep22`.
- `ep23`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep23\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep23`.
- `ep24`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep24\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep24`.
- `ep25`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep25\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep25`.
- `ep26`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep26\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep26`.
- `ep27`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep27\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep27`.
- `ep28`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep28\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep28`.
- `ep29`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep29\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep29`.
- `ep30`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep30\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep30`.
- `ep31`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep31\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep31`.
- `ep32`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep32\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep32`.
- `ep33`: open `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep33\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep33`.

## Manual CLI Example

If a human explicitly chooses to run a CLI, run it manually from PowerShell instead of through Python:

```powershell
codex exec --skip-git-repo-check --sandbox workspace-write --cd "G:\Auto-Storyboard\agent_runs\cangnan-scene" - < "G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep01\agent_prompt.md"
```

Qwen example:

```powershell
qwen < "G:\Auto-Storyboard\agent_runs\cangnan-scene\episodes\ep01\agent_prompt.md"
```

## Collect Results

After agents finish writing `final.txt` and `status.json` in each episode directory:

```powershell
.\COLLECT_RESULTS.ps1
```
