# Task: 苍南风云-第19集

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
5. Re-run `storyboard-reviewer` after repairs and update `review.txt`.
6. Write `status.json` with reviewer metadata, then run validation.
7. If validation reports clean-format or reviewer-evidence issues, fix the affected files and rerun validation.

Validation command:

```powershell
python "G:\Auto-Storyboard\storyboard_agent_workspace.py" validate-episode --episode-dir "G:\Auto-Storyboard\agent_runs\cangnan-single\episodes\ep19"
```

`status.json` shape:

```json
{
  "episode_id": "ep19",
  "status": "done",
  "output_name": "苍南风云-ep19-agent-cli-storyboard.txt",
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
- Work only inside `episodes\ep19`. Treat project-level skill files and `../../context.md` as read-only.
- Do not call external LLM APIs or launch other CLIs.
