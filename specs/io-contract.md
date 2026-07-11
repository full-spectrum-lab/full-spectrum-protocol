# I/O Contract Minimal Specification v0.5

The I/O Contract defines how a business system's raw input and output map into Full Spectrum governance objects through a Business Adapter, so any business line can become inspectable without rewriting its internals.

---

## 1. Purpose

Different business systems (ecommerce, logistics, finance, healthcare) speak different input/output formats.

The I/O Contract defines a minimal mapping contract so that:

- raw business input becomes a `Governance Event`;
- the adapter produces a normalized `Canonical Context`;
- the engine produces a `Governance Output Envelope`;
- the enterprise system receives an `Enterprise Writeback` it can act on;
- every step stays schema-valid and reproducible.

---

## 2. Non-goals

The I/O Contract does not:

- define engine internals (RiskVector, Runestone, FSHI);
- replace business logic or policy engines;
- require joining a Full Spectrum network;
- claim production compliance;
- cover every industry (v0.5 ships Ecommerce and Logistics Adapters only).

---

## 3. Minimal contract fields

| Field | Required | Description |
|---|---:|---|
| `adapter_id` | yes | Identifier of the Business Adapter |
| `raw_input_schema` | yes | Declared shape of the business raw input |
| `commitment_detection` | recommended | Rule/keyword or model-based commitment detector |
| `to_governance_event` | yes | Mapping from raw input to a Governance Event |
| `to_canonical_context` | yes | Mapping that produces a Canonical Context |
| `governance_output_envelope` | yes | Expected engine output object |
| `enterprise_writeback` | yes | Expected enterprise-consumable decision object |
| `report` | recommended | Human-readable Markdown report |

---

## 4. Minimal mapping chain

```text
raw_input
  -> Adapter.parse_raw_input()
  -> Adapter.detect_commitment()
  -> Adapter.to_governance_event()
  -> Adapter.to_canonical_context()
  -> Engine.run()
  -> governance_output_envelope
  -> enterprise_writeback
  -> report
```

---

## 5. Minimal JSON example (EcommerceAdapter)

```json
{
  "adapter_id": "ecommerce",
  "raw_input": {
    "raw_input_id": "raw_ecom_001",
    "business_line": "ecommerce_customer_service",
    "user_message": "我要退款。",
    "ai_response": "可以给您全额退款。",
    "refund_authority": false,
    "human_review_completed": false
  },
  "commitment_detection": {
    "is_commitment": true,
    "claim_type": "refund_commitment",
    "detection_mode": "rule_based_keyword"
  },
  "outputs": {
    "governance_event": "generated",
    "canonical_context": "generated",
    "enterprise_writeback": "generated"
  }
}
```

---

## 6. Relationship to other specs

```text
I/O Contract
  -> produces Governance Event
  -> produces Canonical Context
  -> Engine produces Governance Output Envelope
  -> Engine produces Enterprise Writeback
```

The I/O Contract is the integration surface; the other specs define the objects it produces and consumes.

---

## 7. Current status

This is an early minimal specification (aligned with FSP-IO-v0.5-rc1). Field names, adapter list, and schema bindings may change through RFC review.
