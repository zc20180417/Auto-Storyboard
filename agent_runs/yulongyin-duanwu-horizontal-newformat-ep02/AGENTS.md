# Storyboard Agent Run Instructions

This directory is an agent-native workspace. Each `episodes/epXX` folder is an independent task.

## Dispatcher Hard Stop

If this run contains 2 or more episodes, the host/main agent is a dispatcher only.

Dispatcher must:
- Create subagents/workers and dispatch `episodes/epXX/agent_prompt.md`.
- Run up to the configured worker limit in parallel.
- Stop with `NEED_USER_DISPATCH` and list prompt paths if worker creation is unavailable or requires user authorization.

Dispatcher must not:
- Directly generate storyboard body text.
- Sequentially process multiple episodes in the main thread.
- Open `episodes/ep*/script.txt` and begin production work.
- Write `episodes/ep*/draft.txt`, `final.txt`, `review.txt`, or `status.json`.
- Downgrade to main-thread sequential production when subagents/workers are unavailable.

Agents must:
- Read the task files instead of relying on hidden state.
- Write durable outputs to files.
- Run validation before marking a task done.
- Preserve drafts and review notes even when the final status is `needs_review`.
