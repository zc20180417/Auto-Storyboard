# Agent Dispatch

Python is intentionally limited to prepare / validate / collect.
It must not launch Codex CLI, Qwen CLI, or any model process.

## Recommended Dispatch

Use the current Codex session or Codex subagents to process episodes.
Each episode is an independent task; run up to 5 in parallel if the host agent supports safe parallel work.

## Episode Tasks

- `ep21`: open `G:\Auto-Storyboard\agent_runs\test-single\episodes\ep21\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\test-single\episodes\ep21`.
- `ep22`: open `G:\Auto-Storyboard\agent_runs\test-single\episodes\ep22\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\test-single\episodes\ep22`.
- `ep23`: open `G:\Auto-Storyboard\agent_runs\test-single\episodes\ep23\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\test-single\episodes\ep23`.
- `ep24`: open `G:\Auto-Storyboard\agent_runs\test-single\episodes\ep24\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\test-single\episodes\ep24`.
- `ep25`: open `G:\Auto-Storyboard\agent_runs\test-single\episodes\ep25\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\test-single\episodes\ep25`.

## Manual CLI Example

If a human explicitly chooses to run a CLI, run it manually from PowerShell instead of through Python:

```powershell
codex exec --skip-git-repo-check --sandbox workspace-write --cd "G:\Auto-Storyboard\agent_runs\test-single" - < "G:\Auto-Storyboard\agent_runs\test-single\episodes\ep21\agent_prompt.md"
```

Qwen example:

```powershell
qwen < "G:\Auto-Storyboard\agent_runs\test-single\episodes\ep21\agent_prompt.md"
```

## Collect Results

After agents finish writing `final.txt` and `status.json` in each episode directory:

```powershell
.\COLLECT_RESULTS.ps1
```
