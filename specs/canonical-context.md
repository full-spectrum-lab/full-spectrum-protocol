# Canonical Context Minimal Specification v0.1

The Canonical Context is the normalized, governance-ready representation that a Business Adapter produces from raw business input via `to_canonical_context`. It is the single object the engine consumes, so every business line maps onto one common shape before any risk reasoning runs.

---

## 1. Purpose

Raw business input is noisy and business-specific. Before the engine can reason about risk, the adapter must produce a canonical, schema-valid view that contains:

- who acted (`actor`);
- what they did (`action`);
- whether they were authorized (`authority`);
- what is known vs. unknown (`known_facts` / `unknowns`);
- where the risk sits on normalized axes (`risk_axes`);
- privacy posture of the record (`privacy`).

This lets any downstream engine, report, or enterprise writeback consume one stable object regardless of the originating business line.

---

## 2. Non-goals

The Canonical Context does not:

- perform risk reasoning (that is the engine's job, producing a Governance Output Envelope);
- define adapter internals or commitment-detection rules (see I/O Contract);
- assert final business decisions (see Enterprise Writeback);
- require joining a Full Spectrum network.

---

## 3. Minimal fields

| Field | Required | Description |
|---|---:|---|
| `schema_version` | yes | Must equal `cc-0.1` |
| `canonical_context_id` | yes | Unique id of this canonical context |
| `source_event_id` | yes | Id of the Governance Event this context derives from |
| `actor` | yes | The governed subject: `id` + `type` (`human` / `ai_agent` / `system` / `organization`) |
| `action` | yes | The action under governance: `intent`, optional `commitment_type`, `authority_verified` |
| `authority` | yes | `verified` + optional `reason_code` / `reason` |
| `known_facts` | yes | Array of established facts (`description`, optional `severity`) |
| `unknowns` | yes | Array of open items (`description`, `severity`, `required_for_commitment`) |
| `risk_axes` | yes | Named axes, each a number in `[0, 1]` |
| `privacy` | yes | `public_shareable` + `redaction_status` (`public_redacted` / `synthetic` / `internal`) |
| `extension_fields` | yes | Open object for adapter-specific extras |

---

## 4. Minimal JSON example

```json
{
  "schema_version": "cc-0.1",
  "canonical_context_id": "cc_ecom_refund_001",
  "source_event_id": "ge_ecom_refund_001",
  "actor": {
    "id": "cs_ai_001",
    "type": "ai_agent"
  },
  "action": {
    "intent": "refund_request",
    "commitment_type": "refund_commitment",
    "authority_verified": false
  },
  "authority": {
    "verified": false,
    "reason_code": "REFUND_COMMITMENT_WITHOUT_AUTHORITY",
    "reason": "AI customer-service agent lacks refund commitment authority."
  },
  "known_facts": [
    {"description": "User requested a refund."},
    {"description": "AI made a full-refund commitment without authority."}
  ],
  "unknowns": [
    {"description": "Human review has not been completed.", "severity": "high", "required_for_commitment": true}
  ],
  "risk_axes": {
    "commitment_risk": 0.9,
    "authority_risk": 0.9,
    "knowledge_conflict_risk": 0.1
  },
  "privacy": {
    "public_shareable": true,
    "redaction_status": "synthetic"
  },
  "extension_fields": {}
}
```

---

## 5. Relationship to other specs

```text
I/O Contract (to_canonical_context)
  -> produces Canonical Context
  -> Engine consumes Canonical Context
  -> Engine produces Governance Output Envelope
  -> Engine produces Enterprise Writeback
```

The Canonical Context sits between the Governance Event (raw-ish) and the Governance Output Envelope (engine result). It is the normalization boundary: business-specific noise is resolved here, engine-specific reasoning happens after.

---

## 6. Current status

This is an early minimal specification (aligned with FSP-IO-v0.5-rc1 §8.1 Canonical Context Validator). Field names and axis vocabulary may change through RFC review.
