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

- batch 1: `ep01` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep01\agent_prompt.md`
- batch 2: `ep02` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep02\agent_prompt.md`
- batch 3: `ep03` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep03\agent_prompt.md`
- batch 4: `ep04` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep04\agent_prompt.md`
- batch 5: `ep05` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep05\agent_prompt.md`
- batch 6: `ep06` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep06\agent_prompt.md`
- batch 7: `ep07` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep07\agent_prompt.md`
- batch 8: `ep08` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep08\agent_prompt.md`
- batch 9: `ep09` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep09\agent_prompt.md`
- batch 10: `ep10` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep10\agent_prompt.md`
- batch 11: `ep11` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep11\agent_prompt.md`
- batch 12: `ep12` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep12\agent_prompt.md`
- batch 13: `ep13` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep13\agent_prompt.md`
- batch 14: `ep14` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep14\agent_prompt.md`
- batch 15: `ep15` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep15\agent_prompt.md`
- batch 16: `ep16` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep16\agent_prompt.md`
- batch 17: `ep17` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep17\agent_prompt.md`
- batch 18: `ep18` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep18\agent_prompt.md`
- batch 19: `ep19` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep19\agent_prompt.md`
- batch 20: `ep20` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep20\agent_prompt.md`
- batch 21: `ep21` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep21\agent_prompt.md`
- batch 22: `ep22` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep22\agent_prompt.md`
- batch 23: `ep23` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep23\agent_prompt.md`
- batch 24: `ep24` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep24\agent_prompt.md`
- batch 25: `ep25` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep25\agent_prompt.md`
- batch 26: `ep26` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep26\agent_prompt.md`
- batch 27: `ep27` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep27\agent_prompt.md`
- batch 28: `ep28` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep28\agent_prompt.md`
- batch 29: `ep29` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep29\agent_prompt.md`
- batch 30: `ep30` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep30\agent_prompt.md`

Initial worker wave:

- worker 1: `ep01` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep01\agent_prompt.md`
- worker 2: `ep02` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep02\agent_prompt.md`
- worker 3: `ep03` -> `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep03\agent_prompt.md`

When any worker finishes, dispatch the next unfinished worker batch from the dynamic plan.

## Episode Tasks

- `ep01`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep01\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep01`.
- `ep02`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep02\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep02`.
- `ep03`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep03\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep03`.
- `ep04`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep04\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep04`.
- `ep05`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep05\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep05`.
- `ep06`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep06\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep06`.
- `ep07`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep07\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep07`.
- `ep08`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep08\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep08`.
- `ep09`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep09\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep09`.
- `ep10`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep10\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep10`.
- `ep11`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep11\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep11`.
- `ep12`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep12\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep12`.
- `ep13`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep13\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep13`.
- `ep14`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep14\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep14`.
- `ep15`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep15\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep15`.
- `ep16`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep16\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep16`.
- `ep17`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep17\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep17`.
- `ep18`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep18\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep18`.
- `ep19`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep19\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep19`.
- `ep20`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep20\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep20`.
- `ep21`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep21\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep21`.
- `ep22`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep22\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep22`.
- `ep23`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep23\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep23`.
- `ep24`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep24\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep24`.
- `ep25`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep25\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep25`.
- `ep26`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep26\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep26`.
- `ep27`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep27\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep27`.
- `ep28`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep28\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep28`.
- `ep29`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep29\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep29`.
- `ep30`: dispatch `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep30\agent_prompt.md` to one worker. Worker writes only under `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep30`.

## Pending Prompt List

- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep01\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep02\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep03\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep04\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep05\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep06\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep07\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep08\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep09\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep10\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep11\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep12\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep13\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep14\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep15\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep16\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep17\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep18\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep19\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep20\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep21\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep22\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep23\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep24\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep25\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep26\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep27\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep28\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep29\agent_prompt.md`
- `H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep30\agent_prompt.md`

## Manual CLI Example

If a human explicitly chooses to run a CLI, run it manually from PowerShell instead of through Python:

Codex example:

```powershell
codex exec --skip-git-repo-check --sandbox workspace-write --cd "H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25" - < "H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep01\agent_prompt.md"
```

Qwen example:

```powershell
qwen < "H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\shuangxue-qinglan-mimo-v25\episodes\ep01\agent_prompt.md"
```

## Collect Results

After agents finish writing `final.txt` and `status.json` in each episode directory:

```powershell
.\COLLECT_RESULTS.ps1
```
