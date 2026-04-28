# Agent Dispatch

Python is intentionally limited to prepare / validate / collect.
It must not launch Codex CLI, Qwen CLI, or any model process.

## Recommended Dispatch

Use the current Codex session or Codex subagents to process episodes.
Each episode is an independent task; run up to 5 in parallel if the host agent supports safe parallel work.

## Episode Tasks

- `ep01`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep01\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep01`.
- `ep02`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep02\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep02`.
- `ep03`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep03\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep03`.
- `ep04`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep04\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep04`.
- `ep05`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep05\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep05`.
- `ep06`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep06\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep06`.
- `ep07`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep07\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep07`.
- `ep08`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep08\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep08`.
- `ep09`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep09\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep09`.
- `ep10`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep10\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep10`.
- `ep11`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep11\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep11`.
- `ep12`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep12\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep12`.
- `ep13`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep13\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep13`.
- `ep14`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep14\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep14`.
- `ep15`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep15\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep15`.
- `ep16`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep16\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep16`.
- `ep17`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep17\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep17`.
- `ep18`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep18\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep18`.
- `ep19`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep19\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep19`.
- `ep20`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep20\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep20`.
- `ep21`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep21\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep21`.
- `ep22`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep22\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep22`.
- `ep23`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep23\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep23`.
- `ep24`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep24\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep24`.
- `ep25`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep25\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep25`.
- `ep26`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep26\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep26`.
- `ep27`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep27\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep27`.
- `ep28`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep28\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep28`.
- `ep29`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep29\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep29`.
- `ep30`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep30\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep30`.
- `ep31`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep31\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep31`.
- `ep32`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep32\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep32`.
- `ep33`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep33\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep33`.
- `ep34`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep34\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep34`.
- `ep35`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep35\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep35`.
- `ep36`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep36\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep36`.
- `ep37`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep37\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep37`.
- `ep38`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep38\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep38`.
- `ep39`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep39\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep39`.
- `ep40`: open `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep40\agent_prompt.md` and run it as one independent agent task. Required outputs are under `G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep40`.

## Manual CLI Example

If a human explicitly chooses to run a CLI, run it manually from PowerShell instead of through Python:

```powershell
codex exec --skip-git-repo-check --sandbox workspace-write --cd "G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed" - < "G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep01\agent_prompt.md"
```

Qwen example:

```powershell
qwen < "G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-reviewed\episodes\ep01\agent_prompt.md"
```

## Collect Results

After agents finish writing `final.txt` and `status.json` in each episode directory:

```powershell
.\COLLECT_RESULTS.ps1
```
