# Enterprise Writeback Minimal Specification v0.1

The Enterprise Writeback is the object an enterprise system consumes to decide whether to allow an auto-reply, a commitment, or an auto-execution, and what human review is required.

---

## 1. Purpose

The engine must not execute business actions. Instead it returns an Enterprise Writeback that the enterprise's own system uses to gate replies, commitments, and executions.

This keeps the protocol non-executing while still being actionable inside the enterprise.

---

## 2. Non-goals

The Enterprise Writeback does not:

- execute refunds, penalties, or rulings;
- replace human review;
- prove legal or regulatory compliance;
- require joining a Full Spectrum network.

---

## 3. Minimal fields

| Field | Required | Description |
|---|---:|---|
| `schema_version` | yes | Must be `ew-0.1` |
| `case_status` | yes | e.g. `human_review_required` |
| `allow_auto_reply` | yes | Whether auto-reply is permitted |
| `allow_commitment` | yes | Whether commitment is permitted |
| `allow_auto_execution` | yes | Whether auto-execution is permitted |
| `human_review_required` | yes | Whether human review is required |
| `safety_action` | yes | Recommended safety action |
| `risk_level` | yes | `low` / `medium` / `high` / `critical` |
| `reason_code` | yes | Machine-readable reason |
| `recommended_response` | yes | Suggested reply text |
| `audit_id` | yes | Links back to the audit record |
| `review_role` | recommended | Role that should review |
| `review_queue` | recommended | Queue to route to |

---

## 4. Minimal JSON example

```json
{
  "schema_version": "ew-0.1",
  "case_status": "human_review_required",
  "allow_auto_reply": false,
  "allow_commitment": false,
  "allow_auto_execution": false,
  "human_review_required": true,
  "safety_action": "human_review_required",
  "risk_level": "high",
  "reason_code": "REFUND_COMMITMENT_WITHOUT_AUTHORITY",
  "recommended_response": "当前信息不足，需人工核实退款权限后再处理。",
  "audit_id": "audit_ecom_001",
  "review_role": "customer_service_supervisor",
  "review_queue": "after_sales_review"
}
```

---

## 5. Relationship to other specs

```text
Governance Output Envelope -> embeds Enterprise Writeback
Enterprise system -> applies allow_* gates and routes to human review
```

The Enterprise Writeback is the enterprise-facing leaf of the governance chain.

---

## 6. Current status

This is an early minimal specification (schema `ew-0.1`). Field names and bindings may change through RFC review.
