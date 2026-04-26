# Qwen CLI 入口

先读 `AGENTS.md`。生产主流程写在 `README_AGENT_WORKFLOW.md`。

使用 `agent_runs/<run-name>/episodes/epXX/agent_prompt.md` 作为每集任务提示词。完成后把结果写回对应 episode 目录，并执行任务文件中的校验命令。
