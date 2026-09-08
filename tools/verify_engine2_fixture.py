"""Verify Engine 2 authoring fixtures with RFC 8785 canonical JSON."""
from __future__ import annotations

import argparse
import hashlib
from copy import deepcopy
from pathlib import Path
from typing import Any

import rfc8785
import yaml
from yaml.nodes import MappingNode, ScalarNode, SequenceNode


def reject_duplicate_keys(node: Any) -> None:
    if isinstance(node, MappingNode):
        seen: set[str] = set()
        for key, value in node.value:
            if isinstance(key, ScalarNode) and key.value != "<<":
                if key.value in seen:
                    raise ValueError(f"duplicate YAML key: {key.value}")
                seen.add(key.value)
            reject_duplicate_keys(value)
    elif isinstance(node, SequenceNode):
        for value in node.value:
            reject_duplicate_keys(value)


def digest(value: Any) -> str:
    return hashlib.sha256(rfc8785.dumps(value)).hexdigest().upper()


def verify(path: Path) -> None:
    source = path.read_text(encoding="utf-8")
    reject_duplicate_keys(yaml.compose(source))
    document = yaml.safe_load(source)

    whole = deepcopy(document)
    claimed = whole["digest_policy"]["fixture_set_digest"]
    whole["digest_policy"]["fixture_set_digest"] = ""
    if digest(whole) != claimed:
        raise ValueError("fixture_set_digest mismatch")

    for case in document["fixture_cases"]:
        resolved = deepcopy(case)
        resolved["bindings"]["FIXTURE_DIGEST"] = ""
        expected = digest(case["expected"]) if "expected" in case else "NOT_AVAILABLE"
        audit = digest(case["audit"]) if "audit" in case else "NOT_AVAILABLE"
        bindings = case["bindings"]
        if digest(resolved) != bindings["FIXTURE_DIGEST"]:
            raise ValueError(f"{case['id']}: FIXTURE_DIGEST mismatch")
        if expected != bindings["EXPECTED_RESULT_DIGEST"]:
            raise ValueError(f"{case['id']}: EXPECTED_RESULT_DIGEST mismatch")
        if audit != bindings["AUDIT_EVENT_DIGEST"]:
            raise ValueError(f"{case['id']}: AUDIT_EVENT_DIGEST mismatch")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    args = parser.parse_args()
    verify(args.fixture)
    print(f"VALID: {args.fixture}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
