# FSHI API Contract Mapping

Status: draft  
Last updated: 2026-06-30

This document maps an FSHI-style customer-service inspection API to Full Spectrum protocol objects.

It does not claim to document the production API of any external website. It is a protocol-facing contract draft inspired by the public FSHI/AgentGuard demo materials.

Machine-readable request schema:

- [`fshi-dialogue-inspection.schema.json`](../../schemas/fshi-dialogue-inspection.schema.json)
- [`fshi-dialogue-inspection-response.schema.json`](../../schemas/fshi-dialogue-inspection-response.schema.json)

---

## 1. Public product pattern

The public FSHI demo describes a customer-service quality inspection system that:

- scans AI customer-service conversations;
- detects risk before complaint, compliance penalty, or brand damage occurs;
- supports real-time API testing through JSON input;
- returns FSHI-style scores and risk indicators;
- presents risk dashboards, alert centers, responsibility traces, prediction demos, and ROI calculation.

Protocol extraction:

> The product-facing system inspects dialogue. The protocol-facing layer converts inspection results into `RiskAlert`, `AuditTrace`, and reviewable enterprise action recommendations.

---

## 2. Non-invasive integration principle

FSHI should not require replacing an enterprise's existing customer-service system.

Preferred integration modes:

| Mode | Enterprise provides | FSHI returns | Enterprise executes |
| --- | --- | --- | --- |
| Offline batch | Desensitized dialogue files | Risk report, RiskAlert, AuditTrace | Human review, knowledge-base update, training, workflow correction |
| API inspection | JSON dialogue payload | Structured score, risk items, recommended actions | Human review or configured workflow action |
| Monitoring version | Streaming or near-real-time event fields | RiskAlert, downgrade/circuit-break recommendation, dashboard signal | Enterprise-owned AI or workflow system decides execution |

FSHI can recommend actions. It should not claim that it executed enterprise actions unless execution feedback is explicitly returned by the enterprise system.

---

## 3. Suggested input contract

The minimal inspection request should include:

```json
{
  "request_id": "req_fshi_20260629_0001",
  "tenant_id": "enterprise_mock",
  "inspection_mode": "api",
  "industry_adapter": "logistics",
  "language": "zh-CN",
  "subject_identity": {},
  "dialogue": {
    "dialogue_id": "dlg_mock_0001",
    "messages": []
  },
  "business_context": {},
  "capability_boundary": {},
  "execution_policy": {},
  "privacy": {}
}
```

### Required field groups

| Field group | Purpose | Notes |
| --- | --- | --- |
| `request_id` | Idempotency and traceability | Required for repeatable audit |
| `tenant_id` | Enterprise or test tenant | May be pseudonymous in public examples |
| `inspection_mode` | `offline_batch`, `api`, or `monitoring` | Determines latency and output expectations |
| `industry_adapter` | `general`, `logistics`, `ecommerce`, etc. | Adapter should be optional |
| `subject_identity` | Agent, enterprise, jurisdiction, and optional AIP-style identity anchor | Required only when the inspected subject has identity or responsibility consequences |
| `dialogue` | Desensitized conversation | Minimum viable input |
| `business_context` | Order, ticket, policy, or workflow state | Optional but strongly recommended |
| `capability_boundary` | What the customer-service AI may or may not do | Enables permission-boundary detection |
| `execution_policy` | Enterprise rules for automatic vs manual action | FSHI recommends; enterprise decides |
| `privacy` | Redaction and retention declaration | Required for responsible examples |

---

## 4. Suggested output contract

The minimal inspection response should include:

```json
{
  "request_id": "req_fshi_20260629_0001",
  "inspection_id": "insp_fshi_20260629_0001",
  "status": "completed",
  "overall": {
    "risk_level": "medium",
    "fshi_score": 74,
    "requires_human_review": true
  },
  "risk_items": [],
  "recommended_enterprise_actions": [],
  "protocol_objects": {
    "risk_alerts": [],
    "audit_trace": {}
  }
}
```

### Response mapping

| FSHI output | Full Spectrum object | Notes |
| --- | --- | --- |
| `overall.risk_level` | `AuditTrace.risk_level` | Overall trace severity |
| `risk_items[]` | `RiskAlert[]` | One risk item may become one RiskAlert |
| `recommended_enterprise_actions[]` | `RiskAlert.recommended_action` and `AuditTrace.audit_events[]` | Recommendation, not execution |
| `protocol_objects.risk_alerts[]` | `RiskAlert` | Machine-readable risk object |
| `protocol_objects.audit_trace` | `AuditTrace` | Reviewable responsibility trace |
| `execution_feedback` | `AuditTrace.audit_events[].event_type = execution_recorded` | Only if enterprise returns execution result |

---

## 5. Risk dimensions

FSHI risk dimensions should map to `RiskAlert.risk_dimension`.

| FSHI risk | RiskAlert dimension |
| --- | --- |
| Unauthorized promise | `unauthorized_promise` |
| Permission or capability overreach | `permission_boundary` |
| Business-state conflict | `state_conflict` |
| Multi-turn hidden accumulation | `multi_turn_accumulation` |
| Emotional escalation | `emotional_escalation` |
| Privacy or data exposure | `privacy_or_data` |
| Safety concern | `safety` |
| Responsibility ambiguity | `responsibility_gap` |
| Systemic process issue | `systemic` |

---

## 6. Identity and standards alignment

FSHI inspection can run in a lightweight mode without strong identity binding when the inspected content has no direct external consequence.

For high-consequence or regulated deployments, the inspected AI or workflow should provide an identity anchor:

```json
{
  "subject_identity": {
    "agent_did": "did:fsmp:ai:example",
    "aip_identity_code": "AIP-CN-EXAMPLE-0001",
    "organization_id": "enterprise_legal_identifier",
    "human_responsibility_owner": "enterprise_compliance_owner",
    "jurisdiction": "CN",
    "identity_anchor_status": "verified"
  }
}
```

Protocol rule:

- external tool nodes may be inspected without Full Spectrum certification;
- compatible nodes may declare external ethics profiles and partial alignment;
- certified nodes should bind identity, capability, boundary, responsibility, and audit commitments;
- if local or national standards require an identity code, FSHI DID should anchor to that code instead of replacing it.

---

## 7. Enterprise action boundary

FSHI may output:

- `observe_only`;
- `human_review`;
- `human_handoff`;
- `knowledge_base_update`;
- `create_follow_up_ticket`;
- `downgrade_response`;
- `circuit_break_recommendation`;
- `recovery_workflow_recommendation`.

FSHI should not mark these as executed unless the enterprise system returns explicit execution feedback.

Suggested event distinction:

| Situation | AuditTrace event |
| --- | --- |
| FSHI recommends action | `decision_recorded` or `risk_detected` |
| Enterprise accepts recommendation | `execution_recorded` |
| Enterprise rejects recommendation | `decision_recorded` with rejection metadata |
| Enterprise times out | `review_requested` or `recovery_started` depending on policy |
| Human takes over | `human_handoff` |
| Circuit-break actually triggered | `circuit_break_triggered` |

---

## 8. Adapter principle

FSHI adapters should be plug-in style:

- if industry fields exist, use them;
- if industry fields are missing, fall back to general dialogue inspection;
- do not force all industries into one fixed ontology;
- keep common protocol objects stable even when adapters differ.

Examples:

| Adapter | Optional context fields |
| --- | --- |
| Logistics | order state, tracking state, SLA, delivery promise policy |
| E-commerce | order state, refund state, seller policy, platform policy, product knowledge |
| Finance | product eligibility, risk disclosure, authorization state, compliance rule |
| General | issue type, user emotion, promise boundary, escalation state |

---

## 9. Current examples

Minimal examples:

- [Dialogue inspection request schema](../../schemas/fshi-dialogue-inspection.schema.json)
- [Dialogue inspection response schema](../../schemas/fshi-dialogue-inspection-response.schema.json)
- [API request sample](../../examples/fshi/api-contract/request.sample.json)
- [API response sample](../../examples/fshi/api-contract/response.sample.json)
- [RiskAlert sample](../../examples/fshi/api-contract/risk-alert.sample.json)
- [AuditTrace sample](../../examples/fshi/api-contract/audit-trace.sample.json)

Existing FSHI examples:

- [desensitized dialogue](../../examples/fshi/desensitized-dialogue.example.json)
- [RiskAlert](../../examples/fshi/fshi-risk-alert.example.json)
- [AuditTrace](../../examples/fshi/fshi-audit-trace.example.json)

---

## 10. Boundary statement

This mapping is a protocol draft.

It does not:

- expose real customer data;
- document private production API details;
- claim production accuracy;
- claim legal authority;
- replace enterprise execution systems;
- certify any external system.

It exists to make the path from FSHI inspection to Full Spectrum protocol objects explicit and reviewable.

