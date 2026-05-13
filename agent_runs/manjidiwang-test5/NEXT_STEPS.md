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
Run up to 5 workers in parallel.
Default to one episode per worker.
Use two episodes per worker only for short/simple episodes and only after explicit user approval.
When one worker handles two episodes, it must fully finish generation, review, repair, and validation for the first episode before starting the second.
Never merge reviews or outputs across episodes.

Initial worker wave:

- worker 1: `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep01\agent_prompt.md`
- worker 2: `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep02\agent_prompt.md`
- worker 3: `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep03\agent_prompt.md`
- worker 4: `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep04\agent_prompt.md`
- worker 5: `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep05\agent_prompt.md`

When any worker finishes, dispatch the next unfinished episode prompt.

## Episode Tasks

- `ep01`: dispatch `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep01\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep01`.
- `ep02`: dispatch `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep02\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep02`.
- `ep03`: dispatch `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep03\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep03`.
- `ep04`: dispatch `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep04\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep04`.
- `ep05`: dispatch `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep05\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep05`.

## Pending Prompt List

- `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep01\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep02\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep03\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep04\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep05\agent_prompt.md`

## Manual CLI Example

If a human explicitly chooses to run a CLI, run it manually from PowerShell instead of through Python:

Codex example:

```powershell
codex exec --skip-git-repo-check --sandbox workspace-write --cd "G:\Auto-Storyboard\agent_runs\manjidiwang-test5" - < "G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep01\agent_prompt.md"
```

Qwen example:

```powershell
qwen < "G:\Auto-Storyboard\agent_runs\manjidiwang-test5\episodes\ep01\agent_prompt.md"
```

## Collect Results

After agents finish writing `final.txt` and `status.json` in each episode directory:

```powershell
.\COLLECT_RESULTS.ps1
```
