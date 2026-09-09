"""Run the pinned Observer -> Engine path and emit a KG audit envelope."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--observer", type=Path, required=True)
    parser.add_argument("--engine", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    sys.path.insert(0, str(args.observer / "src"))
    from observer_engine2.adapter import Engine2ObserverAdapter, InMemoryProjectionAudit
    from observer_engine2.canonical import canonical_json, sha256_digest
    from observer_engine2.messages import SnapshotBinding
    from observer_engine2.runtime import PinnedEngineRuntimePort

    engine_commit = os.environ["ENGINE_COMMIT"]
    observer_commit = os.environ["OBSERVER_IMPLEMENTATION_COMMIT"]
    kg_commit = os.environ["KG_COMMIT"]

    def handler(request):
        return "ALLOW", "PINNED_COMPOSITE_RUNTIME", "PASS"

    runtime = PinnedEngineRuntimePort(args.engine, handler)
    projection_audit = InMemoryProjectionAudit([])
    adapter = Engine2ObserverAdapter(runtime, projection_audit)
    protocol_object = {"descriptor": "offline-three-repository-composite"}
    request = adapter.build_request(
        request_id="req-three-repo-001",
        idempotency_key="idem-three-repo-001",
        protocol_object=protocol_object,
        snapshot_binding=SnapshotBinding(
            engine_commit,
            observer_commit,
            kg_commit,
            "0.3.0-rc",
            "fixture-snapshot-three-repo-001",
        ),
    )
    projection = adapter.observe(request)
    if projection_audit.records != [projection]:
        raise RuntimeError("Observer projection audit did not preserve the emitted projection")
    result = projection["engine_response"]
    if projection["engine_response_type"] != "EngineRetrievalResult":
        raise RuntimeError("Pinned Engine did not produce a retrieval result")
    adapter.verify_projection(request, result, projection)

    semantic_request = {
        "generation": request.generation,
        "protocol_object": dict(request.protocol_object),
        "protocol_object_digest": request.protocol_object_digest,
        "snapshot_binding": request.snapshot_binding.to_dict(),
    }
    audit_event = {
        "event_id": f"audit-{request.request_id}",
        "request_id": request.request_id,
        "event_type": "ENGINE_RETRIEVAL",
        "outcome": result["decision"],
        "original_event_ref": "NONE",
        "input_digest": sha256_digest(semantic_request),
        "output_digest": result["result_digest"],
    }
    envelope = {
        "idempotency_key": request.idempotency_key,
        "protocol_object_json": canonical_json(dict(request.protocol_object)).decode("utf-8"),
        "protocol_object_digest": request.protocol_object_digest,
        "snapshot_binding": projection["request_snapshot_binding"],
        "engine_result": result,
        "audit_event": audit_event,
        "audit_event_digest": sha256_digest(audit_event),
        "error_code": "NONE",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(envelope, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("OBSERVER_ENGINE_PROJECTION=PASS")
    print(f"ENVELOPE_SHA256={sha256_digest(envelope)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
