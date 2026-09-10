"""Validate FDE-TRIAL-001 runtime messages and fail-closed invariants."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas/fde-trial-001-runtime-message.schema.json"
EXAMPLES = ROOT / "examples/fde-trial-001-runtime"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate key: {key}")
        result[key] = value
    return result


def validate_semantics(message: dict) -> None:
    payload = message["payload"]
    kind = message["message_type"]
    if kind == "ENGINE_PRE_ACTION_AUDIT":
        result = payload["engine_result"]
        if result["request_id"] != payload["request_id"]:
            raise ValueError("Engine request binding mismatch")
        if result["result_digest"] != result["original_engine_result_digest"]:
            raise ValueError("Engine result was rewritten")
        if payload["engine_result_sha256"] != payload["original_engine_result_sha256"]:
            raise ValueError("Engine audit digest was rewritten")
    elif kind == "HUMAN_DECISION":
        expected = "ACTIVE" if payload["decision"] == "APPROVE" else "REJECTED"
        required = "APPROVE_POLICY_ACTIVATION" if payload["decision"] == "APPROVE" else "REJECT_POLICY_ACTIVATION"
        if payload["resulting_snapshot_state"] != expected or required not in payload["authority_scope"]:
            raise ValueError("Human decision state or authority mismatch")
    elif kind == "ACTION_OUTCOME":
        if (payload["outcome"] == "ACTION_RECEIPT") != (payload["receipt"] is not None):
            raise ValueError("Action outcome and receipt mismatch")
    elif kind == "ACTION_RECONCILIATION_RESULT":
        if (payload["status"] == "FOUND") != (payload["receipt"] is not None):
            raise ValueError("Reconciliation status and receipt mismatch")
        if payload["retry_allowed"] is not False:
            raise ValueError("Reconciliation never grants automatic retry")


def reject(validator, message: dict) -> None:
    try:
        validator.validate(message)
        validate_semantics(message)
    except (jsonschema.ValidationError, ValueError):
        return
    raise AssertionError("invalid runtime message was accepted")


def main() -> int:
    schema = load(SCHEMA)
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    messages = {path.stem: load(path) for path in sorted(EXAMPLES.glob("*.json"))}
    for message in messages.values():
        validator.validate(message)
        validate_semantics(message)

    invalid = deepcopy(messages["engine-pre-action-audit"])
    invalid["payload"]["engine_result"]["decision"] = "ALLOW"
    reject(validator, invalid)
    invalid = deepcopy(messages["human-decision"])
    invalid["payload"]["unexpected"] = True
    reject(validator, invalid)
    invalid = deepcopy(messages["action-outcome"])
    invalid["payload"]["receipt"] = None
    reject(validator, invalid)
    invalid = deepcopy(messages["action-reconciliation-result"])
    invalid["payload"]["status"] = "UNKNOWN"
    invalid["payload"]["receipt"] = None
    invalid["payload"]["retry_allowed"] = True
    reject(validator, invalid)
    print(f"VALID: {len(messages)} runtime message examples; fail-closed negatives PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
