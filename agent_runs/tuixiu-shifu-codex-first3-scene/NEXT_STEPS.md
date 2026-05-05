# Agent Dispatch

Python is intentionally limited to prepare / validate / collect.
It must not launch Codex CLI, Qwen CLI, Kimi Code, or any model process.

## Recommended Dispatch

Use the current Codex session or Codex subagents to process episodes. Quality is checked per episode. Dispatch can use one episode per worker, or two adjacent short/simple episodes per worker when the scripts are small.
Run up to 5 workers in parallel if the host agent supports safe parallel work.
When one worker handles two episodes, finish generation, review, repair, and validation for the first episode before starting the second. Never merge reviews or outputs across episodes.

## Episode Tasks

- `ep01`: open `G:\Auto-Storyboard\agent_runs\tuixiu-shifu-codex-first3-scene\episodes\ep01\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\tuixiu-shifu-codex-first3-scene\episodes\ep01`.
- `ep02`: open `G:\Auto-Storyboard\agent_runs\tuixiu-shifu-codex-first3-scene\episodes\ep02\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\tuixiu-shifu-codex-first3-scene\episodes\ep02`.
- `ep03`: open `G:\Auto-Storyboard\agent_runs\tuixiu-shifu-codex-first3-scene\episodes\ep03\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\tuixiu-shifu-codex-first3-scene\episodes\ep03`.

## Manual CLI Example

If a human explicitly chooses to run a CLI, run it manually from PowerShell instead of through Python:

Codex example:

```powershell
codex exec --skip-git-repo-check --sandbox workspace-write --cd "G:\Auto-Storyboard\agent_runs\tuixiu-shifu-codex-first3-scene" - < "G:\Auto-Storyboard\agent_runs\tuixiu-shifu-codex-first3-scene\episodes\ep01\agent_prompt.md"
```

Qwen example:

```powershell
qwen < "G:\Auto-Storyboard\agent_runs\tuixiu-shifu-codex-first3-scene\episodes\ep01\agent_prompt.md"
```

## Collect Results

After agents finish writing `final.txt` and `status.json` in each episode directory:

```powershell
.\COLLECT_RESULTS.ps1
```
