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
3. Assemble all segment finals into this episode's `final.txt`. Renumber natural group headings globally from 第1组; each group keeps its own time ranges from 0 seconds.
4. Review the assembled `final.txt` once using `storyboard-reviewer`; write the raw reviewer JSON to `review.txt`.
5. If hard issues exist, repair only the failed local groups in `final.txt`; do not rewrite unrelated groups. Re-run `storyboard-reviewer` after repairs.
6. Write `status.json` with reviewer metadata, then run validation.
7. If validation reports clean-format or reviewer-evidence issues, fix the affected files and rerun validation.

Validation command:

```powershell
python "G:\Auto-Storyboard\storyboard_agent_workspace.py" validate-episode --episode-dir "G:\Auto-Storyboard\agent_runs\manjidiwang\episodes\ep15"
```

`status.json` requirements:

- `episode_id`: `ep15`
- `status`: `done` only after the real `review.txt` passes with no hard issues; otherwise `needs_review`
- `output_name`: `EP-15-ep15-agent-cli-storyboard.txt`
- `summary`: short Chinese summary
- `hard_issues_remaining`: copy unresolved hard issues from the real reviewer result
- `warnings`: copy or summarize warnings from the real reviewer result
- `reviewer_source`: must be `storyboard-reviewer`
- `reviewer_pass`: copy the boolean `pass` from `review.txt` after `review.txt` exists
- `reviewer_issues_count`: copy `len(review.txt.issues)` after `review.txt` exists
- `reviewer_warnings_count`: copy `len(review.txt.warnings)` after `review.txt` exists

Do not prefill `reviewer_pass=true` or issue/warning counts before writing the real `review.txt`.

Use `status: "needs_review"` only if hard issues remain after two focused repair attempts.
`review.txt` and `segments/segXX/review.md` must contain real raw JSON returned by `storyboard-reviewer`; clean-format validation is not a substitute for reviewer审稿 and placeholder review JSON will fail validation.
Reviewer JSON must include non-empty `checked_groups` and full `audit_coverage` fields as required by `storyboard-reviewer/SKILL.md`.
Reviewer JSON must also include at least 3 `spot_checks` items with `group`, `type`, and `evidence`.
Reviewer JSON must include at least 3 `semantic_checks` items with `group`, `type`, `result`, `evidence`, and `fix_instruction`; this is the reviewer semantic audit record, not a substitute for fixing hard issues.
`status.json` reviewer fields must stay consistent with `review.txt`.

## Important Constraints
- Rules live in the two `SKILL.md` files. Do not duplicate or reinterpret them here.
- Work only inside `episodes\ep15`. Treat project-level skill files and `../../context.md` as read-only.
- Do not call external LLM APIs or launch other CLIs.
