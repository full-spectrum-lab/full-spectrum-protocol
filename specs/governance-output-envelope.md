# Governance Output Envelope Minimal Specification v0.1

The Governance Output Envelope is the standard engine output object. It bundles the engine result, risk vector, safety action, enterprise writeback, privacy posture, and conformance summary into one consumable record.

---

## 1. Purpose

After the engine runs on a Canonical Context, downstream systems (enterprise case packs, dashboards, human-review queues) need one structured object instead of scattered scores.

The Governance Output Envelope provides that single object.

---

## 2. Non-goals

The envelope does not:

- make the final business decision (refund / penalty / ruling);
- replace human review;
- certify external systems;
- claim production compliance.

---

## 3. Minimal fields

| Field | Required | Description |
|---|---:|---|
| `schema_version` | yes | Must be `goe-0.1` |
| `engine_result` | yes | Engine identifier and run metadata |
| `risk_vector` | yes | Structured RiskVector output |
| `safety_action` | yes | Recommended safety action (e.g. `human_review_required`) |
| `enterprise_writeback` | yes | Embedded Enterprise Writeback object |
| `privacy` | yes | Privacy posture of the output |
| `conformance` | yes | Schema/conformance check summary |
| `audit_references` | recommended | Links to AuditTrace / report |

---

## 4. Minimal JSON example

```json
{
  "schema_version": "goe-0.1",
  "engine_result": {
    "engine": "full-spectrum-engine",
    "version": "v1.0.0",
    "run_id": "run_ecom_001"
  },
  "risk_vector": {
    "dimensions": ["survival", "coordination", "meaning"],
    "values": [0.72, 0.41, 0.55]
  },
  "safety_action": "human_review_required",
  "enterprise_writeback": {
    "schema_version": "ew-0.1",
    "allow_commitment": false,
    "human_review_required": true,
    "reason_code": "REFUND_COMMITMENT_WITHOUT_AUTHORITY"
  },
  "privacy": { "public_shareable": false },
  "conformance": { "schema_valid": true }
}
```

---

## 5. Relationship to other specs

```text
Canonical Context -> Engine.run() -> Governance Output Envelope -> Enterprise Writeback (embedded)
```

The envelope embeds the Enterprise Writeback so enterprise systems receive one object.

---

## 6. Current status

This is an early minimal specification (schema `goe-0.1`). Field names and bindings may change through RFC review.
