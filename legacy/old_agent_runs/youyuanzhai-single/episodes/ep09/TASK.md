# Task: 有缘斋第09集

Mode: `single`

## Required Inputs
- Run context: `../../context.md`
- Generation skill: `G:\Auto-Storyboard\agent_skills\storyboard-generator\SKILL.md`
- Review skill: `G:\Auto-Storyboard\agent_skills\storyboard-reviewer\SKILL.md`
- Full episode script: `script.txt`
- Segment scripts: not used in `single` mode.

## Required Outputs
- `final.txt`
- `review.txt`
- `status.json`

## Workflow
1. Read `../../context.md`, both standard `SKILL.md` files, and `script.txt`.
2. Generate the full episode directly into `final.txt`.
3. Review the full episode once using the review skill; write `review.txt`.
4. If hard issues exist, repair only the failed local groups in `final.txt`; do not rewrite unrelated groups.
5. Run clean-format validation.
6. If validation reports clean-format issues, fix `final.txt` and rerun validation.
7. Write `status.json`.

Validation command:

```powershell
python "G:\Auto-Storyboard\storyboard_agent_workspace.py" validate-episode --episode-dir "G:\Auto-Storyboard\agent_runs\youyuanzhai-single\episodes\ep09"
```

`status.json` shape:

```json
{
  "episode_id": "ep09",
  "status": "done",
  "output_name": "有缘斋-ep09-agent-cli-storyboard.txt",
  "summary": "short Chinese summary",
  "hard_issues_remaining": [],
  "warnings": []
}
```

Use `status: "needs_review"` only if hard issues remain after two focused repair attempts.

## Important Constraints
- Rules live in the two `SKILL.md` files. Do not duplicate or reinterpret them here.
- Work only inside `episodes\ep09`. Treat project-level skill files and `../../context.md` as read-only.
- Do not call external LLM APIs or launch other CLIs.
