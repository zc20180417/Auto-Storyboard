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
Run up to 3 workers in parallel.
Worker batches are generated dynamically from episode complexity.
Simple batch threshold: <= 2500 script chars and <= 1 segment.
Batch size limit: 2 episodes per worker.
When one worker handles two episodes, it must complete the first episode's generation, real review, hard-issue repair, re-review, and validation before starting the second.

Dynamic worker batches:

- batch 1: `ep01`, `ep01` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep01\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep01\agent_prompt.md`
- batch 2: `ep01`, `ep01` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep01\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep01\agent_prompt.md`
- batch 3: `ep02`, `ep02` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep02\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep02\agent_prompt.md`
- batch 4: `ep02`, `ep03` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep02\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep03\agent_prompt.md`
- batch 5: `ep03`, `ep03` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep03\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep03\agent_prompt.md`
- batch 6: `ep04`, `ep04` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep04\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep04\agent_prompt.md`
- batch 7: `ep05`, `ep05` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep05\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep05\agent_prompt.md`
- batch 8: `ep05`, `ep06` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep05\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep06\agent_prompt.md`
- batch 9: `ep06`, `ep06` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep06\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep06\agent_prompt.md`
- batch 10: `ep07`, `ep07` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep07\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep07\agent_prompt.md`
- batch 11: `ep07`, `ep08` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep07\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep08\agent_prompt.md`
- batch 12: `ep08`, `ep08` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep08\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep08\agent_prompt.md`
- batch 13: `ep09`, `ep09` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep09\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep09\agent_prompt.md`
- batch 14: `ep09`, `ep10` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep09\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep10\agent_prompt.md`
- batch 15: `ep10`, `ep10` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep10\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep10\agent_prompt.md`
- batch 16: `ep11`, `ep11` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep11\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep11\agent_prompt.md`
- batch 17: `ep11`, `ep12` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep11\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep12\agent_prompt.md`
- batch 18: `ep12`, `ep12` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep12\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep12\agent_prompt.md`
- batch 19: `ep13`, `ep13` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep13\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep13\agent_prompt.md`
- batch 20: `ep13`, `ep13` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep13\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep13\agent_prompt.md`
- batch 21: `ep14`, `ep14` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep14\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep14\agent_prompt.md`
- batch 22: `ep14`, `ep14` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep14\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep14\agent_prompt.md`
- batch 23: `ep15`, `ep15` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep15\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep15\agent_prompt.md`
- batch 24: `ep15`, `ep15` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep15\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep15\agent_prompt.md`
- batch 25: `ep16`, `ep16` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep16\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep16\agent_prompt.md`
- batch 26: `ep16`, `ep16` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep16\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep16\agent_prompt.md`
- batch 27: `ep17`, `ep17` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep17\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep17\agent_prompt.md`
- batch 28: `ep17`, `ep17` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep17\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep17\agent_prompt.md`
- batch 29: `ep18`, `ep18` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep18\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep18\agent_prompt.md`
- batch 30: `ep18`, `ep18` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep18\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep18\agent_prompt.md`
- batch 31: `ep19`, `ep19` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep19\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep19\agent_prompt.md`
- batch 32: `ep19`, `ep19` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep19\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep19\agent_prompt.md`
- batch 33: `ep20`, `ep20` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep20\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep20\agent_prompt.md`
- batch 34: `ep20`, `ep20` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep20\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep20\agent_prompt.md`
- batch 35: `ep21`, `ep21` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep21\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep21\agent_prompt.md`
- batch 36: `ep21`, `ep21` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep21\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep21\agent_prompt.md`
- batch 37: `ep22`, `ep22` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep22\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep22\agent_prompt.md`
- batch 38: `ep22`, `ep22` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep22\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep22\agent_prompt.md`
- batch 39: `ep23`, `ep23` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep23\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep23\agent_prompt.md`
- batch 40: `ep23`, `ep23` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep23\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep23\agent_prompt.md`
- batch 41: `ep24`, `ep24` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep24\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep24\agent_prompt.md`
- batch 42: `ep24`, `ep24` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep24\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep24\agent_prompt.md`
- batch 43: `ep25`, `ep25` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep25\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep25\agent_prompt.md`
- batch 44: `ep25`, `ep25` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep25\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep25\agent_prompt.md`
- batch 45: `ep26`, `ep26` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep26\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep26\agent_prompt.md`
- batch 46: `ep26`, `ep26` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep26\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep26\agent_prompt.md`
- batch 47: `ep27`, `ep27` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep27\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep27\agent_prompt.md`
- batch 48: `ep27`, `ep27` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep27\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep27\agent_prompt.md`
- batch 49: `ep28`, `ep28` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep28\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep28\agent_prompt.md`
- batch 50: `ep28`, `ep28` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep28\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep28\agent_prompt.md`
- batch 51: `ep29`, `ep29` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep29\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep29\agent_prompt.md`
- batch 52: `ep29`, `ep29` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep29\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep29\agent_prompt.md`
- batch 53: `ep30`, `ep30` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep30\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep30\agent_prompt.md`
- batch 54: `ep30`, `ep30` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep30\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep30\agent_prompt.md`

Initial worker wave:

- worker 1: `ep01`, `ep01` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep01\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep01\agent_prompt.md`
- worker 2: `ep01`, `ep01` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep01\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep01\agent_prompt.md`
- worker 3: `ep02`, `ep02` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep02\agent_prompt.md`, `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep02\agent_prompt.md`

All episode prompts:

- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep01\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep01\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep01\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep01\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep02\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep02\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep02\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep03\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep03\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep03\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep04\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep04\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep05\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep05\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep05\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep06\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep06\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep06\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep07\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep07\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep07\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep08\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep08\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep08\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep09\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep09\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep09\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep10\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep10\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep10\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep11\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep11\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep11\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep12\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep12\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep12\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep13\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep13\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep13\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep13\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep14\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep14\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep14\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep14\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep15\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep15\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep15\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep15\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep16\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep16\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep16\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep16\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep17\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep17\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep17\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep17\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep18\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep18\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep18\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep18\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep19\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep19\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep19\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep19\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep20\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep20\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep20\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep20\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep21\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep21\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep21\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep21\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep22\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep22\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep22\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep22\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep23\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep23\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep23\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep23\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep24\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep24\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep24\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep24\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep25\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep25\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep25\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep25\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep26\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep26\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep26\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep26\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep27\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep27\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep27\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep27\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep28\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep28\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep28\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep28\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep29\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep29\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep29\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep29\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep30\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep30\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep30\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-claude\episodes\ep30\agent_prompt.md`

## After Workers Finish

After workers finish writing `final.txt`, `review.txt`, and `status.json` in each episode directory, run:

```powershell
.\COLLECT_RESULTS.ps1
```

If any episode is unfinished or validation fails, dispatch only that episode's `agent_prompt.md` to a worker for focused repair.
