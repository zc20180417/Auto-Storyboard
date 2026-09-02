import copy
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "tests" / "fixtures" / "seedance25" / "provider-contract-reference.json"
MODEL_CONTRACT_PATH = (
    ROOT
    / "agent_skills"
    / "seedance-2-5-horizontal-xianxia-3d-cg"
    / "references"
    / "model-contract.md"
)
EVIDENCE_PATH = ROOT / "docs" / "seedance25-horizontal-xianxia-contract-evidence.md"

OFFICIAL_URLS = {
    "https://docs.volcengine.com/docs/82379/2607688",
    "https://docs.volcengine.com/docs/82379/1520757",
    "https://docs.volcengine.com/docs/82379/2298881",
    "https://docs.volcengine.com/docs/82379/2637911",
}

SECRET_KEY_RE = re.compile(
    r"authorization|cookie|secret|access[_-]?key|api[_-]?key|signed[_-]?url|signature",
    re.IGNORECASE,
)
SECRET_VALUE_RE = re.compile(
    r"(?i)(bearer\s+[a-z0-9._-]{12,}|x-tos-signature=|x-amz-signature=|aklt[a-z0-9]{12,})"
)


def load_contract() -> dict:
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


def contract_issues(contract: dict) -> list[str]:
    issues: list[str] = []
    provider = contract.get("provider") or {}
    capability = contract.get("official_capability") or {}
    product = contract.get("product_profile") or {}
    mapping = product.get("task_mapping") or {}
    material_limits = capability.get("material_limits") or {}

    if provider.get("model_id") != "doubao-seedance-2-5-260628":
        issues.append("unexpected model_id")
    if provider.get("create_endpoint") != "https://ark.cn-beijing.volces.com/api/v3/contents/generations/tasks":
        issues.append("unexpected create endpoint")
    if "16:9" not in capability.get("ratios", []):
        issues.append("missing 16:9 capability")
    if "720p" not in capability.get("resolutions", []):
        issues.append("missing 720p capability")
    if capability.get("duration_seconds") != {"minimum": 4, "maximum": 30, "auto": -1}:
        issues.append("unexpected provider duration contract")
    if capability.get("generate_audio") is not True:
        issues.append("missing native audio capability")
    if set(capability.get("reference_roles", [])) != {
        "reference_image",
        "reference_video",
        "reference_audio",
    }:
        issues.append("unexpected reference roles")
    if material_limits != {"image": 30, "video": 10, "audio": 10, "total": 50}:
        issues.append("unexpected material limits")
    if product.get("ratio") != "16:9" or product.get("resolution") != "720p":
        issues.append("unexpected product ratio/resolution")
    if product.get("duration_seconds") != {"minimum": 4, "maximum": 30, "integer_only": True}:
        issues.append("unexpected product duration contract")
    if product.get("allow_auto_duration") is not False:
        issues.append("auto duration must be disabled")
    if product.get("minimum_reference_inputs") != 1:
        issues.append("at least one reference input is required")
    if mapping.get("internal_task") != "multimodal_generation":
        issues.append("unexpected internal task")
    if mapping.get("provider_field") != "omni_reference_task_type" or mapping.get("provider_value") != "reference":
        issues.append("unexpected provider task mapping")
    if set(mapping.get("required_reference_roles", [])) != {
        "reference_image",
        "reference_video",
        "reference_audio",
    }:
        issues.append("unexpected product reference roles")
    if "fps" not in product.get("forbidden_create_fields", []):
        issues.append("fps must be forbidden in create requests")
    if "video_task_type" not in product.get("forbidden_create_fields", []):
        issues.append("internal task field must be forbidden in create requests")
    return issues


def valid_product_duration(value: object) -> bool:
    return type(value) is int and 4 <= value <= 30


class Seedance25ProviderContractTests(unittest.TestCase):
    def test_official_fixture_freezes_horizontal_reference_contract(self):
        contract = load_contract()

        self.assertEqual(contract_issues(contract), [])
        self.assertEqual({item["url"] for item in contract["sources"]}, OFFICIAL_URLS)
        self.assertEqual(contract["official_capability"]["output_fps"], 24)
        self.assertEqual(contract["official_capability"]["resolution_pixels"]["16:9"]["720p"], [1280, 720])
        self.assertEqual(contract["product_profile"]["enabled_resolutions"], ["720p"])
        self.assertNotIn("1080p", contract["product_profile"]["enabled_resolutions"])

    def test_product_duration_accepts_integer_boundaries_and_rejects_provider_auto(self):
        self.assertTrue(valid_product_duration(4))
        self.assertTrue(valid_product_duration(30))
        for value in (-1, 3, 31, 4.0, 4.5, True, None):
            with self.subTest(value=value):
                self.assertFalse(valid_product_duration(value))

    def test_missing_critical_provider_capabilities_fail_closed(self):
        base = load_contract()
        mutations = (
            ("16:9", lambda value: value["official_capability"].update(ratios=["9:16"])),
            ("720p", lambda value: value["official_capability"].update(resolutions=["480p"])),
            ("native audio", lambda value: value["official_capability"].update(generate_audio=False)),
            ("reference roles", lambda value: value["official_capability"].update(reference_roles=[])),
        )

        for expected, mutate in mutations:
            with self.subTest(expected=expected):
                candidate = copy.deepcopy(base)
                mutate(candidate)
                self.assertTrue(any(expected in issue for issue in contract_issues(candidate)))

    def test_fixture_is_redacted_non_replayable_and_secret_free(self):
        contract = load_contract()
        serialized = json.dumps(contract, ensure_ascii=False)

        self.assertEqual(contract["fixture_security"]["classification"], "public-redacted-contract-snapshot")
        self.assertIs(contract["fixture_security"]["replayable"], False)
        self.assertIs(contract["fixture_security"]["raw_capture_in_repository"], False)
        self.assertIsNone(SECRET_VALUE_RE.search(serialized))

        def walk(value: object, path: str = "$") -> None:
            if isinstance(value, dict):
                for key, child in value.items():
                    self.assertIsNone(SECRET_KEY_RE.search(key), f"secret-bearing key at {path}.{key}")
                    walk(child, f"{path}.{key}")
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    walk(child, f"{path}[{index}]")

        walk(contract)

    def test_human_contract_and_evidence_repeat_machine_decisions(self):
        model_contract = MODEL_CONTRACT_PATH.read_text(encoding="utf-8")
        evidence = EVIDENCE_PATH.read_text(encoding="utf-8")

        for text in (model_contract, evidence):
            self.assertIn("doubao-seedance-2-5-260628", text)
            self.assertIn("`16:9`", text)
            self.assertIn("`720p`", text)
            self.assertIn("`4`–`30`", text)
            self.assertIn("`omni_reference_task_type=reference`", text)
            self.assertIn("24 fps", text)
            self.assertIn("不是创建请求字段", text)


if __name__ == "__main__":
    unittest.main()
