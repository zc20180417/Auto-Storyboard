# Resolved Workflow Identity Contract

## Purpose

`resolved workflow identity` records the exact local storyboard rules used by the strict Seedance 2.5 horizontal xianxia workflow and carries that identity into the asset stage. It makes stale or mixed-profile artifacts detectable before material handoff.

This contract is evidence for two upstream layers only:

- `storyboard_valid`: the episode passed its configured real reviewer and episode gates, and its index is bound to the current `final.txt` and workflow identity.
- `asset_contract_valid`: the asset reviewer passed, the asset tables/bindings are mechanically valid, and asset evidence is current.

It does not establish `handoff_schema_valid`, `generation_ready`, `submit_allowed`, provider transport support, material authorization, Ark Active state, or successful media generation. Those states belong to later contracts.

## Index schema compatibility

Legacy indexes remain unchanged:

```json
{
  "project": "...",
  "episode_id": "EP01",
  "source_hashes": {"final_txt_sha256": "..."},
  "cuts": []
}
```

The `seedance-2.5-horizontal-xianxia-3d-cg` profile emits index schema v2:

```json
{
  "schema_version": 2,
  "workflow_identity": {
    "identity_schema_version": 1,
    "video_profile": "seedance-2.5-horizontal-xianxia-3d-cg",
    "video_profile_contract_version": 1,
    "provider_contract_version": 1,
    "provider_task_mapping": {
      "field": "omni_reference_task_type",
      "value": "reference"
    },
    "storyboard_aspect": "horizontal",
    "visual_style": "3d-cg",
    "visual_style_preset": "realistic-material-restrained-anime-outline",
    "visual_style_preset_version": 1,
    "visual_style_preset_sha256": "...",
    "project_pack_id": "dandao-xiantu",
    "project_pack_version": 1,
    "project_pack_sha256": "...",
    "generator_skill_name": "seedance-2-5-horizontal-xianxia-3d-cg-generator",
    "reviewer_skill_name": "seedance-2-5-horizontal-xianxia-3d-cg-reviewer",
    "workflow_audit": {
      "schema_version": 1,
      "files": [
        {"role": "profile_skill", "path": "agent_skills/.../SKILL.md", "sha256": "..."}
      ]
    },
    "resolved_workflow_hash": "..."
  },
  "source_hashes": {"final_txt_sha256": "..."},
  "cuts": []
}
```

Consumers must continue accepting the legacy object when `schema_version` and `workflow_identity` are absent. A v2 index is fail-closed: missing identity, a wrong identity hash, an absolute/audited parent path, a missing audited file, or a changed audited file is stale evidence.

## Actual loaded-file manifest

The v2 resolver enumerates only the maintained surfaces that this workflow actually loads. It is deliberately not a general plugin dependency graph.

The generic profile contributes:

- profile `SKILL.md`;
- model contract;
- named visual-preset reference;
- xianxia VFX grammar;
- native-audio contract;
- dedicated generator;
- dedicated reviewer;
- shared 3D CG visual-style skill.

When a project pack is enabled, it additionally contributes:

- project-pack registry;
- selected `pack.json`;
- selected pack `SKILL.md`;
- every reference declared by the selected pack.

Paths are stored relative to `project_root` with `/` separators. Temporary workspace locations therefore do not change a hash when the loaded contents and resolved identity are the same. Unloaded or provisional files are intentionally absent and do not invalidate evidence.

## Hash algorithm

Every listed file uses SHA-256 over its exact bytes. `resolved_workflow_hash` is SHA-256 over UTF-8 JSON of the complete `workflow_identity` before the hash field is added, with recursively sorted object keys, no insignificant whitespace, and Unicode characters kept as UTF-8.

Consequences:

- modifying any listed file changes `resolved_workflow_hash`;
- modifying an unlisted file does not;
- changing profile, provider contract, preset, pack, generator, or reviewer identity changes the hash;
- changing only `final.txt` changes `source_hashes.final_txt_sha256`, not workflow identity;
- re-exporting an index after either type of change invalidates asset evidence through the index SHA-256.

## Asset propagation

For a v2 index, `assets-md-to-xlsx.mjs --mode=episode` copies the complete `workflow_identity` into both `asset_bindings.json` and an existing `asset_status.json`. It also writes identical `asset_evidence` objects to both files:

```json
{
  "asset_evidence_schema_version": 1,
  "asset_contract_version": 2,
  "source_hashes": {
    "final_txt_sha256": "...",
    "storyboard_index_sha256": "...",
    "assets_md_sha256": "...",
    "asset_bible_sha256": "optional when the run bible exists"
  },
  "producer_files": [
    {"role": "asset_extractor_skill", "path": "agent_skills/asset-extractor/SKILL.md", "sha256": "..."},
    {"role": "asset_reviewer_skill", "path": "agent_skills/asset-reviewer/SKILL.md", "sha256": "..."},
    {"role": "asset_converter", "path": "agent_skills/asset-extractor/scripts/assets-md-to-xlsx.mjs", "sha256": "..."},
    {"role": "asset_validator", "path": "agent_skills/asset-extractor/scripts/validate-assets.mjs", "sha256": "..."}
  ],
  "asset_evidence_hash": "..."
}
```

`asset_evidence_hash` uses the same canonical JSON rule over the evidence object before that hash field is added.

Workers write semantic asset tables and reviewer status; they do not invent evidence hashes. The deterministic converter refreshes identity/evidence after the real asset review, then `validate-assets.mjs` checks:

- index `final_txt_sha256` equals current `final.txt`;
- index identity hash and audited files are current;
- `episode.json` identity fields equal index identity;
- bindings/status carry an exact copy of index identity;
- bindings/status carry identical asset evidence;
- final/index/assets and optional bible hashes are current;
- all four asset producer paths and hashes are current;
- the existing cut, asset table, reviewer, workbook, and handoff ownership gates still pass.

For a legacy index, these new fields are not required and the converter does not fabricate them.

## Project fact-source boundary

When `dandao-xiantu` is enabled, `yuanding-visual-bible.md` remains the authority for Yuanding geometry, material partitions, scale, markings, and allowed states. A run-level `asset_bible.md` may register stable Yuanding asset/state IDs and must cite the project-pack version/hash plus the audited Yuanding reference path/hash. It must not restate or independently modify those facts.

This boundary lets storyboard, assets, and later probes share one authority. The asset reviewer treats a duplicated or conflicting definition as a semantic hard issue; the mechanical validator checks the referenced workflow and asset-bible byte hashes, not artistic correctness.

## Staleness and recovery

| Change | Stale artifact | Recovery |
|---|---|---|
| `final.txt` changes | index and all asset evidence | rerun real storyboard review/episode validation, then regenerate/review/convert assets as required |
| loaded workflow file changes | index identity and all downstream asset evidence | revalidate workflow decisions, rerun affected reviewer work, export a new index, then refresh assets |
| index changes | bindings/status asset evidence | rerun converter and asset validator; rerun semantic review if the change affects meaning |
| `assets.md` changes | workbook, bindings/status asset evidence, prior asset review if semantic | rerun asset reviewer when semantic, then converter and validator |
| `asset_bible.md` changes | asset evidence and potentially semantic review | recheck bible consistency, then converter and validator |
| asset producer rule/script changes | bindings/status asset evidence | rerun the affected real reviewer/conversion/validation stages |

No stale artifact is repaired by editing a hash field. The producing stage must be rerun so its evidence reflects the current inputs.
