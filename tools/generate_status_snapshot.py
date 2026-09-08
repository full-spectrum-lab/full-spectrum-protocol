"""Generate a conservative, read-only project status snapshot.

The generator consumes repository status files and the compatibility matrix. It
never promotes a status; missing or contradictory facts are rendered as
UNKNOWN/NOT_CONFIRMED and publication is classified from the caller's input.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError(f"status file must contain an object: {path}")
    return data


def publication_state(data: dict[str, Any], source: Path) -> str:
    state = data.get("publication", {}).get("state")
    if state in {"LOCAL_ONLY", "COMMITTED_NOT_PUSHED", "PUBLISHED_REMOTE"}:
        return state
    return "LOCAL_ONLY" if ".git" not in source.parts else "UNKNOWN"


def source_reference(source: Path) -> str:
    parts = list(source.parts)
    for marker in ("qpp.wiki", "full-spectrum-observer", "full-spectrum-protocol"):
        if marker in parts:
            return "/".join(parts[parts.index(marker):])
    return source.name


def project_record(source: Path, data: dict[str, Any]) -> dict[str, Any]:
    if isinstance(data.get("case"), dict):
        case = data["case"]
        verification = case.get("verification_status", {})
        return {
            "record_type": "CASE_VALIDATION",
            "project": case.get("id", "UNKNOWN_CASE"),
            "source": source_reference(source),
            "authority": {"target_commit": case.get("target_commit"), "target_branch": case.get("target_branch")},
            "publication": case.get("archive_status", "UNKNOWN"),
            "release": {"current": case.get("version")},
            "implementation_status": "NOT_APPLICABLE",
            "verification_status": verification.get("value", "UNKNOWN"),
            "maturity_level": "NOT_APPLICABLE",
            "generation": "NOT_APPLICABLE",
            "contract": {},
            "production_readiness": {"status": "NOT_READY", "boolean": bool(data.get("production_ready", False))},
            "capability": {},
            "compatibility": {"protocol_observer": data.get("protocol_observer_compatibility", "NOT_CONFIRMED"), "observer_engine": data.get("observer_engine_compatibility", "NOT_CONFIRMED")},
            "credential_scope": "NOT_APPLICABLE",
            "credential_lifecycle": {},
            "error_codes_status": "NOT_APPLICABLE",
            "replay_contract_status": "NOT_APPLICABLE",
            "evidence_requirements_status": "NOT_APPLICABLE",
            "evidence_requirements": {},
            "evidence": verification.get("evidence", {}),
            "evidence_scope": verification.get("evidence_scope", "CASE_ONLY"),
            "limitations": verification.get("limitations", []),
            "unknowns": [],
        }
    capability = data.get("capability", {})
    if not capability and isinstance(data.get("capabilities"), dict):
        capability = data["capabilities"]
    compatibility = data.get("compatibility", {})
    return {
        "record_type": "INSTANCE_OR_PROJECT_STATUS",
        "project": data.get("project", data.get("repository", source.parent.parent.name)),
        "source": source_reference(source),
        "authority": data.get("authority", {}),
        "publication": publication_state(data, source),
        "release": data.get("release", {}),
        "inspected_prerelease": data.get("inspected_prerelease", {}),
        "implementation_status": data.get("implementation_status", "UNKNOWN"),
        "verification_status": data.get("verification_status", "UNKNOWN"),
        "maturity_level": data.get("maturity_level", "DESIGNED"),
        "generation": data.get("generation", capability.get("generation", "unknown")),
        "contract": data.get("contract", {}),
        "schema_field_baseline": data.get("schema_field_baseline", {}),
        "production_readiness": data.get("production_readiness", {"status": "UNKNOWN", "boolean": False}),
        "capability": capability,
        "compatibility": compatibility,
        "credential_scope": data.get("credential_scope", "UNKNOWN"),
        "credential_lifecycle": data.get("credential_lifecycle", {}),
        "error_codes_status": data.get("error_codes_status", "UNKNOWN"),
        "replay_contract_status": data.get("replay_contract_status", "UNKNOWN"),
        "evidence_requirements_status": data.get("evidence_requirements_status", "UNKNOWN"),
        "evidence_requirements": data.get("evidence_requirements", {}),
        "evidence": {
            "level": data.get("evidence", {}).get("level"),
            "scope": data.get("evidence", {}).get("scope"),
            "bundle": data.get("evidence", {}).get("bundle"),
            "bundle_sha256": data.get("evidence", {}).get("bundle_sha256"),
        },
        "evidence_scope": data.get("evidence_scope", data.get("evidence", {}).get("scope", "UNKNOWN")),
        "limitations": data.get("evidence", {}).get("limitations", data.get("limitations", [])),
        "unknowns": data.get("unknowns", []),
    }


def markdown(snapshot: dict[str, Any]) -> str:
    lines = ["# Full Spectrum 状态快照（只读生成）", "", f"- 生成时间：`{snapshot['generated_at']}`", "- 生成模式：`READ_ONLY`", "- 高风险自动升级：`FORBIDDEN`", "", "## 项目状态", "", "| 项目 | 代际 | 实现 | 验证 | 发布 | 能力 | 兼容 | 生产就绪 |", "|---|---|---|---|---|---|---|---|"]
    for item in snapshot["projects"]:
        ready = item["production_readiness"].get("status", "UNKNOWN")
        cap = item.get("capability", {})
        compat = item.get("compatibility", {})
        lines.append(f"| {item['project']} | {item['generation']} | {item['implementation_status']} | {item['verification_status']} | {item['publication']} | `{json.dumps(cap, ensure_ascii=False, separators=(',', ':'))}` | `{json.dumps(compat, ensure_ascii=False, separators=(',', ':'))}` | {ready} |")
    lines += ["", "## 分层状态", "", "```json", json.dumps({"implementation_status": [p["implementation_status"] for p in snapshot["projects"]], "verification_status": [p["verification_status"] for p in snapshot["projects"]], "publication_status": [p["publication"] for p in snapshot["projects"]], "capability_status": [p["capability"] for p in snapshot["projects"]], "compatibility_status": snapshot["triangle_status"], "production_readiness": [p["production_readiness"] for p in snapshot["projects"]]}, ensure_ascii=False, indent=2), "```", "", "## 三角兼容性", "", "```json", json.dumps(snapshot["triangle_status"], ensure_ascii=False, indent=2), "```", "", "## 约束", "", "- 本快照不把离线验证升级为真实网络、跨仓库正式兼容或生产就绪。", "- `LOCAL_ONLY`、`COMMITTED_NOT_PUSHED` 不得写成 `PUBLISHED_REMOTE`。", "- `NOT_CONFIRMED`、`UNKNOWN` 只能由人工裁决升级。", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--matrix", required=True, type=Path)
    parser.add_argument("--status", action="append", required=True, type=Path)
    parser.add_argument("--json-out", required=True, type=Path)
    parser.add_argument("--md-out", required=True, type=Path)
    args = parser.parse_args()
    matrix = json.loads(args.matrix.read_text(encoding="utf-8"))
    snapshot = {
        "schema_version": "0.1",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "mode": "READ_ONLY",
        "projects": [project_record(path, load_yaml(path)) for path in args.status],
        "triangle_status": matrix.get("triangle_status", {}),
        "observer_release_truth": matrix.get("observer_release_truth", {}),
        "source_matrix": str(args.matrix),
        "rules": matrix.get("capability_rules", {}),
    }
    snapshot["layered_summary"] = {
        "design_status": [{"project": p["project"], "maturity": p["maturity_level"]} for p in snapshot["projects"]],
        "implementation_status": [{"project": p["project"], "value": p["implementation_status"]} for p in snapshot["projects"]],
        "case_validation_status": [{"project": p["project"], "value": p["verification_status"], "scope": p.get("evidence_scope")} for p in snapshot["projects"] if p["record_type"] == "CASE_VALIDATION"],
        "single_repository_validation_status": [{"project": p["project"], "value": p["verification_status"], "scope": p.get("evidence_scope")} for p in snapshot["projects"] if p["record_type"] != "CASE_VALIDATION"],
        "cross_repository_compatibility_status": snapshot["triangle_status"],
        "real_network_status": "NOT_IMPLEMENTED_OR_NOT_CONFIRMED",
        "production_readiness": [{"project": p["project"], "value": p["production_readiness"]} for p in snapshot["projects"]],
    }
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.md_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.md_out.write_text(markdown(snapshot), encoding="utf-8")
    print(f"GENERATED: {args.json_out}")
    print(f"GENERATED: {args.md_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
