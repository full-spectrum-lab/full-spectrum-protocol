"""Validate FDE-TRIAL-001 inputs and their RFC 8785 manifest digests."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import jsonschema
import rfc8785


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_object)


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def canonical_digest(value: object) -> str:
    return hashlib.sha256(rfc8785.dumps(value)).hexdigest().upper()


def verify(root: Path, schema_path: Path) -> None:
    schema = load_json(schema_path)
    manifest = load_json(root / "CASE-MANIFEST.json")
    assert isinstance(manifest, dict)
    expected_files = manifest["files"]
    assert isinstance(expected_files, dict)
    actual_names = {path.name for path in root.glob("*.json")} - {"CASE-MANIFEST.json"}
    if actual_names != set(expected_files):
        raise ValueError("manifest file set mismatch")
    for name, expected_digest in expected_files.items():
        document = load_json(root / name)
        jsonschema.Draft202012Validator(schema).validate(document)
        if name in {"policy-before.json", "policy-proposed.json"}:
            assert isinstance(document, dict)
            payload = document["payload"]
            assert isinstance(payload, dict)
            source_digest = hashlib.sha256(payload["rule"].encode("utf-8")).hexdigest().upper()
            if source_digest != payload["source_content_sha256"]:
                raise ValueError(f"{name}: source_content_sha256 mismatch")
        actual_digest = canonical_digest(document)
        if actual_digest != expected_digest:
            raise ValueError(f"{name}: digest mismatch")
    if manifest["fixture_status"] != "FREEZE_CANDIDATE":
        raise ValueError("fixture must remain FREEZE_CANDIDATE before review")
    binding = manifest["repository_binding"]
    for field in ("protocol_contract_commit", "qpp_frozen_spec_commit"):
        if len(binding[field]) != 40:
            raise ValueError(f"{field}: full commit required")
    schema_digest = hashlib.sha256(schema_path.read_bytes()).hexdigest().upper()
    if schema_digest != binding["schema_file_sha256"]:
        raise ValueError("schema_file_sha256 mismatch")
    projection = manifest["observer_projection_contract"]
    if set(projection["document_keys"]) != set(expected_files):
        raise ValueError("observer document_keys must cover all fixture documents")
    if set(projection["protected_json_pointers"]) != set(expected_files):
        raise ValueError("protected pointer sets must cover all fixture documents")
    print(f"VALID: {root} ({len(expected_files)} documents)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    parser.add_argument("schema", type=Path)
    args = parser.parse_args()
    verify(args.fixture, args.schema)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
