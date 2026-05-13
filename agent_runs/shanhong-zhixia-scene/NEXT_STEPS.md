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

- worker 1: `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep01\agent_prompt.md`
- worker 2: `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep02\agent_prompt.md`
- worker 3: `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep03\agent_prompt.md`
- worker 4: `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep04\agent_prompt.md`
- worker 5: `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep05\agent_prompt.md`

When any worker finishes, dispatch the next unfinished episode prompt.

## Episode Tasks

- `ep01`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep01\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep01`.
- `ep02`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep02\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep02`.
- `ep03`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep03\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep03`.
- `ep04`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep04\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep04`.
- `ep05`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep05\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep05`.
- `ep06`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep06\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep06`.
- `ep07`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep07\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep07`.
- `ep08`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep08\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep08`.
- `ep09`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep09\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep09`.
- `ep10`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep10\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep10`.
- `ep11`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep11\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep11`.
- `ep12`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep12\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep12`.
- `ep13`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep13\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep13`.
- `ep14`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep14\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep14`.
- `ep15`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep15\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep15`.
- `ep16`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep16\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep16`.
- `ep17`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep17\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep17`.
- `ep18`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep18\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep18`.
- `ep19`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep19\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep19`.
- `ep20`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep20\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep20`.
- `ep21`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep21\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep21`.
- `ep22`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep22\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep22`.
- `ep23`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep23\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep23`.
- `ep24`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep24\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep24`.
- `ep25`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep25\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep25`.
- `ep26`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep26\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep26`.
- `ep27`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep27\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep27`.
- `ep28`: dispatch `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep28\agent_prompt.md` to one worker. Worker writes only under `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep28`.

## Pending Prompt List

- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep01\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep02\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep03\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep04\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep05\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep06\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep07\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep08\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep09\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep10\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep11\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep12\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep13\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep14\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep15\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep16\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep17\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep18\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep19\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep20\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep21\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep22\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep23\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep24\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep25\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep26\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep27\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep28\agent_prompt.md`

## Manual CLI Example

If a human explicitly chooses to run a CLI, run it manually from PowerShell instead of through Python:

Codex example:

```powershell
codex exec --skip-git-repo-check --sandbox workspace-write --cd "G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene" - < "G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep01\agent_prompt.md"
```

Qwen example:

```powershell
qwen < "G:\Auto-Storyboard\agent_runs\shanhong-zhixia-scene\episodes\ep01\agent_prompt.md"
```

## Collect Results

After agents finish writing `final.txt` and `status.json` in each episode directory:

```powershell
.\COLLECT_RESULTS.ps1
```
