# Task: 测试剧本第28集

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
3. Assemble all segment finals into this episode's `final.txt`. Renumber natural group headings globally from 第1组; each group keeps its own time ranges from 0 seconds.
4. Review the assembled `final.txt` once using `storyboard-reviewer`; write the raw reviewer JSON to `review.txt`.
5. If hard issues exist, repair only the failed local groups in `final.txt`; do not rewrite unrelated groups. Re-run `storyboard-reviewer` after repairs.
6. Write `status.json` with reviewer metadata, then run validation.
7. If validation reports clean-format or reviewer-evidence issues, fix the affected files and rerun validation.

Validation command:

```powershell
python "G:\Auto-Storyboard\storyboard_agent_workspace.py" validate-episode --episode-dir "G:\Auto-Storyboard\agent_runs\ceshijuben\episodes\ep28"
```

`status.json` shape:

```json
{
  "episode_id": "ep28",
  "status": "done",
  "output_name": "测试剧本-ep28-agent-cli-storyboard.txt",
  "summary": "short Chinese summary",
  "hard_issues_remaining": [],
  "warnings": [],
  "reviewer_source": "storyboard-reviewer",
  "reviewer_pass": true,
  "reviewer_issues_count": 0,
  "reviewer_warnings_count": 0
}
```

Use `status: "needs_review"` only if hard issues remain after two focused repair attempts.
`review.txt` and `segments/segXX/review.md` must contain real raw JSON returned by `storyboard-reviewer`; clean-format validation is not a substitute for reviewer审稿 and placeholder review JSON will fail validation.

## Important Constraints
- Rules live in the two `SKILL.md` files. Do not duplicate or reinterpret them here.
- Work only inside `episodes\ep28`. Treat project-level skill files and `../../context.md` as read-only.
- Do not call external LLM APIs or launch other CLIs.
