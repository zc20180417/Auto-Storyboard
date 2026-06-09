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
Worker batches are generated dynamically from episode complexity.
Simple batch threshold: <= 2500 script chars and <= 1 segment.
Batch size limit: 2 episodes per worker.
When one worker handles two episodes, it must complete the first episode's generation, real review, hard-issue repair, re-review, and validation before starting the second.

Dynamic worker batches:

- batch 1: `ep01`, `ep02` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep01\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep02\agent_prompt.md`
- batch 2: `ep03`, `ep04` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep03\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep04\agent_prompt.md`
- batch 3: `ep05`, `ep06` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep05\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep06\agent_prompt.md`
- batch 4: `ep07`, `ep08` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep07\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep08\agent_prompt.md`
- batch 5: `ep09`, `ep10` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep09\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep10\agent_prompt.md`
- batch 6: `ep11`, `ep12` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep11\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep12\agent_prompt.md`
- batch 7: `ep13`, `ep14` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep13\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep14\agent_prompt.md`
- batch 8: `ep15`, `ep16` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep15\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep16\agent_prompt.md`
- batch 9: `ep17`, `ep18` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep17\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep18\agent_prompt.md`
- batch 10: `ep19`, `ep20` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep19\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep20\agent_prompt.md`
- batch 11: `ep21`, `ep22` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep21\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep22\agent_prompt.md`
- batch 12: `ep23`, `ep24` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep23\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep24\agent_prompt.md`
- batch 13: `ep25`, `ep26` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep25\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep26\agent_prompt.md`

Initial worker wave:

- worker 1: `ep01`, `ep02` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep01\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep02\agent_prompt.md`
- worker 2: `ep03`, `ep04` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep03\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep04\agent_prompt.md`
- worker 3: `ep05`, `ep06` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep05\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep06\agent_prompt.md`
- worker 4: `ep07`, `ep08` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep07\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep08\agent_prompt.md`
- worker 5: `ep09`, `ep10` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep09\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep10\agent_prompt.md`

All episode prompts:

- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep01\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep02\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep03\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep04\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep05\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep06\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep07\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep08\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep09\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep10\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep11\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep12\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep13\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep14\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep15\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep16\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep17\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep18\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep19\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep20\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep21\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep22\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep23\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep24\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep25\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603\episodes\ep26\agent_prompt.md`

## After Workers Finish

After workers finish writing `final.txt`, `review.txt`, and `status.json` in each episode directory, run:

```powershell
.\COLLECT_RESULTS.ps1
```

If any episode is unfinished or validation fails, dispatch only that episode's `agent_prompt.md` to a worker for focused repair.
