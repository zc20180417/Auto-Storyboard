# Dispatcher Instructions

Python is intentionally limited to prepare / validate / collect.
It must not launch Codex CLI, Qwen CLI, Kimi Code, or any model process.

Do not treat this file as a production task list.
Give `DISPATCH_PROMPT.md` to the host agent. The host agent is a dispatcher only and must not write episode files itself.

## Hard Stop

- Main thread is the dispatcher, not a storyboard production worker.
- Main thread must not directly process any episode.
- Main thread must not open `episodes/ep*/script.txt` and start writing storyboard content.
- Main thread must not write `episodes/ep*/draft.txt`, `final.txt`, `review.txt`, or `status.json`.
- Main thread's only job is to create subagents/workers and dispatch episode prompts.
- If the current environment cannot create subagents/workers, or needs user authorization before creating them, immediately stop and reply `NEED_USER_DISPATCH` with the pending prompt list.
- Do not downgrade to sequential main-thread episode processing.

## Required Dispatch

Use Codex subagents/workers.
Run up to 3 workers in parallel.
Worker batches are generated dynamically from episode complexity.
Simple batch threshold: <= 2500 script chars and <= 1 segment.
Batch size limit: 2 episodes per worker.
When one worker handles two episodes, it must fully finish generation, review, repair, and validation for the first episode before starting the second.
Never merge reviews or outputs across episodes.

Dynamic worker batches:

- batch 1: `ep05`, `ep06` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep05\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep06\agent_prompt.md`
- batch 2: `ep07` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep07\agent_prompt.md`

Initial worker wave:

- worker 1: `ep05`, `ep06` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep05\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep06\agent_prompt.md`
- worker 2: `ep07` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep07\agent_prompt.md`

When any worker finishes, dispatch the next unfinished worker batch from the dynamic plan.

## Episode Tasks

- `ep05`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep05\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep05`.
- `ep06`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep06\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep06`.
- `ep07`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep07\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep07`.

## Pending Prompt List

- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep05\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep06\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep07\agent_prompt.md`

## Manual CLI Example

If a human explicitly chooses to run a CLI, run it manually from PowerShell instead of through Python:

Codex example:

```powershell
codex exec --skip-git-repo-check --sandbox workspace-write --cd "H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx" - < "H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep05\agent_prompt.md"
```

Qwen example:

```powershell
qwen < "H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\jianpo-jiutian-ep05-07-horizontal-cg-fx\episodes\ep05\agent_prompt.md"
```

## Collect Results

After agents finish writing `final.txt` and `status.json` in each episode directory:

```powershell
.\COLLECT_RESULTS.ps1
```
