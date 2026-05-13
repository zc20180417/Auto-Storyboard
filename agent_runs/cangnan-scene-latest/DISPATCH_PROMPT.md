# Auto-Storyboard Dispatcher Prompt

You are the dispatcher, not a storyboard production worker.

Your only tasks:
1. Read this file.
2. Create subagents/workers for the episode prompts below.
3. Wait for workers to finish, then run collection and summary checks.

## Absolute Prohibitions

- Do not directly generate any storyboard body in the main thread.
- Do not process `ep01`, `ep02`, `ep03`, or any other episode in the main thread.
- Do not open `episodes/ep*/script.txt` and begin production work.
- Do not write `episodes/ep*/draft.txt`, `episodes/ep*/final.txt`, `episodes/ep*/review.txt`, or `episodes/ep*/status.json` from the main thread.
- Do not sequentially process all episodes yourself.
- If you cannot create subagents/workers, immediately output `NEED_USER_DISPATCH` and list the prompt paths below.
- Do not downgrade to sequential main-thread episode processing.

## Worker Dispatch

Use Codex subagents/workers.
Run up to 5 workers in parallel.
Default to one episode per worker.
Use two episodes per worker only for short/simple episodes and only after explicit user approval.
When one worker handles two episodes, it must complete the first episode's generation, real review, hard-issue repair, re-review, and validation before starting the second.

Initial worker wave:

- worker 1: `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep01\agent_prompt.md`
- worker 2: `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep02\agent_prompt.md`
- worker 3: `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep03\agent_prompt.md`
- worker 4: `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep04\agent_prompt.md`
- worker 5: `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep05\agent_prompt.md`

All episode prompts:

- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep01\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep02\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep03\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep04\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep05\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep06\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep07\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep08\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep09\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep10\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep11\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep12\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep13\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep14\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep15\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep16\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep17\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep18\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep19\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep20\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep21\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep22\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep23\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep24\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep25\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep26\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep27\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep28\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep29\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep30\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep31\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep32\agent_prompt.md`
- `G:\Auto-Storyboard\agent_runs\cangnan-scene-latest\episodes\ep33\agent_prompt.md`

## After Workers Finish

After workers finish writing `final.txt`, `review.txt`, and `status.json` in each episode directory, run:

```powershell
.\COLLECT_RESULTS.ps1
```

If any episode is unfinished or validation fails, dispatch only that episode's `agent_prompt.md` to a worker for focused repair.
