# Claude Code 入口

先读 `AGENTS.md`。生产主流程写在 `README_AGENT_WORKFLOW.md`。

重要规则：不要让 Python 调用 Claude Code、Codex CLI、Qwen CLI、Kimi Code 或其他模型 CLI。请直接在 `prepare-agent.ps1` 创建的文件工作区里完成生成、审核和修复。
