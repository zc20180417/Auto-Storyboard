# Storyboard Agent Run Instructions

This directory is an agent-native workspace. Each `episodes/epXX` folder is an independent task.

Agents must:
- Read the task files instead of relying on hidden state.
- Write durable outputs to files.
- Run validation before marking a task done.
- Preserve drafts and review notes even when the final status is `needs_review`.
