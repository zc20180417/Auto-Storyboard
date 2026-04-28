# Task: EP-15

Mode: `scene`

## Required Inputs
- Run context: `../../context.md`
- Generation skill: `G:\Auto-Storyboard\agent_skills\storyboard-generator\SKILL.md`
- Review skill: `G:\Auto-Storyboard\agent_skills\storyboard-reviewer\SKILL.md`
- Full episode script: `script.txt`
- Segment scripts: `segments/seg*/script.txt`

## Required Outputs
- `segments/segXX/draft.txt`
- `segments/segXX/review.md`
- `segments/segXX/final.txt`
- `final.txt`
- `review.txt`
- `status.json`

## Workflow
1. Read `../../context.md`, both standard `SKILL.md` files, `script.txt`, and each segment script.
2. For each segment, generate `segments/segXX/draft.txt`, review it, and write `segments/segXX/review.md` plus `segments/segXX/final.txt`.
3. Assemble all segment finals into this episode's `final.txt`. Renumber natural group headings and shot numbers globally from 第1组 / 1-1.
4. Run clean-format validation.
5. If validation reports clean-format issues, fix `final.txt` and rerun validation.
6. Write `review.txt` and `status.json`.

Validation command:

```powershell
python "G:\Auto-Storyboard\storyboard_agent_workspace.py" validate-episode --episode-dir "G:\Auto-Storyboard\agent_runs\chonghui1992-lengku-scene\episodes\ep15"
```

`status.json` shape:

```json
{
  "episode_id": "ep15",
  "status": "done",
  "output_name": "EP-15-ep15-agent-cli-storyboard.txt",
  "summary": "short Chinese summary",
  "hard_issues_remaining": [],
  "warnings": []
}
```

Use `status: "needs_review"` only if hard issues remain after two focused repair attempts.

## Important Constraints
- Rules live in the two `SKILL.md` files. Do not duplicate or reinterpret them here.
- Work only inside `episodes\ep15`. Treat project-level skill files and `../../context.md` as read-only.
- Do not call external LLM APIs or launch other CLIs.
