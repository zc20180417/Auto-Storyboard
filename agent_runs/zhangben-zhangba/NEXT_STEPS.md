# Agent Dispatch

Python is intentionally limited to prepare / validate / collect.
It must not launch Codex CLI, Qwen CLI, Kimi Code, or any model process.

## Recommended Dispatch

Use the current Kimi Code session or Kimi Code Agent tools to process episodes. Quality is checked per episode. Dispatch can use one episode per worker, or two adjacent short/simple episodes per worker when the scripts are small.
Run up to 5 workers in parallel if the host agent supports safe parallel work.
When one worker handles two episodes, finish generation, review, repair, and validation for the first episode before starting the second. Never merge reviews or outputs across episodes.

## Episode Tasks

- `ep01`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep01\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep01`.
- `ep02`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep02\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep02`.
- `ep03`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep03\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep03`.
- `ep04`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep04\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep04`.
- `ep05`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep05\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep05`.
- `ep06`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep06\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep06`.
- `ep07`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep07\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep07`.
- `ep08`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep08\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep08`.
- `ep09`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep09\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep09`.
- `ep10`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep10\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep10`.
- `ep11`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep11\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep11`.
- `ep12`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep12\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep12`.
- `ep13`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep13\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep13`.
- `ep14`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep14\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep14`.
- `ep15`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep15\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep15`.
- `ep16`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep16\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep16`.
- `ep17`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep17\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep17`.
- `ep18`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep18\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep18`.
- `ep19`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep19\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep19`.
- `ep20`: open `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep20\agent_prompt.md` and process it as an independent episode. Required outputs are under `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep20`.

## Manual CLI Example

If a human explicitly chooses to run a CLI, run it manually from PowerShell instead of through Python:

Codex example:

```powershell
codex exec --skip-git-repo-check --sandbox workspace-write --cd "G:\Auto-Storyboard\agent_runs\zhangben-zhangba" - < "G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep01\agent_prompt.md"
```

Qwen example:

```powershell
qwen < "G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep01\agent_prompt.md"
```

Kimi Code example:

Open Kimi Code in the workspace and use the Agent tool with the prompt from `G:\Auto-Storyboard\agent_runs\zhangben-zhangba\episodes\ep01\agent_prompt.md`.

## Collect Results

After agents finish writing `final.txt` and `status.json` in each episode directory:

```powershell
.\COLLECT_RESULTS.ps1
```
