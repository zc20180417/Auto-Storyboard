# Agent Dispatch

Python is intentionally limited to prepare / validate / collect.
It must not launch Codex CLI, Qwen CLI, or any model process.

## Recommended Dispatch

Use the current Codex session or Codex subagents to process episodes.
Each episode is an independent task; run up to 5 in parallel if the host agent supports safe parallel work.

## Episode Tasks

- `ep01`: open `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep01\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep01`.
- `ep02`: open `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep02\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep02`.
- `ep03`: open `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep03\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep03`.
- `ep04`: open `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep04\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep04`.
- `ep05`: open `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep05\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep05`.
- `ep06`: open `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep06\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep06`.
- `ep07`: open `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep07\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep07`.
- `ep08`: open `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep08\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep08`.
- `ep09`: open `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep09\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep09`.
- `ep10`: open `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep10\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep10`.
- `ep11`: open `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep11\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep11`.
- `ep12`: open `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep12\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep12`.
- `ep13`: open `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep13\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep13`.
- `ep14`: open `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep14\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep14`.

## Manual CLI Example

If a human explicitly chooses to run a CLI, run it manually from PowerShell instead of through Python:

```powershell
codex exec --skip-git-repo-check --sandbox workspace-write --cd "G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene" - < "G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep01\agent_prompt.md"
```

Qwen example:

```powershell
qwen < "G:\Auto-Storyboard\agent_runs\youyuanzhai6-scene\episodes\ep01\agent_prompt.md"
```

## Collect Results

After agents finish writing `final.txt` and `status.json` in each episode directory:

```powershell
.\COLLECT_RESULTS.ps1
```
