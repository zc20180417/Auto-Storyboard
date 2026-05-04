# Auto-Storyboard Project Instructions

## Project Overview
Auto-Storyboard is a toolkit designed to automate the conversion of short drama scripts into vertical video storyboards. The project relies on an "Agent Workflow" where AI agents (like Codex, Claude Code, Qwen Code) perform the complex tasks of generating, reviewing, and fixing storyboards, while Python and PowerShell scripts are strictly used for orchestrating file workspaces, validating objective formats, and collecting results.

## Architecture and Workflow
The core workflow separates file management from AI generation to ensure stability and reproducibility:
1.  **Prepare Inputs:** Scripts are split into individual episodes (e.g., located in `split_scripts/`) using dedicated PowerShell scripts (e.g., `split-youyuanzhai6.ps1`).
2.  **Create Agent Workspace:** Use `prepare-agent.ps1` to scaffold the working directory in `agent_runs/<run-name>`.
3.  **Agent Execution:** Agents are dispatched (manually or via subagents) using the prompts provided in the generated `NEXT_STEPS.md`. Agents read context, generate drafts, review themselves using specific skills (e.g., `storyboard-reviewer`), and produce final text.
4.  **Validation:** Python scripts (`storyboard_agent_workspace.py`) strictly validate the objective format, ensuring no JSON or debug markers remain and that quality floors are met.
5.  **Result Collection:** `collect-agent.ps1` gathers the validated outputs into a final directory (`outputs_agent_*`).

## Key Commands

**1. Create Agent Workspace (Default Scene Mode):**
```powershell
.\prepare-agent.ps1 scene <run-name> -Source .\split_scripts\<episode-folder> -OutDir .\outputs_agent_<name> -Force
```

**2. Validate Episode Format:**
```powershell
python .\storyboard_agent_workspace.py validate-episode --episode-dir .\agent_runs\<run-name>\episodes\<ep-name>
```

**3. Collect Final Results:**
```powershell
.\collect-agent.ps1 .\agent_runs\<run-name>
```

## Development Conventions & Rules

*   **No Direct Model Calls from Python:** Python and PowerShell scripts **MUST NOT** directly invoke AI CLIs (Codex, Claude, Qwen) or APIs. Their role is purely for file system operations, workspace preparation, and objective validation.
*   **Output Format:** The final storyboard output must be clean, natural text. **Absolutely no JSON, debug tags, or machine markers** should be present in the final output files.
*   **Processing Modes:** 
    *   Default to `scene` mode (which breaks episodes down by scene) for stability, especially for dense or long episodes.
    *   Only use `single` mode for very short episodes with simple, highly stable formats.
*   **Concurrency Unit:** The unit of work is a single episode. It is recommended to process episodes concurrently using 3-5 workers. Do not bundle multiple episodes into a single task for an agent unless explicitly requested.
*   **Validation is Mandatory:** Every generated storyboard must pass `validate-episode`. This ensures structural integrity and prevents template-like generic descriptions (e.g., "spatial layout is established").
*   **Asset Extraction:** When extracting assets (characters, scenes, props) for image generation, always use the `asset-extractor` skill and maintain a global `asset_bible.md` to ensure consistency across all episodes.
