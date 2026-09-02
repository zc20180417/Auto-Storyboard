# Workflow Readiness Contract

## Single source of readiness truth

`seedance_material_handoff.summarize_workflow_readiness()` is the local readiness reducer. `workflow_readiness.json` and `workflow_readiness.md` are two renderings of the same returned object; the Markdown report must not override machine state.

Readiness is ordered. A later layer cannot pass if an earlier dependency is blocked.

| Layer | Required evidence | Representative blockers |
|---|---|---|
| `storyboard_valid` | current `final.txt` and index hash; real configured reviewer `pass=true`; `status.json` is done with zero hard issues | missing/invalid review or status, wrong reviewer, stale index |
| `asset_contract_valid` | asset reviewer status passed; current `asset_validation.json` produced by the current validator over current inputs | missing validator evidence, failed validator, stale producer/source hash |
| `handoff_schema_valid` | profile/identity/schema/project/episode/duration/provider mapping and source hashes are locally consistent | missing/invalid JSON, identity mismatch, stale requirements, non-integer/out-of-range duration |
| `generation_ready` | all previous layers plus at least one actually serialized Active reference per cut | missing/invalid local material, no Active Ark result, hash/MIME mismatch, limits exceeded, empty reference content |
| `submit_allowed` | generation ready plus authorization, reference-only policy, current authenticated ManJuWeb consumer/preflight evidence, no policy blockers | unconfirmed authorization, missing consumer fixture, unauthenticated/stale/replayed/mismatched external evidence |

## Deterministic missing/error behavior

- Missing or invalid required evidence always yields `valid=false` with a blocker; it is never treated as an empty success.
- An empty reviewer/issues structure is not sufficient unless the configured real reviewer/status contract also passes.
- `handoff_schema_valid` can pass before Ark materials exist. This is intentional and does not imply generation readiness.
- Active Ark declarations count only when local file SHA-256, sync SHA-256, Ark ID/status and provider serialization all agree.
- `generation_ready=true, submit_allowed=false` is valid when technical reference serialization succeeds but authorization or external consumer/preflight policy remains blocked.
- Validator exceptions or unreadable files are exposed as blockers rather than folded into a generic false.
- Any bound source or producer hash change makes the dependent evidence stale.

## Machine schema

```json
{
  "schema_version": 1,
  "profile": "seedance-2.5-horizontal-xianxia-3d-cg",
  "layers": {
    "storyboard_valid": {
      "valid": false,
      "state": "blocked",
      "blockers": ["missing storyboard status.json"],
      "evidence": {}
    }
  },
  "first_blocker": {
    "layer": "storyboard_valid",
    "reason": "missing storyboard status.json"
  },
  "workflow_validated": false,
  "validation_scope": "contract-prototype-only"
}
```

All five layer keys are always present. `first_blocker` is the first blocked layer in dependency order. It is `null` only when all local layers pass.

`workflow_validated` remains false during Units 6–7. It can become true only under Unit 8's three promoted, accepted, current probe attempts and cross-probe signoff; local schema or one generated package cannot set it.

## Asset validator evidence

`validate-assets.mjs` writes `asset_validation.json` on both pass and fail. It records its own byte hash, hashes of current required inputs, a boolean `valid`, and concrete issues. This file is deterministic mechanical evidence; it does not replace the real asset reviewer.

The readiness reducer verifies the validator hash and selected source hashes again. Editing `asset_validation.json` without rerunning the validator cannot create durable readiness because the bound hashes and semantic reviewer status must also agree.

## Human report

`workflow_readiness.md` prints:

1. resolved profile and validation scope;
2. all five layer states and blockers;
3. the first blocker.

Unit 7 已冻结 probe latest/promoted attempt、QA/signoff 和 cross-probe 汇总合同；真实 attempt 只能在 Unit 8 由 ManJuWeb/CPA 外部证据产生。在三类有效 promoted attempts 与跨探针签收齐备前，最高如实声明仍是“合同原型完成，视频工作流未验证”。
