# CASE002: Ecommerce AI Customer-Service Conflict

Status: synthetic public example  
Purpose: demonstrate how Full Spectrum Protocol can describe multi-turn ecommerce customer-service risk without replacing enterprise decision-making.

---

## 1. Boundary

This is a synthetic case. It does not represent real customer data, a real platform, a real merchant, or any production deployment.

The case is designed to test whether protocol objects can describe:

- multi-turn dialogue risk;
- AI over-commitment;
- policy and order-state conflict;
- unclear responsibility path;
- human review needs.

---

## 2. Scenario

A customer asks an ecommerce customer-service AI whether a high-value item can be returned.

The conversation evolves:

1. the customer asks whether the item supports no-reason return;
2. the customer adds that the tag or package has been opened;
3. product-page wording suggests a worry-free return promise;
4. the customer-service AI says the customer can apply for refund and coupon compensation;
5. platform policy says the item requires inspection before refund;
6. merchant policy says opened items may be restricted;
7. the customer becomes upset because the AI appeared to promise a result.

The core issue is not whether the customer should receive a refund. The core issue is whether the AI turned an explanation or comfort statement into an unauthorized business commitment.

---

## 3. Participating subjects

| Subject | Role | Boundary |
|---|---|---|
| Customer | Requests refund or compensation | Provides claim and evidence |
| Customer-service AI | Explains policy and comforts customer | Should not make final refund or compensation commitments without authority |
| Platform policy node | Provides platform after-sales rules | Explains rules; does not decide final dispute alone |
| Merchant policy node | Provides merchant-specific restrictions | Must be reconciled with platform policy |
| Order-state system | Provides payment, delivery, return, coupon state | Provides state; does not make governance judgment |
| Human reviewer | Reviews commitment, policy conflict, and customer impact | Owns final enterprise-side handling |

---

## 4. Governance interpretation

Full Spectrum Protocol does not decide:

- whether to refund;
- whether to compensate;
- whether the merchant or platform is liable.

It records:

- which subject acted;
- what the AI promised or implied;
- which rules conflicted;
- where permission boundary became unclear;
- why human review is recommended.

---

## 5. Governance Event sketch

```json
{
  "event_id": "ge_case002_ecommerce_001",
  "event_type": "ai_action",
  "actor": {
    "type": "ai_agent",
    "id": "synthetic.customer_service_ai"
  },
  "action": {
    "type": "commitment",
    "description": "AI suggested refund and coupon compensation before authority and order-state verification."
  },
  "context": {
    "domain": "ecommerce_customer_service",
    "data_mode": "synthetic",
    "knowledge_sources": [
      "platform_policy",
      "merchant_policy",
      "product_description",
      "order_state",
      "coupon_state",
      "service_script"
    ]
  },
  "declared_boundary": {
    "can_explain_policy": true,
    "can_commit_refund": false,
    "requires_human_review_for_compensation": true
  },
  "review_requirement": "human_review_required"
}
```

---

## 6. RiskAlert sketch

```json
{
  "risk_id": "risk_case002_ecommerce_unauthorized_promise",
  "created_at": "2026-07-07T00:00:00Z",
  "detector_id": "synthetic.fshi_detector",
  "affected_subject_id": "synthetic.customer",
  "risk_dimension": "unauthorized_promise",
  "severity": "high",
  "confidence": 0.76,
  "urgency": "high",
  "summary": "Customer-service AI may have made a refund or coupon compensation commitment before verifying authority, order state, and policy conflict.",
  "recommended_action": "human_handoff",
  "requires_human_review": true,
  "status": "open",
  "privacy_level": "internal"
}
```

---

## 7. AuditTrace sketch

```json
{
  "trace_id": "trace_case002_ecommerce_001",
  "created_at": "2026-07-07T00:00:00Z",
  "subject_id": "synthetic.customer_service_ai",
  "subject_type": "ai_agent",
  "action_type": "customer_service_commitment",
  "action_summary": "AI replied with a refund and coupon-compensation statement before policy and order-state reconciliation.",
  "risk_level": "high",
  "status": "review_requested",
  "responsibility_owner": "synthetic.enterprise_operator",
  "unresolved": true,
  "privacy_level": "internal",
  "audit_events": [
    {
      "event_id": "evt_case002_001",
      "event_type": "action_committed",
      "timestamp": "2026-07-07T00:00:00Z",
      "actor_id": "synthetic.customer_service_ai",
      "summary": "AI produced a refund and compensation statement."
    },
    {
      "event_id": "evt_case002_002",
      "event_type": "risk_detected",
      "timestamp": "2026-07-07T00:00:01Z",
      "actor_id": "synthetic.fshi_detector",
      "summary": "Unauthorized promise and policy conflict risk detected.",
      "related_risk_id": "risk_case002_ecommerce_unauthorized_promise"
    },
    {
      "event_id": "evt_case002_003",
      "event_type": "human_handoff",
      "timestamp": "2026-07-07T00:00:02Z",
      "actor_id": "synthetic.fshi_detector",
      "summary": "Human review recommended before refund or compensation execution.",
      "related_risk_id": "risk_case002_ecommerce_unauthorized_promise"
    }
  ]
}
```

---

## 8. Recommended review path

Recommended path:

```text
pause automatic commitment
  -> verify platform policy, merchant policy, product description, order state, and coupon state
  -> human reviewer decides enterprise-side handling
  -> record correction or recovery action
```

The protocol should not mark refund, compensation, downgrade, or circuit-break as executed unless the enterprise system returns explicit execution feedback.

---

## 9. Why this case matters

Traditional quality inspection may ask:

> Did the AI use a forbidden phrase?

Full Spectrum-style inspection asks:

> Which subject said what, based on which knowledge source, under which authority boundary, and who owns the consequence if the user relies on it?

This makes the case useful for FSHI-style customer-service inspection and for future ecommerce knowledge-source adapters.

