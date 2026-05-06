import fs from "node:fs/promises";
import path from "node:path";

const [episodeDirArg, ...optionArgs] = process.argv.slice(2);
const options = Object.fromEntries(
  optionArgs
    .filter((arg) => arg.startsWith("--"))
    .map((arg) => {
      const [key, ...rest] = arg.slice(2).split("=");
      return [key, rest.join("=") || "true"];
    }),
);

if (!episodeDirArg) {
  console.error("Usage: node validate-assets.mjs <episode-dir> [--storyboard-index=<storyboard_index.json>]");
  process.exit(2);
}

const episodeDir = path.resolve(episodeDirArg);
const requiredFiles = {
  assets: path.join(episodeDir, "assets.md"),
  workbook: path.join(episodeDir, "assets.xlsx"),
  bindings: path.join(episodeDir, "asset_bindings.json"),
  review: path.join(episodeDir, "asset_review.json"),
  status: path.join(episodeDir, "asset_status.json"),
};

const REQUIRED_TABLES = [
  "本集复用资产索引",
  "本集新增资产状态",
  "本集新增基础资产",
  "本集关键道具与场景状态",
  "本集不建议入库元素",
  "本集分镜资产绑定索引",
];
const REQUIRED_SHEETS = [
  "复用资产索引",
  "新增资产状态",
  "新增基础资产",
  "关键道具与场景状态",
  "不建议入库元素",
  "分镜资产绑定索引",
];

const REQUIRED_AUDIT_COVERAGE = [
  "asset_coverage",
  "asset_selection",
  "bible_consistency",
  "registry_structure",
  "duplicate_control",
  "state_modeling",
  "category_boundary",
  "prompt_fidelity",
  "bilingual_consistency",
  "time_range_accuracy",
  "cut_binding_accuracy",
  "binding_completeness",
  "video_reference_readiness",
  "xlsx_readiness",
];

const SEMANTIC_COVERAGE_GROUPS = {
  duplicate_control: ["duplicate_base_asset", "unnecessary_regeneration"],
  state_modeling: ["state_should_be_variant", "variant_over_split", "variant_under_split"],
  bible_consistency: ["bible_conflict", "identity_drift", "costume_state_conflict", "scene_state_conflict", "prop_state_conflict"],
  prompt_fidelity: ["prompt_hallucination", "prop_text_violation", "empty_scene_contamination", "bilingual_mismatch"],
  time_or_xlsx: ["time_range_error", "xlsx_readiness"],
  cut_binding: ["cut_id_missing", "cut_id_not_found", "episode_usage_cut_id_mismatch"],
  binding_readiness: ["missing_primary_scene_binding", "missing_key_character_binding", "missing_key_prop_binding", "unnecessary_video_reference"],
};

const ENUMS = {
  source: ["asset_bible", "episode_new", "episode_variant"],
  asset_type: ["character", "costume", "scene", "prop", "composition"],
  status_type: [
    "base",
    "costume_change",
    "dirt_damage",
    "lighting_time",
    "injury",
    "scene_condition",
    "prop_condition",
    "composition_reference",
    "other",
  ],
  reuse_policy: ["global", "episode_range", "one_episode", "shot_only"],
  needs_generation: ["yes", "no", "conditional"],
  sync_to_bible: ["yes", "no", "candidate"],
  binding_role: ["scene_reference", "character_reference", "costume_reference", "prop_reference", "composition_reference"],
  reference_priority: ["primary", "supporting", "background"],
  use_for_video: ["yes", "no", "conditional"],
  required_for_generation: ["yes", "no", "conditional"],
  binding_source: ["asset_table", "asset_bible", "manual_candidate"],
  semantic_result: ["pass", "warning", "issue"],
};

const REQUIRED_COLUMNS = {
  "复用资产索引": ["使用ID", "episode_id", "cut_ids", "asset_id", "state_id", "asset_type", "source", "episode_usage", "本集用途", "needs_generation", "generation_note"],
  "新增资产状态": ["state_id", "episode_id", "cut_ids", "asset_id", "parent_state_id", "asset_type", "status_type", "state_summary", "changed_fields", "reuse_policy", "first_seen_episode", "episode_usage", "needs_generation", "generation_note", "sync_to_bible", "静态生图提示词(中文)", "负面提示词(中文)", "静态生图提示词(英文)", "负面提示词(英文)"],
  "新增基础资产": ["asset_id", "asset_type", "asset_name", "description", "reuse_policy", "first_seen_episode", "sync_to_bible", "静态生图提示词(中文)", "负面提示词(中文)", "静态生图提示词(英文)", "负面提示词(英文)"],
  "关键道具与场景状态": ["state_id", "episode_id", "cut_ids", "asset_id", "asset_type", "state_summary", "episode_usage", "needs_generation", "generation_note", "入库建议"],
  "不建议入库元素": ["元素", "出现位置", "不入库原因"],
  "分镜资产绑定索引": ["binding_id", "episode_id", "cut_id", "asset_id", "state_id", "asset_type", "binding_role", "reference_priority", "use_for_video", "required_for_generation", "source", "note"],
};

const SECTION_TO_SHEET = {
  "一、本集复用资产索引": "复用资产索引",
  "二、本集新增资产状态": "新增资产状态",
  "三、本集新增基础资产": "新增基础资产",
  "四、本集关键道具与场景状态": "关键道具与场景状态",
  "五、本集不建议入库元素": "不建议入库元素",
  "六、本集分镜资产绑定索引": "分镜资产绑定索引",
};

const TABLE_ENUM_COLUMNS = {
  "复用资产索引": {
    source: ENUMS.source,
    asset_type: ENUMS.asset_type,
    needs_generation: ENUMS.needs_generation,
  },
  "新增资产状态": {
    asset_type: ENUMS.asset_type,
    status_type: ENUMS.status_type,
    reuse_policy: ENUMS.reuse_policy,
    needs_generation: ENUMS.needs_generation,
    sync_to_bible: ENUMS.sync_to_bible,
  },
  "新增基础资产": {
    asset_type: ENUMS.asset_type,
    reuse_policy: ENUMS.reuse_policy,
    sync_to_bible: ENUMS.sync_to_bible,
  },
  "关键道具与场景状态": {
    asset_type: ENUMS.asset_type,
    needs_generation: ENUMS.needs_generation,
  },
  "分镜资产绑定索引": {
    asset_type: ENUMS.asset_type,
    binding_role: ENUMS.binding_role,
    reference_priority: ENUMS.reference_priority,
    use_for_video: ENUMS.use_for_video,
    required_for_generation: ENUMS.required_for_generation,
    source: ENUMS.binding_source,
  },
};

const REQUIRED_NONEMPTY_COLUMNS = {
  "复用资产索引": ["使用ID", "episode_id", "cut_ids", "asset_id", "state_id", "asset_type", "source", "episode_usage", "needs_generation"],
  "新增资产状态": ["state_id", "episode_id", "cut_ids", "asset_id", "asset_type", "status_type", "reuse_policy", "episode_usage", "needs_generation", "sync_to_bible"],
  "新增基础资产": ["asset_id", "asset_type", "asset_name", "reuse_policy", "first_seen_episode", "sync_to_bible"],
  "关键道具与场景状态": ["state_id", "episode_id", "cut_ids", "asset_id", "asset_type", "episode_usage", "needs_generation"],
  "不建议入库元素": ["元素", "出现位置", "不入库原因"],
  "分镜资产绑定索引": ["binding_id", "episode_id", "cut_id", "asset_id", "state_id", "asset_type", "binding_role", "reference_priority", "use_for_video", "required_for_generation", "source"],
};

const errors = [];
let standardAssetTables = [];
let storyboardIndex = null;

async function exists(filePath) {
  try {
    await fs.access(filePath);
    return true;
  } catch {
    return false;
  }
}

async function readJson(filePath, label) {
  try {
    const raw = await fs.readFile(filePath, "utf8");
    return JSON.parse(raw.replace(/^\uFEFF/u, ""));
  } catch (error) {
    errors.push(`${label} is not valid JSON: ${error.message}`);
    return null;
  }
}

function parseMarkdownRow(row) {
  return row
    .replace(/^\|/, "")
    .replace(/\|$/, "")
    .split("|")
    .map((cell) => cell.trim());
}

function parseMarkdownTables(markdown) {
  const lines = markdown.split(/\r?\n/);
  const tables = [];
  let currentSection = "";

  for (let i = 0; i < lines.length; i += 1) {
    const line = lines[i].trim();
    if (/^#{1,3}\s+/.test(line)) {
      currentSection = line.replace(/^#{1,3}\s+/, "").trim();
      continue;
    }
    if (!line.startsWith("|")) continue;

    const next = (lines[i + 1] || "").trim();
    if (!next.startsWith("|") || !/^\|[\s:|\-]+\|$/.test(next)) continue;

    const rows = [];
    const tableStart = i;
    for (let j = tableStart; j < lines.length; j += 1) {
      const row = lines[j].trim();
      if (!row.startsWith("|")) break;
      if (j !== tableStart + 1) rows.push(parseMarkdownRow(row));
      i = j;
    }

    if (rows.length > 0) tables.push({ section: currentSection, rows });
  }

  return tables;
}

function splitCutIds(value) {
  return String(value || "")
    .split(/[,，、\s]+/)
    .map((item) => item.trim())
    .filter(Boolean);
}

function tableRowsBySheet(sheetName) {
  const table = standardAssetTables.find((candidate) => candidate.sheetName === sheetName);
  if (!table) return [];
  const [header, ...dataRows] = table.rows;
  if (!header) return [];
  return dataRows.map((row) => Object.fromEntries(header.map((column, index) => [column, row[index] || ""])));
}

function validateCutIdColumns(table, header, row, rowNumber) {
  const episodeId = columnValue(header, row, "episode_id");
  const cutIdsValue = columnValue(header, row, "cut_ids");
  if (!episodeId && !cutIdsValue) return;

  if (storyboardIndex?.episode_id && episodeId !== storyboardIndex.episode_id) {
    errors.push(`${table.section} row ${rowNumber} episode_id=${episodeId} but storyboard_index episode_id=${storyboardIndex.episode_id}`);
  }

  const knownCuts = new Set((storyboardIndex?.cuts || []).map((cut) => cut.cut_id));
  for (const cutId of splitCutIds(cutIdsValue)) {
    if (storyboardIndex && !knownCuts.has(cutId)) {
      errors.push(`${table.section} row ${rowNumber} cut_id not found in storyboard_index: ${cutId}`);
    }
  }
}

function validateAssetsMarkdown(markdown) {
  const tables = parseMarkdownTables(markdown);
  const standardTables = tables
    .map((table) => {
      const prefix = Object.keys(SECTION_TO_SHEET).find((candidate) => table.section.startsWith(candidate));
      return prefix ? { ...table, sheetName: SECTION_TO_SHEET[prefix] } : null;
    })
    .filter(Boolean);
  standardAssetTables = standardTables;

  const found = new Set(standardTables.map((table) => table.sheetName));
  for (const table of REQUIRED_SHEETS) {
    if (!found.has(table)) errors.push(`assets.md missing required table: ${table}`);
  }

  for (const table of standardTables) {
    const [header, ...dataRows] = table.rows;
    if (!header) {
      errors.push(`${table.section} missing header row`);
      continue;
    }

    const requiredColumns = REQUIRED_COLUMNS[table.sheetName] || [];
    const missing = requiredColumns.filter((column) => !header.includes(column));
    if (missing.length > 0) {
      errors.push(`${table.section} missing required columns: ${missing.join(", ")}`);
    }

    dataRows.forEach((row, index) => {
      if (row.length !== header.length) {
        errors.push(`${table.section} row ${index + 2} has ${row.length} cells but header has ${header.length}`);
        return;
      }

      validateRowValues(table, header, row, index + 2);
    });
  }
}

function columnValue(header, row, column) {
  const index = header.indexOf(column);
  return index >= 0 ? row[index] : "";
}

function validateRowValues(table, header, row, rowNumber) {
  for (const column of REQUIRED_NONEMPTY_COLUMNS[table.sheetName] || []) {
    if (!columnValue(header, row, column)) {
      errors.push(`${table.section} row ${rowNumber} column ${column} must not be empty`);
    }
  }

  const enumColumns = TABLE_ENUM_COLUMNS[table.sheetName] || {};
  for (const [column, allowedValues] of Object.entries(enumColumns)) {
    const value = columnValue(header, row, column);
    if (value && !allowedValues.includes(value)) {
      errors.push(`${table.section} row ${rowNumber} column ${column} has invalid value "${value}". Allowed: ${allowedValues.join(", ")}`);
    }
  }

  const stateId = columnValue(header, row, "state_id");
  if (header.includes("state_id") && !stateId) {
    errors.push(`${table.section} row ${rowNumber} state_id must not be empty; use BASE when no state applies`);
  }
  validateCutIdColumns(table, header, row, rowNumber);
}

function validateBindingRows() {
  const rows = tableRowsBySheet("分镜资产绑定索引");
  const seen = new Set();
  const knownCuts = new Set((storyboardIndex?.cuts || []).map((cut) => cut.cut_id));

  for (const [index, row] of rows.entries()) {
    const rowNumber = index + 2;
    if (seen.has(row.binding_id)) {
      errors.push(`本集分镜资产绑定索引 row ${rowNumber} duplicate binding_id: ${row.binding_id}`);
    }
    seen.add(row.binding_id);
    if (storyboardIndex?.episode_id && row.episode_id !== storyboardIndex.episode_id) {
      errors.push(`本集分镜资产绑定索引 row ${rowNumber} episode_id=${row.episode_id} but storyboard_index episode_id=${storyboardIndex.episode_id}`);
    }
    if (storyboardIndex && !knownCuts.has(row.cut_id)) {
      errors.push(`本集分镜资产绑定索引 row ${rowNumber} cut_id not found in storyboard_index: ${row.cut_id}`);
    }
    if (row.use_for_video === "yes" && row.source === "manual_candidate" && row.required_for_generation === "yes") {
      errors.push(`本集分镜资产绑定索引 row ${rowNumber} cannot require generation from manual_candidate without asset_table or asset_bible confirmation`);
    }
  }

  if (storyboardIndex && rows.length > 0) {
    for (const cut of storyboardIndex.cuts || []) {
      const cutRows = rows.filter((row) => row.cut_id === cut.cut_id);
      if (!cutRows.some((row) => row.binding_role === "scene_reference" && row.reference_priority === "primary")) {
        errors.push(`本集分镜资产绑定索引 missing primary scene binding for ${cut.cut_id}`);
      }
    }
  }
}

function validateAssetBindingsJson(bindingsPayload) {
  if (!bindingsPayload) return;
  if (!Array.isArray(bindingsPayload.bindings)) {
    errors.push("asset_bindings.json bindings must be an array");
    return;
  }
  if (storyboardIndex?.episode_id && bindingsPayload.episode_id !== storyboardIndex.episode_id) {
    errors.push(`asset_bindings.json episode_id=${bindingsPayload.episode_id} but storyboard_index episode_id=${storyboardIndex.episode_id}`);
  }

  const knownCuts = new Set((storyboardIndex?.cuts || []).map((cut) => cut.cut_id));
  const seen = new Set();
  bindingsPayload.bindings.forEach((binding, index) => {
    for (const field of ["binding_id", "cut_id", "asset_id", "state_id", "asset_type", "binding_role", "reference_priority", "use_for_video", "required_for_generation", "source"]) {
      if (!binding?.[field]) errors.push(`asset_bindings.json bindings[${index}] missing ${field}`);
    }
    if (binding?.binding_id) {
      if (seen.has(binding.binding_id)) errors.push(`asset_bindings.json duplicate binding_id: ${binding.binding_id}`);
      seen.add(binding.binding_id);
    }
    for (const [field, allowed] of Object.entries({
      asset_type: ENUMS.asset_type,
      binding_role: ENUMS.binding_role,
      reference_priority: ENUMS.reference_priority,
      use_for_video: ENUMS.use_for_video,
      required_for_generation: ENUMS.required_for_generation,
      source: ENUMS.binding_source,
    })) {
      if (binding?.[field] && !allowed.includes(binding[field])) {
        errors.push(`asset_bindings.json bindings[${index}].${field} has invalid value "${binding[field]}". Allowed: ${allowed.join(", ")}`);
      }
    }
    if (storyboardIndex && binding?.cut_id && !knownCuts.has(binding.cut_id)) {
      errors.push(`asset_bindings.json bindings[${index}] cut_id not found in storyboard_index: ${binding.cut_id}`);
    }
  });

  const bindingTableIds = new Set(tableRowsBySheet("分镜资产绑定索引").map((row) => row.binding_id));
  for (const binding of bindingsPayload.bindings) {
    if (binding.binding_id && bindingTableIds.size > 0 && !bindingTableIds.has(binding.binding_id)) {
      errors.push(`asset_bindings.json binding_id not found in assets.md binding table: ${binding.binding_id}`);
    }
  }
}

function validateReview(review) {
  if (!review) return;
  if (review.pass !== true) errors.push("asset_review.pass must be true");
  if (!Array.isArray(review.issues)) errors.push("asset_review.issues must be an array");
  if (Array.isArray(review.issues) && review.issues.length !== 0) errors.push("asset_review.issues must be empty");
  if (!Array.isArray(review.warnings)) errors.push("asset_review.warnings must be an array");

  const checkedTables = new Set(Array.isArray(review.checked_tables) ? review.checked_tables : []);
  for (const table of REQUIRED_TABLES) {
    if (!checkedTables.has(table)) errors.push(`asset_review.checked_tables missing: ${table}`);
  }

  for (const key of REQUIRED_AUDIT_COVERAGE) {
    if (review.audit_coverage?.[key] !== "checked") {
      errors.push(`asset_review.audit_coverage.${key} must be "checked"`);
    }
  }

  if (!Array.isArray(review.spot_checks) || review.spot_checks.length < 3) {
    errors.push("asset_review.spot_checks must contain at least 3 entries");
  }

  if (!Array.isArray(review.semantic_checks) || review.semantic_checks.length < 5) {
    errors.push("asset_review.semantic_checks must contain at least 5 entries");
    return;
  }

  review.semantic_checks.forEach((check, index) => {
    for (const field of ["table", "type", "result", "evidence", "fix_instruction"]) {
      if (!check?.[field]) errors.push(`asset_review.semantic_checks[${index}] missing ${field}`);
    }
    if (check?.result && !ENUMS.semantic_result.includes(check.result)) {
      errors.push(`asset_review.semantic_checks[${index}].result has invalid value "${check.result}"`);
    }
    if (review.pass === true && check?.result === "issue") {
      errors.push(`asset_review.semantic_checks[${index}] result=issue but asset_review.pass=true`);
    }
  });

  const semanticTypes = new Set(review.semantic_checks.map((check) => check.type));
  for (const [group, types] of Object.entries(SEMANTIC_COVERAGE_GROUPS)) {
    if (!types.some((type) => semanticTypes.has(type))) {
      errors.push(`asset_review.semantic_checks missing coverage for ${group}: ${types.join(" or ")}`);
    }
  }
}

function validateStatus(status, review) {
  if (!status) return;
  if (status.status !== "done") errors.push('asset_status.status must be "done"');
  if (status.reviewer_source !== "asset-reviewer") errors.push('asset_status.reviewer_source must be "asset-reviewer"');
  if (status.reviewer_pass !== review?.pass) errors.push("asset_status.reviewer_pass must match asset_review.pass");
  if (status.reviewer_issues_count !== (review?.issues || []).length) {
    errors.push("asset_status.reviewer_issues_count must match asset_review.issues.length");
  }
  if (status.reviewer_warnings_count !== (review?.warnings || []).length) {
    errors.push("asset_status.reviewer_warnings_count must match asset_review.warnings.length");
  }
  if (!Array.isArray(status.hard_issues_remaining)) errors.push("asset_status.hard_issues_remaining must be an array");
  if (Array.isArray(status.hard_issues_remaining) && status.hard_issues_remaining.length !== 0) {
    errors.push("asset_status.hard_issues_remaining must be empty");
  }
  if (!Array.isArray(status.bible_update_candidates)) errors.push("asset_status.bible_update_candidates must be an array");
}

async function validateWorkbookFreshness() {
  if (!(await exists(requiredFiles.assets)) || !(await exists(requiredFiles.workbook))) return;
  const assetsStat = await fs.stat(requiredFiles.assets);
  const workbookStat = await fs.stat(requiredFiles.workbook);
  if (workbookStat.mtimeMs + 1000 < assetsStat.mtimeMs) {
    errors.push("assets.xlsx is older than assets.md; rerun assets-md-to-xlsx.mjs");
  }
}

for (const [label, filePath] of Object.entries(requiredFiles)) {
  if (!(await exists(filePath))) errors.push(`Missing ${label}: ${filePath}`);
}

let review = null;
let status = null;
let bindings = null;

if (options["storyboard-index"]) {
  const storyboardIndexPath = path.resolve(options["storyboard-index"]);
  if (!(await exists(storyboardIndexPath))) {
    errors.push(`storyboard_index not found: ${storyboardIndexPath}`);
  } else {
    storyboardIndex = await readJson(storyboardIndexPath, "storyboard_index.json");
    if (storyboardIndex && (!storyboardIndex.episode_id || !Array.isArray(storyboardIndex.cuts))) {
      errors.push("storyboard_index.json must include episode_id and cuts[]");
    }
  }
}

if (await exists(requiredFiles.assets)) {
  validateAssetsMarkdown(await fs.readFile(requiredFiles.assets, "utf8"));
  validateBindingRows();
}
if (await exists(requiredFiles.review)) review = await readJson(requiredFiles.review, "asset_review.json");
if (await exists(requiredFiles.status)) status = await readJson(requiredFiles.status, "asset_status.json");
if (await exists(requiredFiles.bindings)) bindings = await readJson(requiredFiles.bindings, "asset_bindings.json");

validateReview(review);
validateStatus(status, review);
validateAssetBindingsJson(bindings);
await validateWorkbookFreshness();

if (errors.length > 0) {
  console.error(`Asset validation failed for ${episodeDir}`);
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

console.log(`Asset validation passed for ${episodeDir}`);
